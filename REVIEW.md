# Review Blueprint

Review Blueprint as a small process product, not a prompt catalogue. Read the issue, complete diff, rendered public docs, and relevant surrounding files.

- Does each skill represent one meaningful engineering phase or delivery outcome?
- Is policy in `AGENTS.md`, with phase behavior and delivery orchestration in skills?
- Does `/architecture` describe verified current implementation while `/design` describes a proposed feature or system-part change?
- Does a read-only architecture explanation, mapping, review, or audit remain in chat unless the user asks for a durable document?
- When a change affects ownership, dependency direction, protocols, durable data, trust boundaries, topology, or hard limits, is the current architecture reference updated?
- Are triggers, outputs, boundaries, proof, and stop conditions clear?
- Is the change one focused, self-contained, reviewable outcome with its related proof?
- Does `/task-to-pr` reach a tested, independently reviewed, green PR without merging by default?
- Is browser-rendered behavior checked in a real browser?
- Can a capable agent choose local mechanics without redundant instructions?
- Are removed concepts handled by an explicit migration instead of compatibility clutter?
- Can each judgment be decided from evidence? Replace vague terms such as "code health", "adequate", "robust", and "production-ready" with concrete criteria.
- Is every sentence useful enough to compete for agent attention?

Prefer the smallest wording that preserves the outcome. Treat extra skills, duplicate workflows, fake personas, and ceremony without proof as regressions.
