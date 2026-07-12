# Working In Blueprint

This file governs contributions to the Blueprint repository. Installed skills do not depend on it.

## Product Model

Blueprint contains exactly five public skills:

- `spec`: turn an idea into a written implementation decision.
- `tickets`: turn an approved spec into agent-ready work.
- `build`: turn one or more GitHub issues into tested and reviewed GitHub PRs.
- `review`: independently review code without editing it.
- `browser-test`: independently test rendered work in a real browser.

The main flow is:

```text
idea -> spec -> tickets -> build -> PRs
```

`review` and `browser-test` also work independently.

## Contribution Rules

- Keep exactly these five skill directories under `skills/`.
- Keep every skill self-contained. Its process, templates, defaults, checks, and stop rules belong in its `SKILL.md`.
- Do not make a skill depend on this file, another skill, a custom agent definition, or a shared root template.
- Do not add helper skills for branches, commits, testing, or PR mechanics. Put required delivery steps in `build`.
- Give each skill one clear input and output. `build` may coordinate several tickets because it owns the complete delivery phase.
- Prefer working outcomes and observable behavior over prescribed files or functions.
- Use simple language. Keep only instructions that change behavior or prevent a real failure.
- Add a new capability to an existing skill when it belongs to that phase. Add a new skill only when it has a distinct, independently useful input and output.
- Never add agent attribution or co-author lines to commits.

## Verification

Before opening a PR:

1. Confirm that only the five public skill directories exist.
2. Check frontmatter, Markdown fences, links, and plain language.
3. Search for stale skill names and hidden runtime dependencies.
4. Review each skill against [REVIEW.md](REVIEW.md).
5. Have a fresh reviewer inspect the final diff.

Deliver complete changes, run relevant checks, use a Conventional Commit, and never merge without an explicit request.
