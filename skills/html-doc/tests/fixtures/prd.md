# Account recovery PRD

> **Status:** Approved

## Summary

Let a locked-out user recover an account without support.

## Goals

- Restore access within five minutes.
- Keep the existing account identity.

## Non-goals

- Replacing multi-factor authentication.

## Requirements

1. Send a single-use recovery link.
2. Expire the link after 15 minutes.

- [x] Record successful recovery.
- [ ] Add translated email copy later.

> Support staff cannot read recovery tokens.

The flow keeps **private data** protected and shows *plain guidance*. Read the [support policy](https://example.com/policy).

| Input | Result |
| --- | --- |
| known email | generic response |
| unknown email | generic response |

```json
{"result":"accepted"}
```

## Acceptance criteria

- `AC-1`: Both known and unknown emails receive the same visible response.
- `AC-2`: A used link cannot be reused.
