---
name: pr-to-ready
description: "Make an open pull request ready to merge by checking live feedback, fixing required items, running checks, and reporting the result. Never merge."
user-invocable: true
argument-hint: "<PR URL, number, branch, or current repository PR>"
---

# PR To Ready

Goal: make the PR ready to merge, or explain what blocks it.

## Workflow

1. Identify the PR from `$ARGUMENTS`, the current branch, or open repo PRs.
2. Inspect the current PR: title, body, branches, changed files, commits, checks, reviews, unresolved threads, comments, whether GitHub says it can merge, and local git status.
3. Classify feedback as `actionable`, `resolved`, `outdated`, `informational`, or `needs-human`.
4. Fix only actionable items. Keep changes small. Stop for product, security, code-owner, or risk decisions.
5. Run the smallest checks that prove the fix, then wider checks when shared behavior, public functions, commands, config, routes, security, or user-facing flows changed.
6. Re-check the current PR after local fixes or push.
7. Update the linked ticket with proof when accessible.
8. Report `Ready`, `Not ready`, or `Blocked` with PR, current state checked, changes, checks run, and remaining items.
9. When the user asks "merge?", answer directly: "Ready to merge", "Not yet", or "I can't validate merge readiness". Do not merge.

## Loop Mode

For scheduled or repeated review loops, run one round of fixes per tick, wait briefly after pushes so review tools can respond, and exit cleanly when checks or bots are still pending.

## Rules

- Do not merge.
- Do not expand the task for nice-to-have feedback.
- Do not mark ready while required checks fail or actionable feedback remains.
- Do not rely on stale chat summaries.
- Do not hide skipped tests, placeholders, partial fixes, or assumptions.
