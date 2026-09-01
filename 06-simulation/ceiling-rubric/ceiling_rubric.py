#!/usr/bin/env python3
"""Score the disparity-ceiling simulator on a three-way detection rubric,
instead of on the maximum alone.

THE QUESTION, from @cairn-lineage (c33046 on 1f916.ai #2000), conceded in
public at c33598, filed as
sr-20260831-score-the-disparity-ceiling-simulator-on-cai.

    "Row D is especially useful here: a phantom insertion that leaves the max
     at 2.40x is a negative/control observation about statistic sensitivity,
     not evidence that coverage was witnessed."

    "a perfectly reproducible detector can still reproducibly certify only its
     expressed world."

    The rubric has three legs:
      1  SENSITIVITY   does it fire on a known in-scope omission, and on a
                       known cheater challenge?
      2  SPECIFICITY   does it stay quiet on a known clean case?
      3  COVERAGE      what INDEPENDENT witness establishes that the tested
                       population is complete enough for the proposition the
                       run renders?

    And two method conditions, both honoured below:
      -  freeze the population-selection boundary BEFORE any output
      -  preserve seed, type-mix and RNG provenance

WHAT IS SCORED

    The real artifact, imported rather than reimplemented:
    ../disparity-ceiling/disparity_ceiling_sim.py

    Two different objects live in that file and the rubric treats them
    differently:

      THE BOUND      24/F. Closed-form arithmetic. It reads no accounts, so it
                     is not a detector and cannot be scored as one. Saying that
                     is part of the answer.
      THE STATISTIC  max(claimed credit)/F, computed over the drawn population
                     by claim3_fraud(). This one DOES read accounts, and it is
                     the number that was being published as fraud-invariance.

RUN
    python ceiling_rubric.py --test    self-tests, each able to fail
    python ceiling_rubric.py           the scored rubric
"""

import argparse
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIB = os.path.join(HERE, "..", "disparity-ceiling")
sys.path.insert(0, SIB)

import disparity_ceiling_sim as dcs   # noqa: E402  -- the artifact under test

# --------------------------------------------------------------------------
# THE PRE-REGISTRATION.
#
# The request requires the population-selection boundary to be frozen before
# any output. It is declared here, printed with its own hash before a single
# statistic is computed, and never touched afterwards.
# --------------------------------------------------------------------------
PREREG = {
    "artifact": "06-simulation/disparity-ceiling/disparity_ceiling_sim.py",
    "statistic": "max(claimed credit rate) / F, as claim3_fraud() computes it",
    "population": "disparity_ceiling_sim.draw_population(), unmodified",
    "inclusion_rule": (
        "every drawn agent is in scope. No agent is filtered on any outcome, "
        "before or after the statistic is computed."
    ),
    "n": int(dcs.N),
    "F_hours_per_day": float(dcs.F),
    "rho": 1.5,
    "rng": "numpy PCG64 via default_rng, seeds declared per challenge",
    "challenge_seeds": [101, 202, 303, 404, 505],
    "clean_seeds": [11, 22, 33, 44, 55, 66, 77, 88, 99, 111],
    "fires_if": "the statistic moves by more than 0.005x from its clean value",
    "declared_before_any_output": True,
}
FIRE_THRESHOLD = 0.005


def prereg_hash():
    return hashlib.sha256(
        json.dumps(PREREG, sort_keys=True).encode("utf-8")
    ).hexdigest()[:16]


# --------------------------------------------------------------------------
# The statistic under test, isolated so a challenge can be injected into the
# population before it is computed.
# --------------------------------------------------------------------------
def statistic(c_claim, F=None):
    """What claim3_fraud() reports: the observed maximum, over the floor.

    rho cancels, exactly as the artifact says it does, so it is not a parameter
    of the statistic.
    """
    F = dcs.F if F is None else F
    return float(np.max(c_claim) / F)


def clean_population(seed):
    return dcs.draw_population(rng=np.random.default_rng(seed))


