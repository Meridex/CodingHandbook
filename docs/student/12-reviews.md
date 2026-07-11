# Chapter 12 — Reviews

## Overview: Code Review as a Research Tool

Code review is the process by which a colleague reads your Pull Request before it is merged.
In a research group, code review serves purposes beyond catching bugs:

- **Correctness verification** — a second pair of eyes on the physics and mathematics
- **Knowledge sharing** — reviewers learn how the code works; authors learn from feedback
- **Quality enforcement** — consistent style, documentation, and test coverage
- **Institutional memory** — review discussions are permanently recorded on the PR

Code review is not criticism. It is one of the most valuable forms of collaboration
available in a research group.

---

## Types of Review Feedback

GitHub's review system categorises comments by severity. Understand these before
responding to feedback:

| Type | Meaning | How to respond |
|------|---------|----------------|
| **Required Change** | Must be fixed before approval | Fix it, push, reply confirming the fix |
| **Suggestion** | A recommendation the reviewer thinks is better | Consider it; implement or explain your reasoning |
| **Question** | Reviewer needs clarification | Answer in the comment; update code/docs if needed |
| **Nit (nitpick)** | Minor style or wording issue; low priority | Fix if quick; note "nit" in your reply if you defer |
| **Praise** | Explicitly positive feedback | Acknowledge; no action required |

When leaving feedback as a reviewer, label your intent:
> "**Required:** The boundary condition at T=0 is wrong — this will crash."
>
> "**Suggestion:** This loop could be replaced with a list comprehension for clarity."
>
> "**Question:** Why is the thermal mass squared always taken as positive here?"

---

## How to Respond Constructively

**As the author receiving review:**

1. Read all comments before changing anything.
2. For each required change, make the fix and push.
3. Reply to every comment explaining what you did (or why you disagree).
4. Use "Resolve conversation" only when the issue is truly addressed.
5. If you disagree with a suggestion, say so politely with reasoning:
   > "I considered this, but the list comprehension version is harder to debug
   > because it hides the intermediate step. I'll keep the loop for now."

6. After addressing all feedback, request a re-review.

**Keep replies brief and professional.** A two-sentence explanation is usually sufficient.

---

## The Review Checklist

When you are the reviewer, evaluate the PR against this checklist:

### Scientific Correctness

- [ ] The mathematical derivation or physical model is correct.
- [ ] Equations are implemented as described (check against the paper or derivation).
- [ ] Numerical parameters (tolerances, step sizes) are physically reasonable.
- [ ] Edge cases are handled (zero temperature, zero field, singular limits).

### Code Quality

- [ ] The code is readable — someone unfamiliar can understand it.
- [ ] Variable and function names are descriptive.
- [ ] No code duplication that should be a function.
- [ ] No dead code (commented-out blocks left behind).
- [ ] No debug output (`print` statements, `breakpoint()` calls) left in.

### Tests

- [ ] New functionality has tests.
- [ ] Tests cover edge cases, not just the happy path.
- [ ] Existing tests still pass.

### Documentation

- [ ] New functions have docstrings (where the codebase uses them).
- [ ] The CHANGELOG or PR description explains what changed and why.
- [ ] No broken links or outdated descriptions.

### Repository Hygiene

- [ ] No generated files committed (`.pyc`, `__pycache__`, output figures).
- [ ] No large data files committed.
- [ ] No credentials or secrets.
- [ ] `.gitignore` updated if new file types need to be excluded.

---

## How to Leave a GitHub Review

1. Go to the PR page and click **"Files changed"**.
2. Read through the diff. Click `+` next to a line to leave an inline comment.
3. For overall feedback, click **"Review changes"** (top right), select the type:
   - **Comment** — general feedback, no approval
   - **Approve** — you are satisfied; the PR can be merged
   - **Request changes** — specific issues must be addressed before approval
4. Submit your review.

!!! tip "Review the whole PR before commenting"
    Read through all the changes before leaving any comment. Something that looks
    wrong on line 10 may be explained on line 80.

---

## Review Etiquette

**For the reviewer:**

- Be specific. "This function is wrong" is less useful than
  "This function will return `None` when `x < 0`, which will crash the caller."

- Focus on the code, not the person.
- Acknowledge good work. A review with only criticisms is demoralising.
- Review in a timely manner. A PR waiting for review for a week blocks the author.

**For the author:**

- Do not take feedback personally. The reviewer is improving the research output, not judging you.
- Do not dismiss feedback without engaging with it.
- Keep PRs small enough to review in one sitting (see Chapter 11).
- Respond promptly. A PR waiting for author response also blocks progress.

---

## Requesting a Re-Review

After addressing all feedback and pushing your changes:

1. On the PR page, locate the **Reviewers** section in the right sidebar.
2. Click the circular arrow icon (↻) next to the reviewer's name.
3. This notifies the reviewer that you have made changes and are ready for another look.

Do not re-request review until all comments are addressed and resolved.

---

## Common Mistakes

1. **Marking comments as resolved without actually fixing them.** Reviewers can
   see when a conversation is resolved. If the issue is not fixed, they will reopen it.

2. **Pushing large changes in response to a minor review comment.** Address exactly
   what was requested. If you want to refactor unrelated code, do it in a separate PR.

3. **Dismissing suggestions without explanation.** Even if you disagree, acknowledge
   the suggestion and explain your reasoning.

4. **Leaving reviews unread for days.** Review your notifications daily.
   A stale PR blocks your colleague's progress.

5. **Approving a PR without reading it.** A rubber-stamp approval defeats the entire
   purpose of code review. If you cannot review properly, say so.

---

## Best Practice Summary

- Respond to every review comment, even if just to say "Done."
- Distinguish between required changes, suggestions, and questions.
- Use "Resolve conversation" only when the issue is truly resolved.
- Request re-review after addressing all feedback.
- As a reviewer: be specific, kind, and timely.
- Keep PR review discussions professional — they are permanently recorded.

---

## Checklist

- [ ] I have read all review comments before making changes.
- [ ] I have addressed all required changes.
- [ ] I have replied to every comment (required changes, suggestions, and questions).
- [ ] I have marked resolved conversations as resolved.
- [ ] I have requested re-review after pushing my fixes.

---

## Exercises

1. **Receive review.** Ask a colleague to review your `feature/exercise-test` PR
   and leave at least two comments. Respond to each comment, make changes, push,
   and request re-review.

2. **Give review.** Review a colleague's PR. Leave at least one required change,
   one suggestion, and one question. Use the correct labels (Required / Suggestion / Question).

3. **Checklist walkthrough.** For a real PR in the group repository (recent or historical),
   go through the full review checklist above. How many items can you evaluate from the
   diff alone? Which require running the code?
