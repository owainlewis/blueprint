---
name: spec
description: "Writes a spec for one feature: a short PRD (problem and user journeys) plus the technical design an agent builds from. Use when decisions must be settled before building. The spec is the ticket."
user-invocable: true
argument-hint: "<feature, change, issue, or brief>"
disable-model-invocation: true
---

# Spec

Fill in the [spec template](references/spec.md) for one feature. The top half says what to build and for whom. The bottom half says how, for the agent that builds it. The spec is the ticket.

## Process

1. Read the request, the code it touches, `REQUIREMENTS.md`, and `ARCHITECTURE.md`.
2. Ask the user about each choice that changes behavior, data, interfaces, or security. Give your recommended answer with each question.
3. Copy the template into the ticket, or into `docs/<feature-slug>/spec.md` if there is none. Fill every section, replace every bracketed placeholder, and delete the guidance comments. Write "None" where a section has nothing.
4. Compare the spec with `REQUIREMENTS.md` and `ARCHITECTURE.md`. Ask the user to settle each place they disagree.
5. Stop when another agent could build it without guessing a decision.

## Template

Use [references/spec.md](references/spec.md).

## Rules

- Keep existing `AC-n`, `J-n`, `REQ-n`, and `INV-n` IDs. Never reuse or renumber them.
- Link to requirements and architecture instead of copying them.
- Every journey has at least one acceptance row that proves it.
- Every spec has a diagram. Check that it agrees with the text.
- Describe interfaces, schemas, and rules. Leave the code and the list of files to the agent that builds it.
- For code that does not exist yet, describe the check as a scenario and expected result.
- Take the author from the request, or else from `git config user.name`. Set the date each time the spec changes.
- Set the status to Approved only when a human approves the spec. After delivery, set it to Delivered and link the PR.

## Return

Report the spec location, the main decision and its tradeoff, and any blocking question.
