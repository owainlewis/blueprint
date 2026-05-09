# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: spec when decisions matter, plan when work needs splitting, test before ship, review before merge.

If you are an AI agent working in this repo, follow this guidance.

## The Flow

Use `spec -> plan -> implement -> review` for changes that touch contracts, schemas, multiple files, user-visible behavior, or invariants. Skip stages only when explicitly told to or when the change is trivial and decision-complete.

Exploration is allowed without creating docs or tracker issues. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

- `spec`: write the technical design before coding.
- `plan`: break a spec into agent-sized tasks.
- `implement`: execute one scoped change with tests and verification.
- `build`: deprecated alias for `implement`; prefer `implement` in new docs and prompts.
- `tdd`: test-first variant of implement.
- `review`: pre-merge review for correctness, security, simplicity, robustness, and tests.
- `compress`: shorten over-long instructions without changing behavior.
- `branch`: create a traceable Git branch with the ticket ID when available.
- `commit`: stage intended changes and write one clear Conventional Commit.

## Guidance

- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Plans default to `docs/<feature-slug>/plan.md`. Push tasks to a tracker only when the user asks.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Density over length. Run `compress` when a skill or instruction starts to feel bloated.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
