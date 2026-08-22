"""
q2_capture.py -- Q2 of the scenario suite.

Question (author): what is the impact of exploitation, cronyism, capitalism, and war
on stolen labour-time?

LOUD REFRAME, per the axioms. Aequitas has NO surplus-value and nothing to steal:
credit is non-transferable (A3), so "stolen labour-time" is not an Aequitas quantity.
The honest, computable question is the SIZE of the pool of human hours currently either
  (a) CAPTURED -- their product accrues to non-working asset-holders (distributional), or
  (b) WASTED   -- spent on enforcement/extraction that exists only because money is
      extractable (allocative),
a pool that is STRUCTURALLY IMPOSSIBLE or shrinks to near-zero under Aequitas:
  - capture is dissolved by A3 (credit can't be transferred -> no rentier income),
  - much enforcement evaporates (no rent to guard, no profit to skim, far less
    inequality to police -- §1, §7.5).

We measure two DISTINCT pools (they answer different questions and must NOT be naively
summed -- they overlap; a supervisor is both captured-from and guard-labour):

  POOL A -- CAPTURE (distributional). Capital's share of national income is the fraction
    of the product that accrues to ownership rather than work. Not all of it is
    extraction (imputed owner-occupied housing, the labour part of proprietors' income
    are not), so we take an EXTRACTIVE fraction of it. Expressed as hours = share x
    total employed hours.

  POOL B -- WASTEFUL ALLOCATION. Bowles-Jayadev "guard labour" (supervisors, guards,
    police, prisons, military) is the labour of enforcing an unequal order. Not all of
    it vanishes (genuine public safety, real coordination), so we take a SHRINKABLE
    fraction. War/military is a named SUBSET of guard labour, reported separately, never
    added on top.

DATA ANCHORS (real, cited in-line):
  - Capital share of US national income ~31% (2022; labour ~69%). BEA / Tax Foundation
    (https://taxfoundation.org/blog/labor-share-net-income-within-historical-range/).
  - Guard labour ~19.5% (1950) -> ~29.4% (2017) of the US labour force; ~20% in the
    2007 Bowles-Jayadev estimate. Jayadev & Bowles, "Garrison America" / "Estimating
    Guard Labor" (https://scholarworks.umb.edu/econ_faculty_pubs/6/).
  - US military: ~1.3M active + ~0.75M DoD civilians + defence-industrial employment
    -> ~2.5-3% of the workforce (a guard-labour subset).
  - Total US employed hours ~ 160M jobs x 1,750 h ~ 2.8e11 h/yr (this project, BLS).

Run:  python q2_capture.py
      python q2_capture.py --test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class CaptureParams:
    jobs: float = 160e6
    hours_per_job: float = 1_750.0
    adults: float = 258e6

    # --- POOL A: capture (distributional) ---
    capital_share: float = 0.31            # capital's share of national income (BEA 2022)
    # fraction of capital income that is genuine EXTRACTION (excl. imputed housing,
    # proprietors' own-labour portion). Contestable -> a band.
    extractive_fraction_lo: float = 0.55
    extractive_fraction_hi: float = 0.85

    # --- POOL B: wasteful allocation (guard labour) ---
    guard_labour_share_lo: float = 0.20    # 2007 estimate
    guard_labour_share_hi: float = 0.29    # 2017 estimate
    # fraction of guard labour that SHRINKS under Aequitas (the rest is genuine
    # public safety / coordination). Contestable -> a band.
    shrinkable_fraction_lo: float = 0.40
    shrinkable_fraction_hi: float = 0.70

    # war / military as a named SUBSET of guard labour (reported, not added)
    military_share: float = 0.028


def compute(p: CaptureParams | None = None):
    p = p or CaptureParams()
    total_hours = p.jobs * p.hours_per_job
    per_adult = total_hours / p.adults

    # Pool A -- capture
    capture_lo = p.capital_share * p.extractive_fraction_lo
    capture_hi = p.capital_share * p.extractive_fraction_hi

    # Pool B -- shrinkable guard labour
    waste_lo = p.guard_labour_share_lo * p.shrinkable_fraction_lo
    waste_hi = p.guard_labour_share_hi * p.shrinkable_fraction_hi

    # Combined, DE-DUPLICATED. The two pools overlap (captured supervisors are also
    # guard labour). We do NOT sum them; the honest combined "structurally-dissolved-
    # or-shrunk" band runs from the LARGER single pool (union lower bound) up to a
    # partial-overlap union (~capture + half the non-overlapping waste).
    combined_lo = max(capture_lo, waste_lo)
    combined_hi = capture_hi + 0.5 * waste_hi

    def h(frac):
        return frac * per_adult

    return dict(
        total_hours=total_hours, per_adult=per_adult,
        capture=(capture_lo, capture_hi), waste=(waste_lo, waste_hi),
        military=p.military_share, combined=(combined_lo, combined_hi),
        capture_h=(h(capture_lo), h(capture_hi)),
        waste_h=(h(waste_lo), h(waste_hi)),
        military_h=h(p.military_share),
        combined_h=(h(combined_lo), h(combined_hi)),
        p=p,
    )


def report(p: CaptureParams | None = None):
    p = p or CaptureParams()
    r = compute(p)
    W = 78
    print("=" * W)
    print("Q2 -- labour-time CAPTURED or WASTED (the pool Aequitas dissolves)")
    print("=" * W)
    print("Reframe: A3 makes credit non-transferable, so there is nothing to STEAL.")
    print("We size the pool of hours currently captured or wasted -- impossible under Aequitas.")
    print(f"(productive labour ~{r['per_adult']:,.0f} h/adult/yr; self-care is separate & larger)")
    print("-" * W)
    cl, ch = r["capture"]; clh, chh = r["capture_h"]
    print("POOL A -- CAPTURE (distributional): product accruing to ownership, not work")
    print(f"  capital share {p.capital_share:.0%} x extractive {p.extractive_fraction_lo:.0%}-{p.extractive_fraction_hi:.0%}")
    print(f"  = {cl:.0%}-{ch:.0%} of labour  =  {clh:,.0f}-{chh:,.0f} h/adult/yr")
    print(f"  -> dissolved by A3: credit can't be transferred, so no rentier income exists")
    wl, wh = r["waste"]; wlh, whh = r["waste_h"]
    print("\nPOOL B -- WASTEFUL ALLOCATION (guard labour that shrinks under Aequitas)")
    print(f"  guard labour {p.guard_labour_share_lo:.0%}-{p.guard_labour_share_hi:.0%} x shrinkable "
          f"{p.shrinkable_fraction_lo:.0%}-{p.shrinkable_fraction_hi:.0%}")
    print(f"  = {wl:.0%}-{wh:.0%} of labour  =  {wlh:,.0f}-{whh:,.0f} h/adult/yr")
    print(f"  (war/military = {r['military']:.1%}, ~{r['military_h']:,.0f} h/adult -- a SUBSET, not added)")
    print(f"  -> shrinks: no rent to guard, no profit to skim, far less inequality to police")
    print("-" * W)
    cbl, cbh = r["combined"]; cblh, cbhh = r["combined_h"]
    print(f"COMBINED (de-duplicated, pools overlap): {cbl:.0%}-{cbh:.0%} of productive labour")
    print(f"  = {cblh:,.0f}-{cbhh:,.0f} h/adult/yr freed")
    print("=" * W)
    print("Headline: roughly a FIFTH to well over a THIRD of productive labour-time is")
    print("captured by ownership or spent enforcing/extracting -- a pool that under")
    print("Aequitas is structurally impossible (A3) or withers (no profit, less to police).")
    print("This is what feeds Q5's reallocation to essentials.")
    print("=" * W)
    return r


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------

def test_capture_below_capital_share():
    r = compute()
    assert r["capture"][1] <= CaptureParams().capital_share + 1e-9, "capture can't exceed capital share"
    print(f"[ok] capture {r['capture'][0]:.0%}-{r['capture'][1]:.0%} <= capital share 31%")


def test_waste_below_guard_labour():
    r = compute()
    assert r["waste"][1] <= CaptureParams().guard_labour_share_hi, "shrinkable can't exceed guard labour"
    print(f"[ok] shrinkable waste {r['waste'][0]:.0%}-{r['waste'][1]:.0%} <= guard labour 29%")


def test_military_is_subset():
    r = compute()
    assert r["military"] < CaptureParams().guard_labour_share_lo, "military must be a subset of guard labour"
    print(f"[ok] military {r['military']:.1%} is a subset of guard labour (not added)")


def test_combined_deduplicated():
    """Combined must be LESS than a naive sum of the two pools (they overlap)."""
    r = compute()
    naive = r["capture"][1] + r["waste"][1]
    assert r["combined"][1] < naive, "combined should be de-duplicated below the naive sum"
    print(f"[ok] combined hi {r['combined'][1]:.0%} < naive sum {naive:.0%} (de-duplicated)")


def test_combined_plausible():
    r = compute()
    assert 0.12 < r["combined"][0] < r["combined"][1] < 0.55, "combined band should be ~a fifth to a third"
    print(f"[ok] combined {r['combined'][0]:.0%}-{r['combined'][1]:.0%} of productive labour (a fifth to a third)")


def run_tests():
    test_capture_below_capital_share()
    test_waste_below_guard_labour()
    test_military_is_subset()
    test_combined_deduplicated()
    test_combined_plausible()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
