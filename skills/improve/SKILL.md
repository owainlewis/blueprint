---
name: improve
description: "Makes existing code easier to understand without changing behavior. Use to simplify structure, remove duplication or dead code, improve names, or remove unnecessary abstractions."
user-invocable: true
argument-hint: "[code, files, diff, branch, or improvement focus]"
---

# Improve

Make existing code easier to understand without changing what it does.

## Workflow

1. **Choose the target**
   - Use the request, current diff, or recently changed code.
   - Read the target, its tests, and the surrounding code needed to understand it.

2. **Protect existing behavior**
   - State what must not change.
   - Add focused tests first when that behavior lacks proof.
   - If automated tests cannot cover it, explain why and name other evidence.

3. **Simplify**
   - Find duplication, dead code, weak names, awkward boundaries, and abstractions that cost more than they help.
   - Delete, combine, rename, extract, inline, or reorder code where it makes the target clearer.
   - Prefer a few focused edits over a broad rewrite.

4. **Verify**
   - Run checks that cover every behavior the refactor could affect.
   - Confirm that public interfaces, data shapes, errors, and user-visible behavior did not change.

5. **Report**
   - Say what became simpler.
   - Say what behavior stayed the same.
   - Give the test or other evidence.

## Rules

- Do not add product scope or absorb unrelated cleanup.
- Preserve behavior unless the user explicitly asks to change it.
