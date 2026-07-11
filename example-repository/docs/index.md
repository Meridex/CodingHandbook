# phys_toolkit — Example Project Documentation

This is the mini-documentation for the `phys_toolkit` example repository.
It exists so students can see what a `docs/` directory looks like in a
real project.

## Modules

### `potential.py`

Implements `QuarticPotential`: the scalar field potential

$$V(\phi) = -\mu^2 \phi^2 + \lambda \phi^4$$

| Method | Description |
|--------|-------------|
| `evaluate(phi)` | Returns $V(\phi)$ |
| `minimum()` | Returns the positive minimum $\phi_\text{min} = \mu / \sqrt{2\lambda}$ |
| `barrier_height()` | Returns $V(0) - V(\phi_\text{min})$ |

### `solver.py`

Provides `bisect(f, a, b)` — a general bisection root-finder — and
`find_minimum(potential)` which uses it to locate the non-trivial minimum
of a `QuarticPotential` numerically.

### `utils.py`

Unit conversion helpers: GeV ↔ natural units, MeV ↔ GeV.

## Running the Tests

```bash
pytest --tb=short
```

## Known Issues

- **Issue #1**: `barrier_height()` returns a negative value (sign error).
- **Issue #3**: Docstrings in `utils.py` are incomplete.
