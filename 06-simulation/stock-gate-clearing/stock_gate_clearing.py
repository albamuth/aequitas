#!/usr/bin/env python3
"""
stock_gate_clearing.py -- clearing rate of the STOCK gate after a capacity shock.

Request sr-20261105-stock-gate-clearing-rate-after-a-capacity-sh.
Foundations 5.5.7's 0.19 comes from a FLOW gate (rho_sweep_anchor.py: admitted =
sum min(want, rho*c/kappa), no history). Foundations 3.0 / 5.5.6 specify a STOCK
gate D <= rho*(C+P) on a cumulative ledger. This builds the ledger, shocks one
year, and reads the stock rho*.

INPUTS (all from existing instruments, none re-derived)
  population, wants   disparity-ceiling/rho_sweep_anchor.build_population (N=200,000, seed 7)
  CAP 0.85, kappa 1380/365, sigma 0.45   rho_sweep_anchor constants
  ages                stable-band/stable_band_cumulative.draw_ages (US-like 5-band pyramid), seeds 11..15
  gate                stable-band/gate.py Kernel.room() = rho*(C+P) - D, P = 0

LEDGER AT THE START OF THE SHOCK YEAR (steady state at rho0)
  C = c*365*age            D = 365*age*min(wants*kappa, rho0*c)      (d_cut: see arm C)
THE YEAR
  accrue 365 days of credit at rate c (Kernel.accrue), then request wants*kappa*365
  and let the gate decide. Capacity (want-units) = CAP * sum(wants) * 0.70.
  rho_s = the rho at which the year's admitted demand = capacity (bisection).
ARMS
  A  gate on all demand
  B  gate only on demand above E = 826 h/yr: min(request, E) is ungated (charged to D
     first), the rest is gated. Sensitivity B2: the rest is gated against room BEFORE
     the ungated part is charged.
  C  D excludes ages under 14: past D = 365*max(age-14,0)*rate, and a person under 14
     at year start consumes ungated (still counted in demand). Sensitivity C2: past only.
YEAR 2   ledger carried on (D += year-1 admitted at rho_s), rho restored to rho0, capacity restored.

Run:  python stock_gate_clearing.py [--test]
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
for sub in ("stable-band", "disparity-ceiling"):
    sys.path.insert(0, os.path.join(SIM, sub))

import rho_sweep_anchor as rsa                                   # noqa: E402
from gate import Kernel, Dials                                   # noqa: E402
from stable_band_cumulative import draw_ages, AGE_BANDS          # noqa: E402

KAPPA = rsa.KAPPA
CAP = rsa.CAP
SHOCK = -0.30
E_BASKET = 826.0
D_CUT = 14.0
FLOORS = (2.0, 10.0, 14.0)
RHO0_OWN = {2.0: 1.017, 10.0: 0.330, 14.0: 0.253}      # Foundations 5.5.3 published flow edges
RHO0_FIXED = 0.33
AGE_SEEDS = (11, 12, 13, 14, 15)
PUBLISHED_FLOW_RHO = 0.19


# ---------------------------------------------------------------- ledger and year
def build_ledger(c, w, ages, rho0, d_cut=0.0):
    C = c * 365.0 * ages
    D = 365.0 * np.maximum(ages - d_cut, 0.0) * np.minimum(w * KAPPA, rho0 * c)
    return C, D


def run_year(c, w, ages_start, F, rho, D0, mode="all", order="ess_first"):
    """One year through the kernel. Returns (admitted hours per person, D after)."""
    n = len(c)
    k = Kernel(n, c, Dials(rho=float(rho), floor_h=float(F)))
    k.C = c * 365.0 * ages_start
    k.D = D0.copy()
    C_before = k.C.copy()
    k.accrue(days=365.0)
    req = w * KAPPA * 365.0
    if mode == "all":
        adm, _ = k.consume(req)
    elif mode == "above_E":
        ess = np.minimum(req, E_BASKET)
        disc = req - ess
        if order == "ess_first":
            k.consume(ess, essential=True)
            a2, _ = k.consume(disc)
        else:                                            # B2: gate before charging the ungated part
            a2 = np.clip(np.minimum(disc, k.room()), 0.0, None)
            k.D += ess + a2
        adm = ess + a2
    elif mode == "no_children":
        kid = ages_start < D_CUT
        k.consume(np.where(kid, req, 0.0), essential=True)
        a2, _ = k.consume(np.where(kid, 0.0, req))
        adm = np.where(kid, req, a2)
    else:
        raise ValueError(mode)
    assert np.allclose(k.D - D0, adm, atol=1e-6), "D must rise by exactly what was admitted"
    assert np.all(k.C >= C_before), "credit never falls"
    return adm, k.D


def units(adm):
    return float(adm.sum() / (KAPPA * 365.0))


def solve_rho(c, w, ages, F, D0, target_units, mode="all", order="ess_first", hi=4.0):
    """rho at which the year's admitted units = target. Returns (rho, flag)."""
    f = lambda r: units(run_year(c, w, ages, F, r, D0, mode, order)[0])   # noqa: E731
    if f(0.0) > target_units:
        return 0.0, "ungated-part-alone-exceeds-capacity"
    if f(hi) < target_units:
        return hi, "never-binds"
    lo, h = 0.0, hi
    while h - lo > 1e-5:
        m = 0.5 * (lo + h)
        if f(m) <= target_units:
            lo = m
        else:
            h = m
    return 0.5 * (lo + h), ""


