# Changelog

This file records notable changes to Blueprint.

## Unreleased

### Added

- Added `/html-doc` to turn an existing Markdown PRD or technical design into a verified static HTML reading view with offline Mermaid diagrams, responsive layout, and print styles.
- Added `/issue-coordinator`, presented as the Ultra-scale workflow, to coordinate large GitHub issue batches through visible Codex worker threads, isolated worktrees, ready-for-review pull requests, review and CI loops, and gated agent merges.

### Changed

- `/plan` now writes each task as a cold handoff with a plain title, standalone summary, useful user stories, defined project terms, and enough context and proof for a new engineer to complete it.
- `/task-to-pr` now accepts one or more tasks. It orders dependent work, can run independent tasks at the same time, and creates one pull request for each task.
- Delivery now has two clear phases: build and review the code, then pass CI and automated code review.
- Automated review findings require a reply that says what changed or why no change was needed.
- Pull requests stay open unless the user asks the agent to merge them.
- Pull requests are marked ready before independent and GitHub review begin.
- Explicitly naming `/issue-coordinator` grants merge authority for only its supplied batch after every quality gate passes. An implicit skill match leaves passing pull requests open.
- Dependent work now stacks on open, independently approved prerequisite pull requests instead of waiting for merge.
- Design invariants and acceptance criteria now use stable IDs that planning, testing, and review preserve.
- Architecture invariants now name their enforcing mechanism, and architecture documents carry their own update triggers.
- Delivery, design, review, testing, planning, and improvement now state their stop conditions and proof handoffs more precisely.

### Removed

- Removed the `/milestone` skill. Pass a GitHub milestone to `/task-to-pr` instead.
