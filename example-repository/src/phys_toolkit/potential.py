"""Quartic scalar potential V(phi) = -mu^2 * phi^2 + lambda * phi^4.

This module provides a simple scalar field potential used as the physics
content for Git workflow practice exercises.
"""


class QuarticPotential:
    """A quartic scalar field potential.

    The potential is defined as::

        V(phi) = -mu^2 * phi^2 + lambda_ * phi^4

    For mu^2 > 0 and lambda_ > 0, this has a 'Mexican hat' shape with
    two degenerate minima at phi = +/- mu / sqrt(2 * lambda_).

    Parameters
    ----------
    mu : float
        Mass parameter (mu > 0).
    lambda_ : float
        Quartic coupling constant (lambda_ > 0).
    """

    def __init__(self, mu: float, lambda_: float) -> None:
        if mu <= 0:
            raise ValueError(f"mu must be positive, got {mu}")
        if lambda_ <= 0:
            raise ValueError(f"lambda_ must be positive, got {lambda_}")
        self.mu = mu
        self.lambda_ = lambda_

    def evaluate(self, phi: float) -> float:
        """Evaluate the potential at field value phi.

        Parameters
        ----------
        phi : float
            Field value.

        Returns
        -------
        float
            V(phi).
        """
        return -(self.mu ** 2) * phi ** 2 + self.lambda_ * phi ** 4

    def minimum(self) -> float:
        """Return the positive non-trivial minimum of the potential.

        Returns
        -------
        float
            phi_min > 0 where dV/dphi = 0 and d^2V/dphi^2 > 0.
        """
        import math
        return self.mu / math.sqrt(2.0 * self.lambda_)

    def barrier_height(self) -> float:
        """Return the height of the potential barrier at phi = 0.

        The barrier height is V(0) - V(phi_min).

        Returns
        -------
        float
            Delta V >= 0.

        .. note::
            Known issue (Issue #1): this method currently returns a negative
            value due to a sign error. See the seeded bug below.
        """
        phi_min = self.minimum()
        # BUG (Issue #1): sign is wrong — should be -self.evaluate(phi_min)
        return self.evaluate(phi_min)
