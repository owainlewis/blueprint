---
name: loop-design
description: "Design or tighten long-running agent goals and loops for Claude Code, Codex, scheduled prompts, or issue-tracker workflows, with verifier evidence, gates, state, guardrails, and stop conditions."
user-invocable: true
argument-hint: "<rough goal, loop idea, issue set, plan, spec, or runbook path>"
---

# Loop Design

Turn a rough goal or loop idea into one portable execution contract.

A goal is the smallest loop: keep acting until the outcome is proven or blocked.
A loop is a goal with explicit triggers, gates, state, and stop rules.

Use this when the user wants Claude Code, Codex, a scheduled prompt, or an issue-tracker workflow to keep working across iterations.
Do not use it for one-off edits, simple answers, or tasks with no meaningful verifier.

## Workflow

### 1. Ground The Loop

Read the user's brief and any referenced issue, spec, plan, runbook, code, tests, docs, or tracker state.

If the loop depends on current Claude Code or Codex behavior, verify the current official guidance before making tool-specific claims.

Ask only when missing information changes the finish line, verifier, safety boundary, external side effect, or blocked condition.

If the objective is too vague to verify, stop and ask for the missing evidence source.

### 2. Pick The Execution Shape

Choose the lightest shape that fits:

- `in-session`: one Claude Code or Codex session keeps working until done.
- `scheduled`: one idempotent tick prompt runs on a cadence.
- `issue-tracker`: labels, comments, PRs, and assignments hold state.
- `runbook`: reusable instructions for a human or external orchestrator.

Do not imply durable orchestration unless an actual orchestrator owns scheduling, concurrency, retries, and restart state.

### 3. Define The Contract

Write the loop around nine elements:

- Outcome: what must be true when the loop is done.
- Context: files, issues, commands, URLs, docs, or APIs the agent must inspect.
- Actions: allowed edits, commands, tools, side effects, and approval points.
- Verification: typed checks that prove progress or completion.
- Gates: plan, delivery, review, or human checkpoints that can block progress.
- State: where status, decisions, blockers, evidence, and outputs are recorded.
- Iteration policy: how the agent chooses the next action after each result.
- Stop conditions: success, max iterations, no progress, budget caps, or human decision required.
- Privacy: what may leave the workspace, which redactions apply, and when consent is required.

Prefer binary verifier outcomes over vague success language.

Classify verification criteria as:

- `programmatic`: command, test, build, lint, schema check, snapshot, or script returns pass/fail.
- `judge`: another model or reviewer applies a specific rubric to visible artifacts and returns a verdict.
- `human`: the user must decide because taste, business judgment, legal risk, or private context is involved.

Use programmatic checks first, judge rubrics second, and human signoff only where real judgment is required.

Reviewer notes and judge verdicts are different roles.
A reviewer can advise.
A judge or human can block a gate.

### 4. Add Guardrails

Every loop needs:

- A concrete done condition.
- A max iteration or revision cap.
- A no-progress signal, such as the same blocker repeating or verifier output staying unchanged.
- A blocked stop condition that names the evidence to report and the input needed to continue.
- An execution boundary: current workspace, branch, worktree, sandbox, issue tracker, or external orchestrator.

For scheduled or parallel work, include a concurrency and duplicate-action story.

For side effects such as pushes, PR comments, deploys, deletes, database writes, messages, or vendor sends, require approval or an idempotency check unless the user explicitly allows them.

### 5. Deliver The Right Artifact

Return exactly what the user needs:

- For Claude Code: provide a paste-ready loop prompt or runbook that names the outcome, checks, gates, state, and stops.
- For Codex: provide a paste-ready `/goal` when the work is in-session, or an automation/tick prompt when the work is scheduled.
- For issue-tracker loops: provide an idempotent tick prompt and the label/state transitions.
- For reusable workflows: write a short runbook with the goal, context, allowed actions, checks, gates, state, guardrails, and blocked conditions.

Do not bury the actual handoff under a long plan.

## Pasteable Patterns

In-session:

```text
Keep working until <outcome>, verified by <programmatic checks, judge rubric, or human signoff>, while preserving <constraints>. Read <context sources>. You may <allowed actions> and must record <state/evidence>. After each result, choose the next action by <iteration policy>. Stop when <success condition>, <cap>, <no-progress signal>, or <blocked condition>, and report <evidence needed>.
```

Codex persistent goal:

```text
/goal <outcome>, verified by <specific evidence>, while preserving <constraints>. Use <allowed context, tools, and boundaries>. Between iterations, <how to choose the next best action>. If blocked, repeated failures occur, or no valid paths remain, <what to report and what would unlock progress>.
```

Scheduled tick:

```text
One idempotent tick of <loop name>. Recover stale state, claim only eligible work, perform at most <unit of work>, run <verification>, record <state/evidence>, and exit cleanly. Do not start new work if <throttle>. Stop and ask for human input when <blocked condition>.
```

## Quality Bar

The loop is strong when a fresh agent can answer:

- What am I trying to make true?
- What context must I read first?
- What am I allowed to change or send?
- What evidence proves progress and completion?
- Who or what can block a gate?
- Where do I record state and evidence?
- What should I try next if the first attempt fails?
- When must I stop instead of guessing?

## Anti-Patterns

Avoid loops like:

- "Improve the app."
- "Keep working until done."
- "Run forever and fix anything."
- "Review your own work and decide if it is good."
- "Deploy when ready" without approval and rollback boundaries.

Rewrite them into measurable contracts with verification, state, gates, and stop conditions.
