# Task list requirements

> Status: proposed teaching example. No application is implemented here.

## Product and users

Task list lets one person keep small tasks from a terminal. It stores tasks on
their computer so they can close the terminal and return later.

## Key features

- Add a task with a short title.
- List unfinished tasks.
- Mark a task complete so it leaves the unfinished list.

## Requirements

| ID | Required behavior |
|---|---|
| REQ-1 | Adding a valid title creates one unfinished task and returns its stable ID. |
| REQ-2 | Listing shows unfinished tasks in creation order, with IDs and titles. An empty list has a clear message. |
| REQ-3 | Completing an existing task removes it from the unfinished list. Repeating completion succeeds without another change. An unknown ID returns a not-found error. |
| REQ-4 | Tasks survive process restarts. Invalid input leaves stored tasks unchanged. Storage failure returns an error without claiming success. |

Titles must contain 1 to 200 Unicode characters after trimming surrounding
whitespace. They must not contain control characters. Duplicate titles are
allowed because different tasks may have the same name.

## Scope and constraints

The product works offline for one local user. No accounts, synchronization,
sharing, editing, deletion, due dates, or web interface are included.

## Acceptance

A person can add two tasks, restart the CLI, list them in order, complete one,
and see only the other. They can distinguish empty results, invalid input,
unknown IDs, and storage failure.

Detailed command behavior and test scenarios belong in each feature spec.

## Open decisions

None. The first feature adds and lists tasks. Completion follows separately.
