# Changelog

This file records notable changes to Blueprint.

## Unreleased

### Changed

- `/task-to-pr` now accepts one or more tasks. It orders dependent work, can run independent tasks at the same time, and creates one pull request for each task.
- Delivery now has two clear phases: build and review the code, then pass CI and automated code review.
- Automated review findings require a reply that says what changed or why no change was needed.
- Pull requests stay open unless the user asks the agent to merge them.

### Removed

- Removed the `/milestone` skill. Pass a GitHub milestone to `/task-to-pr` instead.
