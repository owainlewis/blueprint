---
name: design-doc
description: "Write a lightweight technical design document for ambiguous or consequential architecture decisions before implementation."
user-invocable: true
argument-hint: "<system, feature, architecture question, repo path, or design brief>"
---

# Design Doc

Write a lightweight architecture design doc for a decision that deserves thinking before code. Use this when the problem has real ambiguity, tradeoffs, cross-cutting concerns, or future maintenance risk. If the solution is obvious and the doc would only become an implementation manual, say so and recommend `spec` or `implement` instead.

## Workflow

### 1. Ground

- Treat the full argument as the design brief unless the user names a feature or path.
- Derive a kebab-case slug if no name is given.
- Read referenced docs, code, specs, plans, and architecture notes so the design fits the system as it exists.
- Identify stakeholders, goals, non-goals, constraints, cross-cutting concerns, and decisions that need human review.
- Ask only when a missing fact would materially change the design. Ask one question at a time with your recommended answer.

### 2. Write

Write `docs/<design-slug>/design.md` using the sections below. Keep solo-developer docs short: prefer 1-3 pages unless the architecture genuinely needs more.

- **Status**: Draft, In Review, Approved, or Superseded.
- **Summary**: the problem and recommended direction in a few sentences.
- **Context and Scope**: objective background, current system, and what this doc covers.
- **Goals**: outcomes this design must achieve.
- **Non-Goals**: reasonable adjacent outcomes this design deliberately excludes.
- **Constraints**: technical, product, migration, compatibility, operational, cost, or time constraints.
- **Proposed Design**: the chosen architecture, starting high-level before details.
- **Architecture Views** *(when useful)*: system context, data flow, runtime, deployment, or component diagrams.
- **Interfaces and Data** *(when relevant)*: API, event, schema, storage, or contract changes that affect the design.
- **Alternatives Considered**: plausible options and why they lose under the stated goals and constraints.
- **Tradeoffs**: what the chosen design gains, gives up, risks, or postpones.
- **Cross-Cutting Concerns**: security, privacy, observability, reliability, performance, cost, and operations where relevant.
- **Rollout and Migration** *(when relevant)*: how to ship, migrate, verify, and back out safely.
- **Open Questions**: decisions or facts still unresolved.
- **Decision**: the recommendation, assumptions, and who needs to review or approve it.

### 3. Pause

Stop after writing. Do not continue into `spec`, `plan`, or implementation until the human confirms the design.

## Rules

- The document exists to make reasoning reviewable, not to document every implementation step.
- Focus on tradeoffs, alternatives, and constraints code will not explain later.
- Use diagrams only when they clarify relationships, flows, or deployment.
- Do not copy full schemas, APIs, or code unless the exact shape is central to the decision.
- Write for a future maintainer who needs to understand why this design was chosen.
