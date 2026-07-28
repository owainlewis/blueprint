---
name: task-to-pr
description: "Takes one task, ticket, prepared local change, branch, or existing pull request to a tested, independently reviewed, green pull request ready for human merge. Use when the user asks to implement, build, fix, deliver, publish changes, open or update a pull request, or improve a pull request description."
user-invocable: true
argument-hint: "<ticket, task, local change, branch, or pull request>"
---

# Task to PR

Follow this workflow for the requested task, ticket, prepared change, branch, or pull request. For prepared changes or an existing pull request, inspect the implementation and current evidence, then perform only the missing or outdated steps. Never claim inherited checks or review unless they apply to the current head.

1. **Resolve the source.** Inspect the current branch, worktree, local diff, existing pull request, and linked ticket. Resume an existing pull request when one exists. Treat prepared local changes as source material and preserve them. Otherwise fetch the ticket or use the task as the source. Create a ticket only when the user asks or durable tracking improves the handoff or proof. Do not duplicate tickets or pull requests.
2. **Branch.** Reuse a suitable branch and worktree for prepared changes or an existing pull request. Do not move or discard local changes. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Follow the repository's location convention. Remove a manually created worktree after its pull request is merged or closed.
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

Write the pull request for a reviewer deciding whether the change is safe and useful, not as an inventory of edited files.

- Follow the repository's title convention. Otherwise use a title that states the delivered outcome.
- Follow required repository pull request templates and preserve useful human-written context when updating an existing pull request.
- Link the source ticket with the repository's closing syntax when the pull request completes it.
- Lead with why the change matters and what becomes possible or behaves differently.
- Explain observable behavior, important safety rules, compatibility, failure behavior, and operational impact. Include implementation detail only when it helps review a decision or risk.
- Report only verification that actually ran. Separate automated checks, browser evidence, and manual checks when more than one kind exists. State important gaps.
- Summarize independent agent review as supporting evidence. Do not describe it as GitHub approval or imply that it replaces human review.
- Omit empty headings, boilerplate, process narration, and claims the available evidence does not support.
- Keep the body current when later commits change behavior, risk, or verification.

Use this shape when every section adds value:

```markdown
Closes #<ticket>

## Outcome

Why this change matters and its user or operator impact.

## Behavior

- Observable behavior and safety rules a reviewer must understand.
- Compatibility, failure, migration, or operational notes when relevant.

## Verification

- `<command>`: what it proved
- Browser or manual evidence when required
- Any important unverified behavior

## Independent review

What was reviewed, which important findings were fixed, and whether actionable findings remain.
```

Adapt the headings to the work. A small fix may need only a short summary, ticket link, and verification.
