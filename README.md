# Blueprint

> The software development lifecycle, encoded as skills for AI coding agents.

## Why Blueprint

Most agentic coding frameworks are built on a flawed assumption: that AI agents are unreliable and need hundreds of lines of rules to produce good work. So they add guardrails on guardrails — specialized agents watching other agents, multi-stage orchestration pipelines, permission matrices — until the tooling itself becomes the bottleneck.

**Blueprint takes the opposite stance: agents are smart. Treat them that way.**

A clear 50-line skill outperforms a 500-line skill full of warnings. The agent spends its attention on your work instead of navigating rules. As models improve, heavy frameworks fight the improvement. Simple workflows ride it.

11 skills. You can read the entire framework in 15 minutes.

## How It Works

Blueprint encodes two things: a **planning pipeline** that turns rough ideas into executable tasks, and a **build cycle** that implements them with quality built in.

```
    ┌─────────────────────────────────────────────────────────┐
    │                   PLANNING PIPELINE                     │
    │                                                         │
    │   Rough notes ──▶ Requirements ──▶ Architecture ──▶ Plan│
    └─────────────────────────────────────┬───────────────────┘
                                          │
                                          ▼
    ┌─────────────────────────────────────────────────────────┐
    │                     BUILD CYCLE                         │
    │                                                         │
    │   For each task:                                        │
    │   ┌──────┐   ┌──────┐   ┌────────┐   ┌────────┐       │
    │   │ Code ├──▶│ Test ├──▶│ Review ├──▶│ Commit │       │
    │   └──────┘   └──────┘   └────────┘   └────────┘       │
    │                                                         │
    │   Then: full test suite ──▶ final review ──▶ ship       │
    └─────────────────────────────────────────────────────────┘
```

Run the full cycle with one command (`/blueprint:build`) or use individual skills when you want control over a specific step.

## Install

### Claude Code (plugin marketplace)

```
/install owainlewis/blueprint
```

### npx skills (Claude Code, Codex, Cursor, OpenCode, and 40+ others)

```bash
npx skills add owainlewis/blueprint -a claude-code -g
```

## Skills

### Planning

All planning skills organize artifacts into `docs/<feature>/` — one directory per feature, no collisions.

| Skill | What it does | Example |
|-------|-------------|---------|
| **requirements** | Turn rough notes into structured, testable requirements | `/blueprint:requirements user-auth I need login with OAuth` |
| **architecture** | Turn requirements into a technical design with components, data flow, and file structure | `/blueprint:architecture user-auth` |
| **plan** | Break architecture into phased, atomic tasks with self-contained context | `/blueprint:plan user-auth` |

### Building

| Skill | What it does | Example |
|-------|-------------|---------|
| **build** | Execute a full task plan: code, test, review, and commit each task, then final review | `/blueprint:build user-auth` |
| **task** | Pick up and execute a single task | `/blueprint:task "add rate limiting to the API"` |
| **tdd** | Build test-first: failing tests, then implementation, then simplify | `/blueprint:tdd "retry logic for API client"` |

### Quality

| Skill | What it does | Example |
|-------|-------------|---------|
| **review** | Code review — correctness, security, simplicity, robustness | `/blueprint:review` |
| **refactor** | Simplify code without changing behavior | `/blueprint:refactor src/api/routes.py` |
| **coverage** | Fill test gaps with tests that catch realistic bugs | `/blueprint:coverage src/auth/` |
| **debug** | Systematic root-cause debugging: observe, hypothesize, test, fix | `/blueprint:debug "API returns 500 on POST"` |

### Git

| Skill | What it does | Example |
|-------|-------------|---------|
| **commit** | Stage and commit with a conventional commit message | `/blueprint:commit` |

## Philosophy

**Workflow beats prompts.** The value isn't in clever prompt engineering — it's in encoding the right sequence. Requirements before architecture. Architecture before code. Tests alongside implementation. Review before ship. Get the sequence right and the agent does the rest.

**Simplicity is a feature.** Every skill is under 100 lines. Not because we couldn't write more, but because more is worse. One focused review that checks correctness, security, and simplicity catches more real bugs than 16 agents generating noise.

**Bet on the model.** Frameworks that micromanage agents with hundreds of rules are building on sand. Every model improvement makes those rules less necessary and more likely to conflict with the model's own judgment. Blueprint gives clear goals and gets out of the way. That approach gets better over time, not worse.

**Core SDLC only.** Blueprint encodes the development lifecycle — planning, building, testing, reviewing, shipping. It does not include integrations with specific tools (Linear, Jira, Slack). Integrations are a separate concern and belong in separate plugins.

## Example

The [`examples/`](examples/) folder shows the full planning pipeline for a Python RAG chatbot API:

1. [input.md](examples/input.md) — rough project notes
2. [requirements.md](examples/rag-chatbot/requirements.md) — structured requirements
3. [architecture.md](examples/rag-chatbot/architecture.md) — technical design
4. [tasks.md](examples/rag-chatbot/tasks.md) — phased implementation plan

Regenerate the examples after changing skills:

```bash
./examples/regenerate.sh
```

## Updating

```
claude plugin update blueprint@owainlewis-blueprint
```

## Releasing (for contributors)

```bash
./release.sh patch   # 0.2.0 → 0.2.1
./release.sh minor   # 0.2.0 → 0.3.0
./release.sh major   # 0.2.0 → 1.0.0
```

## Local Development

```bash
claude --plugin-dir /path/to/blueprint
```

## Learn More

https://www.skool.com/aiengineer
