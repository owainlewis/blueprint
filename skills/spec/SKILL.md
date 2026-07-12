---
name: spec
description: "Write a short implementation spec at docs/<feature-slug>/spec.md and pause for review. Use when behavior, interfaces, data, or errors need decisions before coding."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Spec

1. Read the request, relevant code, and linked material.
2. Resolve decisions that would change behavior, interfaces, data, errors, or tests. Ask one question at a time and recommend an answer. Stop if broad architecture is still undecided.
3. Write `docs/<feature-slug>/spec.md` using the template below. Keep it short and omit sections that do not apply.
4. Stop for human review. Do not plan or implement.

```markdown
# <Title>

## Summary
What we are building, why, and the chosen approach.

## Requirements
- Observable, testable behavior.

## Design
Important components, data flow, and implementation decisions.

## Interfaces and data
APIs, commands, events, schemas, or compatibility requirements.

## Error behavior
What happens on invalid input, failure, or partial completion.

## Test plan
How the requirements will be proved.

## Out of scope
- Related work this spec does not include.
```
