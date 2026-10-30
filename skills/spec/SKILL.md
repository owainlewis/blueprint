---
name: spec
description: "Writes one feature or major change as a spec from a fixed template: a short version of the product requirements for this feature, plus the technical design an agent needs to build it. Use when consequential decisions must be settled before delivery. The spec is the ticket."
user-invocable: true
argument-hint: "<feature, change, issue, or brief>"
disable-model-invocation: true
---

# Spec

Fill in the template below for one coherent change. The first half is a cut-down PRD for this feature: the problem and its user stories. The second half is the technical design an agent needs to build it. The spec is the ticket.

## Process

1. Read the request, repository instructions, `REQUIREMENTS.md`, `ARCHITECTURE.md`, and the code the change touches. Verify every claim about current behavior.
2. Ask the user about each choice that could change behavior, data, interfaces, security, compatibility, cost, or proof. Give your recommended answer with each question. Leave reversible local mechanics to implementation.
3. Copy the template into the supplied source (an issue or document) or, with none, into `docs/<feature-slug>/spec.md`. Fill every section. Write "None" in a section that has nothing.
4. Stop when a fresh agent could build it without inventing a consequential decision. Do not plan tasks or write code.

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
- Link shared requirements and architecture instead of copying them.
- Describe a check for code that does not exist yet as a scenario and expected result, not a made-up command.
- After delivery, set the status, link the PR and its proof, and record any decision that changed during delivery.

## Return

Report the spec location, the main decision and its tradeoff, and any blocking question.
