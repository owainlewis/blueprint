---
name: loop-design
description: "Design or tighten long-running agent goals and loops for Claude Code, Codex, scheduled prompts, or issue-tracker workflows, with clear done conditions, checks, saved state, safety limits, and stop rules."
user-invocable: true
argument-hint: "<rough goal, loop idea, issue set, plan, spec, or runbook path>"
---

# Loop Design

Turn a rough goal or loop idea into clear instructions an agent can follow.

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
- `scheduled`: one repeatable prompt runs on a cadence.
- `issue-tracker`: labels, comments, PRs, and assignments hold state.
- `runbook`: reusable instructions for a human or external runner.

Do not claim the loop will keep running unless a real runner owns the schedule, retries, and restart state.

### 3. Define The Instructions

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

### 4. Add Safety Limits

Every loop needs:

- A concrete done condition.
- A max iteration or revision cap.
- A no-progress signal, such as the same blocker repeating or verifier output staying unchanged.
- A blocked stop condition that names the evidence to report and the input needed to continue.
- An execution boundary: current workspace, branch, worktree, sandbox, issue tracker, or external runner.

For scheduled or parallel work, say what happens if two copies run at the same time.
Also say how the loop avoids doing the same external action twice.

For side effects such as pushes, PR comments, deploys, deletes, database writes, messages, or vendor sends, require approval or a check that prevents repeating the same action unless the user explicitly allows them.

### 5. Deliver The Right Artifact

Return exactly what the user needs:

- For Claude Code: provide a paste-ready loop prompt or runbook that says what to do, what to read, how to verify, when to stop, and what not to do.
- For Codex: provide a paste-ready `/goal` when the work is in-session, or an automation/tick prompt when the work is scheduled.
- For issue-tracker loops: provide a repeatable tick prompt and the label or state changes.
- For reusable workflows: write a short runbook with the goal, context, allowed actions, checks, gates, state, guardrails, and blocked conditions.

Do not bury the actual handoff under a long plan.

Write prompts like instructions for a careful beginner.
Use simple headings and direct verbs.
Avoid clever phrasing, compressed abstractions, and unexplained system words.
If a technical word is necessary, explain it in one short sentence.
Prefer this shape:

```text
Your job
<plain outcome>

Read first
<files, issues, docs, commands, or state to inspect before changing anything>

What you may do
<allowed edits, tools, side effects, and limits>

After each pass
<how to choose the next small action and what evidence to record>

You are done when
<checks or evidence that prove the outcome>

Stop and ask when
<human decisions, repeated failures, unsafe actions, or unclear blockers>

Do not
<hard limits>
```

## Pasteable Patterns

In-session:

```text
Your job
Keep working until <plain outcome>.

Read first
Read <context sources>.

What you may do
You may <allowed actions>.
Keep <constraints>.

After each pass
Run <checks>.
Record <state or evidence>.
If the goal is not done, choose the next smallest safe action.

You are done when
<success condition> is true and <verification evidence> proves it.

Stop and ask when
<cap>, <no-progress signal>, or <blocked condition> happens.
Report <evidence gathered>, <blocker>, and <input needed>.

Do not
<hard limits>.
```

Codex persistent goal:

```text
/goal
Your job
<plain outcome>.

Read first
Use <allowed context, tools, and boundaries>.

What you may do
<allowed actions>.
Preserve <constraints>.

After each pass
Run <specific checks>.
If the goal is not done, choose the next smallest safe action.

You are done when
<specific evidence> proves the outcome.

Stop and ask when
Blocked, repeated failures occur, or no valid paths remain.
Report <what happened>, <what is blocking>, and <what would unlock progress>.
```

Scheduled tick:

```text
One tick of <loop name>.

Read first
Recover stale state.
Find work that is eligible.

What you may do
Claim only eligible work.
Do at most <unit of work>.
Do not start new work if <throttle>.

After each pass
Run <verification>.
Record <state/evidence>.
Exit cleanly.

Stop and ask when
<blocked condition>.
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
