---
name: architecture
description: "Documents or explains the current architecture of an implemented system, including its context, invariants, components, dependencies, critical flows, interfaces, data ownership, security boundaries, operations, and verified limitations. Use when the user asks to create, explain, audit, or update ARCHITECTURE.md or map how an existing system works. Do not use for a proposed feature or future system design; use the design skill instead."
user-invocable: true
argument-hint: "[repository, system, subsystem, or existing ARCHITECTURE.md]"
---

# Architecture

## Workflow

1. Read the request, repository instructions, existing architecture material, manifests, entry points, configuration, schemas, migrations, infrastructure, tests, and the implementation of representative flows.
2. Choose the requested output. When the user asks to create or update a durable architecture document, establish its boundary: use root `ARCHITECTURE.md` for a whole repository, or the established document or `docs/<subsystem>/architecture.md` for an explicitly scoped subsystem. When the user asks only to explain, map, review, or audit the current system, return a report in chat and do not modify files.
3. Treat code, schemas, configuration, infrastructure, and executable tests as evidence. Treat existing prose as a claim to verify. Resolve contradictions before repeating them.
4. Describe the current implemented system. For a durable document, use the shape below. For a chat report, keep the same evidence priorities and use only the sections that help answer the request. Link proposed changes to their design documents instead of presenting them as current behavior.
5. Run the review pass. Correct every claim you can verify, identify unresolved evidence gaps, and keep limitations restricted to verified implementation gaps.
6. Return the document or report for human review. Do not design future behavior, plan work, or change implementation.

## Durable document shape

```markdown
# <System> architecture

> **Status:** Current implementation
>
> **Verification basis:** `<commit or version>` or `working tree based on <commit>`

## 1. Executive summary
In two or three short paragraphs, explain what the system is, its central architectural idea, where authoritative state lives, and the most important boundary a contributor must preserve.

## 2. System context
Show the system, its users, external dependencies, and deployment boundary. Include a small diagram when relationships are easier to understand visually.

## 3. Architectural invariants
Numbered statements that the implemented system must preserve. Keep them observable or traceable to enforcement in code, configuration, schemas, or tests.

## 4. Components and dependencies
For each meaningful component, state what it owns, what it depends on, and what it deliberately does not own. Show dependency direction when crossing a boundary is consequential.

## 5. Critical flows
Trace the important end-to-end paths in execution order. Include authentication, validation, persistence, side effects, response timing, cleanup, and recovery where they matter.

## 6. Interfaces and data
Document public protocols, APIs, events, commands, durable schemas, identifiers, compatibility boundaries, and which component owns each source of truth.

## 7. Security and trust boundaries
State how identity is established, where authorization is enforced, what input is untrusted, what fails closed, and which process or service permissions form the trust boundary.

## 8. Failure, capacity, and operations
Document partial failure, retry and recovery, concurrency controls, hard limits, finite resources, deployment topology, observability, startup, shutdown, and operator actions.

## 9. Verification
Point to the tests, checks, dashboards, or runbooks that prove the important invariants and flows. State what remains unverified.

## 10. Known limitations
List verified gaps in the current implementation. Do not mix in aspirations, roadmap items, or speculative redesigns.

## 11. Source map
Link the small set of files that are authoritative for entry points, boundaries, schemas, configuration, and critical flows.
```

## Writing rules

- Keep read-only explanation, mapping, review, and audit requests read-only. Create or update a file only when the user asks for a durable architecture document.
- Describe implemented reality, not intended architecture. Use a design document for future behavior.
- Use `working tree based on <commit>` when the architecture document and implementation change together before commit. Do not claim that an uncommitted state was verified at the base commit.
- Start with the mental model and boundaries. Do not turn the document into a file inventory.
- Keep the length proportional to the system. A small repository may satisfy a section with one paragraph; do not pad it to resemble a large platform.
- Prefer exact execution order, ownership, and failure behavior over broad labels such as "service layer" or "robust".
- Give every component a positive and negative boundary: what it owns and what it does not own.
- Use diagrams for system context, dependencies, or flows only when they make a relationship materially clearer.
- Verify volatile facts such as counts, limits, ports, timeouts, and dependency versions immediately before writing them. Omit facts that add maintenance cost without helping a contributor make a decision.
- Link to detailed protocol, operations, or testing documents instead of duplicating them.
- Keep proposed work in linked designs. Known limitations describe present gaps only.
- Use plain words, define project-specific terms, and do not use em dashes.

## Review pass

Reread the draft and check each category against current evidence.

1. **Current state.** Does every declarative claim describe code and configuration that exist at the stated verification basis?
2. **Authority.** Is each durable state, identifier, policy, and public contract owned in one named place?
3. **Boundaries.** Does every component say what it owns, depends on, and does not own? Does the dependency direction match imports and runtime calls?
4. **Flows.** Do the critical paths include their real ordering, response point, side effects, cleanup, and failure branches?
5. **Security.** Are authentication, authorization, tenant or user isolation, untrusted input, secret access, and fail-open or fail-closed behavior explicit?
6. **Operations.** Are finite resources, concurrency, backpressure, retry, startup, shutdown, observability, and recovery covered where they affect behavior?
7. **Drift.** Do repeated claims agree with README, repository instructions, contributor docs, schemas, config, and tests? Remove duplication or name the authoritative source when they do not.
8. **Limitations.** Are gaps verified and current, with planned changes kept out of the present-state narrative?

Put unresolved evidence gaps under Verification and state what would verify them.
