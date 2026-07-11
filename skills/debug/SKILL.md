---
name: debug
description: "Find and fix the root cause when something breaks: a failing test, a broken build, a bug report, or behavior that doesn't match expectations."
user-invocable: true
argument-hint: "<failure description, error output, or bug report>"
---

# Debug

1. Reproduce the failure. If you cannot, keep gathering information and report what you observed.
2. Trace it to the root cause and explain why it happens.
3. Add a small failing regression test when practical, then make the smallest fix that passes it. If no useful test is practical, say why and verify another way.
4. Run relevant checks. Report the cause, the fix, how it was verified, and anything still unexplained.

## Rules

- Fix the cause, not the symptom. Do not delete the failing check, swallow the error, or weaken the assertion unless that is the real fix.
- One bug at a time.
- Do not pull unrelated failures or flaky infrastructure into the task.
- Stop when the fix needs a product or code-owner decision.
