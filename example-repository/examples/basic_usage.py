"""Basic usage example for phys_toolkit."""

from phys_toolkit import QuarticPotential, find_minimum

# Create a potential with mu=1.0, lambda_=0.25
pot = QuarticPotential(mu=1.0, lambda_=0.25)

# Evaluate V at a few points
for phi in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    print(f"V({phi:+.1f}) = {pot.evaluate(phi):+.4f}")

# Find the positive minimum numerically
phi_min = find_minimum(pot)
print(f"\nNumerical minimum:  phi_min = {phi_min:.6f}")
print(f"Analytic minimum:   phi_min = {pot.minimum():.6f}")
print(f"V(phi_min) = {pot.evaluate(phi_min):.6f}")