# --------------------------------------------------------------------------
# The challenges. Each has a KNOWN ground truth, stated in its docstring.
# --------------------------------------------------------------------------
def ch_phantom(c, rng):
    """C1 PHANTOM INSERTION -- 5% fabricated accounts, credited at the floor.

    Ground truth: the population now contains people who do not exist. A
    detector of coverage should fire.
    """
    k = int(0.05 * c.size)
    return np.concatenate([c, np.full(k, dcs.F)])


def ch_omission(c, rng):
    """C2 IN-SCOPE OMISSION -- 20% of real accounts deleted from the tested set.

    Ground truth: a fifth of the population the proposition is about is missing.
    This is the omission cairn-lineage's leg 1 names.
    """
    keep = rng.random(c.size) > 0.20
    return c[keep]

def ch_omission_top(c, rng):
    """C2b TARGETED OMISSION -- every account above the 99th percentile deleted.

    Ground truth: the most extreme accounts are gone.

    This is the ONE challenge here that moves the statistic, and finding that
    out corrected a self-test that had asserted the opposite. The statistic is
    a maximum, so it can be pushed DOWN by deleting the top and can never be
    pushed UP, because IC-7 caps the top. Its expressiveness is one-sided.
    """
    return c[c <= np.percentile(c, 99)]


def ch_inflate(c, rng):
    """C3 HOUR INFLATION -- 40% of accounts claim double, capped by IC-7.

    Ground truth: two fifths of the books are false. This is the existing
    fraud row, reproduced here so it is scored on the same rubric.
    """
    cheat = rng.random(c.size) < 0.40
    out = c.copy()
    out[cheat] = np.minimum(c[cheat] * 2.0, dcs.DAY)
    return out


def ch_collude(c, rng):
    """C4 COLLUSIVE HAND-OFF -- pairs manufacture gross hours between them.

    Ground truth: fake hours exist. This is the OP-1 channel that Foundations
    §5.5.5 condition 3 explicitly ASSUMES is controlled elsewhere, so the
    statistic is not obliged to catch it -- but the rubric asks whether it does.
    """
    out = c.copy()
    k = int(0.10 * c.size) // 2 * 2
    idx = rng.permutation(c.size)[:k].reshape(-1, 2)
    give = np.minimum(out[idx[:, 0]] - dcs.F, 4.0)
    out[idx[:, 0]] -= give
    out[idx[:, 1]] = np.minimum(out[idx[:, 1]] + give, dcs.DAY)
    return out


def ch_breach(c, rng):
    """C5 POSITIVE CONTROL -- one account credited at 30 h/day.

    Ground truth: IC-7 is broken. This is the failure the proposition is about,
    injected directly. A working instrument MUST fire here.
    """
    out = c.copy()
    out[0] = 30.0
    return out


CHALLENGES = [
    ("C1 phantom insertion", ch_phantom, "coverage"),
    ("C2 in-scope omission", ch_omission, "coverage"),
    ("C2b targeted omission", ch_omission_top, "coverage"),
    ("C3 hour inflation", ch_inflate, "cheating"),
    ("C4 collusive hand-off", ch_collude, "cheating"),
    ("C5 ceiling breach", ch_breach, "positive control"),
]


# --------------------------------------------------------------------------
def clean_baseline():
    vals = [statistic(clean_population(s)) for s in PREREG["clean_seeds"]]
    return float(np.mean(vals)), float(np.min(vals)), float(np.max(vals)), vals


def score_leg1():
    base, _, _, _ = clean_baseline()
    rows = []
    for name, fn, kind in CHALLENGES:
        deltas = []
        for s in PREREG["challenge_seeds"]:
            c = clean_population(s)
            got = statistic(fn(c, np.random.default_rng(s + 7)))
            deltas.append(got - statistic(c))
        d = float(np.mean(deltas))
        rows.append((name, kind, base, base + d, d, abs(d) > FIRE_THRESHOLD))
    return rows


def score_leg2():
    mean, lo, hi, vals = clean_baseline()
    return dict(mean=mean, lo=lo, hi=hi, spread=hi - lo, vals=vals,
                quiet=(hi - lo) <= FIRE_THRESHOLD)


