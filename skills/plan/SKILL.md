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
6. Return the plan in chat by default. Create tracker tickets only when the user asks. When tickets are separate, copy every needed decision and definition into each ticket. Do not rely on a plan introduction or sibling ticket. Never write a plan document.
7. Stop after planning. Do not implement.

## Task writing

Treat each task as a cold handoff to a junior engineer with repository access. Assume they have not seen the conversation, design process, or other tickets. Give them enough purpose, system context, decisions, and proof to complete the work without asking for missing product or technical context. Link the source design for detail, not as a substitute for orientation.

Name the current behavior, the affected person, the change, and its value before implementation detail. Define project-specific roles, records, states, and acronyms the first time they appear. Put database, framework, and code details in Context or Constraints.

Use short, concrete sentences. Prefer familiar words and specific verbs. Do not use slogans, metaphors, filler, marketing language, or vague claims such as "robust", "seamless", "comprehensive", and "future-proof".

Use one user story for each distinct goal that the task serves. Operators, maintainers, and developers are valid users when they experience the problem. Omit the section when no honest user goal exists. Do not invent a story for every technical requirement.

For example, explain that completed tasks currently keep every diagnostic event forever and can make the database grow without limit. Then use the story: `As an operator, I want old diagnostic events removed automatically so that storage stays bounded without losing task results.` Put retention timing, batch deletion, and database rules in Constraints.

For a migration, explain the old model, the new model, how records map between them, and why existing users need the move. Define names such as `Definition`, `Run`, `Job`, and `Runner` from the source material. Never use a list of new names as the explanation. Then state the user goal plainly: `As an operator, I want my existing schedules and audit history to keep working after the new scheduling model replaces the old one.` Put cutover, restart, compatibility, and legacy-data rules in Constraints.

Each task must stand alone:

```markdown
## <Task title>

### Summary
In two to four sentences, explain the current behavior, who it affects, what will change, and why that change matters.

### User stories
- As a <role>, I want <capability> so that <benefit>.

### Outcome
The useful behavior that will work when the task is complete.

### Context
Define the relevant parts of the system, prior work, dependencies, and source decisions that a new agent needs with no session history.

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
- Use a short title that names the action and result in plain words, such as `Remove expired event details automatically`. Do not use only component names or an internal project label.
- Use plain words in the title, Summary, User stories, and Outcome. Define any project term needed there.
- Keep implementation steps out of user stories and acceptance criteria. State observable behavior and proof instead.
- Give each section one job. Summary orients the reader. User stories state people's goals. Outcome states the working result. Context explains the system and dependencies. Some meaning will overlap, but do not copy sentences or add repetition that does not help the reader.
- Reread each task alone. A cold reader must be able to explain why it exists, identify the relevant system boundary, implement the decided behavior, and prove it works. Add anything missing before returning the plan.
