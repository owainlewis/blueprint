---
name: requirements
description: "Writes the product requirements document (PRD) in root REQUIREMENTS.md as user stories with checkable outcomes. Use for a new product or a change to what it should do."
user-invocable: true
argument-hint: "<system, brief, or REQUIREMENTS.md>"
disable-model-invocation: true
---

# Requirements

Fill in this template in root `REQUIREMENTS.md`. It is the PRD for the whole product; keep it current. One feature goes in a [spec](../spec/SKILL.md), technical decisions in [architecture](../architecture/SKILL.md).

## Process

1. Read the request, the existing `REQUIREMENTS.md`, and any research the user gave you.
2. Ask the user about each product decision that is missing. Give your recommended answer with each question. Look up facts in the repository instead of asking.
3. Write one user story for each thing a user needs to do, with a `REQ-n` ID and at least one "Done when" a person could check. Include what the user sees when something fails or is denied.
4. Stop when the document is ready for review.

## Template

```markdown
# <Product> requirements

Status: Proposed | Accepted

## Problem and users

<Who has the problem, what goes wrong for them today, and the outcome they need.
Name each type of user once; the stories below use these names.>

## User stories

### REQ-1: <Short name>

As a <user>, I want to <action>, so that <benefit>.

Done when:
- <Observable result a person could check>
- <What the user sees when it fails or is denied>

### REQ-2: <Short name>

...

## Business rules

<Rules that hold across stories: permissions, limits, states, and what must never happen.>

## Constraints

<Required security, privacy, compatibility, and performance limits. Use numbers when known.
Mark unknown targets as open decisions.>

## Out of scope

<What this product does not do yet.>

## Success measures

<How to judge value after release, when there is evidence for a measure. Otherwise "None yet".>

## Open decisions

<Each unanswered question, your recommended answer, and what it blocks.>
```

## Rules

- Keep existing `REQ-n` IDs. Never reuse or renumber them.
- Write from the user's side. Leave out how it will be built, unless a technology is required.
- Label assumptions. Never invent research, targets, or rules.

## Return

Report the path, the decisions made, and any blocking question.
