# 06 · Site Infrastructure Plan

Covers the MkDocs setup, navigation tree, GitHub Pages deployment, and
repository-level configuration files.

---

## Technology Choices

| Concern | Choice | Reason |
|---------|--------|--------|
| Documentation site | MkDocs | Simple, Markdown-native, Python ecosystem |
| Theme | Material for MkDocs | Best feature set; search, dark mode, Mermaid |
| Deployment | GitHub Pages via Actions | Free, automatic, version-controlled |
| Diagrams | Mermaid (inline) | Renders on GitHub and MkDocs without export |
| Markdown extensions | pymdownx suite | Code highlighting, admonitions, tabs |

---

## `mkdocs.yml` Structure

```yaml
site_name: NNU-PP Research Software Handbook
site_description: Official software engineering handbook for the NNU-PP research group
site_author: NNU-PP Group
repo_url: https://github.com/Meridex/CodeHandbook
repo_name: Meridex/CodeHandbook
edit_uri: edit/main/docs/

theme:
  name: material
  language: en
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy
    - content.code.annotate

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.details
  - tables
  - attr_list

nav:
  - Home: index.md
  - Student Guide:
    - Introduction: student/01-introduction.md
    - Git vs GitHub: student/02-git-vs-github.md
    - Workflow Overview: student/03-workflow-overview.md
    - Initial Setup: student/04-initial-setup.md
    - SSH Authentication: student/05-ssh.md
    - Cloning the Repository: student/06-clone.md
    - Daily Workflow: student/07-daily-workflow.md
    - Branches: student/08-branches.md
    - Commits: student/09-commits.md
    - Pushing: student/10-push.md
    - Pull Requests: student/11-pull-requests.md
    - Reviews: student/12-reviews.md
    - Merge Conflicts: student/13-merge-conflicts.md
    - Updating Branches: student/14-updating-branches.md
    - Common Mistakes: student/15-common-mistakes.md
    - FAQ: student/16-faq.md
    - Cheat Sheet: student/17-cheat-sheet.md
    - Exercises: student/18-exercises.md
  - Maintainer Guide:
    - Repository Creation: maintainer/01-repo-creation.md
    - Repository Settings: maintainer/02-repo-settings.md
    - Branch Protection: maintainer/03-branch-protection.md
    - Collaborator Management: maintainer/04-collaborators.md
    - Labels: maintainer/05-labels.md
    - Milestones: maintainer/06-milestones.md
    - Project Board: maintainer/07-project-board.md
    - Review Workflow: maintainer/08-review-workflow.md
    - Merge Strategy: maintainer/09-merge-strategy.md
    - Releases: maintainer/10-releases.md
    - Tags: maintainer/11-tags.md
    - Documentation Policy: maintainer/12-documentation-policy.md
    - Testing Policy: maintainer/13-testing-policy.md
    - CI Preparation: maintainer/14-ci-preparation.md
    - Backup Strategy: maintainer/15-backup-strategy.md
    - Archiving: maintainer/16-archiving.md
    - Public Transition: maintainer/17-public-transition.md
    - Student Onboarding: maintainer/18-student-onboarding.md
    - Student Offboarding: maintainer/19-student-offboarding.md
  - Appendices:
    - Research Software Principles: appendices/research-software-principles.md
    - Group Policies: appendices/group-policies.md
    - Glossary: appendices/glossary.md
```

---

## GitHub Actions — Deploy Workflow

**File:** `.github/workflows/deploy-docs.yml`

```yaml
name: Deploy Handbook to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # needed for git-revision-date plugin

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install MkDocs and dependencies
        run: |
          pip install mkdocs-material

      - name: Build site
        run: mkdocs build --strict

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## Python Dependencies (`requirements-docs.txt`)

```
mkdocs-material>=9.5
```

---

## Repository Root Files

### `README.md` (handbook repository itself)

Sections:
1. What this handbook is.
2. How to read it online (link to GitHub Pages).
3. How to contribute (link to maintainer guide).
4. How to build locally:
   ```bash
   pip install mkdocs-material
   mkdocs serve
   # Open http://127.0.0.1:8000
   ```
5. License.

### `LICENSE`

MIT License (or group preference — confirm with PI).

### `.gitignore` (handbook repository)

```gitignore
site/           # MkDocs build output
.venv/
venv/
__pycache__/
*.pyc
.DS_Store
```

---

## Local Development Instructions

Students and maintainers can build the handbook locally:

```bash
git clone git@github.com:Meridex/CodeHandbook.git
cd CodeHandbook
pip install mkdocs-material
mkdocs serve
```

Then open `http://127.0.0.1:8000` in a browser.

Changes to any `.md` file are reflected live (hot reload).

---

## MkDocs Material Admonition Types Used

Throughout the handbook, use these admonition types consistently:

| Type | Used for |
|------|----------|
| `!!! note` | Background information |
| `!!! tip` | Best practice advice |
| `!!! warning` | Common mistake or dangerous command |
| `!!! danger` | Command that can cause data loss |
| `!!! example` | Worked example |
| `!!! info` | Reference or further reading |
| `??? details` | Collapsed section for advanced users |
