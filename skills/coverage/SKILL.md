---
name: coverage
description: "Evaluate test coverage and fill real gaps with high-value tests."
user-invocable: true
argument-hint: "[optional: file path or module to evaluate]"
---

# Coverage

## When to use

- You want to check whether recent work is tested well enough
- A file or module looks fragile or under-tested
- You want to add tests without changing behavior

## Process

1. Choose the target from `$ARGUMENTS`, current changes, or the latest commit. If there is still no clear target, ask.
2. Read the code and the existing tests.
3. Identify realistic gaps: edge cases, failure paths, state changes, and integration points.
4. Add only the tests that would catch a real bug.
5. Run the relevant tests and confirm they pass.

## Verification

- The target area is clear
- New tests cover real risk, not coverage vanity
- The code under test was not changed
- Tests pass

## Rules

- Focus on the smallest set of tests that meaningfully improves confidence.
- Add coverage for contract and failure-path behavior before edge-case trivia.
- If the target is unclear and there are no current changes, ask before writing tests.
- Do not write tests just to raise a number.
- Do not add tests for trivial code or framework behavior.
- If the code is already well-tested, say so.
