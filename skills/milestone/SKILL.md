---
name: milestone
description: "Completes all open GitHub issues in a milestone by running the task-to-pr skill one issue at a time. Use when the user asks to complete, deliver, work through, or finish a GitHub milestone."
user-invocable: true
argument-hint: "<GitHub milestone URL or name>"
---

# Milestone

Finish every open issue in a GitHub milestone.

## Workflow

1. Resolve the milestone and repository. Inspect its open issues, dependencies, linked pull requests, checks, and current project state.
2. Order the remaining issues by dependency, risk, and reviewability. Put blockers, bugs, and shared seams before dependent feature work.
3. Take one issue at a time through `/task-to-pr`. Resume a matching pull request instead of creating duplicate work.
4. After each pull request is ready, stop for human merge unless the user explicitly allowed merging for this run.
5. When merging is allowed, merge only after required checks and review are clean. Sync the latest remote default branch before starting the next issue.
6. Refresh the milestone before each issue. Record pull request links, proof, blockers, and final state in the tracker when access permits.
7. Report completed issues, merged and open pull requests, blockers, checks, and anything not verified.

## Boundaries

- Work only on issues in the milestone.
- Use one branch and pull request per issue unless combining issues is required for a working result. Explain any combination before starting it.
- Do not batch unrelated issues or reimplement the inner delivery workflow.
- Never merge without explicit permission.
- Do not merge with failing checks, important unresolved feedback, missing acceptance criteria, or unexplained test gaps.
- Stop when an issue has unresolved product or technical decisions, requires missing secrets or permissions, already has conflicting work, or grows beyond its acceptance criteria.
