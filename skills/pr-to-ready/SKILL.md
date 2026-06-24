---
name: pr-to-ready
description: "Takes an open pull request with feedback to merge-ready by inspecting live PR state, classifying feedback, fixing only still-actionable findings, verifying checks, and reporting merge readiness. Never merges. Use when the user asks 'fix the PR', 'address review comments', 'merge?', 'is this ready?', or wants PR feedback resolved."
user-invocable: true
argument-hint: "<PR URL, number, branch, or current repository PR>"
---

# PR To Ready

Drive an open pull request to merge-ready. Re-read live PR state and decide from evidence. Never merge.

## Workflow

1. Identify the PR from `$ARGUMENTS`, the current branch, or the repository's open PRs.
2. Inspect live state:
   - PR title, body, base/head branches, mergeability, changed files, and latest commits
   - check runs, required statuses, and failing or pending jobs
   - review submissions, unresolved threads, top-level comments, and bot comments
   - local working tree status
3. Classify feedback before editing:
   - `actionable`: still applies and should be fixed
   - `resolved`: already fixed or answered
   - `outdated`: attached to old code or obsolete context
   - `informational`: useful but not required for merge
   - `needs-human`: requires product, security, ownership, or risk acceptance
4. Patch only actionable findings. Keep changes narrow and consistent with the repo.
5. Run the smallest verification that proves the fixes, then broader tests when shared behavior, public APIs, security, or user-visible flows changed.
6. Re-check live PR state after pushing or after local fixes if not pushing.
7. Sync the linked ticket when the PR references one and the tracker is accessible: keep the existing review state, and comment the readiness verdict with fixes made, passing checks, and verification run. Use existing states only.
8. Report merge readiness with evidence.

## Review-Watch Loop

When this skill is run by a scheduled loop, persistent goal, or coordinator watching a PR:

1. Treat human reviews, bot review comments, unresolved review threads, top-level comments, and failing required checks as possible feedback.
2. After opening a PR or pushing fixes, allow a short grace window for review systems to respond. Ten minutes is a good default unless the repo says otherwise.
3. In a scheduled tick, exit cleanly instead of waiting when the latest agent push is still inside the grace window and checks or review bots are pending.
4. Run one bounded repair pass per tick: classify current feedback, fix actionable items, verify, push when appropriate, and record evidence.
5. Continue on later ticks until the PR is ready, merged, closed, blocked on a human decision, or repeating the same failure with no new information.
6. For an in-session goal, cap repair cycles before stopping. Three cycles is the default unless the user set a different budget.

## Rules

- Never merge the PR.
- Do not spin forever waiting for comments. A scheduler, goal, or coordinator owns wakeups and budget.
- Do not rely on stale chat summaries. Inspect the PR again.
- Do not treat a resolved or outdated bot comment as current work.
- Do not mark a PR ready while required checks are failing or pending.
- Do not broaden scope because a bot suggested a nice-to-have refactor.
- Do not hide placeholders, skipped tests, partial fixes, or assumptions.
- Stop for human input if a finding requires authority the agent does not have.
- Update linked tickets only through existing tracker states and comments.
- If you cannot access the PR host, say so and fall back to local branch, diff, and test evidence only.

## Report

Lead with the decision:

- `Ready`: all actionable feedback is resolved and required checks pass.
- `Not ready`: blockers remain.
- `Blocked`: missing access, missing environment, or human decision required.

Then include:

- PR inspected: number or URL
- Live state checked: reviews, threads/comments, checks, mergeability, working tree
- Changes made: concise bullets with files or areas
- Verification: commands run and results
- Remaining items: blockers, pending checks, human decisions, or risks

## Merge answer

When the user asks "merge?", answer directly, but do not merge:

- "Ready to merge" only when live evidence supports it.
- "Not yet" when checks are pending/failing, actionable feedback remains, or the fix is only partially verified.
- "I can't validate merge readiness" when PR state or required environment is unavailable.
