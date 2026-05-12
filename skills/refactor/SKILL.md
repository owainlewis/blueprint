---
name: refactor
description: "Improve the shape of existing code without changing behavior."
user-invocable: true
argument-hint: "[optional files, diff, commit, or cleanup focus]"
---

# Refactor

Improve code shape without changing behavior. Use this when the user asks to refactor, simplify, tidy, clean up, reduce duplication, improve design, or make code easier to maintain.

## Workflow

### 1. Understand

- Use `$ARGUMENTS`, specified files, `git diff`, staged changes, or the latest commit.
- If staged changes exist, review `git diff HEAD`; otherwise review `git diff`.
- If there are no Git changes, review the most recently modified files named by the user or touched in the current task.
- Read the target code, surrounding patterns, tests, contracts, invariants, and verification commands.
- Identify what behavior must stay the same before editing.
- For risky refactors, run existing focused tests first to establish the current baseline.

### 2. Find Simplifications

Look for changes that would make the code easier to understand, maintain, or safely extend:

- duplicated or near-duplicated logic
- unclear names or hidden concepts
- long functions doing multiple jobs
- unnecessary abstractions, wrappers, layers, or indirection
- missing reuse of existing helpers, utilities, or local conventions
- tangled conditionals, data flow, or error handling
- poor module boundaries or leaky abstractions
- comments that could become clearer code
- inefficient work that can be removed without changing behavior

### 3. Refactor

- Make small, targeted, behavior-preserving edits.
- Prefer deleting code, clarifying names, extracting or inlining functions, reusing existing helpers, and simplifying control flow.
- Add an abstraction only when it clearly reduces complexity or meaningful duplication.
- Preserve public contracts, data shape, error behavior, and user-visible output unless the user explicitly asks to change them.
- Skip changes that would make the code merely different rather than simpler.

### 4. Verify

- Run the relevant tests and checks after editing.
- Run broader tests when the refactor touches shared behavior or contracts.
- If no code changes were needed, say the target was already clean.
- Report what changed, what stayed behaviorally the same, and what verification ran.

## Rules

- Refactoring is not feature work.
- Do not broaden scope into unrelated cleanup.
- Do not change behavior to make refactoring easier.
- Stop and ask before changing public contracts, data shape, or user-visible behavior.
- Keep abstractions earned by real simplification, not aesthetic preference.
- A good refactor makes the code easier to understand, not merely different.
