# Blueprint

Blueprint is a small, principles-first workflow for AI coding.

Agents are already good at writing code. They need clear decisions, bounded work, real proof, and independent review. Blueprint provides those boundaries without turning engineering into a catalogue of tiny skills.

## The model

There are three layers:

1. **Repository instructions define policy.** `AGENTS.md` says what good work means in a codebase.
2. **Skills define phases.** Each skill has one durable engineering outcome.
3. **Commands compose workflows.** `/implement` takes one task through the phases to a pull request.

```text
idea -> design -> plan -> task
                         |
                         v
              /implement task
                  code -> test -> review -> improve
                    ^                         |
                    +-------------------------+
                         |
                         v
                  green pull request
                         |
                         v
                     human merge
```

Use only the phases the work needs. A small, decided task can start at `/implement`. A costly or unclear change should start at `design`. A large design can go through `plan` before implementation.

## Principles

- **Encode process, not knowledge.** Skills define outcomes and boundaries. Agents choose the local mechanics.
- **One skill per phase.** A skill should represent a reusable mode of work, not one shell command or one job title.
- **Workflows compose phases.** Ticket lookup, worktrees, commits, pull requests, CI, and feedback are one delivery workflow.
- **Proof is part of the work.** Acceptance criteria map to tests or explicit manual evidence. Browser behavior is checked in a real browser.
- **Review must be independent.** A fresh subagent reviews the diff and its proof. A named reviewer persona adds little value.
- **The source of truth can change.** When implementation exposes a bad requirement, update the ticket or design before continuing.
- **Prefer less.** Keep the smallest complete change, the shortest useful instruction, and no duplicate entry points.
- **Humans own irreversible judgment.** Agents prepare a green PR. A human merges unless they explicitly delegate it.

## Skills

| Skill | Outcome | Stops when |
| --- | --- | --- |
| `design` | A reviewed description of what, why, requirements, acceptance criteria, technical design, constraints, risks, and scope | The design is written for human review |
| `plan` | Ordered, agent-ready tasks and optional milestones | The tasks are ready to hand off |
| `test` | Acceptance criteria and important failures have evidence | Each criterion is pass, fail, or explicitly unverified |
| `review` | A fresh subagent has independently reviewed the change | Findings and a verdict are reported |
| `improve` | Existing code is clearer, simpler, and better structured without changing intended behavior | Relevant tests prove behavior was preserved |

There is no `build` skill. Writing code is a base agent capability. There are no separate skills for branching, committing, opening a PR, debugging, TDD, browser checking, or addressing feedback. Those are techniques or steps inside a phase or workflow.

## `/implement`

`commands/implement.md` is the canonical end-to-end workflow. Give it one ticket, task, or existing PR. It:

1. resolves the task or PR, creating a ticket only for new work when GitHub is available;
2. resumes an existing PR branch and worktree, or creates a ticket- or task-named branch and worktree from the latest remote default branch;
3. inspects, plans, and writes the smallest complete code change;
4. runs `test`, including real-browser verification when relevant;
5. runs `review` with a fresh subagent;
6. addresses valid findings, then repeats tests and review until clean;
7. creates Conventional Commits, pushes, and opens a ready PR;
8. waits for CI and feedback, fixes important findings, and replies with evidence;
9. stops at a green, mergeable PR for a human to merge.

The same workflow is written in `AGENTS.md` so agents that do not support slash commands still follow it. Tool-specific command locations are adapters, not new product concepts.

## Install

Install the five skills:

```bash
npx skills add owainlewis/blueprint
```

Copy `commands/implement.md` to the custom-command directory used by your coding tool, or invoke it as an ordinary prompt. Keep `AGENTS.md` in the repository as the portable fallback.

If you installed an older Blueprint release, read [MIGRATION.md](MIGRATION.md). Skill updaters may leave removed directories behind, so updating alone may not give you the new five-skill surface.

## Examples

The RAG chatbot example shows the full decision flow:

1. [rough input](examples/input.md)
2. [reviewed design](examples/rag-chatbot/design.md)
3. [captured chat plan](examples/rag-chatbot/plan.md)

The [Dispatch control-plane design](examples/dispatch-control-plane/design.md) is a larger architecture example.

## What Blueprint is not

Blueprint is not an issue tracker, agent framework, release system, reviewer persona library, or unattended state machine. It is a compact set of phase instructions plus one normal code-delivery workflow.
