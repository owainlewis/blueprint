# Changelog

This file records notable changes to Blueprint.

## Unreleased

### Added

- Added `/requirements` for system product needs and `/spec` for one feature or major change. The spec serves as the ticket.
- Added `/factory` for delivery through gated merge, reusing `/task-to-pr`. Explicit invocation grants scoped merge authority.
- Added a lightweight README, a branded project visual, and focused guides for choosing skills and following common workflows.
- Added contribution and security guidance, issue forms, repository checks, CI, and Dependabot configuration.
- Added `/html-doc` to turn an existing Markdown PRD or technical design into a verified static HTML reading view with offline Mermaid diagrams, responsive layout, and print styles.
- Added `/codex-issue-coordinator` to coordinate large GitHub issue batches through visible Codex worker threads, isolated worktrees, ready-for-review pull requests, review and CI loops, and gated agent merges.

### Changed

- `/factory` now requires the same tests, independent review, CI, repairs, and required approvals as `/task-to-pr`; it no longer writes separate product and technical specs.
- `/architecture` now designs the intended system and data model, with decision status separate from implementation status. Claims about existing code still require verification.
- Moved detailed skill and workflow guidance out of the README so the repository is easier to understand on first visit.
- Marked the implemented `/html-doc` design accordingly and stopped committing its generated HTML reading view as repository documentation.
- Renamed `/issue-coordinator` to `/codex-issue-coordinator` so the skill is clearly scoped to Codex and can coexist with tool-specific alternatives.
- `/plan` now writes each task as a cold handoff with a plain title, standalone summary, useful user stories, defined project terms, and enough context and proof for a new engineer to complete it.
- `/task-to-pr` now accepts one or more tasks. It orders dependent work, can run independent tasks at the same time, and creates one pull request for each task.
- Delivery now has two clear phases: build and review the code, then pass CI and automated code review.
- Automated review findings require a reply that says what changed or why no change was needed.
- `/task-to-pr` leaves passing pull requests open by default. Explicit `/factory` or `/codex-issue-coordinator` use grants scoped gated merging.
- Pull requests are marked ready before independent and GitHub review begin.
- Explicitly naming `/codex-issue-coordinator` grants merge authority for only its supplied batch after every quality gate passes. An implicit skill match leaves passing pull requests open.
- Dependent work now stacks on open, independently approved prerequisite pull requests instead of waiting for merge.
- Design invariants and acceptance criteria now use stable IDs that planning, testing, and review preserve.
- Architecture invariants now name their enforcing mechanism, and architecture documents carry their own update triggers.
- Delivery, design, review, testing, planning, and improvement now state their stop conditions and proof handoffs more precisely.

### Removed

- Replaced `/design` with `/spec`. System product requirements now belong in `/requirements`.
- Removed the `/milestone` skill. Pass a GitHub milestone to `/task-to-pr` instead.
