#!/usr/bin/env python3
"""
german_lost_crop.py -- one food line (fresh fruit and vegetables) loses 50% of its output at the
German method. Request sr-20261111-lost-crop-at-the-german-method-same-populati.

Extends german-prime-sweep/german_prime_sweep.py (same population, wants, ages, services, essentials,
Kernel gate; imported, not copied). What is new:

  LINE      share g of one lifestyle unit, measured by fruitveg_share.py (fruitveg_result.json).
            Line demand = g * sum(wants) lifestyle units. Line supply = 0.5 * 1.017 * line demand.
            Every other line stays at 101.7%. Surplus in another line cannot make fruit.
  AGGREGATE capacity after the loss = 1.017 * W * (1 - 0.5 g). The sweep's own solve_rho() is asked for
            the rho at which admitted units = that capacity ("none below 4.0" if the gate never binds).
  LINE VIEW Convention A (essentials first): the line is inside E, so it is charged first and ungated.
            Convention B (proportional): the line is admitted at the person's overall admitted fraction f_i.
            Convention C (gated, E = 0): the line is ordinary discretionary goods. C exists only to price
            what lowering rho would cost; it contradicts the essentials rule (Foundations 5.5.4).
  SHARING   pro rata, and smallest wants first, over the line's per-person wants (w_i * g).

Run:  python german_lost_crop.py [--test]      (full run: minutes)
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(SIM, "german-prime-sweep"))
import german_prime_sweep as gps                                      # noqa: E402

rsa = gps.rsa
CAP = gps.CAP_RATIO
LOSS = 0.5
LINE_CAP_FACTOR = CAP * (1.0 - LOSS)                                  # 0.5085
G = json.load(open(os.path.join(HERE, "fruitveg_result.json")))["fruitveg_share_of_all"]
AGE_SEEDS = (11, 12, 13)
POP_SEEDS = (7, 8, 9, 10, 11)
G_SWEEP = (0.005, 0.0116, 0.02, 0.03, 0.033, 0.034, 0.04, 0.06, 0.10, 0.1238 * 1.0, 0.20)
KB = gps.KAPPA_BEFORE * 365.0                                         # debit-h per lifestyle unit per year


# ------------------------------------------------------------------ line arithmetic
def line_numbers(w, g):
    demand = g * float(w.sum())
    supply = LINE_CAP_FACTOR * demand
    return demand, supply, demand - supply


def share_less_pro_rata(w, supply):
    """Everyone gets supply/demand of their want. Share who get less than want."""
    d = w * 1.0
    frac = supply / d.sum()
    return float((frac * d < d - 1e-12).mean())


def smallest_first(w, supply):
    """Fill wants from the smallest up. Returns (share getting less than want, share getting nothing, served total)."""
    order = np.argsort(w, kind="stable")
    ws = w[order]
    cum = np.cumsum(ws)
    full = cum <= supply + 1e-12
    n_full = int(full.sum())
    got = np.zeros_like(ws)
    got[:n_full] = ws[:n_full]
    if n_full < len(ws):
        got[n_full] = min(ws[n_full], supply - (cum[n_full - 1] if n_full else 0.0))
    less = got < ws - 1e-12
    return float(less.mean()), float((got <= 1e-12).mean()), float(got.sum()), float(got.max() if len(got) else 0)


# ------------------------------------------------------------------ aggregate clearing rho
def aggregate(c, w, F, age_seed, E, g):
    ages = gps.draw_ages(len(c), age_seed)
    C0, D0 = gps.joiner_ledger(c, w, ages, "wants", "full", F)
    W = float(w.sum())
    cap = CAP * W * (1.0 - LOSS * g)
    rho, flag = gps.solve_rho(c, w, ages, F, C0, D0, E, cap)
    u_hi = gps.units(gps.run_year(c, w, ages, F, gps.RHO_HI, C0, D0, E)[1])
    u_0 = gps.units(gps.run_year(c, w, ages, F, 0.0, C0, D0, E)[1])
    return dict(rho=rho, flag=flag, cap=cap, W=W, u_hi=u_hi, u_0=u_0, ages=ages, C0=C0, D0=D0)


def g_star(W, u_hi):
    """Loss share g above which aggregate capacity falls to the units the gate admits at rho 4.0."""
    return 2.0 * (1.0 - u_hi / (CAP * W))


# ------------------------------------------------------------------ line view at a given rho
def line_admitted(c, w, ages, F, rho, C0, D0, E, g, convention):
    """Units of the line admitted, by convention A (full if inside E), B (overall f_i) or C (E=0, gated)."""
    s = gps.S_SHARE
    if convention == "A":
        req = w * gps.KAPPA_AFTER * 365.0
        food_h = w * g * KB                                           # the line's debit-hours at the German method
        # the line is charged inside E; it is fully admitted if it fits inside E
        return float(np.where(food_h <= np.minimum(req, E), w * g, w * g * np.minimum(req, E) / food_h).sum())
    Ee = E if convention == "B" else 0.0
    adm, _, _, req = gps.run_year(c, w, ages, F, rho, C0, D0, Ee)
    f = np.divide(adm, req, out=np.ones_like(req), where=req > 0)
    return float((w * g * f).sum())


def line_clearing_rho(c, w, ages, F, C0, D0, E, g, convention):
    d, sup, _ = line_numbers(w, g)
    f = lambda r: line_admitted(c, w, ages, F, r, C0, D0, E, g, convention)   # noqa: E731
    if f(0.0) > sup + 1e-9:
        return None, "none, the ungated part of the line alone exceeds the line's supply"
    if f(gps.RHO_HI) <= sup:
        return None, "none, the gate never binds the line below rho = 4.0"
    lo, hi = 0.0, gps.RHO_HI
    while hi - lo > 1e-5:
        m = 0.5 * (lo + hi)
        if f(m) <= sup:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi), ""


# ------------------------------------------------------------------ self-tests (each can fail)
def _small(F=10.0, n=20000):
    c, w = rsa.build_population(F, n=n)
    return c, w


def test_shortfall_arithmetic():
    c, w = _small()
    d, sup, short = line_numbers(w, 0.0116)
    assert abs(short / d - (1 - 0.5 * 1.017)) < 1e-12 and abs(sup / d - 0.5085) < 1e-12
    print(f"[ok] 1. shortfall = {short / d:.4%} of line demand (1 - 0.5 x 1.017)")


def test_sharing_rules():
    c, w = _small()
    d, sup, _ = line_numbers(w, 0.0116)
    assert share_less_pro_rata(w, sup) == 1.0
    less, zero, served, mx = smallest_first(w * 0.0116, sup)
    assert abs(served - sup) < 1e-9 * d, (served, sup)                 # all supply is handed out
    assert 0.0 < less < 1.0 and zero < less
    # supply larger than demand -> nobody short under either rule
    assert smallest_first(w, w.sum() * 1.01)[0] == 0.0
    assert share_less_pro_rata(w, w.sum() * 1.01) == 0.0
    print(f"[ok] 2. sharing: pro rata 100%; smallest-first {less:.2%} short, supply fully handed out; surplus -> 0%")


def test_smallest_first_serves_small_wants():
    w = np.array([1.0, 2.0, 3.0, 4.0])
    less, zero, served, _ = smallest_first(w, 3.5)                      # 1 + 2 full, 0.5 of the 3
    assert abs(less - 0.5) < 1e-12 and abs(zero - 0.25) < 1e-12 and abs(served - 3.5) < 1e-12
    print("[ok] 3. smallest-first on [1,2,3,4] with supply 3.5: 2 of 4 short, 1 of 4 gets nothing")


def test_threshold_flips():
    """The 'none' verdict can fail: below g* no rho clears, above it a rho in (0, 4) does."""
    c, w = _small()
    F, E = 10.0, gps.E_GER[0]
    r0 = aggregate(c, w, F, 11, E, 0.0)
    gs = g_star(r0["W"], r0["u_hi"])
    assert 0.0 < gs < 0.2, gs
    below = aggregate(c, w, F, 11, E, gs * 0.9)
    above = aggregate(c, w, F, 11, E, min(0.2, gs * 3.0))
    assert below["rho"] is None, below
    assert above["rho"] is not None and 0.0 < above["rho"] < gps.RHO_HI, above
    print(f"[ok] 4. g* = {gs:.3%}: no rho at 0.9 g*, rho = {above['rho']:.3f} at {min(0.2, gs * 3.0):.1%}")


def test_convention_a_is_rho_blind():
    c, w = _small()
    F, E = 10.0, gps.E_GER[0]
    r0 = aggregate(c, w, F, 11, E, 0.0)
    a = [line_admitted(c, w, r0["ages"], F, r, r0["C0"], r0["D0"], E, 0.0116, "A") for r in (0.0, 0.3, 1.2, 4.0)]
    assert max(a) - min(a) < 1e-9 and abs(a[0] - 0.0116 * w.sum()) < 1e-6
    print("[ok] 5. convention A: the line's admitted units do not move with rho and equal its full demand")


def test_convention_b_and_c_respond():
    c, w = _small()
    F, E = 10.0, gps.E_GER[0]
    r0 = aggregate(c, w, F, 11, E, 0.0)
    lo = line_admitted(c, w, r0["ages"], F, 0.0, r0["C0"], r0["D0"], E, 0.0116, "C")
    hi = line_admitted(c, w, r0["ages"], F, 4.0, r0["C0"], r0["D0"], E, 0.0116, "C")
    assert lo < hi - 1e-6, (lo, hi)                                     # a gated line moves with rho
    print(f"[ok] 6. convention C (gated): line admitted {lo:,.1f} at rho 0 and {hi:,.1f} at rho 4")


def test_g_matches_measurement():
    d = json.load(open(os.path.join(HERE, "fruitveg_result.json")))
    assert abs(d["food_at_home_h"] - 131.0) < 1.0 and abs(d["all_consumption_h"] - 1398.0) < 1.0
    assert 0.0 < d["fruitveg_share_of_all"] < d["fruitveg_share_of_food"] < 1.0
    print(f"[ok] 7. g = {d['fruitveg_share_of_all']:.4%} ({d['fruitveg_h']:.1f} h of {d['all_consumption_h']:.0f}); "
          f"measurement reproduces essentials-basket food 131.0 h")


def run_tests():
    for fn in (test_shortfall_arithmetic, test_sharing_rules, test_smallest_first_serves_small_wants,
               test_threshold_flips, test_convention_a_is_rho_blind, test_convention_b_and_c_respond,
               test_g_matches_measurement):
        fn()
    print("\nAll self-tests passed.")


# ------------------------------------------------------------------ the run
def main():
    print(f"GERMAN LOST CROP  N={rsa.N:,}  g={G:.4%}  loss={LOSS:.0%}  line supply = {LINE_CAP_FACTOR:.4f} x line demand")
    print(f"one lifestyle unit = {KB:,.1f} debit-h/yr at the German method (1380 x 0.836)\n")
    # 1. sharing over several population seeds
    print("=" * 100)
    print("A. THE LINE AND ITS SHARING (population seeds 7..11, per F)")
    for F in (10.0, 2.0, 14.0):
        rows = []
        for ps in POP_SEEDS:
            c, w = rsa.build_population(F, seed=ps)
            d, sup, short = line_numbers(w, G)
            less, zero, served, mx = smallest_first(w * G, sup)
            rows.append((float(w.sum()), d, sup, short, share_less_pro_rata(w, sup), less, zero))
        r = np.array(rows)
        m, lo, hi = r.mean(0), r.min(0), r.max(0)
        print(f"F={F:g}: wants {m[0]:,.0f} units | line demand {m[1]:,.1f} | supply {m[2]:,.1f} | shortfall {m[3]:,.1f} "
              f"= {m[3] / m[1]:.2%} of demand = {m[3] * KB:,.0f} debit-h/yr")
        print(f"       pro rata short {m[4]:.2%} | smallest-first short {m[5]:.2%} (min {lo[5]:.2%}, max {hi[5]:.2%}) "
              f"| smallest-first get NOTHING {m[6]:.2%} (min {lo[6]:.2%}, max {hi[6]:.2%})")
    c10, w10 = rsa.build_population(10.0)
    d, sup, short = line_numbers(w10, G)
    print(f"F=10 in persons: smallest-first short = {smallest_first(w10 * G, sup)[0] * len(w10):,.0f} of {len(w10):,}; "
          f"median person's line want = {np.median(w10) * G * KB:.1f} debit-h/yr")

    # 2. aggregate clearing rho at the measured g
    print("=" * 100)
    print(f"B. WHOLE-ECONOMY CLEARING RHO, g = {G:.4%} (capacity = 1.017 x W x (1 - 0.5 g) = {CAP * (1 - LOSS * G):.5f} x W)")
    for F in (10.0, 2.0, 14.0):
        pop = rsa.build_population(F)
        for E in gps.E_GER:
            res = [aggregate(pop[0], pop[1], F, s_, E, G) for s_ in AGE_SEEDS]
            flags = sorted(set(x["flag"] for x in res))
            rh = [x["rho"] for x in res if x["rho"] is not None]
            gs = np.mean([g_star(x["W"], x["u_hi"]) for x in res])
            txt = ("none below 4.0 (" + "; ".join(flags) + ")") if not rh else f"rho {np.mean(rh):.3f} ({len(rh)}/{len(res)} seeds)"
            print(f"F={F:g} E={E:.1f}: {txt} | capacity {res[0]['cap']:,.0f} vs wants {res[0]['W']:,.0f} "
                  f"({res[0]['cap'] / res[0]['W']:.4f}x) | units admitted at rho 4.0 = {res[0]['u_hi']:,.0f} "
                  f"({res[0]['u_hi'] / res[0]['W']:.4f} of wants) | g* = {gs:.3%}")

    # 3. line view under three conventions
    print("=" * 100)
    print("C. THE LINE ITSELF: can any rho move its supply or demand? (F = 10, age seed 11)")
    pop = rsa.build_population(10.0)
    c, w = pop
    for E in gps.E_GER:
        a0 = aggregate(c, w, 10.0, 11, E, G)
        d, sup, short = line_numbers(w, G)
        for conv, label in (("A", "A essentials first (line inside E, ungated)"),
                            ("B", "B proportional within E"),
                            ("C", "C gated, E = 0 (contradicts 5.5.4; prices the alternative)")):
            vals = {r: line_admitted(c, w, a0["ages"], 10.0, r, a0["C0"], a0["D0"], E, G, conv) for r in (0.0, 0.3, 1.2, 4.0)}
            rho_l, flag = line_clearing_rho(c, w, a0["ages"], 10.0, a0["C0"], a0["D0"], E, G, conv)
            print(f"E={E:.1f} {label}: line admitted/demand at rho 0, 0.3, 1.2, 4.0 = "
                  + ", ".join(f"{v / d:.3f}" for v in vals.values())
                  + f" | line supply/demand {sup / d:.4f} | line-clearing rho: " + (f"{rho_l:.3f}" if rho_l is not None else flag))
            if conv == "C" and rho_l is not None:
                ages, C0, D0 = a0["ages"], a0["C0"], a0["D0"]
                adm, u, _, req = gps.run_year(c, w, ages, 10.0, rho_l, C0, D0, 0.0)
                cut_elsewhere = float(w.sum() - u.sum())
                print(f"      at that rho the whole economy admits {u.sum():,.0f} of {w.sum():,.0f} units; "
                      f"units cut in all lines = {cut_elsewhere:,.0f} against a line shortfall of {short:,.1f} "
                      f"({cut_elsewhere / short:,.1f}x); share of people admitted nothing above E=0: "
                      f"{float((adm <= 1e-6).mean()):.2%}")

    # 4. where the verdict would flip
    print("=" * 100)
    print("D. SWEEP OF g (F = 10, E = 437.2, age seeds 11-13): where does a clearing rho first appear?")
    c, w = pop
    for g in G_SWEEP:
        res = [aggregate(c, w, 10.0, s_, gps.E_GER[0], g) for s_ in AGE_SEEDS]
        rh = [x["rho"] for x in res if x["rho"] is not None]
        txt = "none below 4.0" if not rh else f"rho {np.mean(rh):.3f} (min {min(rh):.3f}, max {max(rh):.3f}, {len(rh)}/{len(res)})"
        d, sup, short = line_numbers(w, g)
        less = smallest_first(w * g, sup)[0]
        print(f"g = {g:.3%}: capacity {res[0]['cap'] / res[0]['W']:.4f} x wants | {txt} | line shortfall {short:,.0f} units "
              f"| smallest-first short {less:.2%}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        main()
