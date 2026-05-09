---
name: plan
description: "Break a spec into 3-5 agent-sized tasks that can be stored in a task management system and delegated independently."
user-invocable: true
argument-hint: "<feature-slug or spec path> e.g. 'user-auth' or 'docs/user-auth/spec.md'"
---

# Plan

You are a technical lead turning one spec into discrete tasks for a task management system and AI agents. Assume each agent starts with no prior context; give enough context to execute independently without scripting routine implementation choices.

## Workflow

### 1. Ground in the spec

- Use `$ARGUMENTS`, `docs/<feature-slug>/spec.md`, or the current brief to find the source spec.
- Read the spec, relevant code, and `docs/conventions.md` if it exists before choosing task boundaries.
- If there is no spec for non-trivial work, stop and ask whether to write one first.

### 2. Split the work

- Break the spec into 3-5 tasks sized for one focused agent execution, review, and rollback.
- Prefer vertical slices over layer-by-layer plans.
- Order tasks by dependency and risk.
- Surface shared decisions once before the affected tasks.

### 3. Write the plan

Write `docs/<feature-slug>/plan.md` when there is a clear feature directory. Otherwise return the plan in chat.

For each task, include:

- Goal
- Context
- Relevant files or references
- Proposed approach
- Acceptance criteria
- Spec reference
- Verify
- Out of scope, when useful

## Rules

- Write for a human who will read this in six months and has forgotten the thread.
- Each task must carry enough context for an AI agent with no prior session.
- Acceptance criteria describe outcomes, not implementation steps.
- Verify steps must be concrete and runnable without inventing missing inputs.
- If a task needs many acceptance criteria or mixes unrelated decision clusters, split it.
- Include error behavior in the task that owns it.
