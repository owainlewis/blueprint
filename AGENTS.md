# Working in Blueprint

Blueprint encodes world-class software engineering and agentic engineering practice: design when architecture is ambiguous, spec when decisions matter, plan when work needs splitting, test before ship, refactor when code needs simplifying, review before merge, drive PR feedback to merge-ready with judgment.

If you are an AI agent working in this repo, follow this guidance.

## The Two Flows

Blueprint has two flows. The handoff between them is a task with acceptance criteria.

**Decide** (`design-doc` -> `spec` -> `plan`): turn ambiguity into reviewed decisions and agent-sized tasks. Every stage pauses for human review. Start at `design-doc` when the architecture is ambiguous, at `spec` when decisions, contracts, or invariants need review, at `plan` when the work just needs splitting. Skip stages when the change is trivial and decision-complete.

**Deliver** (`task-to-pr`): turn one task into a draft PR with the ticket as the audit trail. `task-to-pr` runs workspace preparation -> `implement` -> review subagent -> acceptance-verification subagent -> `pr`, preferring worktrees when isolation reduces risk. Use `multitask` to run several independent tickets in parallel, one isolated worker per ticket. Use `pr-to-ready` once feedback exists to drive the PR to merge-ready; merging is always a human decision. Use `implement` alone when the workspace is prepared and no PR is expected, `tdd` when a failing test can describe the behavior first, `refactor` to tidy the changed code before review, and `debug` when something breaks.

Exploration is allowed without creating docs or issue tracker entries. Do not manufacture fake specs, plans, or issues for spikes.

## Skills

Decide:

- `design-doc`: write a lightweight architecture design doc when the design is ambiguous.
- `spec`: write the technical design before coding.
- `plan`: break a spec, brief, or request into agent-sized tasks.

Deliver:

- `task-to-pr`: orchestrate one ticket to a draft PR, keeping the ticket updated with evidence; uses isolated branches/worktrees, tests, review, and acceptance verification.
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

## Running Unattended

The two flows can run as scheduled loops over an issue tracker, with agents filing every issue. Three phases:

1. **Ready**: turn ideas and specs into agent-ready issues. The agent filing an issue judges it at creation: decision-complete work gets `agent:ready`; a real problem with open decisions gets `needs:spec`. Nothing unjudged enters the tracker.
2. **Work**: a scheduled agent claims one `agent:ready` issue and runs `task-to-pr` to a draft PR.
3. **Review**: a human reviews the PR, `pr-to-ready` drives feedback to merge-ready, a human merges.

### Definition of Ready

An issue is agent-ready when a fresh agent could finish it without asking questions:

- Goal stated as an outcome, not an implementation.
- Enough context to execute with no prior session.
- Testable acceptance criteria.
- A concrete, runnable verify step.
- Decision-complete: no open product or design decisions.

### Labels

Namespaces separate dimensions: `agent:*` is the state machine, `needs:*` is what an issue waits on, `risk:*` and `type:*` are metadata set when the issue is filed.

- `needs:spec`: real problem, open decisions. The spec loop picks it up.
- `agent:ready`: meets the definition of ready. The work loop claims it.
- `agent:working`: claimed by a worker. A claim with no linked branch or PR activity after 24 hours is stale; release it back to `agent:ready`.
- `agent:complete`: PR open, awaiting human review. The work loop's throttle counts these.
- `blocked`: waiting on another issue, linked in the body. Remove when the blocker closes.
- `needs:human`: an agent hit a decision only a human can make, explained in a comment.
- `risk:low` / `risk:high`: blast radius if the work goes wrong, judged at filing. Unattended loops claim `risk:low` only.
- `type:feature` / `type:bug` / `type:chore`: optional classification for reporting; not part of the loop.

Humans flip `needs:spec` to `agent:ready` after spec review, review PRs, and merge. Agents do everything else. Full label reference: `guides/labels.md`. Setup and sample prompts: `guides/loops.md`.

## Guidance

- Design docs default to `docs/<design-slug>/design.md`.
- One spec per feature, at `docs/<feature-slug>/spec.md`.
- Specs are durable; plans are transport. A plan goes to exactly one destination: tracker issues when the user asks or the repo runs an unattended loop, `docs/<feature-slug>/plan.md` when there is a feature directory, chat otherwise.
- If the task, spec, or plan is wrong, stop and update it. Do not push through.
- Tests are the verification mechanism; review checks they are real.
- Density over length.

## Out of Scope

Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.
