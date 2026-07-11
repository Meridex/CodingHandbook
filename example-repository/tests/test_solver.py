import math
import pytest
from phys_toolkit.potential import QuarticPotential
from phys_toolkit.solver import bisect, find_minimum


def test_bisect_simple():
    """bisect finds the root of x^2 - 4 = 0 near x=2."""
    root = bisect(lambda x: x ** 2 - 4.0, 1.0, 3.0)
    assert root == pytest.approx(2.0, abs=1e-9)


def test_bisect_raises_on_same_sign():
    with pytest.raises(ValueError):
        bisect(lambda x: x ** 2 + 1.0, 0.0, 2.0)


def test_find_minimum_matches_analytic():
    """find_minimum agrees with the analytic formula phi_min = mu/sqrt(2*lambda_)."""
    mu, lam = 1.0, 0.25
    p = QuarticPotential(mu=mu, lambda_=lam)
    expected = mu / math.sqrt(2.0 * lam)
    result = find_minimum(p)
    assert result == pytest.approx(expected, rel=1e-6)


def test_find_minimum_various_params():
    """find_minimum works for several (mu, lambda_) pairs."""
    cases = [(1.0, 0.5), (2.0, 1.0), (0.5, 0.1)]
    for mu, lam in cases:
        p = QuarticPotential(mu=mu, lambda_=lam)
        expected = mu / math.sqrt(2.0 * lam)
        result = find_minimum(p)
        assert result == pytest.approx(expected, rel=1e-6), f"Failed for mu={mu}, lam={lam}"