def flow_rho(c, w, target_units, hi=4.0):
    f = lambda r: float(np.minimum(w, r * c / KAPPA).sum())              # noqa: E731
    lo, h = 0.0, hi
    while h - lo > 1e-6:
        m = 0.5 * (lo + h)
        if f(m) <= target_units:
            lo = m
        else:
            h = m
    return 0.5 * (lo + h)


# ---------------------------------------------------------------- summaries
BAND_EDGES = [(b[1], b[2]) for b in AGE_BANDS]


def by_band(adm, ages):
    return np.array([adm[(ages >= lo) & (ages < hi)].sum() for lo, hi in BAND_EDGES]) / (KAPPA * 365.0)


def by_decile(adm, C0):
    order = np.argsort(C0, kind="stable")
    out = np.empty(10)
    for d, idx in enumerate(np.array_split(order, 10)):
        out[d] = adm[idx].sum()
    return out / (KAPPA * 365.0)


def zero_shares(adm, ages):
    z = adm <= 1e-6
    return float(z.mean()), float(z[ages >= D_CUT].mean())


def one_cell(F, age_seed, rho0, n=rsa.N):
    c, w = rsa.build_population(F, n=n)
    ages = draw_ages(n, age_seed)
    cap_full = CAP * w.sum()
    cap_shock = cap_full * (1.0 + SHOCK)
    C0, D_A = build_ledger(c, w, ages, rho0)
    _, D_C = build_ledger(c, w, ages, rho0, d_cut=D_CUT)
    res = {"cap_full": cap_full, "cap_shock": cap_shock, "wants": float(w.sum())}
    res["flow_rho_shock"] = flow_rho(c, w, cap_shock)
    res["flow_rho_full"] = flow_rho(c, w, cap_full)
    base_adm, _ = run_year(c, w, ages, F, rho0, D_A)
    res["base_units"] = units(base_adm)
    res["base_band"] = by_band(base_adm, ages)
    res["base_dec"] = by_decile(base_adm, C0)
    arms = {"A": ("all", "ess_first", D_A), "B": ("above_E", "ess_first", D_A),
            "B2": ("above_E", "gate_first", D_A), "C": ("no_children", "ess_first", D_C),
            "C2": ("all", "ess_first", D_C)}
    for name, (mode, order, D0) in arms.items():
        rho_s, flag = solve_rho(c, w, ages, F, D0, cap_shock, mode, order)
        adm, D1 = run_year(c, w, ages, F, rho_s, D0, mode, order)
        z_all, z_adult = zero_shares(adm, ages)
        adm2, _ = run_year(c, w, ages + 1.0, F, rho0, D1, mode, order)
        # same arm's own baseline (rho0, no shock) for the band/decile comparison
        b_adm, _ = run_year(c, w, ages, F, rho0, D0, mode, order)
        res[name] = dict(rho_s=rho_s, flag=flag, units=units(adm), z_all=z_all, z_adult=z_adult,
                         band=by_band(adm, ages), dec=by_decile(adm, C0),
                         base_units=units(b_adm), base_band=by_band(b_adm, ages),
                         base_dec=by_decile(b_adm, C0), year2=units(adm2),
                         half=float((adm < 0.5 * w * KAPPA * 365.0).mean()))
    return res


# ---------------------------------------------------------------- self-tests (each can fail)
def _small(F=10.0, n=20000):
    c, w = rsa.build_population(F, n=n)
    return c, w, draw_ages(n, 11)


def test_age0_stock_equals_flow():
    """With an empty ledger the stock year must equal the flow admitted demand exactly."""
    c, w, _ = _small()
    z = np.zeros(len(c))
    for r in (0.15, 0.33, 0.9):
        a, _ = run_year(c, w, z, 10.0, r, z)
        flow = np.minimum(w, r * c / KAPPA).sum()
        assert abs(units(a) - flow) < 1e-6 * flow, (r, units(a), flow)
    print("[ok] 1. empty ledger: stock year == flow admitted demand at 3 rhos")


