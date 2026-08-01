---
name: task-to-pr
description: "Completes one or more tasks. Creates one tested and reviewed pull request for each task. Use to implement, build, fix, or deliver tasks, tickets, pull requests, or a milestone."
user-invocable: true
argument-hint: "<tasks, tickets, pull requests, or milestone>"
---

# Task to PR

Review the tasks you were given. Decide which order to do them in and make a short plan.

Complete each task in two phases.

## Phase 1: Build the code

1. Create or reuse a branch and worktree for the task. Start new work from the latest default branch.
2. Write the code.
3. Run the tests and relevant quality checks.
4. Ask a subagent to review the code.
5. Fix any problems, then repeat the tests and review.
6. Commit and push the changes.
7. Create or update one pull request on GitHub.
8. Mark the ticket as `In Review` when possible.

## Phase 2: Pass the automated checks

1. Use the GitHub CLI to wait for CI and automated code review when the repository uses them.
2. Fix any failures or review findings.
3. After changing code, repeat the tests, quality checks, and subagent review.
4. Commit and push the changes. Update the pull request summary and proof, then wait for the automated checks again.
5. Repeat until all available checks pass and the automated review has no unresolved findings.

If the user asked you to merge the pull requests, merge each one after its automated checks pass. Otherwise, leave it open.

After the automated checks pass, move to the next task. Continue until every task has a pull request with all available checks passing and no unresolved automated review findings. If you are blocked, explain what is needed.
