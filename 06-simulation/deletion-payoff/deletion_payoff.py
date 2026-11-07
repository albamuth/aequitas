#!/usr/bin/env python3
"""
deletion_payoff.py -- does deleting a year of declared span pay, across the conforming band?

Request sr-20260914-sweep-rho-f-across-the-conforming-band-f-fro (filed 2026-09-14).
Extends ../stable-band (rho*(F) comes from its kernel; nothing there is changed).

THE ARITHMETIC (Foundations 4.4, condition 3)
    Slack = rho*(C + P) - D.   A declared year gives the filer
        credit  F*365 h      (floor credit, proof of life)
        debit   d h          (a year of consumption; the median anchor is 1,380)
    Deleting that year removes both.  P is untouched.  So per year deleted:
        gate gain = d - rho*F*365
    It is positive exactly when rho*F < d/365 (3.78 h/day at d = 1,380).

WHAT IS SWEPT
    F    1 .. 14 h/day, step 0.5
    rho  from the affordability floor E/(365 F) up to rho*(F), 200 steps per F
    E    four baskets: narrow 516/655 h, broad 826/965 h   (essentials-basket)
    CAP  physical capacity / wants: 0.70, 0.85 (published), 0.95
    d    the filer's yearly debit in the deleted year: 690, 1162, 1296, 1380, 2760
         (the economy's anchor stays 1,380 unless --anchor says otherwise)

Run:  python deletion_payoff.py            (full sweep, writes sweep_cells.csv + sweep_summary.json)
      python deletion_payoff.py --test     (self-tests)
Seed: population seed 7 (stable_band.RNG_SEED). No other randomness.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(os.path.dirname(HERE), "stable-band")
sys.path.insert(0, SB)

import stable_band as sb                      # noqa: E402
import stable_band_cumulative as sc           # noqa: E402

ANCHOR = 1380.0
FLOORS = np.arange(1.0, 14.01, 0.5)
BASKETS = {"narrow_lo": 516.0, "narrow_hi": 655.0, "broad_lo": 826.0, "broad_hi": 965.0}
CAPS = (0.70, 0.85, 0.95)
D_FILER = (690.0, 1162.0, 1296.0, 1380.0, 2760.0)
RHO_STEPS = 200


# ---------------------------------------------------------------- arithmetic

def gate_gain(rho, F, d):
    """Change in slack rho*(C+P)-D from deleting one declared year (P = 0 and unchanged)."""
    return d - rho * F * 365.0


def ledger_slack(years, rho, P=0.0):
    """Explicit ledger: years = list of (credit_h, debit_h). Slack = rho*(C+P) - D."""
    C = sum(c for c, _ in years)
    D = sum(d for _, d in years)
    return rho * (C + P) - D


def stat_change(F, span_years, work_hours_total, deleted_credit_per_day=None):
    """Change in the published credit-per-day statistic when one year is deleted.

    The filer lived span_years, credited F/day every day plus work_hours_total once.
    The deleted year is a floor-only year unless deleted_credit_per_day is given.
    """
    days = span_years * 365.0
    C = F * days + work_hours_total
    before = C / days
    dc = F if deleted_credit_per_day is None else deleted_credit_per_day
    after = (C - dc * 365.0) / (days - 365.0)
    return after - before


# ---------------------------------------------------------------- rho*(F)

def rho_star_grid(cap, anchor=ANCHOR, floors=FLOORS):
    w, x = sb.build_people(sb.N, seed=sb.RNG_SEED)
    R = cap * x.sum()
    kappa = anchor / 365.0
    out = {}
    for F in floors:
        v, flag = sc.edge_one_day(w, x, float(F), kappa, R)
        out[float(F)] = (float(v), flag)
    return out


# ---------------------------------------------------------------- the sweep

def sweep_one(rstar, E, d):
    """rstar: {F:(value, flag)}. Returns per-F rows and area shares for basket E, filer debit d."""
    rows = []
    cells_total = cells_pay = 0
    for F, (up, flag) in rstar.items():
        lo = E / (365.0 * F)
        if lo >= up:
            rows.append(dict(F=F, lo=lo, up=up, flag=flag, open=False, cells=0, pay=0,
                             gain_lo=None, gain_up=None, breakeven=d / (365.0 * F)))
            continue
        rhos = np.linspace(lo, up, RHO_STEPS)
        g = gate_gain(rhos, F, d)
        n_pay = int((g > 0).sum())
        cells_total += RHO_STEPS
        cells_pay += n_pay
        rows.append(dict(F=F, lo=lo, up=up, flag=flag, open=True, cells=RHO_STEPS, pay=n_pay,
                         gain_lo=float(g[0]), gain_up=float(g[-1]), breakeven=d / (365.0 * F)))
    open_rows = [r for r in rows if r["open"]]
    # area share: weight each F by its band width (rho units)
    wsum = sum(r["up"] - r["lo"] for r in open_rows)
    wpay = sum(max(0.0, min(r["up"], r["breakeven"]) - r["lo"]) for r in open_rows)
    return dict(
        rows=rows,
        open_floors=len(open_rows),
        all_floors=len(rows),
        cell_share=(cells_pay / cells_total) if cells_total else float("nan"),
        width_share=(wpay / wsum) if wsum else float("nan"),
        floors_fully_paying=sum(1 for r in open_rows if r["pay"] == r["cells"]),
        floors_never_paying=sum(1 for r in open_rows if r["pay"] == 0),
    )


# ---------------------------------------------------------------- self-tests

def test_foundations_worked_rows():
    # 4.4: F=10, rho=1.2 -> an honest year is +3000, so deleting it is -3000;
    #      F=2, rho=1.0 -> honest year -650, deleting it is +650.
    assert abs(gate_gain(1.2, 10, 1380) - (-3000.0)) < 1e-9
    assert abs(gate_gain(1.0, 2, 1380) - 650.0) < 1e-9
    print("[ok] reproduces Foundations 4.4 rows: -3000 h at (10, 1.2), +650 h at (2, 1.0)")


def test_closed_form_matches_explicit_ledger():
    # Build a 40-year ledger, delete year 3 as an explicit event-log edit, compare slacks.
    for F, rho, d in ((10, 1.2, 1380), (2, 1.0, 1380), (6, 0.5, 900), (14, 0.25, 2760)):
        years = [(F * 365.0, d)] * 40
        before = ledger_slack(years, rho)
        after = ledger_slack(years[:2] + years[3:], rho)
        assert abs((after - before) - gate_gain(rho, F, d)) < 1e-6, (F, rho, d)
    print("[ok] closed form = explicit 40-year ledger with one year removed (4 settings)")


def test_sign_flips_at_breakeven():
    for F in (2.0, 5.0, 10.0, 14.0):
        r0 = ANCHOR / (365.0 * F)
        assert abs(gate_gain(r0, F, ANCHOR)) < 1e-9
        assert gate_gain(r0 * 0.99, F, ANCHOR) > 0 > gate_gain(r0 * 1.01, F, ANCHOR)
    print("[ok] gain is 0 at rho = d/(365 F), positive below, negative above")


def test_rho_star_reproduces_published_edges():
    rs = rho_star_grid(0.85, floors=[2.0, 10.0, 14.0])
    for F, pub in ((2.0, 1.017), (10.0, 0.330), (14.0, 0.253)):
        assert abs(rs[F][0] - pub) < 0.005, (F, rs[F], pub)
    print("[ok] rho* at F=2,10,14 = " + ", ".join(f"{rs[F][0]:.3f}" for F in (2.0, 10.0, 14.0))
          + "  (published 1.017 / 0.330 / 0.253)")


def test_share_is_not_forced_to_one():
    # A made-up economy whose edge sits ABOVE break-even must give a share < 1.
    fake = {10.0: (0.60, ""), 12.0: (0.60, "")}
    r = sweep_one(fake, 826.0, ANCHOR)
    assert r["width_share"] < 0.99, r["width_share"]
    # and one wholly below must give exactly 1
    fake2 = {10.0: (0.30, ""), 12.0: (0.25, "")}
    assert abs(sweep_one(fake2, 826.0, ANCHOR)["width_share"] - 1.0) < 1e-9
    print("[ok] the share can come out below 1 (0.60 edge at F=10 gives "
          f"{sweep_one({10.0: (0.60, '')}, 826.0, ANCHOR)['width_share']:.3f})")


def test_stat_zero_for_floor_only_and_positive_for_worker():
    assert abs(stat_change(10, 40, 0.0)) < 1e-12
    assert stat_change(10, 40, 50_000.0) > 0
    # deleting a worked year (credit above average) lowers the statistic
    assert stat_change(10, 40, 50_000.0, deleted_credit_per_day=24.0) < 0
    print("[ok] statistic: floor-only filer 0.000, worker +, deleting a 24 h/day year -")


def test_ceiling_survives_deletion():
    # 24/F ceiling: a 24 h/day filer deleting any year stays at 24 per day; a floor-only
    # filer stays at F.  Ratio stays 24/F.
    F = 10.0
    top = 24.0 + stat_change(F, 40, (24 - F) * 365.0 * 40, deleted_credit_per_day=24.0)
    bot = F + stat_change(F, 40, 0.0)
    assert abs(top / bot - 24.0 / F) < 1e-9, (top, bot)
    print(f"[ok] 24/F holds under deletion: {top:.3f} / {bot:.3f} = {top/bot:.3f}")


def test_edge_scales_with_anchor():
    a = rho_star_grid(0.85, 1380.0, [10.0])[10.0][0]
    b = rho_star_grid(0.85, 1162.0, [10.0])[10.0][0]
    assert abs(b - a * 1162.0 / 1380.0) < 0.01, (a, b)
    print(f"[ok] rho*(10) scales with the economy's anchor: {a:.3f} -> {b:.3f} (x{1162/1380:.3f})")


def run_tests():
    for fn in (test_foundations_worked_rows, test_closed_form_matches_explicit_ledger,
               test_sign_flips_at_breakeven, test_share_is_not_forced_to_one,
               test_stat_zero_for_floor_only_and_positive_for_worker, test_ceiling_survives_deletion,
               test_rho_star_reproduces_published_edges, test_edge_scales_with_anchor):
        fn()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return

    summary = {"anchor": ANCHOR, "seed": sb.RNG_SEED, "n": sb.N, "caps": {}}
    cells_out = []
    for cap in CAPS:
        rs = rho_star_grid(cap)
        summary["caps"][str(cap)] = {"rho_star": {str(F): v for F, v in rs.items()}, "tables": {}}
        print(f"\n=== CAP {cap}  rho*(F) (value, flag) ===")
        print("  " + "  ".join(f"F{F:g}:{v:.3f}{'*' if fl else ''}" for F, (v, fl) in rs.items()))
        print("  E_max = 365 F rho*: " + "  ".join(f"F{F:g}:{365*F*v:,.0f}" for F, (v, fl) in rs.items()))
        for bname, E in BASKETS.items():
            for d in D_FILER:
                r = sweep_one(rs, E, d)
                summary["caps"][str(cap)]["tables"][f"{bname}|d={d:g}"] = {
                    k: r[k] for k in ("open_floors", "all_floors", "cell_share", "width_share",
                                      "floors_fully_paying", "floors_never_paying")}
                for row in r["rows"]:
                    cells_out.append([cap, bname, E, d, row["F"], round(row["lo"], 4), round(row["up"], 4),
                                      row["flag"], int(row["open"]), row["cells"], row["pay"],
                                      round(row["breakeven"], 4),
                                      "" if row["gain_lo"] is None else round(row["gain_lo"], 1),
                                      "" if row["gain_up"] is None else round(row["gain_up"], 1)])
                print(f"  CAP {cap} {bname:<10} d={d:>6g}: open F {r['open_floors']}/{r['all_floors']}, "
                      f"cells paying {r['cell_share']:.3f}, width-weighted {r['width_share']:.3f}, "
                      f"F fully paying {r['floors_fully_paying']}, never {r['floors_never_paying']}")

    # headline per-F table (published CAP, broad_lo, d = anchor)
    rs = {float(k): tuple(v) for k, v in summary["caps"]["0.85"]["rho_star"].items()}
    print("\n=== per-F detail: CAP 0.85, broad_lo (826 h), d = 1,380 ===")
    print(f"{'F':>5} {'lo':>7} {'rho*':>7} {'break-even':>10} {'gain@lo':>9} {'gain@rho*':>10}")
    for row in sweep_one(rs, 826.0, ANCHOR)["rows"]:
        if row["open"]:
            print(f"{row['F']:>5g} {row['lo']:>7.3f} {row['up']:>7.3f} {row['breakeven']:>10.3f} "
                  f"{row['gain_lo']:>9.0f} {row['gain_up']:>10.0f}")
        else:
            print(f"{row['F']:>5g} {row['lo']:>7.3f} {row['up']:>7.3f} {row['breakeven']:>10.3f}   band closed")

    # statistic side
    print("\n=== credit-per-day statistic, one floor-only year deleted (h/day change) ===")
    for F in (2.0, 10.0, 14.0):
        for span, W in ((40, 0.0), (40, 20_000.0), (40, 50_000.0), (60, 100_000.0)):
            print(f"F={F:g} span {span} y, work {W:>9,.0f} h: {stat_change(F, span, W):+.4f} h/day "
                  f"(from {(F*span*365+W)/(span*365):.3f})")

    with open(os.path.join(HERE, "sweep_cells.csv"), "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["cap", "basket", "E_h", "d_h", "F", "rho_lo", "rho_star", "flag", "open",
                     "cells", "cells_paying", "breakeven_rho", "gain_at_lo_h", "gain_at_rhostar_h"])
        wr.writerows(cells_out)
    with open(os.path.join(HERE, "sweep_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)


if __name__ == "__main__":
    main()
