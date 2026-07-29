---
name: review
description: "Uses a fresh agent to review a design or code change without editing it. Checks behavior, security, regressions, complexity, tests, docs, and missing proof. Use for code, PR, diff, security, second-opinion, or pre-merge reviews."
user-invocable: true
argument-hint: "[ticket, design, diff, branch, commit, PR, or file path]"
---

# Review

The reviewer must be a fresh subagent that did not implement the change. Do not edit files.

## Standard

Approve only when:

- The change matches its source and behaves as required.
- No known defect or unhandled risk could break the source or repository rules for security, data loss, compatibility, or operations.
- No simpler design has been identified that delivers the same outcome and proof with less state, indirection, duplication, or operational work.

Do not demand perfection or block on personal taste. Cite technical evidence or repository conventions.

The verdict is independent agent evidence. It is not GitHub approval or a replacement for human review.

## Review order

1. **Set the frame.** Give the reviewer the task, acceptance criteria, repository rules, complete diff or pull request, and test evidence. Name the user or developer affected by the change.
2. **Take the broad view.** Read the change summary and the relevant design or ticket. Confirm that the change belongs in the system, matches the intended behavior, and delivers one reviewable outcome. Report a mismatch before reviewing details.
3. **Review the main behavior.** Start with the files and flows that deliver the outcome. Check behavior, failures, security boundaries, interfaces, compatibility, migrations, concurrency, and operations.
4. **Review every human-written changed line in context.** Read enough surrounding code to judge correctness, regressions, complexity, names, comments, style, and docs. For generated files or large data, inspect the source and spot-check the output. Keep findings within the change's scope.
5. **Review the proof.** Check that tests:
   - Cover the changed behavior and affected failure paths.
   - Prove the acceptance criteria.
   - Assert behavior a user or caller can observe, or a documented internal contract.
   - Would fail under a broken implementation.
   - Do not copy implementation logic or hide the scenario in setup.
6. Run focused checks that can confirm or disprove a claim that could change a finding or verdict.
7. **Check specialist coverage.** Identify security, privacy, concurrency, accessibility, internationalization, or domain-specific work. Mark a risk unverified when the reviewer lacks the evidence or skill to judge it. Use `Blocked` when that gap could hide a problem that breaks a rule and no qualified reviewer covers it.
8. **Report findings.** Return actionable findings in severity order. For each finding give the location, impact, evidence, and smallest fix direction.

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
