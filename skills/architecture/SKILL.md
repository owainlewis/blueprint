---
name: architecture
description: "Writes an optional project-level ARCHITECTURE.md from a fixed template: the intended system, a data flow diagram, the data model, and system invariants. Use for a new system or a change to its boundaries, data, or deployment."
user-invocable: true
argument-hint: "<system, brief, or ARCHITECTURE.md>"
disable-model-invocation: true
---

# Architecture

Fill in the [architecture template](references/architecture.md) in root `ARCHITECTURE.md`. This project-level document is optional: use it when a repository benefits from a living map of its intended system and invariants. Feature requirements and technical design go in a [spec](../spec/SKILL.md); a product-wide PRD can live in [requirements](../requirements/SKILL.md) if the team uses one.

## Steps

1. Read the request, repository instructions, and any existing code, schemas, and infrastructure. Read `REQUIREMENTS.md` if it exists, but do not require it. Check every claim about the current system against the code.
2. Ask the user about each decision that shapes the system: boundaries, who owns which data, dependencies, and hard limits. Ask one or two related questions at a time with your recommended answer.
3. Choose the simplest design that meets the need. For each big decision, name the strongest alternative and why you did not pick it.
4. Fill in the template. Replace every bracketed placeholder and delete the guidance comments. Render or check the diagram so it agrees with the text.
5. Stop when the document is ready for review. Do not plan tasks or write code.

## Template

Use [references/architecture.md](references/architecture.md).

## Rules

- Write in plain, simplified technical English. Keep every section concise and concrete.
- Keep existing `INV-n` IDs. Never reuse or renumber them.
- Set the status to Approved only when a human approves the document. Approved is not the same as built.
- Take the author from the request, or else from `git config user.name`. Set the date each time the document changes.
- Never invent workload or latency numbers. Mark unknown targets as open decisions.
- Update this document when a change moves ownership, data, interfaces, trust boundaries, or deployment.

## Return

Report the path, the main decisions and their tradeoffs, and any blocking question.
