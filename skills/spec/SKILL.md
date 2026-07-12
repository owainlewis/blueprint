---
name: spec
description: "Turn an idea, problem, or rough brief into one written implementation decision. Use for brainstorming and design before breaking work into tickets."
user-invocable: true
argument-hint: "<idea, problem, brief, issue, or repo path>"
---

# Spec

Turn an unclear idea into one reviewable written decision.

1. Read the request, referenced material, and relevant code. Learn existing behavior and constraints before proposing a design.
2. Explore the problem with the user. Surface meaningful options and tradeoffs. Ask one question at a time only when the answer changes behavior or design; include a recommended answer.
3. Decide what, why, and how. Choose defaults where two implementations would behave differently.
4. Write `docs/<feature-slug>/spec.md` with the template below. Omit sections that do not apply.
5. Stop for human review. Do not create tickets or implement the work.
6. When the user explicitly approves the spec, change its status from `Draft` to `Approved`. Make no other changes unless the user asks.

## Rules

- Write one spec for one coherent decision scope.
- Describe observable behavior before implementation detail.
- Match existing architecture unless the spec explicitly changes it.
- Record constraints, invariants, interfaces, data shapes, and failures that future agents must preserve.
- Check current documentation before pinning a dependency, runtime, API, or framework behavior.
- Keep unresolved questions visible. Do not hide them behind vague language.
- Exploration that produces no decision does not require a spec.

## Template

```markdown
# <Title>

**Status:** Draft

## Summary
What we are building, why it matters, and the proposed approach.

## Goals
- Observable results this work must achieve.

## Non-goals
- Related problems this work will not solve.

## Requirements
- Testable behavior and constraints.

## Design
Components, data flow, boundaries, and important implementation choices.

## Interfaces and data
APIs, commands, events, schemas, state transitions, or compatibility requirements.

## Error behavior
Expected behavior for invalid input, failures, retries, and partial completion.

## Decisions and tradeoffs
Chosen options, rejected alternatives, and why.

## Test strategy
How the requirements and important failure paths will be proved.

## Rollout and risks
Migration, compatibility, operational risk, backout, or release constraints.

## Open questions
Decisions still needed, with a recommended answer and owner when known.
```
