---
name: requirements
description: "Writes an optional product requirements document (PRD) in root REQUIREMENTS.md as user stories with checkable outcomes. Use when a team separates product requirements from feature specs."
user-invocable: true
argument-hint: "<system, brief, or REQUIREMENTS.md>"
disable-model-invocation: true
---

# Requirements

Fill in the [requirements template](references/requirements.md) in root `REQUIREMENTS.md`. This document is optional: use it when a product or larger team maintains a shared PRD separate from technical docs. Feature-level requirements can live directly inside a [spec](../spec/SKILL.md); system design belongs in [architecture](../architecture/SKILL.md).

## Process

1. Read the request, any existing `REQUIREMENTS.md`, and any research the user gave you.
2. Ask the user about each missing product decision, one or two related questions at a time, with your recommended answer. Look up facts in the repository instead of asking.
3. Write one user story for each thing a user needs to do, with a `REQ-n` ID and at least one "Done when" a person could check. Include what the user sees when something fails or is denied.
4. Replace every bracketed placeholder and delete the guidance comments.
5. Stop when the document is ready for review.

## Template

Use [references/requirements.md](references/requirements.md).

## Rules

- Write in plain, simplified technical English. Keep stories short, concrete, and free of filler.
- Keep existing `REQ-n` IDs. Never reuse or renumber them.
- Write from the user's side. Leave out how it will be built, unless a technology is required.
- Label assumptions. Never invent research, targets, or rules.
- Take the author from the request, or else from `git config user.name`. Set the date each time the document changes.
- Set the status to Approved only when a human approves the document.

## Return

Report the path, the decisions made, and any blocking question.
