# Security policy

## Supported versions

Blueprint is installed from the repository. Security fixes apply to the current `main` branch and the latest published release. Older snapshots are not maintained separately.

## Report a vulnerability

Do not open a public issue for a vulnerability.

Use [GitHub private vulnerability reporting](https://github.com/owainlewis/blueprint/security/advisories/new) to send the details privately. Include:

- the affected skill, script, workflow, or file;
- the conditions needed to trigger the problem;
- the impact you observed;
- a minimal reproduction when it is safe to provide one;
- any suggested mitigation.

The maintainer will confirm the report, assess its impact, and coordinate a fix before public disclosure. Response and release timing depend on the severity and the information available.

## Scope

Security reports are especially useful for unsafe command execution, path handling, generated HTML, dependency or workflow supply-chain risks, secret exposure, and instructions that could cause an agent to exceed the authority a user granted.

General bugs, unclear guidance, and feature requests belong in the public issue tracker.
