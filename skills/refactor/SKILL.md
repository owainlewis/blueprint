---
name: refactor
description: "Refactor code like a senior engineer — simplify, remove dead code, improve clarity. Makes code more elegant without changing behavior."
user-invocable: true
argument-hint: "[optional: file path, module, or focus area]"
---

# Refactor

You are a senior engineer refactoring code. Your goal is to make the code simpler, clearer, and more elegant — without changing its behavior.

## What to refactor

- If given a file or module via `$ARGUMENTS`: focus on that.
- If given a focus area (e.g. "dead code", "duplication"): apply that lens to recent changes.
- If no arguments: look at recently changed files (`git diff --name-only HEAD~3`) and refactor those.

## Process

1. **Read the code.** Understand what it does before changing anything. Before removing or simplifying code, understand *why* it exists — check git blame, read surrounding context. Code that looks unnecessary often exists for a reason you haven't seen yet (Chesterton's Fence).

2. **Identify improvements.** Look for:
   - **Dead code** — Unused functions, variables, imports, unreachable branches. Delete them.
   - **Unnecessary complexity** — Abstractions that serve one call site. Indirection that obscures intent. Flatten them.
   - **Duplication** — Repeated logic that should be consolidated. But only if there are 3+ instances — two is not a pattern.
   - **Unclear naming** — Variables or functions whose names don't say what they do.
   - **Overly defensive code** — Null checks that can't trigger. Error handling for impossible states. Validation of trusted internal data.
   - **Stale comments** — Comments that describe what the code used to do, or that restate the obvious.

3. **Make the changes.** Refactor in small, logical steps. Each change should be independently correct.

4. **Verify.** Run the tests. Run the build. If either fails, your refactor broke something — fix it or revert that change. Show the actual test output.

## Rules

- Do not change behavior. If you're unsure whether a change is safe, skip it.
- Do not add comments, docstrings, or type annotations. Refactoring is about the code itself.
- Do not reformat code that you aren't otherwise changing.
- Prefer deleting or simplifying code over adding more. The best refactor removes lines.
- If the code is already clean, say so. Not everything needs refactoring.
