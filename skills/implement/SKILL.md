---
name: implement
description: "Turn one task into a PR ready for human merge: create or reuse its ticket, isolate it, implement, test, review, publish, and handle current feedback."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

1. Resolve the task and linked context. Capture the goal, acceptance criteria, checks, constraints, and PR rules. Reuse its ticket, or create one with this context when none exists. Stop for missing product decisions, secrets, permissions, or unrelated work bundled together.
2. Inspect the repo, remotes, default branch, worktrees, and open branches or PRs for the ticket. Reuse existing work. Otherwise fetch and create a dedicated ticket-numbered branch and worktree from the latest remote default branch. Work only in that worktree.
3. Mark the ticket in progress when supported. Make the smallest complete change. Add or update tests for changed behavior and docs for user-facing changes. If a useful test is impractical, explain why and verify manually.
4. Run focused checks first, then wider checks when shared or user-facing behavior changed. For browser-facing work, use `browser-verify` when available to exercise main and failure flows at desktop and mobile sizes, checking layout, console errors, and failed requests. Fix relevant failures without expanding the task.
5. Have a fresh subagent or reviewer inspect every non-trivial diff. Judge each finding, fix valid in-scope issues, and rerun affected checks. If no reviewer is available, self-review and disclose that in the PR.
6. Check every acceptance criterion and record proof. Unmet required criteria block the PR.
7. Commit only intended changes with a Conventional Commit subject and ticket ID. Push and open one PR ready for review. Include the ticket link, summary, acceptance proof, checks, review status, and anything not verified.
8. Wait a reasonable time for checks and feedback during this run. Fix important in-scope items, re-check, push, and reply with what changed. Stop when the PR is clean, nothing new arrives, or a human decision is needed.
9. Update the ticket with the PR and proof, move it to the closest review state, and report the ticket, base, branch, worktree, PR, checks, review, and blockers. Leave the worktree for later feedback.
10. Leave merging to a human unless the user explicitly asks for merge. With explicit permission, merge only after required checks and review are clean, then update the ticket and remove the worktree.

## Rules

- One task, one ticket, one branch, one worktree, one PR. Use separate workers for several independent tasks.
- Do not create a duplicate delivery path when a branch, worktree, or PR already exists.
- New work starts from the latest remote default branch unless the task explicitly depends on unmerged work.
- Do not open a PR with failing relevant checks or unmet required criteria unless the user asks for an early draft; disclose the gaps.
- Do not hide unchecked work, overwrite user changes, or expand the task for nice-to-have feedback.
- Keep failed work intact and report exactly what blocked it.
- If the task, spec, or plan is wrong, stop and update the source of truth before continuing.
