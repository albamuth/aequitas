#!/usr/bin/env python3
"""
Q1b -- CAN THE LABOUR ACTUALLY BE STAFFED?  A strict-hours recomputation of
Q1's labour row.

WHY THIS EXISTS
---------------
Q1_AUTARKY.md published a labour row of 3,647 h/yr available against a
1,600 h/yr footprint -- ratio 2.28, "room" -- and the project quoted it as
"labour was never the constraint".

On 2026-08-27 @alfred-pennyworth (c23625 on 1f916.ai post #2466) showed the
row cannot fail:

    "One does not lay cable with sleepers. Credited hours are a convention in
     a ratio's clothes: credit ten hours a day to every living person and
     3,647/1,600 cannot bind, however the world is staffed."

The numerator is CREDITED hours. Credited hours include the self-care floor
F, and F is a value the trust network sets by rule (Foundations 7.5.1). So
the pass condition is fixed the moment F is chosen, before a single worker is
counted. Set F = 10 h/day and the pool exceeds any productive requirement in
any world. Sleeping is credited work under 6.1b and it cannot lay cable.

Author ruling 2026-08-27: STRIKE the credited-hours ratio, and run this.

WHAT THIS COMPUTES INSTEAD
--------------------------
Deployable hours only -- hours a human could actually spend producing:

    deployable h/capita = working_age_share * participation * hours_per_worker

against the labour a median lifestyle commands. Both operands are swept
across defensible bands, and the question is whether the ratio crosses 1.0
anywhere inside them.

THIS ROW CAN FAIL. That is the point of it.

TYPE: physical feasibility envelope, same family as q1_autarky.py.
NOT a forecast. It answers "is there a staffing configuration that works",
never "will this happen".

SOURCES
-------
  working-age share   US 15-64 is ~65% and falling with ageing. Band 0.60-0.68.
  participation       US LFPR ~62-63%; wartime peaks reached ~0.85 of the
                      working-age population. Band 0.62-0.85.
  hours per worker    US average ~1,750 h/yr (OECD). Band 1,600-2,080
                      (2,080 = 40 h x 52 wk, a full-time year with no leave).
  footprint           1,380 h/yr measured -- 06-simulation/median-lifestyle/
                      MEDIAN_LIFESTYLE_RESULT.md. Q1 used 1,600; both are run.
  peer efficiency     Q6.md: Germany/Sweden/France/Japan deliver a comparable
                      or better standard at ~55-67% of US labour. 0.65 used.

Run:      python q1b_deployable_labour.py
Tests:    python q1b_deployable_labour.py --test
"""

from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass

W = 78


@dataclass(frozen=True)
class Band:
    """A swept parameter: low, central, high."""
    lo: float
    mid: float
    hi: float

    def points(self):
        return (self.lo, self.mid, self.hi)


@dataclass(frozen=True)
class DeployableParams:
    # --- the three staffing dials, each a band ---
    working_age_share: Band = Band(0.60, 0.65, 0.68)
    participation: Band = Band(0.62, 0.72, 0.85)
    hours_per_worker: Band = Band(1_600.0, 1_750.0, 2_080.0)

    # --- what a median lifestyle commands, h/yr ---
    fp_measured_us: float = 1_380.0     # median-lifestyle, measured
    fp_q1_anchor: float = 1_600.0       # the figure Q1_AUTARKY.md still runs
    peer_efficiency: float = 0.65       # Q6: peers at ~55-67% of US labour

    # --- the withdrawn row, kept only to reproduce and refute it ---
    credited_available: float = 3_647.0
    credited_footprint: float = 1_600.0


def deployable(share: float, part: float, hours: float) -> float:
    """Hours per head of TOTAL population that could actually be worked."""
    return share * part * hours


def sweep(p: DeployableParams, footprint: float):
    """Every corner of the three bands against one footprint."""
    rows = []
    for share, part, hours in itertools.product(
            p.working_age_share.points(),
            p.participation.points(),
            p.hours_per_worker.points()):
        h = deployable(share, part, hours)
        rows.append({
            "share": share, "part": part, "hours": hours,
            "deployable_h": h, "ratio": h / footprint,
        })
    rows.sort(key=lambda r: r["ratio"])
    return rows


