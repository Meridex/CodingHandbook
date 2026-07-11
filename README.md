# Meridex Research Software Handbook

> Official software engineering handbook for the Meridex research group.

This handbook defines **how research software is developed, reviewed, and maintained in the group**.
It is the authoritative onboarding document for all students and developers — not a generic Git tutorial.

---

## Quick Links

| Document | Purpose |
|----------|---------|
| [Student Guide](docs/student/01-introduction.md) | Start here if you are a new student |
| [Maintainer Guide](docs/maintainer/01-repo-creation.md) | Repository administration and policy |
| [Templates](docs/templates/) | PR template, issue templates, checklists |
| [Appendices](docs/appendices/) | Glossary, group policies, research software principles |

---

## Repository Layout

```text
CodeHandbook/
├── README.md                    ← This file
├── mkdocs.yml                   ← MkDocs site configuration
├── docs/
│   ├── index.md                 ← Handbook landing page
│   ├── student/                 ← Student Guide (18 chapters)
│   ├── maintainer/              ← Maintainer Guide (19 chapters)
│   ├── appendices/              ← Glossary, policies, principles
│   ├── templates/               ← PR, issue, README templates
│   └── assets/                  ← Diagrams and images
├── example-repository/          ← Practice repository for exercises
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
└── LICENSE
```

---

## Canonical Workflow (Summary)

All work in this group follows a single protected workflow:

```
main
  │
  ├── git pull origin main          (sync)
  ├── git checkout -b feature/task  (branch)
  ├── [develop → commit → repeat]   (work)
  ├── git push origin feature/task  (push)
  ├── Pull Request on GitHub        (review)
  └── Squash Merge → main           (merge)
```

**No direct commits to `main`. All changes go through Pull Requests.**

---

## Building the Site Locally

```bash
pip install mkdocs-material
mkdocs serve
```

Open `http://127.0.0.1:8000` in your browser.

---

## Contributing

This handbook is itself maintained using the same workflow it describes.
To suggest a correction or addition, open a Pull Request following the standard process.

---

## License

[MIT License](LICENSE)

## Contact

Meridex Research Group
