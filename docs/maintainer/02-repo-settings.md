# Chapter 2 — Repository Settings

## Overview

GitHub repository settings control which operations are allowed, how merges work,
and which features are enabled. Configuring these correctly enforces the group workflow
at the platform level — preventing mistakes rather than correcting them after the fact.

Configure these settings **immediately after repository creation**, before adding collaborators.

---

## Navigate to Settings

From the repository page: **Settings → General**

---

## Section 1: General → Merge Button

This is the most critical setting. It controls which merge strategies GitHub allows.

**Required configuration:**

| Option | Setting | Reason |
|--------|---------|--------|
| Allow merge commits | **Disabled** | Regular merge creates noisy merge commits on `main` |
| Allow squash merging | **Enabled** | The group's required merge strategy |
| Allow rebase merging | **Disabled** | Rebase merging bypasses squash; creates multiple commits on `main` |

**How to set:**

1. Scroll to **"Pull Requests"** section under General.
2. Uncheck **"Allow merge commits"**.
3. Ensure **"Allow squash merging"** is checked.
4. Set the default commit message for squash merge to **"Pull request title and description"**.
5. Uncheck **"Allow rebase merging"**.

After this, the green "Merge pull request" button on every PR will only offer
"Squash and merge" — the wrong options are removed.

---

## Section 2: Automatically Delete Head Branches

Enable this so merged feature branches are deleted from GitHub automatically.

1. Under **"Pull Requests"**, find **"Automatically delete head branches"**.
2. Check the box.

Students still need to delete their local branches manually (`git branch -d ...`),
but the remote cleanup is automatic.

---

## Section 3: Features

Under **"Features"**:

| Feature | Setting | Note |
|---------|---------|------|
| Wikis | Disabled | Documentation lives in `docs/` and MkDocs, not the Wiki |
| Issues | **Enabled** | The group uses Issues for task tracking |
| Projects | Enabled (optional) | Enable if using a GitHub Project board (Chapter 7) |
| Discussions | Disabled | Use group chat for discussions |
| Sponsorships | Disabled | Not applicable |

---

## Section 4: Pull Requests — Additional Settings

Still under General → Pull Requests:

- **"Always suggest updating pull request branches"** — Enable.
  This shows a button on PRs when the branch is behind `main`, prompting the author to rebase.

- **"Allow auto-merge"** — Disable (for now).
  Auto-merge can be enabled later once CI is fully in place and reliable.

---

## Section 5: The Danger Zone

Located at the bottom of Settings → General. Understand these options:

| Action | When to use |
|--------|------------|
| **Change repository visibility** | When transitioning to public (Chapter 17) |
| **Transfer ownership** | If the repository moves to another organisation or user |
| **Archive this repository** | When a project is complete (Chapter 16) |
| **Delete this repository** | Never, without PI approval and full backup |

!!! danger "Never delete without backup"
    Repository deletion is irreversible on GitHub. Before any deletion:
    - Create a `git bundle` of the entire repository
    - Confirm with the PI in writing
    - Wait 24 hours after confirmation before proceeding

---

## Verifying the Configuration

After applying all settings, verify by checking the PR merge button.
Create a test branch and open a test PR:

```bash
git checkout -b chore/test-settings
echo "# test" >> README.md
git add README.md
git commit -m "Test: verify repository settings"
git push -u origin chore/test-settings
```

Open a PR. On the PR page, the green merge button should show only **"Squash and merge"**.
Close the PR without merging. Delete the test branch.

---

## Settings Checklist

- [ ] Allow merge commits: **Disabled**
- [ ] Allow squash merging: **Enabled**
- [ ] Default squash message: **Pull request title and description**
- [ ] Allow rebase merging: **Disabled**
- [ ] Automatically delete head branches: **Enabled**
- [ ] Wikis: **Disabled**
- [ ] Issues: **Enabled**
- [ ] "Always suggest updating pull request branches": **Enabled**
- [ ] Verified: merge button shows only "Squash and merge"
