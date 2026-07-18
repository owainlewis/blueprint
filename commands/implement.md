---
description: "Takes one task, ticket, or existing PR to a tested, independently reviewed, green pull request ready for human merge."
argument-hint: "<ticket, task, or PR>"
---

# Workflow: Code changes

Follow this workflow for `$ARGUMENTS`:

1. Resolve `$ARGUMENTS`. Resume an existing PR and its linked ticket when one exists. Otherwise fetch the ticket or use the task as the source. Create a ticket only when the user asks or durable tracking improves the handoff or proof. Do not duplicate tickets or PRs.
2. Set up isolated work before editing. Resume the branch and worktree for an existing PR. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Follow the repository's location convention and reuse a suitable existing worktree. Remove a manually created worktree after its PR is merged or closed.
3. Read the repository instructions and inspect the relevant code.
4. Outline the smallest complete change and check it against the ticket, task, or PR. This is a local execution outline, not the `plan` phase. Do not create tickets or a plan document.
5. Implement the changes and add tests where necessary.
6. Run the `test` phase, including real-browser checks for browser-rendered behavior.
7. Run the `review` phase with a fresh subagent to review the diff independently.
8. Address valid review findings, then rerun affected tests and fresh review.
9. Create a Conventional Commit, push the branch, and open or update a ready pull request. Link the ticket when one exists and include test and review evidence.
10. Wait for CI checks to finish. Fix relevant failures and rerun affected tests and review until required checks pass. If no checks are configured, continue.
11. Inspect the human and bot feedback available at that point. Fix important findings, reply to addressed comments with evidence, and rerun affected tests and fresh review. Do not wait indefinitely for future human feedback.

Commit and push every post-PR fix before reassessing checks or feedback.

If the ticket, task, or design is wrong or incomplete, update the source of truth before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop when the pull request is green, mergeable, and has no important unresolved feedback currently available. Never merge unless the user explicitly asks. Report an exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.
