# Review Blueprint

Review Blueprint as a small set of engineering instructions. Read the issue, complete diff, rendered public docs, and relevant surrounding files.

- Can a new teammate understand the summary without already knowing Blueprint terms?
- Does the writing use short sentences, everyday words, and only useful detail?
- Does each skill represent one meaningful engineering phase or delivery outcome?
- Is policy in `AGENTS.md`, with each phase and delivery workflow in its skill?
- Does `/architecture` describe verified current implementation while `/design` describes a proposed feature or system-part change?
- Does `/architecture-review` challenge a technical proposal while `/review` checks an implementation change?
- Does architecture review surface only questions that could materially change behavior, data, interfaces, security, scale, performance, operations, cost, compatibility, or proof?
- Does architecture review test the goal, clarity, chosen design, failure behavior, limits, security, operations, and proof without requiring irrelevant sections?
- Does a read-only architecture explanation, mapping, review, or audit remain in chat unless the user asks for a document?
- When a change affects ownership, dependency direction, protocols, stored data, trust boundaries, topology, or hard limits, is the current architecture document updated?
- Are triggers, outputs, boundaries, proof, and stop conditions clear?
- Is the change one focused, self-contained, reviewable outcome with its related proof?
- Does `/task-to-pr` order one or more tasks and create one tested and independently reviewed pull request for each task?
- Does each task use its own branch and worktree, with independent tasks allowed to run at the same time?
- Does it stop after configured CI and automated review instead of waiting for human feedback?
- Does it merge only when the user asks?
- Is browser-rendered behavior checked in a real browser?
- Can a capable agent choose local mechanics without redundant instructions?
- Are removed concepts handled by an explicit migration instead of compatibility clutter?
- Can each judgment be decided from evidence? Replace vague terms such as "code health", "adequate", "robust", and "production-ready" with concrete criteria.
- Is every sentence useful enough to compete for agent attention?

Prefer the shortest wording that preserves the rule. Treat extra skills, duplicate workflows, fake reviewer roles, and steps without proof as regressions.
