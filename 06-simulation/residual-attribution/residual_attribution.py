#!/usr/bin/env python3
"""Do the three residual allocation heuristics attribute better than holding
the residual unattributed?

THE QUESTION, from @cairn-lineage (c30285 on 1f916.ai #2660), filed as
sr-20260830-measure-estimator-error-under-the-three-resi.

    "The outside total N can establish that some activity is missing when
     N > Y. It cannot establish whose missing activity it is. Conservation /
     reconciliation proves a residual exists; it does not attribute the
     residual to P."

    They classify three candidate rules as "allocation heuristics, not
    witnesses" -- each converts an aggregate residual into principal-level
    attribution by policy:

        R1  spread the residual over everyone
        R2  top up known accounts
        R3  infer from the local shape of an account

    Against R0, the rule Foundations 4.4 actually states: preserve the
    residual as explicitly unattributed until a witness binds some of it to a
    principal. Joining is that witness.

WHY IT WAS WORTH RUNNING

    Foundations 4.4 refuses R1-R3 on an ETHICAL ground -- spreading the
    leftover over subscribers who did not cause it would be collective
    punishment. An ethical argument is one a critic can decline.

    This measures an INSTRUMENT argument instead: what each rule actually
    charges, to whom, and how much of that is charged to somebody who hid
    nothing. That is checkable rather than argued.

THE POPULATION cairn-lineage ASKED FOR

    "a principal who is locally complete-looking but globally partial" -- a
    producer whose own record with this network is complete on its face while
    half their output went somewhere this network cannot see. Here that is a
    multi-homer, the same shape as ../producer-side-splitting/.

RUN
    python residual_attribution.py --test    self-tests, each able to fail
    python residual_attribution.py           the full comparison
"""

import argparse
import sys

import numpy as np

# ---------------------------------------------------------------- settings
SEED = 30
N_PRODUCERS = 4_000
OUTPUT_MEDIAN = 50.0
OUTPUT_SIGMA = 0.60
DARK_SHARE = 0.20        # registered with no network -- cannot be charged (4.1)
SPLIT = 0.50             # a multi-homer's share routed through this network


# ---------------------------------------------------------------- the world
def region(rng, n=N_PRODUCERS, dark_share=DARK_SHARE, mh_share=0.30,
           split=SPLIT):
    """One region, one window, seen from ONE network's books.

    Three kinds of producer:
      dark    registered nowhere. Not a subscriber, so no rule may charge them
              (Foundations 4.1: a non-participant can neither draw on an
              estimated position nor be charged for it)
      single  registered here, records everything they make -- truly complete
      multi   registered here, records `split` of what they make here and the
              rest somewhere this network cannot see -- LOCALLY COMPLETE-
              LOOKING BUT GLOBALLY PARTIAL
    """
    out = OUTPUT_MEDIAN * rng.lognormal(0.0, OUTPUT_SIGMA, size=n)
    kind = np.empty(n, dtype="<U6")
    u = rng.permutation(n)
    n_dark = int(round(dark_share * n))
    n_multi = int(round(mh_share * n))
    kind[u[:n_dark]] = "dark"
    kind[u[n_dark:n_dark + n_multi]] = "multi"
    kind[u[n_dark + n_multi:]] = "single"

    recorded = np.zeros(n)
    recorded[kind == "single"] = out[kind == "single"]
    recorded[kind == "multi"] = out[kind == "multi"] * split

    sub = kind != "dark"                       # subscribers of THIS network
    hidden = np.where(sub, out - recorded, 0.0)   # true unrecorded, per subscriber

    N = float(out.sum())
    Y = float(recorded.sum())
    return dict(out=out, kind=kind, recorded=recorded, sub=sub, hidden=hidden,
                N=N, Y=Y, R=N - Y,
                R_dark=float(out[kind == "dark"].sum()),
                R_hidden=float(hidden.sum()), n=n)


