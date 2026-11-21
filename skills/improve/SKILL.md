---
name: improve
description: "Simplifies existing code without changing behavior. Flattens shallow wrappers, removes duplication and dead code, consolidates fragmented helpers, and clarifies data flow. Use on a diff, file, module, or codebase."
user-invocable: true
argument-hint: "[code, files, diff, branch, or module]"
disable-model-invocation: true
---

# Improve

Make code easier to understand and change without altering what it does. Reduce the layers a reader must trace and the hidden state they must remember.

## Process

1. Identify the target from the request, current diff, or recently changed code.
2. Read the target, its tests, and relevant callers. State the behavior that must not change.
3. Choose the mode from the scope:
   - **Focused target** (diff, function, or a few files): make targeted edits directly.
   - **Broad target** (whole module, package, or codebase): report the top 3 to 5 highest-leverage simplifications with tradeoffs and confirm which to apply before editing.
4. Before editing, add focused characterization tests if the preserved behavior lacks coverage, run them against the unchanged code, and commit that test-only change. If automated tests cannot exercise the behavior, explain why and give other evidence.
5. Delete first: remove dead code, unused parameters, and redundant checks before reshaping what remains.
6. Simplify with clear structural goals:
   - Flatten shallow wrappers and pass-through layers that add indirection without hiding real complexity.
   - Consolidate fragmented single-use helpers or files back into one cohesive module.
   - Pull complexity downward so callers see a smaller, clearer interface.
   - Replace flag soup, hidden mutable state, and premature abstractions with direct, readable code.
7. Preserve public interfaces, data shapes, errors, and user-visible behavior unless the user explicitly asks to change them.
8. Run the tests and checks covering every behavior the refactor can affect.

## Return

In plain, simplified technical English, state what became simpler, what behavior stayed the same, and which checks prove it. Name any behavior that remains unverified.

## Boundaries

- Do not add product scope or absorb unrelated cleanup.
- Prefer a few clear edits over a broad rewrite.
- Preserve behavior even when a redesign would be easier.
