# Blueprint repository policy

Blueprint is a small set of instructions for AI coding. It separates deciding what to build from shipping code.

## Principles

- Give agents outcomes, constraints, and proof. Trust them with mechanics.
- Keep one skill per meaningful engineering phase or delivery outcome.
- Keep current architecture separate from proposed design.
- Review technical proposals before implementation when a wrong choice could materially affect behavior, data, security, scale, performance, compatibility, operations, cost, or proof.
- Update an existing architecture document when code changes ownership, dependency direction, protocols, stored data, trust boundaries, deployment topology, or hard limits.
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
- Humans review decisions and normally merge. Agents may merge only when the user explicitly delegates it. Explicitly naming `/codex-issue-coordinator` delegates merge authority for the supplied batch after its quality gates pass; an implicit skill match does not.

## Writing

Write for a new teammate who needs to understand the point on the first read.

- Lead with the outcome, decision, or rule. Put supporting detail after it.
- Use short sentences and everyday words. Give each sentence one main idea.
- Write instructions as direct commands. Put a condition before the step it controls.
- Name the actor. Prefer `the parser rejects the file` to `the file is rejected`.
- Use the same word for the same thing. Define a necessary technical term once.
- Use real names, paths, commands, limits, and effects. Replace vague claims with facts.
- Cut filler, repetition, sales language, fake warmth, and generic conclusions.
- Use sentence case for headings. Use numbered lists for sequences and bullets for real lists.
- Keep a human voice. State a judgment when the document calls for one. Keep instructions and reference text neutral.
- Vary sentence length when it helps the prose sound natural. Do not force every point into the same shape.

Before finishing, reread the text. Cut words that do no work. Fix sentences that can be read two ways. Rewrite anything that sounds generated instead of written for this project.

## Phases

- `/architecture`: create or update root `ARCHITECTURE.md` from verified implementation. Stop with the document ready for human review.
- `/design`: decide what to build, why, and how. Stop with a proposed design.
- `/architecture-review`: challenge a technical proposal and surface material flaws or open questions before implementation.
- `/plan`: split decided work into ordered, agent-ready tasks. Stop before implementation.
- `/test`: prove acceptance criteria and failure paths affected by the change, including real-browser checks when browser-rendered behavior changes.
- `/review`: use a fresh subagent for an independent, read-only implementation review.
- `/improve`: inspect existing code and improve its clarity, simplicity, and structure without changing intended behavior.
- `/codex-issue-coordinator`: coordinate a large GitHub issue batch through separate Codex worker threads, reviewed pull requests, and gated merges.

## Workflow for code changes

For one or more code changes, follow the [`/task-to-pr` skill](skills/task-to-pr/SKILL.md). It stacks dependent work after prerequisite pull requests are open and independently approved, runs independent work at the same time when useful, and takes each task through a tested and reviewed pull request. A milestone is one possible source of tasks.

Merge pull requests only when the user asks. Otherwise, leave them open.

For a large GitHub issue batch that needs visible, isolated Codex sessions, use [`/codex-issue-coordinator`](skills/codex-issue-coordinator/SKILL.md). Explicitly naming it asks in-scope workers to merge after every required test, review, CI, approval, and mergeability gate passes. An implicit match leaves passing pull requests open. Neither mode grants deployment or release authority.

Writing code is a basic agent ability, not a separate skill. Debugging and test-driven development are ways to implement a change, not separate product skills.

## Outputs

- Architecture documentation uses root `ARCHITECTURE.md`.
- Designs default to `docs/<feature-slug>/design.md`.
- Plans are returned in chat by default or published as tracker tickets when asked. They are not stored as plan documents.
- Pull requests start with a short plain English summary. They then explain only the detail a reviewer needs.
- The checklist states the real status of tests, checks, independent review, findings, documentation, and CI.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
