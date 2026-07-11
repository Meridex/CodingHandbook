# phys_toolkit — Example Repository

> **This is a practice sandbox for Git workflow exercises.**
> Make mistakes here — that is the point.

`phys_toolkit` is a minimal Python package built around a simple quartic scalar
field potential $V(\phi) = -\mu^2\phi^2 + \lambda\phi^4$. The physics is
intentionally simple so you can focus on learning Git, not on understanding the
code.

## Status

![Tests](https://github.com/ORG/phys-toolkit-example/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/github/license/ORG/phys-toolkit-example)

## Requirements

- Python >= 3.10
- numpy >= 1.24
- pytest >= 7.0 (for running tests)
- matplotlib >= 3.5 (optional, for plots)

## Installation

```bash
git clone git@github.com:ORG/phys-toolkit-example.git
cd phys-toolkit-example
pip install -e ".[test]"
```

## Quick Start

```python
from phys_toolkit import QuarticPotential, find_minimum

pot = QuarticPotential(mu=1.0, lambda_=0.25)
print(pot.evaluate(0.0))        # 0.0
print(pot.minimum())            # ~1.4142
print(find_minimum(pot))        # ~1.4142 (numerical)
```

Or run the example script:

```bash
python examples/basic_usage.py
```

## Repository Structure

```
phys-toolkit-example/
├── src/phys_toolkit/   # Package source code
│   ├── potential.py    # QuarticPotential class
│   ├── solver.py       # Bisection root-finder
│   └── utils.py        # Unit conversion helpers
├── tests/              # pytest test suite
├── examples/           # Runnable example scripts
├── scripts/            # Parameter scan utilities
├── docs/               # Project documentation
└── .github/            # PR template, issue templates, CI workflow
```

## Exercises

This repository supports all exercises in the
[Group Coding Handbook](https://ORG.github.io/GroupCodingHandbook/),
Student Guide Chapter 18. The seeded issues below give you real tasks to work on:

| Issue | Title | Type |
|-------|-------|------|
| #1 | Fix sign error in `barrier_height()` | bugfix |
| #2 | Add `second_derivative()` method | feature |
| #3 | Improve docstrings in `utils.py` | docs |
| #4 | Add test for zero-barrier edge case | feature |
| #5 | Rename `lambda_` to `lam` (PEP 8) | refactor |

## License

[MIT](LICENSE)

## Contact

NNU-PP Research Group
