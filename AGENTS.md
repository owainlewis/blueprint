# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: design when architecture is ambiguous, spec when decisions matter, plan when work needs splitting, test before ship, refactor when code needs simplifying, review before merge, drive PR feedback to merge-ready with judgment.

If you are an AI agent working in this repo, follow this guidance.

## The Flow

Use `design-doc -> spec -> plan -> implement -> review` for changes with ambiguous architecture, tradeoffs, or cross-cutting concerns. Use `spec -> plan -> implement -> review` for changes that touch contracts, schemas, multiple files, user-visible behavior, or invariants. Skip stages only when explicitly told to or when the change is trivial and decision-complete.

Use `refactor` after implementation when changed code needs cleanup for reuse, quality, or efficiency. Use `pr-to-ready` after PR review comments exist.

Exploration is allowed without creating docs or issue tracker entries. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

- `design-doc`: write a lightweight architecture design doc before implementation when the design is ambiguous.
- `spec`: write the technical design before coding.
- `plan`: break a spec, brief, or request into agent-sized tasks.
- `implement`: execute one scoped change with tests and verification.
- `tdd`: test-first variant of implement.
- `refactor`: simplify changed code without changing behavior.
- `review`: pre-merge review for correctness, security, simplicity, robustness, and tests.
- `task-to-pr`: run the loop from ticket to draft PR, keeping the ticket updated with evidence.
- `pr-to-ready`: drive an open PR with feedback to merge-ready; never merges.
- `browser-verify`: verify browser-rendered work in a real browser.
- `branch`: create a traceable Git branch with the ticket ID when available.
- `commit`: stage intended changes and write one clear Conventional Commit.

## Guidance

- Design docs default to `docs/<design-slug>/design.md`.
- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Plans default to `docs/<feature-slug>/plan.md`. Push tasks to an issue tracker only when the user asks.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Density over length.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