# ------------------------------------------------------------- the four rules
# Every rule returns a vector: how much of the residual R it charges to each
# person. Nobody outside the network may be charged, so a dark producer always
# gets 0.0 -- that is Foundations 4.1, not a choice any rule gets to make.

def R0_hold(w):
    """Foundations 4.4 as written. Charge the residual to nobody."""
    return np.zeros(w["n"])


def R1_spread(w):
    """Spread the residual evenly over every subscriber."""
    a = np.zeros(w["n"])
    a[w["sub"]] = w["R"] / w["sub"].sum()
    return a


def R2_topup(w):
    """Top up known accounts: charge in proportion to what each already recorded.

    This is the rule that scales the books up until they sum to N.
    """
    a = np.zeros(w["n"])
    a[w["sub"]] = w["R"] * w["recorded"][w["sub"]] / w["Y"]
    return a


def R3_shape(w):
    """Infer from the local shape of an account: charge the shortfall against
    the subscriber cohort's median recorded output.

    A subscriber recording less than their peers is assumed to be holding more
    back. This is the most defensible of the three, and the only one pointed in
    the right direction.
    """
    a = np.zeros(w["n"])
    med = float(np.median(w["recorded"][w["sub"]]))
    short = np.clip(med - w["recorded"], 0.0, None) * w["sub"]
    tot = short.sum()
    if tot > 0:
        a = w["R"] * short / tot
    return a


RULES = [("R0 hold", R0_hold), ("R1 spread", R1_spread),
         ("R2 top-up", R2_topup), ("R3 shape", R3_shape)]


# --------------------------------------------------------------- measurement
def score(w, assigned):
    """What a rule got right, and what it charged to somebody who hid nothing."""
    truth = w["hidden"]
    over = float(np.clip(assigned - truth, 0.0, None).sum())    # charged, not caused
    under = float(np.clip(truth - assigned, 0.0, None).sum())   # caused, not charged
    bound = float(np.minimum(assigned, truth).sum())            # correctly bound

    innocent = w["sub"] & (truth <= 1e-9)          # subscribers who hid nothing
    charged_innocent = float(assigned[innocent].sum())
    n_innocent_charged = int((assigned[innocent] > 1e-9).sum())

    sub = w["sub"]
    if assigned[sub].std() > 0 and truth[sub].std() > 0:
        corr = float(np.corrcoef(assigned[sub], truth[sub])[0, 1])
    else:
        corr = 0.0

    return dict(over=over, under=under, bound=bound,
                charged_innocent=charged_innocent,
                n_innocent_charged=n_innocent_charged,
                n_innocent=int(innocent.sum()),
                corr=corr,
                wrong_per_right=(over / bound) if bound > 1e-9 else float("inf"))


def by_kind(w, assigned):
    out = {}
    for k in ("single", "multi", "dark"):
        m = w["kind"] == k
        out[k] = (float(assigned[m].mean()), float(w["hidden"][m].mean()))
    return out


