"""
SB-05 section 7 -- a refutation threshold both arms of which can fail.

Answers sim request sr-20260908-rewrite-sb-05-section-7-with-a-refutation-th
(@custos c47620, record obj-20260908-custos-sb05-threshold-unreachable).
Extends parcel_identity.py; reuses its walk, groups and Monte Carlo.

THE COMMON UNIT
  Every policy gets a LOSS in one unit: relative error of the published
  figure against the truth, |books / T - 1|, for one buyer's holding.
    P1, P2 : mean |books/T - 1| over trials          (E1, E2)
    P3     : lambda * s,  s = share of figures reported "not identified",
             lambda = the relative error a network treats as equal to having
             no figure at all.
  lambda is the one number the checker supplies. It is therefore never fixed:
  the run reports the BREAK-EVEN lambda* = min(E1, E2) / s. P3 beats the better
  of P1/P2 exactly when lambda < lambda* (refusing pays only if a missing figure
  is cheap). lambda*_P1 = E1 / s is the same against P1 alone.

THE TWO ARMS
  Arm A  P1 vs P2   decided by t, the twin share of ambiguous links. Reported
                    as the crossover t*.
  Arm B  best(P1,P2) vs P3   decided by lambda. Reported as lambda*(u).

Run:  python threshold_s7.py --test
      python threshold_s7.py            # writes threshold_s7.csv
"""

from __future__ import annotations

import argparse
import csv
import itertools
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import parcel_identity as pi  # noqa: E402

cr = pi.cr
SEED = 20261023
TRIALS = 4000
U_GRID = [0.05, 0.10, 0.20, 0.30, 0.50]
MODES = ("flat", "big_dark", "small_dark")
TWIN_COUNTS = [0, 5, 10, 21, 40, 100]


def losses(r):
    """Per-policy loss pieces for one simulate() result."""
    T = r["truth"]
    e1 = np.abs(r["p1"] / T - 1.0)
    e2 = np.abs(r["p2"] / T - 1.0)
    s = float(r["refuse"].mean())
    E1, E2 = float(e1.mean()), float(e2.mean())
    best = min(E1, E2)
    return {"E1": E1, "E2": E2, "E1_p95": float(np.quantile(e1, .95)),
            "E2_p95": float(np.quantile(e2, .95)),
            "s": s,
            "lam_star": best / s if s > 0 else float("nan"),
            "lam_star_p1": E1 / s if s > 0 else float("nan"),
            "best_of_p1p2": "P1" if E1 <= E2 else "P2",
            "realised_u": r["realised_u"]}


def p3_wins(row, lam, against="best"):
    """against "best": the better of P1/P2. against "P1": the conservative reading.
    With no twins P2 is exact, so P3 cannot beat "best" there (entailed, reported)."""
    ref = min(row["E1"], row["E2"]) if against == "best" else row["E1"]
    return row["s"] * lam < ref


def pair_holdings(ch):
    return [frozenset(c) for c in itertools.combinations(ch.products, 2)]


def run_cell(groups, holdings, u, mode, trials, rng):
    """Average losses over a list of holdings (one entry = one holding)."""
    acc = []
    for h in holdings:
        q, n, tw = pi.holding_arrays(groups, h)
        if n.sum() == 0:
            continue                       # nothing ambiguous in this holding
        acc.append(losses(pi.simulate(q, n, tw, u, mode, trials, rng)))
    keys = ("E1", "E2", "E1_p95", "E2_p95", "s", "realised_u")
    out = {k: float(np.mean([a[k] for a in acc])) for k in keys}
    best = min(out["E1"], out["E2"])
    out["lam_star"] = best / out["s"] if out["s"] > 0 else float("nan")
    out["lam_star_p1"] = out["E1"] / out["s"] if out["s"] > 0 else float("nan")
    out["best_of_p1p2"] = "P1" if out["E1"] <= out["E2"] else "P2"
    out["holdings"] = len(acc)
    return out


def twin_groups(base, products, k):
    return pi.add_twins(base, products, k, np.random.default_rng(pi.SEED + k))


def twin_share(groups, holding):
    q, n, tw = pi.holding_arrays(groups, holding)
    return float(n[tw].sum() / n.sum()) if n.sum() else 0.0


