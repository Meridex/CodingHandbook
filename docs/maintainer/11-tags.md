# Chapter 11 — Tags

## Overview

Tags are permanent, named pointers to specific commits. Unlike branches
(which move as new commits are added), tags never change once created.

In a research group, tags serve a critical function: **they link published
results back to the exact code that produced them**.

---

## The Core Principle

> **Every published figure must correspond to a tagged commit.**
> **Every paper must have a corresponding Git tag.**

Without tags, it is impossible to answer the question:
*"What exact code produced Figure 3 of the 2026 paper?"*
With tags, the answer is: *"Check out tag `fig/PRD-2026-fig3`."*

---

## Lightweight vs Annotated Tags

| | Lightweight | Annotated |
|--|------------|-----------|
| Contains | Commit hash only | Commit hash + message + author + date |
| Visible in release list | No | Yes |
| Group policy | Not used | **Always use** |

Always use annotated tags:

```bash
git tag -a v1.0.0 -m "Version corresponding to arXiv:2601.12345"
```

---

## Tagging Convention

| Context | Format | Example |
|---------|--------|---------|
| Version release | `vMAJOR.MINOR.PATCH` | `v1.2.0` |
| Paper submission | `paper/arxiv-YYMM-NNNNN` | `paper/arxiv-2601-12345` |
| Paper figure | `fig/JOURNAL-YEAR-figN` | `fig/PRD-2026-fig3` |
| Conference | `conference/NAME-YEAR` | `conference/Lattice-2026` |

---

## Creating a Tag

Tags are created locally and then pushed to GitHub:

```bash
# Step 1: Ensure you are on main and up to date
git checkout main
git pull origin main

# Step 2: Create an annotated tag
git tag -a v1.2.0 -m "Version corresponding to PRD paper arXiv:2601.12345"

# Step 3: Push the tag to GitHub
git push origin v1.2.0
```

To push all local tags at once:

```bash
git push origin --tags
```

---

## Tagging a Past Commit

If the tag should point to an earlier commit (e.g., the exact commit used
for a figure produced last month):

```bash
# Find the commit hash
git log --oneline

# Tag that specific commit
git tag -a fig/PRD-2026-fig3 a3f2c91 -m "Code state for Figure 3 of PRD submission"
git push origin fig/PRD-2026-fig3
```

---

## Listing Tags

```bash
git tag -l              # list all tags
git tag -l "v*"         # list only version tags
git tag -l "paper/*"    # list only paper tags
```

On GitHub: **Releases → Tags** shows all tags with their associated commits.

---

## Checking Out a Tag

To inspect or reproduce results from a tagged version:

```bash
git checkout v1.2.0
```

This puts you in **detached HEAD** state — you can read files and run code,
but any new commits will not be on any branch. To create a branch from a tag
(e.g., to backport a bug fix):

```bash
git checkout -b bugfix/backport-v1.2 v1.2.0
```

---

## Deleting a Tag (Rare)

Tags should almost never be deleted — they are permanent scientific records.
Discuss with the PI before deleting any tag.

```bash
# Delete locally
git tag -d v1.2.0

# Delete on GitHub (use with extreme caution)
git push origin --delete v1.2.0
```

---

## Tagging Workflow for a Paper Submission

When submitting a paper:

```bash
# 1. Ensure all code for the paper is merged into main
# 2. Verify tests pass
# 3. Tag the submission state
git checkout main
git pull origin main
git tag -a paper/arxiv-2601-12345 -m "Code for arXiv:2601.12345 — Phase transitions in NNU-PP model"
git push origin paper/arxiv-2601-12345

# 4. Create a GitHub Release (Chapter 10) using this tag
```

Also tag individual figures:

```bash
git tag -a fig/PRD-2026-fig1 a3f2c91 -m "Code for Figure 1: phase diagram"
git tag -a fig/PRD-2026-fig2 b4d3e02 -m "Code for Figure 2: GW spectrum"
git push origin --tags
```

---

## Checklist

- [ ] All published figures tagged with `fig/JOURNAL-YEAR-figN`
- [ ] All paper submissions tagged with `paper/arxiv-YYMM-NNNNN`
- [ ] All release versions tagged with `vMAJOR.MINOR.PATCH`
- [ ] Tags use annotated format (not lightweight)
- [ ] All tags pushed to GitHub (`git push origin --tags`)
- [ ] Tag messages reference the arXiv ID or paper title
