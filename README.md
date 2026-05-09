# Blueprint

> World-class software engineering and agentic engineering, encoded as a workflow agents can follow.

Blueprint is the SDLC done right for AI coding agents. Spec before code. Plan before implement. Test before ship. Review before merge. The practices excellent engineering teams have always followed, distilled into six skills an agent can execute reliably.

It is the deliberate opposite of guardrail-heavy frameworks that try to constrain agents into producing good work. Blueprint bets on the model and encodes the workflow. Every model improvement makes that bet pay off more, not less.

## Principles

- **Encode process, not knowledge.** Skills are workflows. Reference material lives elsewhere.
- **Verification is non-negotiable.** Tests prove the spec. Review checks the tests are real.
- **Bet on the model.** Smart agents, not heavy guardrails. Every model improvement makes guardrails less necessary and more likely to conflict with the model's own judgment.
- **Density over length.** Skills are as short as they can be while remaining clear. The `compress` skill keeps them honest.
- **Six skills, not sixty.** Saying no is the discipline.

## The Shape

| Phase | Skill | What it does |
|---|---|---|
| **Define** | `spec` | One document with requirements and design |
| **Plan** | `plan` | Break a spec into 3-5 agent-sized tasks |
| **Build** | `implement` / `tdd` | Execute one task; tests prove acceptance |
| **Review** | `review` | Correctness, security, simplicity before merge |
| **Maintain** | `compress` | Keep skills tight; the meta-skill |

## The Flow

```mermaid
flowchart TD
    Start([Feature or task]) --> Spec[spec<br/>requirements + technical design<br/>one document]
    Spec --> Plan[plan<br/>break into 3-5 agent-sized tasks]
    Plan --> Linear[Push tickets to Linear<br/>tickets are the state]
    Linear --> Loop{For each ticket}
    Loop --> Implement[implement<br/>read spec first, then do work]
    Implement --> Tests[tests pass<br/>tests prove acceptance criteria]
    Tests --> Review[review<br/>correctness, security, simplicity]
    Review --> Decision{spec still right?}
    Decision -->|Yes| Ship[PR or merge]
    Decision -->|No, drifted| Respec[update spec -> re-run plan]
    Respec --> Plan
    Ship --> Loop
    Loop -->|All tickets done| Done([Feature shipped])
```

**If implementation reveals the spec is wrong, stop.** Update the spec, then re-run `plan` against the updated spec. Do not push through a stale plan. Re-planning costs minutes; pushing through a wrong plan costs the rest of the feature.

**Tests are the verification.** Blueprint does not run a separate "did the implementation match the spec?" pass. The spec defines the testing strategy. The implementation produces tests that prove the requirements. Review checks the tests are real and not theatre. If you want stronger verification, write the additional concerns into `REVIEW.md`; the review skill will pick them up.

## Commands and Skills

Blueprint exposes two surfaces. **Slash commands** (`/blueprint:plan`, `/blueprint:implement`, etc.) are what you type. **Skills** (`skills/plan/`, `skills/implement/`, etc.) are how those commands are implemented. The vocabulary is shared; the command and skill for a given verb have the same name.

| Command | Skill | Purpose |
|---|---|---|
| `/blueprint:spec` | `skills/spec/` | Write a spec |
| `/blueprint:plan` | `skills/plan/` | Break a spec into 3-5 tasks |
| `/blueprint:implement` | `skills/implement/` | Execute a single task |
| `/blueprint:tdd` | `skills/tdd/` | Test-first variant of implement |
| `/blueprint:review` | `skills/review/` | Local code review |
| `/blueprint:compress` | `skills/compress/` | Shorten agent-facing instructions |
| `/blueprint:branch` | Thin command, no skill | Create a feature branch |
| `/blueprint:commit` | Thin command, no skill | Conventional commit |

`branch` and `commit` are mechanical enough that they do not need skills backing them. They can exist as thin commands in tools that support slash-command files.

`/blueprint:build` is deprecated. Use `/blueprint:implement`; the old name was retired because "build" collides with project build steps and CI vocabulary.

The old `/blueprint:requirements`, `/blueprint:architecture`, and `/blueprint:task` commands are removed. Requirements and architecture now live together in `/blueprint:spec`; task execution is `/blueprint:implement`.

## Install

```bash
npx skills add owainlewis/blueprint
```

Install Blueprint with the `skills` CLI. The skills are plain Markdown and can be used from Claude Code, Codex, Cursor, Windsurf, GitHub Copilot, and other agents that support local instructions or reusable workflows.

See [docs/getting-started.md](docs/getting-started.md) for the universal install path and tool-specific setup notes.

## Update

```bash
npx skills update
```

Run this to update Blueprint and your installed skills to the latest version.

## Skills

| Skill | What it does | Example |
|---|---|---|
| `spec` | Writes `docs/<feature-slug>/spec.md`: requirements and design in one document | `Write a spec for user-auth` |
| `plan` | Breaks a spec into tasks sized for agents, review, and rollback | `Create a plan for user-auth` |
| `implement` | Executes one task after reading the spec first | `Implement LIN-123 from user-auth` |
| `tdd` | Implements behavior test-first | `Use TDD for retry logic in the API client` |
| `review` | Reviews specs or code for correctness, security, simplicity, robustness, and tests | `Review the current diff` |
| `compress` | Shortens agent-facing instructions without changing behavior | `Compress docs/user-auth/spec.md` |

## Agent Instructions

Blueprint creates instructions for agents. Sometimes that instruction is a one-sentence prompt. Sometimes it is a Linear ticket. Sometimes it is a markdown spec in the repo. The format should match the work.

One spec lives at `docs/<feature-slug>/spec.md`. External requirements flow into it; the spec is the artifact that brings context into the codebase.

State lives in Linear, not in the repo. No `state.md`, no handoff file. The ticket is the state.

Use the full pipeline for work that touches contracts, schemas, multiple files, or invariants. For trivial changes, just do them. For exploration, explore without manufacturing fake specs, plans, or tickets.

## Philosophy

**Specs are prompts with weight.** A spec is an instruction with enough structure to make decisions reviewable. Once the code is right, the spec's job is done.

**Do not confuse planning with prompting.** Professional teams do planning in the systems they already use: issue trackers, docs, design reviews, meetings, and PRs. Blueprint turns that context into the distilled instruction an agent needs.

**Compress context.** Every word competes for attention. Cut restated rules, overlap, padding, and preamble. Keep constraints, exact names, commands, paths, schemas, and examples that carry meaning.

**Agent inputs only.** Blueprint is not an issue tracker, architecture review board, or release process. It turns external context into high-quality instructions for coding agents. That's the entire job.

## Example

The [examples/](examples/) folder shows the planning output for a Python RAG chatbot API:

1. [input.md](examples/input.md): rough project notes
2. [spec.md](examples/rag-chatbot/spec.md): the spec
3. [plan.md](examples/rag-chatbot/plan.md): ordered tasks

## Learn More

https://www.skool.com/aiengineer
