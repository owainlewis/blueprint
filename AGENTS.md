# Working in Blueprint

Blueprint encodes software engineering practice for coding agents: design when architecture is unclear, write specs when behavior or interfaces need review, plan when work needs splitting, test before ship, refactor when code needs simplifying, review before merge, and drive PR feedback to ready with judgment.

If you are an AI agent working in this repo, follow this guidance.

## The Two Flows

Blueprint has two flows. The input to the next step is a spec, plan, or task with acceptance criteria.

**Decide** (`design-doc` -> `spec` -> `plan`): turn unclear work into reviewed decisions and tasks a new agent can do. Every stage pauses for human review. Start at `design-doc` when architecture, options, or tradeoffs are unclear. Use `spec` when requirements, function signatures, return values, data shapes, or error behavior need review. Use `plan` when the work just needs splitting. Skip stages when the change is small and already decided.

**Deliver** (`implement`): turn one ticket or task into a PR that is ready for human merge, with the ticket as the record of the work. For a task without a ticket, `implement` creates a GitHub issue with `gh` when available. It uses a dedicated ticket-numbered branch and worktree from the latest remote default branch, implements the change, tests it, gets a fresh-agent review, checks each acceptance criterion, commits, pushes, opens the PR, waits for feedback, fixes important items, and updates the ticket. Later runs resume the same PR. Use `milestone` to complete a GitHub milestone through `implement`, one issue at a time. Use `multitask` to run several independent tickets in parallel, one worker per ticket. Merging is a human decision unless explicitly requested. Use `tdd` when a failing test can describe the behavior first, `refactor` to simplify changed code before review, and `debug` when something breaks.

Exploration is allowed without creating docs or issue tracker entries. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

Decide:

- `design-doc`: write a short design doc when architecture or tradeoffs are unclear.
- `spec`: write requirements, interfaces, data shapes, and error behavior before coding.
- `plan`: break a spec, brief, or request into tasks a new agent can do.
- `goal-design`: turn rough goals into Codex or Claude Code `/goal` prompts with clear checks, proof, and stop rules.

Deliver:

- `implement`: turn one ticket or task into a PR ready for human merge; creates missing GitHub issues with `gh`, uses a dedicated branch and worktree, tests, review, acceptance checks, and feedback handling.
- `milestone`: complete all open issues in a GitHub milestone by running `implement` one issue at a time.
- `multitask`: run several tickets to PRs in parallel, one worker per ticket.
- `tdd`: test-first variant of implement.
- `debug`: find the root cause of a failure, then fix it with a regression test first when practical.
- `refactor`: simplify changed code without changing behavior.
- `review`: pre-merge code review for correctness, security, simplicity, robustness, and tests.
- `pr`: commit, push, and open a PR with a clear description.
- `browser-verify`: verify browser-rendered work in a real browser.

Helper entry points:

- `branch`: create a Git branch with the ticket ID or task name.
- `commit`: stage intended changes and write one clear Conventional Commit.

## Agents

- `code-reviewer` (`agents/code-reviewer.md`): separate reviewer. `implement` should use it for code review when agent definitions are installed.

## Running Unattended

Blueprint can run as scheduled loops over an issue tracker, with agents filing every issue. Three phases:

1. **Ready**: turn ideas and specs into issues a new agent can do. The agent filing an issue judges it at creation: decided work gets `agent:ready`; real work with open decisions gets `needs:spec`. Nothing unjudged enters the tracker.
2. **Work**: a scheduled agent claims one `agent:ready` issue and runs `implement` to a PR ready for review.
3. **Review**: humans, review bots, and checks leave feedback. A review-watch loop resumes `implement` on the existing PR after a short grace window, repeats until ready or blocked, and a human merges.

### Definition of Ready

An issue is ready for an agent when a new agent could finish it without asking questions:

- Goal stated as a result, not an implementation.
- Enough background to execute with no prior session.
- Testable acceptance criteria.
- A specific check command or manual check.
- Decision-complete: no open product or design decisions.

### Labels

Namespaces separate dimensions: `agent:*` is the state machine, `needs:*` is what an issue waits on, `risk:*` and `type:*` are metadata set when the issue is filed.

- `needs:spec`: real problem, open decisions. The spec loop picks it up.
- `agent:ready`: meets the definition of ready. The work loop claims it.
- `agent:working`: claimed by a worker. A claim with no linked branch or PR activity after 24 hours is stale; release it back to `agent:ready`.
- `agent:complete`: PR open, awaiting feedback or merge. The work loop's throttle counts these.
- `blocked`: waiting on another issue, linked in the body. Remove when the blocker closes.
- `needs:human`: an agent hit a decision only a human can make, explained in a comment.
- `risk:low` / `risk:high`: blast radius if the work goes wrong, judged at filing. Unattended loops claim `risk:low` only.
- `type:feature` / `type:bug` / `type:chore`: optional classification for reporting; not part of the loop.

Humans flip `needs:spec` to `agent:ready` after spec review, review PRs when judgment is needed, and merge. Agents do everything else. Full label reference: `guides/labels.md`. Setup and sample prompts: `guides/loops.md`.

## Guidance

- Design docs default to `docs/<design-slug>/design.md`.
- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Specs stay in the repo; plans are temporary. A plan goes to exactly one place: tracker issues when the user asks or the repo runs without a human present, `docs/<feature-slug>/plan.md` when there is a feature directory, chat otherwise.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests prove the change; review checks that they test the real behavior.
- Density over length.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns outside information into clear instructions for coding agents. That's the entire job.
