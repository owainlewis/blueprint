---
name: multitask
description: "Run several tickets to PRs at the same time, one worker per ticket. Use when the user passes multiple tickets and wants them worked in parallel."
user-invocable: true
argument-hint: "<ticket list> e.g. LIN-101, LIN-102, LIN-103"
---

# Multitask

Goal: run one worker per ticket and report each PR or blocker.

## Workflow

1. Read each ticket and the code it is likely to touch. Tickets that share files, data shapes, or behavior go in one ordered group. Tickets that do not overlap get separate workers.
2. Give each worker its own worktree, branch, and full session when possible. If parallel workers are not available, run the groups one after another and say so.
3. Start each worker with a complete prompt: ticket, repo path, branch rule, acceptance criteria, checks, review rule, PR rules, and report format. The worker must resolve the ticket, implement, test, check each acceptance criterion, get code review, commit, push, open a PR ready for review, handle current feedback, update the ticket, and report proof.
4. Watch the workers. When one fails or changes an assumption another worker needs, stop the affected workers and report why. Report failures instead of silently retrying them.
5. Report every ticket with branch, PR URL, status, stopped work, what blocked it, and proof. Clean up worktrees whose PRs are open.

## Rules

- Cap parallel workers around five.
- Never merge, rebase, or cherry-pick between workers. One ticket, one branch, one PR.
- The coordinator never edits code. Fixes happen inside the worker.
- A failed worker is reported, not quietly merged into another worker's task.
