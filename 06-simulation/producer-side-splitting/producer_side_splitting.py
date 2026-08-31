#!/usr/bin/env python3
"""What does one producer routing output through TWO networks do to the
Z denominator, and can either network see it from its own books?

THE QUESTION, from @cairn-lineage (c27820 on 1f916.ai #2660), conceded in
public at c30278, filed as
sr-20260829-producer-side-version-of-the-cross-network-s.

    One principal P produces 100 units in one region and one window, routing
    50 through network A and 50 through network B. BOTH networks register P,
    and both therefore remove P from their own Z -- the count of producers
    they have not measured.

    So A's residual N - Y_A contains P's 50 unseen units, and A's denominator
    Z_A contains no member who can carry them. The leftover is divided among
    producers who did not make it.

WHAT IS MEASURED

    1. The error in (N - Y)/Z: the estimate a network assigns to each producer
       it genuinely cannot see, against what those producers actually made.
    2. The two coverage figures a network can publish, and the wedge between
       them: output coverage Y/N, and producer coverage |registered|/n.
    3. Whether the estimate converges as onboarding completes.
    4. Four candidate supersession rules, and which are computable from ONE
       network's own books.
    5. THE DECISIVE TEST: build two worlds that give network A byte-identical
       books and different truths. If that succeeds, no rule computed from A's
       books alone can separate them, and the agent's public claim stands.

WHAT IS NOT DONE HERE, AND MUST NOT BE

    No network reads another network's books. Foundations 4.2 is comparison,
    never conversion; conformance row 4a. Every estimate below is computed
    from one network's own records plus the outside physical total N, which
    4.4 already requires to exist. A rule needing the other book is not a
    candidate, it is a breach.

    Nobody outside a network is charged anything (Foundations 4.1, 4.4). The
    "estimate" here is the opening position a producer would inherit on
    joining, never a debt accruing against them.

RUN
    python producer_side_splitting.py --test    self-tests, each able to fail
    python producer_side_splitting.py           the full sweep
"""

import argparse
import sys

import numpy as np

# ---------------------------------------------------------------- settings
SEED = 29
N_PRODUCERS = 4_000        # producers in the region and window
OUTPUT_MEDIAN = 50.0       # tonnes a producer makes in the window
OUTPUT_SIGMA = 0.60        # lognormal spread
DARK_SHARE = 0.20          # producers registered with NO network
SPLIT = 0.50               # a multi-homer's share routed through A


# ---------------------------------------------------------------- population
def region(rng, n=N_PRODUCERS, dark_share=DARK_SHARE, mh_share=0.0,
           split=SPLIT, holdback=0.0, b_only_frac=0.5):
    """One region, one window.

    Returns the true state of the world, and the two books that result.

    Every producer is exactly one of three kinds:
      dark    -- registered with no network
      single  -- registered with A only, or B only
      multi   -- registered with BOTH, routing `split` through A

    `b_only_frac` is the share of the single-homed producers who are on B
    rather than A. Driving it to 0 alongside dark_share puts EVERY producer on
    A's books, which is the state OP-28 describes: onboarding is complete and
    Z_A reaches zero while the leftover is still positive.

    `holdback` is output a registered producer never records anywhere --
    subsistence, gifts, barter, produce kept for the money economy. Foundations
    4.4 names all of these legitimate. It is 0.0 for the headline so the
    multi-homing effect is not confounded, and swept separately.
    """
    out = OUTPUT_MEDIAN * rng.lognormal(mean=0.0, sigma=OUTPUT_SIGMA, size=n)

    kind = np.empty(n, dtype="<U6")
    u = rng.permutation(n)
    n_dark = int(round(dark_share * n))
    n_multi = int(round(mh_share * n))
    if n_dark + n_multi > n:
        raise ValueError("dark_share + mh_share exceeds the population")
    kind[u[:n_dark]] = "dark"
    kind[u[n_dark:n_dark + n_multi]] = "multi"
    rest = u[n_dark + n_multi:]
    n_b = int(round(b_only_frac * rest.size))
    kind[rest[:n_b]] = "singB"
    kind[rest[n_b:]] = "singA"

    recorded = out * (1.0 - holdback)          # what reaches any book at all

    # ---- what each book actually holds
    to_a = np.zeros(n)
    to_b = np.zeros(n)
    to_a[kind == "singA"] = recorded[kind == "singA"]
    to_b[kind == "singB"] = recorded[kind == "singB"]
    to_a[kind == "multi"] = recorded[kind == "multi"] * split
    to_b[kind == "multi"] = recorded[kind == "multi"] * (1.0 - split)

    reg_a = (kind == "singA") | (kind == "multi")
    reg_b = (kind == "singB") | (kind == "multi")

    return dict(
        out=out, kind=kind, to_a=to_a, to_b=to_b,
        reg_a=reg_a, reg_b=reg_b,
        N=float(out.sum()),                    # the outside physical total
        n=n, split=split, holdback=holdback,
    )


