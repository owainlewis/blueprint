---
name: plan
description: "Turns an approved design or decided brief into ordered tasks for separate agent runs. Use for implementation tasks, tracker tickets, or useful milestones. Do not use for one coding task or its short execution outline."
user-invocable: true
argument-hint: "<design, brief, issue, or request>"
---

# Plan

## Workflow

1. Read the source, repository instructions, and relevant code.
2. Stop and return to design if product or technical choices remain open.
3. Break the work into tasks that each deliver working behavior. Each task must:
   - Fit one agent run.
   - Produce one focused pull request.
   - Let a reviewer understand the outcome, behavior, and proof without separating unrelated work.
4. Separate refactoring when it would hide the behavior change. Small local cleanup may stay when it makes the change easier to review.
5. Order tasks by dependency. Add milestones only when they create a useful delivery or review boundary.
6. Return the plan in chat by default. Create tracker tickets only when the user asks. Never write a plan document.
7. Stop after planning. Do not implement.

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

- Do not split one piece of working behavior into separate file or technical-layer tasks.
- Do not create scaffolding or cleanup tasks without a checked outcome.
- Do not hide unresolved decisions inside implementation tickets.
