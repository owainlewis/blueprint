---
name: debug
description: "Find and fix the root cause when something breaks: a failing test, a broken build, a bug report, or behavior that doesn't match expectations. Use when the user says 'debug', 'why is this failing', 'fix this bug', or when a failure interrupts other work."
user-invocable: true
argument-hint: "<failure description, error output, or bug report>"
---

# Debug

Find the root cause before continuing other work.

## Workflow

1. **Preserve the evidence.** Capture the error output, logs, and the state that produced the failure before changing anything.
2. **Reproduce it.** Make the failure happen reliably. If you can't reproduce it, gather context until you can; report what you observed rather than fixing blind.
3. **Find the root cause.** Trace the error to the code and explain why it happens.
4. **Prefer regression-test-first.** When a focused test can capture the failure, run `tdd`: write the failing test from the root cause, make it pass, and keep it. If not practical, explain why, make the smallest justified fix, and verify with the strongest relevant checks.
5. **Verify and report.** Run wider checks, then report root cause, fix, guard test or why none, and anything still unexplained.

## Rules

- Fix the cause, not the symptom. Deleting the assertion, widening the type, or swallowing the exception is not a fix.
- One bug at a time. If diagnosis reveals a second issue, report it instead of expanding the fix.
- If the failure comes from unrelated code or flaky infrastructure, say so and report it; don't absorb it into the current task.
- Stop and hand back when the root cause needs a product or ownership decision.
