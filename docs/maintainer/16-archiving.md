# Chapter 16 — Archiving

## Overview

A repository should be archived when a project is complete: the paper is published,
the code is stable, and no further active development is planned.

Archiving is distinct from deletion. An archived repository:
- Remains accessible on GitHub
- Is clearly marked as inactive (read-only)
- Can be cloned and cited forever
- Cannot receive new issues, PRs, or commits (unless unarchived)

---

## When to Archive

Archive a repository when **all** of the following are true:

- [ ] The corresponding paper is published (or definitively not being published)
- [ ] The code is in a documented, working state
- [ ] A final release and tag have been created
- [ ] No further active development is planned by anyone in the group
- [ ] The PI has approved archiving

Do **not** archive repositories that other group members are using for ongoing work,
even if the original project is complete.

---

## Pre-Archiving Checklist

Complete these steps before clicking "Archive":

### 1. Create a Final Release and Tag

```bash
git checkout main
git pull origin main
git tag -a v1.0.0-final -m "Final release — paper published in PRD (DOI:10.1103/...)"
git push origin v1.0.0-final
```

Create a GitHub Release (Chapter 10) using this tag.
The release notes should include the paper DOI and a summary of what the code does.

### 2. Update README

The README should clearly state:
- The paper this code corresponds to (with full citation and DOI)
- That the repository is archived and not actively maintained
- Contact information for questions (PI email)

```markdown
> **Note:** This repository is archived. The code corresponds to:
> Author et al., *Title*, Journal, Year. DOI: [10.XXXX/...](https://doi.org/10.XXXX/...)
> For questions, contact [PI Name](mailto:pi@institute.edu).
```

### 3. Deposit to Zenodo

Zenodo provides a DOI for software, making it formally citable:

1. Go to [zenodo.org](https://zenodo.org) and log in with GitHub.
2. Go to **GitHub → Linked Repositories** → enable the repository.
3. On GitHub, create the final release (Zenodo automatically detects it).
4. Zenodo assigns a DOI (e.g., `10.5281/zenodo.XXXXXXX`).

Update `README.md` and `CITATION.cff` with the Zenodo DOI.

### 4. Add `CITATION.cff`

Create a `CITATION.cff` file in the repository root for machine-readable citation:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it using the following metadata."
type: software
title: "Phase Transition Solver"
authors:
  - family-names: "Lastname"
    given-names: "Firstname"
    orcid: "https://orcid.org/0000-0000-0000-0000"
version: 1.0.0
date-released: "2026-07-10"
doi: "10.5281/zenodo.XXXXXXX"
repository-code: "https://github.com/ORG/phase-transition-solver"
license: MIT
```

### 5. Scan for Secrets

Before archiving (especially before making public), scan the history for accidentally
committed credentials:

```bash
git log -p | grep -iE '(password|api.key|secret|token|credential)' | head -50
```

If any are found, they must be removed from history (consult the PI — this is a
non-trivial operation).

### 6. Clean Up Stale Branches

Delete all merged and abandoned branches. Only `main` should remain (plus any
explicitly preserved feature branches, archived with tags per Chapter 11).

### 7. Public Transition (if applicable)

If the repository should be public after archiving, complete Chapter 17 first,
then archive.

---

## Archiving on GitHub

1. **Settings → Danger Zone → Archive this repository**
2. Read the warning: all issues and PRs are locked; branches become read-only.
3. Confirm by typing the repository name.
4. Click **"I understand the consequences, archive this repository"**.

The repository is now read-only. It is still cloneable and visible.

---

## After Archiving

- Add the Zenodo DOI to the group's publications list.
- Notify collaborators.
- Update the group website if the repository was listed there.
- Create a git bundle as a final backup (Chapter 15).

---

## Unarchiving

If circumstances change and active development must resume:

**Settings → Danger Zone → Unarchive this repository**

Note: unarchiving does not restore closed issues or resolved PRs to their open state.

---

## Checklist

- [ ] Final release and tag created
- [ ] README updated with paper citation and archived notice
- [ ] `CITATION.cff` created or updated
- [ ] Code deposited on Zenodo (DOI obtained)
- [ ] History scanned for secrets
- [ ] Stale branches deleted
- [ ] Public transition completed (if applicable)
- [ ] Git bundle created and stored
- [ ] PI has approved archiving
- [ ] Repository archived on GitHub
- [ ] Zenodo DOI recorded in group publication list
