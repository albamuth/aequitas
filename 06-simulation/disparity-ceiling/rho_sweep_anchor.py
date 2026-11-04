"""
rho_sweep_anchor.py -- the sr-20261104 re-run: rho_sweep.py's clearing rate with
demand tied to the median-lifestyle anchor.

WHAT CHANGED AGAINST rho_sweep.py (two lines, per the request):
  1. kappa = 1,380/365 = 3.7808 debit-h/day per median-lifestyle unit (the Tracks
     1-4 anchor, Foundations 3.5) -- NOT the median credit rate (~13.8 h/day).
     rho_sweep.py defined the anchor on its line 51 and never read it; its line 73
     set kappa to median credit. The stable-band re-measure of 2026-10-27
     (stable-band/RESULTS_KAPPA.md) ruled that admitted demand must be priced at
     the anchor; this run applies the same ruling to this instrument.
  2. The rho grid runs 0.01 to 4.00 in steps of 0.01. rho_sweep.py's grid started
     at 0.2, which would censor the deep-shock cells.

THE SWEEP (per request sr-20261104-re-run-rho-sweep-py-s-clearing-rate-with-dem):
  Budget shock 0% (baseline) and -5% to -50% in steps of 5%, at F = 2, 10, 14.
  R_max = CAP * (sum of wants) * (1 + shock), CAP = 0.85 (Q1: materials/energy
  bind). P = 0 everywhere. Report rho* per cell, flag censored cells, and give
  the first shock step where rho* falls below the affordability edge E/(365*F)
  for E = 516, 655 (narrow basket) and 826, 965 (broad basket), Foundations 5.5.3.

MODEL (identical to rho_sweep.py in every other respect):
  c_i in [F, 24] from disparity_ceiling_sim.draw_population (set_floor per F).
  wants: lognormal(0, 0.45), median-normalised, mild link (c/median c)^0.25,
  re-normalised. Demand admitted at rho: sum_i min(want_i, rho * c_i / kappa).
  Clearing rho*: the grid rho minimising |demand - R_max|.
  Demand does not depend on the shock, so one demand curve per F serves all cells.

EXACT RESCALING CHECK. R_max never reads kappa, so rho* is proportional to kappa:
  rho*_anchor = rho*_old x (3.7808 / 13.797) = rho*_old / 3.65. Self-test 3 checks
  the F = 10 baseline against 1.20 / 3.65 = 0.329 and against the stable-band's
  independently measured edge 0.330 (Foundations 5.5.3).

Run:  python rho_sweep_anchor.py
"""
from __future__ import annotations

import numpy as np

import disparity_ceiling_sim as dcs

SEED = 7
N = 200_000
CAP = 0.85
WANTS_SIGMA = 0.45
KAPPA = 1380.0 / 365.0                 # 3.7808 debit-h/day per lifestyle unit
FLOORS = (2.0, 10.0, 14.0)
SHOCKS = [0.00] + [round(-0.05 * k, 2) for k in range(1, 11)]   # 0%, -5% ... -50%
RHOS = np.round(np.arange(0.01, 4.00 + 1e-9, 0.01), 2)  # grid to 0.01, per request
BASKETS = (516.0, 655.0, 826.0, 965.0)                  # E, h/yr (5.5.3)


def build_population(floor, n=N, seed=SEED):
    """rho_sweep.py's population at a chosen floor, same seed discipline."""
    dcs.set_floor(floor)
    rng = np.random.default_rng(seed)
    c = dcs.draw_population(n, rng)                   # credit h/day in [F, 24]
    wants = rng.lognormal(mean=0.0, sigma=WANTS_SIGMA, size=n)
    wants /= np.median(wants)
    wants *= (c / np.median(c)) ** 0.25
    wants /= np.median(wants)
    return c, wants


def demand_curve(c, wants, rhos=RHOS):
    """Admitted demand at each rho. Vectorised over the grid."""
    # (n_rho, N) would be 320 MB; loop the grid instead, each step vectorised.
    return np.array([np.minimum(wants, r * c / KAPPA).sum() for r in rhos])


def clearing(dem, R_max, rhos=RHOS):
    """Grid rho* and a censor flag ('' | 'low-edge' | 'high-edge' | 'never-binds')."""
    if dem[-1] < R_max:
        return None, "never-binds"                    # gate never rations
    i = int(np.argmin(np.abs(dem - R_max)))
    flag = "low-edge" if i == 0 else ("high-edge" if i == len(rhos) - 1 else "")
    return float(rhos[i]), flag


