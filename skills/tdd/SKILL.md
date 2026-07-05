---
name: tdd
description: "Test-first variant of implement: understand the desired behavior, write a failing test, make it pass, then simplify."
user-invocable: true
argument-hint: "<task reference or behavior> e.g. 'LIN-123' or 'retry logic for API client'"
---

# Test-Driven Development

Goal: write the failing test first, then make it pass.

## Workflow

### 1. Understand

- Read the request, task, issue tracker item, plan, spec, and relevant code as available.
- Identify the desired behavior, current function signatures, return values, data shapes, failure paths, and checks.
- If a spec exists, note decisions, behavior that must not change, and test plan.
- Ask before writing tests when missing information would change behavior, what to change, safety, function signatures, return values, data shapes, or checks.

### 2. Red

- Write the smallest failing test that proves the desired behavior or reproduces the bug.
- Run it and confirm it fails for the expected reason.

### 3. Green

- Write the minimum implementation needed to pass the test.
- Preserve existing function signatures, return values, data shapes, and user-visible behavior unless the task explicitly changes them.
- Add failure-path tests where they matter.

### 4. Refine

- Simplify code and tests while they keep passing.
- Run the focused checks first, then wider project checks, before finishing.
- Report the test that failed before the fix, passed after the fix, and final checks.

## Rules

- Do not write implementation code before a failing test for the behavior.
- If an assumption is low-risk, make it explicit and keep moving.
- Tests describe behavior, not implementation details.
- Prefer real boundaries over mocks when practical.
- Skip TDD for documentation, formatting, or non-behavioral scaffolding work.