def test_monotone_in_rho():
    c, w, ages = _small()
    _, D = build_ledger(c, w, ages, 0.33)
    for mode in ("all", "above_E", "no_children"):
        u = [units(run_year(c, w, ages, 10.0, r, D, mode)[0]) for r in np.linspace(0, 2, 21)]
        assert all(b >= a - 1e-9 for a, b in zip(u, u[1:])), mode
    print("[ok] 2. admitted demand never falls as rho rises, in every arm")


def test_rationing_can_fail_and_pass():
    c, w, ages = _small()
    _, D = build_ledger(c, w, ages, 0.33)
    cap = CAP * w.sum() * (1 + SHOCK)
    lo = units(run_year(c, w, ages, 10.0, 0.01, D)[0])
    hi = units(run_year(c, w, ages, 10.0, 4.0, D)[0])
    assert lo < cap < hi, (lo, cap, hi)
    print(f"[ok] 3. the clearing test can pass (rho .01: {lo:,.0f}) and fail (rho 4: {hi:,.0f}) vs {cap:,.0f}")


def test_steady_state_reproduces_flow_capacity():
    """The ledger built at rho0=.33 must, unshocked, admit about CAP*sum(wants) (the flow edge)."""
    c, w, ages = _small(n=60000)
    _, D = build_ledger(c, w, ages, 0.33)
    u = units(run_year(c, w, ages, 10.0, 0.33, D)[0])
    cap = CAP * w.sum()
    assert abs(u / cap - 1.0) < 0.04, (u, cap)
    print(f"[ok] 4. steady-state year at rho0 admits {u / cap:.3f} x capacity (flow edge reproduced)")


def test_arms_collapse_to_A():
    c, w, ages = _small()
    _, D = build_ledger(c, w, ages, 0.33)
    a, _ = run_year(c, w, ages, 10.0, 0.2, D, "all")
    global E_BASKET, D_CUT
    e0, d0 = E_BASKET, D_CUT
    try:
        E_BASKET = 0.0
        b, _ = run_year(c, w, ages, 10.0, 0.2, D, "above_E")
        D_CUT = 0.0
        k, _ = run_year(c, w, ages, 10.0, 0.2, D, "no_children")
    finally:
        E_BASKET, D_CUT = e0, d0
    assert np.allclose(a, b) and np.allclose(a, k)
    print("[ok] 5. arm B with E=0 and arm C with cutoff 0 both equal arm A")


def test_gate_respected():
    c, w, ages = _small()
    _, D = build_ledger(c, w, ages, 0.33)
    adm, D1 = run_year(c, w, ages, 10.0, 0.2, D)
    room = np.maximum(0.2 * (c * 365.0 * (ages + 1.0)) - D, 0.0)
    assert np.all(adm <= room + 1e-6)
    print("[ok] 6. nobody is admitted more than rho*(C+P) - D")


def test_flow_published_level():
    """Declared outcome 1, a LEVEL: the flow rho* at -30%, F=10 must read 0.19 +/- 0.02."""
    c, w = rsa.build_population(10.0)
    r = flow_rho(c, w, CAP * w.sum() * 0.7)
    assert abs(r - PUBLISHED_FLOW_RHO) <= 0.02, r
    print(f"[ok] 7. flow rho* at -30%, F=10 = {r:.3f} (published 0.19 +/- 0.02)")


def run_tests():
    for fn in (test_age0_stock_equals_flow, test_monotone_in_rho, test_rationing_can_fail_and_pass,
               test_steady_state_reproduces_flow_capacity, test_arms_collapse_to_A,
               test_gate_respected, test_flow_published_level):
        fn()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------- the run
def fmt_arr(a, d=0):
    return " ".join(f"{x:>{8 + d}.{d}f}" for x in a)


