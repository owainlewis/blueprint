---
name: task-to-pr
description: "Delivers a spec, issue, or decided task as a pull request that passes its checks, CI, and an independent review. Leaves the PR open unless merging was explicitly authorized."
user-invocable: true
argument-hint: "<specs, tasks, issues, PRs, or milestone>"
disable-model-invocation: true
---

# Task to PR

Deliver each task as one focused pull request that passes CI and an independent review. The spec, issue, or task is the ticket; do not write another one.

When a step names [test](../test/SKILL.md), [review](../review/SKILL.md), [spec](../spec/SKILL.md), or [plan](../plan/SKILL.md), read that file and follow it.

## Steps

1. Read the ticket, the repository instructions, and the code it touches. If a decision that changes behavior is missing, ask the user or return to spec. Split large work with plan.
2. Branch from the latest default branch, or continue the existing branch and PR.
3. Build the change with tests. Update `REQUIREMENTS.md`, `ARCHITECTURE.md`, or the spec if the change makes them wrong.
4. Follow test until every check passes.
5. Commit with a Conventional Commit message, push, and open the PR. Use the repository's PR template, or What, Why, What changed, Verification, and Risk if it has none.
6. Follow review. Wait for CI and any review bot on the latest commit.
7. Fix each real finding and failure, and reply on each review thread with the fix or the reason for no change. Go back to step 4. After three rounds on the same problem, stop and report it.
8. Link the PR and its proof in the ticket.

## Dependent tasks

Start a task that depends on another once that task has an open PR with an `Approve` review. Branch from it, and update your branch when it changes or merges.

## Merge

Leave the PR open. Merge only when the user asks (for example "/task-to-pr and merge it") or `/codex-issue-coordinator` was invoked by name, and only when:

- CI passes on the latest commit.
- The latest review verdict is `Approve` and no finding is open.
- Every approval the repository requires is given.
- The PR is up to date with its base.

Never bypass branch protection. After merging, update the ticket and delete any worktree you created. Merging never includes deploying or releasing.

## Return

Each PR link with its check results, review verdict, CI state, and anything blocked.
