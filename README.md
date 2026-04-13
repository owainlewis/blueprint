# Blueprint

> The software development lifecycle, encoded as skills for AI coding agents.

## Why Blueprint

Most agentic coding frameworks assume AI agents are unreliable and need hundreds of lines of rules. So they add guardrails on guardrails — specialized agents watching other agents, multi-stage orchestration, permission matrices — until the tooling becomes the bottleneck.

**Blueprint takes the opposite stance: agents are smart. Treat them that way.**

A clear 50-line skill outperforms a 500-line skill full of warnings. As models improve, heavy frameworks fight the improvement. Simple workflows ride it.

12 skills. You can read the entire framework in 15 minutes.

## How It Works

```
    Idea ──▶ Spec ──▶ Build ──▶ Ship

    Where "Build" means:
    ┌──────┐   ┌──────┐   ┌────────┐   ┌────────┐
    │ Code ├──▶│ Test ├──▶│ Review ├──▶│ Commit │  (for each task)
    └──────┘   └──────┘   └────────┘   └────────┘

    Then: full test suite ──▶ final review ──▶ ship
```

Write a spec. Build it. Ship it. That's the flow.

```
/blueprint:spec user-auth add OAuth login with Google and GitHub
/blueprint:build user-auth
```

## Specs, Not Design Documents

**These docs are for agents, not humans.**

Your real design thinking happens elsewhere — in Confluence, on a whiteboard, in a Slack thread, in your head. What lands in the repo as markdown is the distilled brief an agent needs to build correctly. Not a design document. Not a PRD. A spec: what to build, how it fits in, what order to build it.

Blueprint uses a single spec document that combines requirements, design, and tasks in one place. Many frameworks split these into separate documents (requirements → architecture → implementation plan). That separation makes sense when different people own different phases — a PM writes requirements, an architect designs, an engineer plans. Three docs because three roles.

**An AI agent is all three roles.** It doesn't need hand-offs between phases. It doesn't need sign-off gates between documents. Splitting into three docs just means the same information gets restated three times in slightly different formats. A single spec forces the same rigorous thinking (what → how → tasks) in one pass, without the ceremony.

Keep specs short. If it's getting long, the feature is too big — split the feature, not the document.

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

| Skill | What it does | Example |
|-------|-------------|---------|
| **spec** | Write a spec — what to build, how, and in what order | `/blueprint:spec user-auth add OAuth login` |

Specs are written to `docs/<feature>/spec.md` — one directory per feature, no collisions.

<details>
<summary>Standalone planning skills (requirements, architecture, plan)</summary>

These skills are available for when you need them individually — generating standalone requirements, designing architecture for documentation, or producing a detailed task breakdown. They're not part of the main flow.

| Skill | What it does | Example |
|-------|-------------|---------|
| **requirements** | Turn rough notes into structured, testable requirements | `/blueprint:requirements user-auth I need login with OAuth` |
| **architecture** | Turn requirements into a technical design | `/blueprint:architecture user-auth` |
| **plan** | Break architecture into phased, atomic tasks | `/blueprint:plan user-auth` |

</details>

### Building

| Skill | What it does | Example |
|-------|-------------|---------|
| **build** | Execute a spec: code, test, review, and commit each task, then final review | `/blueprint:build user-auth` |
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

**Workflow beats prompts.** The value isn't in clever prompt engineering — it's in encoding the right sequence. Spec before code. Tests alongside implementation. Review before ship. Get the sequence right and the agent does the rest.

**Simplicity is a feature.** One focused review catches more real bugs than 16 agents generating noise. One spec doc beats three separate documents. If the spec is getting long, split the feature — not the document.

**Bet on the model.** Frameworks that micromanage agents with hundreds of rules are building on sand. Every model improvement makes those rules less necessary. Blueprint gives clear goals and gets out of the way.

**Docs are for agents.** Your real design thinking happens elsewhere — Confluence, whiteboards, conversations. What lands in markdown is the minimum an agent needs to build correctly.

**Core SDLC only.** Blueprint encodes the development lifecycle — planning, building, testing, reviewing, shipping. Integrations with specific tools (Linear, Jira, Slack) are a separate concern and belong in separate plugins.

## Example

The [`examples/`](examples/) folder shows the planning output for a Python RAG chatbot API:

1. [input.md](examples/input.md) — rough project notes
2. [spec.md](examples/rag-chatbot/spec.md) — the spec an agent would use to build it

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
