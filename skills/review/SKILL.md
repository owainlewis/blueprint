---
name: review
description: "Have a fresh subagent independently review a change for correctness, security, regressions, complexity, and missing proof. Never edit the code."
user-invocable: true
argument-hint: "[ticket, design, diff, branch, commit, PR, or file path]"
---

# Review

The reviewer must be a fresh subagent that did not implement the change. Do not edit files.

1. Give the reviewer the task, acceptance criteria, repository guidance, diff or PR, and test evidence.
2. Have it read the relevant surrounding code and try to prove the change wrong. Check behavior, edge cases, failures, security boundaries, interfaces, compatibility, regressions, scope, complexity, and whether tests exercise the changed behavior.
3. Have it run focused checks when practical.
4. Return actionable findings in severity order. For each finding give the location, impact, evidence, and smallest fix direction.

- **blocker:** unsafe to merge.
- **important:** should fix before merge.
- **nit:** optional; omit unless asked.

If fresh subagents are unavailable, stop and report that independent review is blocked unless the user explicitly accepts a documented self-review.

If there are no findings, say so. End with `Approve`, `Request changes`, or `Blocked`, then state what remains unverified.

Review only the change. Do not turn preferences into findings or approve solely because checks pass.
