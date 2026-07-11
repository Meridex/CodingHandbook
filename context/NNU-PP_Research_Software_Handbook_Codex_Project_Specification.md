# NNU-PP Research Software Handbook --- Codex Project Specification

> This document is the complete project specification for building a
> group software handbook.

## 1. Vision

Build a long-term, professional handbook defining **how research
software is developed in the group**. It is **not** a Git tutorial;
Git is only one tool within a broader engineering workflow emphasizing
reproducibility, collaboration, documentation, testing, code review, and
maintainability.

The handbook should become the official onboarding material for all
students and developers.

## 2. Objectives

-   Teach new students with zero Git experience.
-   Standardize development across all projects.
-   Produce documentation suitable for long-term maintenance.
-   Use one consistent workflow rather than many alternatives.

## 3. Audience

### Students

Assume no prior knowledge.

Teach: - Git basics only as required. - Daily workflow. - Pull
Requests. - Responding to reviews. - Recovering from common mistakes.

### Maintainers

Teach: - Repository administration. - Permissions. - Branch
protection. - Releases. - Review policy. - Repository organization. -
Long-term maintenance.

## 4. Repository Layout

``` text
CodeHandbook/
├── README.md
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── student/
│   ├── maintainer/
│   ├── appendices/
│   ├── templates/
│   └── assets/
├── example-repository/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
└── LICENSE
```

Generate Markdown first; structure should also support MkDocs and GitHub
Pages.

## 5. Group Workflow (Canonical)

Protected `main` branch.

Every change follows:

``` text
main
  │
  ├── git pull
  │
  ├── create feature branch
  │
  ├── develop
  │
  ├── commit
  │
  ├── push
  │
  ├── Pull Request
  │
  ├── review
  │
  └── squash merge → main
```

No direct commits to `main`.

## 6. Repository Policies

-   Private repository.
-   3--10 developers.
-   Students are collaborators.
-   Students never push directly to main.
-   All work through Pull Requests.
-   Branch protection enabled.
-   Squash Merge is default.
-   Delete feature branches after merge.

## 7. Branch Naming

-   feature/
-   bugfix/
-   docs/
-   refactor/
-   experiment/
-   chore/

Examples:

-   feature/gw-spectrum
-   feature/leptogenesis-solver
-   bugfix/interpolation
-   docs/install
-   refactor/io
-   experiment/new-scan

## 8. Commit Convention

Use imperative tense.

Good:

-   Add thermal correction
-   Fix interpolation bug
-   Improve documentation
-   Refactor solver interface

Avoid:

-   update
-   fix
-   final
-   temp
-   test

## 9. Pull Request Policy

Every PR contains:

-   Motivation
-   Summary
-   Files affected
-   Testing performed
-   Screenshots if UI exists
-   Related issue

Small PRs preferred.

One feature per PR.

## 10. Review Checklist

Reviewer verifies:

-   Scientific correctness.
-   Builds successfully.
-   Tests pass.
-   Documentation updated.
-   Style consistent.
-   No dead code.
-   No debug output.
-   No generated files.

## 11. Documentation Philosophy

Explain every concept using:

1.  Why
2.  What
3.  How
4.  Common mistakes
5.  Best practice

Never assume prior knowledge.

## 12. Student Guide Outline

1.  Introduction
2.  Git vs GitHub
3.  Development workflow
4.  Initial setup
5.  SSH
6.  Clone repository
7.  Daily workflow
8.  Branches
9.  Commits
10. Push
11. Pull Requests
12. Reviews
13. Merge conflicts
14. Updating branches
15. Common mistakes
16. FAQ
17. Cheat sheet
18. Exercises

Every chapter includes:

-   Summary
-   Checklist
-   Common mistakes
-   Exercises

## 13. Maintainer Guide Outline

1.  Repository creation
2.  Repository settings
3.  Branch protection
4.  Collaborator management
5.  Labels
6.  Milestones
7.  Project board
8.  Review workflow
9.  Merge strategy
10. Releases
11. Tags
12. Documentation policy
13. Testing policy
14. CI preparation
15. Backup strategy
16. Archiving
17. Public transition
18. Student onboarding
19. Student offboarding

## 14. Templates

Generate:

-   README template
-   Issue template
-   Bug report
-   Feature request
-   Pull Request template
-   Review checklist
-   Release checklist
-   Student onboarding checklist
-   Repository checklist

## 15. Example Repository

Include:

``` text
example-repository/
├── README.md
├── src/
├── tests/
├── docs/
├── examples/
├── scripts/
└── .github/
```

Used only for practice.

## 16. Visual Requirements

Use Mermaid extensively:

-   workflow
-   branch graph
-   lifecycle
-   review process
-   release timeline
-   repository layout
-   decision trees

## 17. Writing Style

Professional. Patient. Clear. Consistent.

Avoid unnecessary alternatives. Recommend one workflow.

## 18. Research Software Principles

-   Correctness before optimization.
-   Readability before cleverness.
-   Reproducibility before speed.
-   Documentation is part of research.
-   Every published figure should correspond to a tagged commit.
-   Every published paper should correspond to a Git tag.
-   Large datasets are not committed to Git.
-   Tests accompany important scientific algorithms whenever practical.

## 19. Future Expansion

Reserve sections for:

-   Python style guide
-   C++ style guide
-   Documentation guide
-   Testing guide
-   AI-assisted development
-   Reproducible research
-   Release & publication workflow
-   HPC development
-   Coding standards
-   Licensing
-   Citation policy

## 20. Deliverables

Produce a complete handbook, not notes.

Every Markdown page should be publication quality.

Every workflow should include diagrams.

Every command should include explanations.

The result should be suitable as the official software engineering
handbook for a theoretical physics research laboratory.
