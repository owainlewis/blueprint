---
name: architecture
description: "Creates or updates root ARCHITECTURE.md from verified implementation. Use when a repository needs current architecture documentation or a structural change made it stale. Use design for proposed systems or changes."
user-invocable: true
argument-hint: "[repository or existing ARCHITECTURE.md]"
---

# Architecture

Create or update root `ARCHITECTURE.md` so a new teammate can understand the system that exists in code today.

The document should reveal the few rules that give the system its shape: where truth lives, which way dependencies point, how important work moves through the system, and which boundaries a change must preserve.

## Process

1. Read the request, repository instructions, and any existing `ARCHITECTURE.md`.
2. Inspect the implementation. Start with manifests, entry points, configuration, schemas, migrations, infrastructure, tests, and the code behind a few critical flows. Follow evidence rather than trying to read every file.
3. Identify the load-bearing facts: the system boundary, trust boundaries, source of truth, main parts, dependency direction, important protocols or data, and the one rule a contributor must not break.
4. Create or update root `ARCHITECTURE.md`. Preserve useful verified content from an existing document, remove stale claims, and organize the body around the system rather than a generic template.
5. Verify each concrete claim against code, configuration, schemas, infrastructure, or executable tests. Treat existing prose as a claim, not evidence.
6. Run the review pass and stop with the document ready for human review. Do not propose future behavior, write a design, plan work, or change implementation.

## Document shape

Start every document with this small common frame:

```markdown
# <System> architecture

## Executive summary

Explain what the system does, name its source of truth, show how its main parts work together, and state the most important architectural rule.

### System architecture

Show the users, outside systems, runtime parts, and data stores in one small diagram when this makes the boundary clearer.

### Dependency hierarchy

Show which way important dependencies point. State the rule in prose below the diagram.
```

Shape the remaining sections around the repository itself. Prefer names such as `Protocol`, `Request lifecycle`, `Event pipeline`, `Storage model`, or the real component names. Do not add sections that have nothing useful to say.

For each critical flow:

- walk the path in exact execution order;
- include authentication, authorization, validation of untrusted input, persistence, side effects, response timing, cleanup, and recovery when they matter;
- show where permissions are enforced and whether security-sensitive failures fail closed;
- put hard limits and failure behavior beside the step they affect.

For each important component, state:

- what it owns;
- its important inputs, outputs, interfaces, or stored data;
- what it depends on;
- the permissions it has and the trust boundaries it crosses, when relevant;
- what it does **not** own.

End with a small source map that links concepts to their authoritative files and a verification section that names the checks or tests supporting important claims. State genuine evidence gaps instead of guessing.

## Writing rules

- Describe implemented reality only. Use `/design` to decide future architecture or behavior.
- Write for a new teammate who needs to change the system safely.
- Lead with the source of truth, dependency direction, and load-bearing rules. Put detail later.
- For each architectural invariant, name the code, schema, runtime guard, or test that enforces it.
- Organize around runtime concepts and flows, not the directory tree.
- Prefer exact names and execution order over broad labels such as "service layer" or "robust".
- Keep diagrams small and useful. Use them for topology, dependency direction, or a flow that is harder to understand in prose.
- Keep the length proportional to the system. A small repository needs a small document. A large system may need detailed protocol, lifecycle, and component sections.
- Link to detailed API, schema, operations, or test documentation instead of copying it.
- Do not include proposals, roadmaps, possible redesigns, or speculative limitations.
- Do not turn the document into an exhaustive API reference, file inventory, or generated code tour.
- Use short sentences and everyday words. Define technical and project-specific terms when first used.
- Do not use em dashes.

Update `ARCHITECTURE.md` when implementation changes ownership, dependency direction, protocols, stored data, trust boundaries, deployment topology, or hard limits.

## Review pass

Reread the document and check:

1. **Truth.** Does every current-state claim match the working tree?
2. **Shape.** Can a new teammate find the source of truth, system boundary, dependency direction, and critical flows quickly?
3. **Boundaries.** Does each important part say what it owns, does not own, may access, and must not trust?
4. **Mechanics.** Are order, data movement, failure behavior, cleanup, and limits concrete where they matter?
5. **Maintenance.** Does the document avoid volatile detail that adds upkeep without helping someone make a safe change?
6. **Separation.** Are all proposed changes kept in design documents rather than presented as implemented architecture?

Correct every issue supported by repository evidence. Put anything that cannot be verified under `Verification` with the evidence needed to resolve it.

## Return

Report the document path, the main sources used to verify it, and any evidence
gap that remains.
