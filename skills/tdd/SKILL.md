---
name: tdd
description: "Build a feature test-first. Write failing tests that define the behavior, then implement until green."
user-invocable: true
argument-hint: "<what to build> e.g. 'user registration endpoint' or 'retry logic for API client'"
---

# Test-Driven Development

> Every test should justify its existence. A small suite that catches real bugs beats a large one that catches nothing.

Build a feature by writing the tests first. The tests define what the code should do. Then write the code to make them pass.

## Input

The user provides: $ARGUMENTS

This is a description of the feature or behavior to implement.

## Process

1. **Understand the requirement.** Read any referenced files, existing code, or architecture docs to understand context. If the requirement is ambiguous, ask before proceeding.

2. **Write failing tests.** Define the behavior through tests:
   - Start with the core behavior — what must this do?
   - Add edge cases — what happens at boundaries?
   - Add failure modes — what should happen when things go wrong?
   - Run the tests. They must fail. If they pass, you're not testing anything new.

3. **Implement.** Write the minimum code to make the tests pass.
   - Do not write code that isn't demanded by a failing test.
   - Run tests after each meaningful change. Show the output.
   - Stop as soon as all tests are green.

4. **Simplify.** Look at the implementation and the tests together:
   - Can the implementation be simpler while keeping tests green?
   - Are any tests redundant now that you see the implementation?
   - Remove anything that isn't pulling its weight.

5. **Final verification.** Run the full test suite. Show output. Confirm nothing is broken.

## What tests to write

Apply the same standards as `/blueprint:coverage` — every test must catch a realistic bug.

**Good tests for TDD:**
- Behaviors the user described ("it should retry 3 times")
- Error handling ("it should return 404 when not found")
- Boundary conditions ("empty input", "maximum length")
- State that matters ("after cancellation, no further events are emitted")

**Skip:**
- Tests that verify wiring or delegation without logic
- Tests for behavior the framework guarantees
- Mock-heavy tests that test the mock, not the code

## Rules

- Tests come first. Do not write implementation code before you have a failing test for it.
- Keep tests focused. One behavior per test.
- The implementation should be the simplest thing that passes. Resist the urge to over-engineer.
- If the requirement is too large for one pass, break it into smaller behaviors and TDD each one.
- Commit when green — working code with passing tests is a natural commit point.