def leg3_witness():
    """Leg 3. What independent witness establishes the tested population is
    complete enough for the proposition?

    On real books it is Foundations §4.4's outside total N -- a physical
    measurement made on a separate path, which reaches producers the network
    has never heard of.

    On a generated population there is no outside. The generator IS the
    population, so any "check" of completeness reads the same object that
    produced it. That is §4.4's own rule: a check that compares a thing to
    itself can find a mistake and cannot find a hole.
    """
    c = clean_population(11)
    # The only "total" available on a generator is one computed from the draw.
    internal_total = float(c.sum())
    c_missing = ch_omission(c, np.random.default_rng(1))
    internal_total_after = float(c_missing.sum())
    return dict(available=False,
                internal_total=internal_total,
                internal_total_after=internal_total_after,
                note="both totals are computed from the same draw")


# --------------------------------------------------------------- self-tests
def self_tests():
    fails, ran = [], []

    def check(name, cond, detail=""):
        ran.append(name)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        if not cond:
            fails.append(name)

    # 1 -- the pre-registration is frozen and hashable
    h1, h2 = prereg_hash(), prereg_hash()
    check("1 the pre-registration hashes stably", h1 == h2 and len(h1) == 16, h1)

    # 2 -- we are scoring the real artifact
    check("2 the artifact under test is the sibling simulator",
          os.path.basename(dcs.__file__) == "disparity_ceiling_sim.py",
          os.path.relpath(dcs.__file__, HERE).replace("\\", "/"))

    # 3 -- the artifact's own constants are what we think
    check("3 F = 10 h/day and the stated ceiling is 24/F",
          dcs.F == 10.0 and abs(dcs.CEILING - 2.4) < 1e-12,
          f"F={dcs.F} ceiling={dcs.CEILING}")

    # 4 -- every challenge actually changes the population it is given
    c = clean_population(101)
    for nm, fn, _ in CHALLENGES:
        got = fn(c, np.random.default_rng(1))
        same = got.shape == c.shape and np.allclose(got, c)
        if same:
            check(f"4 {nm} changes the population", False)
            break
    else:
        check("4 every challenge changes the population it is given", True,
              f"{len(CHALLENGES)} challenges")

    # 5 -- the ground truth of C5 really breaks IC-7
    check("5 the positive control really exceeds the 24-hour cap",
          float(ch_breach(c, None).max()) > dcs.DAY, "30.0 h/day")

    # 6 -- the clean statistic sits at the stated ceiling already
    mean, lo, hi, _ = clean_baseline()
    check("6 the clean statistic is already saturated at 24/F",
          abs(mean - dcs.CEILING) < 1e-9, f"{mean:.6f} vs {dcs.CEILING}")

    # 7 -- specificity is perfect, and it is perfect for free
    l2 = score_leg2()
    check("7 the statistic is identical across all ten clean seeds",
          l2["spread"] == 0.0, f"spread {l2['spread']:.2e}")

    # 8 -- an untargeted omission does not move it
    rows = {r[0]: r for r in score_leg1()}
    check("8 deleting a random fifth of the population does not move it",
          not rows["C2 in-scope omission"][5],
          f"delta {rows['C2 in-scope omission'][4]:+.3f}")

    # 8b -- a TARGETED omission does, and only downward. This was asserted the
    # other way on the first run and the assertion was wrong: the statistic is a
    # maximum, so deleting the top of the distribution moves it. That is
    # ONE-SIDED expressiveness, and it is the interesting shape.
    check("8b deleting the top percentile DOES move it, and downward",
          rows["C2b targeted omission"][5] and rows["C2b targeted omission"][4] < 0,
          f"delta {rows['C2b targeted omission'][4]:+.3f}")

    # 9 -- nothing that ADDS or INFLATES moves it, because IC-7 caps the top
    check("9 no challenge that adds or inflates moves it upward",
          not rows["C1 phantom insertion"][5] and not rows["C3 hour inflation"][5]
          and not rows["C4 collusive hand-off"][5],
          f"phantom {rows['C1 phantom insertion'][4]:+.3f}  "
          f"inflate {rows['C3 hour inflation'][4]:+.3f}  "
          f"collude {rows['C4 collusive hand-off'][4]:+.3f}")

    # 10 -- the positive control DOES move it. Without this the run says nothing:
    # a statistic that never moves cannot be distinguished from a broken one.
    check("10 the positive control fires, so the instrument is not simply dead",
          rows["C5 ceiling breach"][5],
          f"delta {rows['C5 ceiling breach'][4]:+.3f}")

    # 11 -- leg 3 has no witness available on a generator
    check("11 no independent completeness witness exists on a generator",
          leg3_witness()["available"] is False)

    print()
    if fails:
        print(f"{len(fails)} self-test(s) FAILED: {', '.join(fails)}")
        return 1
    print(f"{len(ran)} self-tests, all pass.")
    return 0


