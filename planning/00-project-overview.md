# 00 · Project Overview

## Vision Recap

Build a long-term, professional handbook that defines **how research software is
developed in the group**. This is the official onboarding document for all
students and developers — not a generic Git tutorial.

---

## Target Repository Layout (Final Deliverable)

```text
Lab-Handbook/
├── README.md                    ← Project entry point & quick-start
├── mkdocs.yml                   ← MkDocs site configuration
├── docs/
│   ├── index.md                 ← Handbook landing page
│   ├── student/                 ← Student Guide (18 chapters)
│   │   ├── 01-introduction.md
│   │   ├── 02-git-vs-github.md
│   │   ├── 03-workflow-overview.md
│   │   ├── 04-initial-setup.md
│   │   ├── 05-ssh.md
│   │   ├── 06-clone.md
│   │   ├── 07-daily-workflow.md
│   │   ├── 08-branches.md
│   │   ├── 09-commits.md
│   │   ├── 10-push.md
│   │   ├── 11-pull-requests.md
│   │   ├── 12-reviews.md
│   │   ├── 13-merge-conflicts.md
│   │   ├── 14-updating-branches.md
│   │   ├── 15-common-mistakes.md
│   │   ├── 16-faq.md
│   │   ├── 17-cheat-sheet.md
│   │   └── 18-exercises.md
│   ├── maintainer/              ← Maintainer Guide (19 chapters)
│   │   ├── 01-repo-creation.md
│   │   ├── 02-repo-settings.md
│   │   ├── 03-branch-protection.md
│   │   ├── 04-collaborators.md
│   │   ├── 05-labels.md
│   │   ├── 06-milestones.md
│   │   ├── 07-project-board.md
│   │   ├── 08-review-workflow.md
│   │   ├── 09-merge-strategy.md
│   │   ├── 10-releases.md
│   │   ├── 11-tags.md
│   │   ├── 12-documentation-policy.md
│   │   ├── 13-testing-policy.md
│   │   ├── 14-ci-preparation.md
│   │   ├── 15-backup-strategy.md
│   │   ├── 16-archiving.md
│   │   ├── 17-public-transition.md
│   │   ├── 18-student-onboarding.md
│   │   └── 19-student-offboarding.md
│   ├── appendices/
│   │   ├── research-software-principles.md
│   │   ├── group-policies.md
│   │   └── glossary.md
│   ├── templates/               ← Raw template files (not rendered as chapters)
│   │   ├── README-template.md
│   │   ├── PULL_REQUEST_TEMPLATE.md
│   │   ├── issue-bug-report.md
│   │   ├── issue-feature-request.md
│   │   ├── review-checklist.md
│   │   ├── release-checklist.md
│   │   ├── student-onboarding-checklist.md
│   │   └── repository-checklist.md
│   └── assets/
│       ├── diagrams/            ← Source Mermaid / SVG diagrams
│       └── images/
├── example-repository/          ← Practice repository for exercises
│   ├── README.md
│   ├── src/
│   ├── tests/
│   ├── docs/
│   ├── examples/
│   ├── scripts/
│   └── .github/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── deploy-docs.yml      ← MkDocs → GitHub Pages
└── LICENSE
```

---

## Writing Conventions for All Pages

Every handbook page follows this internal structure:

```
# Title

## Overview / Why
(Motivation — why does this matter for research software?)

## What
(Concept definition — what is it exactly?)

## How
(Step-by-step instructions with commands, screenshots, or diagrams)

## Common Mistakes
(Numbered list of pitfalls with correction advice)

## Best Practice Summary
(2–5 bullet points)

## Checklist
(Can be checked off before moving on)

## Exercises
(Concrete tasks to practise the concept)
```

---

## Audience Summary

| Audience | Prior Knowledge Assumed | Goal |
|----------|------------------------|------|
| Students (new) | Zero Git / GitHub knowledge | Complete daily development workflow |
| Students (experienced) | Basic Git | Team workflow, PR process |
| Maintainers | Developer experience | Repository administration & policy |

---

## Core Engineering Principles (appears in appendix)

1. Correctness before optimisation.
2. Readability before cleverness.
3. Reproducibility before speed.
4. Documentation is part of research.
5. Every published figure → tagged commit.
6. Every published paper → Git tag.
7. Large datasets are never committed to Git.
8. Tests accompany important scientific algorithms whenever practical.

---

## Deliverable Quality Standard

- Every Markdown page: publication quality.
- Every workflow: accompanied by a diagram.
- Every command: explained (not just listed).
- Suitable as the official software engineering handbook for a theoretical
  physics research group.
