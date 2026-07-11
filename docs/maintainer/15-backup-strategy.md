# Chapter 15 — Backup Strategy

## Overview

GitHub is a collaboration platform, not a backup system.
A repository can be deleted, made inaccessible, or corrupted.
The group's backup strategy ensures that no code is ever permanently lost.

---

## Backup Layers

The group maintains three layers of backup:

| Layer | Location | Who maintains it | Update frequency |
|-------|----------|-----------------|-----------------|
| **GitHub** | Remote (cloud) | Automatic | On every push |
| **Local clones** | Each developer's machine | Each developer | On every pull |
| **Archive bundles** | Institutional server or external storage | Maintainer | At major milestones |

The combination of multiple local clones and GitHub means that even if GitHub
were to become unavailable, at least two independent copies of the complete
history exist.

---

## Ensuring All Work Is on GitHub

The backup is only as good as the most recent push.
All branches with meaningful work must be pushed to GitHub before:

- Extended absences (vacations, field work, conferences)
- Leaving the group
- Handing off a project

Push all local branches and tags:

```bash
git push --all origin
git push --tags origin
```

Verify GitHub has all tags:

```bash
git ls-remote --tags origin
```

Compare with your local tags:

```bash
git tag -l
```

---

## Git Bundle: Long-Term Archiving

A `git bundle` creates a single portable file containing the entire repository
history — all commits, branches, and tags. It can be stored anywhere and
restored completely.

### Creating a bundle

```bash
cd /path/to/repository
git bundle create /path/to/archive/repo-name-$(date +%Y%m%d).bundle --all
```

This creates a file like `phase-transition-solver-20260710.bundle`.

### Verifying the bundle

```bash
git bundle verify /path/to/archive/repo-name-20260710.bundle
```

### Restoring from a bundle

```bash
git clone /path/to/archive/repo-name-20260710.bundle restored-repo
cd restored-repo
git remote set-url origin git@github.com:ORG/REPO.git
git push --all origin
git push --tags origin
```

---

## When to Create a Bundle

| Event | Create a bundle? |
|-------|----------------|
| Paper submitted | ✓ Yes |
| Major release (`v1.0.0`) | ✓ Yes |
| Student offboarding | ✓ Yes |
| Before repository archiving | ✓ Yes |
| Every month (active projects) | Recommended |

Store bundles on:

- The group's institutional server (if available)
- An external hard drive stored at the institute
- A cloud storage service with access controlled by the PI

---

## If GitHub Goes Down

If GitHub is temporarily unavailable:

1. Continue working locally — Git does not require GitHub to be available.
2. Continue committing to local branches.
3. When GitHub is back, push normally: `git push --all origin`.

If GitHub becomes permanently unavailable (account deletion, service shutdown):

1. Identify the machine with the most recent clone.
2. Use that clone to push to an alternative platform (GitLab, Bitbucket, self-hosted).
3. Update all collaborators' remotes:
   ```bash
   git remote set-url origin git@gitlab.com:ORG/REPO.git
   ```

---

## Common Mistakes

1. **Assuming GitHub is the backup.** GitHub repositories can be deleted.
   A student with Admin access could delete a repository (another reason
   not to give students Admin).

2. **Never pushing feature branches.** Work-in-progress branches on local
   machines only exist on those machines. If the machine fails, the work is lost.
   Push branches early and often.

3. **Forgetting to push tags.** `git push` does not push tags by default.
   Always use `git push --tags` after creating tags.

---

## Checklist

- [ ] All branches pushed to GitHub before extended absences
- [ ] All tags pushed to GitHub (`git push --tags origin`)
- [ ] Git bundle created at each major milestone
- [ ] Bundle stored in at least one location outside GitHub
- [ ] Bundle verification run (`git bundle verify`)
- [ ] Restore procedure documented for the group
