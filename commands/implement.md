---
name: implement
description: "Take one task or ticket to a tested, independently reviewed, green pull request ready for human merge."
argument-hint: "<ticket, task, or PR>"
---

# Workflow: Code changes

Follow this workflow for `$ARGUMENTS`:

1. Resolve `$ARGUMENTS`. If it is an existing PR, resume that PR and its linked ticket when one exists; do not create a new ticket. Otherwise fetch the ticket, or create one from the task before coding when `gh` is available.
2. Read the repository instructions and inspect the relevant code.
3. Create a plan and verify it against the ticket, task, or PR.
4. Implement the changes and add tests where necessary.
5. Run the `test` phase, including real-browser checks for browser-rendered behavior.
6. Run the `review` phase with a fresh subagent to review the diff independently.
7. Address valid review findings, then rerun affected tests and fresh review.
8. Create a Conventional Commit, push the branch, and open or update a ready pull request. Link the ticket when one exists and include test and review evidence.
9. Wait for CI checks and current review feedback.
10. Fix important CI or review feedback, reply to addressed comments with evidence, then repeat affected tests and fresh review until the PR is green and has no important unresolved feedback.

Resume the branch and worktree for an existing PR. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Do not duplicate tickets or PRs. If the ticket is wrong or incomplete, update it before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop at a green pull request ready for human merge. Never merge unless the user explicitly asks. Report an exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.
