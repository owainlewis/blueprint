---
name: plan
description: "Splits a spec or brief into small, agent-ready vertical slices that each fit one pull request. Returns tasks in chat or publishes them to GitHub Issues, Linear, Jira, or local Markdown when asked."
user-invocable: true
argument-hint: "<spec, brief, issue, or request>"
disable-model-invocation: true
---

# Plan

Split decided work into vertical slices that each deliver working behavior, end to end, in one pull request and one fresh agent session. Split by result, never by layer: "add a task and see it after a restart" is one slice covering input, storage, and output, not three.

## Steps

1. Read the spec, the repository instructions, and the code it touches. If a decision that changes behavior is missing, return to [spec](../spec/SKILL.md).
2. Design slice 1 as a thin tracer bullet: the smallest end-to-end path through every layer that proves the plumbing and unlocks parallel follow-up slices.
3. Write each task with the template below. Keep shared contracts in one task, and put refactoring in its own task when it would hide a behavior change.
4. Order tasks by dependency and show which slices can run in parallel. Group into milestones only when a milestone is itself a usable result.
5. Return the plan in chat. Do not write a plan file or start building unless asked.
6. If the user asks to create tracker tickets (GitHub Issues, Linear, Jira, or local Markdown), first preview the slice titles, one-line outcomes, and `Blocked by` dependencies for approval. Once approved, check for existing tickets to avoid duplicates, then create tickets in dependency order so real issue IDs (`#42`, `ENG-104`, `PROJ-88`) wire into native blocking or parent/sub-issue links.

## Template

```markdown
## <Action and result, in plain words>

### What are we building?
<1–3 sentences: what is missing today and what works after this task.>

### Why?
<1–2 sentences on the value to a user or developer.>

### Done when
- <3–7 results a person could check in the running app or with a command. Keep AC-n, J-n, and REQ-n IDs when present.>

### How to check
<Exact commands, and any manual or browser check.>

### Agent notes
- Blocked by: <issue IDs or task titles, or None>
- Source: <link to the spec or section>
- Starting pointers: <existing modules, symbols, or patterns to follow>
- <Key decisions, invariants, and failure rules specific to this task. Repeat critical constraints concisely when publishing to an external tracker.>

### Out of scope
- <Nearby work this task must not absorb.>
```

## Rules

- Write in plain, simplified technical English. Keep every ticket short, concrete, and free of filler.
- A human should understand the task from the title and first two sections alone. Keep IDs and implementation detail out of them.
- Say what happens, not jargon: "sending the same event twice creates one reply", not "prove idempotency".
- Each Done when line names an action and what you see. "Moving a reel to a new status moves it to that column, and it stays there after a refresh" belongs. "Looks better" does not.
- Aim for 250 to 500 words per task. If a task needs more, split it.
- A task is ready when a fresh agent can finish it without asking a product or design question.

## Return

The ordered tasks, their dependency map (`Blocked by` and parallelizable slices), any created ticket links, and any decision that still blocks building.
