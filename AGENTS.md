# Blueprint repository policy

Blueprint is a small, principles-first process for AI coding. It separates thinking phases from the workflow that ships code.

## Principles

- Give agents outcomes, constraints, and proof. Trust them with mechanics.
- Keep one skill per meaningful engineering phase or delivery outcome.
- Keep current architecture separate from proposed design. Update existing architecture documents when implementation changes ownership, dependency direction, protocols, durable data, trust boundaries, deployment topology, or hard limits.
- Skip phases that add no value. Small, decided work can go straight to implementation.
- A task is ready when a new agent can finish it without asking product or technical questions.
- Each pull request delivers one focused, self-contained outcome with its related proof. A change is reviewable when its outcome, behavior, and proof can be understood without first separating unrelated work. Separate refactoring when it would obscure the behavior diff. Small local cleanup may remain when it makes the changed behavior easier to review.
- Logic changes include automated tests for changed behavior and failure paths affected by the change or named in its acceptance criteria. Refactors include tests for behavior that must not change. If the change has no executable behavior, or the affected behavior cannot be exercised through available automated interfaces, state the concrete reason and substitute evidence.
- Review checks correctness. If the same outcome and proof can be delivered with less state, indirection, duplication, or operational work, request the simpler design. Do not block on personal taste. Cite technical evidence or repository conventions.
- Browser behavior is proven in a real browser, not by reading source.
- If the task, design, or plan is wrong, update it before changing more code.
- Prefer the smallest complete change. Do not mix product work with unrelated cleanup.
- Humans review decisions and merge. Agents handle the path between them.

## Phases

- `/architecture`: document the verified current system and its boundaries. Stop for human review.
- `/design`: decide what to build, why, and how. Stop for human review.
- `/plan`: split decided work into ordered, agent-ready tasks. Stop before implementation.
- `/test`: prove acceptance criteria and failure paths affected by the change, including real-browser checks when browser-rendered behavior changes.
- `/review`: use a fresh subagent for an independent, read-only review.
- `/improve`: inspect existing code and improve its clarity, simplicity, and structure without changing intended behavior.

## Workflow: Milestones

For a GitHub milestone, use `/milestone`. It orders open issues and runs `/task-to-pr` one issue at a time. Stop for human merge after each green pull request unless the user explicitly delegates merging for that run.

Writing code is a base capability, not a separate phase skill. Debugging and test-driven development are implementation techniques, not product-level entry points.

## Workflow: Code changes

For one end-to-end code change, follow the canonical [`/task-to-pr` skill](skills/task-to-pr/SKILL.md). It owns ticket handling, worktree isolation, coding, tests, independent review, commits, pull requests, CI, and current feedback. Never merge unless the user explicitly asks.

## Outputs

- Whole-system architecture defaults to `ARCHITECTURE.md`. Explicitly scoped subsystem architecture defaults to its established document or `docs/<subsystem>/architecture.md`.
- Designs default to `docs/<feature-slug>/design.md`.
- Plans are returned in chat by default or published as tracker tickets when asked. They are not stored as plan documents.
- Pull requests explain what changed, why it matters, what the reviewer should consider, and a truthful checklist covering tests, checks, independent review, findings, documentation, and CI.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
