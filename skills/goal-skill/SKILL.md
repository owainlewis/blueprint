---
name: goal-skill
description: "Create or tighten Codex /goal prompts with measurable completion criteria, verifier evidence, constraints, boundaries, iteration policy, and blocked stop conditions."
user-invocable: true
argument-hint: "<rough goal, issue set, plan, spec, or runbook path>"
---

# Goal Skill

Turn a rough objective into a strong Codex `/goal`.

Use this when the user wants Codex to keep working across turns until an outcome is proven.

Do not use it for one-off edits, simple answers, or tasks with no meaningful verifier.

## Workflow

### 1. Ground The Goal

Read the user's brief and any referenced issue, spec, plan, runbook, code, tests, or docs.

If the goal depends on current Codex behavior, verify the current Codex goal guidance from official docs before making product claims.

Ask only when missing information changes the finish line, verifier, safety boundary, or blocked condition.

If the objective is too vague to verify, stop and ask for the missing evidence source.

### 2. Define The Contract

Write the goal around six elements:

- Outcome: what must be true when work is done.
- Verification surface: commands, tests, URLs, logs, reports, artifacts, or tracker evidence that prove it.
- Constraints: what must not regress or be violated.
- Boundaries: allowed repos, files, services, tools, data, credentials, and resources.
- Iteration policy: how Codex chooses the next action after each result.
- Blocked stop condition: when Codex must stop, report evidence, and ask for specific input.

Prefer binary verifier outcomes over vague success language.

Use observable evidence such as passing commands, deployed URLs, screenshots, logs, build links, issue comments, and commit SHAs.

Name the final evidence template when the work is complex.

### 3. Keep `/goal` Pasteable

The actual `/goal` should be compact enough to paste into Codex.

If the operating contract is long, write or point to a runbook file and make the `/goal` reference it.

The `/goal` should fit this pattern:

```text
/goal <desired end state>, verified by <specific evidence>, while preserving <constraints>. Use <allowed inputs, tools, or boundaries>. Between iterations, <how to choose the next best action>. If blocked or no valid paths remain, <what to report and what would unlock progress>.
```

### 4. Deliver

Return exactly what the user needs:

- For chat: provide the paste-ready `/goal`, then the verifier evidence template when useful.
- For docs: update the requested file with a paste-ready `/goal` near the top and keep longer instructions below it.
- For a reusable workflow: create a short runbook with the goal, done criteria, verifier evidence, loop policy, guardrails, and blocked conditions.

Do not bury the actual `/goal` under a long plan.

## Quality Bar

The goal is strong when a fresh Codex thread can answer:

- What am I trying to make true?
- What evidence proves it?
- What must stay unchanged?
- Where am I allowed to work?
- What should I try next if the first attempt fails?
- When must I stop instead of guessing?

## Anti-Patterns

Avoid goals like:

- "Improve the app."
- "Keep working until done."
- "Deploy everything."
- "Fix all issues."

Rewrite them into measurable contracts with verifier evidence and blocked stop conditions.
