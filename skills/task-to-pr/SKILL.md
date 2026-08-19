---
name: task-to-pr
description: "Completes one or more tasks. Creates one tested and reviewed pull request for each task. Use to implement, build, fix, or deliver tasks, tickets, pull requests, or a milestone."
user-invocable: true
argument-hint: "<tasks, tickets, pull requests, or milestone>"
---

# Task to PR

Take each task from a decided outcome to a tested and reviewed pull request. Keep one task, branch, and pull request focused on one result.

Review the tasks first. Decide their order, note dependencies, and identify work that can run at the same time. Then make a short plan.

## Order dependent work

- Start independent tasks together when useful.
- Start a dependent task only after each prerequisite has an open pull request, an independent `/review` verdict of `Approve`, and no known blocking finding.
- Stack dependent work on the prerequisite branch. If a task has several unmerged prerequisites, stack those branches in dependency order before creating the dependent branch.
- When a prerequisite branch or pull request base changes, update every dependent branch to that reviewed state. Repeat `/test` and `/review`.
- After a prerequisite merges, retarget its stacked pull requests to the default branch. Repeat the proof against that base.

## Phase 1: build the code

1. Create or reuse a branch and worktree for the task. Start independent work from the latest default branch and dependent work from its reviewed prerequisite or stacked base.
2. Write the code.
3. Use `/test` to prove the task works, affected failures are handled, and refactors preserve behavior.
4. Commit and push the changes.
5. Create or update one pull request on GitHub. Include a short summary and the current proof, then mark it ready for review.
6. Move the ticket to the repository's review state, such as `In Review` or `Review`, when possible.
7. Use `/review` with a fresh subagent that did not write the code.
8. Fix valid problems, then repeat `/test` and `/review`. Commit and push every reviewed fix before continuing.

## Phase 2: pass the automated checks

1. Use the GitHub CLI to wait for CI and automated code review when the repository uses them.
2. Fix failures caused by your changes and valid review findings.
3. If a fix needs a product or technical decision that the task does not contain, stop that task and report the missing decision.
4. After changing code, repeat `/test` and `/review`.
5. If you changed code, commit and push it. Update the pull request summary and proof when needed.
6. Reply to every automated review finding. Say what you changed or why you made no change. Resolve the thread when it is fully addressed.
7. Wait for the automated checks again.
8. Repeat until all available checks pass and the automated review has no unresolved findings.
9. Update the ticket with final proof and the pull request link when possible. Keep it in the repository's review state while the pull request is open.

## Merge only when asked

If the user asks for merges, merge pull requests in dependency order. Before each merge, confirm that:

- automated checks pass;
- the final `/review` verdict is `Approve`;
- required approvals are present; and
- no review thread remains unresolved.

Explicitly naming `/codex-issue-coordinator` grants merge authority only for that coordinator's issue batch. Automatic skill selection does not grant merge authority.

After a prerequisite merges, retarget its dependents to the default branch and update them to that base. Repeat `/test`, `/review`, CI, and automated review before merging. Never bypass repository rules. Wait until GitHub reports the pull request as merged before marking its ticket complete when possible. If the user did not ask for merges, leave the pull request open.

## Return

Continue with every task that can make progress. For each task, report the pull request, tests, review verdict, CI state, and any blocker.

Without merge authority, stop when every task has a pull request with all
available checks passing, a final `/review` verdict of `Approve`, and no
unresolved automated review finding. Record required human approval or merge as
the task blocker. With merge authority, stop when every in-scope pull request is
merged and its ticket is complete when possible. If no task can move forward,
state what is needed.
