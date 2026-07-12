---
name: refactor
description: "Improve the shape of existing code without changing behavior."
user-invocable: true
argument-hint: "[optional files, diff, commit, or cleanup focus]"
---

# Refactor

1. Identify the target from `$ARGUMENTS`, the current diff, latest commit, or recently touched files.
2. Read the code and tests. Understand what behavior must not change. For risky refactors, run focused tests first.
3. Make small behavior-preserving edits: delete, deduplicate, rename, simplify, extract or inline.
4. Don't change public interfaces, data shapes, errors, or user-visible output unless the user asks.
5. Run relevant checks, wider ones when shared behavior was touched.
6. Report what changed, what stayed the same, and checks run.

## Rules

- Refactoring is not feature work. Don't expand into unrelated cleanup.
- Don't change behavior to make the refactor easier.
- Keep an abstraction only when it reduces complexity or duplication.
