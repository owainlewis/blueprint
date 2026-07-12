---
name: review
description: "Independently review a diff, branch, commit, or PR for bugs, security problems, broken behavior, unnecessary complexity, and missing tests. Never edit the code."
user-invocable: true
argument-hint: "[ticket, spec, diff, branch, commit, PR, or file path]"
---

# Review

Do not edit files.

1. Read the task, acceptance criteria, repository review guidance, tests, diff, and relevant surrounding code.
2. Try to prove the change wrong. Check behavior, edge cases, failures, security boundaries, interfaces, compatibility, regressions, scope, complexity, and whether tests exercise the changed behavior.
3. Run focused checks when practical.
4. Report actionable findings in severity order. For each finding give the location, impact, evidence, and smallest fix direction.

- **blocker:** unsafe to merge.
- **important:** should fix before merge.
- **nit:** optional; omit unless asked.

If there are no findings, say so. End with `Approve`, `Request changes`, or `Blocked`, then state what remains unverified.

Review only the change. Do not turn preferences into findings or approve solely because checks pass.
