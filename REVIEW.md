# Review Blueprint

Review Blueprint as a small set of engineering instructions. Read the issue, complete diff, rendered public docs, and relevant surrounding files.

- Does the writing lead with the outcome, decision, or rule?
- Can a new teammate understand it without already knowing Blueprint terms?
- Does each sentence carry one main idea in short, everyday words?
- Does each concept keep the same name throughout the text?
- Are claims tied to real names, paths, commands, limits, or effects?
- Did the writer cut filler, repetition, sales language, fake warmth, and generic conclusions?
- Do headings use sentence case and tell the reader what follows?
- Does each skill represent one meaningful engineering phase or delivery outcome?
- Is policy in `AGENTS.md`, with each phase and delivery workflow in its skill?
- Does `/architecture` create or update root `ARCHITECTURE.md` from verified implementation while `/design` describes a proposed system or feature change?
- Does `/architecture-review` challenge a technical proposal while `/review` checks an implementation change?
- Does architecture review surface only questions that could materially change behavior, data, interfaces, security, scale, performance, operations, cost, compatibility, or proof?
- Does architecture review test the goal, clarity, chosen design, failure behavior, limits, security, operations, and proof without requiring irrelevant sections?
- Does `/architecture` have one outcome instead of mixing document generation with chat explanations, maps, reviews, or audits?
- When a change affects ownership, dependency direction, protocols, stored data, trust boundaries, topology, or hard limits, is the current architecture document updated?
- Are triggers, outputs, boundaries, proof, and stop conditions clear?
- Is the change one focused, self-contained, reviewable outcome with its related proof?
- Does `/task-to-pr` order one or more tasks and create one tested and independently reviewed pull request for each task?
- Does `/task-to-pr` mark each pull request ready before independent and GitHub review begin?
- Does each task use its own branch and worktree, with independent tasks allowed to run at the same time and dependent tasks stacked after prerequisite pull requests are open and independently approved?
- Does it stop after configured CI and automated review instead of waiting for human feedback?
- Does it reply to every automated review finding and resolve threads only after they are fully addressed?
- Does it merge only when the user asks, including the explicit batch authority granted by `/codex-issue-coordinator`?
- Does `/codex-issue-coordinator` use one visible Codex worker thread, worktree, branch, and pull request per GitHub issue?
- Does it name workers after issue numbers, bound concurrency, wait for prerequisite merges, and keep implementation context out of the coordinator?
- Does every worker test first, mark its pull request ready, obtain fresh approval, pass CI, resolve review feedback, and satisfy repository rules before merging?
- Does coordinator merge authority require explicit user wording, remain limited to the supplied batch, and exclude deployment, releases, destructive actions, and unrelated pull requests?
- Does the coordinator resume an open pull request from its exact head branch and reconcile already-merged pull requests with closed issue state only after the change and proof satisfy the issue?
- In no-merge mode, does it record dependent issues as waiting for human merge instead of dispatching from an unmerged branch or waiting indefinitely?
- In no-merge mode, does it stop after agent-completable gates and record required human approval or merge as a blocker instead of waiting indefinitely?
- Is browser-rendered behavior checked in a real browser?
- Can a capable agent choose local mechanics without redundant instructions?
- Are removed concepts handled by an explicit migration instead of compatibility clutter?
- Can each judgment be decided from evidence? Replace vague terms such as "code health", "adequate", "robust", and "production-ready" with concrete criteria.
- Is every sentence useful enough to compete for agent attention?
- Can any sentence be read two ways? If so, rewrite it.
- Does any passage sound generated instead of written for this project? If so, make it specific or cut it.

Prefer the shortest wording that preserves the rule. Treat extra skills, duplicate workflows, fake reviewer roles, and steps without proof as regressions.
