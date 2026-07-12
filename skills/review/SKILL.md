---
name: review
description: "Independently review a diff, branch, commit, or PR for correctness, security, broken contracts, scope, complexity, and missing tests. Never edit the code."
user-invocable: true
argument-hint: "[ticket, spec, diff, branch, commit, PR, or file path]"
---

# Review

Find actionable reasons the change should not merge. Do not edit files.

1. Identify the change and the task it claims to satisfy. Read the ticket, spec, or request when available; state what context is missing. Also read repository review guidance such as `REVIEW.md` when present. Project guidance supplements the built-in checks below; it never replaces them.
2. Read the tests before the implementation. Inspect the diff, relevant surrounding code, and existing contracts.
3. Run focused checks when practical. Treat code, tests, and command output as evidence; do not trust the author's summary.
4. Check every acceptance criterion and the quality areas below.
5. Report findings in severity order with the template below. If there are no findings, say so plainly and name any residual verification gap.

## Check

- Correct behavior, edge cases, invalid input, retries, partial failure, and cleanup.
- Security boundaries, authorization, secrets, injection, unsafe input, and data exposure.
- Public interfaces, schemas, state transitions, error shapes, compatibility, and migrations.
- Regressions in behavior the change reaches or replaces.
- Tests that prove the requested outcome and important failure paths. Flag tests that mock the unit under test, miss the changed branch, or only repeat the implementation.
- Scope beyond the task, unrelated cleanup, dead code, placeholders, and undocumented behavior changes.
- Unnecessary dependencies, wrappers, configuration, one-use abstractions, and custom code the platform already provides.

## Severity

- **blocker:** unsafe to merge; correctness, security, data, contract, or proof failure.
- **important:** should fix before merge; meaningful regression risk, missing behavior, weak proof, or avoidable complexity.
- **nit:** optional and non-blocking. Omit nits unless the user asks for them.

## Finding Template

```markdown
### <Severity>: <Short title>

- Location: `<file:line>`
- Problem: What is wrong.
- Impact: What breaks or becomes risky.
- Evidence: Code path, test gap, or reproducible behavior.
- Fix: The smallest valid direction, without implementing it.
```

End with:

```markdown
Verdict: Approve | Request changes | Blocked
Tests: Whether the checks exercise the changed behavior and what remains unproved.
```

## Rules

- Review the change, not unrelated pre-existing code.
- Do not turn preferences into findings unless they violate a stated convention or create concrete risk.
- Do not approve because checks pass; judge whether the checks prove the right behavior.
- Do not fix findings. The author owns the code and reruns review after material changes.
