---
name: plan
description: "Breaks a reviewed design or brief into ordered, agent-ready tasks, tickets, and optional milestones. Use when the user asks to break a feature or project into implementation tasks, create implementation tickets or issues from a design, brief, or project, define milestones, or prepare work for multiple agent runs. Do not use for one ticket or the short execution plan inside one coding task."
user-invocable: true
argument-hint: "<design, brief, issue, or request>"
---

# Plan

## Workflow

1. Read the source, repository instructions, and relevant code.
2. Stop and return to design if product or technical choices remain open.
3. Break the work into vertical, outcome-based tasks small enough for one agent run. Order them by dependency. Add milestones only when they create a useful delivery or review boundary.
4. Return the plan in chat by default. Create tracker tickets only when the user asks. Never write a plan document.
5. Stop after planning. Do not implement.

Each task must stand alone:

```markdown
## <Task title>

### Outcome
The working result.

### Context
What a new agent needs with no session history.

### Constraints
Decisions and behavior that must not change.

### Acceptance criteria
- Testable condition.

### Checks
Exact commands and any required manual verification.

### Out of scope
Related work this task must not absorb.
```

## Boundaries

- Do not split by file or technical layer when one vertical slice can deliver working behavior.
- Do not create scaffolding or cleanup tasks without a checked outcome.
- Do not hide unresolved decisions inside implementation tickets.
