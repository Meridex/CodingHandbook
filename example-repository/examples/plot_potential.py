"""Plot the quartic potential for several mu values.

Requires: matplotlib
    pip install matplotlib
"""

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise SystemExit("matplotlib is required: pip install matplotlib")

from phys_toolkit import QuarticPotential

phi = np.linspace(-2.5, 2.5, 500)

fig, ax = plt.subplots(figsize=(7, 4))

for mu in [0.5, 1.0, 1.5]:
    pot = QuarticPotential(mu=mu, lambda_=0.25)
    V = np.array([pot.evaluate(p) for p in phi])
    ax.plot(phi, V, label=rf"$\mu={mu}$, $\lambda=0.25$")

ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
ax.set_xlabel(r"$\phi$")
ax.set_ylabel(r"$V(\phi)$")
ax.set_title(r"Quartic potential $V(\phi) = -\mu^2\phi^2 + \lambda\phi^4$")
ax.legend()
ax.set_ylim(-3, 3)
plt.tight_layout()
plt.savefig("potential.png", dpi=150)
print("Saved potential.png")
