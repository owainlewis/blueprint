---
name: bootstrap-project
description: "Bootstrap a new or empty project repository with clean defaults: README, license, .gitignore, AGENTS.md, docs, optional PRD/roadmap, tracker issues or board, initial commit, and optional remote setup. Interview the repo creator when product, license, tracker, or GitHub/Linear setup decisions are unclear."
user-invocable: true
argument-hint: "<project idea, repo path, tracker preference, or bootstrap scope>"
---

# Bootstrap Project

Turn a new or empty repository into a ready-to-build project skeleton.
Do not invent product direction or external setup decisions.
Inspect first, ask only for decisions that change what gets created, then write the smallest useful baseline.

## Workflow

### 1. Inspect

- Confirm the project root, git state, current branch, remotes, and existing files.
- Detect language/framework hints from files already present.
- Check for existing `README.md`, `LICENSE`, `.gitignore`, `AGENTS.md`, `docs/`, issue templates, and tracker references.
- If a remote or tracker is mentioned, inspect what exists before creating anything.
- Stop before overwriting meaningful existing project identity, docs, license, or tracker setup.

### 2. Interview The Creator

Ask one question at a time, with a recommended answer, only when the answer changes the baseline.

Ask when unclear:

- project name and one-sentence purpose;
- whether to initialize git;
- whether to create or attach a GitHub repo;
- whether to push the initial baseline;
- license choice;
- tracker choice: GitHub Issues, GitHub Project, Linear, none, or later;
- whether a product PRD is known enough to write now;
- whether roadmap tasks should be created now or left as docs;
- repo-specific agent guidance or constraints.

Do not ask what the repo already answers.
If the user says to use defaults, use conservative defaults: git initialized, MIT license for open-source personal projects, minimal README, `AGENTS.md`, `docs/`, no remote creation unless a repo name or URL is explicit, no tracker items unless the work is already split.

### 3. Create The Skeleton

Create or update only the files needed for the chosen baseline:

- `README.md`: minimalist project identity, status, and links to docs.
- `LICENSE`: chosen license.
- `.gitignore`: language and platform defaults.
- `AGENTS.md`: repo-specific agent instructions and project constraints.
- `docs/prd.md`: only when product direction is known enough.
- `docs/roadmap.md`: only when the work can be split into agent-sized tasks.
- `docs/prompt.md` or loop prompts: only when the user wants a coordinator/work loop.

Keep docs plain and practical.
For long Markdown files, put each full sentence on its own physical line.

### 4. Set Up Tracker

If requested, create tracker artifacts from the roadmap:

- GitHub Issues: one issue per task, with goal, context, acceptance criteria, verify, and out of scope.
- GitHub Project: create or reuse a board, link it to the repo, add issues, and set initial status.
- Linear: create issues in the selected team/project when access and conventions are clear.

Do not create duplicate issues or boards.
Do not invent tracker states, labels, teams, or milestones.
If setup requires permissions or missing identifiers, ask or report the exact blocker.

### 5. Commit And Push

- Stage only intended bootstrap files.
- Do not stage secrets, `.env`, keys, generated dependency directories, or unrelated local changes.
- Create one Conventional Commit, usually `docs: bootstrap project` or `chore: bootstrap project`.
- Push only when the user asked for it or the bootstrap request explicitly included remote setup.

### 6. Report

Report:

- files created or changed;
- repo and remote state;
- tracker or board links;
- commit hash, if committed;
- push status, if pushed;
- the next recommended action.

## Rules

- Prefer defaults, but never guess external ownership decisions.
- Do not create a GitHub repo, Linear project, license, or public-facing product claim without enough user intent.
- Do not turn a vague idea into a fake PRD.
- Do not overwrite existing docs or project identity without explicit permission.
- Keep the skeleton small.
- Leave the repo ready for `spec`, `plan`, or `task-to-pr`.