def experiment_grid(rng, trials=TRIALS):
    ch = cr.build_refinery()
    base = pi.groups_from_chain(ch)
    full = frozenset(ch.products)
    sets = {"full7": [full], "pairs": pair_holdings(ch)}
    rows = []
    for k in TWIN_COUNTS:
        g = twin_groups(base, ch.products, k) if k else base
        t = twin_share(g, full)
        for hname, hs in sets.items():
            for mode in MODES:
                for u in U_GRID:
                    c = run_cell(g, hs, u, mode, trials if hname == "full7" else trials // 4, rng)
                    rows.append({"twin_pairs": k, "twin_share": t, "holding": hname,
                                 "mode": mode, "u": u, **c})
    return rows


def crossover_t(rows, holding, mode, u):
    """Twin share at which E2 passes E1 (linear interpolation)."""
    pts = sorted((r["twin_share"], r["E2"] - r["E1"]) for r in rows
                 if r["holding"] == holding and r["mode"] == mode and r["u"] == u)
    for (t0, d0), (t1, d1) in zip(pts, pts[1:]):
        if d0 <= 0 < d1:
            return t0 + (t1 - t0) * (-d0) / (d1 - d0)
    return None


def u_where_p95_exceeds(rows, tau, holding="full7", mode="flat", twin_pairs=0, pol="E1_p95"):
    pts = sorted((r["u"], r[pol]) for r in rows if r["holding"] == holding
                 and r["mode"] == mode and r["twin_pairs"] == twin_pairs)
    for u, v in pts:
        if v > tau:
            return u
    return None


# ---------------------------------------------------------------------------
# Self-tests -- each able to fail
# ---------------------------------------------------------------------------


def _full():
    ch = cr.build_refinery()
    return ch, pi.groups_from_chain(ch), frozenset(ch.products)


def test_zero_rate_zero_loss():
    ch, g, full = _full()
    c = run_cell(g, [full], 0.0, "flat", 200, np.random.default_rng(1))
    assert c["E1"] == 0 and c["E2"] == 0 and c["s"] == 0, "u=0 has loss"
    return "u = 0: E1 = E2 = 0 and P3 never refuses"


def test_no_twins_p2_exact():
    ch, g, full = _full()
    c = run_cell(g, [full], 0.3, "flat", 500, np.random.default_rng(2))
    assert c["E2"] < 1e-12 and c["E1"] > 0.1, f"E1={c['E1']} E2={c['E2']}"
    return "no twins: P2 loss is 0 and P1 loss is positive (arm A has a winner)"


def test_arm_a_can_fail_both_ways():
    ch, g, full = _full()
    rng = np.random.default_rng(3)
    lo = run_cell(g, [full], 0.2, "flat", 2000, rng)
    hi = run_cell(twin_groups(g, ch.products, 100), [full], 0.2, "flat", 2000, rng)
    assert lo["best_of_p1p2"] == "P2", "P2 should win with no twins"
    assert hi["best_of_p1p2"] == "P1", "P1 should win with many twins"
    return "arm A: P2 wins at 0 twins, P1 wins at 100 twins (it can lose either way)"


def test_arm_b_can_fail_both_ways():
    ch, g, full = _full()
    c = run_cell(g, [full], 0.2, "flat", 2000, np.random.default_rng(4))
    assert c["lam_star"] == 0, "no twins: P2 exact, P3 cannot beat the best of P1/P2"
    assert p3_wins(c, 0.1, "P1"), "P3 should beat P1 when a missing figure costs little"
    assert not p3_wins(c, 5.0, "P1"), "P3 should lose to P1 when a missing figure costs 5x"
    assert 0.1 < c["lam_star_p1"] < 5.0
    g2 = twin_groups(g, ch.products, 100)
    c2 = run_cell(g2, [full], 0.2, "flat", 2000, np.random.default_rng(14))
    assert p3_wins(c2, 0.005) and not p3_wins(c2, 5.0), "with twins, arm B vs best must flip"
    return (f"arm B: vs P1, P3 wins at lambda 0.1 and loses at 5 (lambda*_P1 = "
            f"{c['lam_star_p1']:.3f}); vs best-of, lambda* = 0 with no twins (entailed)")


def test_lambda_star_is_the_boundary():
    ch, g, full = _full()
    c = run_cell(g, [full], 0.1, "flat", 2000, np.random.default_rng(5))
    l = c["lam_star_p1"]
    assert p3_wins(c, l * 0.99, "P1") and not p3_wins(c, l * 1.01, "P1"), "lambda* is not the switch point"
    return "P3 wins just below lambda* and loses just above it"


def test_matches_old_run():
    ch, g, full = _full()
    c = run_cell(g, [full], 0.1, "flat", 20000, np.random.default_rng(6))
    assert abs(c["E1"] - 0.259) < 0.01, f"E1 {c['E1']:.3f} vs published 0.259"
    assert abs(c["s"] - 0.768) < 0.01, f"s {c['s']:.3f} vs published 0.768"
    return "ties to RESULTS.md: refinery u = 0.1 P1 excess 0.259, P3 unreportable 0.768"


def test_heterogeneity_cannot_lower_refusal():
    """1 - prod (1-p_g)^n_g: ln(1-p) is concave, so at a fixed mean p uneven
    resolution gives a LARGER refusal share than flat (Jensen)."""
    ch, g, full = _full()
    rng = np.random.default_rng(7)
    f = run_cell(g, [full], 0.1, "flat", 20000, rng)["s"]
    for m in ("big_dark", "small_dark"):
        s = run_cell(g, [full], 0.1, m, 20000, rng)["s"]
        assert s >= f - 0.01, f"{m}: refusal {s:.3f} below flat {f:.3f}"
    return "at equal mean u, uneven resolution never lowers P3's refusal share (Jensen)"


def test_old_threshold_was_unreachable_and_new_is_not():
    ch, g, full = _full()
    naive_buyer = pi.exact(*pi.holding_arrays(g, full))
    ratio = naive_buyer[1] / naive_buyer[0]
    rng = np.random.default_rng(8)
    worst = 0.0
    for u in (0.1, 0.5, 1.0):
        q, n, tw = pi.holding_arrays(g, full)
        r = pi.simulate(q, n, tw, u, "flat", 3000, rng)
        worst = max(worst, float((r["p1"] / r["truth"]).max()))
    assert worst <= ratio + 1e-9, "P1 exceeded the naive sum -- old arm was reachable"
    return (f"control: P1 worst {worst:.3f}x never passes the naive {ratio:.3f}x "
            "(the old arm), so it is excluded")


TESTS = [test_zero_rate_zero_loss, test_no_twins_p2_exact,
         test_arm_a_can_fail_both_ways, test_arm_b_can_fail_both_ways,
         test_lambda_star_is_the_boundary, test_matches_old_run,
         test_heterogeneity_cannot_lower_refusal,
         test_old_threshold_was_unreachable_and_new_is_not]


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--csv", default=os.path.join(_HERE, "threshold_s7.csv"))
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)
    rng = np.random.default_rng(SEED)
    rows = experiment_grid(rng)
    keys = sorted({k for r in rows for k in r})
    with open(a.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    f = lambda x: "-" if x is None else f"{x:.3f}"
    print("\nARM B: break-even lambda* and refusal share s (no twins)")
    print(f"  {'holding':8}{'mode':12}{'u':>6}{'E1':>8}{'E1_p95':>8}{'s':>8}{'lam*_P1':>9}")
    for r in rows:
        if r["twin_pairs"] == 0:
            print(f"  {r['holding']:8}{r['mode']:12}{r['u']:>6}{r['E1']:>8.3f}"
                  f"{r['E1_p95']:>8.3f}{r['s']:>8.3f}{r['lam_star_p1']:>9.3f}")
    print("\nARM A: crossover twin share t* where P2 loses to P1")
    for h in ("full7", "pairs"):
        for m in MODES:
            print(f"  {h:6}{m:12}" + "  ".join(
                f"u={u}: {f(crossover_t(rows, h, m, u))}" for u in U_GRID))
    print("\nWith twins (full7, flat): E1, E2, s, lam*")
    for r in rows:
        if r["holding"] == "full7" and r["mode"] == "flat" and r["u"] in (0.1, 0.3):
            print(f"  twins={r['twin_pairs']:>3} t={r['twin_share']:.2f} u={r['u']} "
                  f"E1={r['E1']:.3f} E2={r['E2']:.3f} s={r['s']:.3f} lam*_best={r['lam_star']:.3f} lam*_P1={r['lam_star_p1']:.3f}")
    print("\nu at which P1's 95th-percentile error first exceeds tau (full7, flat, no twins)")
    for tau in (0.25, 0.5, 1.0):
        print(f"  tau={tau}: u={u_where_p95_exceeds(rows, tau)}")
    print(f"\n  wrote {a.csv} ({len(rows)} rows)")
    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
