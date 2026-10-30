---
name: spec
description: "Writes a spec for one feature: a short PRD (problem and user stories) plus the technical design an agent builds from. Use when decisions must be settled before building. The spec is the ticket."
user-invocable: true
argument-hint: "<feature, change, issue, or brief>"
disable-model-invocation: true
---

# Spec

Fill in this template for one feature. The top half says what to build and for whom. The bottom half says how, for the agent that builds it. The spec is the ticket.

## Process

1. Read the request, the code it touches, `REQUIREMENTS.md`, and `ARCHITECTURE.md`.
2. Ask the user about each choice that changes behavior, data, interfaces, or security. Give your recommended answer with each question.
3. Copy the template into the ticket, or into `docs/<feature-slug>/spec.md` if there is none, and fill every section. Write "None" where a section has nothing.
4. Stop when another agent could build it without guessing a decision.

## Template

```markdown
# <Feature name>

Status: Proposed | Accepted | Delivered (<PR link>)

## Problem

<Who is affected, what goes wrong for them today, and why it matters. Two to four sentences.>

## User stories

<The stories from REQUIREMENTS.md this feature delivers, cited by REQ-n, plus any
new ones in the same form: As a <user>, I want to <action>, so that <benefit>.
Say what the user sees on success, denial, invalid input, and failure.>

## Technical design

<A Mermaid diagram of the main flow: the parts this change touches, what moves
between them, and the order. It is for the human reviewer, so keep it to one
screen and label every arrow.>

<What the agent needs to build it: the modules and interfaces it changes, data
and schema changes, API contracts, migrations, and where the tests go.
For each decision a reviewer could question, give the choice, the reason, and
the cost. Name any change to ARCHITECTURE.md.>

## Acceptance

| ID | Done when | How to check |
|---|---|---|
| AC-1 | <Observable result> | <Test, command, or browser flow> |

## Out of scope

<What this change does not do.>

## Open decisions

<Each unanswered question, your recommended answer, and whether it blocks delivery.>
```

## Rules

- Keep existing `AC-n`, `REQ-n`, and `INV-n` IDs. Never reuse or renumber them.
- Link to requirements and architecture instead of copying them.
- Every spec has a diagram. Check that it agrees with the text.
- For code that does not exist yet, describe the check as a scenario and expected result.
- After delivery, set the status to Delivered and link the PR.

## Return

Report the spec location, the main decision and its tradeoff, and any blocking question.