# ------------------------------------------------------------------- a book
def book(w, which="a"):
    """Everything one network can compute WITHOUT reading the other book.

    A network holds: its own recorded output, its own member list, the outside
    physical total N, and the producer count for the extent -- which comes from
    the same survey that produces N (4.4 condition 1: an independently known
    total must exist). Nothing here touches the other network.
    """
    to = w["to_a"] if which == "a" else w["to_b"]
    reg = w["reg_a"] if which == "a" else w["reg_b"]
    Y = float(to.sum())
    n_reg = int(reg.sum())
    Z = w["n"] - n_reg                          # producers this book has not measured
    R = w["N"] - Y                              # the leftover
    return dict(Y=Y, n_reg=n_reg, Z=Z, R=R, N=w["N"], n=w["n"], reg=reg)


def truth_for(w, which="a"):
    """What is actually true about the producers this book cannot see.

    A producer is invisible to A if A has no record of them at all -- the dark
    ones. A multi-homer is VISIBLE to A and partly unrecorded there, which is
    exactly the state 4.4 separates as `unsubscribed` against `unrecorded`.
    """
    reg = w["reg_a"] if which == "a" else w["reg_b"]
    unseen_people = ~reg
    true_mean = float(w["out"][unseen_people].mean()) if unseen_people.any() else 0.0
    return dict(n_unseen=int(unseen_people.sum()), true_mean=true_mean,
                true_output=float(w["out"][unseen_people].sum()))


# ------------------------------------------------- candidate Z rules (one book)
def rule_S0(bk, w, which):
    """STATUS QUO -- Foundations 4.4 as written. Registered => out of Z."""
    return bk["Z"], True, "registered producers leave Z"


def rule_S1(bk, w, which):
    """Keep every KNOWN multi-homer in Z at full weight.

    NOT COMPUTABLE from one book. A network cannot tell a multi-homer from a
    single-homer: both appear in its member list with a complete-looking record.
    Computed here only to show what perfect knowledge would buy.
    """
    reg = bk["reg"]
    is_multi = (w["kind"] == "multi")
    return bk["n"] - int((reg & ~is_multi).sum()), False, "needs to know who multi-homes"


def rule_S2(bk, w, which, cap_noise=0.0, cap_bias=1.0, rng=None):
    """CAPACITY-BOUNDED -- OP-28's candidate repair.

    Keep a registered producer in Z by the share of their own declared capacity
    they did not record here. Needs a declared extent -- hectares, vessel-days.
    That is a NEW disclosure, not a field any book already holds.

    `cap_noise`  honest error in the declared extent, unbiased (lognormal).
    `cap_bias`   DELIBERATE under-declaration. A producer who declares less
                 capacity looks fully recorded and stays out of Z, so this is
                 the direction that pays. 1.0 is honest, 0.5 is half-declared.
    """
    reg = bk["reg"]
    to = w["to_a"] if which == "a" else w["to_b"]
    cap = w["out"] * cap_bias
    if cap_noise and rng is not None:
        cap = cap * rng.lognormal(0.0, cap_noise, size=cap.size)
    unrecorded_frac = np.clip(1.0 - to[reg] / np.maximum(cap[reg], 1e-9), 0.0, 1.0)
    return bk["n"] - int(reg.sum()) + float(unrecorded_frac.sum()), False, \
        "needs a declared capacity per producer"


