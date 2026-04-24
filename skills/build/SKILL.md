---
name: build
description: "Implement one task or scoped change: make the change, add valuable tests, and verify it works."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'Task 2 from user-auth' or 'add rate limiting to the API'"
---

# Build

## When to use

- Implementing a single task from a plan
- Executing a clear, scoped behavioral change
- Delivering one focused vertical slice

## Process

1. Read the task, spec, and relevant code before editing.
2. If the scope is vague or too large for one pass, stop and clarify or break it down.
3. Work in the repo's normal git context.
4. Implement the smallest useful slice that satisfies the task.
5. If the task has several parts, work in small runnable steps and verify each step before continuing.
6. Add tests when behavior changes, bugs are fixed, or interfaces change.
7. Run the strongest project checks available: the full test suite when practical, plus any task-specific verification.

## Verification

- The behavior matches the task or request
- New or changed behavior is covered by tests where it matters
- Tests pass
- Task-specific verification passes
- No unrelated scope was added

## Rules

- One task at a time.
- Make the smallest safe change that fully solves the task.
- Preserve contracts unless the task explicitly changes them. If a contract must change, call it out clearly.
- Handle failure paths explicitly instead of leaving them implicit.
- Do not bundle several independent changes into one generation when they can land as working steps.
- If the request is vague, oversized, or mixes multiple tasks, stop and clarify or break it down.
- Do not hide missing verification. If you could not run something important, say so.
- Do not use this skill as an excuse for unrelated refactors.
