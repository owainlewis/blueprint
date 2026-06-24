---
name: bootstrap-project
description: "Bootstrap a new or empty project repository with a local skeleton: README, license, .gitignore, AGENTS.md, docs, and optional commit or push only when explicit. Interview the repo creator when file-changing decisions are unclear."
user-invocable: true
argument-hint: "<project idea, repo path, or bootstrap scope>"
---

# Bootstrap Project

Turn a new or empty repository into a local project skeleton.
Keep the work local unless the user explicitly asks for commit, push, or remote setup.
Inspect first, ask only for file-changing decisions, then write the smallest baseline.
Do not invent product direction, ownership, or external workflow.

## Workflow

### 1. Inspect First

- Confirm the project root, git state, current branch, remotes, and meaningful existing files.
- Detect language/framework hints from files already present.
- Check for existing `README.md`, `LICENSE`, `.gitignore`, `AGENTS.md`, and `docs/`.
- Stop before overwriting project identity, docs, license, or agent guidance.
- Ignore unrelated files and never touch secrets, vendored files, generated files, dependency directories, lockfiles, or changelogs unless the user explicitly asks and the bootstrap requires it.

### 2. Ask Only Necessary Questions

Ask one question at a time, with a recommended answer, only when the answer changes the baseline:

- project name and one-sentence purpose, if `README.md` needs project identity;
- license choice, if `LICENSE` should be created;
- whether to initialize git, if the directory is not already a repo;
- repo-specific agent guidance or constraints, if `AGENTS.md` is missing or too generic;
- remote URL, commit, or push intent, only when the user explicitly requested that work.

Do not ask what the repo already answers.
If the user says to use defaults, create a minimal local baseline only: `README.md`, appropriate `.gitignore`, lightweight `AGENTS.md`, docs only when they add supplied context, no public claims, no remote setup, no commit, and no push.

### 3. Create Or Update The Skeleton

Create or update chosen baseline files:

- `README.md`: project identity, status, and links to useful docs.
- `LICENSE`: chosen license.
- `.gitignore`: language and platform defaults.
- `AGENTS.md`: repo-specific agent instructions and project constraints.
- `docs/`: short notes only when the user supplied enough context.

For long Markdown files, put each full sentence on its own physical line.
Prefer editing existing files over replacing them wholesale, and preserve existing identity.

### 4. Commit And Push Only When Explicit

- Stage only intended bootstrap files.
- If asked to commit, create one Conventional Commit.
- If asked to push, confirm the branch and remote first.
- Never stage secrets, `.env`, keys, generated or vendored files, dependency directories, or unrelated changes.

### 5. Report

Report files changed, repo state, remote state, commit hash if committed, push status if pushed, and next action.

## Rules

- Prefer defaults, but never guess external ownership.
- Do not create external services, tracker artifacts, licenses, or public-facing claims without enough user intent.
- Do not turn a vague idea into fake product docs.
- Do not overwrite existing docs or project identity without explicit permission.
- Keep the skeleton small.
- Leave the repo ready for `spec`, `plan`, or `task-to-pr`.
