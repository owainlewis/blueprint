# Blueprint

A Claude Code plugin that encodes the software development lifecycle as executable commands.

Six commands. No framework to learn. Just the workflow every good engineering team already follows.

## Why Blueprint?

Most agentic coding frameworks add enormous complexity — dozens of commands, multi-stage review pipelines, anti-rationalization tables — solving problems that don't exist while creating new ones.

Blueprint takes the opposite stance: **agents are smart. Treat them that way.**

As models get more capable, the right move is to simplify your instructions, not add more. A clear 50-line skill outperforms a 500-line skill full of warnings and iron laws — because the agent spends its attention on the work instead of navigating the rules. Workflow beats prompts.

```mermaid
graph LR
    A[Requirements] --> B[Architecture]
    B --> C[Plan]
    C --> D[Execute]
    D --> E[Ship]

    style A fill:#2d333b,stroke:#768390,color:#adbac7
    style B fill:#2d333b,stroke:#768390,color:#adbac7
    style C fill:#2d333b,stroke:#768390,color:#adbac7
    style D fill:#2d333b,stroke:#768390,color:#adbac7
    style E fill:#2d333b,stroke:#768390,color:#adbac7
```

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
/blueprint:task            Pick up a task, execute it, mark it done
/blueprint:branch          Create branch with conventional naming
/blueprint:commit          Stage and commit with conventional messages
```

## Usage

```
/blueprint:requirements I need a CLI tool that parses markdown and generates HTML
/blueprint:architecture
/blueprint:plan
/blueprint:branch feature markdown-parser
/blueprint:task LIN-123
/blueprint:commit
```

## Local Development

```bash
claude --plugin-dir /path/to/blueprint
```

## Learn More

I cover all of this in more depth at: https://www.skool.com/aiengineer
