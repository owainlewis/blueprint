---
name: review
description: "Independently reviews whether a design can satisfy its requirements, plus behavior, security, regressions, complexity, test quality, documentation, and missing evidence. Use when the user asks for a code review, PR review, diff review, security review, second opinion, or pre-merge review. Launches a fresh subagent and never edits the code."
user-invocable: true
argument-hint: "[ticket, design, diff, branch, commit, PR, or file path]"
---

# Review

The reviewer must be a fresh subagent that did not implement the change. Do not edit files.

## Standard

Approve only when the change matches its source, behaves as required, and has no known defect or unmitigated risk that could violate the source or repository policy in security, data loss, compatibility, or operations. If the same outcome and proof can be delivered with less state, indirection, duplication, or operational work, request the simpler design. Do not demand perfection or block on personal taste. Cite technical evidence or repository conventions.

The verdict is independent agent evidence. It is not GitHub approval or a replacement for human review.

## Review order

1. **Set the frame.** Give the reviewer the task, acceptance criteria, repository guidance, complete diff or pull request, and test evidence. Identify the user or developer affected by the change.
2. **Take the broad view.** Read the available change summary, local execution outline, or pull request description, plus the relevant design or ticket. Confirm the change belongs in the system, matches the intended behavior, and is one reviewable outcome. Report a mismatch with the source or a design that cannot satisfy its requirements before reviewing details.
3. **Review the main behavior.** Start with the files and flows that implement the outcome. Check functionality for users and developers, failures, security boundaries, interfaces, compatibility, migrations, concurrency, and operations.
4. **Review every human-written changed line in context.** Inspect enough surrounding code to judge correctness, regressions, complexity, naming, comments, style, and documentation. For generated files or large data, inspect the generator or source and spot-check output. Keep findings within the change's scope.
5. **Review the proof.** Check that tests cover the changed behavior and failure paths affected by the change or named in its acceptance criteria, assert observable behavior or a documented internal contract, would fail under a broken implementation, and do not duplicate implementation logic or obscure the scenario with setup. Run focused checks that can confirm or falsify a claim that could change a finding or verdict.
6. **Check specialist coverage.** Identify security, privacy, concurrency, accessibility, internationalization, or domain-specific work. If the reviewer lacks evidence or expertise for a risk that could violate the source or repository policy, mark it unverified. Use `Blocked` when that gap could conceal such a violation and no qualified reviewer covers it.
7. **Report findings.** Return actionable findings in severity order. For each finding give the location, impact, evidence, and smallest fix direction.

- **blocker:** unsafe to merge.
- **important:** should fix before merge.
- **nit:** optional; omit unless asked.

## Verdict

If fresh subagents are unavailable, stop and report that independent review is blocked unless the user explicitly accepts a documented self-review.

If there are no findings, say so. End with `Approve`, `Request changes`, or `Blocked`, then state what remains unverified.

## Boundaries

- Keep findings within the change, but inspect enough surrounding code to judge each changed line and its system effect.
- Do not turn preferences into findings. Use technical evidence and repository conventions.
- Do not approve solely because checks pass.
