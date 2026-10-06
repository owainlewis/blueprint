---
name: task-to-pr
description: "Delivers specs or decided tasks as tested, independently reviewed pull requests. Runs the CI and review repair loop, then leaves passing pull requests open unless merging was explicitly authorized."
user-invocable: true
argument-hint: "<specs, tasks, issues, PRs, or milestone>"
---

# Task to PR

Deliver each task as one focused pull request with proof. The spec is the ticket;
accept a Markdown spec, GitHub issue, or decided task with acceptance checks.
Do not create a second work definition.

## Prepare

1. Read the source, repository instructions, relevant requirements and architecture, code, and tests. Reuse an existing branch, worktree, and pull request when continuing work.
2. Confirm the outcome, scope, decisions, and checks are sufficient. If a consequential choice is missing, return to `/spec` or report the needed decision before implementing. Do not write specs for small, decided work.
3. Split larger specs with `/plan` when useful. Each task delivers one working result. Identify dependencies and start independent work together when useful.

## Deliver and repair

1. Create or reuse an isolated branch and worktree. Start independent work from the latest remote default branch. Follow repository naming and worktree rules.
2. Implement the task and meaningful tests for changed behavior and affected failures. Update requirements, architecture, and the spec when the change affects them. Keep intended architecture and implementation status accurate.
3. Use `/test` to prove acceptance and affected rules. Fix failures before committing.
4. Create a Conventional Commit, push, and open or update the pull request. Follow the repository PR template. Lead with the problem and result; include proof and the source link. Mark it ready for review and move a tracker ticket to Review when supported.
5. Use `/review` with a fresh subagent that did not implement the change. Wait for configured CI and automated review on the current commit.
6. Fix valid findings and failures caused by the change. Reply to review findings with the fix or evidence for making no change. Resolve a thread only when fully addressed.
7. After changing the implementation, repeat affected `/test` checks and fresh `/review`, commit, push, and wait for CI and automated review again. Update PR proof. Continue until all available checks pass and no actionable finding remains.
8. Report a blocker when progress requires a missing decision, permission, unavailable check, or external repair. Do not weaken tests, bypass repository rules, or claim unrun checks passed.
9. Record final proof and the PR link in the source spec or task. Update delivery status to reflect the actual result, including whether the PR is open or merged. Update the original tracker item when one exists. Leave passing PRs open for human review by default. Pending human approval is a merge blocker, not a failed implementation check.

## Dependencies

Start dependent work only after each prerequisite has an open PR, a fresh
`Approve` review, and no known blocking finding. Stack its branch on the reviewed
prerequisite. If there are several prerequisites, combine them in dependency
order. Keep each PR diff focused on its own task.

When a prerequisite changes or merges, update dependent branches and PR bases.
Repeat affected tests, independent review, and CI against the new base.

## Merge only with authority

Explicit `/factory` or `/codex-issue-coordinator` use grants their scoped merge
authority. Otherwise merge only when the user asks. Automatic skill selection
does not grant it. Before merging, require:

- Complete scope and acceptance proof on the final commit.
- Passing tests, required CI, and a fresh `/review` verdict of `Approve`.
- No unresolved actionable review finding or consequential decision.
- Every repository-required approval.
- A ready, mergeable PR current with its required base.

Merge in dependency order using the repository's preferred method. Never bypass
branch protection. Confirm GitHub reports the merge, then update delivery status in the source
spec or task and update the original issue and project state. Remove manually created worktrees after merge or close;
use the host's lifecycle tools for managed worktrees. Keep open-PR worktrees.
Merge authority does not authorize deployment or release publication.

## Return

Report each PR, tests, review verdict, CI state, and blocker. Stop with passing
PRs open unless scoped merge authority was given. In merge mode, report verified
merges and any work that still needs human action.
