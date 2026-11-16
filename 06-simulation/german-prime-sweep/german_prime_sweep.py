#!/usr/bin/env python3
"""
german_prime_sweep.py -- clearing rho of the STOCK gate at the German method, swept over
capacity shocks from +20% to -40%, at F = 2, 10, 14.

Request sr-20261109-prime-rate-sweep-at-the-german-method-on-the.
Extends stock-gate-clearing/stock_gate_clearing.py (same population, wants, age pyramid,
Kernel gate). What changes, each item from the request or PLAN-2026-11-09 section 7:

  METHOD      German every-payer ratio 0.836 of US hours. Capacity = 1.017 x sum(wants) x (1+shock).
  GATE        stock, D <= rho*(C+P), P = 0 (Foundations 3.0, 5.5.6). Kernel.room().
  ESSENTIALS  the first E h/yr of each person's request is ungated (5.5.4) and charged to D first.
              E = (523 .. 553) x 0.836 = 437.2 .. 462.3 h (goods only, author ruling 7.1). Both ends run.
  SERVICES    care 253 + schooling 87 + land transport 59 + post/telecoms 13 = 412 h/yr (US method,
              essentials-basket/RESULTS.md) leave the receiver's D (author ruling 2026-11-09).
              kappa_before = 1380*0.836/365 ; kappa_after = (1380-412)*0.836/365 (printed).
              Services are still produced: they take s = 412/1380 of every person's physical request,
              are never refused, and count against capacity.
  PASTS       joiners (4.4): D_past = 365*age*want*kappa_after  (uncapped; NOT min(.., rho0*c)),
              C_past = c*365*age (as the stock-gate-clearing population).
  YEAR        accrue 365 d of credit, request want*kappa_after*365 goods debit-hours, essentials
              ungated, rest through the gate.
  UNITS       person i's admitted whole-lifestyle units = want_i*(s + (1-s)*f_i), f_i = admitted
              goods h / requested goods h. Capacity is in the same units.
  CELL        rho_s = rho at which the year's admitted units = capacity (bisection, 0..4.0).
              Flags: 'none, gate never binds below rho = 4.0' ; 'none, ungated part alone exceeds capacity'.
  YEAR 2      ledger carried (D += admitted), ages+1, capacity restored to baseline, rho = RHO0 (1.2).
              If the year had no clearing rho, year 1 itself is run at RHO0.

Run:  python german_prime_sweep.py [--test]   (full run ~ minutes; prints a table)
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

GERMAN = 0.836
CAP_RATIO = 1.017                       # 5.5.3: capacity = 101.7% of wants at the German method
ANCHOR = 1380.0                         # h/yr, US-method median (3.5)
SERVICE_H = {"care": 253.0, "schooling": 87.0, "land transport services": 59.0, "post and telecoms": 13.0}
SERVICE_TOTAL = sum(SERVICE_H.values())              # 412
S_SHARE = SERVICE_TOTAL / ANCHOR                      # share of a request that is services
KAPPA_BEFORE = ANCHOR * GERMAN / 365.0                # debit-h/day per lifestyle unit, German, services on D
KAPPA_AFTER = (ANCHOR - SERVICE_TOTAL) * GERMAN / 365.0
E_US = (523.0, 553.0)                                 # broad basket, goods only (PLAN 7.2)
E_GER = tuple(e * GERMAN for e in E_US)               # 437.2, 462.3
SHOCKS = (0.20, 0.10, 0.0, -0.10, -0.20, -0.30, -0.40)
FLOORS = (2.0, 10.0, 14.0)
AGE_SEEDS = (11, 12, 13, 14, 15)
RHO0 = 1.2                                            # baseline rho for year 2 (the document's worked setting)
RHO_HI = 4.0
BAND_EDGES = [(b[1], b[2]) for b in AGE_BANDS]


# ------------------------------------------------------------------ ledger and year
def joiner_ledger(c, w, ages, past="wants", credit="full", F=10.0):
    """C and D at the start of the year for people who joined with a rebuilt past (4.4)."""
    rate = c if credit == "full" else np.full_like(c, F)
    C = rate * 365.0 * ages
    per_year = w * KAPPA_AFTER * 365.0 if past == "wants" else np.full_like(w, np.median(w) * KAPPA_AFTER * 365.0)
    return C, per_year * ages


def run_year(c, w, ages, F, rho, C0, D0, E, s=S_SHARE, kappa=None):
    """One year. Returns (goods debit-hours admitted, units admitted per person, D after, request)."""
    kappa = KAPPA_AFTER if kappa is None else kappa
    k = Kernel(len(c), c, Dials(rho=float(rho), floor_h=float(F)))
    k.C = C0.copy()
    k.D = D0.copy()
    k.accrue(days=365.0)
    req = w * kappa * 365.0
    ess = np.minimum(req, E)
    k.consume(ess, essential=True)
    a2, _ = k.consume(req - ess)
    adm = ess + a2
    assert np.allclose(k.D - D0, adm, atol=1e-6), "D must rise by exactly what was admitted"
    f = np.divide(adm, req, out=np.ones_like(req), where=req > 0)
    return adm, w * (s + (1.0 - s) * f), k.D, req


def units(u):
    return float(u.sum())


def solve_rho(c, w, ages, F, C0, D0, E, target, s=S_SHARE, kappa=None):
    f = lambda r: units(run_year(c, w, ages, F, r, C0, D0, E, s, kappa)[1])   # noqa: E731
    if f(0.0) > target + 1e-9:
        return None, "none, ungated part alone exceeds capacity"
    if f(RHO_HI) <= target:
        return None, "none, gate never binds below rho = 4.0"
    lo, hi = 0.0, RHO_HI
    while hi - lo > 1e-5:
        m = 0.5 * (lo + hi)
        if f(m) <= target:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi), ""


def by_band(w, u, ages):
    return np.array([u[(ages >= lo) & (ages < hi)].sum() for lo, hi in BAND_EDGES])


def band_wants(w, ages):
    return np.array([w[(ages >= lo) & (ages < hi)].sum() for lo, hi in BAND_EDGES])


def cell(F, age_seed, shock, E, past="wants", credit="full", pop=None):
    c, w = pop if pop is not None else rsa.build_population(F)
    ages = draw_ages(len(c), age_seed)
    C0, D0 = joiner_ledger(c, w, ages, past, credit, F)
    cap_full = CAP_RATIO * w.sum()
    cap = cap_full * (1.0 + shock)
    rho_s, flag = solve_rho(c, w, ages, F, C0, D0, E, cap)
    rho_year = RHO0 if rho_s is None else rho_s
    adm, u, D1, req = run_year(c, w, ages, F, rho_year, C0, D0, E)
    over = req > E + 1e-9
    above = adm - np.minimum(req, E)
    zero_above = float((above[over] <= 1e-6).mean()) if over.any() else 0.0
    # next year: same people one year older, baseline rho, capacity restored
    C1 = C0 + c * 365.0
    _, u2, _, _ = run_year(c, w, ages + 1.0, F, RHO0, C1, D1, E)
    _, ub, _, _ = run_year(c, w, ages, F, RHO0, C0, D0, E)          # unshocked baseline year at RHO0
    return dict(rho=rho_s, flag=flag, units=units(u), cap=cap, cap_full=cap_full, wants=float(w.sum()),
                zero_above=zero_above, zero_all=float((adm <= 1e-6).mean()),
                band=by_band(w, u, ages), bandw=band_wants(w, ages), year2=units(u2), base=units(ub),
                ungated=float((w * S_SHARE).sum() + ((1 - S_SHARE) * w * np.minimum(req, E) / req).sum()))


# ------------------------------------------------------------------ self-tests (each can fail)
def _small(F=10.0, n=20000):
    c, w = rsa.build_population(F, n=n)
    return c, w, draw_ages(n, 11)


def test_empty_ledger_equals_flow():
    """Empty past, no services, no essentials: stock year == flow admitted demand sum(min(w, rho*c/kappa))."""
    c, w, _ = _small()
    z = np.zeros(len(c))
    for r in (0.15, 0.6, 1.5):
        _, u, _, _ = run_year(c, w, z, 10.0, r, z, z, 0.0, s=0.0, kappa=rsa.KAPPA)
        flow = np.minimum(w, r * c / rsa.KAPPA).sum()
        assert abs(units(u) - flow) < 1e-6 * flow, (r, units(u), flow)
    print("[ok] 1. empty ledger, s=0, E=0: stock year == flow demand at 3 rhos")


def test_ungated_floor_is_exact():
    """At rho=0 a person with room<=0 admits exactly services + essentials, nothing else."""
    c, w, ages = _small()
    C0, D0 = joiner_ledger(c, w, ages)
    E = E_GER[0]
    _, u, _, req = run_year(c, w, ages, 10.0, 0.0, C0, D0, E)
    expect = (w * (S_SHARE + (1 - S_SHARE) * np.minimum(req, E) / req)).sum()
    assert abs(units(u) - expect) < 1e-6 * expect, (units(u), expect)
    print(f"[ok] 2. rho=0 admits exactly services + essentials ({units(u):,.0f} units)")


def test_monotone_in_rho():
    c, w, ages = _small()
    C0, D0 = joiner_ledger(c, w, ages)
    u = [units(run_year(c, w, ages, 10.0, r, C0, D0, E_GER[0])[1]) for r in np.linspace(0, 2, 21)]
    assert all(b >= a - 1e-9 for a, b in zip(u, u[1:]))
    print("[ok] 3. admitted units never fall as rho rises")


def test_gate_respected_above_E():
    c, w, ages = _small()
    C0, D0 = joiner_ledger(c, w, ages)
    E, r = E_GER[1], 0.3
    adm, _, _, req = run_year(c, w, ages, 10.0, r, C0, D0, E)
    ess = np.minimum(req, E)
    room = np.maximum(r * (C0 + c * 365.0) - (D0 + ess), 0.0)
    assert np.all(adm - ess <= room + 1e-6)
    print("[ok] 4. nobody is admitted above E beyond rho*(C+P) - D")


def test_clearing_can_pass_and_fail():
    c, w, ages = _small()
    C0, D0 = joiner_ledger(c, w, ages)
    cap = CAP_RATIO * w.sum() * 0.8
    lo = units(run_year(c, w, ages, 10.0, 0.0, C0, D0, E_GER[0])[1])
    hi = units(run_year(c, w, ages, 10.0, RHO_HI, C0, D0, E_GER[0])[1])
    assert lo < cap < hi, (lo, cap, hi)
    r, flag = solve_rho(c, w, ages, 10.0, C0, D0, E_GER[0], cap)
    assert r is not None and 0 < r < RHO_HI, (r, flag)
    r2, flag2 = solve_rho(c, w, ages, 10.0, C0, D0, E_GER[0], hi * 1.01)
    assert r2 is None and "never binds" in flag2
    r3, flag3 = solve_rho(c, w, ages, 10.0, C0, D0, E_GER[0], lo * 0.99)
    assert r3 is None and "ungated" in flag3
    print(f"[ok] 5. clearing passes (-20%: rho {r:.3f}), and both 'none' flags can fire")


def test_inputs():
    assert abs(CAP_RATIO * 100 - 101.7) < 1e-9 and abs(E_GER[0] - 437.2) < 0.1 and abs(E_GER[1] - 462.3) < 0.1
    assert abs(KAPPA_AFTER / KAPPA_BEFORE - 968.0 / 1380.0) < 1e-12 and SERVICE_TOTAL == 412.0
    print(f"[ok] 6. inputs: E = {E_GER[0]:.1f}-{E_GER[1]:.1f}; kappa {KAPPA_BEFORE:.4f} -> {KAPPA_AFTER:.4f}")


def run_tests():
    for fn in (test_empty_ledger_equals_flow, test_ungated_floor_is_exact, test_monotone_in_rho,
               test_gate_respected_above_E, test_clearing_can_pass_and_fail, test_inputs):
        fn()
    print("\nAll self-tests passed.")


# ------------------------------------------------------------------ the run
def summarise(cells):
    rhos = [x["rho"] for x in cells]
    flags = sorted(set(x["flag"] for x in cells))
    if all(r is None for r in rhos):
        r_txt = flags[0] if len(flags) == 1 else " / ".join(flags)
    else:
        v = [r for r in rhos if r is not None]
        r_txt = f"{np.mean(v):.3f} (min {min(v):.3f}, max {max(v):.3f}; {len(v)}/{len(rhos)} seeds)"
        if len(v) < len(rhos):
            r_txt += " + other seeds: " + " / ".join(f for f in flags if f)
    return r_txt


def main():
    print(f"GERMAN PRIME-RATE SWEEP  N={rsa.N:,} pop seed={rsa.SEED} age seeds={AGE_SEEDS} RHO0={RHO0}")
    print(f"kappa BEFORE services removed = {KAPPA_BEFORE:.4f} h/day = {KAPPA_BEFORE * 365:.1f} h/yr (1380 x {GERMAN})")
    print(f"kappa AFTER  services removed = {KAPPA_AFTER:.4f} h/day = {KAPPA_AFTER * 365:.1f} h/yr ((1380-{SERVICE_TOTAL:.0f}) x {GERMAN})")
    print(f"services removed: {SERVICE_H}; share of a request s = {S_SHARE:.4f}")
    print(f"E (goods only, x{GERMAN}) = {E_GER[0]:.1f} and {E_GER[1]:.1f} h/yr\n")
    arms = [("PRIMARY wants-scaled past, credit c*age", "wants", "full", (10.0, 2.0, 14.0), E_GER)]
    arms += [("SENS-1 uniform-kappa past (stable-band style), F=10", "uniform", "full", (10.0,), E_GER),
             ("SENS-2 floor-only past credit (4.4 cond. 2 conservative), F=10", "wants", "floor", (10.0,), E_GER)]
    for label, past, credit, floors, Es in arms:
        print("=" * 110)
        print(label)
        for F in floors:
            pop = rsa.build_population(F)
            for E in Es:
                print("-" * 110)
                print(f"F={F:g}  E={E:.1f} h/yr   wants={pop[1].sum():,.0f}  capacity base={CAP_RATIO * pop[1].sum():,.0f}")
                for shock in SHOCKS:
                    cells = [cell(F, s_, shock, E, past, credit, pop) for s_ in AGE_SEEDS]
                    m = lambda f: np.mean([f(x) for x in cells])       # noqa: E731
                    print(f"  shock {shock:+.0%}: cap {cells[0]['cap']:,.0f} | rho_s: {summarise(cells)}"
                          f" | admit>E zero {m(lambda x: x['zero_above']):.2%}"
                          f" | units {m(lambda x: x['units']):,.0f} ({m(lambda x: x['units'] / x['cap']):.3f} x cap)"
                          f" | ungated {m(lambda x: x['ungated']):,.0f}"
                          f" | yr2@{RHO0} {m(lambda x: x['year2']):,.0f} ({m(lambda x: x['year2'] / x['cap_full']):.3f} x full cap)")
                    if label.startswith("PRIMARY") and E == Es[0]:
                        bnd = np.mean([x["band"] for x in cells], 0)
                        bw = np.mean([x["bandw"] for x in cells], 0)
                        print("      units by age band", [f"{lo:g}-{hi:g}" for lo, hi in BAND_EDGES], ":",
                              " ".join(f"{v:,.0f}" for v in bnd), "| share of band's wants:",
                              " ".join(f"{v:.3f}" for v in bnd / bw))


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        main()
