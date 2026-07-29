---
name: task-to-pr
description: "Takes one task from its source to a tested and independently reviewed pull request. Use to implement, build, fix, or deliver one task, ticket, or existing pull request."
user-invocable: true
argument-hint: "<ticket, task, or pull request>"
---

# Task to PR

Take one task to a pull request that is ready for human merge.

## Workflow

1. **Code**
   - Read the task, repository instructions, and relevant code.
   - For an existing pull request, use its branch in a worktree. Otherwise fetch the remote and create both from the latest default branch.
   - Define one focused outcome and its proof. If the task is wrong, unclear, or too large, update it or return to design or planning.
   - Implement the smallest complete change. Update the architecture document when system boundaries or contracts change.

2. **Review**
   - Inspect the complete diff for mistakes, unrelated changes, unclear code, and missing proof.
   - Fix problems before testing.

3. **Test**
   - Prove the acceptance criteria, changed behavior, affected failure paths, and behavior a refactor must preserve.
   - Run focused automated checks. Run wider checks when shared behavior changed.
   - Use a real browser when browser-rendered behavior changed.
   - If automated tests cannot cover something, explain why and give other evidence.
   - Give the task, repository instructions, complete diff, and final evidence to a fresh subagent.
   - Fix valid findings. After any code change, repeat Test and this final Review until approved.

4. **Open the PR**
   - Create a Conventional Commit, push the branch, and open or update a ready pull request.
   - Use the repository template. If none exists, use `Plain English summary`, `Reviewer notes`, and `Proof`.
   - Link the source task. Explain the change without requiring the ticket or diff. Do not list files.
   - Keep the summary to two to four short sentences. Give the status and evidence for tests, checks, review findings, documentation, CI, and anything unverified.

5. **Pass checks**
   - Wait for configured CI and automated review of the latest commit. Request a new automated review after a push when needed.
   - Continue when CI or automated review is not configured.
   - Fix CI failures caused by the change and valid automated feedback.
   - After a code change, repeat Review and Test. Commit, push, and start Pass checks again.
   - When automated checks pass, inspect human comments once. Address those present, but do not wait for future comments.
   - If a human comment changes the code, repeat Review and Test, commit, push, and start Pass checks again.
   - Update the pull request with the final check state, feedback outcome, and proof.
   - Stop when the pull request is mergeable, required CI passes or is not configured, automated review covers the latest commit or is not configured, every current comment is handled, and no required change remains.

Never merge unless the user explicitly asks.
