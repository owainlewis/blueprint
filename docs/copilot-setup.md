# GitHub Copilot Setup

GitHub Copilot supports repository instructions in `.github/copilot-instructions.md`, path-specific instructions in `.github/instructions/*.instructions.md`, and `AGENTS.md` files for agents.

For Blueprint:

1. Keep `AGENTS.md` at the repo root for shared agent guidance.
2. Optionally create `.github/copilot-instructions.md` with a short pointer to `AGENTS.md` and the Blueprint workflow.
3. Install or copy `skills/` wherever your Copilot environment or skill manager can reference reusable Markdown workflows.

Suggested `.github/copilot-instructions.md`:

```markdown
Follow the shared agent guidance in AGENTS.md. For non-trivial coding work, use the Blueprint flow: spec -> plan -> implement -> review. Skills live in skills/<name>/SKILL.md.
```

Do not duplicate full skills into Copilot instructions; that turns workflow files into always-on context.

Reference:

- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
