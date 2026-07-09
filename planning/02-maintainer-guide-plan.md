# 02 · Maintainer Guide — Detailed Chapter Plan

Target audience: lab members who administer repositories and set policy.
Prior knowledge assumed: developer-level Git familiarity.

---

## Chapter 1 — Creating a Repository

**Goal:** Walk through the correct way to create a new group repository from scratch.

### Sections
- Naming convention for repositories (lowercase, hyphen-separated, descriptive).
  - Examples: `phase-transition-solver`, `gw-spectrum-calculator`
- Private vs public: all repositories start private.
- Initialise with README, `.gitignore` (Python / C++), and LICENSE.
- Clone locally immediately and verify.
- Default branch: must be `main`.
- Add a repository description and topics/tags on GitHub.

### Checklist
- [ ] Repository named correctly
- [ ] Private
- [ ] README present
- [ ] `.gitignore` appropriate for the language
- [ ] LICENSE selected
- [ ] Default branch is `main`
- [ ] Description and topics added

---

## Chapter 2 — Repository Settings

**Goal:** Configure GitHub repository settings correctly.

### Sections
- General settings:
  - Disable "Allow merge commits" (only squash merge allowed).
  - Enable "Allow squash merging".
  - Enable "Automatically delete head branches".
  - Disable "Allow rebase merging".
- Features: enable Issues, Wikis (optional), Projects (optional).
- Merge button options: set default to Squash and Merge.
- Danger Zone: archiving, transferring, deleting — when and how.

---

## Chapter 3 — Branch Protection Rules

**Goal:** Enforce the canonical workflow at the GitHub level.

### Sections
- Navigate to Settings → Branches → Add rule.
- Required settings for `main`:
  - Require a pull request before merging.
  - Require at least 1 approval.
  - Dismiss stale pull request approvals when new commits are pushed.
  - Require status checks to pass (once CI is added).
  - Require branches to be up to date before merging.
  - Restrict who can push to matching branches (maintainers only).
  - Do not allow bypassing the above settings.
- Why each rule exists.
- Testing the rules with a test branch.

### Diagram
- Screenshot walkthrough (annotated images or descriptive text).

---

## Chapter 4 — Collaborator Management

**Goal:** Add and remove students and developers with the correct permissions.

### Sections
- GitHub permission levels: Read / Triage / Write / Maintain / Admin.
- Group policy:
  - Students: **Write** access (can push branches, open PRs, cannot change settings).
  - Maintainers: **Maintain** access.
  - PI: **Admin** access.
- Adding a collaborator: Settings → Collaborators → Add people.
- Inviting via GitHub username or email.
- Revoking access when a student leaves.
- Teams (for organisations): creating a team, assigning members, assigning team to repository.
- Audit log — checking who did what.

---

## Chapter 5 — Labels

**Goal:** Use GitHub labels to organise issues and PRs.

### Sections
- Default GitHub labels and their meaning.
- Group-specific labels to create:

| Label | Colour | Meaning |
|-------|--------|---------|
| `type: feature` | `#0075ca` | New calculation or feature |
| `type: bugfix` | `#d73a4a` | Something is wrong |
| `type: docs` | `#cfd3d7` | Documentation only |
| `type: refactor` | `#e4e669` | No behaviour change |
| `type: experiment` | `#f9d0c4` | Exploratory, may not merge |
| `priority: high` | `#b60205` | Urgent |
| `priority: low` | `#0e8a16` | Can wait |
| `status: needs-review` | `#fbca04` | Waiting for reviewer |
| `status: blocked` | `#e11d48` | Waiting on something else |
| `good first issue` | `#7057ff` | Good for new students |

- Creating labels via the GitHub UI and via the API.
- Applying labels consistently.

---

## Chapter 6 — Milestones

**Goal:** Track progress toward paper deadlines and project goals.

### Sections
- What is a milestone? (group of issues/PRs with a due date)
- When to use milestones: paper submission, conference deadline, major release.
- Creating a milestone: title, description, due date.
- Assigning issues and PRs to milestones.
- Milestone progress bar.
- Closing a milestone.
- Naming convention: `paper-JOURNAL-YEAR`, `v1.0`, `conference-NAME-YEAR`.

---

## Chapter 7 — Project Board

**Goal:** Use GitHub Projects to visualise the state of work.

