# Working in Blueprint

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

Use `/implement <ticket, task, or PR>` for one end-to-end code change. It composes the phase skills and repository tools.

1. Resolve the input. Resume an existing PR without manufacturing a ticket. Otherwise fetch the ticket, or create one from the task when `gh` is available.
2. Read the repository instructions and inspect the relevant code.
3. Create a plan and verify it against the ticket, task, or PR.
4. Implement the changes and add tests where necessary.
5. Run the `test` phase, including real-browser checks for browser-rendered behavior.
6. Run the `review` phase with a fresh subagent to review the diff independently.
7. Address valid review findings, then rerun affected tests and fresh review.
8. Create a Conventional Commit, push the branch, and open or update a ready pull request. Link the ticket when one exists and include evidence.
9. Wait for CI checks and current review feedback.
10. Fix important CI or review feedback, reply to addressed comments with evidence, then repeat affected tests and fresh review until the PR is green and has no important unresolved feedback.

Resume the branch and worktree for an existing PR. For new work, fetch the remote and create a dedicated branch and worktree from the latest remote default branch, named with the ticket number or task slug. Reuse a Codex-managed worktree when the task already has one. When creating one locally, use `~/Code/.worktrees/<repo>/<ticket-or-task>` and remove it after the PR is merged or closed. Never merge unless the user explicitly asks.

## Outputs

- Designs default to `docs/<feature-slug>/design.md`.
- Plans are returned in chat by default or published as tracker tickets when asked. They are not stored as plan documents.
- Pull requests state the outcome, link the ticket, and include test, browser, and review evidence as relevant.

Exploration does not require a design, plan, or ticket. Do not create process artifacts that do not improve a decision, handoff, or proof.
