# Contributing to Blueprint

Blueprint stays useful by keeping its instructions small, clear, and easy to verify. Contributions should improve one engineering phase or delivery outcome without adding a second way to do the same job.

## Before you start

Search the [open issues](https://github.com/owainlewis/blueprint/issues) and existing skills first. For a larger change, open a proposal issue before writing code so the purpose and boundaries can be agreed.

A useful issue explains:

- what is hard or missing today;
- who experiences the problem;
- what should be observable when it is fixed;
- how the result can be checked;
- what related work is outside the change.

Small documentation corrections can go straight to a pull request.

## Make a focused change

- Keep one pull request to one outcome.
- Put repository policy in `AGENTS.md` and phase-specific behavior in the relevant skill.
- Use short sentences and familiar words. Define project terms before using them.
- Do not add placeholders, fake examples presented as proof, or unfinished sections.
- Update examples and public guides when a skill change would make them inaccurate.

Read [REVIEW.md](REVIEW.md) for the standard used to review Blueprint itself.

## Run the checks

The complete check requires Python 3.11 or newer, Pandoc 3 or newer, Node.js 22.12 or newer, and npm.

```bash
./scripts/check
```

The command creates an ignored Python check environment and installs the locked `html-doc` dependencies when needed. It validates skill metadata, repository structure, and links, checks shell syntax, and runs the renderer tests.

When public documentation changes, also read the rendered files on GitHub. Check the README at desktop and mobile widths. Source review alone does not prove the GitHub layout works.

## Open the pull request

Use the pull request template. Explain the problem and result in plain English, include the commands and manual checks you ran, and link the issue when one exists.

Pull requests remain open for human review. Maintainers may ask for a smaller change when unrelated work makes the result harder to judge.
