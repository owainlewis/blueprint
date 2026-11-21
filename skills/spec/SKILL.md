---
name: spec
description: "Writes a feature spec: the feature's requirements (problem, goals, user journeys) plus the technical design and proof an agent builds from. Interviews the user on open choices before writing. The spec is the ticket."
user-invocable: true
argument-hint: "<feature, change, issue, or brief>"
disable-model-invocation: true
---

# Spec

Fill in the [spec template](references/spec.md) for one feature. The top half defines the feature's requirements (what to build and for whom). The bottom half defines how to build and prove it. The spec is the ticket.

## Process

1. Read the request and the existing code it touches. Read `ARCHITECTURE.md` and `REQUIREMENTS.md` if the repository has them, but do not require them.
2. Answer what you can from the codebase first. Never ask the user a question the code already answers.
3. Interview the user on unresolved decisions that change behavior, data, interfaces, or security. Ask one or two related questions at a time, each with your recommended answer, and resolve one branch before moving to the next. Skip re-asking decisions already settled in the conversation.
4. Copy the template into the ticket, or into `docs/<feature-slug>/spec.md` if there is none. Fill every section, replace every bracketed placeholder, and delete the guidance comments. Write "None" where a section has nothing.
5. If `ARCHITECTURE.md` or `REQUIREMENTS.md` exists, check the spec against them and ask the user to settle any disagreement.
6. Stop when another agent could build the feature without guessing a decision.

## Template

Use [references/spec.md](references/spec.md).

## Rules

- Write in plain, simplified technical English. Keep every section short, direct, and free of filler.
- Keep existing `AC-n`, `J-n`, `REQ-n`, and `INV-n` IDs. Never reuse or renumber them.
- Link to `ARCHITECTURE.md` or `REQUIREMENTS.md` only when they exist, instead of copying them. Do not invent external IDs when they do not exist.
- Every journey has at least one acceptance row that proves it.
- Every spec has a diagram. Check that it agrees with the text.
- Describe interfaces, schemas, rules, and testing seams (what boundary to test at and what not to mock). Leave the code and file list to the agent that builds it.
- For code that does not exist yet, describe the check as a scenario and expected result.
- Take the author from the request, or else from `git config user.name`. Set the date each time the spec changes.
- Set the status to Approved only when a human approves the spec. After delivery, set it to Delivered and link the PR.

## Return

Report the spec location, the main decision and its tradeoff, and any blocking question.
