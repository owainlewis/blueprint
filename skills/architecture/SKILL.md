---
name: architecture
description: "Designs and maintains root ARCHITECTURE.md for the intended system, including its data model and shared technical rules. Use for new systems or changes to system boundaries, ownership, storage, or deployment."
user-invocable: true
argument-hint: "<system, requirements, or ARCHITECTURE.md>"
---

# Architecture

Create or update root `ARCHITECTURE.md`. Design the system we intend to build.
Keep this as a long-running system document alongside `REQUIREMENTS.md`.
Use `/requirements` for product needs and `/spec` for a feature's technical change.

## Process

1. Read the requirements, repository instructions, existing architecture, and relevant code, schemas, tests, and infrastructure. A new system may have no code yet.
2. Identify the decisions that shape the system: boundaries, responsibilities, data ownership, dependencies, and quality constraints. Ask for missing consequential decisions; recommend an answer with its tradeoff when evidence supports one.
3. Choose the simplest structure that satisfies the requirements. Compare alternatives only when they could change the choice. Explain each important decision, its reason, and its main cost.
4. Write the architecture using the shape below. Always include an architecture and data flow diagram. Reference requirements instead of copying them.
5. Trace critical success and failure flows. Check ownership, contracts, data consistency, security, recovery, and measurable limits against the requirements.
6. Stop with the architecture ready for review. Do not plan tasks or implement it.

## Document shape

- **Summary and goals:** the system, its main parts, source of truth, and the requirements driving the design.
- **System boundary:** users, outside systems, components, and important interfaces. Include the required architecture and data flow diagram.
- **Responsibilities and dependencies:** what each part owns, what it does not own, and which way dependencies may point.
- **Data model:** core entities, relationships, identifiers, ownership, lifecycle, constraints, consistency rules, retention, and storage choices. Include an entity diagram when useful. Link larger schemas rather than repeating them.
- **Runtime flows:** important execution order, data movement, transactions, side effects, failures, retries, and recovery.
- **Security and operations:** trust boundaries, authorization, deployment, observability, resource limits, and operator recovery where they affect the design.
- **Decisions and status:** mark decisions proposed or accepted. Separately state what is implemented, missing, or different in the current system. Acceptance does not mean implementation.
- **Risks and proof:** unresolved decisions, assumptions, quality scenarios, and checks needed to validate the design.

## Diagram

Always include a Mermaid diagram showing the main components, external actors, data stores, and data flow. A single diagram may cover architecture and flow; use a second when combining them would make either hard to read.

Use clear labels, labeled arrows, and groups for system or trust boundaries. Show what moves between parts, not just which parts connect. Keep spacing generous and the layout easy to follow. Use a restrained, consistent palette with readable contrast. Avoid crossing arrows and decorative detail. Split crowded diagrams by flow and keep an overview.

Render the diagram and inspect it before finishing. Check labels, arrow direction, legibility, and agreement with the written design. Include a caption explaining the main flow and any boundary the reader needs to understand.

Use only other sections that help explain this system. Describe shared rules here; put feature-specific schema changes and migrations in its spec.

Verify claims about existing implementation against authoritative files or runtime evidence. Label future behavior and assumptions clearly. Do not mark a proposal accepted without human approval. Give important architectural rules stable `INV-n` IDs and name their intended enforcement and proof.

Update this document when an accepted change alters ownership, dependencies, interfaces, stored data, trust boundaries, deployment, or hard limits. Preserve useful content and stable references.

## Return

Report the path, main decisions and tradeoffs, implementation gaps, and any blocking question.
