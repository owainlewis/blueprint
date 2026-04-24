---
name: init
description: "Scaffold a new project from your standards. Use when starting a greenfield repo so the agent applies your preferred setup, tooling, and repo hygiene instead of inventing defaults."
user-invocable: true
argument-hint: "<project-name or brief> e.g. 'support-inbox AI API for triaging customer email'"
---

# Init

## When to use

- Starting a new repo from scratch
- Turning a brief or spec into the first working scaffold
- Applying your standard setup without restating the same preferences

## Inputs

1. Use `$ARGUMENTS`, the current brief, or the current spec as the project description.
2. Read [references/python-service.md](references/python-service.md) for the built-in Python service defaults.
3. If `~/.agents/stacks/python-service.md` exists, read it and let it override the built-in Python reference.
4. If the request is not a Python service or API, stop and ask for an explicit supported stack or a new stack reference.

## Questions

Ask at most three concise questions in one message, and only if the answer is missing from the brief or spec:

- project name
- repo visibility, if creating a GitHub repo
- any deviations from the stack defaults

Do not ask about standard tool choices already defined by the stack.

## Process

1. Read the brief or spec first. Infer project needs from the requirements instead of asking setup questions the stack already answers.
2. Load the Python service reference and any user override.
3. Infer conditional choices from the requirements:
   - If persistence is needed, use PostgreSQL.
   - If retrieval or RAG is needed, use PostgreSQL with `pgvector`.
   - If no persistence is implied, do not add database code.
4. Check the latest stable versions of the core dependencies before pinning them. Do not rely on remembered versions.
5. Generate the smallest working scaffold that follows the stack defaults.
6. Write `AGENTS.md` with the standard `just` commands and repo rules so future agents inherit the same workflow.
7. Run the strongest relevant verification before finishing.
8. If asked, initialize git, make the first commit, and create the GitHub repo.

## Output

Generate the standard project files, tool configuration, minimal app code, tests, and an `AGENTS.md` that tells future agents to use the `just` commands first.

## Rules

- Keep the scaffold lean. No empty folders, placeholder features, or speculative dependencies.
- Prefer standards over invention.
- Use FastAPI, `pydantic-settings`, `uv`, `ruff`, `pyright`, `pytest`, and `just` for Python services.
- If a database is needed, default to PostgreSQL.
- Document every required environment variable in `.env.example`.
- Stop after scaffolding. Do not build product features.

## Verification

- `just build`
- `just test`
- `just check`
- The app starts without import or settings errors
- No secrets are committed
