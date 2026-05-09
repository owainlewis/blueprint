---
name: build
description: "Deprecated compatibility alias for implement. Use implement for new workflows."
user-invocable: true
argument-hint: "<task reference or description>"
---

# Build

`build` is deprecated. Use `implement` for new workflows.

For compatibility with existing prompts and automation, treat this invocation as `implement`.

## Workflow

1. Read the request, task, ticket, plan, spec, or code needed to understand the change.
2. Ask for clarification if missing information would materially change the implementation.
3. Make a short implementation plan for non-trivial work.
4. Implement the smallest safe change that solves the request.
5. Run the relevant tests, checks, or build command for the project.
6. Report what changed and what passed.

## Rules

- Do not confuse this skill with project build commands such as `npm build`, `cargo build`, or CI build steps.
- Preserve unrelated user changes.
- If the change reveals the task or spec is wrong, stop and explain before continuing.
