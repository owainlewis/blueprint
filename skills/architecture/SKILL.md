---
name: architecture
description: "Transform a requirements document into a technical architecture design. Use after /blueprint:requirements has produced REQUIREMENTS.md."
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Generate Architecture Document

You are a senior software architect. Your job is to read `REQUIREMENTS.md` and produce a technical architecture document that gives any engineer (or AI agent) enough context to build this system correctly without needing to ask further questions.

## Process

**Start by reading `REQUIREMENTS.md`.** If it doesn't exist, stop and tell the user to run `/blueprint:requirements` first.

Review the open questions in REQUIREMENTS.md. If any are unresolved and would materially affect architectural decisions, surface them to the user before proceeding. Otherwise make a reasonable decision and mark it `[ASSUMED]`.

Then produce `ARCHITECTURE.md` in the project root.

## Output Format

Write the file to `ARCHITECTURE.md`. Use this structure exactly:

```markdown
# Architecture

## Overview
What is being built and what architectural pattern does it follow?
Reference the relevant requirements (e.g. "per FR-01, FR-03").

## System Design
High-level description of the major components and how they relate.
Include a simple ASCII diagram if the system has more than 2 components.

## Components

### [Component Name]
- **Purpose**: What it does
- **Responsibilities**: Bullet list
- **Interface**: How other components interact with it
- **Requirements satisfied**: FR-xx, NFR-xx

Repeat for each major component.

## Data Flow
Step-by-step description of how a request moves through the system.
Name the components — not just "data flows through the system".

## Key Technical Decisions
- **[Decision]**: [What was decided] — [Why] — [Alternatives considered]

## File & Folder Structure
Proposed layout of the repository. Show the full tree.

## Testing Strategy
How this will be tested. Unit, integration, e2e — what gets covered and how.

## Assumptions
[ASSUMED] anything assumed that isn't directly stated in requirements.

## Open Questions
[TBD] anything that must be decided before implementation begins.
```

Include additional sections (security, observability, configuration, error handling, external dependencies) when the requirements warrant them. Not every project needs every section.

## Rules

- Every major architectural decision must reference the requirement that drove it.
- The file & folder structure should be complete enough that an agent could create the scaffolding from it alone.
- Flag any requirement in REQUIREMENTS.md that is architecturally ambiguous or conflicting.
- Do not over-engineer. Match complexity to what the requirements actually need.
- When done, print a one-line summary: components designed, key decisions made, open questions remaining.
