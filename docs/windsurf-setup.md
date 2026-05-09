# Windsurf Setup

Windsurf Cascade can use repo instructions from `AGENTS.md` and workspace rules in `.windsurf/rules/`.

For Blueprint:

1. Keep `AGENTS.md` at the repo root. Windsurf processes it through the Rules engine.
2. Install or copy `skills/` where your skill manager or workspace workflow can reference it.
3. Add optional `.windsurf/rules/*.md` files only for project-specific conventions that should be always-on, glob-scoped, model-decided, or manual.

Use Blueprint by asking Cascade for the workflow by name:

```text
Use Blueprint plan for this spec.
Use Blueprint review on the current diff.
```

Keep Windsurf rules short. Durable shared workflow guidance belongs in `AGENTS.md`; workflow steps belong in the skills.

Reference:

- https://docs.windsurf.com/windsurf/cascade/memories
