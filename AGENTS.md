# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: spec before code, plan before implement, test before ship, review before merge.

If you are an AI agent working in this repo, follow these conventions.

## The Flow

Use `spec -> plan -> implement -> review` for changes that touch contracts, schemas, multiple files, user-visible behavior, or invariants. Skip stages only when explicitly told to or when the change is trivial and decision-complete.

Exploration is allowed without creating docs or tickets. Do not manufacture fake specs, plans, or Linear tasks for spikes.

## Skills

- `spec`: write the technical design before coding.
- `plan`: break a spec into 3-5 agent-sized tasks.
- `implement`: execute one task; read the spec first.
- `tdd`: test-first variant of implement.
- `review`: pre-merge review for correctness, security, simplicity, robustness, and tests.
- `compress`: shorten over-long instructions without changing behavior.

## Conventions

- One spec per feature, at `docs/<feature-slug>/spec.md`.
- State lives in Linear, not in the repo. The ticket is the state.
- If the spec is wrong, stop and re-spec. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Add one line to `docs/conventions.md` when implementation reveals a reusable non-obvious convention.
- Density over length. Run `compress` when a skill or instruction starts to feel bloated.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
