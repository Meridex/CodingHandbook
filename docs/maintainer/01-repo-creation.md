# Chapter 1 — Creating a Repository

## Overview

Every group repository starts correctly or it accumulates technical debt immediately.
This chapter walks through the full process of creating a new repository from scratch,
with every setting configured before the first student clones it.

**Do not shortcut this process.** A repository created hastily — wrong visibility,
missing `.gitignore`, wrong default branch — causes problems that are hard to fix later.

---

## Repository Naming Convention

Repository names must follow these rules:

- **Lowercase only**
- **Hyphens** for word separation (not underscores, not spaces)
- **Descriptive** — the name should tell an outsider what the code does
- **Concise** — aim for 2–4 words maximum

| ✓ Good | ✗ Bad |
|--------|-------|
| `phase-transition-solver` | `PTS` |
| `gw-spectrum-calculator` | `GW_calc_v2` |
| `bubble-nucleation-rate` | `mycode` |
| `thermal-potential-py` | `Project1` |

If the repository is language-specific and multiple language versions may exist,
append the language: `thermal-potential-py`, `thermal-potential-cpp`.

---

## Step 1: Create the Repository on GitHub

1. Navigate to the group's GitHub organisation page.
2. Click **Repositories → New**.
3. Fill in:
   - **Repository name:** following the convention above
   - **Description:** one sentence describing the code and its physics application
   - **Visibility:** **Private** (all repositories start private)
   - **Initialize with:** check all three:
     - Add a README file
     - Add `.gitignore` (select the appropriate template: Python or C++)
     - Choose a license (MIT for most cases; confirm with PI)
4. Click **Create repository**.

!!! warning "Always start private"
    All group repositories begin private. The public transition is a deliberate step
    covered in Chapter 17. Never create a public repository without PI approval.

---

## Step 2: Verify the Default Branch

GitHub's default may still create `master` in some contexts.
Verify immediately after creation:

1. Go to **Settings → General → Default branch**.
2. Confirm it says `main`.
3. If it says `master`: click the pencil icon, type `main`, click **Update**.

---

## Step 3: Add Repository Description and Topics

A well-labelled repository is discoverable and professional.

1. On the repository's main page, click the gear icon next to **"About"**.
2. Add:
   - **Description:** one-sentence summary (same as the creation description)
   - **Website:** link to the paper DOI or group website once published (leave blank initially)
   - **Topics:** relevant tags for discoverability, e.g.:
     ```
     physics  cosmology  phase-transition  python  research-code
     ```

3. Click **Save changes**.

---

## Step 4: Clone Locally and Verify

Immediately clone the new repository to verify it was created correctly:

```bash
git clone git@github.com:ORG/new-repo-name.git
cd new-repo-name
git log --oneline
git remote -v
ls -la
```

Confirm:

- `.gitignore` is present and appropriate for the language
- `README.md` is present
- `LICENSE` is present
- Default branch is `main`
- Remote URL is SSH

---

## Step 5: Initial Repository Structure

After cloning, set up the standard directory structure before adding any other files:

```bash
mkdir -p src tests docs examples scripts
touch src/.gitkeep tests/.gitkeep docs/.gitkeep
```

Edit `README.md` using the [README template](../templates/README-template.md).
At minimum, fill in the project name, description, and requirements sections.

Commit the initial structure:

```bash
git add .
git commit -m "Initialise repository structure"
git push origin main
```

!!! note "This is the only direct commit to `main`"
    The initial structure commit is the one acceptable direct push to `main`.
    All subsequent changes must go through Pull Requests.

---

## Post-Creation: Configure Settings and Protection

The next two chapters cover this in detail, but immediately after creation:

1. **Chapter 2:** Configure merge settings (disable regular merge, enable squash merge).
2. **Chapter 3:** Enable branch protection on `main`.
3. **Chapter 4:** Add collaborators.

Do not give students access until all protection rules are in place.

---

## Creation Checklist

- [ ] Repository named correctly (lowercase, hyphen-separated, descriptive)
- [ ] Visibility: Private
- [ ] README.md present
- [ ] `.gitignore` present and appropriate for the language
- [ ] LICENSE selected (confirm with PI)
- [ ] Default branch is `main` (not `master`)
- [ ] Description added on GitHub
- [ ] Topics/tags added
- [ ] Cloned locally and verified
- [ ] Initial directory structure committed
- [ ] Repository settings configured (Chapter 2)
- [ ] Branch protection enabled (Chapter 3)
- [ ] Collaborators added (Chapter 4)

---

## Common Mistakes

1. **Creating the repository with `master` as the default branch.** Always verify
   and rename to `main` before anyone clones.

2. **Skipping the `.gitignore`.** The first commit students make will include
   `__pycache__/` and `.DS_Store` if `.gitignore` is missing.

3. **Using a vague name.** Repository names cannot be easily changed once
   collaborators have cloned and set up their remotes.

4. **Adding collaborators before protection rules are in place.** A student could
   accidentally push to `main` in the gap.
