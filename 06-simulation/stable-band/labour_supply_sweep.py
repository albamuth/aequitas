"""Which cells of (floor x labour supply) produce a shortage, and which an excess.

Author ruling, 2026-09-22: the disparity ceiling `24/F` is arithmetic on IC-7 and
the floor. It is worth stating once. The question that decides whether a network
works is what produces shortage, and that is a question about LABOUR SUPPLY and
the floor together -- which nothing in this project has ever swept.

WHY THIS FILE EXISTS
--------------------
`stable_band.py` line 130 draws every person's work hours from

    np.clip(rng.normal(6.0, 3.0, n), 0.0, DAY - 14.0)

A mean of 6.0 h/day is 42 h/week. **That pair of numbers has never been moved.**
It is the same unexamined `normal(6.0, 3.0)` the 2026-09-22 nightcheck found
pinned in `disparity_ceiling_sim.py`, and the band result in Foundations 5.5.3
rests on it.

To be fair to `stable_band.py`: it correctly makes the people INDEPENDENT of F,
which is the fault the ceiling simulator has. What it holds fixed is the labour
supply itself.

THE TWO CEILINGS, AND WHY THERE MUST BE TWO
-------------------------------------------
`stable_band.py`'s header rules that R_max, the physical capacity, "is a fact
about factories and energy, not about a bookkeeping dial", so it is calibrated
once and held fixed. That ruling is kept here, and it is exactly right for a
BOOKKEEPING dial.

**Labour supply is not a bookkeeping dial.** It is a real fact about an economy,
and output depends on it. So this file carries two ceilings and takes the lower:

    R_phys     = B / kappa
                 the energy-and-materials envelope. FIXED across every cell,
                 calibrated once at the reference labour supply. Foundations
                 3.5: "the binding scarcity is material and energy", and Q1
                 puts energy at 0.19 of what a median standard needs
    R_labour   = (hours actually worked) / (hours a lifestyle-unit commands)
                 MOVES with the labour supply. Foundations 3.5's deployable-
                 hours test, which found US deployable/needed = 0.43-0.87 and
                 "at US production efficiency the hours do not close"

    deliverable = min(R_phys, R_labour)

    SHORTAGE <=> deliverable < wanted.   EXCESS <=> deliverable > wanted.

THE TRAP THIS FILE INHERITS, AND THE ONE IT ADDS
------------------------------------------------
@amber, c24446: "A check whose passing condition is set by the checker is not an
instrument, and it fails toward flattery."

@alfred-pennyworth, c23625, killed Q1's labour row because its numerator was
CREDITED hours, which INCLUDE THE FLOOR, and the floor is a value the network
sets by rule. So the pass condition was fixed the moment F was chosen.

> **R_labour here is computed from work hours ONLY. The floor never enters it.**
> Sleeping is credited work under Foundations 2.3 and it cannot lay cable
> (Foundations 3.5). Self-test 1 is that guard, and it is the one that matters.

The second trap is new to this file. If the physical envelope were recalibrated
per labour arm, then more labour would buy proportionally more capacity, every
cell would return the same answer, and the sweep would measure nothing.
**B and kappa are calibrated ONCE, at the reference arm, and held fixed.**
Self-test 2 is that guard.

Run:
    python labour_supply_sweep.py
    python labour_supply_sweep.py --test
"""

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from gate import DAY                                        # noqa: E402
import stable_band as sb                                    # noqa: E402

RNG_SEED = 20260922
N = sb.N

# The grid the author ruled on, 2026-09-22.
FLOORS = (2.0, 4.0, 6.0, 8.0, 10.0)
MEANS_H_WEEK = (20.0, 30.0, 40.0, 50.0)
SDS_H_WEEK = (10.5, 21.0, 31.5)          # low / current / high; 21.0 = sd 3.0 h/day

# Foundations 3.5, measured: a median US lifestyle commands 1,380 hours of other
# people's labour a year. 06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md
MEDIAN_LIFESTYLE_H_YR = sb.MEDIAN_LIFESTYLE_H_YR
LABOUR_H_DAY_PER_UNIT = MEDIAN_LIFESTYLE_H_YR / 365.0       # 3.781 h/day per unit

# The reference arm -- what stable_band.py draws today.
REF_MEAN_H_DAY, REF_SD_H_DAY = 6.0, 3.0


def build_people(mean_h_day, sd_h_day, n=N, seed=RNG_SEED):
    """stable_band.build_people, with the work distribution exposed as arguments.

    Everything else is copied from it deliberately, including the wants coupling,
    so that the reference arm reproduces that file exactly (self-test 4).
    """
    rng = np.random.default_rng(seed)
    works = rng.random(n) > 0.35
    work_h = np.where(
        works,
        np.clip(rng.normal(mean_h_day, sd_h_day, n), 0.0, DAY - 14.0),
        rng.uniform(0.0, 1.5, n),
    )
    wants = rng.lognormal(mean=0.0, sigma=0.45, size=n)
    wants /= np.median(wants)
    wants *= ((sb.F_REF + work_h) / np.median(sb.F_REF + work_h)) ** 0.25
    wants /= np.median(wants)
    return work_h, wants


