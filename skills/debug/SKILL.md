---
name: debug
description: "Find and fix the root cause when something breaks: a failing test, a broken build, a bug report, or behavior that doesn't match expectations."
user-invocable: true
argument-hint: "<failure description, error output, or bug report>"
---

# Debug

1. Reproduce the failure. If you can't, keep gathering information and report what you observed.
2. Trace it to the root cause and explain why it happens.
3. Add a small failing test when practical, then make the smallest fix that passes it. If no test is practical, say why and verify another way.
4. Run relevant checks. Report the cause, the fix, how it was verified, and anything still unexplained.

## Rules

- Fix the cause, not the symptom. One bug at a time.
- Don't pull unrelated failures or flaky infrastructure into the task.
- Stop when the fix needs a product or code-owner decision.
