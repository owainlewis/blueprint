---
name: architecture
description: "Writes root ARCHITECTURE.md from a fixed template: the intended system, a data flow diagram, the data model, and the rules every feature must follow. Use for a new system or a change to its boundaries, data, or deployment."
user-invocable: true
argument-hint: "<system, requirements, or ARCHITECTURE.md>"
disable-model-invocation: true
---

# Architecture

Fill in the [architecture template](references/architecture.md) in root `ARCHITECTURE.md`. It describes the system you intend to build and stays current as it changes. Product needs go in [requirements](../requirements/SKILL.md); one feature's design goes in a [spec](../spec/SKILL.md).

## Steps

1. Read `REQUIREMENTS.md`, the repository instructions, and any existing code, schemas, and infrastructure. Check every claim about the current system against them.
2. Ask the user about each decision that shapes the system: boundaries, who owns which data, dependencies, and hard limits. Give your recommended answer with each question.
3. Choose the simplest design that meets the requirements. For each big decision, name the strongest alternative and why you did not pick it.
4. Fill in the template. Replace every bracketed placeholder and delete the guidance comments. Render the diagram and check that it matches the text.
5. Stop when the document is ready for review. Do not plan tasks or write code.

## Template

Use [references/architecture.md](references/architecture.md).

## Rules

- Keep existing `INV-n` IDs. Never reuse or renumber them.
- Set the status to Approved only when a human approves the document. Approved is not the same as built.
- Take the author from the request, or else from `git config user.name`. Set the date each time the document changes.
- Never invent workload or latency numbers. Mark unknown targets as open decisions.
- Update this document when a change moves ownership, data, interfaces, trust boundaries, or deployment.

## Return

Report the path, the main decisions and their tradeoffs, and any blocking question.
