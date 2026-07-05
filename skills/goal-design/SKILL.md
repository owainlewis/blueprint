---
name: goal-design
description: "Write short Codex and Claude Code /goal prompts with a clear result, checks, proof, and stop rules."
user-invocable: true
argument-hint: "<rough goal, task, ticket, issue set, or prompt>"
---

# Goal Design

1. Read the brief and anything it references. Ask only when the goal can't be checked from the input.
2. Write one plain paragraph starting with `/goal`, 5-8 sentences: what to read first, what to change, what checks must pass, what proof to report, an effort budget, when to stop as blocked.
3. Return the prompt first. Add a note after only when useful.

## Rules

- The completion condition must be provable from the agent's own output. Name the exact command and expected result; goal evaluation reads the session, it doesn't run checks itself.
- Checks are a gate, not a suggestion. Concrete proof: command results, links, files, screenshots.
- Always include a budget: a turn, iteration, or time limit.
- Require reviewer sign-off before PR, and a check of each acceptance criterion when criteria exist.
- Include stop conditions: unclear change, missing secrets or permission, repeating failure, duplicate PR, scope growing beyond the request.
- No giant Markdown docs, scheduled jobs, or external automation unless asked.

## Shape

    /goal Finish <result>. Before changing anything, read <sources>. Change only <allowed files or behavior>. Make the smallest complete change, add or update tests, ask another reviewer to check it, and run <checks>. Do not open a PR or report done until <proof> shows <expected output>. Stop after <budget>, or if <stop condition>, and report what blocks the work.
