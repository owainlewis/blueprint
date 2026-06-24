---
name: goal-design
description: "Write or tighten Codex and Claude Code /goal prompts with clear done conditions, required checks, evidence, and stop rules."
user-invocable: true
argument-hint: "<rough goal, task, ticket, issue set, or prompt>"
---

# Goal Design

Turn a rough objective into a `/goal` prompt with finish line, checks, evidence, and stop rules.

Use when the user wants the agent to continue until proven complete or blocked.
Skip simple questions, one-off edits, and work with no verifiable success condition.

## Rules

- Start with `/goal`.
- First sentence: name the skill or workflow and required outcome.
- Make verification a gate, for example: `Do not open the PR until tests and verification pass.`
- Require evidence: reports, command results, links, and artifacts.
- Use pass/fail checks, not "looks done".
- Use simple language.
- Skip headings unless the user asks for a longer structured prompt.
- Do not use conversational headings such as "Your job".
- Do not design scheduled jobs or external automation unless the user asks.

## Workflow

### 1. Understand The Work

Read the brief and referenced ticket, issue, plan, spec, docs, code, tests, or commands.
Define the finish line.
Ask only when finish line, checks, allowed side effects, or stop conditions are missing.
If the goal is too vague to verify, ask for the evidence source.

### 2. Write The Contract

Answer:

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

Use known checks:

- Run relevant automated tests.
- Run lint, typecheck, build, or documented quality commands.
- Run the app locally when behavior changes.
- For UI changes, verify desktop and mobile in a real browser.
- Use a review subagent for bugs, regressions, missing tests, and scope creep.
- Use a separate acceptance subagent to check acceptance criteria.

### 3. Add Stop Rules

Add concrete stop rules:

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

### 4. Deliver The Prompt

Return the paste-ready `/goal` prompt first.
Keep explanation short.
Avoid clever phrasing, abstract labels, and unexplained system words.

## Template

Single task:

```md
/goal
Use the `task-to-pr` skill to implement the provided task.

Do not stop until one of these is true:
1. A draft PR has been opened for the task.
2. The work is genuinely blocked and the blocker is reported with evidence.

Before changing code, read the task, repo instructions, and referenced files or docs.
Keep scope to the task.
Use a dedicated branch and worktree.
Follow existing codebase patterns.
Make the smallest complete change that satisfies the task.
Add or update tests for changed behavior.
Do not open the PR until the work has been tested and verified.

Required verification:
- Run the relevant automated tests.
- Run documented lint and quality checks.
- Run the app locally if the task changes user-facing behavior.
- For UI changes, verify desktop and mobile in a real browser.
- Use a review subagent to check for bugs, regressions, missing tests, and scope creep.
- Use a separate acceptance subagent to check the task's acceptance criteria.
- Review the final diff for unrelated changes, brittle code, missing tests, and broken docs.

Fix valid failures and repeat until verification is clean.
Then commit, push, open a draft PR, and update the task with the PR link and verification evidence.
The PR body must include the task link or task text, summary of changes, acceptance criteria status, and verification commands.
Stop and ask if the task is unclear, already has an open PR, needs missing secrets or product decisions, repeats the same blocker three times, or requires expanding beyond task scope.
Do not merge, deploy, combine unrelated work, discard unrelated local changes, or edit changelogs, generated files, vendored files, or lockfiles unless required.
```

Task list:

```md
/goal
Use the `task-to-pr` workflow to implement the provided task list.

Create one draft PR per task.

Do not stop until every task has either a verified draft PR or a blocker reported with evidence.

Before changing code, read the task list, repo instructions, and referenced files or docs.
Work one task at a time unless the user explicitly asks for parallel work.
For each task, use a dedicated branch and worktree.
Keep each PR scoped to exactly one task.
Follow existing codebase patterns.
Make the smallest complete change that satisfies the current task.
Add or update tests for changed behavior.
Do not open a PR until that task has been tested and verified.
For each task, run the relevant automated tests, the repo's documented lint and quality checks, and any required browser checks.
Use a review subagent and a separate acceptance subagent for each task.
Review the final diff for unrelated changes, brittle code, missing tests, and broken docs.
Fix valid failures and repeat until verification is clean for that task.
Then commit, push, open a draft PR, and update the task with the PR link and verification evidence.
Each PR body must include the task link or task text, summary of changes, acceptance criteria status, and verification commands.
Keep at most 2 draft PRs open from this goal unless the user approves more.
Stop and ask if a task is unclear, depends on an unreviewed earlier PR, already has an open PR, needs missing secrets or product decisions, repeats the same blocker three times, or requires expanding beyond its scope.
Do not merge, deploy, combine tasks in one PR, discard unrelated local changes, or edit changelogs, generated files, vendored files, or lockfiles unless required.
```

## Quality Bar

The prompt must answer:

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

Rewrite them into `/goal` prompts with checks, evidence, and stop rules.
