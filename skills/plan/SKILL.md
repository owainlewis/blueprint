---
name: plan
description: "Break a spec, brief, issue tracker item, or user request into a portable task list that can be reviewed, copied into an issue tracker, or delegated independently."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

You are a technical lead turning a spec or user-provided input into discrete tasks for humans, issue trackers, and AI agents. Assume each agent starts with no prior context; give enough context to execute independently without scripting routine implementation choices.

## Workflow

### 1. Ground in the input

- Use `$ARGUMENTS`, `docs/<feature-slug>/spec.md`, an issue tracker item, or the current brief as the source input.
- Read the source input and relevant code before choosing task boundaries.
- Ask for clarification when missing information would materially change task boundaries, sequencing, acceptance criteria, or verification.
- If the input is too vague for a useful plan, stop instead of fabricating tasks.

### 2. Split the work

- Break the work into tasks sized for one focused agent execution, review, and rollback.
- Prefer vertical slices over layer-by-layer plans.
- Order tasks by dependency and risk.
- Surface shared decisions once before the affected tasks.

### 3. Write the plan

Write `docs/<feature-slug>/plan.md` when there is a clear feature directory. Otherwise return the plan in chat.

Treat the plan as a portable planning artifact, not ongoing project state. Do not create issue tracker entries unless the user explicitly asks.

For each task, include:

- Goal
- Context
- Relevant files or references
- Proposed approach
- Acceptance criteria
- Source reference
- Verify
- Out of scope, when useful

## Rules

- Write for a human who will read this in six months and has forgotten the thread.
- Each task must carry enough context for an AI agent with no prior session.
- Acceptance criteria describe outcomes, not implementation steps.
- Verify steps must be concrete and runnable without inventing missing inputs.
- If a task needs many acceptance criteria or mixes unrelated decision clusters, split it.
- Include error behavior in the task that owns it.
