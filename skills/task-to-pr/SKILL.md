---
name: task-to-pr
description: "Completes one or more tasks. Creates one tested and reviewed pull request for each task. Use to implement, build, fix, or deliver tasks, tickets, pull requests, or a milestone."
user-invocable: true
argument-hint: "<tasks, tickets, pull requests, or milestone>"
---

# Task to PR

Review the tasks you were given. Decide the order and which tasks can run at the same time. Make a short plan.

Complete each task in two phases. Keep working without waiting for the user while any task can make progress.

Do not start a task until the tasks it depends on are merged.

## Phase 1: Build the code

1. Create or reuse a branch and worktree for the task. Start new work from the latest default branch.
2. Write the code.
3. Run tests that prove the task works, affected failures are handled, and refactors preserve behavior. Run relevant quality checks. If tests cannot cover something, give other proof.
4. Ask a fresh subagent that did not write the code to review it without editing.
5. Fix valid problems, then repeat the tests, quality checks, and review.
6. Commit and push the changes.
7. Create or update one pull request on GitHub. Include a short summary and the current proof.
8. Mark the ticket as `In Review` when possible.

## Phase 2: Pass the automated checks

1. Use the GitHub CLI to wait for CI and automated code review when the repository uses them.
2. Fix failures caused by your changes and valid review findings.
3. After changing code, repeat the tests, quality checks, and subagent review.
4. If you changed code, commit and push it. Update the pull request summary and proof when needed.
5. Reply to every automated review finding. Say what you changed or why you made no change. Resolve the thread when it is fully addressed.
6. Wait for the automated checks again.
7. Repeat until all available checks pass and the automated review has no unresolved findings.

If the user asked you to merge the pull requests, merge each one after its automated checks pass. Otherwise, leave it open.

Continue with every task that can make progress. Stop when every task has a pull request with all available checks passing and no unresolved automated review findings. If no remaining task can move forward, explain what is needed.
