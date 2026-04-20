---
name: debug
description: "Debug systematically: observe, hypothesize, test, fix, verify."
user-invocable: true
argument-hint: "[optional: description of the bug or symptom]"
---

# Debug

## When to use

- Something is broken
- A test is failing
- Behavior does not match expectations

## Process

1. Reproduce the problem and read the real error or failing output.
2. Form one hypothesis about the root cause.
3. Run one targeted check to confirm or reject that hypothesis.
4. Fix the root cause and add a test that proves it.
5. Run the strongest relevant verification before finishing.

## Verification

- The problem is reproduced before the fix
- The root cause is identified, not guessed
- The fix is covered by a test where possible
- The final checks pass

## Rules

- Make the smallest safe fix for the proven root cause.
- If the bug comes from a contract mismatch or unhandled failure path, fix that explicitly.
- If there is no concrete bug or symptom, clarify the problem before debugging.
- One hypothesis at a time.
- Fix root cause, not symptoms.
- Do not hide missing evidence. If you did not run it, say so.
- If repeated attempts fail, step back and trace the data flow from the entry point.
