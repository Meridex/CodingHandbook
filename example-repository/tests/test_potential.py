import math
import pytest
from phys_toolkit.potential import QuarticPotential


def test_evaluate_at_zero():
    """V(0) = 0 for any mu, lambda_."""
    p = QuarticPotential(mu=1.0, lambda_=0.25)
    assert p.evaluate(0.0) == 0.0


def test_evaluate_at_minimum():
    """V at the minimum is negative (Mexican hat shape)."""
    p = QuarticPotential(mu=1.0, lambda_=0.25)
    phi_min = p.minimum()
    assert p.evaluate(phi_min) < 0.0


def test_minimum_value():
    """phi_min = mu / sqrt(2 * lambda_)."""
    mu, lam = 2.0, 0.5
    p = QuarticPotential(mu=mu, lambda_=lam)
    expected = mu / math.sqrt(2.0 * lam)
    assert p.minimum() == pytest.approx(expected, rel=1e-10)


def test_minimum_is_symmetric():
    """The negative minimum has the same potential value."""
    p = QuarticPotential(mu=1.0, lambda_=0.25)
    phi_min = p.minimum()
    assert p.evaluate(phi_min) == pytest.approx(p.evaluate(-phi_min))


def test_barrier_height_positive():
    """barrier_height() should return a positive value (Issue #1: currently broken)."""
    p = QuarticPotential(mu=1.0, lambda_=0.25)
    # This test will FAIL until Issue #1 is fixed.
    assert p.barrier_height() > 0.0


def test_barrier_height_formula():
    """barrier_height = mu^4 / (4 * lambda_)."""
    mu, lam = 2.0, 0.5
    p = QuarticPotential(mu=mu, lambda_=lam)
    expected = mu ** 4 / (4.0 * lam)
    assert p.barrier_height() == pytest.approx(expected, rel=1e-10)


def test_invalid_mu_raises():
    with pytest.raises(ValueError):
        QuarticPotential(mu=-1.0, lambda_=0.25)


def test_invalid_lambda_raises():
    with pytest.raises(ValueError):
        QuarticPotential(mu=1.0, lambda_=0.0)