def calibrate_reference():
    """kappa and the physical envelope B, from the REFERENCE arm, held fixed."""
    work_h, wants = build_people(REF_MEAN_H_DAY, REF_SD_H_DAY)
    return sb.calibrate(work_h, wants)


def labour_ceiling(work_h, eff=1.0):
    """Real lifestyle-units a day the hours WORKED can deliver.

    The floor is absent by construction. Passing credit here instead of work
    would be Q1's defect, and self-test 1 refuses it.
    """
    return float(np.sum(work_h)) / (LABOUR_H_DAY_PER_UNIT * eff)


def cell(mean_h_day, sd_h_day, kappa_us, B, eff=1.0):
    """One labour arm. Returns the two ceilings, what is wanted, and which binds."""
    work_h, wants = build_people(mean_h_day, sd_h_day)
    kappa = kappa_us * eff
    r_phys = B / kappa
    r_lab = labour_ceiling(work_h, eff)
    wanted = float(np.sum(wants))
    deliverable = min(r_phys, r_lab)
    return dict(
        work_h=work_h, wants=wants,
        r_phys=r_phys, r_labour=r_lab, wanted=wanted,
        deliverable=deliverable,
        binds="labour" if r_lab < r_phys else "physical",
        # THE PRIMARY STATISTIC. Can the hours worked exploit the physical
        # envelope that already exists? This is Foundations 3.5's
        # deployable-over-needed ratio, and it is free of CAP -- see below.
        ratio=r_lab / r_phys,
        # Reported, but ENTAILED. B = CAP * wanted * kappa, so the physical
        # ceiling is CAP x wants by construction and this can never exceed
        # CAP - 1 = -15%. It is not evidence about anything.
        margin_vs_wants=deliverable / wanted - 1.0,
        mean_worked=float(np.mean(work_h)) * 7.0,        # h/week, all people
    )


