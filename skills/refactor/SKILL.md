---
name: refactor
description: "Refactor code to simplify it without changing behavior."
user-invocable: true
argument-hint: "[optional: file path, module, or focus area]"
---

# Refactor

## When to use

- Simplifying code after behavior already works
- Removing duplication, dead code, or unnecessary complexity
- Cleaning up a focused area without changing what it does

## Process

1. Choose the target from `$ARGUMENTS`, current changes, or a clearly relevant recent area. If there is still no clear target, ask.
2. Read the code and its surrounding context before changing it.
3. Remove dead code, flatten needless indirection, and simplify naming or structure where the behavior stays the same.
4. Run the relevant tests and build checks.

## Verification

- Behavior is unchanged
- The code is simpler or smaller
- Tests and build checks pass

## Rules

- Make the smallest safe refactor.
- Preserve contracts and externally visible behavior.
- Do not erase failure-path handling in the name of simplification.
- If the goal is to change behavior, use a different skill.
- If you are not sure a change is behavior-preserving, skip it.
- Prefer deleting or simplifying over adding new abstraction.
- If the code is already clean, say so.