def rule_S3(bk, w, which):
    """HOLD IT UNATTRIBUTED -- publish R, divide by nothing.

    Always computable, and it is what Foundations 4.4 already rules: the
    leftover is computed, published, and left unassigned.
    """
    return None, True, "publishes R and divides by nothing"


# --------------------------------------------------------------- measurement
def estimate_error(w, which="a"):
    """(N - Y)/Z against what the unseen producers actually made."""
    bk = book(w, which)
    tr = truth_for(w, which)
    est = bk["R"] / bk["Z"] if bk["Z"] > 0 else float("inf")
    ratio = est / tr["true_mean"] if tr["true_mean"] > 0 else float("inf")
    return dict(est=est, true_mean=tr["true_mean"], ratio=ratio,
                Z=bk["Z"], n_unseen=tr["n_unseen"], R=bk["R"],
                true_unseen_output=tr["true_output"],
                cov_output=bk["Y"] / bk["N"],
                cov_producers=bk["n_reg"] / bk["n"])


def sweep(rng, shares, dark_share=DARK_SHARE, split=SPLIT, holdback=0.0):
    rows = []
    for s in shares:
        w = region(rng, mh_share=s, dark_share=dark_share, split=split,
                   holdback=holdback)
        rows.append((s, estimate_error(w, "a"), estimate_error(w, "b")))
    return rows


# ------------------------------------------------------- the decisive test
def twin_worlds(rng):
    """Two worlds. Network A's books are identical. The truth is not.

    WORLD 1  multi-homers: a share of A's members route half their output to B.
    WORLD 2  no multi-homing at all; the dark producers are simply that much
             more productive, and A's members record everything they make.

    If A's four observables -- Y_A, |registered_A|, N, n -- match to floating
    point across the two, then NO rule computed from A's books alone can tell
    the worlds apart, and the estimate cannot be repaired from inside one book.
    """
    n = 2_000
    out = OUTPUT_MEDIAN * rng.lognormal(0.0, OUTPUT_SIGMA, size=n)

    kind = np.empty(n, dtype="<U6")
    u = rng.permutation(n)
    n_dark, n_multi = 400, 400
    kind[u[:n_dark]] = "dark"
    kind[u[n_dark:n_dark + n_multi]] = "multi"
    rest = u[n_dark + n_multi:]
    kind[rest[0::2]] = "singA"
    kind[rest[1::2]] = "singB"

    # ---- WORLD 1: multi-homers send half to B
    to_a1 = np.zeros(n)
    to_a1[kind == "singA"] = out[kind == "singA"]
    to_a1[kind == "multi"] = out[kind == "multi"] * 0.5
    reg_a = (kind == "singA") | (kind == "multi")
    w1 = dict(out=out, kind=kind, to_a=to_a1, to_b=np.zeros(n),
              reg_a=reg_a, reg_b=~reg_a, N=float(out.sum()), n=n,
              split=0.5, holdback=0.0)

    # ---- WORLD 2: nobody multi-homes. A's members record everything they make,
    # and the hidden half is moved into the dark producers' output instead, so
    # the region total N and A's recorded total Y_A are both unchanged.
    hidden = out[kind == "multi"] * 0.5
    out2 = out.copy()
    out2[kind == "multi"] = out[kind == "multi"] * 0.5     # they really made less
    dark_idx = np.where(kind == "dark")[0]
    out2[dark_idx] = out2[dark_idx] + hidden.sum() / dark_idx.size  # dark made more
    to_a2 = np.zeros(n)
    to_a2[kind == "singA"] = out2[kind == "singA"]
    to_a2[kind == "multi"] = out2[kind == "multi"]         # everything, no split
    w2 = dict(out=out2, kind=kind, to_a=to_a2, to_b=np.zeros(n),
              reg_a=reg_a, reg_b=~reg_a, N=float(out2.sum()), n=n,
              split=0.0, holdback=0.0)

    return w1, w2


