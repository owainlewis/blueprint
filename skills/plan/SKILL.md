---
name: plan
description: "Turns a reviewed spec or decided brief into ordered tasks for separate agent runs. Use for implementation tasks, tracker tickets, or useful milestones. Do not use for one coding task or its short execution outline."
user-invocable: true
argument-hint: "<spec, brief, issue, or request>"
disable-model-invocation: true
---

# Plan

Use this skill only when the user explicitly selects it, or when an already selected Blueprint workflow requires its instructions. Do not select it from a general task match. For a required dependency, read its linked `SKILL.md` directly as part of the selected workflow; do not use a model-invoked skill command that the client blocks.

Create tasks that a new agent can finish without making product or technical decisions. Every task and milestone must be a vertical slice: a usable outcome that runs through the required layers and has acceptance checks. Split by working result, not by file, layer, or team boundary.

## Process

1. Read the source, repository instructions, and relevant code.
2. Stop and return to `/spec` if an unresolved choice would change behavior, interfaces, data, security, scale, performance, compatibility, operations, cost, or proof.
3. Split the work into tasks that each deliver working behavior, fit one agent run, and produce one focused pull request.
4. Keep shared contracts in one task. Do not make two tasks answer the same question independently.
5. Separate refactoring when it would hide a behavior change.
6. Order tasks by dependency. Group tasks into milestones when useful. Each milestone delivers a usable end-to-end result, with acceptance checks and dependencies. Do not use milestones such as “database”, “backend”, or “frontend”.
7. Return the plan in chat. Create tracker tickets only when the user asks. Never write a plan document.
8. Stop after planning. Do not implement.

For example, “add a task and see it after a restart” includes CLI input, validation, storage, output, and tests in one task. A later milestone could deliver “manage unfinished tasks” through add, list, and complete slices. Name the milestone's observable result and how to prove the whole result works.

## Write for two readers

Each task is read by a human and executed by an agent.

The first sections must let a human understand the task in under a minute. State the concrete problem, the result, and why it matters in everyday words. Do not use requirement IDs, implementation details, undefined project terms, or acronyms unfamiliar to the intended readers there.

Put task-specific decisions, interfaces, failure rules, and security constraints in Agent notes. Link the spec or decided source for shared architecture and full requirement definitions. Use a repository path or URL that will resolve from the published ticket, and pin the decided version when later edits could change the contract. If no durable source exists, include the required shared decisions in Agent notes. Do not copy the whole source into every ticket.

A task stands alone when its purpose, boundary, dependencies, non-negotiable decisions, and proof are clear. It does not need to repeat background that the linked source already explains.

## Task shape

Use this compact shape. Omit optional sections that add no information.

```markdown
## <Plain action and result>

### What are we building?
In one to three short sentences, say what is wrong or missing and what will work after this task.

### Why?
In one or two short sentences, explain the practical value to a user, operator, or developer.

### Done when
- Three to seven observable results.

### How to check
Exact commands and required manual checks.

### Agent notes
- Depends on: <task titles, or None>
- Source: <durable spec, brief, issue, or request path/URL, pinned when needed>
- Only the definitions, decisions, constraints, and failure behavior specific to this task.

### Out of scope
- Related work this task is likely to absorb by mistake.
```

## Writing rules

- Use a short title that names an action and result.
- Use familiar words and specific verbs.
- Define a necessary technical term where it first appears. Otherwise replace it with observable behavior.
- Say `sending the same event twice creates one reply`, not `prove idempotency`.
- Say `the answer is supported by the cited document`, not `prove grounding`.
- Do not add user stories by default. Add one only when it clarifies product behavior that the first two sections do not.
- Keep implementation mechanics out of the first two sections.
- Keep task-specific implementation choices in Agent notes. Leave interchangeable local mechanics to the implementing agent.
- Preserve applicable `AC-n`, `REQ-n`, and `INV-n` references in Done when or Agent notes without making a reader decode them to understand the task.
- Aim for 250 to 500 words per ticket. Exceed 700 only when the extra text is required to prevent an unsafe or incompatible implementation. Otherwise split the task or link the shared source.
- Do not repeat a fact in several sections.
- Do not use slogans, metaphors, filler, or vague claims such as `robust`, `seamless`, `comprehensive`, and `future-proof`.

## Boundaries

- Do not split one working behavior into separate file or technical-layer tasks.
- Do not create scaffolding or cleanup tasks without a checked outcome.
- Do not hide unresolved decisions inside implementation tickets.
- Keep each task small enough for one agent run and one focused review.
- In Done when, state observable behavior and any internal rule that must hold.
- In How to check, include exact commands and manual proof when automation cannot cover the behavior.
- If the source uses requirement IDs, keep each ID attached to the same rule. Do not renumber or reuse it.

Before returning the plan, read each task twice:

1. Human pass: can someone explain what will change and why after reading only the title and first two sections?
2. Agent pass: can a fresh agent find the source, identify dependencies and fixed decisions, implement the task, and prove it without asking a product or architecture question?

Delete repeated background after both passes succeed.

## Return

Return the ordered tasks, any useful milestones with acceptance checks, their dependencies, and any decision that still
blocks implementation. Do not add a separate summary that repeats the tasks.
