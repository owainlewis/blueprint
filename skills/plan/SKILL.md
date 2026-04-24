---
name: plan
description: "Break a project, phase, spec, or rough request into small agent-ready tasks with acceptance criteria and verification."
user-invocable: true
argument-hint: "<project, phase, spec, or feature-name> e.g. 'user-auth'"
---

# Plan

## When to use

- A project, phase, or feature needs implementable tasks
- The scope is too large to execute safely in one pass
- Multiple tasks or dependencies need ordering

## Process

1. Use `$ARGUMENTS`, the current brief, or `docs/<feature-name>/spec.md` as the source.
2. Read the relevant code and docs before choosing task boundaries.
3. Write `docs/<feature-name>/plan.md` when there is a clear feature directory. Otherwise return the plan in chat.
4. Break the work into tasks small enough for:
   - one focused agent execution
   - a reviewer to catch problems
   - cheap debugging or rollback
5. For each task, include:
   - Goal
   - Context
   - Proposed Approach
   - Acceptance Criteria
   - Spec: `none`, `short`, or `full`
   - Verify
   - Out of Scope, when useful
6. Order tasks by dependency and risk. Surface shared decisions once, before the affected tasks.

## Verification

- The plan is saved or returned in the requested location
- Each task fits the execution, review, and rollback limits
- Acceptance criteria describe outcomes, not implementation steps
- Each task says whether it needs a spec
- Verify commands are concrete
- Dependency order is clear

## Rules

- Plan the smallest safe change that fully solves the problem.
- Call out contract changes, compatibility risks, and migrations explicitly.
- Prefer vertical slices over layer-by-layer plans.
- Use phases only when the work naturally breaks into coherent milestones. Otherwise use a plain task list.
- Skip planning when the change is already tiny and decision-complete.
- Each task should carry the minimum setup context needed to execute it without hidden assumptions.
- Every verify step must be runnable without inventing missing inputs. If it needs a fixture, payload, or prior ID, say exactly how to get it.
- If a task needs more than a few acceptance criteria, split it.
- If a task mixes unrelated decision clusters, split it.
- If two split tasks need the same design decision, move that decision up or redraw the boundary.
- Include error behavior in the task that owns it.
