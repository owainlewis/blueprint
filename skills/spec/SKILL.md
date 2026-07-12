---
name: spec
description: "Turn decided feature direction into a written implementation spec at docs/<feature-slug>/spec.md, then pause for human review. Use after broad architecture is settled."
user-invocable: true
argument-hint: "<idea, problem, brief, issue, or repo path>"
---

# Spec

Turn decided feature direction into one reviewable implementation decision.

1. Read the request, referenced material, and relevant code. Learn existing behavior and constraints before proposing a design.
2. Clarify behavior, interfaces, data, errors, and implementation constraints with the user. Ask one question at a time only when the answer changes the spec; include a recommended answer. Stop if broad architecture is still unclear or expensive to reverse.
3. Decide what, why, and how. Choose defaults where two implementations would behave differently.
4. Write `docs/<feature-slug>/spec.md` with the template below. Omit sections that do not apply.
5. Stop for human review. Do not plan or implement the work.
6. When the user explicitly approves the spec, first resolve every open question that affects behavior, interfaces, data, errors, or scope. Questions explicitly deferred outside the spec may remain. Then change its status from `Draft` to `Approved`.

## Rules

- Write one spec for one coherent decision scope.
- Treat broad architecture and cross-team tradeoffs as prior decisions, not hidden work inside the spec.
- Describe observable behavior before implementation detail.
- Match existing architecture unless the spec explicitly changes it.
- Record constraints, invariants, interfaces, data shapes, and failures future agents must preserve.
- Check current documentation before pinning a dependency, runtime, API, or framework behavior.
- Keep unresolved questions visible. Do not hide them behind vague language.
- Exploration that produces no decision does not require a spec.

## Template

```markdown
# <Title>

Status: Draft

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
