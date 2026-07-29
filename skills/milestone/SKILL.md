---
name: milestone
description: "Completes every open issue in a GitHub milestone. Takes one issue at a time to a tested and reviewed pull request. Use when the user asks to finish or deliver a milestone."
user-invocable: true
argument-hint: "<GitHub milestone URL or name>"
---

# Milestone

Finish every open issue in a GitHub milestone.

## Workflow

1. Resolve the milestone and repository. Inspect its open issues, dependencies, linked pull requests, checks, and current project state.
2. Order the remaining issues by dependency, risk, and how easy each change will be to review. Put blockers, bugs, and shared foundations before features that depend on them.
3. Take one issue at a time to a ready pull request. Create the branch and worktree, implement the smallest complete change, test it, review it with a fresh agent, then open the PR. Resume a matching pull request instead of creating duplicate work.
4. After each pull request is ready, stop for human merge unless the user explicitly allowed merging for this run.
5. When merging is allowed, merge only when:
   - Required checks pass or are confirmed unconfigured.
   - The pull request is mergeable.
   - Every current comment has a clear outcome.
   - No required change remains unresolved.
   - The description and checklist match the final commit.
6. Sync the latest remote default branch before starting the next issue.
7. Refresh the milestone before each issue. Record pull request links, proof, blockers, and final state in the tracker when access permits.
8. Report completed issues, merged and open pull requests, blockers, checks, and anything not verified.

## Boundaries

- Work only on issues in the milestone.
- Use one branch and pull request per issue unless combining issues is required for a working result. Explain any combination before starting it.
- Do not batch unrelated issues.
- Never merge without explicit permission.
- Do not merge with failing required checks, missing acceptance criteria, a current comment without a clear outcome, or a required change still open.
- Do not merge when an acceptance criterion or affected failure path is unverified unless the user accepts that exception.
- Stop when an issue has unresolved product or technical decisions, requires missing secrets or permissions, already has conflicting work, or grows beyond its acceptance criteria.
