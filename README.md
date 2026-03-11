# Blueprint

A Claude Code plugin for spec-driven development. Turns rough ideas into structured requirements, architecture docs, and atomic implementation plans — then helps you execute with clean git workflow.

## Commands

| Command | Description |
|---------|-------------|
| `/blueprint:requirements` | Transform rough notes into a structured requirements document (`REQUIREMENTS.md`) |
| `/blueprint:architecture` | Generate a technical architecture design from requirements (`ARCHITECTURE.md`) |
| `/blueprint:plan` | Break architecture into phased, atomic tasks with Linear export (`TASKS.md`) |
| `/blueprint:commit` | Stage and commit with conventional commit messages |
| `/blueprint:branch` | Create branches with conventional naming (`feature/`, `fix/`, `docs/`, etc.) |

## Workflow

```
rough idea
    │
    ▼
/blueprint:requirements    →  REQUIREMENTS.md
    │
    ▼
/blueprint:architecture    →  ARCHITECTURE.md
    │
    ▼
/blueprint:plan            →  TASKS.md (+ Linear export)
    │
    ▼
/blueprint:branch feature my-feature
    │
    ▼
  ... build each task ...
    │
    ▼
/blueprint:commit
```

## Install

Add the marketplace, then install the plugin:

```
/plugin marketplace add owainlewis/blueprint
/plugin install blueprint@owainlewis-blueprint
```

## Local Development

Test the plugin locally:

```bash
claude --plugin-dir /path/to/blueprint
```

Then use any command:

```
/blueprint:requirements I need a CLI tool that...
/blueprint:branch feature user-auth
/blueprint:commit
```

## Project Structure

```
blueprint/
├── .claude-plugin/
│   ├── plugin.json           # Plugin manifest
│   └── marketplace.json      # Marketplace manifest
├── skills/
│   ├── requirements/
│   │   └── SKILL.md          # /blueprint:requirements
│   ├── architecture/
│   │   └── SKILL.md          # /blueprint:architecture
│   ├── plan/
│   │   └── SKILL.md          # /blueprint:plan
│   ├── commit/
│   │   └── SKILL.md          # /blueprint:commit
│   └── branch/
│       └── SKILL.md          # /blueprint:branch
└── README.md
```