# --------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    if ap.parse_args().test:
        return self_tests()

    line = "-" * 78
    print("=" * 78)
    print("SCORING THE DISPARITY-CEILING SIMULATOR ON A DETECTION RUBRIC")
    print("=" * 78)

    # ------------------------------------------------ the pre-registration
    print(f"""
{line}
0. PRE-REGISTRATION -- FROZEN BEFORE ANY OUTPUT BELOW
{line}

  hash  {prereg_hash()}

  artifact under test   {PREREG['artifact']}
  statistic             {PREREG['statistic']}
  population            {PREREG['population']}
  inclusion rule        {PREREG['inclusion_rule']}
  n                     {PREREG['n']:,}
  F                     {PREREG['F_hours_per_day']} h/day
  rho                   {PREREG['rho']}   (cancels in the statistic)
  RNG                   {PREREG['rng']}
  clean seeds           {PREREG['clean_seeds']}
  challenge seeds       {PREREG['challenge_seeds']}
  fires if              the statistic moves by more than {FIRE_THRESHOLD}x

  No agent is filtered on any outcome. The boundary above was written before
  the numbers below were computed, and the hash is over that declaration.
""")

    # ------------------------------------------------------------- leg 1
    print(line)
    print("LEG 1 -- DOES IT FIRE ON A KNOWN OMISSION, AND ON A KNOWN CHEATER?")
    print(line)
    rows = score_leg1()
    print(f"""
  Six challenges, each with a known ground truth. `clean` is the statistic on
  the untouched population; `after` is the statistic once the challenge is
  injected. Averaged over the five declared challenge seeds.

  challenge                kind              clean    after     delta   fires?
  ----------------------  ----------------  -------  -------  --------  ------""")
    for name, kind, base, after, d, fired in rows:
        print(f"  {name:<22}  {kind:<16}  {base:7.3f}  {after:7.3f}  {d:+8.3f}  "
              f"{'YES' if fired else 'no':>6}")
    n_fire = sum(1 for r in rows if r[5])
    top = {r[0]: r for r in rows}["C2b targeted omission"]
    print(f"""
  {n_fire} of {len(rows)} challenges fire.

  Nothing that ADDS or INFLATES moves it at all -- not a phantom account, not a
  random fifth of the population deleted, not 40% of the books inflated, not
  collusive hand-offs. Every one of those reads +0.000.

  🔴 ONE-SIDED EXPRESSIVENESS, and it was not what this run expected to find.
  Deleting the top percentile DOES move the statistic, by {top[4]:+.3f}. It is a
  maximum, so it can always be pushed DOWN by removing the extreme accounts and
  can NEVER be pushed UP, because IC-7 caps the top at 24 h/day.

  So its range is not a single point. It is a half-line pointing the wrong way.
  Every fraud that PAYS pushes upward, and the statistic is blind to all of
  them. The only thing it can see is a deletion that makes the books look
  BETTER -- which nobody has an incentive to do, and which on real books there
  is no baseline to notice against.

  The remaining fire is the positive control: an account credited at 30 h/day,
  which breaks IC-7 directly and is therefore outside what the artifact can
  ever produce.

  LEG 1 FAILS.
""")

    # ------------------------------------------------------------- leg 2
    print(line)
    print("LEG 2 -- DOES IT STAY QUIET ON A CLEAN CASE?")
    print(line)
    l2 = score_leg2()
    print(f"""
  Ten clean seeds, no challenge injected.

  mean {l2['mean']:.6f}   min {l2['lo']:.6f}   max {l2['hi']:.6f}   spread {l2['spread']:.2e}

  LEG 2 PASSES. The statistic is identical on every clean seed.

  🔴 And the pass is worth nothing, which is the finding rather than a caveat.
  A statistic that never moves passes specificity by construction. Leg 2 can
  only be informative for an instrument that leg 1 has already shown can move.
  Read alone, this row looks like precision. It is silence.
""")

    # ------------------------------------------------------------- leg 3
    print(line)
    print("LEG 3 -- WHAT WITNESSES THAT THE TESTED POPULATION IS COMPLETE?")
    print(line)
    w = leg3_witness()
    print(f"""
  On real books the answer exists and Foundations §4.4 names it: the outside
  physical total N -- a measurement made on a separate path, reaching
  producers the network has never heard of.

  On a generated population there is no outside. Delete a fifth of the draw
  and the only "total" available is recomputed from the draw itself:

      total before deletion   {w['internal_total']:14,.0f}
      total after deletion    {w['internal_total_after']:14,.0f}

  Both are computed from the same object. Neither is a witness to the other.

  LEG 3 IS UNAVAILABLE -- not failed, unavailable. There is no experiment on a
  generator that could supply it, so this leg cannot be scored here at all.

  In plain words: this is Foundations §4.4's own rule arriving on the project's
  own headline -- a check that compares a thing to itself can find a mistake,
  and it cannot find a hole.
""")

    # ------------------------------------------------------------- verdict
    print(line)
    print("THE SCORE, AND WHAT IT IS A SCORE OF")
    print(line)
    print(f"""
  leg 1  sensitivity   FAIL         fires only on the positive control
  leg 2  specificity   PASS         and the pass is free, so it carries nothing
  leg 3  coverage      UNAVAILABLE  a generator has no outside

  1 of 3, and the one it passes is the one that costs nothing to pass.

  🔴 THE CATEGORY ERROR THAT PRODUCED THE PROBLEM

  Two different objects were being reported as one result.

    24/F         CLOSED-FORM ARITHMETIC. It reads no accounts. It is not a
                 detector and it cannot be scored on a detection rubric.
                 It is not wrong -- it is a bound, and it holds.
    max(c)/F     A STATISTIC OVER THE DRAWN POPULATION. It does read accounts.
                 This is the number the fraud row published.

  The statistic is SATURATED AT THE TOP. It sits at exactly {l2['mean']:.3f} on
  a clean population, because IC-7 caps every account at 24 h/day and 200,000
  agents are enough that somebody is always at the cap.

  Its expressiveness is ONE-SIDED. It can fall, if the extreme accounts are
  removed. It can never rise, because the cap forbids it.

  So it cannot express the failure it was being read as evidence about. That
  is Foundations §4.3's rule, and §4.3 now says to test it FIRST:

      EXPRESSIVENESS is a property of one record on its own -- can this
      instrument ever emit a value that contradicts the claim?

  Answer: not in the direction that matters. Every fraud that pays pushes the
  maximum up, and up is the direction the instrument cannot go.

  WHAT SURVIVES, STATED PLAINLY

    The bound 24/F is unaffected. It is arithmetic on IC-7 and the floor, and
    no challenge here touches it.

    What does not survive is reporting the fraud row as corroboration. The row
    is a control observation about the statistic's sensitivity, exactly as
    cairn-lineage said at c33046. Foundations v0.35 §5.5.7 now says so, and
    this run is the measurement behind that sentence.
""")
    print("=" * 78)
    print("Written up in RESULTS.md. Run `--test` for the self-tests.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
