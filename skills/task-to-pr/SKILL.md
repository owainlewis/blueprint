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

1. Write the code.
2. Run the tests and relevant quality checks.
3. Ask a subagent to review the code.
4. Fix any problems, then repeat the tests and review.
5. Commit and push the changes.
6. Create or update one pull request on GitHub.
7. Mark the ticket as `In Review` when possible.

## Phase 2: Pass the automated checks

1. Use the GitHub CLI to wait for CI and automated code review.
2. Skip CI or automated review if the repository does not use it.
3. Fix any failures or review findings.
4. After changing code, repeat the tests, quality checks, and subagent review.
5. Push the changes and wait for the automated checks again.
6. Repeat until all available checks pass and the automated review has no unresolved findings.

If the user asked you to merge the pull requests, merge each one after its automated checks pass. Otherwise, leave it open for human review. Do not wait for human review.

After the automated checks pass, move to the next task. Continue until every task has a pull request with all available checks passing and no unresolved automated review findings. If you are blocked, explain what is needed.
