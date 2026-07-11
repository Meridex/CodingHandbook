"""Parameter scan over mu for the quartic potential.

Prints a table of phi_min and V(phi_min) for a range of mu values.
"""

import math
from phys_toolkit import QuarticPotential, find_minimum

LAMBDA = 0.25
MU_VALUES = [round(0.25 * i, 2) for i in range(1, 13)]  # 0.25, 0.50, ..., 3.00

print(f"{'mu':>6}  {'phi_min (numeric)':>18}  {'phi_min (analytic)':>18}  {'V(phi_min)':>12}")
print("-" * 62)

for mu in MU_VALUES:
    pot = QuarticPotential(mu=mu, lambda_=LAMBDA)
    phi_num = find_minimum(pot)
    phi_ana = mu / math.sqrt(2.0 * LAMBDA)
    v_min = pot.evaluate(phi_num)
    print(f"{mu:>6.2f}  {phi_num:>18.8f}  {phi_ana:>18.8f}  {v_min:>12.6f}")
