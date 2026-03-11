# Blueprint

A Claude Code plugin that encodes the standard software development lifecycle as executable commands.

Six commands. No framework to learn. Just the same process every good engineering team already follows.

## Why not the other spec frameworks?

Most "agentic development" frameworks massively overcomplicate a simple process. Dozens of commands, custom DSLs, novel methodologies — solving problems that don't exist while ignoring the one that does: discipline.

The way we build software hasn't changed. Requirements. Design. Plan. Build. Review. Ship. This process works whether you're a team at Google, a solo founder, or an AI agent. Adding agents to the loop doesn't mean we need to reinvent software engineering from scratch — it just means we move faster.

Blueprint has six commands because that's all you need. If your spec framework requires a tutorial to understand, it's the framework that's the problem.

```mermaid
graph LR
    A[Requirements] --> B[Technical Design]
    B --> C[Task Breakdown]
    C --> D[Create Tickets]
    D --> E[Execute Ticket]
    E --> F[Commit & Ship]

    style A fill:#2d333b,stroke:#768390,color:#adbac7
    style B fill:#2d333b,stroke:#768390,color:#adbac7
    style C fill:#2d333b,stroke:#768390,color:#adbac7
    style D fill:#2d333b,stroke:#768390,color:#adbac7
    style E fill:#2d333b,stroke:#768390,color:#adbac7
    style F fill:#2d333b,stroke:#768390,color:#adbac7
```

This is the SDLC. It has worked for decades. Blueprint just makes each step a command.

## How it maps

| SDLC Phase | Traditional | Blueprint |
|---|---|---|
| **Requirements** | PM writes PRD, stakeholder reviews | `/blueprint:requirements` |
| **Technical Design** | Eng writes design doc, architecture review | `/blueprint:architecture` |
| **Planning** | Sprint planning, ticket breakdown | `/blueprint:plan` |
| **Execution** | Engineer picks up ticket, does the work | `/blueprint:task LIN-123` |
| **Git workflow** | Branch, commit, PR | `/blueprint:branch` + `/blueprint:commit` |

State lives in your project management tool (Linear, Jira, whatever), not in markdown files. Blueprint generates the docs and the plan, you create the tickets, then hand them to an agent one at a time.

## Install

```
/plugin marketplace add owainlewis/blueprint
/plugin install blueprint@owainlewis-blueprint
```

## Commands

```
/blueprint:requirements    Rough notes → REQUIREMENTS.md
/blueprint:architecture    Requirements → ARCHITECTURE.md
/blueprint:plan            Architecture → TASKS.md
/blueprint:task            Pick up a ticket, execute it, mark it done
/blueprint:branch          Create branch with conventional naming (feature/, fix/, docs/, ...)
/blueprint:commit          Stage and commit with conventional commit messages
```

## Usage

```
/blueprint:requirements I need a CLI tool that parses markdown and generates HTML
/blueprint:architecture
/blueprint:plan
  ... create tickets in Linear from TASKS.md ...
/blueprint:branch feature markdown-parser
/blueprint:task LIN-123
/blueprint:commit
```

## Local Development

```bash
claude --plugin-dir /path/to/blueprint
```
