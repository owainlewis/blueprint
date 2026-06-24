---
name: multitask
description: "Run several tickets to draft PRs at the same time, one isolated worker per ticket. Use when the user passes multiple tickets and wants them worked in parallel. Composes task-to-pr per ticket; never writes code itself."
user-invocable: true
argument-hint: "<ticket list> e.g. LIN-101, LIN-102, LIN-103"
---

# Multitask

Turn a ticket list into draft PRs in parallel. Partition the work, run one worker per lane, report the fleet. Do not edit code directly.

## Workflow

1. **Classify independence first.** Read each ticket and touched code. Tickets sharing files, schema, or behavioral assumptions go in one sequential lane. Independent tickets get separate lanes. If most overlap, run sequentially and report why.
2. **Isolate each lane**: its own worktree, its own branch, one full-session worker. Use the harness's mechanism for parallel workers (subagents, worker threads); when none exists, run the lanes one after another and say so.
3. **Each worker runs `task-to-pr`** for its ticket, end to end.
4. **Monitor.** When a lane fails or its outcome changes shared assumptions, stop the lanes that depend on it and report; don't let workers build on a broken premise. Report failures, don't silently retry them.
5. **Report the fleet**: every ticket with its branch, PR URL, and status, including stopped and blocked lanes. Clean up worktrees whose PRs are open.

## Rules

- Cap parallel lanes around five.
- Never merge, rebase, or cherry-pick between lanes. One ticket, one branch, one PR.
- The coordinator never edits code. Fixes happen inside the lane's worker.
- A failed lane is reported, not quietly absorbed into another lane.
