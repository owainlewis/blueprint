---
name: improve
description: "Makes existing code easier to understand without changing behavior. Use to simplify structure, remove duplication or dead code, improve names, or remove unnecessary abstractions."
user-invocable: true
argument-hint: "[code, files, diff, branch, or improvement focus]"
---

# Improve

## Workflow

1. Identify the target from the request, current diff, or recently changed code.
2. Read the target, its tests, and relevant surrounding code. State the behavior that must not change.
3. If that behavior lacks tests, add focused coverage before refactoring. If automated tests cannot exercise it, explain why and give other evidence.
4. Find unnecessary complexity, duplication, dead code, weak names, awkward boundaries, and abstractions that cost more than they help.
5. Make focused improvements by deleting, deduplicating, renaming, simplifying, extracting, or inlining.
6. Preserve public interfaces, data shapes, errors, and user-visible behavior unless the user explicitly asks to change them.
7. Run tests and checks that cover behavior the refactor can affect. Report what improved, what behavior was preserved, and the evidence.

## Boundaries

- Do not add product scope or absorb unrelated cleanup.
- Prefer a few clear edits over a broad rewrite.
- Preserve behavior even when a redesign would be easier.
