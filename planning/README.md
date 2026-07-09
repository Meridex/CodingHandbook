# NNU-PP Research Software Handbook — Planning Index

This directory contains the detailed planning documents for building the group's
research software handbook. Each file covers one major topic area.

## File Index

| File | Topic |
|------|-------|
| [00-project-overview.md](00-project-overview.md) | Overall structure, objectives, deliverables, and writing conventions |
| [01-student-guide-plan.md](01-student-guide-plan.md) | Chapter-by-chapter plan for the Student Guide |
| [02-maintainer-guide-plan.md](02-maintainer-guide-plan.md) | Chapter-by-chapter plan for the Maintainer Guide |
| [03-templates-plan.md](03-templates-plan.md) | All templates to be created (PR, Issue, README, checklists, …) |
| [04-example-repository-plan.md](04-example-repository-plan.md) | Content and purpose of the practice example repository |
| [05-diagrams-plan.md](05-diagrams-plan.md) | Every Mermaid diagram to be produced, with a sketch of its content |
| [06-site-infrastructure-plan.md](06-site-infrastructure-plan.md) | MkDocs configuration, GitHub Pages CI, navigation tree |
| [07-future-expansion-plan.md](07-future-expansion-plan.md) | Reserved sections for language guides, HPC, AI-assisted development, etc. |

## Key Decisions (from Spec)

- Protected `main` branch; all changes via Pull Requests.
- Squash Merge only; delete feature branches after merge.
- Branch naming: `feature/`, `bugfix/`, `docs/`, `refactor/`, `experiment/`, `chore/`
- Commit messages: imperative tense, descriptive.
- Documentation built with MkDocs; deployed to GitHub Pages.
- Every published figure → tagged commit. Every paper → Git tag.
