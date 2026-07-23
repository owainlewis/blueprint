---
name: task-to-pr
description: "Takes one task, ticket, or existing pull request to a tested, independently reviewed, green pull request ready for human merge. Use when the user asks to implement, build, fix, deliver, or take one task or issue to a pull request."
user-invocable: true
argument-hint: "<ticket, task, or pull request>"
---

# Task to PR

Follow this workflow for the requested task, ticket, or pull request:

1. **Resolve the source.** Resume an existing pull request and its linked ticket when one exists. Otherwise fetch the ticket or use the task as the source. Create a ticket only when the user asks or durable tracking improves the handoff or proof. Do not duplicate tickets or pull requests.
2. **Isolate the work before editing.** Resume the branch and worktree for an existing pull request. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Follow the repository's location convention and reuse a suitable existing worktree. Remove a manually created worktree after its pull request is merged or closed.
3. **Read the context.** Read the repository instructions and inspect the relevant code.
4. **Outline the change.** Define the smallest complete change and check it against the ticket, task, or pull request. This is a local execution outline for this one task, not a multi-task plan document. Do not create tickets or a plan document.
5. **Implement.** Make the change and add tests where necessary.
6. **Test.** Run any automated checks and tests, including real-browser checks for browser-rendered behavior.
7. **Review.** Review the change with a fresh subagent that did not implement it.
8. **Address findings.** Fix valid review findings, then rerun affected tests and fresh review.
9. **Publish.** Create a Conventional Commit, push the branch, and open or update a ready pull request. Link the ticket when one exists and include test and review evidence.
10. **Finish CI.** Wait for checks to finish. Fix relevant failures and rerun affected tests and review until required checks pass. If no checks are configured, continue.
11. **Handle current feedback.** Inspect the human and bot feedback available at that point. Fix important findings, reply to addressed comments with evidence, and rerun affected tests and fresh review. Do not wait indefinitely for future human feedback.

Commit and push every post-PR fix before reassessing checks or feedback.

If the ticket, task, or design is wrong or incomplete, update the source of truth before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop when the pull request is green, mergeable, and has no important unresolved feedback currently available. Never merge unless the user explicitly asks. Report an exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.
