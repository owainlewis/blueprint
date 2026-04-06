---
name: coverage
description: "Evaluate test coverage for recent code and fill gaps with high-value tests. Only adds tests worth having."
user-invocable: true
argument-hint: "[optional: file path or module to evaluate]"
---

# Test Coverage

> Every test should justify its existence. A small suite that catches real bugs beats a large one that catches nothing.

Evaluate whether the code has adequate test coverage. If not, write the tests that are missing — but only tests that earn their place.

## What to evaluate

- If given a file or module via `$ARGUMENTS`: evaluate that.
- If no arguments: evaluate recently changed files (`git diff --name-only HEAD~3`).

## Process

1. **Read the code.** Understand what it does, what its edge cases are, and where bugs could hide.

2. **Find existing tests.** Look for test files that cover this code. Read them. Understand what's already tested.

3. **Identify gaps.** Ask: what could break that isn't tested? Focus on:
   - Error paths and failure modes
   - Edge cases and boundary conditions
   - Business logic with real consequences if wrong
   - State transitions and side effects
   - Integration points between components

4. **Write the missing tests.** Add them to the appropriate test files (or create a test file if none exists, following the project's conventions).

5. **Run the tests.** Show the actual output. All tests must pass.

## What makes a good test

A test earns its place if you can describe a realistic bug it would catch. If you can't, don't write it.

**Write tests for:**
- Your logic, your decisions, your edge cases
- Things that broke before or look fragile
- Complex conditions where off-by-one or wrong-branch errors hide
- Integration between your components

**Do not write tests for:**
- Constructors, getters, setters, or trivial field assignments
- Framework or library behavior (they have their own tests)
- Code that only delegates to a dependency without adding logic
- Happy paths that are obvious and unlikely to break
- Mock-heavy tests that verify you called a method — test outcomes, not call sequences

**Testing principles:**
- Test behavior, not implementation. Tests should survive refactoring.
- Prefer real dependencies over mocks. A real database call catches more than a mock.
- One assertion per concept. A test that checks five things tests nothing well.
- Name tests after the behavior: "rejects expired tokens" not "test_validate_token_3".
- Prefer clarity over DRY in tests. Duplicating setup across tests is fine if it makes each test self-explanatory. A reader should understand what a test does without jumping to shared helpers.
- If you need complex setup to test something, that's a design smell — note it, don't hide it with test infrastructure.

## Rules

- Never write a test just to increase a coverage number.
- Never mock something to make a test pass that wouldn't pass against the real thing.
- If the code is well-tested, say so. Not everything has gaps.
- Do not modify the code under test. You are adding tests, not refactoring.
