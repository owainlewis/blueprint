---
name: design
description: "Designs what to build and how it should work, including requirements, acceptance criteria, interfaces, data, errors, technical choices, constraints, risks, and scope. Use when the user asks to design or architect a feature, write a spec or design doc, define requirements, or resolve important product or technical decisions before implementation."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

1. Read the request, repository instructions, relevant code, and linked material.
2. Resolve choices that would change behavior, interfaces, data, errors, security, operations, or tests. Ask only questions whose answers materially change the design. Recommend an answer when asking.
3. Write `docs/<feature-slug>/design.md` using the shape below. Keep it short and omit sections that do not apply.
4. Stop for human review. Do not plan or implement.

```markdown
# <Title>

## What and why
The problem, desired outcome, and users affected.

## Requirements
- Observable behavior and constraints.

## Acceptance criteria
- Testable conditions that prove the work is complete.

## Design
The chosen approach, important components, data flow, and technical choices.

## Interfaces and data
APIs, commands, events, schemas, compatibility, or migration requirements.

## Failure behavior
Invalid input, partial failure, recovery, and operational limits.

## Test approach
How each important requirement will be proved.

## Risks
- Risk and mitigation.

## Out of scope
- Related work this design does not include.
```

Prefer one clear recommendation over a catalogue of options. Record rejected options only when the tradeoff matters later.