def main():
    if "--test" in sys.argv:
        run_tests()
        return
    print(f"N={rsa.N:,} seed={rsa.SEED} CAP={CAP} kappa={KAPPA:.4f} shock={SHOCK:+.0%} E={E_BASKET:.0f} cut={D_CUT:.0f}")
    print(f"age seeds {AGE_SEEDS}; published flow rho* = {PUBLISHED_FLOW_RHO}\n")
    for label, rho0_of in (("PRIMARY rho0 = each F's published flow edge", lambda F: RHO0_OWN[F]),
                           ("SENSITIVITY rho0 = 0.33 at every F", lambda F: RHO0_FIXED)):
        print("=" * 100)
        print(label)
        for F in FLOORS:
            rho0 = rho0_of(F)
            cells = [one_cell(F, s, rho0) for s in AGE_SEEDS]
            m = lambda f: np.array([f(x) for x in cells])                  # noqa: E731
            print("-" * 100)
            print(f"F={F:g}  rho0={rho0}  wants={cells[0]['wants']:,.0f}  capacity full={cells[0]['cap_full']:,.0f}"
                  f"  shocked={cells[0]['cap_shock']:,.0f}  baseline year admits "
                  f"{m(lambda x: x['base_units']).mean():,.0f} ({m(lambda x: x['base_units'] / x['cap_full']).mean():.3f} x cap)")
            fl = m(lambda x: x["flow_rho_shock"])
            print(f"  FLOW rho* at -30% (this population): {fl.mean():.3f}   [published 0.19]")
            for arm in ("A", "B", "B2", "C", "C2"):
                r = m(lambda x: x[arm]["rho_s"])
                flags = sorted(set(x[arm]["flag"] for x in cells))
                print(f"  ARM {arm:<2} stock rho_s {r.mean():.3f} (min {r.min():.3f}, max {r.max():.3f}) flags {flags}"
                      f" | zero-admit all {m(lambda x: x[arm]['z_all']).mean():.3%}"
                      f" adults {m(lambda x: x[arm]['z_adult']).mean():.3%}"
                      f" | <50% of request {m(lambda x: x[arm]['half']).mean():.3%}"
                      f" | year2 @rho0 {m(lambda x: x[arm]['year2']).mean():,.0f}"
                      f" ({m(lambda x: x[arm]['year2'] / x[arm]['base_units']).mean():.3f} x own baseline,"
                      f" {m(lambda x: x[arm]['year2'] / x['cap_full']).mean():.3f} x full cap)")
            if F == 10.0 or rho0_of is not None:
                for arm in ("A", "B", "C"):
                    print(f"  ARM {arm} admitted / own baseline, by age band {[f'{lo:g}-{hi:g}' for lo, hi in BAND_EDGES]}")
                    bnd = m(lambda x: x[arm]["band"]).mean(0)
                    bb = m(lambda x: x[arm]["base_band"]).mean(0)
                    print("     shock   :", fmt_arr(bnd), "\n     baseline:", fmt_arr(bb), "\n     ratio   :",
                          fmt_arr(bnd / bb, 3))
                    dc = m(lambda x: x[arm]["dec"]).mean(0)
                    db = m(lambda x: x[arm]["base_dec"]).mean(0)
                    print(f"  ARM {arm} by credit decile (low->high C)\n     shock   :", fmt_arr(dc),
                          "\n     baseline:", fmt_arr(db), "\n     ratio   :", fmt_arr(dc / db, 3))


def recal_arm_c():
    """Arm C removes under-14 debit, so rho0 = published edge no longer clears capacity in
    its own baseline year. Re-find rho0 for arm C's own ledger, then shock it."""
    print("=" * 100)
    print("ARM C RECALIBRATED: rho0 solved so arm C's OWN unshocked year admits CAP*sum(wants)")
    for F in FLOORS:
        rows = []
        for s in AGE_SEEDS:
            c, w = rsa.build_population(F)
            ages = draw_ages(rsa.N, s)
            cap_full = CAP * w.sum()

            def base(r):
                _, D = build_ledger(c, w, ages, r, d_cut=D_CUT)
                return units(run_year(c, w, ages, F, r, D, "no_children")[0])
            lo, hi = 0.01, 4.0
            while hi - lo > 1e-4:
                m = 0.5 * (lo + hi)
                if base(m) <= cap_full:
                    lo = m
                else:
                    hi = m
            r0 = 0.5 * (lo + hi)
            _, D = build_ledger(c, w, ages, r0, d_cut=D_CUT)
            rs, fl = solve_rho(c, w, ages, F, D, cap_full * (1 + SHOCK), "no_children")
            adm, D1 = run_year(c, w, ages, F, rs, D, "no_children")
            adm2, _ = run_year(c, w, ages + 1.0, F, r0, D1, "no_children")
            rows.append((r0, base(r0) / cap_full, rs, fl, zero_shares(adm, ages)[1], units(adm2) / cap_full))
        a = np.array([[x[0], x[1], x[2], x[4], x[5]] for x in rows])
        print(f"F={F:g}: rho0_C {a[:,0].mean():.3f} (base/cap {a[:,1].mean():.3f}) -> rho_s {a[:,2].mean():.3f}"
              f" (min {a[:,2].min():.3f} max {a[:,2].max():.3f}) | adults admitting zero {a[:,3].mean():.3%}"
              f" | year2 {a[:,4].mean():.3f} x full cap | flags {sorted(set(x[3] for x in rows))}")


if __name__ == "__main__":
    if "--armc" in sys.argv:
        recal_arm_c()
    else:
        main()
