---
name: test
description: "Proves that a code change works: runs every repository check until green, then proves each acceptance criterion with focused tests and a real browser for browser-facing work. Use to test or verify a diff, branch, PR, URL, or user flow."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
disable-model-invocation: true
---

# Test

Prove the behavior that matters. A passing build or a reading of the source can support the proof, but neither proves a user-visible flow.

## Process

1. Read the task, its spec, the changed code, existing tests, and repository instructions. Take acceptance criteria from the task or spec with their `AC-n`, `REQ-n`, and `INV-n` IDs. Never rewrite criteria to match the code.
2. Run every check the repository defines: format, lint, typecheck, and the test suite. Find the commands in `AGENTS.md`, `CLAUDE.md`, the README, or the project's scripts. Fix each failure the change caused and run all checks again. Stop after three rounds on the same failure and report it with the output.
3. Map each criterion, cited invariant, and affected failure path to a proof. Include behavior a refactor must keep.
4. Add focused tests where proof is missing. Test what a user or caller can observe through the public interface. Each assertion must fail if the changed behavior breaks; for the main new test, revert the implementation once and confirm it fails.
5. When browser-rendered behavior changes, start the app and run the flows in a real browser with Playwright.
   - Check desktop and mobile widths when layout changed.
   - Check keyboard use when interactions changed.
   - Check the console and network for errors during each flow.
   - Save screenshots for the PR.
6. If automated tests cannot reach the behavior, say why and give other evidence.

## Return

Lead with failures and unverified criteria. Report each criterion like this:

```text
Criterion: <ID or exact wording>
Result: Pass / Fail / Unverified
Evidence: <command, browser flow, or screenshot>
Gap: <what remains unknown, or None>
```

Then list every check command you ran and its result.

## Rules

- Keep assertions as strict as the behavior requires. Fix the code, not the test.
- Leave unrelated failures alone and report them.
- If browser tooling is unavailable, report browser checks as blocked unless the user accepts a manual check.
