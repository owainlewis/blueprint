# Queue design

> **Status:** Proposed

## Summary

Keep jobs durable and ordered.

## Requirements

- `INV-1`: Jobs survive a restart.
- `AC-1`: A restored job runs once.

### Repeated

First repeated heading.

### Repeated

Second repeated heading.

## 設計

Unicode heading.

## !!!

Punctuation heading.

## Diagram

```mermaid
flowchart LR
    Queue --> Worker
```

| Input | Result |
| --- | --- |
| job | accepted |

```python
print("kept")
```
