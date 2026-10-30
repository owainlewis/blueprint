---
name: requirements
description: "Writes the product requirements document (PRD) in root REQUIREMENTS.md from a fixed template built on user stories: who the users are, what each needs to do, the business rules, and how to tell it works. Use for a new service or system, or a change to its product expectations."
user-invocable: true
argument-hint: "<system, brief, or REQUIREMENTS.md>"
disable-model-invocation: true
---

# Requirements

Fill in the template below in root `REQUIREMENTS.md`. It is the product requirements document (PRD) for the whole system and stays current as the product changes. Use [spec](../spec/SKILL.md) for one feature and [architecture](../architecture/SKILL.md) for technical decisions.

## Process

1. Read the request, repository instructions, the existing `REQUIREMENTS.md`, and any research or feedback supplied. Reuse decisions already made.
2. Ask the user about each missing product decision that could change the result. Give your recommended answer with each question. Inspect the repository for facts instead of asking.
3. Write one user story for each thing a user needs to do. Give each a stable `REQ-n` ID and at least one "Done when" condition a person could check.
4. Check that the stories cover denial, invalid input, and failure where users meet them, and that no two stories conflict.
5. Stop with the document ready for review. Do not design the implementation, plan tasks, or write code.

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
- Write stories from the user's side. Keep implementation choices out; include an imposed technology only as a constraint.
- Label assumptions. Never invent research, targets, or business rules.
- Keep feature detail and acceptance tables in specs. Update this document when the product, scope, or business rules change.

## Return

Report the path, the decisions made, and any blocking question.
