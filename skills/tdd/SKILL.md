---
name: tdd
description: "Test-first variant of implement: understand the desired behavior, write a failing test, make it pass, then simplify."
user-invocable: true
argument-hint: "<task reference or behavior> e.g. 'LIN-123' or 'retry logic for API client'"
---

# TDD

1. Read the request, its sources, and the relevant code. Ask before writing tests only when a missing decision would change behavior, interfaces, or checks.
2. Red: write the smallest failing test that proves the behavior or reproduces the bug. Run it and confirm it fails for the expected reason.
3. Green: write the minimum implementation that passes. Don't change existing interfaces or user-visible behavior unless the task requires it. Add failure-path tests where they matter.
4. Refine: simplify code and tests while they keep passing. Run focused checks, then wider ones.
5. Report the test that failed before, passes after, and final checks.

## Rules

- No implementation code before a failing test for the behavior.
- State low-risk assumptions and keep moving.
- Tests describe behavior, not implementation details.
- Prefer real boundaries over mocks when practical.
- Skip TDD for docs, formatting, or non-behavioral scaffolding.