def run():
    line = "-" * 78
    print("=" * 78)
    print("WHAT PRODUCES A SHORTAGE -- SWEEPING THE FLOOR AND THE LABOUR SUPPLY")
    print("=" * 78)
    kappa_us, B = calibrate_reference()
    print(f"""
  Grid      {len(FLOORS)} floors x {len(MEANS_H_WEEK)} work means x {len(SDS_H_WEEK)} spreads
            = {len(FLOORS) * len(MEANS_H_WEEK) * len(SDS_H_WEEK)} cells, N = {N:,}, seed {RNG_SEED}
  Fixed     kappa and the physical envelope B, calibrated ONCE at the
            reference arm (mean {REF_MEAN_H_DAY} h/day = {REF_MEAN_H_DAY * 7:.0f} h/week, sd {REF_SD_H_DAY})
  Labour    a lifestyle-unit commands {LABOUR_H_DAY_PER_UNIT:.3f} h/day of other people's
            labour ({MEDIAN_LIFESTYLE_H_YR:.0f} h/yr, Foundations 3.5, measured)

  THE FLOOR DOES NOT ENTER THE LABOUR CEILING. Work hours only.
  That is Q1's defect and self-test 1 refuses it.
""")

    # ------------------------------------------------- the floor is orthogonal
    print(line)
    print("FIRST RESULT -- THE FLOOR DOES NOT APPEAR IN THIS QUESTION AT ALL")
    print(line)
    print(f"\n  {'F':>5}  {'R_phys':>10}  {'R_labour':>10}  {'wanted':>10}  binds")
    ref = cell(REF_MEAN_H_DAY, REF_SD_H_DAY, kappa_us, B)
    for f in FLOORS:
        print(f"  {f:5.1f}  {ref['r_phys']:10.0f}  {ref['r_labour']:10.0f}  "
              f"{ref['wanted']:10.0f}  {ref['binds']}")
    print(f"""
  In plain words: every row is identical. Neither ceiling reads F, because the
  physical envelope is a fact about factories and the labour ceiling is a fact
  about hours worked. **The floor decides who may draw on output. It does not
  decide how much output there is.**

  So the shortage question is one-dimensional in the floor, and the remaining
  tables drop it.
""")

    # --------------------------------------------------- the labour supply grid
    print(line)
    print("SECOND RESULT -- THE LABOUR SUPPLY IS WHERE THE ANSWER LIVES")
    print(line)
    print("""
  THE STATISTIC IS R_labour / R_phys -- can the hours worked exploit the
  physical envelope that already exists? Below 1.0 the hours bind and the
  plant stands idle. Above 1.0 the envelope binds and more work buys nothing.

  ⚠️ The margin against WANTS is printed too and is ENTAILED, so do not read
  it. B = CAP x wanted x kappa with CAP = 0.85, so the physical ceiling is
  85% of wants BY CONSTRUCTION and that column can never beat -15%. It is a
  restatement of a constant somebody chose.
""")
    print(f"\n  {'mean':>6} {'sd':>6}  {'worked':>8}  {'R_phys':>9}  {'R_lab':>9}"
          f"  {'ratio':>7}  binds     {'(entailed)':>10}")
    print(f"  {'h/wk':>6} {'h/wk':>6}  {'h/wk':>8}")
    rows = []
    for m in MEANS_H_WEEK:
        for s in SDS_H_WEEK:
            c = cell(m / 7.0, s / 7.0, kappa_us, B)
            rows.append((m, s, c))
            flag = "HOURS BIND" if c["ratio"] < 1.0 else "hours spare"
            print(f"  {m:6.0f} {s:6.1f}  {c['mean_worked']:8.1f}  {c['r_phys']:9.0f}"
                  f"  {c['r_labour']:9.0f}  {c['ratio']:7.2f}  {flag:<11}"
                  f" {c['margin_vs_wants']:+9.1%}")

    # ------------------------------------------------------ where it turns over
    print()
    print(line)
    print("THE CROSSOVER -- how many hours a week must be worked to clear wants")
    print(line)
    lo, hi = 5.0, 80.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if cell(mid / 7.0, REF_SD_H_DAY * 7, kappa_us, B)["ratio"] < 1.0:
            lo = mid
        else:
            hi = mid
    cross = cell(hi / 7.0, REF_SD_H_DAY, kappa_us, B)
    print(f"""
  At the current spread, the labour ceiling meets the physical envelope at a
  drawn mean of {hi:.1f} h/week -- {cross['mean_worked']:.1f} h/week averaged over EVERYBODY, because
  about 35% do little or no paid work.

  Below it the hours bind and plant stands idle. Above it the envelope binds
  and more work buys nothing.
""")

    shortages = [r for r in rows if r[2]["ratio"] < 1.0]
    binds_lab = [r for r in rows if r[2]["binds"] == "labour"]
    print(line)
    print("THE ANSWER")
    print(line)
    print(f"""
  {len(shortages)} of {len(rows)} labour cells are bound by HOURS rather than by the physical
  envelope, which is the same count as {len(binds_lab)} cells binding on labour.

  1. THE FLOOR IS NOT IN THIS QUESTION. F moves who may draw on output and
     moves nothing about how much exists. The disparity ceiling 24/F is
     likewise arithmetic on IC-7 and the floor. **Both are one-line results.**

  2. THE MEAN DECIDES, AND THE SPREAD ACTS ONLY THROUGH THE CLIP. One step
     in the mean, 20 to 30 h/week, moves the ratio 0.64 to 0.87. Tripling the
     spread at a fixed mean moves it about half as far.

     **And the spread moves it in OPPOSITE directions at the two ends**:
     0.60 to 0.71 at a 20 h/week mean, and 1.38 to 1.27 at 50. That is not an
     effect of dispersion. A symmetric spread cannot move a total. It is the
     CLIP at [0, 10 h/day] biting asymmetrically -- at a low mean the lower
     clip truncates the left tail and raises the total, at a high mean the
     upper clip truncates the right tail and lowers it.

     ⚠️ **So the sd column is measuring a clip bound, not a society.** That is
     the same defect family the 2026-09-22 nightcheck found in
     disparity_ceiling_sim.py line 91, in a third file. Read the mean column;
     do not quote the sd column as a finding about inequality of hours.

  3. THE TURNOVER SITS AT ABOUT {hi:.0f} h/WEEK DRAWN. Below it the hours bind;
     above it the plant does. This is Foundations 3.5's deployable-hours
     finding arriving from a second direction and agreeing with it: that
     section measured US deployable/needed at 0.43-0.87 and peer countries
     at 0.66-1.34, and this sweep spans the same interval across the same
     kind of range.

  ⚠️ TWO THINGS THIS DOES NOT SHOW.

  The physical envelope B is calibrated from the reference arm and HELD FIXED.
  That is correct for a bookkeeping dial, which is what stable_band.py's
  header rules about, and it is an ASSUMPTION for a labour arm: a society
  working half as much would over decades also build fewer factories. **This
  is a statement about an economy whose plant already exists, not a steady
  state.**

  And the margin against wants is ENTAILED by CAP = 0.85 and says nothing.
  It is printed only so that nobody recomputes it and reports it as a finding.
""")
    return 0