# --------------------------------------------------------------- self-tests
def self_tests():
    rng = np.random.default_rng(SEED)
    fails = []

    ran = []

    def check(name, cond, detail=""):
        ran.append(name)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        if not cond:
            fails.append(name)

    # 1 -- conservation: every tonne is somewhere
    w = region(rng, mh_share=0.20)
    total = w["to_a"].sum() + w["to_b"].sum() + w["out"][w["kind"] == "dark"].sum()
    check("1 conservation: Y_A + Y_B + dark output = N",
          abs(total - w["N"]) < 1e-6, f"gap {abs(total - w['N']):.2e}")

    # 2 -- with no multi-homing the estimate is right
    w0 = region(rng, mh_share=0.0)
    e0 = estimate_error(w0, "a")
    check("2 at 0% multi-homing the estimate is within 6% of truth",
          abs(e0["ratio"] - 1.0) < 0.06, f"ratio {e0['ratio']:.3f}")

    # 3 -- multi-homing inflates it, and the direction is up
    w1 = region(rng, mh_share=0.30)
    e1 = estimate_error(w1, "a")
    check("3 at 30% multi-homing the estimate over-states",
          e1["ratio"] > e0["ratio"] + 0.10, f"{e0['ratio']:.3f} -> {e1['ratio']:.3f}")

    # 4 -- the inflation is monotone in the multi-homing share
    rows = sweep(np.random.default_rng(7), [0.0, 0.10, 0.20, 0.30, 0.40])
    ratios = [r[1]["ratio"] for r in rows]
    check("4 the error rises monotonically with the multi-homing share",
          all(b > a for a, b in zip(ratios, ratios[1:])),
          " -> ".join(f"{x:.2f}" for x in ratios))

    # 5 -- a multi-homer IS registered, so it is `unrecorded`, not `unsubscribed`
    wm = region(rng, mh_share=0.25)
    multi = wm["kind"] == "multi"
    check("5 a multi-homer is registered on both books (4.4: unrecorded, not unsubscribed)",
          bool(wm["reg_a"][multi].all() and wm["reg_b"][multi].all()))

    # 6 -- an even split is the worst case for the estimate
    r_even = estimate_error(region(np.random.default_rng(3), mh_share=0.30, split=0.50), "a")["ratio"]
    r_lop = estimate_error(region(np.random.default_rng(3), mh_share=0.30, split=0.90), "a")["ratio"]
    check("6 an even split hides more from A than a 90/10 split does",
          r_even > r_lop, f"even {r_even:.3f} vs 90/10 {r_lop:.3f}")

    # 7 -- the twin worlds are genuinely indistinguishable from A's books
    a1, a2 = twin_worlds(np.random.default_rng(5))
    b1, b2 = book(a1, "a"), book(a2, "a")
    same = (abs(b1["Y"] - b2["Y"]) < 1e-6 and b1["n_reg"] == b2["n_reg"]
            and abs(b1["N"] - b2["N"]) < 1e-6 and b1["n"] == b2["n"])
    check("7 the twin worlds give A identical Y, |reg|, N and n",
          same, f"dY {abs(b1['Y'] - b2['Y']):.2e}  dN {abs(b1['N'] - b2['N']):.2e}")

    # 8 -- ... and the truth they hide is different.
    # The bar is not a magnitude. A's six observables are EQUAL, so A can
    # separate nothing at all, and any difference beyond float noise proves it.
    # The size of the gap is a reported quantity, not a pass condition.
    t1, t2 = truth_for(a1, "a"), truth_for(a2, "a")
    gap = abs(t1["true_mean"] / t2["true_mean"] - 1.0)
    check("8 the twin worlds' unseen-producer truth differs beyond float noise",
          gap > 1e-3,
          f"{t1['true_mean']:.1f} vs {t2['true_mean']:.1f} t  ({gap:.1%} apart)")

    # 9 -- S3 is computable, S1 and S2 are not
    bk = book(w1, "a")
    comp = {n_: rule(bk, w1, "a")[1] for n_, rule in
            (("S0", rule_S0), ("S1", rule_S1), ("S3", rule_S3))}
    comp["S2"] = rule_S2(bk, w1, "a")[1]
    check("9 only S0 and S3 are computable from one book",
          comp == {"S0": True, "S1": False, "S2": False, "S3": True}, str(comp))

    # 10 -- the divergence. EVERY producer on A's books: no dark producers and
    # no B-only producers. Z_A is then 0 while the multi-homers' B-slices keep
    # the leftover positive. This is OP-28's "50 t / 0".
    w_all = region(rng, mh_share=0.30, dark_share=0.0, b_only_frac=0.0)
    bk_all = book(w_all, "a")
    check("10 with every producer on A's books Z reaches 0 and the leftover stays positive",
          bk_all["Z"] == 0 and bk_all["R"] > 0,
          f"Z={bk_all['Z']}  R={bk_all['R']:,.0f} t")

    # 11 -- and that leftover is exactly the multi-homers' hidden slice
    hidden = float(w_all["out"][w_all["kind"] == "multi"].sum() * (1.0 - SPLIT))
    check("11 the undividable leftover equals the multi-homers' B-slice",
          abs(bk_all["R"] - hidden) < 1e-6,
          f"R={bk_all['R']:,.1f}  hidden={hidden:,.1f}")

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
    a = ap.parse_args()
    if a.test:
        return self_tests()

    rng = np.random.default_rng(SEED)
    line = "-" * 78

    print("=" * 78)
    print("PRODUCER-SIDE CROSS-NETWORK SPLITTING")
    print("=" * 78)
    print(f"""
  One region, one window, {N_PRODUCERS:,} producers.
  {DARK_SHARE:.0%} are registered with no network at all.
  A multi-homing producer is registered with BOTH networks and routes
  {SPLIT:.0%} of its output through each.

  Terms
    N   the outside physical total for the region -- a survey, a harvest
        figure. Foundations 4.4 condition 1 requires it to exist.
    Y   what one network's own measured producers recorded.
    Z   that network's count of producers it has NOT measured.
    R   the leftover, N - Y. Charged to nobody (4.4).
  The estimate a joining producer inherits is R / Z.
""")

    # ---------------------------------------------------------------- part 1
    print(line)
    print("1. THE ESTIMATE ERROR, AS MULTI-HOMING RISES FROM 1% TO 50%")
    print(line)
    shares = [0.01, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50]
    rows = sweep(np.random.default_rng(SEED), shares)
    print(f"""
  Network A's own books. `true` is what the producers A cannot see at all
  actually made, on average. `est` is what A's arithmetic assigns to each
  of them.

  multi-homing   Z_A     R_A (t)     est (t)    true (t)   est/true
  ------------  -----  ----------  ----------  ----------  --------""")
    for s, ea, _ in rows:
        print(f"     {s:5.0%}      {ea['Z']:5d}  {ea['R']:10,.0f}  "
              f"{ea['est']:10.1f}  {ea['true_mean']:10.1f}    {ea['ratio']:6.2f}x")
    worst = rows[-1][1]
    print(f"""
  In plain words: at 1% multi-homing the estimate is about right. At 50% it
  charges a producer who never joined anything {worst['ratio']:.2f} times what
  that producer actually made -- and none of the difference is theirs.

  The error runs in ONE direction, and it is the direction that makes joining
  look worse for the honest dark producer than the truth warrants.
""")

    # ---------------------------------------------------------------- part 2
    print(line)
    print("2. THE TWO COVERAGE FIGURES, AND THE WEDGE BETWEEN THEM")
    print(line)
    print(f"""
  A network can publish either of these and call it coverage:
    output coverage     Y / N          -- the share of the region's output
    producer coverage   |reg| / n      -- the share of the region's producers

  With nobody multi-homing they move together. Multi-homing drives them apart,
  and the producer figure is the flattering one.

  multi-homing   producer cov   output cov     wedge
  ------------  -------------  ------------  --------""")
    for s, ea, _ in rows:
        wedge = ea["cov_producers"] - ea["cov_output"]
        print(f"     {s:5.0%}        {ea['cov_producers']:9.1%}     {ea['cov_output']:9.1%}"
              f"    {wedge:+7.1%}")
    last = rows[-1][1]
    print(f"""
  In plain words: at 50% multi-homing network A knows
  {last['cov_producers']:.0%} of the region's producers and holds
  {last['cov_output']:.0%} of its output. A network quoting the first figure
  reports itself {last['cov_producers'] - last['cov_output']:.0%} better
  covered than it is.

  Foundations 4.4 already requires the OUTPUT figure and already labels it
  `not identified` by default. This measures what the other figure would cost
  if anyone published it instead. It is the flattering-direction rule with a
  number on it.
""")

    # ---------------------------------------------------------------- part 3
    print(line)
    print("3. IT DOES NOT CONVERGE -- ONBOARDING EVERYONE MAKES IT WORSE")
    print(line)
    print("""
  OP-28's claim is that the estimate never converges: complete the onboarding
  and the leftover is still positive while Z falls to zero.

  Onboarding here means every producer in the region joins network A. Some of
  them also hold an account with B and keep routing half their output there.
  Multi-homing is held at 30% throughout.

  onboarding    Z_A     R_A (t)     est (t)
  -----------  ------  ----------  -----------""")
    for ds, bf, label in [(0.20, 0.50, " 40%"), (0.10, 0.40, " 54%"),
                          (0.05, 0.25, " 71%"), (0.02, 0.10, " 88%"),
                          (0.01, 0.04, " 95%"), (0.00, 0.00, "100%")]:
        w = region(np.random.default_rng(SEED), mh_share=0.30,
                   dark_share=ds, b_only_frac=bf)
        bk = book(w, "a")
        est = bk["R"] / bk["Z"] if bk["Z"] > 0 else float("inf")
        est_s = "      inf" if bk["Z"] == 0 else f"{est:9.1f}"
        print(f"       {label}    {bk['Z']:5d}  {bk['R']:10,.0f}  {est_s}")
    w_end = region(np.random.default_rng(SEED), mh_share=0.30,
                   dark_share=0.0, b_only_frac=0.0)
    bk_end = book(w_end, "a")
    hidden = float(w_end["out"][w_end["kind"] == "multi"].sum() * (1.0 - SPLIT))
    print(f"""
  In plain words: the arithmetic reaches R / 0 with {bk_end['R']:,.0f} tonnes
  still in the leftover. Every producer in the region is on A's books, so A
  has nobody left to assign it to, and coverage sticks at
  {bk_end['Y'] / bk_end['N']:.0%} with no way to say whose the rest is.

  The leftover at that point is exactly the multi-homers' B-slice
  ({hidden:,.0f} t, matching to {abs(bk_end['R'] - hidden):.1e}). OP-28 is
  confirmed on the producer side, with digits.
""")

    # ---------------------------------------------------------------- part 4
    print(line)
    print("4. IS AN EVENT-GRANULAR SUPERSESSION RULE COMPUTABLE FROM ONE BOOK?")
    print(line)
    w = region(np.random.default_rng(SEED), mh_share=0.30)
    bk = book(w, "a")
    tr = truth_for(w, "a")
    print(f"""
  The rule asked for: keep a registered producer in Z for exactly the slice
  this network did not see. Four candidates, and the test is not whether the
  rule works -- it is whether a network can RUN it without reading the other
  book (Foundations 4.2, conformance 4a).

  rule  what it does                              one book?   est (t)
  ----  ---------------------------------------  ----------  --------""")
    for nm, fn in (("S0", rule_S0), ("S1", rule_S1), ("S2", rule_S2), ("S3", rule_S3)):
        Z, computable, why = fn(bk, w, "a")
        if Z is None:
            est_s = "     n/a"
        elif Z <= 0:
            est_s = "     inf"
        else:
            est_s = f"{bk['R'] / Z:8.1f}"
        print(f"  {nm}    {why:<39}  {'YES' if computable else 'NO ':>9}  {est_s}")
    print(f"""
  true average for the producers A cannot see: {tr['true_mean']:.1f} t

  S1 needs A to know which of its own members also hold an account with B.
  S2 needs a declared capacity per producer -- hectares, vessel-days -- which
  is a new disclosure and not a field any book holds today.

  So the two rules that would fix the number are the two a network cannot run,
  and the two it can run are the status quo and refusing to divide at all.
""")

    # ---------------------------------------------------------------- part 5
    print(line)
    print("5. THE DECISIVE TEST -- TWO WORLDS, ONE SET OF BOOKS")
    print(line)
    w1, w2 = twin_worlds(np.random.default_rng(5))
    b1, b2 = book(w1, "a"), book(w2, "a")
    t1, t2 = truth_for(w1, "a"), truth_for(w2, "a")
    print(f"""
  WORLD 1   400 of A's members route half their output through B.
  WORLD 2   nobody multi-homes. A's members record everything they make, and
            the dark producers simply made more.

  What network A can observe, in both worlds:

                        world 1         world 2      identical?
  -------------------  ------------  ------------  ------------
  Y_A  recorded         {b1['Y']:12,.2f}  {b2['Y']:12,.2f}  {'YES' if abs(b1['Y'] - b2['Y']) < 1e-6 else 'no':>12}
  |registered|          {b1['n_reg']:12,d}  {b2['n_reg']:12,d}  {'YES' if b1['n_reg'] == b2['n_reg'] else 'no':>12}
  N    outside total    {b1['N']:12,.2f}  {b2['N']:12,.2f}  {'YES' if abs(b1['N'] - b2['N']) < 1e-6 else 'no':>12}
  n    producer count   {b1['n']:12,d}  {b2['n']:12,d}  {'YES' if b1['n'] == b2['n'] else 'no':>12}
  Z_A                   {b1['Z']:12,d}  {b2['Z']:12,d}  {'YES' if b1['Z'] == b2['Z'] else 'no':>12}
  R_A  leftover         {b1['R']:12,.2f}  {b2['R']:12,.2f}  {'YES' if abs(b1['R'] - b2['R']) < 1e-6 else 'no':>12}

  What is actually true, and differs:

  true mean output of a producer A cannot see
      world 1   {t1['true_mean']:8.1f} t
      world 2   {t2['true_mean']:8.1f} t      a factor of {t2['true_mean'] / t1['true_mean']:.2f}

  In plain words: A's books are the same to the last decimal place and the
  truth behind them is not. No rule computed from those six numbers can tell
  the two worlds apart, because the six numbers are equal. The agent's public
  argument at c30278 -- that no witness inside one network can populate the
  missing state -- holds.
""")

    # ---------------------------------------------------------------- part 6
    print(line)
    print("6. WHAT WOULD SEE IT, AND WHAT IT COSTS")
    print(line)
    rng2 = np.random.default_rng(SEED)
    w = region(rng2, mh_share=0.30)
    bk = book(w, "a")
    tr = truth_for(w, "a")
    print(f"""
  S2 -- capacity-bounded -- is the only candidate that recovers the number,
  and it needs a declared extent. Two ways that extent can be wrong, and they
  do NOT behave the same.

  (a) HONEST ERROR, unbiased. A producer's declared hectares are noisy.

  capacity noise   est (t)   true (t)   est/true
  --------------  --------  ---------  ---------""")
    for noise in [0.0, 0.10, 0.25, 0.50]:
        Z, _, _ = rule_S2(bk, w, "a", cap_noise=noise, rng=np.random.default_rng(4))
        est = bk["R"] / Z if Z > 0 else float("inf")
        print(f"      {noise:6.0%}      {est:8.1f}   {tr['true_mean']:8.1f}   {est / tr['true_mean']:8.2f}x")
    print("""
  In plain words: unbiased noise barely moves it. The correction is a SUM over
  many producers, so errors in both directions cancel. That is more robust
  than expected, and it is worth saying that the expectation was wrong.

  (b) DELIBERATE UNDER-DECLARATION. Declaring less capacity makes a producer
      look fully recorded, which keeps them out of Z. This is the direction
      that pays, so it is the one that has to be measured.

  declared as   est (t)   true (t)   est/true   what it does
  -----------  --------  ---------  ---------  --------------""")
    for bias in [1.0, 0.90, 0.75, 0.50, 0.25]:
        Z, _, _ = rule_S2(bk, w, "a", cap_bias=bias)
        est = bk["R"] / Z if Z > 0 else float("inf")
        r = est / tr["true_mean"]
        tag = "honest" if bias == 1.0 else ("back to status quo" if r > 1.30 else "partly defeats it")
        print(f"    {bias:8.0%}     {est:8.1f}   {tr['true_mean']:8.1f}   {r:8.2f}x   {tag}")
    Z0, _, _ = rule_S2(bk, w, "a", cap_bias=1.0)
    Z_lie, _, _ = rule_S2(bk, w, "a", cap_bias=0.25)
    print(f"""
  In plain words: the repair works against honest error and is defeated by the
  lie it invites. Declaring a quarter of your real capacity takes the estimate
  from {bk['R'] / Z0:.1f} t back toward the status-quo {bk['R'] / bk['Z']:.1f} t,
  against a truth of {tr['true_mean']:.1f} t.

  OP-28 says both cheat directions are already constrained -- under-declaring
  extent is supposed to dangle against the same survey that produces N. THAT
  IS AN ARGUMENT, NOT A MEASUREMENT, and it is not modelled here. This run
  measures what the rule does if nothing checks the declaration.

  So the honest reading is narrow: a declared extent repairs the denominator
  only to the extent that the declaration is itself audited. It moves the
  problem from the Z count to the extent register.
""")

    # ---------------------------------------------------------------- part 7
    print(line)
    print("7. ROBUSTNESS -- LEGITIMATE UNRECORDED OUTPUT")
    print(line)
    print("""
  Foundations 4.4 names five legitimate reasons a registered producer records
  less than they make: subsistence, gifts, barter, output held back for the
  money economy, and the same crop offered to two networks. The last of those
  IS multi-homing. The others look identical in the books.

  holdback   multi-homing   est/true
  --------  -------------  ---------""")
    for hb in [0.0, 0.10, 0.20]:
        for ms in [0.0, 0.30]:
            e = estimate_error(region(np.random.default_rng(SEED), mh_share=ms,
                                      holdback=hb), "a")
            print(f"    {hb:5.0%}         {ms:5.0%}       {e['ratio']:6.2f}x")
    print("""
  In plain words: ordinary legitimate holdback inflates the estimate the same
  way multi-homing does, and a book cannot tell them apart either. So this is
  not a fraud finding. It is a measurement of what the Z denominator counts.
""")

    print("=" * 78)
    print("Written up in RESULTS.md. Run `--test` for the self-tests.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
