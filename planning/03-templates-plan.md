# 03 · Templates Plan

All templates live in `docs/templates/` and are also copied to `.github/` where
GitHub requires them.

---

## 1. README Template

**File:** `docs/templates/README-template.md`
**Used for:** Every new group repository.

### Required Sections
```markdown
# Project Name

One-paragraph description of what the code does and what physics it addresses.

## Status
Badge: CI · License · Version

## Requirements
- Python >= 3.10 (or C++ standard)
- Dependencies listed

## Installation
Step-by-step. Not just `pip install .`.

## Quick Start
Minimal working example (< 20 lines).

## Usage
Common use cases with real commands.

## Repository Structure
Annotated directory tree.

## Documentation
Link to full handbook / MkDocs site.

## Citation
How to cite this code. Include CITATION.cff reference.

## License
Name and link.

## Contact
PI name and email.
```

---

## 2. Pull Request Template

**File:** `.github/PULL_REQUEST_TEMPLATE.md`

### Content
```markdown
## Motivation
<!-- Why is this change needed? What problem does it solve? -->

## Summary of Changes
<!-- What was changed? High-level description. -->

## Files Affected
<!-- List the main files modified. -->

## Testing Performed
<!-- How was this tested? Run command, expected output. -->

## Screenshots
<!-- If applicable (plots, output, UI). Delete if not applicable. -->

## Related Issue
<!-- Closes #N, or "None" -->

## Checklist
- [ ] Code compiles / runs without errors
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No debug output left in code
- [ ] No large data files committed
- [ ] Branch is up to date with main
```

---

## 3. Issue Template — Bug Report

**File:** `.github/ISSUE_TEMPLATE/bug_report.yml`

### Fields
- **Title prefix:** `[Bug]`
- **Labels:** `type: bugfix`
- Fields:
  - **Describe the bug** (textarea, required)
  - **To reproduce** (steps numbered, textarea)
  - **Expected behaviour** (textarea)
  - **Actual behaviour / error message** (textarea, code block)
  - **Environment** (OS, Python/C++ version, relevant package versions)
  - **Relevant commit or tag** (text input)
  - **Possible cause** (textarea, optional)

---

## 4. Issue Template — Feature Request

**File:** `.github/ISSUE_TEMPLATE/feature_request.yml`

### Fields
- **Title prefix:** `[Feature]`
- **Labels:** `type: feature`
- Fields:
  - **Motivation** (why is this feature needed? what physics problem?)
  - **Proposed implementation** (how might it work?)
  - **Alternatives considered** (what else was considered?)
  - **Is this related to a paper or calculation?** (text)
  - **Priority** (dropdown: high / medium / low)

---

## 5. Review Checklist

**File:** `docs/templates/review-checklist.md`
**Used by:** Reviewers when evaluating a PR.

```markdown
# Review Checklist

## Scientific Correctness
- [ ] The algorithm matches the described method
- [ ] Units and conventions are consistent
- [ ] Edge cases are handled (zero, negative, large values)
- [ ] Results validated against known limit or reference

## Code Quality
- [ ] Code is readable without needing to ask the author
- [ ] No dead code (commented-out blocks, unused variables)
- [ ] No debug print statements or hardcoded paths
- [ ] No generated or binary files committed

## Correctness
- [ ] Code compiles / runs without errors
- [ ] Tests pass (run locally if needed)
- [ ] No obvious bugs in logic

## Documentation
- [ ] Docstrings present for all new public functions
- [ ] Inline comments on non-obvious logic
- [ ] README updated if installation/usage changed
- [ ] CHANGELOG or release notes updated (if applicable)

## Style
- [ ] Naming is clear and consistent with the rest of the codebase
- [ ] Formatting follows group conventions

## Process
- [ ] PR description is complete (motivation, summary, testing)
- [ ] Branch is up to date with main
- [ ] Related issue is linked
```

---

## 6. Release Checklist

