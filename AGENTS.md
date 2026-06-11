# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: design when architecture is ambiguous, spec when decisions matter, plan when work needs splitting, test before ship, refactor when code needs simplifying, review before merge, drive PR feedback to merge-ready with judgment.

If you are an AI agent working in this repo, follow this guidance.

## The Two Flows

Blueprint has two flows. The handoff between them is a task with acceptance criteria.

**Decide** (`design-doc` -> `spec` -> `plan`): turn ambiguity into reviewed decisions and agent-sized tasks. Every stage pauses for human review. Start at `design-doc` when the architecture is ambiguous, at `spec` when decisions, contracts, or invariants need review, at `plan` when the work just needs splitting. Skip stages when the change is trivial and decision-complete.

**Deliver** (`task-to-pr`): turn one task into a draft PR with the ticket as the audit trail. `task-to-pr` runs `branch` -> `implement` -> `review` -> `pr`. Use `multitask` to run several independent tickets in parallel, one isolated worker per ticket. Use `pr-to-ready` once feedback exists to drive the PR to merge-ready; merging is always a human decision. Use `implement` alone when the workspace is prepared and no PR is expected, `tdd` when a failing test can describe the behavior first, `refactor` to tidy the changed code before review, and `debug` when something breaks.

Exploration is allowed without creating docs or issue tracker entries. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

Decide:

- `design-doc`: write a lightweight architecture design doc when the design is ambiguous.
- `spec`: write the technical design before coding.
- `plan`: break a spec, brief, or request into agent-sized tasks.

Deliver:

- `task-to-pr`: orchestrate one ticket to a draft PR, keeping the ticket updated with evidence.
- `multitask`: run several tickets to draft PRs in parallel, one isolated worker per ticket; composes task-to-pr.
- `branch`: create a traceable Git branch with the ticket ID when available.
- `implement`: turn one scoped task into a verified diff with tests.
- `tdd`: test-first variant of implement.
- `debug`: find the root cause of a failure, then fix it via tdd so a test guards it.
- `refactor`: simplify changed code without changing behavior.
- `review`: pre-merge review for correctness, security, simplicity, robustness, and tests.
- `pr`: commit, push, and open a PR with a clear description.
- `commit`: stage intended changes and write one clear Conventional Commit.
- `pr-to-ready`: drive an open PR with feedback to merge-ready; never merges.
- `browser-verify`: verify browser-rendered work in a real browser.

## Agents

- `code-reviewer` (`agents/code-reviewer.md`): fresh-context adversarial reviewer. The subagent that `implement` and `task-to-pr` should use for their fresh review step when agent definitions are installed.

## Guidance

- Design docs default to `docs/<design-slug>/design.md`.
- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Plans default to `docs/<feature-slug>/plan.md`. Push tasks to an issue tracker only when the user asks.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Density over length.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