### Sections
- GitHub Projects (v2) overview.
- Recommended board columns: `Backlog` / `In Progress` / `In Review` / `Done`.
- Linking issues and PRs to the board.
- Automation: auto-move card when PR is merged.
- When to use a board vs milestones (board = current sprint; milestone = deadline).
- Keeping the board current (weekly habit).

---

## Chapter 8 — Review Workflow

**Goal:** Define how the maintainer conducts and enforces code reviews.

### Sections
- Who reviews: maintainer reviews all student PRs; students may review each other.
- Review SLA: respond within N working days (group to decide).
- Using the review checklist (from templates).
- Review comment types: `LGTM`, suggestion, required change, question.
- Approving vs requesting changes vs commenting.
- What to look for:
  - Scientific correctness (most important).
  - Does the code do what the PR description says?
  - Tests present and passing.
  - No dead code or debug output.
  - Documentation updated.
  - Style consistent with rest of codebase.
- Blocking a PR: when and how to leave a blocking review.
- Resolving a stale PR (no response from author).

---

## Chapter 9 — Merge Strategy

**Goal:** Explain and enforce the squash merge policy.

### Sections
- Why squash merge? (clean, linear history on `main`; feature branch noise hidden)
- How squash merge works (all commits → one commit on `main`).
- The squash merge commit message convention:
  ```
  Add gravitational wave spectrum calculation (#42)
  ```
- Verifying the merge was done correctly (`git log --oneline`).
- Deleting the feature branch after merge (done automatically if setting is on).
- What to do when someone accidentally used a regular merge.
- Revert strategy: `git revert <sha>` for reverting a squash-merged feature.

### Diagram
- Mermaid: before squash merge (feature branch with 5 commits) → after (one commit on `main`).

---

## Chapter 10 — Releases

**Goal:** Package and publish a release for publication or distribution.

### Sections
- What is a release on GitHub? (tag + release notes + optional binary assets)
- When to create a release:
  - Corresponding to a paper submission.
  - Corresponding to a conference presentation.
  - Stable, tested version that others will use.
- Release checklist (see templates).
- Semantic versioning: `MAJOR.MINOR.PATCH`.
  - `1.0.0` — first stable version
  - `1.1.0` — new feature added
  - `1.1.1` — bug fix
- Creating a release via GitHub UI.
- Writing good release notes (what changed, what's new, what's fixed).
- Attaching assets (pre-built binaries, data snapshots) — when appropriate.

---

## Chapter 11 — Tags

**Goal:** Use Git tags to mark scientifically significant states of the code.

### Sections
- Difference between lightweight and annotated tags.
- Group policy: always use annotated tags.
  ```bash
  git tag -a v1.0.0 -m "Version corresponding to arXiv:XXXX.XXXXX"
  git push origin v1.0.0
  ```
- Tagging convention:
  - `v1.0.0` — version tag
  - `paper/arxiv-XXXX` — paper submission
  - `fig/paper-YEAR-figN` — specific figure
- The principle: **every published figure must correspond to a tagged commit**.
- Listing tags: `git tag -l`.
- Checking out a tag for reproducibility.

---

## Chapter 12 — Documentation Policy

**Goal:** Define standards for in-code and external documentation.

### Sections
- Documentation is not optional; it is part of the research output.
- What must be documented:
  - Every public function/class: docstring with purpose, parameters, return value.
  - Every non-obvious algorithm: reference to equation or paper.
  - Every script: header with description, usage, and example.
  - Every configuration file: inline comments.
- MkDocs usage: all `docs/` Markdown files are part of the handbook.
- The README must stay current.
- Deprecation notice before removing old interfaces.
- Language-specific documentation standards (to be added in future expansion):
  - Python: NumPy-style or Google-style docstrings.
  - C++: Doxygen comments.

---

## Chapter 13 — Testing Policy

**Goal:** Define minimum testing requirements for research code.

### Sections
- Philosophy: not every line needs 100% coverage; critical algorithms must be tested.
- What must have tests:
  - Numerical solvers (regression tests: known input → known output).
  - Parser/loader functions (edge cases).
  - Any function that is referenced in a paper.
- Testing framework recommendations: `pytest` (Python), `Catch2` (C++).
- Test organisation: `tests/` directory mirrors `src/` structure.
- Running tests locally before opening a PR.
- CI will eventually run tests automatically (see Chapter 14).
- Test file naming: `test_<module>.py`.

---

