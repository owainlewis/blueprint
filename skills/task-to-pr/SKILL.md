---
name: task-to-pr
description: "Completes one or more tasks. Creates one tested and reviewed pull request for each task. Use to implement, build, fix, or deliver tasks, tickets, pull requests, or a milestone."
user-invocable: true
argument-hint: "<tasks, tickets, pull requests, or milestone>"
---

# Task to PR

Review the tasks you were given. Decide the order and which tasks can run at the same time. Make a short plan.

Complete each task in two phases. Keep working without waiting for the user while any task can make progress.

Independent tasks may start together. Start a dependent task after every prerequisite has an open pull request, an independent `/review` verdict of `Approve`, and no known blocking finding. Stack dependent work on the prerequisite branch. If several unmerged prerequisites feed one task, stack those prerequisite branches in dependency order before branching the dependent task. Retarget each stacked pull request to the default branch after its prerequisite merges.

## Phase 1: Build the code

1. Create or reuse a branch and worktree for the task. Start independent work from the latest default branch and dependent work from its reviewed prerequisite or stacked base.
2. Write the code.
3. Use `/test` to prove the task works, affected failures are handled, and refactors preserve behavior.
4. Use `/review` with a fresh subagent that did not write the code.
5. Fix valid problems, then repeat `/test` and `/review`.
6. Commit and push the changes.
7. Create or update one pull request on GitHub. Include a short summary and the current proof.
8. Move the ticket to the repository's review state, such as `In Review` or `Review`, when possible.

## Phase 2: Pass the automated checks

1. Use the GitHub CLI to wait for CI and automated code review when the repository uses them.
2. Fix failures caused by your changes and valid review findings.
3. If a fix needs a product or technical decision that the task does not contain, stop that task and report the missing decision.
4. After changing code, repeat `/test` and `/review`.
5. If you changed code, commit and push it. Update the pull request summary and proof when needed.
6. Reply to every automated review finding. Say what you changed or why you made no change. Resolve the thread when it is fully addressed.
7. Wait for the automated checks again.
8. Repeat until all available checks pass and the automated review has no unresolved findings.
9. Update the ticket with final proof and the pull request link when possible. Keep it in the repository's review state while the pull request is open.

If the user asked you to merge the pull requests, merge each one after its automated checks pass, then mark its ticket complete when possible. Otherwise, leave it open.

Continue with every task that can make progress. Stop when every task has a pull request with all available checks passing and no unresolved automated review findings. If no remaining task can move forward, explain what is needed.
