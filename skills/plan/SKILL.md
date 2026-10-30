---
name: plan
description: "Splits a spec into small tasks, each a working slice an agent can finish in one pull request. Use when a spec is too big for one PR, or to create tracker tickets."
user-invocable: true
argument-hint: "<spec, brief, issue, or request>"
disable-model-invocation: true
---

# Plan

Split decided work into tasks that each deliver something that works, end to end, in one pull request. Split by result, never by layer: "add a task and see it after a restart" is one task covering input, storage, and output, not three.

## Steps

1. Read the spec, the repository instructions, and the code it touches. If a decision is missing, return to [spec](../spec/SKILL.md).
2. Write each task with the template below. Keep shared contracts in one task, and put refactoring in its own task if it would hide a behavior change.
3. Order tasks by dependency. Group them into milestones only when a milestone is itself a usable result.
4. Return the plan in chat. Create tracker tickets only if the user asks. Do not write a plan file or start building.

## Template

```markdown
## <Action and result, in plain words>

### What are we building?
<One to three sentences: what is missing today and what will work after this task.>

### Why?
<One or two sentences on the value to a user or developer.>

### Done when
- <Three to seven results someone can see or test. Keep AC-n and REQ-n IDs.>

### How to check
<Exact commands, and any manual check.>

### Agent notes
- Depends on: <task titles, or None>
- Source: <link to the spec section>
- <Decisions and failure rules specific to this task. Link the spec for the rest.>

### Out of scope
- <Nearby work this task might absorb by mistake.>
```

## Rules

- A human should understand the task from the title and first two sections alone. Keep IDs and implementation detail out of them.
- Say what happens, not the jargon: "sending the same event twice creates one reply", not "prove idempotency".
- Aim for 250 to 500 words a task. If it needs more, split it.
- A task is ready when a fresh agent could finish it without asking a product or design question.

## Return

The ordered tasks, their dependencies, and any decision that still blocks building.
