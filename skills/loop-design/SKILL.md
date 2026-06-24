---
name: loop-design
description: "Write or tighten long-running Codex and Claude Code goals with clear done conditions, required checks, evidence, and stop rules."
user-invocable: true
argument-hint: "<rough goal, task, ticket, issue set, or prompt>"
---

# Loop Design

Turn a rough goal into clear instructions for Codex or Claude Code.

Use this when the user wants an agent to keep working until a result is proven or blocked.

Do not use it for simple questions, one-off edits, or work with no meaningful way to verify success.

## Workflow

### 1. Understand The Work

Read the user's brief and any referenced ticket, issue, plan, spec, docs, code, tests, or commands.

Work out the result the user actually wants.

Ask only if you cannot define the finish line, required checks, allowed side effects, or stop conditions.

If the goal is too vague to verify, ask for the missing evidence source.

### 2. Choose The Goal Type

Default to a Codex `/goal` when the user is working in Codex.

Use a Claude Code goal prompt when the user asks for Claude Code.

Do not design scheduled jobs or external automation unless the user explicitly asks for that.

### 3. Write The Contract

The goal must answer these questions in simple language:

- What result should exist at the end?
- What should the agent read before changing anything?
- What is the allowed scope?
- What can the agent edit, run, create, push, or send?
- What must be tested?
- What must be verified?
- What evidence must be reported?
- What should happen after a failure?
- When must the agent stop and ask?
- What must the agent never do?

Make verification a gate.

For example, say:

> The PR must not be opened until the work has been tested and verified.

Prefer pass/fail checks over vague success language.

Use specific checks when they are known.

Examples:

- Run relevant automated tests.
- Run lint, typecheck, build, or documented quality commands.
- Run the app locally when behavior changes.
- For UI changes, verify desktop and mobile in a real browser.
- Use a review subagent for bugs, regressions, missing tests, and scope creep.
- Use a separate acceptance subagent to check acceptance criteria.

### 4. Add Stop Rules

Every goal needs stop rules.

Use concrete stop rules such as:

- The task is unclear.
- Required secrets, permissions, or product decisions are missing.
- The task already has an open PR.
- The same blocker repeats three times.
- The work requires expanding beyond the requested scope.
- Required checks keep failing for the same reason.

When blocked, the agent must report:

- What happened.
- What evidence was gathered.
- What is blocking progress.
- What input would unblock the work.

### 5. Deliver The Prompt

Return the paste-ready prompt first.

Keep any explanation short.

For short Codex goals, use a compact instruction block without headings.

For longer Claude Code prompts, headings are allowed if they make the prompt easier to scan.

Do not use conversational headings such as "Your job".

Avoid clever phrasing, abstract labels, and unexplained system words.

## Style Examples

Single Codex task:

```md
/goal
Use the `task-to-pr` skill to implement the provided task.

Do not stop until one of these is true:

1. A draft PR has been opened for the task.
2. The work is genuinely blocked and the blocker is reported with evidence.

Before changing code, read the task, the repo instructions, and any referenced files or docs.

Keep the work scoped to the task.

Use a dedicated branch and worktree.

The PR must not be opened until the work has been tested and verified.

Required verification:

- Run the relevant automated tests.
- Run the repo's documented lint and quality checks.
- Run the app locally if the task changes user-facing behavior.
- For UI changes, verify desktop and mobile in a real browser.
- Use a review subagent to check for bugs, regressions, missing tests, and scope creep.
- Use a separate acceptance subagent to check the task's acceptance criteria.

Fix valid failures and repeat until verification is clean.

Then commit, push, open a draft PR, and update the task with the PR link and verification evidence.

The PR body must include the task link or task text, summary of changes, acceptance criteria status, and verification commands.

Stop and ask if the task is unclear, already has an open PR, needs missing secrets or product decisions, repeats the same blocker three times, or requires expanding beyond task scope.

Do not merge, deploy, combine unrelated work, discard unrelated local changes, or edit changelogs, generated files, vendored files, or lockfiles unless required.
```

Task list:

```md
Use the `task-to-pr` workflow to implement the provided task list.

Create one draft PR per task.

Work one task at a time unless the user explicitly asks for parallel work.

For each task, use a dedicated branch and worktree.

Do not open a PR until that task has been tested and verified.

For each task, run the relevant automated tests, the repo's documented lint and quality checks, and any required browser checks.

Use a review subagent and a separate acceptance subagent for each task.

Fix valid failures and repeat until verification is clean for that task.

Then commit, push, open a draft PR, and update the task with the PR link and verification evidence.

Keep at most 2 draft PRs open from this goal unless the user approves more.

Stop and ask if a task is unclear, depends on an unreviewed earlier PR, already has an open PR, needs missing secrets or product decisions, repeats the same blocker three times, or requires expanding beyond its scope.

Do not merge, deploy, combine tasks in one PR, discard unrelated local changes, or edit changelogs, generated files, vendored files, or lockfiles unless required.
```

## Quality Bar

The prompt is strong when a fresh agent can answer:

- What am I making true?
- What should I read first?
- What am I allowed to change or send?
- What checks must pass?
- What evidence proves completion?
- What should I do after a failed check?
- When must I stop instead of guessing?

## Anti-Patterns

Avoid prompts like:

- "Improve the app."
- "Keep working until done."
- "Run forever and fix anything."
- "Review your own work and decide if it is good."
- "Deploy when ready" without approval and rollback boundaries.

Rewrite them into clear goals with checks, evidence, and stop rules.
