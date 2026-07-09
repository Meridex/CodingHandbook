# Group Policies

This appendix documents the concrete policies that apply to all developers
and all repositories in the NNU-PP research group.
These policies are referenced throughout the handbook.

When a policy is updated, it is updated here and the change is announced in the group.

---

## Repository Policies

### R1 — Visibility
All new repositories are created as **private**.
Public transition requires PI approval and completion of the
[public transition checklist](../maintainer/17-public-transition.md).

### R2 — Naming
Repository names use lowercase letters and hyphens only.
Format: `descriptive-name` or `descriptive-name-language`.
Examples: `phase-transition-solver`, `gw-spectrum-calculator-py`.

### R3 — Required Files
Every repository must contain at the time of first collaborator access:
- `README.md` (using the group template)
- `.gitignore` (appropriate for the primary language)
- `LICENSE` (MIT unless the PI specifies otherwise)
- `CITATION.cff` (added before archiving/publication)

### R4 — Default Branch
The default branch is always `main`. The name `master` is not used.

---

## Workflow Policies

### W1 — No Direct Commits to `main`
All changes to `main` go through Pull Requests.
Direct pushes to `main` are blocked by branch protection rules.

### W2 — Squash Merge Only
The only permitted merge strategy for PRs into `main` is **Squash and Merge**.
Regular merge commits and rebase merges are disabled in repository settings.

### W3 — Branch Naming
Branches must use one of the approved prefixes:
`feature/`, `bugfix/`, `docs/`, `refactor/`, `experiment/`, `chore/`.
Followed by a lowercase, hyphen-separated description.
Example: `feature/thermal-correction`.

### W4 — Delete After Merge
Feature branches are deleted after their PR is merged.
GitHub auto-deletes remote branches (repository setting).
Developers delete local branches manually with `git branch -d`.

### W5 — Commit Message Format
Commit messages use the imperative mood, ≤72 characters on the subject line.
Format: `Verb Description` (e.g., `Add thermal correction`, `Fix sign error`).
Vague messages (`update`, `fix`, `wip`) are not acceptable.

---

## Access Policies

### A1 — Permission Levels
| Role | GitHub Level |
|------|-------------|
| Student | Write |
| Post-doc / Senior student | Maintain |
| PI | Admin |
| External collaborator | Write (specific repository, PI approval required) |

### A2 — No Admin for Students
Students are never granted Admin access, regardless of seniority or trust.

### A3 — Access Revocation
Access is revoked upon departure from the group.
The offboarding process (Maintainer Guide Chapter 19) must be completed
before access is revoked.

---

## Review Policies

### RV1 — Minimum Approval Count
Every PR requires at least **1 approval** from a reviewer with Maintain or Admin permission.

### RV2 — Review Response Time (SLA)
Assigned reviewers respond within **2 working days** of assignment.
"Respond" means approve, request changes, or leave a substantive comment with a timeline.

### RV3 — Stale Approval Dismissal
Approvals are automatically dismissed when new commits are pushed to an approved PR.
The reviewer must re-approve the updated code.

### RV4 — Self-Review Prohibited
Authors may not approve their own Pull Requests.

### RV5 — Scientific Correctness First
Review must address scientific correctness before code style.
A PR with perfect code style but wrong physics must not be approved.

---

## Tagging and Release Policies

### T1 — Annotated Tags
All tags are annotated (created with `git tag -a`).
Lightweight tags are not used.

### T2 — Published Figures
Every figure that appears in a published paper must correspond to a tagged commit.
Tag format: `fig/JOURNAL-YEAR-figN`.

### T3 — Paper Submissions
Every paper submission must be tagged.
Tag format: `paper/arxiv-YYMM-NNNNN`.

### T4 — Semantic Versioning
All releases use semantic versioning: `vMAJOR.MINOR.PATCH`.
Releases are created via GitHub Releases, not manual tags alone.

---

## Testing Policies

### TS1 — Tests Before PR
All tests must pass locally before opening a PR.
The PR description must include the test command run and its result.

### TS2 — Tests for Published Results
Every function whose output appears in a paper must have a corresponding test.

### TS3 — Regression Tests
New bug fixes must include a regression test that would have caught the bug.

---

## Documentation Policies

### D1 — Docstrings Required
Every public function must have a docstring documenting purpose, parameters,
return value, and (if applicable) the source equation/paper.

### D2 — Algorithm Citations
Every implementation of a non-trivial algorithm must cite the source
inline in the code.

### D3 — README Currency
The README must accurately reflect the current code state.
Outdated README sections must be updated as part of any PR that changes
user-facing behaviour.

---

## Policy Update Process

Policies are updated via Pull Request to this handbook.
Proposed policy changes must:
1. Be discussed in a group meeting or in an Issue before opening a PR.
2. Be approved by the PI.
3. Be communicated to all active group members after merging.

Policy version: **2026-07-10** — initial handbook release.
