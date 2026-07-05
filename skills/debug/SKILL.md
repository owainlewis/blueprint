---
name: debug
description: "Find and fix the root cause when something breaks: a failing test, a broken build, a bug report, or behavior that doesn't match expectations."
user-invocable: true
argument-hint: "<failure description, error output, or bug report>"
---

# Debug

Goal: find why it fails and fix it.

## Workflow

1. Save the error output, logs, inputs, commands, environment, and current state.
2. Reproduce the failure. If you cannot reproduce it, keep gathering information and report what you observed.
3. Trace the failure to its cause and explain why it happens.
4. Add a small failing test when practical. Make the smallest fix that passes it. If no useful test is practical, explain why and verify another way.
5. Run relevant checks and report the cause, fix, test or reason none, checks run, and anything still unexplained.

## Rules

- Fix the cause, not the symptom.
- One bug at a time.
- Do not pull unrelated failures or flaky infrastructure into the current task.
- Stop when the fix needs a product or code-owner decision.
