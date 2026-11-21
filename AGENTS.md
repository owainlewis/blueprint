# Blueprint repository policy

Blueprint is a small set of instructions for AI coding. Blueprint skills are opt-in workflows. Use them only when explicitly selected by the user or required by an already selected Blueprint workflow.

## Principles

- Give agents outcomes, constraints, and proof. Trust them with mechanics.
- Keep one skill per meaningful engineering phase or delivery outcome.
- Requirements (`REQUIREMENTS.md`) and system architecture (`ARCHITECTURE.md`) are optional project-level documents. A feature spec stands on its own and defines both that feature's requirements and its technical design.
- Distinguish approved architecture from implemented behavior. Verify claims about existing code.
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
- Humans review decisions and normally merge. Agents may merge only when the user explicitly delegates it. Explicitly naming `/codex-issue-coordinator` delegates merge authority for the supplied work after its quality gates pass; an implicit skill match does not.

## Writing

Write in plain, simplified technical English for a new teammate who needs to understand the point on the first read.

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

- `/requirements`: optional product-wide PRD in root `REQUIREMENTS.md` (useful when product requirements are kept separate from feature specs). Stop with requirements ready for human review.
- `/architecture`: optional project-level intended system and data model, with an architecture and data flow diagram, in root `ARCHITECTURE.md`. Stop with architecture ready for review.
- `/spec`: define one feature or major change—both its requirements and its technical design—after interviewing the user on unresolved choices. The spec is the ticket. Stop before planning or implementation.
- `/architecture-review`: challenge a technical proposal and surface material flaws or open questions before implementation.
- `/plan`: split decided work into ordered vertical slices and tracker tickets (GitHub, Linear, Jira, or chat) with acceptance checks. Stop before implementation.
- `/pr`: write and open or update a pull request from the branch diff with plain summary, visual change shape, verification proof, and merge risk.
- `/test`: prove acceptance criteria and failure paths affected by the change, including real-browser checks when browser-rendered behavior changes.
- `/review`: use a fresh subagent or another agent CLI for an independent, read-only review of spec fit, correctness, and design standards.
- `/improve`: inspect existing code and simplify its structure without changing intended behavior.
- `/codex-issue-coordinator`: coordinate a large GitHub issue batch through separate Codex worker threads, reviewed pull requests, and gated merges.

## Workflow for code changes

For ordinary code requests, implement the smallest complete change within the agreed scope. Define acceptance checks, verify changed behavior and affected failures, review consequential changes, and follow repository delivery policy. Do not load a Blueprint skill merely because the task matches its description.

When the user explicitly selects [`/task-to-pr`](skills/task-to-pr/SKILL.md), follow its full delivery workflow.

Merge pull requests only when the user asks. Otherwise, leave them open.

Explicitly selecting [`/codex-issue-coordinator`](skills/codex-issue-coordinator/SKILL.md) asks in-scope workers to merge after every required test, review, CI, approval, and mergeability gate passes. Do not select it from an implicit task match. It does not grant deployment or release authority.

Writing code is a basic agent ability, not a separate skill. Debugging and test-driven development are ways to implement a change, not separate product skills.

## Outputs

- Optional system requirements use root `REQUIREMENTS.md`.
- Optional project-level system architecture and its data model use root `ARCHITECTURE.md`.
- Feature specs default to `docs/<feature-slug>/spec.md` and work with or without root system documents. A supplied issue or document may serve as the spec; do not duplicate it.
- Plans are returned in chat by default or published as tracker tickets (GitHub, Linear, Jira, or local Markdown) after preview and approval.
- Pull requests use `/pr` (What, Why, What changed, optional Where to look closely, Verification, and Risk). Verification states the real status of tests, checks, screenshots, independent review, CI, and anything not verified. Risk names blast radius and reversibility; database, API contract, auth, and data-deletion changes are High.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
