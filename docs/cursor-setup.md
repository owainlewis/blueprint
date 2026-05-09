# Cursor Setup

Cursor supports persistent agent instructions through Project Rules in `.cursor/rules` and a simpler root-level `AGENTS.md`.

For Blueprint:

1. Install or copy the `skills/` directory where your skill manager or Cursor workflow can reference it.
2. Keep `AGENTS.md` at the repo root for shared agent guidance.
3. If you want Cursor-native rules, create a small `.cursor/rules/blueprint.mdc` that points to `AGENTS.md` and the relevant skill files instead of duplicating them.

Use Blueprint by asking Cursor for the workflow by name, for example:

```text
Use the Blueprint spec skill for this feature.
Use the Blueprint implement skill for LIN-123.
```

Avoid `.cursorrules` for new setup; Cursor documents it as legacy.

Reference:

- https://docs.cursor.com/en/context