**File:** `docs/templates/release-checklist.md`
**Used by:** Maintainer before creating a GitHub release.

```markdown
# Release Checklist — vX.Y.Z

## Before Tagging
- [ ] All planned features for this release are merged to main
- [ ] All tests pass on main
- [ ] CHANGELOG updated with release notes
- [ ] Version number bumped in code (setup.cfg / pyproject.toml / CMakeLists.txt)
- [ ] Documentation up to date
- [ ] No known blocking bugs

## Tagging
- [ ] Annotated tag created:
      git tag -a vX.Y.Z -m "Release vX.Y.Z — brief description"
- [ ] Tag pushed: git push origin vX.Y.Z
- [ ] Tag verified on GitHub

## GitHub Release
- [ ] Release created from tag on GitHub
- [ ] Release title: "vX.Y.Z — Brief description"
- [ ] Release notes written (new features, bug fixes, breaking changes)
- [ ] Assets attached if applicable

## If Paper-Linked
- [ ] Tag includes arXiv ID in message
- [ ] README citation section updated
- [ ] Zenodo deposit created and DOI recorded
- [ ] CITATION.cff updated

## After Release
- [ ] Announce to group
- [ ] Close corresponding milestone
```

---

## 7. Student Onboarding Checklist

**File:** `docs/templates/student-onboarding-checklist.md`
**Used by:** Maintainer when a new student joins.

```markdown
# Student Onboarding Checklist

**Student name:** ___________________
**Start date:** ___________________
**Assigned maintainer:** ___________________

## Before First Day
- [ ] GitHub username received
- [ ] Added to repository as collaborator (Write permission)
- [ ] Handbook link sent
- [ ] Group chat / mailing list access granted

## First Week
- [ ] Git installed and configured (`user.name`, `user.email`)
- [ ] SSH key generated and added to GitHub
- [ ] SSH connection tested (`ssh -T git@github.com`)
- [ ] Repository cloned successfully
- [ ] Handbook chapters 1–7 read
- [ ] First branch created
- [ ] First commit made (can be trivial)
- [ ] First PR opened (can be a docs fix)
- [ ] First PR reviewed and merged

## First Two Weeks
- [ ] Handbook chapters 8–18 read
- [ ] Exercises 1–10 completed in example repository
- [ ] Familiar with PR template and review checklist
- [ ] Assigned first real issue

## Ongoing
- [ ] Understands branch protection (no direct push to main)
- [ ] Knows how to rebase a branch
- [ ] Knows how to resolve a merge conflict
- [ ] Knows how to tag a commit
```

---

## 8. Repository Checklist

**File:** `docs/templates/repository-checklist.md`
**Used by:** Maintainer when setting up a new repository.

```markdown
# New Repository Checklist

**Repository name:** ___________________
**Created by:** ___________________
**Date:** ___________________

## Creation
- [ ] Name follows convention (lowercase, hyphen-separated)
- [ ] Private visibility
- [ ] README created
- [ ] .gitignore appropriate for language
- [ ] LICENSE selected (MIT / GPL / see group policy)
- [ ] Default branch: main
- [ ] Description and topics added

## Settings
- [ ] Allow squash merging: ON
- [ ] Allow merge commits: OFF
- [ ] Allow rebase merging: OFF
- [ ] Automatically delete head branches: ON

## Branch Protection (main)
- [ ] Require PR before merging: ON
- [ ] Require 1 approval: ON
- [ ] Dismiss stale approvals: ON
- [ ] Restrict direct push to main: ON

## Collaborators
- [ ] All relevant students added (Write)
- [ ] Maintainer added (Maintain or Admin)

## Labels
- [ ] Group label set created

## Initial Structure
- [ ] docs/ directory created
- [ ] src/ directory created
- [ ] tests/ directory created
- [ ] .github/PULL_REQUEST_TEMPLATE.md added
- [ ] .github/ISSUE_TEMPLATE/ populated
```