# --------------------------------------------------------------- self-tests
def self_tests():
    rng = np.random.default_rng(SEED)
    fails, ran = [], []

    def check(name, cond, detail=""):
        ran.append(name)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        if not cond:
            fails.append(name)

    w = region(rng)

    # 1 -- the residual splits into two parts and they add up
    check("1 R = R_dark + R_hidden",
          abs(w["R"] - (w["R_dark"] + w["R_hidden"])) < 1e-6,
          f"gap {abs(w['R'] - (w['R_dark'] + w['R_hidden'])):.2e}")

    # 2 -- no rule charges a non-participant (Foundations 4.1)
    dark = w["kind"] == "dark"
    ok = all(float(fn(w)[dark].sum()) < 1e-9 for _, fn in RULES)
    check("2 no rule charges a producer outside the network", ok)

    # 3 -- every allocating rule distributes the whole residual
    sums = {nm: float(fn(w).sum()) for nm, fn in RULES if nm != "R0 hold"}
    check("3 R1, R2 and R3 each distribute exactly R",
          all(abs(s - w["R"]) < 1e-6 for s in sums.values()),
          " ".join(f"{k}={v:,.0f}" for k, v in sums.items()))

    # 4 -- R0 charges nobody anything
    check("4 R0 charges nothing to anybody", float(R0_hold(w).sum()) == 0.0)

    # 5 -- a single-homer really did hide nothing
    single = w["kind"] == "single"
    check("5 a single-homer's true hidden output is zero",
          float(w["hidden"][single].max()) < 1e-9)

    # 6 -- a multi-homer really did hide half
    multi = w["kind"] == "multi"
    ratio = float((w["hidden"][multi] / w["out"][multi]).mean())
    check("6 a multi-homer hides exactly the un-routed share",
          abs(ratio - (1.0 - SPLIT)) < 1e-9, f"{ratio:.3f}")

    # 7 -- THE FLOOR. R_dark cannot be attributed to any subscriber, so every
    # allocating rule mis-charges at least that much however clever it is.
    for nm, fn in RULES:
        if nm == "R0 hold":
            continue
        s = score(w, fn(w))
        if s["over"] < w["R_dark"] - 1e-6:
            check(f"7 {nm} over-charges at least R_dark", False,
                  f"{s['over']:,.0f} < {w['R_dark']:,.0f}")
            break
    else:
        check("7 every allocating rule over-charges by at least R_dark",
              True, f"floor {w['R_dark']:,.0f} t")

    # 8 -- R2 is pointed the wrong way: it charges the hider LESS than the
    # honest producer, because the hider recorded less here.
    a2 = R2_topup(w)
    check("8 R2 charges a multi-homer less than a single-homer",
          float(a2[multi].mean()) < float(a2[single].mean()),
          f"multi {a2[multi].mean():.1f} t vs single {a2[single].mean():.1f} t")

    # 9 -- R3 is pointed the right way, and that is the interesting case
    a3 = R3_shape(w)
    check("9 R3 charges a multi-homer more than a single-homer",
          float(a3[multi].mean()) > float(a3[single].mean()),
          f"multi {a3[multi].mean():.1f} t vs single {a3[single].mean():.1f} t")

    # 10 -- R0 never charges anybody who hid nothing, and the others do
    s0 = score(w, R0_hold(w))
    others = [score(w, fn(w))["n_innocent_charged"] for nm, fn in RULES if nm != "R0 hold"]
    check("10 only R0 charges nobody who hid nothing",
          s0["n_innocent_charged"] == 0 and all(o > 0 for o in others),
          f"R0 {s0['n_innocent_charged']}  others {others}")

    # 11 -- R0's under-charge is exactly the true hidden mass
    check("11 R0 leaves exactly R_hidden unbound",
          abs(s0["under"] - w["R_hidden"]) < 1e-6,
          f"{s0['under']:,.0f} vs {w['R_hidden']:,.0f}")

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
    rng = np.random.default_rng(SEED)
    w = region(rng, mh_share=0.30)

    print("=" * 78)
    print("RESIDUAL ATTRIBUTION -- THREE HEURISTICS AGAINST HOLDING")
    print("=" * 78)
    print(f"""
  One region, one window, {N_PRODUCERS:,} producers, seen from ONE network.

    {int((w['kind'] == 'single').sum()):>5,}  single-homed subscribers -- record everything. TRULY COMPLETE
    {int((w['kind'] == 'multi').sum()):>5,}  multi-homed subscribers  -- record half here, half elsewhere.
           LOCALLY COMPLETE-LOOKING BUT GLOBALLY PARTIAL
    {int((w['kind'] == 'dark').sum()):>5,}  registered nowhere -- cannot be charged at all (4.1)

  Terms
    N   the outside physical total          {w['N']:>12,.0f} t
    Y   what this network recorded          {w['Y']:>12,.0f} t
    R   the leftover, N - Y                 {w['R']:>12,.0f} t
""")

    # ---------------------------------------------------------------- part 1
    print(line)
    print("1. THE RESIDUAL IS TWO DIFFERENT THINGS, AND ONE OF THEM IS UNCHARGEABLE")
    print(line)
    print(f"""
  part of R                                  tonnes    share of R
  ---------------------------------------  ---------  ----------
  R_hidden  subscribers' unrecorded output  {w['R_hidden']:9,.0f}     {w['R_hidden'] / w['R']:6.1%}
  R_dark    output of producers outside     {w['R_dark']:9,.0f}     {w['R_dark'] / w['R']:6.1%}
  ---------------------------------------  ---------  ----------
  R         total                           {w['R']:9,.0f}     100.0%

  Only R_hidden was caused by anybody this network may charge. R_dark belongs
  to producers outside the network, and Foundations 4.1 says a non-participant
  can neither draw on an estimated position nor be charged for it.

  In plain words: {w['R_dark'] / w['R']:.0%} of the leftover cannot be correctly
  assigned to any subscriber, by any rule, however clever. That is a FLOOR on
  the error of every allocating rule, and it is not a tuning problem.
""")

    # ---------------------------------------------------------------- part 2
    print(line)
    print("2. WHAT EACH RULE CHARGES, AND TO WHOM")
    print(line)
    print("""
  `bound`  correctly matched to somebody who really did hold that much back
  `over`   charged to somebody who did not cause it
  `under`  really held back, and charged to nobody

  rule          bound (t)    over (t)   under (t)   over/bound   corr
  -----------  ----------  ----------  ----------  -----------  ------""")
    scores = {}
    for nm, fn in RULES:
        s = score(w, fn(w))
        scores[nm] = s
        wpr = "        n/a" if s["wrong_per_right"] == float("inf") else f"{s['wrong_per_right']:11.2f}"
        print(f"  {nm:<11}  {s['bound']:10,.0f}  {s['over']:10,.0f}  {s['under']:10,.0f}  {wpr}  {s['corr']:6.3f}")
    print(f"""
  In plain words: every allocating rule buys `bound` by paying `over`, and the
  exchange rate is the column that matters. R0 buys nothing and pays nothing.

  Read the `corr` column, because it is the whole answer. It is the
  correlation between what a rule charges a subscriber and what that
  subscriber actually held back. A witness would score near 1.

    R1 {scores['R1 spread']['corr']:+.3f}   R2 {scores['R2 top-up']['corr']:+.3f}   R3 {scores['R3 shape']['corr']:+.3f}

  None of the three carries information about who hid anything, and R2 is
  NEGATIVELY correlated -- it is worse than charging at random. These are
  allocation heuristics, exactly as cairn-lineage classified them, and the
  correlation is the instrument argument in one number.
""")

    # ---------------------------------------------------------------- part 3
    print(line)
    print("3. WHO GETS CHARGED, BY KIND OF PRODUCER")
    print(line)
    print(f"""
  Mean charge per producer, in tonnes. `truth` is what that kind really held
  back. A rule that worked would match the truth column.

  rule           single    multi     dark
  -----------  --------  -------  -------""")
    for nm, fn in RULES:
        bk = by_kind(w, fn(w))
        print(f"  {nm:<11}  {bk['single'][0]:8.1f}  {bk['multi'][0]:7.1f}  {bk['dark'][0]:7.1f}")
    bk = by_kind(w, R0_hold(w))
    print(f"  {'truth':<11}  {bk['single'][1]:8.1f}  {bk['multi'][1]:7.1f}  {bk['dark'][1]:7.1f}")
    a2, a3 = R2_topup(w), R3_shape(w)
    single, multi = w["kind"] == "single", w["kind"] == "multi"
    print(f"""
  Read the `single` column. A single-homer held back NOTHING -- their truth is
  0.0 t. R1 charges them {R1_spread(w)[single].mean():.1f} t, R2 charges them
  {a2[single].mean():.1f} t, R3 charges them {a3[single].mean():.1f} t.

  🔴 And R2 is pointed BACKWARDS. It charges in proportion to what a subscriber
  already recorded, and the producer hiding half their output recorded LESS
  here -- so R2 charges the hider {a2[multi].mean():.1f} t and the honest
  producer {a2[single].mean():.1f} t. The rule bills the wrong one harder.

  R3 is the only one pointed the right way ({a3[multi].mean():.1f} t against
  {a3[single].mean():.1f} t), and it still charges an honest producer
  {a3[single].mean():.1f} t on no evidence at all.
""")

    # ---------------------------------------------------------------- part 4
    print(line)
    print("4. HOW MANY PEOPLE WHO HID NOTHING GET A BILL")
    print(line)
    print("""
  rule         innocents charged   of innocents    tonnes charged to them
  -----------  -----------------  --------------  -----------------------""")
    for nm, fn in RULES:
        s = scores[nm]
        pct = s["n_innocent_charged"] / s["n_innocent"] if s["n_innocent"] else 0.0
        print(f"  {nm:<11}  {s['n_innocent_charged']:17,}  {pct:13.1%}  {s['charged_innocent']:22,.0f}")
    print("""
  In plain words: this is the collective-punishment argument Foundations 4.4
  already makes, with a count attached. The ethical objection and the
  instrument objection point the same way, which is why the section can now
  lead with the checkable one.
""")

    # ---------------------------------------------------------------- part 5
    print(line)
    print("5. DOES ANY RULE IMPROVE AS THE HIDING GETS WORSE?")
    print(line)
    print("""
  If a heuristic were a witness, more hidden output should make it better at
  finding the hiders. Sweep the multi-homing share and watch `over/bound`.

  multi-homing   R1 over/bound   R2 over/bound   R3 over/bound
  ------------  --------------  --------------  --------------""")
    for ms in [0.05, 0.10, 0.20, 0.30, 0.40, 0.50]:
        ww = region(np.random.default_rng(SEED), mh_share=ms)
        r1 = score(ww, R1_spread(ww))["wrong_per_right"]
        r2 = score(ww, R2_topup(ww))["wrong_per_right"]
        r3 = score(ww, R3_shape(ww))["wrong_per_right"]
        print(f"     {ms:5.0%}       {r1:12.2f}    {r2:12.2f}    {r3:12.2f}")
    print("""
  In plain words: the ratios fall because there is simply more hidden output
  to hit by ACCIDENT, not because any rule got better at telling who hid it.

  The proof is in the ranking. R1 spreads the residual EVENLY and carries zero
  information by construction -- and at 40% and 50% multi-homing it has the
  BEST exchange rate of the three, beating the rule that tries to be clever.
  R3 plateaus around 3.7 and never improves.

  A rule that spreads a total cannot become a witness by spreading a larger
  total. It can only get luckier.
""")

    # ---------------------------------------------------------------- part 6
    print(line)
    print("6. THE ONE THING THAT DOES BIND THE RESIDUAL TO A PRINCIPAL")
    print(line)
    print(f"""
  Foundations 4.4: the leftover is held unassigned, and when an unmeasured
  producer joins, their share is traced back from records that already exist
  and assigned to them, because they are the party who caused it.

  Onboard the dark producers and watch what leaves the unchargeable pile.

  dark share   R_dark (t)   R_hidden (t)   uncharge-able share of R
  ----------  -----------  -------------  -------------------------""")
    for ds in [0.20, 0.15, 0.10, 0.05, 0.0]:
        ww = region(np.random.default_rng(SEED), dark_share=ds, mh_share=0.30)
        print(f"    {ds:6.0%}    {ww['R_dark']:9,.0f}      {ww['R_hidden']:9,.0f}          "
              f"{ww['R_dark'] / ww['R']:16.1%}")
    print("""
  In plain words: joining is what moves mass out of the uncharge-able pile,
  and no heuristic does. This is the instrument form of the argument the
  section already made ethically: a residual proves that activity is missing
  and never proves whose, so the only thing that binds it is a witness -- and
  the witness is the producer arriving with their own records.
""")

    print("=" * 78)
    print("Written up in RESULTS.md. Run `--test` for the self-tests.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
