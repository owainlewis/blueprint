---
name: architecture
description: "Explains how an existing system works today. Use for architecture maps, audits, or ARCHITECTURE.md. Return a chat report unless the user asks for a file. Use design for proposed changes."
user-invocable: true
argument-hint: "[repository, system, subsystem, or existing ARCHITECTURE.md]"
---

# Architecture

## Workflow

1. Read the request and repository instructions. Then inspect existing architecture docs, manifests, entry points, configuration, schemas, migrations, infrastructure, tests, and a few important flows.
2. Choose the output:
   - For a whole repository document, use root `ARCHITECTURE.md`.
   - For a named subsystem, use its existing document or `docs/<subsystem>/architecture.md`.
   - For an explanation, map, review, or audit, answer in chat and do not modify files.
3. Treat code, schemas, configuration, infrastructure, and executable tests as evidence. Treat existing prose as a claim to verify. Resolve contradictions before repeating them.
4. Describe the system that exists now. Use the shape below for a document. For a chat report, use only the sections that answer the request. Link proposed changes to their design documents.
5. Run the review pass. Correct every claim you can verify, identify unresolved evidence gaps, and keep limitations restricted to verified implementation gaps.
6. Return the document or report for human review. Do not design future behavior, plan work, or change implementation.

## Document shape

```markdown
# <System> architecture

> **Status:** Current implementation
>
> **Verification basis:** `<commit or version>` or `working tree based on <commit>`

## 1. Executive summary
In two or three short paragraphs, say what the system does, name its main parts, explain how they work together, say where the real data lives, and name the one rule a contributor must not break.

## 2. System context
Show the users, outside systems, and what runs inside or outside this system. Include a small diagram when it makes those relationships clearer.

## 3. Architectural invariants
List numbered rules that the current code must preserve. Each rule must be visible in behavior or backed by code, configuration, schemas, or tests.

## 4. Components and dependencies
For each important part, state what it owns, what it depends on, and what it does not own. Show which way a dependency points when crossing the boundary matters.

## 5. Critical flows
Trace the important end-to-end paths in execution order. Include authentication, validation, persistence, side effects, response timing, cleanup, and recovery where they matter.

## 6. Interfaces and data
Document public protocols, APIs, events, commands, stored data, identifiers, compatibility rules, and which part owns each piece of data or policy.

## 7. Security and trust boundaries
State how identity is established, where authorization is enforced, what input is untrusted, what fails closed, and which process or service permissions form the trust boundary.

## 8. Failure, capacity, and operations
Document partial failure, retry and recovery, concurrency controls, hard limits, limited resources, deployment layout, monitoring, startup, shutdown, and operator actions.

## 9. Verification
Point to the tests, checks, dashboards, or runbooks that prove the important rules and flows. State what remains unverified.

## 10. Known limitations
List gaps that current evidence confirms. Do not mix in goals, roadmap items, or possible redesigns.

## 11. Source map
Link the small set of files that define entry points, boundaries, schemas, configuration, and critical flows.
```

## Writing rules

- Keep explanation, mapping, review, and audit requests read-only. Create or update a file only when the user asks for an architecture document.
- Describe implemented reality, not intended architecture. Use a design document for future behavior.
- Use `working tree based on <commit>` when the document and code change together before commit. Do not claim that uncommitted code was verified at the base commit.
- Start with the simplest useful explanation. Write for a new teammate, not someone who already knows the project.
- Use short sentences and everyday words. Define technical terms before using them.
- Put detail after the reader understands the main idea. Do not turn the document into a file inventory.
- Keep the length proportional to the system. A small repository may satisfy a section with one paragraph; do not pad it to resemble a large platform.
- Prefer exact execution order, ownership, and failure behavior over broad labels such as "service layer" or "robust".
- Give every component a positive and negative boundary: what it owns and what it does not own.
- Use diagrams for system context, dependencies, or flows only when they make a relationship materially clearer.
- Check facts that can change immediately before writing them. Examples include counts, limits, ports, timeouts, and dependency versions.
- Omit facts that add maintenance work without helping a contributor make a decision.
- Link to detailed protocol, operations, or testing documents instead of duplicating them.
- Keep proposed work in linked designs. Known limitations describe present gaps only.
- Use plain words, define project-specific terms, and do not use em dashes.

## Review pass

Reread the draft and check each category against current evidence.

1. **Clear summary.** Can a new teammate explain what the system does, how its main parts work together, where the real data lives, and the main rule to preserve?
2. **Current state.** Does every statement describe code and configuration that exist at the stated verification basis?
3. **Ownership.** Is each stored value, identifier, policy, and public contract owned in one named place?
4. **Boundaries.** Does every component say what it owns, depends on, and does not own? Does the dependency direction match imports and runtime calls?
5. **Flows.** Do the critical paths include their real ordering, response point, side effects, cleanup, and failure branches?
6. **Security.** Are authentication, authorization, tenant or user isolation, untrusted input, secret access, and fail-open or fail-closed behavior explicit?
7. **Operations.** Does the document cover limited resources, concurrency, retries, startup, shutdown, monitoring, and recovery? Does it say how the system slows incoming work when full?
8. **Consistency.** Do repeated claims agree with README, repository instructions, contributor docs, schemas, config, and tests? Remove duplication or name the source when they do not.
9. **Limitations.** Are gaps verified and current, with planned changes kept out of the current-system explanation?

Put unresolved evidence gaps under Verification and state what would verify them.
