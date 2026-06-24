---
name: plan
description: "Break a spec, brief, issue tracker item, or user request into agent-sized tasks, delivered to exactly one destination: tracker issues, a plan doc, or chat."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

Turn a spec or user-provided input into tasks for humans, issue trackers, or AI agents. Give each task enough context to execute independently without scripting routine implementation choices.

## Workflow

### 1. Ground in the input

- Use `$ARGUMENTS`, `docs/<feature-slug>/spec.md`, an issue tracker item, or the current brief as the source input.
- Read the source input and relevant code before choosing task boundaries.
- Ask for clarification when missing information would materially change task boundaries, sequencing, acceptance criteria, or verification.
- If the input is too vague, stop instead of fabricating tasks.

### 2. Split the work

- Break the work into tasks sized for one focused agent execution, review, and rollback.
- Prefer vertical slices over layer-by-layer plans.
- Order tasks by dependency and risk.
- Surface shared decisions once before the affected tasks.

### 3. Deliver the plan

Specs are durable; plans are transport. Deliver the tasks to exactly one destination, never two:

- **Tracker**: when the user asks for issues or the repo documents an issue-driven loop, file one issue per task and write no plan doc. The issues are the plan. Apply the repo's documented labels: tasks meeting the definition of ready get the agent-ready label; tasks with unmet dependencies get the blocked label with a link to the blocking issue.
- **Doc**: write `docs/<feature-slug>/plan.md` when there is a clear feature directory.
- **Chat**: return the plan inline otherwise.

For each task, include:

- Goal
- Context
- Relevant files or references
- Proposed approach
- Acceptance criteria
- Source reference
- Verify
- Out of scope, when it prevents accidental expansion

## Rules

- Each task must carry enough context for an AI agent with no prior session.
- Acceptance criteria describe outcomes, not implementation steps.
- Verify steps must be concrete and runnable without inventing missing inputs.
- If a task needs many acceptance criteria or mixes unrelated decision clusters, split it.
- Include error behavior in the task that owns it.
