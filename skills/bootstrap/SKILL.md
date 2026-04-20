---
name: bootstrap
description: "Scaffold a new project from minimal, opinionated defaults: uv for Python, bun + Next.js for TypeScript. Use when the user says bootstrap, scaffold, new project, new service, or new app."
user-invocable: true
argument-hint: "<project-type> <project-name> e.g. 'python my-service' or 'nextjs my-app'"
---

# Bootstrap a Project

Scaffold a new project with minimal, opinionated defaults. Stop after scaffolding — do not build features.

## Defaults

- **Python** → `uv`, `pydantic-settings`, PostgreSQL when a DB is needed
- **TypeScript** → `bun`, Next.js (App Router)

## Input

The user provides: `$ARGUMENTS`

The first argument is the project type (`python`, `nextjs`, `cli`, `library`). The second is the project name. If either is missing, ask for it. If both are provided and no deviations from the defaults are mentioned, proceed without further questions.

Only ask about deviations if the user's message suggests them ("use MySQL instead of Postgres", "skip pydantic-settings", etc.).

## Process

1. **Target directory check.** The scaffold writes to `./<project-name>/`. If that directory exists and is non-empty, stop and report — do not overwrite. Create the directory and `cd` into it.

2. **Prerequisites.** Every scaffold needs `just`. Check `command -v just`; if missing, `brew install just` on macOS (see https://github.com/casey/just#installation otherwise).

   Stack-specific:
   - Python: `command -v uv` or `brew install uv`
   - TypeScript: `command -v bun` or `brew install oven-sh/bun/bun`

3. **Pin the latest stable versions.** Don't guess from memory:
   - Python: `uv self update && uv --version`
   - TypeScript: `bun upgrade && bun --version`
   - Next.js: invoke via `npx create-next-app@latest` — the `@latest` tag is the pin

4. **Scaffold** the project using the templates below.

5. **First commit:** `git init && git commit -m "chore: initial scaffold"`.

6. **Stop.** Do not write features. Do not add example code.

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