def summarise(rows):
    lo, hi = rows[0], rows[-1]
    crosses = any(r["ratio"] >= 1.0 for r in rows)
    share_over = sum(1 for r in rows if r["ratio"] >= 1.0) / len(rows)
    return {
        "min_ratio": lo["ratio"], "max_ratio": hi["ratio"],
        "min_case": lo, "max_case": hi,
        "crosses_one": crosses, "fraction_over_one": share_over,
        "n": len(rows),
    }


def compute(p: DeployableParams | None = None):
    p = p or DeployableParams()
    out = {}
    for name, fp in (
            ("US efficiency, measured footprint (1,380 h)", p.fp_measured_us),
            ("US efficiency, Q1's anchor (1,600 h)", p.fp_q1_anchor),
            ("peer efficiency, measured footprint", p.fp_measured_us * p.peer_efficiency),
            ("peer efficiency, Q1's anchor", p.fp_q1_anchor * p.peer_efficiency),
    ):
        out[name] = {"footprint_h": fp, **summarise(sweep(p, fp))}
    out["_params"] = p
    return out


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def report():
    p = DeployableParams()
    r = compute(p)

    print("=" * W)
    print("Q1b -- DEPLOYABLE LABOUR: can the hours actually be staffed?")
    print("=" * W)

    print("\nTHE ROW THIS REPLACES, AND WHY IT WAS WITHDRAWN")
    print("-" * W)
    print(f"  Q1_AUTARKY.md published : {p.credited_available:,.0f} h/yr available"
          f"  /  {p.credited_footprint:,.0f} h/yr footprint"
          f"  = {p.credited_available / p.credited_footprint:.2f}")
    print("  The numerator is CREDITED hours. Credited hours include the self-care")
    print("  floor F, and F is set by rule (Foundations 7.5.1). The pass condition is")
    print("  fixed when F is chosen, before any worker is counted.")
    print("  -> The row cannot fail, so it was never evidence. Withdrawn.")

    print("\nDEPLOYABLE HOURS PER HEAD OF POPULATION")
    print("-" * W)
    print("  deployable = working_age_share x participation x hours_per_worker")
    print(f"  working_age_share  {p.working_age_share.lo:.2f} .. {p.working_age_share.hi:.2f}")
    print(f"  participation      {p.participation.lo:.2f} .. {p.participation.hi:.2f}")
    print(f"  hours_per_worker   {p.hours_per_worker.lo:,.0f} .. {p.hours_per_worker.hi:,.0f}")
    lo = deployable(p.working_age_share.lo, p.participation.lo, p.hours_per_worker.lo)
    hi = deployable(p.working_age_share.hi, p.participation.hi, p.hours_per_worker.hi)
    print(f"  -> {lo:,.0f} to {hi:,.0f} h/yr per head "
          f"({27} corner cases swept)")

    print("\nRATIO OF DEPLOYABLE HOURS TO WHAT A MEDIAN LIFESTYLE COMMANDS")
    print("-" * W)
    print(f"  {'case':<44}{'footprint':>10}{'ratio band':>16}{'>=1?':>7}")
    for name, v in r.items():
        if name.startswith("_"):
            continue
        band = f"{v['min_ratio']:.2f} - {v['max_ratio']:.2f}"
        mark = "YES" if v["crosses_one"] else "NO"
        print(f"  {name:<44}{v['footprint_h']:>9,.0f}h{band:>16}{mark:>7}")

    print("\nWHAT THIS SAYS")
    print("-" * W)
    us = r["US efficiency, measured footprint (1,380 h)"]
    peer = r["peer efficiency, measured footprint"]
    if not us["crosses_one"]:
        print("  * At US production efficiency the ratio NEVER reaches 1.0, at any")
        print("    corner of the three bands -- including full-time hours for 85% of")
        print("    every working-age adult. Deployable labour DOES bind.")
        print(f"    Best case {us['max_ratio']:.2f}: "
              f"share {us['max_case']['share']:.2f}, "
              f"participation {us['max_case']['part']:.2f}, "
              f"{us['max_case']['hours']:,.0f} h/worker.")
    if peer["crosses_one"]:
        print(f"  * At peer-country efficiency ({p.peer_efficiency:.0%} of US labour per unit")
        print(f"    of standard) it clears in {peer['fraction_over_one']:.0%} of the swept cases.")
    print()
    print("  So the honest claim is NOT 'labour was never the constraint'.")
    print("  It is: THE CONSTRAINT IS PRODUCTION EFFICIENCY, AND AT US EFFICIENCY")
    print("  THE HOURS DO NOT CLOSE.")
    print()
    print("  This AGREES with Q6.md, which already found a US-efficiency median")
    print("  standard for 8.1B people needs ~10.4 T labour-h/yr against ~6.5 T")
    print("  available -- 'impossible without a ~50-58 h workweek' -- while")
    print("  Germany/Sweden/Japan efficiency reaches break-even.")
    print("  The contradiction was between Q1's row and Q6, and Q6 was right.")

    print("\nWHAT DOES NOT CHANGE")
    print("-" * W)
    print("  q1_autarky.py's headline stands on its other rows: an autarkic US is")
    print("  bound by the energy transition and critical minerals. Energy binds at")
    print("  0.19 of the current build. That was always the tighter constraint and")
    print("  it does not depend on any labour figure.")
    print("=" * W)
    return r


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------

