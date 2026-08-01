# Blueprint repository policy

Blueprint is a small set of instructions for AI coding. It separates deciding what to build from shipping code.

## Principles

- Give agents outcomes, constraints, and proof. Trust them with mechanics.
- Keep one skill per meaningful engineering phase or delivery outcome.
- Keep current architecture separate from proposed design.
- Review technical proposals before implementation when a wrong choice could materially affect behavior, data, security, scale, performance, compatibility, operations, cost, or proof.
- Update an existing architecture document when code changes ownership, dependency direction, protocols, stored data, trust boundaries, deployment topology, or hard limits.
- Start with the simplest useful explanation. Use short sentences and everyday words. Define technical terms before using them.
- Write for a new teammate. Put detail after the main idea. Remove anything that does not help someone decide, build, test, or review the work.
- Skip phases that add no value. Small, decided work can go straight to implementation.
- A task is ready when a new agent can finish it without asking product or technical questions.
- Each pull request delivers one focused outcome and its proof. A reviewer should not have to separate unrelated work to understand it.
- Separate refactoring when it would hide the behavior change. Small local cleanup may stay when it makes that change easier to review.
- Logic changes include automated tests for changed behavior and affected failure paths, including any named in the acceptance criteria.
- Refactors include tests for behavior that must not change.
- If automated tests cannot exercise the affected behavior, explain why and give other evidence.
- Review checks correctness. Ask for a simpler design when it can deliver the same outcome and proof with less state, indirection, duplication, or operational work.
- Do not block on personal taste. Cite technical evidence or repository conventions.
- Browser behavior is proven in a real browser, not by reading source.
- If the task, design, or plan is wrong, update it before changing more code.
- Prefer the smallest complete change. Do not mix product work with unrelated cleanup.
- Humans review decisions and merge. Agents handle the path between them.

## Phases

- `/architecture`: explain the verified current system in chat, or write an architecture document when asked. Stop for human review.
- `/design`: decide what to build, why, and how. Stop with a proposed design.
- `/architecture-review`: challenge a technical proposal and surface material flaws or open questions before implementation.
- `/plan`: split decided work into ordered, agent-ready tasks. Stop before implementation.
- `/test`: prove acceptance criteria and failure paths affected by the change, including real-browser checks when browser-rendered behavior changes.
- `/review`: use a fresh subagent for an independent, read-only implementation review.
- `/improve`: inspect existing code and improve its clarity, simplicity, and structure without changing intended behavior.

## Workflow: Code changes

For one or more code changes, follow the [`/task-to-pr` skill](skills/task-to-pr/SKILL.md). It waits for prerequisite pull requests to merge, runs independent work at the same time when useful, and takes each task through a tested and reviewed pull request. A milestone is one possible source of tasks.

Merge pull requests only when the user asks. Otherwise, leave them open.

Writing code is a basic agent ability, not a separate skill. Debugging and test-driven development are ways to implement a change, not separate product skills.

## Outputs

- A whole-system architecture document defaults to `ARCHITECTURE.md`.
- A named subsystem uses its existing document or `docs/<subsystem>/architecture.md`.
- Designs default to `docs/<feature-slug>/design.md`.
- Plans are returned in chat by default or published as tracker tickets when asked. They are not stored as plan documents.
- Pull requests start with a short plain English summary. They then explain only the detail a reviewer needs.
- The checklist states the real status of tests, checks, independent review, findings, documentation, and CI.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
