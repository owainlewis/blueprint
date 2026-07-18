---
name: improve
description: "Inspect existing code and improve its clarity, simplicity, and structure without changing intended behavior."
user-invocable: true
argument-hint: "[code, files, diff, branch, or improvement focus]"
---

# Improve

1. Identify the target from the request, current diff, or recently changed code.
2. Read the target, its tests, and relevant surrounding code. Establish the behavior that must not change.
3. Look for unnecessary complexity, duplication, dead code, weak names, awkward boundaries, and abstractions that cost more than they help.
4. Make focused improvements by deleting, deduplicating, renaming, simplifying, extracting, or inlining.
5. Preserve public interfaces, data shapes, errors, and user-visible behavior unless the user explicitly asks to change them.
6. Run the relevant tests and checks. Report what improved, what behavior was preserved, and the evidence.

Do not add product scope or absorb unrelated cleanup. Prefer a few clear edits over a broad rewrite.
