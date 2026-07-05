---
name: goal-design
description: "Write short Codex and Claude Code /goal prompts with a clear result, checks, proof, and stop rules."
user-invocable: true
argument-hint: "<rough goal, task, ticket, issue set, or prompt>"
---

# Goal Design

Goal: write one short paste-ready `/goal` prompt.

## Workflow

1. Read the brief and any referenced ticket, issue, plan, spec, docs, code, tests, or commands.
2. Define the result, what can change, checks, proof, and when to stop. Ask only when the goal cannot be checked from the input.
3. Write one plain paragraph starting with `/goal`. Prefer 5-8 sentences. Include what to read first, what to change, what checks must pass, what proof to report, and when to stop as blocked.
4. Return the prompt first. Add a short note after it only when useful.

## Rules

- Keep goals short. Do not write giant Markdown docs unless the user asks.
- Make checks a gate, not a suggestion.
- Require another reviewer for code changes before PR.
- Require checking each acceptance criterion when acceptance criteria exist.
- Name concrete proof: command results, links, files, screenshots, or other outputs.
- Stop when the requested change is unclear, secrets are missing, permission is missing, the same failure repeats, a duplicate PR exists, or the task would grow beyond the request.
- Do not design scheduled jobs or external automation unless asked.

## Shape

```md
/goal Finish <result>. Before changing anything, read <sources>. Change only <allowed files or behavior>. Make the smallest complete change, add or update tests, ask another reviewer to check it, and run <checks>. Do not open a PR or report done until <proof> shows it works. If <stop condition>, stop and report what blocks the work.
```
