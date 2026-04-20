---
name: bootstrap
description: "Scaffold a new project from minimal, opinionated defaults. Python uses uv, TypeScript uses bun and Next.js, PostgreSQL by default. Use when the user says bootstrap, scaffold, new project, new service, or new app."
user-invocable: true
argument-hint: "<project-type> <project-name> e.g. 'python my-service' or 'nextjs my-app'"
---

# Bootstrap a Project

Scaffold a new project with minimal, opinionated defaults. Stop after scaffolding — do not build features.

## Defaults

- **Python** → `uv`, `pydantic-settings`, PostgreSQL when a DB is needed
- **TypeScript** → `bun`, Next.js (App Router)

## Rule: Check Latest Versions

Before running any scaffolder, check the latest stable version of the tool or framework. Do not assume from memory. Pin to what's current today.

## Process

1. Check prerequisites. `just` is required for every scaffolded project. Run `command -v just`. If missing, install it before scaffolding (`brew install just` on macOS; see https://github.com/casey/just#installation otherwise).

2. Ask at most three questions, grouped:
   - What are we building? (CLI, service, library, web app)
   - What's the project name?
   - Any deviations from the defaults?

3. Check the latest versions of the tools you're about to use.

4. Scaffold the project using the templates below.

5. First commit: `git init && git commit -m "chore: initial scaffold"`.

6. Stop. Do not write features. Do not add example code.

## Templates

Every scaffolded project gets these files at the root.

### `justfile`

````just
default:
    @just --list

# Run the dev server
dev:
    @echo "Not implemented"

# Run tests
test:
    @echo "Not implemented"
````

Replace the placeholders with real commands once the project has something to run and test. Add more recipes (`lint`, `typecheck`, `check`) only when there's something to wire them to.

### `README.md`

````markdown
# <project-name>

<One paragraph: what this is and what it does.>

## Requirements

<Tools needed to run this project.>

## Run

```bash
just dev
```

## Test

```bash
just test
```
````

### `CLAUDE.md`

````markdown
# CLAUDE.md

## Core rule
**Always use `just`, not raw commands.**

## Development workflow
1. Make changes
2. Review your work and fix any issues you find
3. Run tests to confirm nothing is broken

## Architecture
(Where things live. Key decisions. Grows over time.)

## Corrections
(Empty at start. Add a rule every time a mistake is made that shouldn't repeat.)
````

### `LICENSE`

Add an MIT license. Use `git config user.name` for the copyright holder and the current year.

### Also included

- `.env.example` — documented variables if relevant (no real `.env`)
- `.gitignore` — appropriate to the stack

## Rules

- Minimal dependencies. Add nothing "just in case."
- No example routes, no sample data, no placeholder pages.
- If `~/.claude/STACK.md` exists, prefer its defaults over the ones here.
