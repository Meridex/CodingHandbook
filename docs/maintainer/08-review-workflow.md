# Chapter 8 — Review Workflow

## Overview

The maintainer is responsible for ensuring that every Pull Request receives
a timely, thorough review. This chapter defines who reviews, what they look for,
how to handle edge cases, and how to enforce review quality.

---

## Who Reviews

| PR type | Primary reviewer |
|---------|-----------------|
| Student's feature work | Maintainer |
| Student's bug fix | Maintainer |
| Maintainer's own PR | Another maintainer or the PI |
| PI's PR | Maintainer |
| External collaborator's PR | Maintainer |

**Students may also review each other's PRs** — this is encouraged for knowledge sharing —
but their approval does not count toward the required approval unless the maintainer
also approves. The minimum 1 approval required by branch protection must come from
someone with Maintain or Admin permission.

---

## Review SLA (Service Level Agreement)

The group policy: **respond to a PR within 2 working days** of it being assigned.

"Respond" means:
- Approve and merge, or
- Leave at least one substantive comment and request changes, or
- Leave a comment explaining a delay ("I'll review this by [date]")

A PR that waits for review for more than a week blocks the author's progress
and signals that the process has broken down.

If you are unable to review within the SLA, reassign to another reviewer.

---

## What to Look For

### 1. Scientific Correctness (highest priority)

- Are the equations implemented correctly? Check against the paper or derivation.
- Are numerical parameters (tolerances, step sizes, grid points) physically reasonable?
- Are edge cases handled (T = 0, φ = 0, singular limits)?
- Does the output match expectations for known test cases?

### 2. Code Does What the PR Says

- Read the PR description. Then read the diff. Does the diff implement what the description says?
- Are there changes in the diff that are not mentioned in the description?
- Are there items mentioned in the description that are not in the diff?

### 3. Tests

- Is there a test for the new functionality?
- Do the tests cover edge cases, not just the happy path?
- Run the tests locally when the change involves numerical output:
  ```bash
  git fetch origin
  git checkout feature/branch-name
  python -m pytest
  ```

### 4. Documentation

- New functions should have docstrings.
- Non-obvious algorithms must reference the equation or paper.
- If a public interface changed, the documentation must reflect it.
- The PR description itself is part of the permanent record — ensure it is complete.

### 5. Code Quality

- No dead code (commented-out blocks from debugging).
- No debug print statements.
- No generated files committed.
- Style is consistent with the rest of the codebase.
- Names are descriptive and follow existing conventions.

---

## Review Comment Types

Label your intent explicitly:

```
Required: The Daisy correction sign is wrong — this inverts the phase boundary direction.

Suggestion: This loop could be replaced with numpy broadcasting for clarity and speed.

Question: Why is phi_min hardcoded to 0.01 here? Is there a physics reason?

Nit: Extra blank line on line 47.
```

**Required** changes must be fixed before approval.
**Suggestions** are recommendations — the author may accept or decline with reasoning.
**Questions** may or may not require code changes — they may result in a clarifying comment.
**Nits** are trivial; do not block a PR over them.

---

## Approving vs Requesting Changes vs Commenting

| Action | When to use |
|--------|------------|
| **Approve** | The PR is correct and ready to merge (with or without minor nits addressed) |
| **Request changes** | One or more Required changes must be addressed before merge |
| **Comment** | You have feedback but are not the blocking reviewer; or you need to think more |

Do not approve a PR if you are uncertain about the scientific correctness.
Leave a **Comment** with your questions and wait for resolution.

---

## After Approval: Merging

The maintainer merges the PR:

1. Confirm the branch is up to date with `main` (GitHub shows a warning if not).
   If not: ask the author to rebase, or click "Update branch" (merge) as a last resort.
2. Confirm all conversations are resolved.
3. Confirm CI passes (once CI is active).
4. Click **"Squash and merge"**.
5. Edit the squash commit message to:
   ```
   Brief description of change (#PR-number)
   
   Optional: one-line context if the title is not fully self-explanatory.
   ```
6. Click **"Confirm squash and merge"**.
7. The remote branch is deleted automatically.

---

## Handling Stale PRs

A PR is stale if the author has not responded to review feedback within 7 days.

Steps:
1. Leave a comment: *"Pinging @author — any update on this? Happy to help if you're stuck."*
2. Wait 3 more days.
3. If still no response: label `status: stale`.
4. After 2 weeks without response: close the PR with a note explaining it can be reopened.

Do not let stale PRs accumulate. They clutter the repository and create false
impressions about work in progress.

---

## Checklist

- [ ] Review responded to within 2 working days
- [ ] Scientific correctness checked (most important)
- [ ] Tests run locally for numerical changes
- [ ] All comments labelled (Required / Suggestion / Question / Nit)
- [ ] Merge uses "Squash and merge" only
- [ ] Squash commit message follows the convention
- [ ] Stale PRs actioned weekly