def run():
    results = {}                                      # (F, shock) -> (rho*, flag)
    for floor in FLOORS:
        c, wants = build_population(floor)
        dem = demand_curve(c, wants)
        unconstrained = wants.sum()
        for shock in SHOCKS:
            R_max = CAP * unconstrained * (1.0 + shock)
            results[(floor, shock)] = clearing(dem, R_max)
    return results


def first_step_below(results, floor):
    """Per basket E: the first shock step where rho* < E/(365*F). None if never."""
    out = {}
    for E in BASKETS:
        edge = E / (365.0 * floor)
        hit = None
        for shock in SHOCKS:
            rstar, _ = results[(floor, shock)]
            if rstar is not None and rstar < edge:
                hit = shock
                break
        out[E] = (edge, hit)
    return out


def report(results):
    W = 86
    print("=" * W)
    print("rho-SWEEP, ANCHOR-TIED -- sr-20261104 re-run")
    print(f"  kappa = 1380/365 = {KAPPA:.4f} debit-h/day per median-lifestyle unit")
    print(f"  CAP = {CAP}, wants sigma = {WANTS_SIGMA}, N = {N}, seed = {SEED}")
    print(f"  rho grid: {RHOS[0]:.2f} to {RHOS[-1]:.2f}, step 0.01.  P = 0.")
    print("=" * W)
    header = "  {:<10}".format("shock") + "".join(f"{f'F={int(f)}':>10}" for f in FLOORS)
    print(header)
    print("-" * W)
    for shock in SHOCKS:
        row = f"  {shock * 100:>7.0f}%  "
        for floor in FLOORS:
            rstar, flag = results[(floor, shock)]
            cell = "never" if rstar is None else f"{rstar:.2f}"
            if flag and rstar is not None:
                cell += "!"
            row += f"{cell:>10}"
        print(row)
    print("-" * W)
    print("  '!' marks a censored cell (rho* at a grid edge). 'never' = never binds.")
    print()
    for floor in FLOORS:
        print(f"  F = {int(floor)}: first shock step with rho* below E/(365*F)")
        for E, (edge, hit) in first_step_below(results, floor).items():
            where = "never (within -50%)" if hit is None else f"{hit * 100:.0f}%"
            print(f"    E = {E:>5.0f} h/yr  edge = {edge:.3f}  first step below: {where}")
    print("=" * W)


# --- self-tests ----------------------------------------------------------------
def self_tests(results):
    ok = 0
    # 1. No censored or never-binding cell anywhere in the sweep.
    flags = [flag for (rstar, flag) in results.values() if flag]
    assert not flags, f"censored/never cells: {flags}"
    ok += 1
    print("[ok] 1. no cell is censored and every cell binds")
    # 2. rho* falls monotonically as the shock deepens, at every floor.
    for floor in FLOORS:
        seq = [results[(floor, s)][0] for s in SHOCKS]
        assert all(a >= b for a, b in zip(seq, seq[1:])), f"not monotone at F={floor}"
    ok += 1
    print("[ok] 2. deeper shock -> lower rho*, at every floor")
    # 3. The F=10 baseline matches the exact rescale of the old run (1.20/3.65 =
    #    0.329) and the stable band's measured edge 0.330, within the grid step.
    base = results[(10.0, 0.0)][0]
    assert abs(base - 0.33) <= 0.02, f"F=10 baseline {base} vs expected ~0.33"
    ok += 1
    print(f"[ok] 3. F=10 baseline rho* = {base:.2f} (rescale 0.329; stable band 0.330)")
    # 4. A higher floor lowers rho* at baseline (more floor credit per person
    #    admits the same demand at a lower tolerance).
    b2, b10, b14 = (results[(f, 0.0)][0] for f in FLOORS)
    assert b2 > b10 > b14, f"floor ordering broken: {b2}, {b10}, {b14}"
    ok += 1
    print(f"[ok] 4. baseline rho* falls as F rises: {b2:.2f} > {b10:.2f} > {b14:.2f}")
    # 5. The -30% cell at F=10 sits below the broad-basket lower edge (0.226),
    #    the agent's headline arithmetic, now measured rather than rescaled.
    r30 = results[(10.0, -0.30)][0]
    assert r30 < 826.0 / 3650.0, f"-30% cell {r30} not below broad lower edge"
    ok += 1
    print(f"[ok] 5. F=10 at -30%: rho* = {r30:.2f}, below the broad-basket edge 0.226")
    print(f"[ok] {ok}/5 self-tests green")


if __name__ == "__main__":
    res = run()
    report(res)
    self_tests(res)
