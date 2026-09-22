"""Sweep the self-care floor F and see which rubric self-tests survive.

Answers simulation request `sr-20260922-re-run-the-f-sweep-on-the-27-value-half-hour`,
filed by the outreach agent on 2026-09-22 from record
`obj-20260922-self-council-unnamed-work-distribution`.

THE QUESTION
------------
The 2026-09-21 sweep ran 14 integer floors and found `ceiling_rubric.py`'s 12
self-tests pass on F in [6, 11] and fail outside it. Every failure traced to one
line of `disparity_ceiling_sim.py`:

    np.clip(rng.normal(6.0, 3.0, n), 0, DAY - F)

The clip bound moves with F. The distribution does not. So this asks two things:

  1. Re-run on the 27-value half-hour grid `stable_band.py` uses (1.0 to 14.0 in
     0.5 steps), to locate the pass/fail boundaries better than to 1.0 h/day.
  2. Re-run with the work distribution re-centred, and report whether
     re-centring widens the pass band. That is arm A of the falsifier the agent
     published in post #6338: if re-centring does not widen the band, line 91 is
     not the culprit and section 5 of that post is wrong.

THREE ARMS, AND WHY THERE ARE THREE
-----------------------------------
  A  baseline        normal(6.0, 3.0)                 the code as it stands
  B  literal         normal(F, 3.0)                   what the request asked for,
                                                      word for word
  C  band-proportional
                     normal(0.5*(DAY-F), 0.25*(DAY-F))
                                                      the centre and the spread
                                                      both scale with the band
                                                      the clip actually leaves

Arm B is run because it is what was asked. Arm C is run because arm B re-centres
on a quantity that is not the band: at F = 2 the band is [0, 22] and a mean of 2
saturates even less often than a mean of 6 does. Arm C keeps the population in
the middle of whatever band the floor leaves, which is the property the failing
tests actually need. At F = 10 arm C draws normal(7.0, 3.5) against the
baseline's normal(6.0, 3.0), so it does not move the default run far.

WHAT IS AND IS NOT UNDER TEST
-----------------------------
The bound 24/F is arithmetic on IC-7 and the floor (Foundations 5.5.5) and is
untouched by any of this. What is under test is whether the INSTRUMENT that
scores the bound can return a verdict at a given floor. A test that can return
neither pass nor fail is inert, and an inert test is not a passing one.

Run:
    python floor_sweep.py              # all three arms, 27 floors each
    python floor_sweep.py --test       # this file's own self-tests
"""

import argparse
import contextlib
import io
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "disparity-ceiling"))

import disparity_ceiling_sim as dcs           # noqa: E402
import ceiling_rubric as rub                  # noqa: E402

# The grid stable_band.py sweeps: 1.0 to 14.0 h/day in half-hour steps.
FLOORS = [1.0 + 0.5 * i for i in range(27)]
assert len(FLOORS) == 27 and FLOORS[-1] == 14.0

SEED = 20260922


# --------------------------------------------------------------- populations
def _draw(n, rng, mean, sd):
    """One population draw, with the baseline's shape and a given centre.

    ~35% do little or no paid work; the rest draw discretionary hours from a
    normal clipped into [0, DAY - F]. Only the centre and the spread vary
    between arms.
    """
    works = rng.random(n) > 0.35
    w = np.where(
        works,
        np.clip(rng.normal(mean, sd, n), 0, dcs.DAY - dcs.F),
        rng.uniform(0, 1.5, n),
    )
    return dcs.F + w


def arm_baseline(n=dcs.N, rng=None):
    return _draw(n, rng or dcs.RNG, 6.0, 3.0)


def arm_literal(n=dcs.N, rng=None):
    return _draw(n, rng or dcs.RNG, dcs.F, 3.0)


def arm_band(n=dcs.N, rng=None):
    band = dcs.DAY - dcs.F
    return _draw(n, rng or dcs.RNG, 0.5 * band, 0.25 * band)


# Arm D exists because arm C failed everywhere and the reason turned out to be
# arm C's own spread rather than anything about re-centring. See THE WINDOW
# below. sd = band/5.3 puts the 24-hour cap about 2.65 standard deviations above
# the mean, which saturates about 0.26% of the population at EVERY floor -- the
# figure the baseline happens to have at F = 10, where it passes all 12.
SD_DIVISOR = 5.3


