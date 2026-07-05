---
name: refactor
description: "Improve the shape of existing code without changing behavior."
user-invocable: true
argument-hint: "[optional files, diff, commit, or cleanup focus]"
---

# Refactor

Goal: simplify code without changing behavior.

## Workflow

1. Identify the target from `$ARGUMENTS`, specified files, current diff, staged diff, latest commit, or recently touched files.
2. Read the code, tests, function signatures, return values, data shapes, behavior that must not change, and check commands. For risky refactors, run focused tests first.
3. Make small edits that keep behavior the same: delete code, remove duplication, clarify names, simplify control flow, improve file boundaries, reuse existing helpers, extract or inline functions.
4. Preserve public functions, commands, config, routes, return values, data shapes, errors, and user-visible output unless the user explicitly asks to change them.
5. Run relevant checks. Run wider checks when shared behavior or public behavior was touched.
6. Report what changed, what stayed the same, and checks run.

## Rules

- Refactoring is not feature work.
- Do not expand the task into unrelated cleanup.
- Do not change behavior to make the refactor easier.
- Keep abstractions only when they reduce complexity or duplication.
