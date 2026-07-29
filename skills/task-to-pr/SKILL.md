---
name: task-to-pr
description: "Takes one task from its source to a tested and independently reviewed pull request. Use to implement, build, fix, or deliver one task, ticket, or existing pull request."
user-invocable: true
argument-hint: "<ticket, task, or pull request>"
---

# Task to PR

Follow this workflow for the requested task, ticket, or pull request:

1. **Resolve the source.** Resume an existing pull request and its linked ticket when one exists. Otherwise fetch the ticket or use the task as the source. Create a ticket only when the user asks or saved tracking would improve the handoff or proof. Do not duplicate tickets or pull requests.
2. **Branch.** Resume the branch and worktree for an existing pull request. For new work:
   - Fetch the remote.
   - Create a branch and worktree from the latest remote default branch.
   - Name it with the ticket number or task slug.
   - Follow the repository's location rules and reuse a suitable worktree.
   - Remove a manually created worktree after its pull request is merged or closed.
3. **Read the context.** Read the repository instructions and inspect the relevant code.
4. **Outline the change.** Define one focused outcome and its proof. A reviewer must be able to understand it without separating unrelated work. If the source requires several outcomes, split it or return to planning before coding.
   - Separate refactoring when it would hide the behavior change.
   - Keep small local cleanup only when it makes the change easier to review.
   - Keep this as a local execution outline, not a plan document.
5. **Implement.** Make the change and test:
   - Changed behavior.
   - Affected failure paths and any failure path named in the acceptance criteria.
   - Behavior that a refactor must preserve.
6. Update the existing architecture document when code changes documented ownership, dependency direction, protocols, stored data, trust boundaries, deployment topology, or hard limits.
7. If automated tests cannot exercise the affected behavior, explain why and give other evidence.
8. **Test and self-review.** Run tests and checks that cover the changed behavior and affected interfaces. Use a real browser when browser-rendered behavior changes. Inspect the final diff for accidental scope, unclear code, and missing proof.
9. **Review.** Review the change with a fresh subagent that did not implement it.
10. **Address findings.** Fix valid review findings, then rerun affected tests and fresh review.
11. **Publish.** Create a Conventional Commit, push the branch, and open or update a ready pull request that meets the pull request standard below.
12. **Pass CI.** Wait for checks. Fix failures caused by the change or required by repository policy. Rerun affected tests and review until required checks pass. Continue when no checks are configured.
13. **Address feedback.** Inspect every current human and bot comment and review thread. Give each one a clear outcome:
    - Change the code or lasting documentation.
    - Answer the question.
    - Push back with technical evidence.
    - Link a tracked follow-up and explain why the suggestion is outside this pull request.
    - Mark information that needs no action.
14. If a reviewer cannot understand the code, clarify the code or documentation before relying on a thread reply. Resolve a thread only when fully addressed.
15. Rerun affected tests and fresh review after requested changes. Do not wait indefinitely for future feedback.
16. **Refresh the pull request.** Update the title, description, and checklist to match the final commit, verification, CI state, review findings, and feedback outcomes.

Commit and push every post-PR fix before reassessing checks or feedback.

If the ticket, task, or design is wrong or incomplete, update it before continuing. Prefer the smallest complete change and no unrelated cleanup.

Stop when the pull request is mergeable, all required checks pass, every current comment has a clear outcome, and no required change remains unresolved.

Never merge unless the user explicitly asks. Report the exact blocker when required access, checks, or independent review remain unavailable after safe alternatives are exhausted.

## Pull request standard

Treat the pull request title and body as useful history for reviewers now and engineers later. Follow the repository template when one exists. Add information below it only when a reviewer needs it. Otherwise use the structure below.

- Follow the repository's title convention. Otherwise use a short, standalone title that states the delivered outcome.
- Link the source ticket with the repository's closing syntax when the pull request completes it.
- Give enough context to understand the change without opening the ticket or reading the whole diff.
- Start with two to four short sentences. Explain the problem, what changed, and why it matters.
- Use everyday words. Define any technical term the reader needs.
- Put technical detail after the summary. Include only behavior, decisions, risks, shortcomings, and evidence that help the review.
- Do not list edited files.
- For a complex change, say where to start and what needs the closest review.
- Answer every checklist item with an explicit status and evidence. Use `Not applicable`, `Not configured`, or `Pending` instead of a checked box that implies success.
- Treat independent agent review as evidence, not GitHub approval or a replacement for human review.
- Preserve useful human-written context when updating an existing pull request.
- Keep the body short and current when later commits change behavior, risk, or verification.

```markdown
Closes #<ticket>

## Plain English summary

In two to four short sentences, explain the problem, what changed, and why it
matters. Use everyday words. Do not list files or use unexplained technical
terms.

## Details

Add only behavior or decisions that are not clear from the summary. Skip this
section when the summary is enough.

## Reviewer notes

Include only facts that change how this pull request should be reviewed: risk,
tradeoff, failure behavior, compatibility, migration, or where to start. Write
`None` when none apply.

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