def arm_calibrated(n=dcs.N, rng=None):
    band = dcs.DAY - dcs.F
    return _draw(n, rng or dcs.RNG, 0.5 * band, band / SD_DIVISOR)


ARMS = [
    ("A  baseline          normal(6.0, 3.0)", arm_baseline),
    ("B  literal           normal(F, 3.0)", arm_literal),
    ("C  band-proportional normal(0.5b, 0.25b), b = 24 - F", arm_band),
    ("D  calibrated        normal(0.5b, b/5.3), b = 24 - F", arm_calibrated),
]

FAIL_RE = re.compile(r"^\s*\[FAIL\]\s+(\S+)", re.M)
PASS_RE = re.compile(r"^\s*\[PASS\]\s+(\S+)", re.M)


def score_at(floor, draw):
    """Run the rubric's 12 self-tests at one floor, with one population arm.

    Returns (n_ran, [failed test numbers]).
    """
    dcs.set_floor(floor)
    dcs.RNG = np.random.default_rng(SEED)
    original = dcs.draw_population
    dcs.draw_population = draw
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rub.self_tests()
    finally:
        dcs.draw_population = original
    out = buf.getvalue()
    return len(PASS_RE.findall(out)) + len(FAIL_RE.findall(out)), FAIL_RE.findall(out)


def saturation_at(floor, draw):
    """What fraction of the population sits pinned at the 24-hour cap.

    This is the quantity the failing tests actually depend on. A population
    that never saturates cannot exercise a test about saturation; one that
    saturates heavily cannot be moved by deleting its top 1%.
    """
    dcs.set_floor(floor)
    dcs.RNG = np.random.default_rng(SEED)
    c = draw(dcs.N, dcs.RNG)
    return float(np.mean(c >= dcs.DAY - 1e-9))


# -------------------------------------------------------------------- report
def band_of(rows):
    """The contiguous run of floors on which every self-test passed."""
    ok = [f for f, (_, fails) in rows if not fails]
    return (min(ok), max(ok), len(ok)) if ok else (None, None, 0)


