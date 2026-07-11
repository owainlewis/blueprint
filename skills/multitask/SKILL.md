---
name: multitask
description: "Run several tickets to PRs at the same time, one worker per ticket. Use when the user passes multiple tickets and wants them worked in parallel."
user-invocable: true
argument-hint: "<ticket list> e.g. LIN-101, LIN-102, LIN-103"
---

# Multitask

1. Read each ticket and the code it likely touches. Tickets that overlap in files, data shapes, or behavior go in one ordered group; the rest get separate workers.
2. Give each worker its own worktree, branch, and full session. If parallel workers are not available, run groups sequentially and say so.
3. Start each worker with a complete prompt: ticket, repo path, branch rule, acceptance criteria, checks, review rule, PR rules, report format. The worker owns the full loop from implement through PR, ticket update, and proof.
4. Watch the workers. If one fails or invalidates an assumption another needs, stop the affected workers and report why. Report failures, never silently retry.
5. Report every ticket: branch, PR URL, status, blockers, proof, and any worktree path. Clean up worktrees only when the repo convention says to or the user asks.

## Rules

- A worker is a Codex thread or a Claude Code subagent, one per ticket, each in its own worktree.
- Worker reports are short: branch, PR URL, status, proof. Nothing else returns to the coordinator.
- Cap parallel workers around five.
- One ticket, one branch, one PR. Never merge, rebase, or cherry-pick between workers.
- The coordinator never edits code. Fixes happen inside the worker.
- A failed worker is reported, not folded into another worker's task.
