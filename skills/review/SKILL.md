---
name: review
description: "Uses a fresh agent to review a design or code change without editing it. Checks behavior, security, regressions, complexity, tests, docs, and missing proof. Use for code, PR, diff, security, second-opinion, or pre-merge reviews."
user-invocable: true
argument-hint: "[ticket, design, diff, branch, commit, PR, or file path]"
---

# Review

Use a fresh subagent that did not implement the change. Review without editing files.

## Workflow

1. **Set the frame**
   - Give the reviewer the task, acceptance criteria, repository rules, complete diff or pull request, and test evidence.
   - Name the user or developer affected by the change.

2. **Check the outcome**
   - Read the source design, ticket, or request.
   - Confirm that the change belongs in the system, matches the requested behavior, and delivers one focused outcome.
   - Report a mismatch before reviewing details.

3. **Check the change**
   - Start with the files and flows that deliver the outcome.
   - Check behavior, failures, security boundaries, interfaces, compatibility, migrations, concurrency, and operations.
   - Review every human-written changed line in context for correctness, regressions, complexity, names, comments, style, and documentation.
   - For generated files or large data, inspect the source and spot-check the result.
   - Run focused checks when they can change a finding or verdict.

4. **Check the proof**
   - Confirm that tests cover the acceptance criteria, changed behavior, and affected failure paths.
   - Confirm that assertions would fail for a broken change.
   - Prefer user-visible behavior or a documented internal contract over copied implementation logic.
   - Confirm that test setup does not hide the scenario.
   - Check whether security, privacy, concurrency, accessibility, internationalization, or domain work needs specialist evidence.
   - Mark a risk unverified when the reviewer lacks the evidence or skill to judge it.

5. **Give the verdict**
   - Report findings in severity order. For each one, give the location, impact, evidence, and smallest fix direction.
   - Use `blocker` for unsafe to merge and `important` for should fix before merge. Omit optional nits unless asked.
   - End with `Approve`, `Request changes`, or `Blocked`.
   - State anything that remains unverified.

## Rules

- Approve only when the change matches its source and repository rules, no known defect or unhandled risk threatens security, data, compatibility, or operations, and no simpler design delivers the same outcome and proof.
- Keep findings within the change, but inspect enough context to judge its system effect.
- Cite technical evidence or repository conventions. Do not block on personal taste.
- Do not approve only because checks pass.
- Use `Blocked` when missing specialist evidence could hide a rule-breaking problem.
- If a fresh subagent is unavailable, report that independent review is blocked unless the user accepts a documented self-review.
- Treat the verdict as independent evidence, not GitHub approval or a replacement for human review.
