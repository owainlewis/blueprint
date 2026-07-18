# Blueprint repository policy

Blueprint is a small, principles-first process for AI coding. It separates thinking phases from the workflow that ships code.

## Principles

- Give agents outcomes, constraints, and proof. Trust them with mechanics.
- Keep one skill per meaningful engineering phase.
- Skip phases that add no value. Small, decided work can go straight to implementation.
- A task is ready when a new agent can finish it without asking product or technical questions.
- Tests prove the requested behavior. Review checks that the proof and implementation are sound.
- Browser behavior is proven in a real browser, not by reading source.
- If the task, design, or plan is wrong, update it before changing more code.
- Prefer the smallest complete change. Do not mix product work with unrelated cleanup.
- Humans review decisions and merge. Agents handle the path between them.

## Phases

- `design`: decide what to build, why, and how. Stop for human review.
- `plan`: split decided work into ordered, agent-ready tasks. Stop before implementation.
- `test`: prove acceptance criteria and important failures, including browser checks when relevant.
- `review`: use a fresh subagent for an independent, read-only review.
- `improve`: inspect existing code and improve its clarity, simplicity, and structure without changing intended behavior.

Writing code is a base capability, not a separate phase skill. Debugging and test-driven development are implementation techniques, not product-level entry points.

## Workflow: Code changes

For one end-to-end code change, follow the canonical [`/implement` workflow](commands/implement.md). It owns ticket handling, worktree isolation, coding, tests, independent review, commits, pull requests, CI, and current feedback. Never merge unless the user explicitly asks.

## Outputs

- Designs default to `docs/<feature-slug>/design.md`.
- Plans are returned in chat by default or published as tracker tickets when asked. They are not stored as plan documents.
- Pull requests state the outcome, link the ticket, and include test, browser, and review evidence as relevant.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
