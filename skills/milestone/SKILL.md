---
name: milestone
description: "Complete all open GitHub issues in a milestone by running task-to-pr one issue at a time."
user-invocable: true
argument-hint: "<GitHub milestone URL>"
---

# Milestone

Goal: finish every open issue in a GitHub milestone.

## Workflow

1. Inspect the milestone, repo, open issues, open PRs, and project state when accessible.
2. Order issues by dependency, risk, and reviewability. Put blockers, bugs, and shared seams before dependent feature work.
3. Work one issue at a time by running `task-to-pr`. Do not reimplement its inner loop.
4. After each PR is ready, stop for human merge unless the user explicitly allowed merging for this run.
5. If merging is allowed, merge only after local checks, CI, and review are clean. Then sync the default branch before starting the next issue.
6. Keep the issue and project state updated with PR links, proof, blockers, and final status.
7. Report the milestone result: completed issues, merged PRs, open PRs, blockers, checks, and anything not verified.

## Rules

- One issue, one branch, one PR unless combining is clearly required. Explain any combination before doing it.
- Do not start issues outside the milestone.
- Do not batch unrelated issues.
- Do not merge without explicit permission from the user.
- Do not merge with failing checks, unresolved required review, missing acceptance criteria, or unexplained test gaps.
- Stop if an issue is unclear, already has a matching PR, needs missing secrets or permissions, repeats the same blocker, or grows beyond its acceptance criteria.
