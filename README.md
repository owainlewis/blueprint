# Blueprint

Five self-contained skills for turning ideas into reviewed pull requests.

```text
idea -> spec -> written decision
written decision -> tickets -> agent-ready work
ticket or milestone -> build -> reviewed PRs
```

`review` and `browser-test` are independent quality tools. Use them whenever you need a second opinion or real browser evidence.

Each skill includes its own process, defaults, templates, checks, and stop rules. An installed skill does not depend on this repository's `AGENTS.md`, another Blueprint skill, a custom agent definition, or a shared template.

## Skills

| Skill | Input | Output | Example |
| --- | --- | --- | --- |
| `spec` | An idea, problem, or rough brief | A draft implementation decision ready for review | `/spec Add team invitations` |
| `tickets` | An approved spec | One or more agent-ready ticket drafts | `/tickets docs/team-invitations/spec.md` |
| `build` | One GitHub issue, several issues, or a milestone | Tested and reviewed GitHub PRs | `/build https://github.com/org/repo/issues/123` |
| `review` | A diff, branch, commit, or PR | Independent findings and a verdict | `/review PR 42` |
| `browser-test` | A URL, route, flow, or browser-facing change | Browser test evidence | `/browser-test http://localhost:3000/invitations` |

After human review, `spec` changes the document status from `Draft` to `Approved`. `tickets` accepts approved specs and returns drafts in chat by default. Ask it to publish the drafts as GitHub issues before passing them to `build`.

`build` owns the full delivery workflow. It resolves existing work, creates one branch and worktree per ticket from `origin/main`, implements and tests the change, gets a fresh review, checks acceptance criteria, commits, pushes, opens the PR, and handles current feedback. It never merges.

## Principles

- One clear transformation per planning skill.
- A ticket is the complete input to a coding agent.
- Tickets describe working outcomes, not disconnected technical layers.
- Tests and browser checks are evidence, not ceremony.
- Review is independent and read-only.
- Human decisions stay visible.
- Merging stays human.

## Install

```bash
npx skills add owainlewis/blueprint
```

Update installed skills with:

```bash
npx skills update
```

`browser-test` needs access to a real browser automation tool.

## Contributing

See [AGENTS.md](AGENTS.md) for repository contribution rules and [REVIEW.md](REVIEW.md) for review checks. These files govern Blueprint itself. Installed skills are standalone.