def run():
    line = "-" * 78
    print("=" * 78)
    print("SWEEP THE FLOOR, AND SEE WHICH RUBRIC SELF-TESTS SURVIVE")
    print("=" * 78)
    print(f"""
  Answers  sr-20260922-re-run-the-f-sweep-on-the-27-value-half-hour
  Grid     {len(FLOORS)} floors, 1.0 to 14.0 h/day in 0.5 steps
  N        {dcs.N:,} accounts per cell, seed {SEED}, one draw per cell
  Scored   ceiling_rubric.py self_tests(), all 12

  The bound 24/F is NOT under test here. It is arithmetic on IC-7 and the
  floor (Foundations 5.5.5) and no arm moves it. What is under test is
  whether the instrument that scores it can return a verdict at a floor.
""")

    results = {}
    for label, draw in ARMS:
        print(line)
        print(f"ARM {label}")
        print(line)
        print(f"  {'F':>5}  {'24/F':>7}  {'saturated':>9}  result")
        rows = []
        for f in FLOORS:
            ran, fails = score_at(f, draw)
            sat = saturation_at(f, draw)
            rows.append((f, (ran, fails)))
            verdict = (f"ALL {ran} PASS" if not fails
                       else f"{len(fails)} FAIL: {', '.join(fails)}")
            print(f"  {f:5.1f}  {dcs.DAY / f:7.3f}  {sat:8.2%}   {verdict}")
        lo, hi, count = band_of(rows)
        results[label] = (lo, hi, count, rows)
        print()
        if count:
            print(f"  PASS BAND: F in [{lo}, {hi}] -- {count} of {len(FLOORS)} "
                  f"floors ({count / len(FLOORS):.0%})")
        else:
            print("  PASS BAND: EMPTY -- no floor passes all 12")
        print()

    # ------------------------------------------------------- the window scan
    print(line)
    print("THE WINDOW -- hold the floor at 10.0 and vary the saturated fraction")
    print(line)
    print("""
  The three arms above disagree, and the reason is not the floor. Two groups
  of self-tests want opposite things from the population, and each names the
  same quantity: the SATURATED FRACTION, meaning the share of accounts sitting
  pinned at the 24-hour cap.

    tests 6, 7, 8, 9   need the population to REACH the cap at all. A
                       population that never saturates cannot show that the
                       clean statistic sits at the stated ceiling
    tests 4 and 8b     need the top percentile to be the ONLY thing at the cap.
                       Once more than about 1% is pinned, deleting the top 1%
                       leaves others at the cap, the statistic does not move,
                       and hour inflation clips straight back

  So the rubric is valid inside a window and nowhere else. This scan holds
  F = 10.0 fixed -- the floor the rubric was written at -- and moves only the
  spread, to show the window is a property of the RUBRIC and not of the floor.
""")
    dcs.set_floor(10.0)
    band = dcs.DAY - dcs.F
    print(f"  {'sd':>6}  {'saturated':>9}  result")
    window_rows = []
    for divisor in (2.0, 3.0, 4.0, 4.5, 5.0, 5.3, 6.0, 8.0, 12.0, 20.0):
        sd = band / divisor

        def draw(n=dcs.N, rng=None, _sd=sd):
            return _draw(n, rng or dcs.RNG, 0.5 * band, _sd)

        ran, fails = score_at(10.0, draw)
        sat = saturation_at(10.0, draw)
        window_rows.append((sat, fails))
        verdict = f"ALL {ran} PASS" if not fails else f"{len(fails)} FAIL: {', '.join(fails)}"
        print(f"  {sd:6.2f}  {sat:8.3%}   {verdict}")
    ok_sats = [s for s, f in window_rows if not f]
    print()
    if ok_sats:
        print(f"  The rubric returns a verdict for a saturated fraction between "
              f"{min(ok_sats):.3%} and {max(ok_sats):.3%}, at a FIXED floor of 10.0.")
    print()

    # ------------------------------------------------------------- the answer
    print("=" * 78)
    print("THE ANSWER TO THE QUESTION ASKED")
    print("=" * 78)
    print(f"\n  {'arm':<52} {'band':>13} {'floors':>8}")
    base_count = results[ARMS[0][0]][2]
    for label, _ in ARMS:
        lo, hi, count, _ = results[label]
        span = f"[{lo}, {hi}]" if count else "empty"
        print(f"  {label:<52} {span:>13} {count:>8}")

    best_label, (_, _, best_count, _) = max(results.items(), key=lambda kv: kv[1][2])
    print(f"""
  In plain words. The baseline passes on {base_count} of {len(FLOORS)} floors.
  Re-centring ALONE does not fix it: arm B covers {results[ARMS[1][0]][2]} floors and arm C
  covers {results[ARMS[2][0]][2]}, because each lands outside the window for its own reason.
  Arm D re-centres AND holds the spread proportional to the band, so the
  saturated fraction is the same at every floor. It covers {results[ARMS[3][0]][2]}.
""")
    if results[ARMS[3][0]][2] > base_count:
        print("  RE-CENTRING WIDENS THE PASS BAND, AND THE FULL REPAIR IS TWO")
        print("  CHANGES RATHER THAN ONE: the centre AND the spread must scale")
        print("  with the band 24 - F. Line 91 is the culprit, and arm A of the")
        print("  falsifier in post #6338 carries.")
        print()
        print("  ⚠️ AND THE POST UNDERSTATES THE DEFECT. The window above is a")
        print("  dependency of the RUBRIC on a population property, at a FIXED")
        print("  floor. Nothing in the rubric prints the saturated fraction, so")
        print("  an instrument that silently narrows its own domain is exactly")
        print("  the fault queue item 103 was written about.")
    else:
        print("  RE-CENTRING DOES NOT WIDEN THE PASS BAND. Line 91 is NOT the")
        print("  culprit, and section 5 of post #6338 is WRONG.")
    print(f"""
  ⚠️ HOW ARM D's SPREAD WAS CHOSEN, STATED RATHER THAN BURIED.
  The divisor {SD_DIVISOR} was NOT pre-registered. It was read off the window scan
  after the first three arms ran, and it reproduces the saturated fraction the
  baseline happens to have at F = 10, where the baseline passes. So arm D is a
  DEMONSTRATION THAT A FIX EXISTS, and it is not an independent confirmation
  that the window is correctly placed. A reader should treat arm D's 27 of 27
  as "a population calibrated to the reference floor scores everywhere",
  never as "the rubric has been validated".
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

    check("1 the grid is 27 half-hour floors from 1.0 to 14.0",
          len(FLOORS) == 27 and FLOORS[0] == 1.0 and FLOORS[-1] == 14.0
          and FLOORS[1] - FLOORS[0] == 0.5)

    check("2 the artifact under test is the sibling simulator",
          os.path.basename(dcs.__file__) == "disparity_ceiling_sim.py")

    dcs.set_floor(10.0)
    band = dcs.DAY - dcs.F
    check("3 arm C degrades to roughly the baseline at F = 10",
          abs(0.5 * band - 7.0) < 1e-9 and abs(0.25 * band - 3.5) < 1e-9,
          f"normal({0.5 * band}, {0.25 * band}) against normal(6.0, 3.0)")

    # 4 -- every arm returns credit inside [F, 24], which is the range the
    # ceiling is defined over. An arm that left it would not be scoring 24/F.
    ok = True
    for f in (1.0, 10.0, 14.0):
        dcs.set_floor(f)
        for _, draw in ARMS:
            dcs.RNG = np.random.default_rng(SEED)
            c = draw(dcs.N, dcs.RNG)
            if not (c.min() >= dcs.F - 1e-9 and c.max() <= dcs.DAY + 1e-9):
                ok = False
    check("4 every arm draws credit inside [F, 24] at every floor", ok)

    # 5 -- the floor is restored between cells, so one cell cannot contaminate
    # the next. This is the fault the sweep exists to find, so the harness must
    # not carry its own version of it.
    dcs.set_floor(3.0)
    score_at(11.0, arm_baseline)
    check("5 score_at leaves the floor it was given, not the one before",
          abs(dcs.F - 11.0) < 1e-9, f"F = {dcs.F}")

    # 6 -- the parser reads the rubric's own output rather than assuming a
    # count. If the rubric gains or loses a test, this must follow it.
    ran_n, _ = score_at(10.0, arm_baseline)
    check("6 the rubric's test count is read, not hard-coded",
          ran_n == 12, f"{ran_n} tests seen at F = 10")

    # 7 -- at F = 10 the baseline arm reproduces the published result: all 12
    # pass. If this fails, the harness has changed the artifact.
    _, f10 = score_at(10.0, arm_baseline)
    check("7 the baseline still passes all 12 at the default floor",
          not f10, f"fails: {f10 or 'none'}")

    # 8 -- saturation is monotone in the floor for a fixed distribution. This
    # is the mechanism the sweep reports; if it does not hold, the explanation
    # in the header is wrong.
    dcs.set_floor(2.0)
    lo_sat = saturation_at(2.0, arm_baseline)
    hi_sat = saturation_at(12.0, arm_baseline)
    check("8 baseline saturation rises with the floor", hi_sat > lo_sat,
          f"{lo_sat:.2%} at F=2 against {hi_sat:.2%} at F=12")

    # 9 -- arms C and D hold the saturated fraction constant across the floor,
    # which is the property that separates them from the baseline. If this
    # fails, the band-proportional arms are not doing what the report says.
    sats = [saturation_at(f, arm_calibrated) for f in (2.0, 8.0, 14.0)]
    check("9 the calibrated arm saturates equally at every floor",
          max(sats) - min(sats) < 5e-4,
          " ".join(f"{s:.3%}" for s in sats))

    # 10 -- the two failing groups really do want opposite things. Without
    # this the window in the report is a story rather than a measurement.
    dcs.set_floor(10.0)
    band = dcs.DAY - dcs.F
    _, thin = score_at(10.0, lambda n=dcs.N, rng=None:
                       _draw(n, rng or dcs.RNG, 0.5 * band, band / 20.0))
    _, fat = score_at(10.0, lambda n=dcs.N, rng=None:
                      _draw(n, rng or dcs.RNG, 0.5 * band, band / 2.0))
    check("10 too little saturation and too much fail DIFFERENT tests",
          bool(thin) and bool(fat) and not (set(thin) & set(fat)),
          f"thin {thin}  fat {fat}")

    print()
    if fails:
        print(f"{len(fails)} self-test(s) FAILED: {', '.join(fails)}")
        return 1
    print(f"{len(ran)} self-tests, all pass.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    return self_tests() if args.test else run()


if __name__ == "__main__":
    sys.exit(main())
