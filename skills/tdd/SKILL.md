---
name: tdd
description: "Use test-first development for behavioral changes. Write a failing test, make it pass, then simplify."
user-invocable: true
argument-hint: "<what to build> e.g. 'user registration endpoint' or 'retry logic for API client'"
---

# Test-Driven Development

## When to use

- New logic or behavior
- Bug fixes
- Changes that could break existing behavior

## Process

1. Understand the requirement and the relevant code.
2. Write a failing test for the behavior you want.
3. Write the minimum code needed to make the test pass.
4. Simplify the code and tests while they stay green.
5. Run the full relevant test suite before finishing.

## Verification

- The new behavior has a failing-then-passing test
- Bug fixes include a reproduction test
- Tests describe behavior, not implementation details
- The final test suite passes

## Rules

- Make the smallest safe change that satisfies the failing test.
- Preserve existing contracts unless the task explicitly changes them.
- Add tests for failure paths when they matter to the behavior.
- Do not write implementation code before you have a failing test for the behavior.
- Skip TDD for documentation, formatting, or non-behavioral scaffolding work.
- Prefer testing behavior over internals.
- Use mocks sparingly. Prefer real boundaries when practical.
