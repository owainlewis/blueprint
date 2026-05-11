# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: spec when decisions matter, plan when work needs splitting, test before ship, review before merge.

If you are an AI agent working in this repo, follow this guidance.

## The Flow

Use `spec -> plan -> implement -> review` for changes that touch contracts, schemas, multiple files, user-visible behavior, or invariants. Skip stages only when explicitly told to or when the change is trivial and decision-complete.

Exploration is allowed without creating docs or issue tracker entries. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

Delivery skills turn software work into shipped changes:

- `spec`: write the technical design before coding.
- `plan`: break a spec, brief, or request into agent-sized tasks.
- `implement`: execute one scoped change with tests and verification.
- `tdd`: test-first variant of implement.
- `review`: pre-merge review for correctness, security, simplicity, robustness, and tests.
- `branch`: create a traceable Git branch with the ticket ID when available.
- `commit`: stage intended changes and write one clear Conventional Commit.

Engineering productivity skills help agents and engineers work faster, understand better, and avoid quality regressions:

- `browser-verify`: verify browser-rendered work in a real browser.
- `explain-visually`: create a responsive HTML explainer for a repo, spec, PR, architecture, or concept.
- `excalidraw-diagram`: create an editable Excalidraw diagram for a repo, spec, architecture, workflow, or concept.
- `compress`: shorten over-long instructions without changing behavior.

## Guidance

- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Plans default to `docs/<feature-slug>/plan.md`. Push tasks to an issue tracker only when the user asks.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Density over length. Run `compress` when a skill or instruction starts to feel bloated.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
