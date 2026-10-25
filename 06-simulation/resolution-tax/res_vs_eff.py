"""
Resolution spread against efficiency spread -- off ONE generator, ONE statistic.

REQUEST sr-20260909-off-one-generator-measure-the-spread-in-a-co.
Source: SB-06 section 7 (sim-briefs/SB-06_resolution-tax.md) and the self-council
record obj-20260909-self-council-sb-06-threshold-model-entailed.

QUESTION. A co-product's published debit-hours per kg varies across producers for
two reasons. (RES) producers read the same physical chain at different
resolution, because instruments cost and scale pays for them. (EFF) producers
really do spend different hours, because some are more efficient. Measure both
as the same statistic, from the same generator. Does RES dominate EFF?

Builds on resolution_tax.py (same folder): the process draw, the charge rule
(Foundations 3.4a), the affordability rule and the greedy cut placement are all
imported, not rewritten.

THE THREE ARMS (same processes, same producer scales, same good):
  RES   every producer has the identical physical process (efficiency 1.0) and
        reads it at the resolution its scale affords.
  EFF   every producer reads the chain at the finest resolution (truth), and
        its step hours are multiplied by a real efficiency factor
        f = exp(a_p + e_ps), a_p ~ N(0, SIG_A) producer-wide, e_ps ~ N(0, SIG_E)
        step-specific. No resolution effect.
  BOTH  efficiency factors AND scale-driven resolution together.

THE STATISTICS (all per good per process, over that process's producers; then
the median and mean over processes):
  p90/p10   ratio of the 90th to the 10th percentile figure. Does not grow with
            the number of producers. PRIMARY.
  max/min   over all N producers. Grows with N, so reported for N and for N=3.
  max/min3  mean max/min over random triples, the sample size of the external
            bar (three national production methods, 1,380 / 759 = 1.82).
  sd(ln)    standard deviation of ln(figure). Variance adds across independent
            causes, so var share of RES = var_res / (var_res + var_eff).

THE EXTERNAL ANCHOR. 1.82 is a published whole-lifestyle ratio across three
countries (median-lifestyle/Q6.md). SIG_A is CALIBRATED so that the mean
max/min3 of the EFF arm equals 1.82. That is a calibration, not a check, and is
reported as one. Whole-lifestyle national ratios average over thousands of
goods, so a single good's producer-to-producer efficiency spread is plausibly
WIDER than 1.82. SIG_A is therefore also swept.

Run:  python res_vs_eff.py          # full run, then self-tests
      python res_vs_eff.py --test   # self-tests only
"""

from __future__ import annotations

import argparse
import math
import os
import random
import statistics as st
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "chain-resolution"))
import resolution_tax as rt  # noqa: E402

SEED = 20261025
R_EFF_BAR = 1380.0 / 759.0          # 1.818, median-lifestyle/Q6.md
SIG_E_DEFAULT = 0.0
N_PRODUCERS = 200
N_PROCESSES = 400
N_GRID = (3, 7, 12, 20)


def eff_charge(cost, exit_step, cuts, factors):
    """charged_hours with a per-step efficiency factor on every step's hours."""
    scaled = [c * f for c, f in zip(cost, factors)]
    return rt.charged_hours(scaled, exit_step, cuts)


def draw_cost(rng, n, sigma_cost):
    raw = [math.exp(rng.gauss(0.0, sigma_cost)) for _ in range(n)]
    t = sum(raw)
    return [rt.CHAIN_H * r / t for r in raw]


