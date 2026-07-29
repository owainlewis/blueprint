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
4. **Outline the change.** Define one focused, self-contained outcome with its related proof. A reviewer must be able to understand its behavior and proof without first separating unrelated work. If the source requires several such changes, split it or return to planning before coding. Separate refactoring when it would obscure the behavior diff. Small local cleanup may remain when it makes the changed behavior easier to review. This is a local execution outline, not a plan document.
5. **Implement.** Make the change. Test changed behavior, failure paths affected by the change or named in its acceptance criteria, and behavior a refactor must preserve. If implementation changes documented ownership, dependency direction, protocols, durable data, trust boundaries, deployment topology, or hard limits, update the existing architecture reference in the same change. If the change has no executable behavior, or the affected behavior cannot be exercised through available automated interfaces, record the concrete reason and substitute evidence.
6. **Test and self-review.** Run tests and checks that cover the changed behavior and affected interfaces, including a real browser when browser-rendered behavior changes. Inspect the final diff for accidental scope, unclear code, and missing proof before independent review.
7. **Review.** Review the change with a fresh subagent that did not implement it.
8. **Address findings.** Fix valid review findings, then rerun affected tests and fresh review.
9. **Publish.** Create a Conventional Commit, push the branch, and open or update a ready pull request that meets the pull request standard below.
10. **Pass CI.** Wait for checks, fix failures caused by the change or required by repository policy, and rerun affected tests and review until required checks pass. If no checks are configured, continue.
11. **Address feedback.** Inspect every current human and bot comment and review thread. Give each one a disposition: change the code or durable documentation, answer the question, push back with technical evidence, link a tracked follow-up and explain why a non-blocking suggestion is outside this pull request, or mark informational feedback as requiring no action. If a reviewer cannot understand the code, clarify the code or documentation before relying on a thread reply. Resolve a thread only when fully addressed. Rerun affected tests and fresh review after requested changes. Do not wait indefinitely for future feedback.
12. **Refresh the pull request.** Update the title, description, and checklist to match the final head, verification, CI state, review findings, and feedback disposition.

Commit and push every post-PR fix before reassessing checks or feedback.

If the ticket, task, or design is wrong or incomplete, update the source of truth before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop when the pull request is green, mergeable, every current comment has a disposition, and no required change remains unresolved. Never merge unless the user explicitly asks. Report an exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.

## Pull request standard

Treat the pull request title and body as durable history for reviewers now and engineers later. Follow a required repository template and add any information or evidence below that it does not cover. If no template exists, use the structure below.

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
  Commands, browser or manual checks, results, and any unverified criteria or affected failure paths.
- **Did you independently review the final diff and address valid findings?** <Yes | No>
  Review evidence, findings fixed, and anything unresolved.
- **Did you update documentation when behavior changed?** <Yes | No | Not applicable>
  User, contributor, and architecture documentation changed or why each was not needed.
- **Did required CI checks pass?** <Yes | No | Pending | Not configured>
  Check names and results.
```
