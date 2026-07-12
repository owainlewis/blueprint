---
name: pr-to-ready
description: "Make an open pull request ready to merge by checking live feedback, fixing required items, running checks, and reporting the result. Never merge."
user-invocable: true
argument-hint: "<PR URL, number, branch, or current repository PR>"
---

# PR To Ready

1. Identify the PR from `$ARGUMENTS`, the current branch, or open repo PRs.
2. Inspect the live PR: diff, commits, checks, reviews, unresolved threads, comments, mergeability, and local git status.
3. Classify feedback: actionable, disputed, resolved, outdated, informational, needs-human.
4. Fix actionable items, keeping changes small. Push back on disputed items with a comment on the thread explaining why, and do not change the code. Stop for product, security, code-owner, or risk decisions.
5. Run the smallest checks that prove the fix, wider checks when shared or user-facing behavior changed.
6. Re-check the PR after pushing. Reply on each addressed thread with what changed. Update the linked ticket with proof when accessible.
7. Report Ready, Not ready, or Blocked, with changes, checks run, pushed-back items, and remaining items.
8. If asked "merge?", answer directly. Never merge.

## Rules

- Never merge.
- Push back only with a concrete reason: correctness, scope, or a documented convention. Preference disagreements from a human reviewer go to needs-human, not a rebuttal.
- Do not expand the task for nice-to-have feedback.
- Do not mark ready while required checks fail or actionable feedback remains.
- Trust the live PR state, not stale summaries.
- Do not hide skipped tests, placeholders, partial fixes, or assumptions.
