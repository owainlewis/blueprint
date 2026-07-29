---
name: plan
description: "Turns a reviewed design or brief into ordered tasks for separate agent runs. Use for implementation tasks, tracker tickets, or useful milestones. Do not use for one coding task or its short execution outline."
user-invocable: true
argument-hint: "<design, brief, issue, or request>"
---

# Plan

Turn decided work into ordered tasks for separate agent runs.

## Workflow

1. **Read**
   - Read the source, repository instructions, and relevant code.
   - Identify the outcome, fixed decisions, constraints, and proof.

2. **Check readiness**
   - Stop and return to design if a product or technical choice remains open.
   - Continue only when a new agent could complete each task without asking those questions.

3. **Create tasks**
   - Make each task fit one agent run and one focused pull request.
   - Make each task deliver working behavior and its proof.
   - Separate refactoring when it would hide a behavior change. Keep small local cleanup only when it makes that change easier to review.
   - Use the task template below.

4. **Order tasks**
   - Put dependencies before the work that needs them.
   - Add a milestone only when it creates a useful delivery or review point.

5. **Publish and stop**
   - Return the plan in chat by default.
   - Create tracker tickets only when the user asks.
   - Do not write a plan document or implement the work.

## Task template

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

## Rules

- Do not split one piece of working behavior into separate file or technical-layer tasks.
- Do not create scaffolding or cleanup tasks without a checked outcome.
- Do not hide unresolved decisions inside implementation tickets.
- Give each task enough context to stand alone.
