# Blueprint

A Claude Code plugin that encodes the software development lifecycle as executable commands.

Seven commands. No framework to learn. Just the workflow every good engineering team already follows.

## Why Blueprint?

Most agentic coding frameworks add enormous complexity — dozens of commands, multi-stage review pipelines, anti-rationalization tables — solving problems that don't exist while creating new ones.

Blueprint takes the opposite stance: **agents are smart. Treat them that way.**

As models get more capable, the right move is to simplify your instructions, not add more. A clear 50-line skill outperforms a 500-line skill full of warnings and iron laws — because the agent spends its attention on the work instead of navigating the rules. Workflow beats prompts.

```mermaid
graph LR
    A[Requirements] --> B[Architecture]
    B --> C[Plan]
    C --> D[Execute]
    D --> E[Review]
    E --> F[Ship]
```

## Install

```
/plugin marketplace add owainlewis/blueprint
/plugin install blueprint@owainlewis-blueprint
```

## Commands

All document commands take explicit file paths — you decide where things live.

### 1. Requirements

Turn rough notes into a structured requirements document. The agent acts as a technical PM — it will ask clarifying questions before producing the doc.

```
/blueprint:requirements REQUIREMENTS.md I need a CLI tool that parses markdown and generates HTML
```

### 2. Architecture

Turn a requirements doc into a technical architecture design. Covers system design, components, data flow, key decisions, and file structure.

```
/blueprint:architecture REQUIREMENTS.md ARCHITECTURE.md
```

### 3. Plan

Break an architecture into phased, executable tasks. Each task is self-contained — written so an agent (or engineer) with zero prior context can pick it up and start working.

```
/blueprint:plan REQUIREMENTS.md ARCHITECTURE.md TASKS.md
```

### 4. Task

Pick up a single task and execute it. Accepts a ticket ID from any tracker (Linear, Jira, GitHub) or a plain description. Creates a branch, does the work, verifies the acceptance criteria, and commits.

```
/blueprint:task LIN-123
/blueprint:task "add rate limiting to the API"
```

### 5. Code Review

Review your changes like a senior engineer before shipping. Checks correctness, security, simplicity, and robustness.

```
/blueprint:code-review
/blueprint:code-review src/auth.py
/blueprint:code-review security
```

If your project has a `REVIEW.md` in the root, those concerns are automatically included in every review. This is optional — the review works fine without one, but it's a good way to encode things your team has learned the hard way:

```markdown
# Review Concerns
- All database queries must use parameterized statements
- API responses must include a request_id for tracing
- No synchronous HTTP calls inside request handlers
```

**When to use this vs Claude Code built-ins:**

| | `/blueprint:code-review` | `/review` | `/simplify` |
|---|---|---|---|
| **Focus** | Correctness, security, robustness | General code review | Code clarity and maintainability |
| **Project context** | Reads REVIEW.md for project-specific concerns | No project-specific context | No project-specific context |
| **Output** | Grouped findings (must fix / should fix / observations) | Inline suggestions | Refactored code |
| **Best for** | Pre-ship review of a complete change | Quick feedback on any code | Cleaning up code that works but is messy |

Use them together: `/blueprint:code-review` to catch real problems, then `/simplify` to clean up what's left.

### 6. Branch

Create a feature branch with conventional naming.

```
/blueprint:branch feature markdown-parser
/blueprint:branch fix login-redirect
```

### 7. Commit

Stage and commit with a conventional commit message. Reviews the diff and writes the message for you.

```
/blueprint:commit
```

## Example

The [`examples/`](examples/) folder shows the full pipeline for a real project — a Python RAG chatbot API. Start with the [raw notes](examples/input.md) and see what each stage produces:

1. [input.md](examples/input.md) — rough project notes
2. [REQUIREMENTS.md](examples/REQUIREMENTS.md) — structured requirements
3. [ARCHITECTURE.md](examples/ARCHITECTURE.md) — technical design
4. [TASKS.md](examples/TASKS.md) — phased implementation plan

## Local Development

```bash
claude --plugin-dir /path/to/blueprint
```

## Learn More

I cover all of this in more depth at: https://www.skool.com/aiengineer
