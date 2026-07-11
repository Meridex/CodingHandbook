"""Bisection root-finder for locating the non-trivial minimum of a potential."""


def bisect(f, a: float, b: float, tol: float = 1e-10, max_iter: int = 200) -> float:
    """Find a root of f in the interval [a, b] using bisection.

    Parameters
    ----------
    f : callable
        A continuous function. Must satisfy f(a) * f(b) < 0.
    a, b : float
        Bracket endpoints.
    tol : float, optional
        Convergence tolerance on |b - a|.
    max_iter : int, optional
        Maximum number of iterations.

    Returns
    -------
    float
        Approximate root x such that |f(x)| < tol (approximately).

    Raises
    ------
    ValueError
        If f(a) and f(b) have the same sign.
    """
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(
            f"f(a) and f(b) must have opposite signs; got f({a})={fa}, f({b})={fb}"
        )

    for _ in range(max_iter):
        mid = 0.5 * (a + b)
        fmid = f(mid)
        if abs(b - a) < tol or fmid == 0.0:
            return mid
        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid

    return 0.5 * (a + b)


def find_minimum(potential, phi_max: float = None) -> float:
    """Find the positive non-trivial minimum of a QuarticPotential via bisection.

    Solves dV/dphi = 0 on (0, phi_max].

    Parameters
    ----------
    potential : QuarticPotential
        The potential object.
    phi_max : float, optional
        Upper search bound. Defaults to 10 * mu.

    Returns
    -------
    float
        Approximate location of the positive minimum.
    """
    if phi_max is None:
        phi_max = 10.0 * potential.mu

    def dv(phi):
        # dV/dphi = -2 * mu^2 * phi + 4 * lambda_ * phi^3
        return -2.0 * potential.mu ** 2 * phi + 4.0 * potential.lambda_ * phi ** 3

    # dv(0) = 0, so we search on a small positive lower bound
    eps = 1e-8
    return bisect(dv, eps, phi_max)
