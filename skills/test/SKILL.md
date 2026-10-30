---
name: test
description: "Proves a code change works: runs every repository check until green, then proves each acceptance criterion with tests, and with a real browser for anything visible. Use to test or verify a diff, branch, PR, URL, or user flow."
user-invocable: true
argument-hint: "<task, acceptance criteria, diff, branch, PR, URL, or flow>"
disable-model-invocation: true
---

# Test

Show that each acceptance criterion passes. Reading the code is not proof.

## Steps

1. Run every check the repository has: format, lint, typecheck, and tests. The commands are in `AGENTS.md`, `CLAUDE.md`, the README, or the project's scripts. Fix what the change broke and run them all again. After three rounds on the same failure, stop and report it.
2. List each acceptance criterion (`AC-n`, `REQ-n`, `INV-n`) from the ticket, word for word.
3. Point each criterion to a test that proves it. Where none exists, write one that calls the public interface. Revert the code once to confirm the main new test fails.
4. If the change is visible in a browser, run the flow in Playwright. Check desktop and mobile widths, keyboard use, and console errors. Save screenshots for the PR.

## Return

Failures and unverified criteria first:

```text
Criterion: <ID or exact wording>
Result: Pass / Fail / Unverified
Evidence: <command, browser flow, or screenshot>
```

Then each check command you ran and its result.

Fix the code, not the test. Report failures the change did not cause; leave them alone.