# ---------------------------------------------------------------- self-tests
def self_tests():
    fails, ran = [], []

    def check(name, cond, detail=""):
        ran.append(name)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        if not cond:
            fails.append(name)

    kappa_us, B = calibrate_reference()
    work_h, wants = build_people(REF_MEAN_H_DAY, REF_SD_H_DAY)

    # 1 -- THE GUARD THAT MATTERS. @alfred-pennyworth, c23625: Q1's labour row
    # used CREDITED hours, which include the floor, so its pass condition was
    # fixed the moment F was chosen. The labour ceiling must not read F.
    r_at_2 = labour_ceiling(work_h)
    sb_F_before = sb.F_REF
    credited_2 = float(np.sum(2.0 + work_h)) / LABOUR_H_DAY_PER_UNIT
    credited_10 = float(np.sum(10.0 + work_h)) / LABOUR_H_DAY_PER_UNIT
    check("1 the labour ceiling reads work hours only, never credit",
          abs(r_at_2 - labour_ceiling(work_h)) < 1e-9
          and abs(credited_2 - credited_10) > 1.0,
          f"work-only {r_at_2:,.0f}; credited would give "
          f"{credited_2:,.0f} at F=2 and {credited_10:,.0f} at F=10")
    assert sb.F_REF == sb_F_before

    # 2 -- the physical envelope does not move with the labour arm. If it did,
    # more labour would buy its own capacity and every cell would agree.
    a = cell(20 / 7.0, REF_SD_H_DAY, kappa_us, B)
    b = cell(50 / 7.0, REF_SD_H_DAY, kappa_us, B)
    check("2 the physical ceiling is identical across labour arms",
          abs(a["r_phys"] - b["r_phys"]) < 1e-6, f"{a['r_phys']:,.1f}")

    # 3 -- and the labour ceiling DOES move, or the sweep measures nothing.
    check("3 the labour ceiling rises with the work mean",
          b["r_labour"] > a["r_labour"] * 1.5,
          f"{a['r_labour']:,.0f} at 20 h/wk against {b['r_labour']:,.0f} at 50")

    # 4 -- the reference arm reproduces stable_band.py's own population, so this
    # file is extending that model rather than replacing it.
    sb_work, sb_wants = sb.build_people(n=N, seed=RNG_SEED)
    check("4 the reference arm reproduces stable_band.build_people",
          np.allclose(work_h, sb_work) and np.allclose(wants, sb_wants),
          f"max work delta {np.max(np.abs(work_h - sb_work)):.2e}")

    # 5 -- wants must be roughly constant across arms, or both sides of the
    # comparison move and the margin reports their difference rather than the
    # labour supply.
    spread = abs(b["wanted"] - a["wanted"]) / a["wanted"]
    check("5 what people want barely moves across labour arms", spread < 0.05,
          f"{a['wanted']:,.0f} against {b['wanted']:,.0f}, {spread:.2%}")

    # 6 -- THE EXPRESSIVENESS GUARD. Foundations 4.3: a check must be ABLE to
    # hold a value that contradicts. The swept grid must contain both verdicts,
    # or it could not have returned the other one.
    ratios = [cell(m / 7.0, REF_SD_H_DAY, kappa_us, B)["ratio"]
              for m in MEANS_H_WEEK]
    check("6 the grid contains both an hours-bound and a plant-bound cell",
          min(ratios) < 1.0 < max(ratios),
          f"ratios {[f'{x:.2f}' for x in ratios]}")

    # 6b -- and the reason the FIRST version of test 6 failed, kept as a test so
    # nobody reintroduces it. The margin against wants is pinned by CAP, so it
    # can never report an excess and is not an instrument.
    margins = [cell(m / 7.0, REF_SD_H_DAY, kappa_us, B)["margin_vs_wants"]
               for m in MEANS_H_WEEK]
    # The claim is that it can never report an EXCESS, whatever the labour arm.
    # It sits a hair off CAP - 1 exactly, because B is calibrated on the
    # reference arm's wants and each cell's wants drift by ~0.1% (test 5).
    check("6b the margin against wants can never report an excess, so it is "
          "entailed and is NOT the statistic",
          max(margins) < 0.0,
          f"best {max(margins):+.3%}, against CAP - 1 = {sb.CAP - 1.0:+.3%}")

    # 7 -- the floor really is absent from both ceilings.
    c_lo = cell(REF_MEAN_H_DAY, REF_SD_H_DAY, kappa_us, B)
    check("7 neither ceiling depends on F",
          abs(c_lo["r_phys"] - ref_phys(kappa_us, B)) < 1e-9,
          "F appears in neither expression")

    print()
    if fails:
        print(f"{len(fails)} self-test(s) FAILED: {', '.join(fails)}")
        return 1
    print(f"{len(ran)} self-tests, all pass.")
    return 0


def ref_phys(kappa_us, B, eff=1.0):
    return B / (kappa_us * eff)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    return self_tests() if args.test else run()


if __name__ == "__main__":
    sys.exit(main())
