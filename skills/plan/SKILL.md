---
name: plan
description: "Break a spec into small, implementation-ready tasks. Use when a spec exists and the work needs execution order, acceptance criteria, and verification."
user-invocable: true
argument-hint: "<feature-name> e.g. 'user-auth'"
---

# Plan

## When to use

- A spec exists and the work needs implementable tasks
- The scope is too large to execute safely in one pass
- Multiple tasks or dependencies need ordering

## Process

1. Use the feature name to read `docs/<feature-name>/spec.md`.
2. Write `docs/<feature-name>/plan.md`.
3. Break the work into small vertical slices. Each task should leave the system in a working state.
4. For each task, include:
   - Context
   - Acceptance Criteria
   - Verify
5. Order tasks by dependency and risk. Leave no decisions to the implementer.

## Verification

- The plan is saved to `docs/<feature-name>/plan.md`
- Each task is small enough for one focused session
- Acceptance criteria describe outcomes, not implementation steps
- Verify commands are concrete
- Dependency order is clear

## Rules

- Plan the smallest safe change that fully solves the problem.
- Call out contract changes, compatibility risks, and migrations explicitly.
- Prefer vertical slices over layer-by-layer plans.
- Skip planning when the change is already tiny and decision-complete.
- If a task needs more than a few acceptance criteria, split it.
- Include error behavior in the task that owns it.
