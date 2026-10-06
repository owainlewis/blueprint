# Add and list tasks

> Status: proposed teaching example. This spec is the ticket.

## Outcome and scope

Deliver the first working slice of [Task list](../../REQUIREMENTS.md): add a task
and list unfinished tasks across process restarts. Implement REQ-1, REQ-2, and
the relevant persistence, validation, and storage rules in REQ-4.

Follow the [architecture](../../ARCHITECTURE.md), including INV-1 and INV-2.
Completing tasks (REQ-3), editing, deletion, synchronization, and schema migration
are out of scope. No architecture change is required.

## Required behavior

Expose the CLI through Python's module entry point:

```text
python -m task_list [--db PATH] add TITLE
python -m task_list [--db PATH] list
```

`--db` precedes the subcommand. Without it, use `tasks.sqlite3` in the working
directory. Open or create the database and its table using the architecture's
schema. Do not create missing parent directories or modify an incompatible
existing table. Report those as storage failures.

Add trims surrounding whitespace and applies the title rules in REQ-1. Reject
Unicode control characters in category Cc, including newline and tab. On success,
print `Added task <id>.` to stdout and exit 0. Repeating a valid add creates
another task; duplicate titles are allowed.

List prints one line per open task: `<id>  <title>`. Order by ascending ID. With
no open tasks, print `No open tasks.`. Exit 0 and do not change task rows.

Invalid titles print `Error: title must be 1 to 200 characters with no control characters.`
to stderr and exit 2. Invalid command syntax uses argparse's help and exit 2.
Storage failures print `Error: cannot read or write the task database.` to stderr
and exit 1. These failures print no success message or task list to stdout.
A missing database is created on either command, including an initial list.

## Technical design

Use `task_list/__main__.py` for argument parsing and output. Task operations
accept a store and return the inserted ID or ordered tasks. The SQLite store
opens the database, checks or creates its schema, and uses parameterized SQL.
Keep titles out of diagnostic logs.

Validate an add before opening the database. Insert state `open` in a transaction
and return its generated ID only after commit. On failure, roll back and propagate
a storage error to the CLI. The store sets the architecture's five-second lock
timeout and closes the connection even when an operation fails.

List reads `id` and `title` where state is `open`, ordered by `id`. Finish the
read before printing so a storage failure cannot leave a partial task list.
Tests use temporary database files and standard-library unittest. Run CLI
scenarios in separate processes to exercise the real entry point and restart
persistence. Inject a failing commit at the store boundary to exercise INV-1.

## Acceptance and proof

These scenarios define required tests. They are not reports of passing checks.
Once the app exists, run them with `python -m unittest discover -s tests -v`.

| ID | Done when | How to check |
|---|---|---|
| AC-1 | A padded valid title creates one open task, stores the trimmed title, prints its ID, and exits 0. | Run add against a temporary database; inspect the row and stdout. |
| AC-2 | Two adds with the same title create different IDs. Listing after a restart shows both in creation order. | Run separate CLI processes against the same file and compare output. |
| AC-3 | An initial list creates the database, prints the empty message, and exits 0. Done tasks never appear. | Test a fresh path, then seed a done task and list again. |
| AC-4 | Empty, whitespace-only, overlong, and control-character titles exit 2 without writes. A 200-character title succeeds. | Test each boundary, compare existing rows, and verify invalid add does not create a new database. Covers INV-2. |
| AC-5 | Missing parents, incompatible schemas, and locks lasting beyond the timeout exit 1 with only the storage error. | Use temporary files and a second connection holding a write lock. |
| AC-6 | A failed insert or commit leaves no task and prints no success message. | Inject both failures at the store boundary and inspect the database and CLI result. Covers INV-1. |

## Open decisions

None. This change fits one delivery task and does not need a separate plan.
