---
name: task-to-pr
description: "Turn one ticket into a PR ready for review in its own branch and worktree, with code, tests, review, acceptance checks, and proof."
user-invocable: true
argument-hint: "<ticket reference> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

1. Resolve the ticket and linked context. Capture the goal, acceptance criteria, verification, constraints, and PR rules. Stop if the ticket is unclear, spans unrelated work, duplicates existing work, or needs a missing decision, secret, or permission.
2. Inspect the repository, remotes, default branch, current worktrees, and open branches or PRs for the ticket. If work already exists, reuse its branch and worktree, or create a worktree for that branch. Never create a duplicate delivery path.
3. Fetch the remote. For new work, create a ticket-named branch and dedicated worktree from the latest remote default branch. Use another base only when the repo or ticket explicitly requires it. Do all implementation in the dedicated worktree, never the caller's checkout.
4. Mark the ticket in progress when the tracker supports it. Implement the smallest complete change in the worktree. Add or update tests, and update docs when user-facing behavior changes.
5. Run focused checks first, then wider checks when shared or user-facing behavior changed. Fix relevant failures without growing the ticket.
6. Get non-trivial diffs reviewed by a fresh agent or reviewer. Judge each finding, fix valid in-scope issues, and rerun affected checks. If no reviewer is available, self-review and disclose that in the PR.
7. Check every acceptance criterion against the ticket and record its proof. Unmet required criteria block the PR.
8. Commit only intended changes with a Conventional Commit subject and ticket ID. Push and open one PR ready for review. Include the ticket link, summary, acceptance proof, checks, review status, and anything not verified.
9. Handle checks and feedback that arrive during this run. Fix actionable items, re-check, and push. Stop when clean, when nothing arrives after a reasonable wait, or when a human decision is needed.
10. Update the ticket with the PR link and proof, move it to the closest review state, and report the ticket, base, branch, worktree, PR, checks, review, and blockers.

## Rules

- One ticket, one branch, one PR. A list of tickets means one worker per ticket.
- Every ticket runs in a dedicated branch and worktree. New work starts from the latest remote default branch. Keep the original checkout untouched.
- Reuse an existing branch, worktree, or PR for the ticket instead of creating a duplicate.
- Branch from unmerged work only when the ticket explicitly depends on it.
- Never merge. Long-running review watching is a separate run unless asked.
- Do not open a PR with failing relevant checks or unmet required criteria unless the user asks for an early draft, and disclose it.
- Do not expand the task for nice-to-have suggestions from review, checks, or bots.
- Keep the worktree after opening the PR. Remove it only after merge or when the user asks.
- On failure, keep the branch and worktree intact and report exactly what failed.
- Unattended runs report through the ticket, not chat. When blocked: comment proof, apply the needs-human label, release any claim label, exit cleanly.