def test_row_can_fail():
    """The whole point: unlike the withdrawn row, this one has a failing state."""
    p = DeployableParams()
    # A world that cannot staff itself must produce a ratio below 1.
    starved = sweep(p, footprint=10_000.0)
    assert all(r["ratio"] < 1.0 for r in starved), "an impossible footprint must fail"
    # A world that trivially can must produce one above 1.
    easy = sweep(p, footprint=100.0)
    assert all(r["ratio"] > 1.0 for r in easy), "a trivial footprint must pass"
    print("[ok] the row has both a passing and a failing state -- it is an instrument")


def test_no_credited_hours_anywhere():
    """Self-care must not appear in the numerator, at any corner."""
    p = DeployableParams()
    hi = deployable(p.working_age_share.hi, p.participation.hi, p.hours_per_worker.hi)
    assert hi < 3_650.0, "deployable hours must stay far below the self-care floor pool"
    print(f"[ok] max deployable {hi:,.0f} h/yr -- no self-care credit in the numerator")


def test_us_efficiency_binds():
    r = compute()
    us = r["US efficiency, measured footprint (1,380 h)"]
    assert not us["crosses_one"], "expected US efficiency to bind across the whole band"
    print(f"[ok] US efficiency ratio band {us['min_ratio']:.2f}-{us['max_ratio']:.2f} "
          f"-- never reaches 1.0")


def test_peer_efficiency_relieves():
    r = compute()
    peer = r["peer efficiency, measured footprint"]
    assert peer["crosses_one"], "peer efficiency should reach 1.0 somewhere in the band"
    print(f"[ok] peer efficiency ratio band {peer['min_ratio']:.2f}-{peer['max_ratio']:.2f} "
          f"-- clears in {peer['fraction_over_one']:.0%} of cases")


def test_direction_of_the_old_error():
    """The withdrawn row was flattering, not merely wrong. Show by how much."""
    p = DeployableParams()
    old = p.credited_available / p.credited_footprint
    new = compute()["US efficiency, Q1's anchor (1,600 h)"]["max_ratio"]
    assert old > new, "the withdrawn row must be the more flattering one"
    print(f"[ok] withdrawn row {old:.2f} vs strict best case {new:.2f} "
          f"-- overstated by {old / new:.1f}x, in the flattering direction")


def run_tests():
    test_row_can_fail()
    test_no_credited_hours_anywhere()
    test_us_efficiency_binds()
    test_peer_efficiency_relieves()
    test_direction_of_the_old_error()
    print("\nAll self-tests passed.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="run self-tests only")
    a = ap.parse_args()
    if a.test:
        run_tests()
    else:
        report()
