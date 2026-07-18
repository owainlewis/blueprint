---
name: improve
description: "Improves existing code without changing intended behavior by simplifying structure, removing duplication and dead code, clarifying names, and reducing unnecessary abstractions. Use when the user asks to improve, simplify, clean up, refactor, reduce complexity, remove duplication, or make existing code easier to understand."
user-invocable: true
argument-hint: "[code, files, diff, branch, or improvement focus]"
---

# Improve

## Workflow

1. Identify the target from the request, current diff, or recently changed code.
2. Read the target, its tests, and relevant surrounding code. Establish the behavior that must not change.
3. Look for unnecessary complexity, duplication, dead code, weak names, awkward boundaries, and abstractions that cost more than they help.
4. Make focused improvements by deleting, deduplicating, renaming, simplifying, extracting, or inlining.
5. Preserve public interfaces, data shapes, errors, and user-visible behavior unless the user explicitly asks to change them.
6. Run the relevant tests and checks. Report what improved, what behavior was preserved, and the evidence.

## Boundaries

- Do not add product scope or absorb unrelated cleanup.
- Prefer a few clear edits over a broad rewrite.
- Preserve behavior even when a redesign would be easier.