## Chapter 14 — CI Preparation

**Goal:** Prepare the repository for Continuous Integration (GitHub Actions).

### Sections
- What is CI and why the group needs it.
- Current state: CI is prepared but not fully deployed.
- The first CI workflow: run `pytest` on every PR.
- GitHub Actions basics: `.github/workflows/`, YAML syntax.
- Example minimal workflow:
  ```yaml
  name: Tests
  on: [push, pull_request]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with:
            python-version: '3.11'
        - run: pip install -r requirements.txt
        - run: pytest
  ```
- Adding the CI badge to README.
- Future workflows: linting, type checking, docs build.

---

## Chapter 15 — Backup Strategy

**Goal:** Ensure the code is never permanently lost.

### Sections
- GitHub is not a backup — it is a collaboration platform.
- Backup layers:
  1. GitHub (remote; always up to date if all branches are pushed).
  2. Local clones on multiple machines.
  3. Institutional server backup (if available).
  4. Periodic `git bundle` for long-term archiving.
- Pushing all branches before leaving a project:
  ```bash
  git push --all origin
  git push --tags origin
  ```
- Verifying that GitHub has all tags:
  ```bash
  git ls-remote --tags origin
  ```
- What to do if GitHub goes down (local copy is sufficient to continue working).

---

## Chapter 16 — Archiving

**Goal:** Preserve a finished project for long-term scientific record.

### Sections
- When to archive: project is complete, paper published, no further active development.
- Archiving on GitHub: Settings → Danger Zone → Archive repository.
  - Repository becomes read-only.
  - Issues and PRs are locked.
  - Still publicly visible (after public transition).
- Create a final release and tag before archiving.
- Deposit code to Zenodo or similar for a DOI.
- Record the DOI in the README.
- `CITATION.cff` file for machine-readable citation.
- Notify collaborators before archiving.

---

## Chapter 17 — Public Transition

**Goal:** Move a repository from private to public when a paper is published.

### Sections
- When to go public: paper is accepted or posted to arXiv.
- Pre-transition checklist:
  - [ ] No credentials or secrets in history.
  - [ ] No unpublished data in repository.
  - [ ] LICENSE is present and correct.
  - [ ] README is complete and accurate.
  - [ ] All temporary branches cleaned up.
  - [ ] Final release and tag created.
  - [ ] PI has approved.
- Scanning for secrets: `git log -p | grep -E '(password|key|token|secret)'`.
- Changing visibility: Settings → Danger Zone → Change repository visibility.
- Announce to the community (Twitter/X, group website, collaborators).
- Add to the group's public repository list.

---

## Chapter 18 — Student Onboarding

**Goal:** Efficiently bring a new student up to speed.

### Sections
- Use the student onboarding checklist (see templates).
- Step-by-step:
  1. Invite student to GitHub organisation / repository.
  2. Send links to this handbook (student section).
  3. Verify SSH key is set up.
  4. Verify student can clone the repository.
  5. Assign the first "good first issue".
  6. Walk through the first PR together.
  7. Confirm student is in the group chat / mailing list.
- First assignment: complete the handbook exercises (Chapter 18 of student guide).
- Expected timeline for a new student to become self-sufficient: ~2 weeks.

### Onboarding Checklist (also in templates/)
- [ ] GitHub account created
- [ ] Added to repository as collaborator (Write)
- [ ] SSH key configured
- [ ] Repository cloned successfully
- [ ] First branch created
- [ ] First commit made
- [ ] First PR opened and reviewed
- [ ] Handbook exercises completed

---

## Chapter 19 — Student Offboarding

**Goal:** Cleanly remove a departing student from the repository.

### Sections
- When: graduation, end of exchange, or departure from group.
- Actions before removing access:
  - All open PRs: either merge, transfer to another branch owner, or close with note.
  - All open issues assigned to the student: reassign.
  - All branches pushed and not abandoned silently.
  - Final documentation of any in-progress work.
- Remove from repository collaborators: Settings → Collaborators → Remove.
- If the student is in a GitHub organisation team: remove from team.
- Transfer any domain knowledge (Slack/email handover notes).
- Archive student-specific branches if needed:
  ```bash
  git tag archive/student-NAME/feature-xyz feature/feature-xyz
  git push origin archive/student-NAME/feature-xyz
  git push origin --delete feature/feature-xyz
  ```
- Add to the alumni list in the group README (optional).
