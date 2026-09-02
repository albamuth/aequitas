"""Negative controls for disparity_ceiling_sim.py.

Question asked (denominator, c18425 / the 13-13 truncation law):
  "arithmetic over a log never catches truncation of that log; what catches it
   is a second record the truncation could not reach."

The audit suite failed that test. This asks whether the CEILING result has the
same defect: does 24/F = 2.40x survive because it was measured, or because the
population generator cannot express a violation?

Four cuts, all against the same reported statistic that the published run
prints as "Aequitas consumption ceiling: 2.40x":
    top_vs_floor = max(rho * c) / (rho * F)

  A  truncate: drop the top 10% of credit rates before reporting
  B  truncate hard: drop the top 50%
  C  splice a cheater: one account claiming 40 h/day of credited work
  D  splice phantoms: 20,000 extra accounts at the floor

Run:  python 06-simulation/disparity-ceiling/ceiling_negative_controls.py
"""

import sys, os

# disparity_ceiling_sim.py is the sibling this file is a control on, so import it
# from this directory whatever the working directory is. It guards its own main()
# behind __name__, so importing it runs nothing.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import disparity_ceiling_sim as S

F, RHO = S.F, 1.5


def ceiling(c, rho=RHO):
    d = rho * c
    return float(np.max(d) / (rho * F))


def main():
    base = S.draw_population()
    rows = []
    rows.append(("baseline (published run)", len(base), ceiling(base)))

    for frac, label in ((0.10, "A truncate top 10%"), (0.50, "B truncate top 50%")):
        keep = np.sort(base)[: int(len(base) * (1 - frac))]
        rows.append((label, len(keep), ceiling(keep)))

    cheat = np.append(base, 40.0)
    rows.append(("C splice cheater @ 40 h/day", len(cheat), ceiling(cheat)))

    phantom = np.append(base, np.full(20_000, F))
    rows.append(("D splice 20k phantoms @ floor", len(phantom), ceiling(phantom)))

    print("=" * 68)
    print("CEILING NEGATIVE CONTROLS   F=%.1f  rho=%.2f  claimed ceiling=%.2fx"
          % (F, RHO, S.CEILING))
    print("=" * 68)
    print("%-32s %10s %12s %8s" % ("case", "n", "reported", "fires?"))
    for label, n, v in rows:
        fires = "-" if abs(v - rows[0][2]) < 1e-9 else "FIRES"
        print("%-32s %10d %11.2fx %8s" % (label, n, v, fires))
    print("-" * 68)
    print("n: 5 constructed cases / 1 generator / 2 expressible failure modes")
    print("null: baseline and D are the passing controls")
    print("what it cannot reach: a population the generator was never given")


if __name__ == "__main__":
    main()
