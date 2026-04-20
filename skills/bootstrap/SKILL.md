---
name: bootstrap
description: "Scaffold a new project from minimal, opinionated defaults. Prefer uv for Python and bun + Next.js for TypeScript unless the user asks for something else. Use when the user says bootstrap, scaffold, new project, new service, or new app."
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

The first argument is the stack or project type. The second is the project name. If either is missing, ask for it. If both are provided and no deviations from the defaults are mentioned, proceed without further questions.

Only ask about deviations if the user's message suggests them ("use MySQL instead of Postgres", "skip pydantic-settings", etc.).

If the request is abstract (`cli`, `library`) and the language/runtime is not clear, ask one clarifying question before scaffolding. Do not invent a language when that choice would materially change the project.

## Process

1. **Target directory check.** The scaffold writes to `./<project-name>/`. If that directory exists and is non-empty, stop and report — do not overwrite. Create the directory and `cd` into it.

2. **Check prerequisites.** Inspect what tooling is already available for the requested stack.
   - If something required is missing, tell the user what is missing or ask before installing it.
   - Do not silently install packages, modify the user's global toolchain, or run global upgrade commands just to scaffold.

3. **Choose the scaffold.** Prefer the ecosystem's standard stable scaffolding flow for the requested stack. Do not guess version numbers from memory. Use the official or conventional bootstrap path for the stack instead of inventing structure from scratch.

4. **Scaffold** the project using the templates below and the chosen stack conventions.

5. **Git.** Initialize git and make the first commit if the directory is not already a git repo and the user has not asked otherwise.

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

### `LICENSE`

Add an MIT license. Use `git config user.name` for the copyright holder and the current year.

### Also included

- `.env.example` — documented variables if relevant (no real `.env`)
- `.gitignore` — appropriate to the stack
- An agent instruction file only if the user asks for one or the project already uses a shared convention for it

## Rules

- Minimal dependencies. Add nothing "just in case."
- No example routes, no sample data, no placeholder pages.
- Keep the generated structure small and unsurprising.
- If you make an assumption for an abstract request, state it clearly before scaffolding.
