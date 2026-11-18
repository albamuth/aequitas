#!/usr/bin/env python3
"""
scale_the_anchor.py -- sr-20261105: scale the anchor kappa by 0.5 and 2 in
rho_sweep_anchor.py and stable_band_kappa.py and require rho* to scale by the
same factor within one grid step. No literal in any assertion.

Run:  python scale_the_anchor.py          (seed 7, N from each script)
"""
from __future__ import annotations

import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "disparity-ceiling"))
sys.path.insert(0, os.path.join(ROOT, "stable-band"))

import rho_sweep_anchor as ra                      # noqa: E402
import stable_band as sb                           # noqa: E402
import stable_band_cumulative as sc                # noqa: E402
import stable_band_kappa as sk                     # noqa: E402

SCALES = (0.5, 1.0, 2.0)
STEP = float(ra.RHOS[1] - ra.RHOS[0])


def part_a():
    """rho_sweep_anchor: every one of 3 floors x 11 shocks, at three scales."""
    out = {}                                       # (scale, F, shock) -> rho*
    flags = []
    for F in ra.FLOORS:
        c, wants = ra.build_population(F)
        unc = wants.sum()
        for s in SCALES:
            dem = ra.demand_curve(c, wants, kappa=ra.KAPPA * s)
            # exact identity: demand at (s*rho, s*kappa) equals demand at (rho, kappa)
            if s != 1.0:
                base = ra.demand_curve(c, wants, kappa=ra.KAPPA)
                probe = np.array([0.20, 0.33, 0.60])
                d_s = np.array([np.minimum(wants, (s * r) * c / (ra.KAPPA * s)).sum() for r in probe])
                d_1 = np.array([np.minimum(wants, r * c / ra.KAPPA).sum() for r in probe])
                assert np.allclose(d_s, d_1, rtol=1e-12), "demand not homogeneous"
            for shock in ra.SHOCKS:
                r, flag = ra.clearing(dem, ra.CAP * unc * (1.0 + shock))
                out[(s, F, shock)] = r
                if flag or r is None:
                    flags.append((s, F, shock, flag))
    return out, flags


def part_b():
    """stable_band_kappa: one-day and cumulative edges at three scales."""
    w, x, kappa_old, R = sk.setup()
    ag = sc.draw_ages(len(w), sc.AGE_SEEDS[0])
    rows = {}
    for F in sk.FLOORS:
        for s in SCALES:
            k = sk.KAPPA_ANCHOR * s
            od, fo = sc.edge_one_day(w, x, F, k, R)
            cu_both, f1 = sc.edge_cumulative(w, x, ag, F, k, R, past_rate=sc.PAST_RATE * s)
            cu_kappa_only, f2 = sc.edge_cumulative(w, x, ag, F, k, R)   # past debit left at 1,380
            rows[(F, s)] = (od, fo, cu_both, f1, cu_kappa_only, f2)
    return rows


def main():
    print("== A. rho_sweep_anchor.py, all 33 cells ==")
    a, flags = part_a()
    print(f"censored / never-binding cells across 99 runs: {len(flags)} {flags[:5]}")
    n_strict = n_loose = 0
    worst = 0.0
    for (s, F, shock), r in sorted(a.items()):
        if s == 1.0 or r is None:
            continue
        want = a[(1.0, F, shock)] * s
        dev = abs(r - want)
        worst = max(worst, dev)
        n_strict += dev <= STEP + 1e-9
        n_loose += dev <= STEP + 0.5 * STEP * s + 1e-9
    n_cells = sum(1 for k in a if k[0] != 1.0)
    print(f"cells at s=0.5 and s=2: {n_cells}; within one grid step ({STEP}): {n_strict}; "
          f"within one step + half-step x s: {n_loose}; worst deviation {worst:.3f}")
    print("\nF=10 published-cell prediction vs measured (rho*):")
    for shock in (0.0, -0.30):
        b = a[(1.0, 10.0, shock)]
        print(f"  shock {shock*100:>4.0f}%: base {b:.2f} | x0.5 pred {b*0.5:.3f} got {a[(0.5,10.0,shock)]:.2f}"
              f" | x2 pred {b*2:.3f} got {a[(2.0,10.0,shock)]:.2f}")
    print("\nrho* by floor, baseline, three scales:")
    for F in ra.FLOORS:
        print(f"  F={F:>4g}: " + "  ".join(f"x{s}: {a[(s, F, 0.0)]:.2f}" for s in SCALES))

    print("\n== B. stable_band_kappa.py (N=60,000, age seed 11, M=100) ==")
    rows = part_b()
    print(f"{'F':>4} {'x':>4} | {'one-day':>8} {'/x':>7} | {'cum (past scaled)':>18} {'/x':>7} | "
          f"{'cum (kappa only)':>17} {'/x':>7}")
    for (F, s), (od, fo, c1, f1, c2, f2) in sorted(rows.items()):
        print(f"{F:>4g} {s:>4g} | {od:>8.3f} {od/s:>7.3f} | {c1:>18.3f} {c1/s:>7.3f} | {c2:>17.3f} {c2/s:>7.3f}"
              f"  flags {fo!r} {f1!r} {f2!r}")
    print("\nmax relative deviation from exact scaling:")
    for name, idx in (("one-day", 0), ("cumulative, past debit scaled too", 2),
                      ("cumulative, kappa only", 4)):
        dev = max(abs(rows[(F, s)][idx] / (rows[(F, 1.0)][idx] * s) - 1.0)
                  for F in sk.FLOORS for s in (0.5, 2.0))
        print(f"  {name:<36} {dev:.4%}")


if __name__ == "__main__":
    main()
