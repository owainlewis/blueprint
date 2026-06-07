---
name: codex-run-loop
description: "Use when the user asks Codex to coordinate multiple tickets, run a batch of issues, work tickets in parallel, or create worker threads/worktrees that produce draft PRs."
user-invocable: true
argument-hint: "<task reference, ticket list, issue reference, or parallel task set>"
---

# Codex Run Loop

Coordinate Codex worker threads that turn planned tasks into draft PRs. Use this when the user asks for a coordinator to work through tickets, especially in parallel or with separate worktrees. For one ordinary coding task, code it directly unless the user asks for this loop.

## Workflow

### 1. Select Work

Read the requested tickets, source context, issue tracker context, and repo state. Classify tickets as independent, dependent, conflicting, or unclear. Run independent tickets in parallel, run dependent tickets in waves, sequence conflicting tickets, and stop on unclear acceptance criteria.

For dependent tickets, prefer stacked draft PRs when each ticket remains reviewable on its own. If the tickets are really one feature or heavily overlap, ask whether to use one integration branch and PR.

### 2. Prepare Worktrees

Inspect `git status`, current branch, remotes, and existing worktrees. For each unblocked ticket in the current wave, derive a traceable branch name from the ticket ID and short task summary, then create a separate worktree. Default to a sibling root such as `../<repo-name>-worktrees/<branch-name>`.

Use `git worktree add -b <branch> <path> <base>` for new branches. Reuse an existing worktree only when it is for the same branch and clean.

For stacked PRs, base each dependent branch on its predecessor branch. For an integration PR, run the dependent tickets sequentially in one integration worktree.

### 3. Start Workers

Create one Codex worker thread per ticket when thread tools are available. For an integration PR, start one worker at a time in the integration worktree. Send each worker a compact packet:

```text
Ticket:
Source context:
Worktree:
Branch:
Base:
Acceptance criteria:
Verification:
PR target:
Pause after:
```

If thread tools are unavailable, stop unless the user explicitly allows sequential local execution.

### 4. Execute Each Ticket

In each worker thread, make the smallest complete code change for the ticket. Use test-first work when the user asked for it. The worker owns code changes, tests, and verification for exactly one ticket.

### 5. Review And Fix

Have each worker request a code-review subagent when available. Fix valid findings that are in scope, rerun the relevant checks, and stop on findings that require a human decision or source-context change.

### 6. Publish Draft PRs

Have each worker stage only intended files, create one clear commit, push its branch, and open a draft PR with available GitHub tools or `gh`. The PR body should include the ticket or source link, acceptance criteria, verification run, review result, and anything not verified. If push or PR creation fails, keep the branch local and report the exact missing remote, auth, command, or tool capability.

### 7. Pause

The run is complete when each selected ticket is blocked or has a draft PR. Stop there. Do not merge, resolve GitHub review, fix CI, or start follow-up changes unless explicitly asked.

### 8. Report

Report each ticket's worker thread, worktree path, branch, commit, draft PR URL, verification, review findings fixed, and any blocked tickets.

## Rules

- The coordinator routes work; workers code one ticket each.
- Use one worktree and branch per ticket, unless the user chose one integration branch.
- Parallelize only tickets that can be reviewed, merged, and reverted independently.
- Do not overwrite, discard, or stage unrelated uncommitted work.
- Do not invent issue tracker tickets or rewrite source context.
- Skip or stop dependent tickets when an earlier ticket fails or changes the source context.
- Judge review findings; do not blindly implement every comment.
- Open draft PRs only after verification ran, or clearly report what could not be verified.
- Pause at draft PRs; merging is out of scope.
