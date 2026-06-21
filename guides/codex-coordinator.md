# Codex Coordinator Loop

Use this when you want one attended Codex thread to work through a small, explicit issue set.
It is a prompt pattern, not a skill.
The skills still do the judgment: `task-to-pr`, `implement`, `review`, `pr`, and `pr-to-ready`.

This loop is useful when:

- the issue set is finite and ordered;
- a project board or tracker should stay current;
- each issue should become its own branch and PR;
- the coordinator should run an adversarial review before PR;
- merging is explicitly authorized for this run.

Do not use this as Blueprint's default unattended loop.
The default remains draft PRs for human review.

## Coordinator Prompt

```text
Create a goal for this thread:

Work through <issue-list> in <repo> and turn them into merged PRs, one issue at a time, using a coordinator workflow.

Repository:
- Local path: <absolute-path>
- GitHub repo: <owner/repo>
- Remote: <remote-url>
- Base branch: <base-branch>

Source of truth:
- The listed issues
- The repo's AGENTS.md
- Any linked spec, roadmap, or plan docs
- The project board or tracker, if one is listed below

Project tracking:
- Project or tracker: <url-or-name>
- Status states: <todo>, <in-progress>, <done>
- Move an issue to <in-progress> when active work starts.
- Keep it in <in-progress> through planning, coding, review, PR, and checks.
- Move it to <done> only after the PR is merged.
- If blocked after work starts, leave it in <in-progress> and comment the blocker on the issue.
- If work never starts, leave it in <todo>.

Workflow for each issue:

1. Pull the ticket.
- Read the issue, linked context, AGENTS.md, and relevant repo docs.
- Inspect the current repo state.
- Decide whether the issue is unblocked.
- If blocked, stop and explain.
- If unblocked and active work is starting, update the tracker to <in-progress>.

2. Plan the work.
- For simple issues, write a short plan in the thread.
- For non-trivial issues, write a plan under docs/issues/<issue-number>-plan.md.
- Include goal, context, likely files, acceptance criteria, verification, and out of scope.

3. Branch and isolate.
- Use one branch per issue.
- Branch naming format: issue-<number>-<short-slug>.
- Prefer a separate worktree when isolation reduces risk.
- Do not overwrite, discard, or stage unrelated changes.

4. Implement.
- Make the smallest complete change that satisfies the issue.
- Follow existing project patterns.
- Add or update tests that would catch the behavior.
- Keep docs aligned when behavior, commands, public APIs, or decisions change.

5. Verify.
- Run the issue's listed verification commands.
- Run the relevant test suite.
- For user-visible or terminal/browser behavior, run the manual smoke checks the issue calls for.
- Record anything that could not be verified.

6. Adversarial review.
- Use a fresh subagent to review the branch before opening the PR.
- Ask it to check correctness, acceptance criteria, missing tests, edge cases, regressions, maintainability, and over-broad scope.
- Judge every finding.
- Fix valid in-scope findings.
- Rerun relevant checks.

7. Open PR.
- Commit only intended changes.
- Push the branch.
- Open a PR against <base-branch>.
- Include linked issue, summary, acceptance checklist, tests run, manual verification, review summary, and known limitations.

8. Merge.
- Merge only because this prompt explicitly authorizes it.
- Before merging, ensure local tests pass and remote checks pass if checks exist.
- If checks fail, inspect and fix them.
- Use the repo's documented merge policy.
- If no policy exists, use squash merge.
- After merge, update the tracker to <done>.
- Update local <base-branch> before starting the next issue.

Execution:
- Process issues in the listed order.
- Parallelize only when issues are genuinely independent and can be reviewed and merged separately.
- Prefer clean sequencing over speed when issues share files, decisions, or assumptions.

Stop conditions:
- Stop if acceptance criteria are unclear.
- Stop if tracker, push, PR, or merge permissions fail.
- Stop if a design decision needs human approval.
- Stop if tests reveal a deeper problem outside the issue scope.

Report after each issue:
- Issue number and title
- Tracker status
- Branch
- Worktree path, if used
- PR URL
- Merge result
- Tests run
- Review findings fixed
- Anything deferred

Begin with the first issue.
```

## Notes

This loop deliberately extends beyond `task-to-pr`.
It owns sequencing and, when explicitly authorized, merge.
Use it for attended project pushes, not unattended background work.
