---
name: plan
description: "Break a spec, brief, issue tracker item, or user request into agent-sized tasks, using phases and milestones only when they clarify larger work, delivered to exactly one destination."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

Turn a spec or user-provided input into tasks for humans, issue trackers, or AI agents. For larger efforts, first define phases with clear goals; for simple work, skip phases and go straight to tasks. Each task must carry enough context to execute independently without scripting routine implementation choices.

## Workflow

### 1. Ground in the input

- Use `$ARGUMENTS`, `docs/<feature-slug>/spec.md`, an issue tracker item, or the current brief as the source input.
- Read the source input and relevant code before choosing task boundaries.
- Ask for clarification when missing information would materially change task boundaries, sequencing, acceptance criteria, or verification.
- If the input is too vague, stop instead of fabricating tasks.

### 2. Decide whether phases help

Use phases only when they make the work clearer.

- Skip phases for one-off bugs, small features, and short task lists.
- Use phases for multi-system work, long delivery paths, release planning, or anything that needs milestones.
- When using phases, make each phase one clear outcome, such as "interface exists", "state persists", or "integration works".
- Order phases by dependency, risk, and learning value.
- Name each phase with a short title and one-sentence goal.
- Use milestones for phases when delivering to an issue tracker and the tracker supports them.
- Keep phases outcome-based, not team-based or layer-based. Prefer "users can complete the workflow" over "frontend work".
- If the user asks for a whole project plan, include release, operations, migration, documentation, training, or rollout phases only where relevant to that project.

### 3. Split the work into tasks

- Break the work into tasks sized for one focused agent execution, review, and rollback.
- Prefer vertical slices over layer-by-layer plans.
- Order tasks by dependency and risk.
- Surface shared decisions once before the affected tasks.
- If phases are used, assign each task to exactly one phase.
- Tasks with unmet dependencies should name the blocking task or phase.

### 4. Deliver the plan

Specs are durable; plans are transport. Deliver the tasks to exactly one destination, never two:

- **Tracker**: when the user asks for issues or the repo documents an issue-driven loop, create milestones for phases when the tracker supports them, then file one issue per task and write no plan doc. The issues are the plan. Apply the repo's documented labels: tasks meeting the definition of ready get the agent-ready label; tasks with unmet dependencies get the blocked label with a link to the blocking issue.
- **Doc**: write `docs/<feature-slug>/plan.md` when there is a clear feature directory.
- **Chat**: return the plan inline otherwise.

For each task, include:

- Phase, when phases are used
- Phase goal, when phases are used
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
- Do not create "phase issues" unless a phase has its own concrete deliverable. Use milestones or headings for phases; use issues for executable tasks.
