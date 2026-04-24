# Python Service

## Purpose

Default scaffold for Owain's client AI Python services: modern, typed, minimal, and ready for an agent to extend without re-deciding the basics.

## Fixed Defaults

- Python 3.12+
- `uv` for dependency management and execution
- FastAPI for the service entrypoint
- `pydantic-settings` for configuration
- `just` for the command contract
- `ruff` for formatting and linting
- `pyright` for type checking
- `pytest` for tests
- `README.md`, `LICENSE`, `.gitignore`, `.gitattributes`, `.env.example`, GitHub CI, and `AGENTS.md` in every repo
- Commit the lockfile

## Conditional Defaults

- If persistence is needed, use PostgreSQL.
- If retrieval, embeddings, semantic search, or RAG are required, use PostgreSQL with `pgvector`.
- If no persistence is implied, do not add database code or dependencies.
- Do not add Docker unless the requirements clearly call for containerized deployment.

## Directory Shape

Create only the directories that contain real files on day one:

- `app/__init__.py`
- `app/main.py`
- `app/config.py`
- `tests/test_smoke.py`

Only add these when needed:

- `app/db.py` when the project needs a database
- `app/llm.py` when there is a real provider integration to wrap

Do not create `utils/`, `helpers/`, `common/`, `routers/`, or `services/` by default.

## Dependencies

Always pin the latest stable versions confirmed at scaffold time.

Default runtime dependencies:

- `fastapi`
- `pydantic`
- `pydantic-settings`
- `uvicorn`

Add only when required:

- `asyncpg` for PostgreSQL access

Default development dependencies:

- `pytest`
- `ruff`
- `pyright`

Do not add an ORM, task queue, vector SDK, or agent framework unless the requirements clearly justify it.

## Generated Files

Generate these files for every project:

- `.github/workflows/ci.yml`
- `AGENTS.md`
- `.env.example`
- `.gitattributes`
- `.gitignore`
- `LICENSE`
- `README.md`
- `justfile`
- `pyproject.toml`
- `pyrightconfig.json`
- `ruff.toml`
- `uv.lock`
- `app/__init__.py`
- `app/main.py`
- `app/config.py`
- `tests/test_smoke.py`

When a database is needed, also generate:

- `app/db.py`

## justfile

Use this command contract:

```makefile
build:
    uv sync

dev:
    uv run uvicorn app.main:app --reload

test:
    uv run pytest

lint:
    uv run ruff check .
    uv run ruff format --check .

typecheck:
    uv run pyright

check: build lint typecheck test

clean:
    find . -type d -name __pycache__ | xargs rm -rf
    rm -rf .pytest_cache .ruff_cache .pyright dist build
```

## AGENTS.md

Write a short `AGENTS.md` that captures the repo standards for future agents:

- prefer `just` commands over raw tool commands
- build: `just build`
- run the dev server: `just dev`
- test: `just test`
- lint: `just lint`
- typecheck: `just typecheck`
- full verification: `just check`
- use `pydantic-settings` for config
- if a database is present, it is PostgreSQL
- run `just check` before handing work back

## File Expectations

`README.md`

- one short paragraph explaining what the service does
- quick start with `just build`, `just dev`, and `just test`
- environment variable setup

`.env.example`

- document every required variable
- no real values or secrets

`pyrightconfig.json`

- strict mode
- include `app` and `tests`
- Python version `3.12`

`ruff.toml`

- enable linting and formatting
- keep the config small

`tests/test_smoke.py`

- one passing smoke test that proves the app imports and the root health path works if present

`.github/workflows/ci.yml`

- install Python and `uv`
- install `just`
- run `just check`

## Verification

The scaffold is complete when:

- `just build` succeeds
- `just test` passes
- `just check` passes
- the app starts without settings or import failures
- `.env.example` documents the required configuration
- no optional structure was added without a requirement
