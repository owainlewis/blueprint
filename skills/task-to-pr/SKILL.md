---
name: task-to-pr
description: "Takes one task, ticket, or existing pull request to a tested, independently reviewed, green pull request ready for human merge. Use when the user asks to implement, build, fix, deliver, or take one task or issue to a pull request."
user-invocable: true
argument-hint: "<ticket, task, or pull request>"
---

# Task to PR

Follow this workflow for the requested task, ticket, or pull request:

1. **Resolve the source.** Resume an existing pull request and its linked ticket when one exists. Otherwise fetch the ticket or use the task as the source. Create a ticket only when the user asks or durable tracking improves the handoff or proof. Do not duplicate tickets or pull requests.
2. **Branch.** Resume the branch and worktree for an existing pull request. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Follow the repository's location convention and reuse a suitable existing worktree. Remove a manually created worktree after its pull request is merged or closed.
3. **Read the context.** Read the repository instructions and inspect the relevant code.
4. **Outline the change.** Define the smallest complete change and check it against the ticket, task, or pull request. This is a local execution outline for this one task, not a multi-task plan document. Do not create tickets or a plan document.
5. **Implement.** Make the change and add tests where necessary.
6. **Test.** Run any automated checks and tests, including real-browser checks for browser-rendered behavior.
7. **Review.** Review the change with a fresh subagent that did not implement it.
8. **Address findings.** Fix valid review findings, then rerun affected tests and fresh review.
9. **Publish.** Create a Conventional Commit, push the branch, and open or update a ready pull request that meets the pull request standard below.
10. **Pass CI.** Wait for checks, fix relevant failures, and rerun affected tests and review until required checks pass. If no checks are configured, continue.
11. **Address feedback.** Inspect current human and bot feedback. Fix important findings, reply to addressed comments with evidence, and rerun affected tests and fresh review. Do not wait indefinitely for future human feedback.

Commit and push every post-PR fix before reassessing checks or feedback.

If the ticket, task, or design is wrong or incomplete, update the source of truth before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop when the pull request is green, mergeable, and has no important unresolved feedback currently available. Never merge unless the user explicitly asks. Report an exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.

## Pull request standard

Treat the pull request title and body as durable history for reviewers now and engineers later. Follow a required repository template when one exists. Otherwise use the structure below.

- Follow the repository's title convention. Otherwise use a short, standalone title that states the delivered outcome.
- Link the source ticket with the repository's closing syntax when the pull request completes it.
- Include enough context to understand the change without opening the ticket or reading the entire diff.
- Answer the reviewer questions with concrete behavior, decisions, risks, shortcomings, and evidence. Do not write an inventory of edited files.
- For a complex change, say where to start and which parts need the closest scrutiny.
- Answer every checklist item with an explicit status and evidence. Use `Not applicable`, `Not configured`, or `Pending` instead of a checked box that implies success.
- Treat independent agent review as evidence, not GitHub approval or a replacement for human review.
- Preserve useful human-written context when updating an existing pull request.
- Keep the body current when later commits change behavior, risk, or verification.

```markdown
Closes #<ticket>

## What is this change?

Summarize the major changes and observable behavior so a reader understands
what changed without reading the entire diff.

## Why is it important?

Explain the problem, who it affects, the context behind the change, and why
this approach was chosen.

## What should the reviewer know or consider?

Call out decisions not obvious from the code, scope boundaries, tradeoffs,
shortcomings, safety rules, compatibility, migrations, failure behavior,
operational impact, and known risks. Link relevant designs, benchmarks, or
related changes while preserving the essential context here. For a complex
change, tell the reviewer where to start and what needs the closest scrutiny.

## Checklist

- **Is this one focused, self-contained change?** <Yes | No>
  Evidence or why the size and scope are necessary.
- **Did you write or update tests?** <Yes | No | Not applicable>
  Evidence or why tests do not apply.
- **Did you run the relevant tests and checks?** <Yes | No>
  Commands, browser or manual checks, results, and important gaps.
- **Did you independently review the final diff and address valid findings?** <Yes | No>
  Review evidence, findings fixed, and anything unresolved.
- **Did you update documentation when behavior changed?** <Yes | No | Not applicable>
  Documentation changed or why it was not needed.
- **Did required CI checks pass?** <Yes | No | Pending | Not configured>
  Result or relevant details.
```
