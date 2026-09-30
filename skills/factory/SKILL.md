---
name: factory
description: "Takes a GitHub issue to a pull request with passing CI in one shot, without supervision. Writes product and technical specs, implements them, and fixes CI failures and automated review comments. Use when asked to build an issue end to end without supervision."
user-invocable: true
argument-hint: "<GitHub issue number or URL>"
---

# Factory

Take the provided GitHub issue to a pull request. Do not ask the user anything.

Work in a new git worktree at `../<repo>-<issue>`, on a new branch from the latest
default branch. Put the issue number in the branch name, such as `42-fix-login`.
Keep the repository's branch prefix if it has one.

1. Review the provided issue and write a PRODUCT_SPEC.md and a TECHNICAL_SPEC.md
   in `docs/<feature-slug>/`.
2. Implement TECHNICAL_SPEC.md, with a test for each requirement in PRODUCT_SPEC.md.
3. Run the tests and fix any failures. Check that each new test fails without
   your change.
4. Open a pull request. Start its description with `Closes #<issue>`, then add
   three sections: What changed, Why, and Verification.
5. Wait for CI with `gh pr checks --watch`. Fix any failures and push.
6. If recent pull requests in the repository have automated reviews, wait up to
   10 minutes for them. Fix each comment, or reply with why not. If you pushed a
   fix, go back to step 5.
7. Comment on the issue with the pull request link and what happened.

Stop after 3 rounds of CI or review fixes. Never weaken a test, merge, or force-push.