def draw_exits(rng, n, m, exit_mode):
    if exit_mode == "uniform":
        return [rng.randint(1, n) for _ in range(m)]
    if exit_mode == "late":        # goods leave in the last third of the chain
        lo = max(1, n - max(1, n // 3))
        return [rng.randint(lo, n) for _ in range(m)]
    raise ValueError(exit_mode)


def simulate_arms(n, *, sigma_cost=rt.SIGMA, exit_mode="uniform", m=rt.M_DEFAULT,
                  h=rt.H_DEFAULT, share=rt.S_DEFAULT, sig_a=0.354,
                  sig_e=SIG_E_DEFAULT, n_proc=N_PROCESSES, n_prod=N_PRODUCERS,
                  seed=SEED):
    """One record per process: the good's h/kg for every producer, in each arm."""
    rng = random.Random(seed * 1000 + n * 10 + m)
    full = frozenset(range(1, n))
    recs = []
    for _ in range(n_proc):
        cost = draw_cost(rng, n, sigma_cost)
        exits = draw_exits(rng, n, m, exit_mode)
        mass = [math.exp(rng.gauss(0.0, 0.7)) * 100.0 for _ in range(m)]
        g = rng.randrange(m)
        eg, mg = exits[g], mass[g]
        cache = {}
        res, eff, both = [], [], []
        for _p in range(n_prod):
            q = math.exp(rng.uniform(math.log(rt.Q_LO), math.log(rt.Q_HI)))
            b = rt.cuts_afforded(q, h, share)
            if b not in cache:
                cache[b] = rt.place_cuts_greedy(cost, exits, b)
            cuts = cache[b]
            a = rng.gauss(0.0, sig_a)
            fac = [math.exp(a + rng.gauss(0.0, sig_e)) for _ in range(n)]
            res.append(rt.charged_hours(cost, eg, cuts) / mg)
            eff.append(eff_charge(cost, eg, full, fac) / mg)
            both.append(eff_charge(cost, eg, cuts, fac) / mg)
        recs.append({"res": res, "eff": eff, "both": both,
                     "terminal": eg == n})
    return recs


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))]


def stats_one(vals, rng):
    """The four statistics for one arm of one process."""
    lv = [math.log(v) for v in vals]
    mean = sum(lv) / len(lv)
    var = sum((x - mean) ** 2 for x in lv) / len(lv)
    tri = []
    for _ in range(20):
        t = [vals[rng.randrange(len(vals))] for _ in range(3)]
        tri.append(max(t) / min(t))
    return {"p9010": pct(vals, 0.9) / pct(vals, 0.1),
            "maxmin": max(vals) / min(vals),
            "maxmin3": sum(tri) / len(tri),
            "var": var}


def summarise_arms(recs, seed=SEED + 7, early_only=False):
    rng = random.Random(seed)
    rows = [r for r in recs if not (early_only and r["terminal"])]
    out = {}
    for arm in ("res", "eff", "both"):
        per = [stats_one(r[arm], rng) for r in rows]
        out[arm] = {k: (st.median(p[k] for p in per), st.mean(p[k] for p in per))
                    for k in ("p9010", "maxmin", "maxmin3", "var")}
    vr, ve = out["res"]["var"][1], out["eff"]["var"][1]
    out["res_var_share"] = vr / (vr + ve) if vr + ve > 0 else float("nan")
    out["count"] = len(rows)
    return out


def calibrate_sig_a(target=R_EFF_BAR, seed=SEED + 99):
    """Bisect SIG_A so that mean max/min of 3 efficiency draws equals target.
    Only the producer-wide factor is used (sig_e = 0), as in the anchor arm."""
    def mm3(sig):
        rng = random.Random(seed)
        xs = []
        for _ in range(60000):
            t = [rng.gauss(0.0, sig) for _ in range(3)]
            xs.append(math.exp(max(t) - min(t)))
        return sum(xs) / len(xs)
    lo, hi = 0.01, 1.5
    for _ in range(40):
        mid = (lo + hi) / 2
        if mm3(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def crossing_sig_a(recs_res_p9010, seed=SEED + 5):
    """SIG_A at which the EFF arm's median p90/p10 equals the RES arm's.
    Efficiency p90/p10 of a normal producer factor is exp(2.5631 * sigma), so
    solve it in closed form and check it by simulation in the self-tests."""
    return math.log(recs_res_p9010) / 2.5631


# ---------------------------------------------------------------------------
# Self-tests. Each can fail.
# ---------------------------------------------------------------------------

def test_steer_digits() -> str:
    import chain_resolution as cr
    c = cr.build_steer()
    n = len(c.steps)
    coarse = cr.product_cost_per_kg(c, "hide", [(0, n)])["energy_mj"]
    fine = cr.product_cost_per_kg(c, "hide", [(i, i + 1) for i in range(n)])["energy_mj"]
    beef_c = cr.product_cost_per_kg(c, "packaged_beef", [(0, n)])["energy_mj"]
    beef_f = cr.product_cost_per_kg(c, "packaged_beef", [(i, i + 1) for i in range(n)])["energy_mj"]
    assert abs(coarse - 12.5) < 1e-9 and abs(fine - 2.0) < 1e-9, (coarse, fine)
    assert abs(beef_c - 2.0) < 1e-9 and abs(beef_f - 2.0) < 1e-9, (beef_c, beef_f)
    return "steer hide 12.50 / 2.00 (6.25x); packaged beef 2.00 at both resolutions"


def test_no_instruments_no_efficiency_gives_spread_one() -> str:
    """RES with nobody able to buy a cut, and EFF with sigma 0, are both flat."""
    recs = simulate_arms(8, share=0.0, sig_a=0.0, n_proc=30, n_prod=25)
    for r in recs:
        for arm in ("res", "eff", "both"):
            assert max(r[arm]) / min(r[arm]) < 1 + 1e-9, arm
    return "no instruments and no efficiency differences: every arm has spread 1.00"


def test_arms_isolate_their_cause() -> str:
    """EFF with identical resolution must not move when scale changes, and RES
    must not move when SIG_A changes. Each fails if the arms are cross-wired."""
    a = simulate_arms(8, sig_a=0.0, n_proc=40, n_prod=40, seed=5)
    b = simulate_arms(8, sig_a=0.6, n_proc=40, n_prod=40, seed=5)
    for ra, rb in zip(a, b):
        assert all(abs(x - y) < 1e-9 for x, y in zip(ra["res"], rb["res"])), "RES moved with SIG_A"
    c = simulate_arms(8, share=0.0, sig_a=0.3, n_proc=40, n_prod=40, seed=5)
    d = simulate_arms(8, share=0.05, sig_a=0.3, n_proc=40, n_prod=40, seed=5)
    for rc, rd in zip(c, d):
        assert all(abs(x - y) < 1e-9 for x, y in zip(rc["eff"], rd["eff"])), "EFF moved with scale share"
    return "RES ignores SIG_A and EFF ignores affordability (arms are separate)"


def test_calibration_matches_closed_form() -> str:
    """For three N(0,s) draws E[max-min] = 3 s / sqrt(pi); a first-order check on
    the bisection (exp makes it a little larger, so allow a band)."""
    s = calibrate_sig_a()
    lo = R_EFF_BAR
    approx = math.exp(3 * s / math.sqrt(math.pi))      # Jensen: a lower bound
    assert 0.2 < s < 0.6, s
    assert approx <= lo + 1e-3, (approx, lo)
    assert 0.9 * lo < approx, (approx, lo)
    return f"calibrated SIG_A = {s:.3f}; closed-form lower bound {approx:.3f} <= {lo:.3f}"


def test_variance_adds_when_independent() -> str:
    """ln(both) = ln(res) + a_p when sig_e = 0, and a_p is independent of scale:
    var(both) must equal var(res) + var(eff)."""
    recs = simulate_arms(10, sig_a=0.4, sig_e=0.0, n_proc=150, n_prod=200, seed=9)
    s = summarise_arms(recs)
    vb, vr, ve = s["both"]["var"][1], s["res"]["var"][1], s["eff"]["var"][1]
    assert abs(vb - (vr + ve)) < 0.12 * vb, (vb, vr, ve)
    return f"var(both) {vb:.3f} = var(res) {vr:.3f} + var(eff) {ve:.3f} within 12%"


def test_eff_p9010_matches_normal() -> str:
    """With sig_e=0 and a terminal-heavy chain, EFF p90/p10 = exp(2.563*SIG_A)."""
    sig = 0.35
    recs = simulate_arms(6, sig_a=sig, n_proc=40, n_prod=2000, seed=3)
    med = st.median(pct(r["eff"], 0.9) / pct(r["eff"], 0.1) for r in recs)
    want = math.exp(2.5631 * sig)
    assert abs(med - want) < 0.08 * want, (med, want)
    return f"EFF median p90/p10 {med:.3f} vs normal closed form {want:.3f}"


def test_verdict_can_flip() -> str:
    """The verdict 'RES beats EFF' must come back both ways as SIG_A is swept.
    If one end did not flip, the comparison could not have failed."""
    recs = simulate_arms(12, sig_a=0.05, n_proc=80, n_prod=100, seed=4)
    lo = summarise_arms(recs)
    recs = simulate_arms(12, sig_a=0.9, n_proc=80, n_prod=100, seed=4)
    hi = summarise_arms(recs)
    assert lo["res"]["p9010"][0] > lo["eff"]["p9010"][0], "RES should win at tiny SIG_A"
    assert hi["res"]["p9010"][0] < hi["eff"]["p9010"][0], "EFF should win at huge SIG_A"
    return "RES wins at SIG_A 0.05 and EFF wins at SIG_A 0.9: the comparison can lose"


TESTS = [
    test_steer_digits,
    test_no_instruments_no_efficiency_gives_spread_one,
    test_arms_isolate_their_cause,
    test_calibration_matches_closed_form,
    test_variance_adds_when_independent,
    test_eff_p9010_matches_normal,
    test_verdict_can_flip,
]


def run_tests() -> int:
    print("\nSELF-TESTS\n" + "-" * 78)
    failed = 0
    for t in TESTS:
        try:
            print(f"  PASS  {t()}")
        except AssertionError as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print("-" * 78 + f"\n  {len(TESTS) - failed}/{len(TESTS)} passed\n")
    return failed


# ---------------------------------------------------------------------------
# Main run
# ---------------------------------------------------------------------------

def fmt(s, arm, key):
    return f"{s[arm][key][0]:>6.2f}/{s[arm][key][1]:<6.2f}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)

    sig_a = calibrate_sig_a()
    print(f"seed {SEED}; {N_PROCESSES} processes x {N_PRODUCERS} producers per cell; "
          f"external bar R_eff = 1380/759 = {R_EFF_BAR:.3f}; calibrated SIG_A = {sig_a:.3f}")
    print("cells show median/mean over processes of the statistic\n")

    hdr = (f"{'':>3} {'p90/p10 RES':>13} {'p90/p10 EFF':>13} {'max/min3 RES':>13} "
           f"{'max/min3 EFF':>13} {'maxmin200 RES':>14} {'maxmin200 EFF':>14} "
           f"{'RES var%':>8} {'count':>6}")

    def row(label, s):
        return (f"{label:>3} {fmt(s,'res','p9010'):>13} {fmt(s,'eff','p9010'):>13} "
                f"{fmt(s,'res','maxmin3'):>13} {fmt(s,'eff','maxmin3'):>13} "
                f"{fmt(s,'res','maxmin'):>14} {fmt(s,'eff','maxmin'):>14} "
                f"{100*s['res_var_share']:>7.0f}% {s['count']:>6}")

    for early in (False, True):
        print(("2. EARLY-LEAVING GOODS ONLY" if early else
               "1. ALL GOODS (terminal goods have RES spread 1.00 by theorem)")
              + f", lognormal costs sigma={rt.SIGMA}, uniform exits, SIG_A={sig_a:.3f}")
        print(f"{'n':>3} " + hdr[4:])
        for n in N_GRID:
            s = summarise_arms(simulate_arms(n, sig_a=sig_a), early_only=early)
            print(row(str(n), s))
        print()

    print("3. SKEW OF E_s AND EXIT MODE, n=12, all goods")
    print(f"{'cell':>14} " + hdr[4:])
    for sc in (0.0, 0.8, 1.6):
        for em in ("uniform", "late"):
            s = summarise_arms(simulate_arms(12, sigma_cost=sc, exit_mode=em, sig_a=sig_a))
            print(f"{'sc'+str(sc)+' '+em:>14} " + row('', s)[4:])
    print()

    print("4. SWEEP OF SIG_A (efficiency spread), n=12, all goods, uniform exits")
    print(f"{'SIG_A':>6} {'p90/p10 EFF':>12} {'max/min3 EFF':>13} {'p90/p10 RES':>12} "
          f"{'RES var%':>9} {'BOTH p90/p10':>13}")
    res_p = None
    for sg in (0.1, 0.2, sig_a, 0.5, 0.7, 1.0):
        s = summarise_arms(simulate_arms(12, sig_a=sg))
        res_p = s["res"]["p9010"][0]
        print(f"{sg:>6.3f} {s['eff']['p9010'][0]:>12.2f} {s['eff']['maxmin3'][1]:>13.2f} "
              f"{res_p:>12.2f} {100*s['res_var_share']:>8.0f}% {s['both']['p9010'][0]:>13.2f}")
    x = crossing_sig_a(res_p)
    print(f"\n  SIG_A at which EFF p90/p10 equals RES median p90/p10 ({res_p:.2f}): {x:.3f}; "
          f"EFF max/min3 there is about {math.exp(3*x/math.sqrt(math.pi)):.2f}")

    print("\n5. SEED STABILITY of the headline (n=12, all goods, calibrated SIG_A)")
    for sd in (SEED, SEED + 1, SEED + 2, SEED + 3):
        s = summarise_arms(simulate_arms(12, sig_a=sig_a, seed=sd), seed=sd)
        print(f"  seed {sd}: p90/p10 RES {s['res']['p9010'][0]:.2f}  EFF {s['eff']['p9010'][0]:.2f}  "
              f"RES var share {100*s['res_var_share']:.0f}%")

    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
