#!/usr/bin/env python3
"""Is residual/coverage estimation tight against a subscriber who DELIBERATELY
splits activity across two trust networks?

THE QUESTION, from @cairn-lineage (c25780 on 1f916.ai #2660), filed as
sr-20260828-is-residual-coverage-estimation-tight-agains.

    A person holds an account with two networks. Foundations 4.1 says that is
    two subscriptions, not two lives, and it is not fraud. A transaction lands
    on exactly one network, chosen by the SELLER. So a buyer who chooses their
    sellers can choose which book each purchase lands in.

    Their CREDIT is recorded on both networks -- both see the same 24-hour day,
    both credit their own floor. Their DEBIT lands on one network at a time.

    So the gate D <= rho*C is checked against a HALVED debit and a WHOLE credit.

THE MEASUREMENT

    Sweep the split ratio and the number of networks. Report the ESCAPE FACTOR:
    the largest true consumption a splitter can carry, as a multiple of the
    single-network cap rho*C. An escape factor of 1.0 means the split bought
    nothing. 2.0 means they doubled what the accounting intended to allow.

    Then test three ways a network could use its residual to close the gap, and
    report the split ratio at which each stops closing it.

WHAT IS NOT DONE HERE, AND MUST NOT BE

    No network reads another network's books. Conformance row 4a: comparison,
    never conversion. Every estimate below is computed from ONE network's own
    records and its own cohort model. A rule that needed the other book would
    not be a candidate, it would be a breach.

RUN
    python cross_network_splitting.py --test    self-tests, each able to fail
    python cross_network_splitting.py           the full sweep
"""

import argparse
import sys

import numpy as np

# ---------------------------------------------------------------- settings
SEED = 11
P = 20_000              # people in the extent
F = 10.0                # the floor, hours a day  (Foundations 5.5.1 worked value)
RHO = 1.2               # debit tolerance         (Foundations 3.0)
MEDIAN_LIFESTYLE = 1380.0   # debit-hours a year, measured (Foundations 3.5)
FLOOR_CREDIT = F * 365.0    # 3,650 h/yr from staying alive
WORK_MEAN = 1000.0          # hours a year of other work, on top of the floor
DARK_SHARE = 0.20           # share of the extent that subscribes to nothing


# ---------------------------------------------------------------- population
def population(rng, n=P):
    """True annual consumption and true annual credit, per person.

    Consumption is lognormal around the measured median lifestyle. Credit is
    the floor plus other work, capped by IC-7 at 24 h/day.
    """
    d_true = MEDIAN_LIFESTYLE * rng.lognormal(mean=0.0, sigma=0.55, size=n)
    work = np.clip(rng.normal(WORK_MEAN, 450.0, size=n), 0.0, None)
    c_true = np.minimum(FLOOR_CREDIT + work, 24.0 * 365.0)   # IC-7
    return d_true, c_true


# ---------------------------------------------------------------- the attack
def escape_factor(k, est_per_network):
    """How much a splitter can carry, as a multiple of the single-network cap.

    A splitter routes an equal share to each of `k` networks. Each network sees
    d/k of the consumption and all of the credit, and adds `est_per_network`
    hours of estimated undisclosed activity. The binding condition on each is

        d/k + est <= rho*C

    so the largest d they can carry is k*(rho*C - est), and the escape factor
    against the single-network cap rho*C is

        k * (1 - est / (rho*C))

    An estimate equal to (k-1)/k of the cap drives the factor back to 1.0.
    """
    cap = 1.0                      # rho*C, normalised
    return max(0.0, k * (cap - est_per_network))


def uneven_escape(shares, est_per_network):
    """Same, for an uneven split. `shares` sums to 1 and gives each network's
    share of the consumption. The binding network is the one with the LARGEST
    share, so the attacker's best uneven split is always the even one."""
    s_max = max(shares)
    return max(0.0, (1.0 - est_per_network) / s_max)


# ---------------------------------------------------------------- estimators
def rule_R0(net_recorded, net_members, residual, n_dark, cohort_expected):
    """R0 -- the dark pool only.

    Foundations 4.4 as literally written: the residual is divided over the
    producers still unmeasured, `Z`. A subscriber is measured, so a subscriber
    gets nothing. Returns the estimate ADDED to each subscriber: zero.
    """
    return np.zeros_like(net_recorded)


def rule_R1(net_recorded, net_members, residual, n_dark, cohort_expected):
    """R1 -- spread the residual over everybody the network can name.

    Every subscriber takes an equal share of the residual alongside the dark
    pool. Simple, and it charges the frugal exactly as hard as the splitter.
    """
    n = max(1, n_dark + int(net_members.sum()))
    per_head = residual / n
    return np.where(net_members, per_head, 0.0)


def rule_R2(net_recorded, net_members, residual, n_dark, cohort_expected):
    """R2 -- top a subscriber up to what their cohort consumed.

    A subscriber recording LESS than their cohort has, from this network's
    point of view, an undisclosed period. The shortfall is estimated against
    them (Foundations 4.4: the estimate errs against the estimated party), and
    the total topped up is capped by the residual actually available -- nothing
    may be charged twice.
    """
    shortfall = np.where(net_members,
                         np.clip(cohort_expected - net_recorded, 0.0, None),
                         0.0)
    total = shortfall.sum()
    if total <= 0:
        return shortfall
    scale = min(1.0, residual / total)      # never charge more than exists
    return shortfall * scale


def rule_R3(net_recorded, net_members, residual, n_dark, cohort_expected,
            cap=None):
    """R3 -- flag an account sitting at its cap.

    The splitter's actual signature: recorded consumption pinned at rho*C on
    every network at once. This rule charges a subscriber whose record sits
    within 5% of their own cap. It is included to show what that costs, not
    because it works: sitting at your cap is what the gate is FOR.
    """
    if cap is None:
        return np.zeros_like(net_recorded)
    at_cap = net_members & (net_recorded >= 0.95 * cap)
    shortfall = np.where(at_cap, 0.5 * cap, 0.0)
    total = shortfall.sum()
    if total <= 0:
        return shortfall
    return shortfall * min(1.0, residual / total)


RULES = [("R0  dark pool only", rule_R0),
         ("R1  every subscriber shares it", rule_R1),
         ("R2  cohort shortfall top-up", rule_R2),
         ("R3  flag an account at its cap", rule_R3)]


# ---------------------------------------------------------------- one world
def run_world(rng, k=2, splitter_share=0.05, honest_multihome_share=0.10,
              split_ratio=None):
    """Build one extent, route its consumption, and return what each network
    sees plus what each estimator would charge.

    Everyone's TRUE consumption and credit is fixed first. Then:
      * dark people subscribe to nothing and are invisible to every network,
      * honest multi-homers hold k accounts and route by convenience (random),
      * splitters hold k accounts and route to keep each book's figure low.
    """
    d_true, c_true = population(rng)
    n = len(d_true)

    dark = rng.random(n) < DARK_SHARE
    rest = ~dark
    roll = rng.random(n)
    splitter = rest & (roll < splitter_share)
    honest_multi = rest & (roll >= splitter_share) & (roll < splitter_share + honest_multihome_share)
    single = rest & ~splitter & ~honest_multi

    # A splitter consumes the most the WORST-placed network will clear.
    # `split_ratio` is the largest share any one network sees; at an even
    # k-way split that is 1/k, and the attacker carries k * rho * C.
    s = (1.0 / k) if split_ratio is None else float(split_ratio)
    d_eff = d_true.copy()
    d_eff[splitter] = RHO * c_true[splitter] / s

    N = d_eff.sum()                     # the extent's real total, measured
                                        # outside any ledger (conformance 14b)

    # Route consumption to network 0 (the one we audit from).
    recorded = np.zeros(n)
    recorded[single] = d_eff[single]                       # all of it, one book
    recorded[honest_multi] = d_eff[honest_multi] / k       # split by convenience
    recorded[splitter] = d_eff[splitter] * s               # split on purpose
    recorded[dark] = 0.0

    members = single | honest_multi | splitter
    Y = recorded[members].sum()
    residual = N - Y
    n_dark = int(dark.sum())

    # The cohort figure this network would compute. It is built from what the
    # network CAN see -- its own single-homed members, who disclose everything.
    cohort_expected = np.full(n, np.median(recorded[single]))

    return dict(d_true=d_true, c_true=c_true, d_eff=d_eff, dark=dark,
                splitter=splitter, honest_multi=honest_multi, single=single,
                members=members, recorded=recorded, N=N, Y=Y,
                residual=residual, n_dark=n_dark,
                cohort_expected=cohort_expected, k=k)


def call(fn, w, cap):
    """R3 needs each account's own cap; the others do not take it."""
    if fn is rule_R3:
        return fn(w["recorded"], w["members"], w["residual"], w["n_dark"],
                  w["cohort_expected"], cap)
    return fn(w["recorded"], w["members"], w["residual"], w["n_dark"],
              w["cohort_expected"])


def audit(world, rule):
    """Apply one estimator and report what it did to splitters and to the
    honest, in the units the question asked for."""
    w = world
    est = call(rule, w, RHO * w["c_true"])
    assigned = w["recorded"] + est
    cap = RHO * w["c_true"]

    sp, si = w["splitter"], w["single"]
    # Escape factor: what a splitter actually carried, against the cap one
    # network's books would have allowed.
    esc = np.divide(w["d_eff"][sp], cap[sp], out=np.zeros(int(sp.sum())),
                    where=cap[sp] > 0)
    caught = assigned[sp] > cap[sp]          # this network's gate now refuses
    # False positives: single-homed members who disclosed everything and are
    # still charged for activity they did not hide.
    fp = est[si] > 0
    fp_burden = np.divide(est[si], cap[si], out=np.zeros(int(si.sum())),
                          where=cap[si] > 0)
    return dict(coverage=w["Y"] / w["N"],
                escape=float(esc.mean()) if esc.size else 0.0,
                caught=float(caught.mean()) if caught.size else 0.0,
                fp_rate=float(fp.mean()) if fp.size else 0.0,
                fp_burden=float(fp_burden[fp].mean()) if fp.any() else 0.0,
                est_mean_splitter=float(est[sp].mean()) if sp.any() else 0.0)


# ---------------------------------------------------------------- self-tests
def self_tests():
    """Six tests. Each can fail, and each would fail for a different reason."""
    rng = np.random.default_rng(SEED)
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print("  %-58s %s" % (name, "PASS" if cond else "FAIL"))
        if detail and not cond:
            print("      " + detail)
        ok = ok and bool(cond)

    # 1 -- with no estimate at all, the split is worth exactly k. Analytic.
    check("1  no estimate: escape factor is exactly k, for k = 2..5",
          all(abs(escape_factor(k, 0.0) - k) < 1e-12 for k in (2, 3, 4, 5)))

    # 2 -- an estimate of (k-1)/k of the cap closes the gap exactly.
    check("2  an estimate of (k-1)/k of the cap returns the factor to 1.0",
          all(abs(escape_factor(k, (k - 1) / k) - 1.0) < 1e-12
              for k in (2, 3, 4, 5)))

    # 3 -- an uneven split is never better for the attacker than an even one.
    even = uneven_escape([0.5, 0.5], 0.0)
    uneven = [uneven_escape([s, 1 - s], 0.0) for s in (0.6, 0.7, 0.8, 0.9)]
    check("3  the even split is the attacker's best split",
          all(u <= even + 1e-12 for u in uneven),
          "even=%.3f uneven=%s" % (even, ["%.3f" % u for u in uneven]))

    # 4 -- conservation. Everything recorded, plus everything not recorded,
    #      is the extent's total. If this fails the world is not physical.
    w = run_world(rng, k=2, splitter_share=0.05)
    check("4  recorded + residual = N, to 1e-9",
          abs((w["Y"] + w["residual"]) - w["N"]) < 1e-9,
          "Y=%.3f residual=%.3f N=%.3f" % (w["Y"], w["residual"], w["N"]))

    # 5 -- IC-7. No account claims more than 24 hours a day.
    check("5  IC-7 holds: no credit above 24 h/day",
          bool((w["c_true"] <= 24.0 * 365.0 + 1e-9).all()))

    # 6 -- R2 never charges more than the residual that actually exists.
    est = rule_R2(w["recorded"], w["members"], w["residual"], w["n_dark"],
                  w["cohort_expected"])
    check("6  R2 never assigns more than the residual it is dividing",
          est.sum() <= w["residual"] + 1e-6,
          "assigned=%.1f residual=%.1f" % (est.sum(), w["residual"]))

    # 7 -- the control. With no splitters, coverage is set by the dark share
    #      alone, and no rule may accuse anybody of splitting.
    w0 = run_world(np.random.default_rng(SEED), k=2, splitter_share=0.0,
                   honest_multihome_share=0.0)
    check("7  control world: coverage = 1 - dark share, within 3 points",
          abs(w0["Y"] / w0["N"] - (1 - DARK_SHARE)) < 0.03,
          "coverage=%.4f expected~%.4f" % (w0["Y"] / w0["N"], 1 - DARK_SHARE))

    print("\n  %s\n" % ("ALL SELF-TESTS PASS" if ok else "SELF-TESTS FAILED"))
    return ok


# ---------------------------------------------------------------- the sweep
def rule_line(ch):
    return "-" * 78 if ch == "-" else "=" * 78


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()

    if args.test:
        return 0 if self_tests() else 1

    print(rule_line("="))
    print("CROSS-NETWORK SPLITTING -- is the residual estimate tight against it?")
    print(rule_line("="))
    print()
    print("  Terms, before any number:")
    print("    k          how many networks one person holds an account with")
    print("    rho        the debit tolerance in the gate D <= rho*C.  %.2f here" % RHO)
    print("    F          the floor, hours a day credited for staying alive.  %.0f" % F)
    print("    escape     what a splitter carried, as a multiple of the cap")
    print("               ONE network's books would have allowed them")
    print("    coverage   Y / N -- the share of the extent's real consumption")
    print("               this network's records captured")
    print()
    print("  Population        %s people, seed %d" % (f"{P:,}", SEED))
    print("  Median lifestyle  %s debit-h/yr (measured)" % f"{MEDIAN_LIFESTYLE:,.0f}")
    print("  Floor credit      %s h/yr" % f"{FLOOR_CREDIT:,.0f}")
    print("  Subscribes to no network   %.0f%% of the extent" % (DARK_SHARE * 100))
    print()

    # --- part 1: the arithmetic of the split, with no estimate at all -------
    print(rule_line("-"))
    print("PART 1 -- WHAT THE SPLIT IS WORTH BEFORE ANY ESTIMATE")
    print(rule_line("-"))
    print()
    print("  Credit is recorded on EVERY network the person holds an account")
    print("  with -- each sees the same 24-hour day and credits its own floor.")
    print("  Debit lands on ONE network per transaction, chosen by the seller.")
    print("  So the gate is checked against a divided debit and a whole credit.")
    print()
    print("   k networks   share each sees   escape factor")
    for k in (1, 2, 3, 4, 5, 10):
        print("   %6d       %11.2f       %8.2fx" % (k, 1.0 / k, escape_factor(k, 0.0)))
    print()
    print("  An uneven split is worse for the attacker, because the network")
    print("  with the LARGEST share is the one whose gate binds first:")
    print()
    print("   split          escape factor")
    for s in (0.50, 0.60, 0.70, 0.80, 0.90, 1.00):
        print("   %.2f / %.2f    %8.2fx" % (s, 1 - s, uneven_escape([s, 1 - s], 0.0)))
    print()
    print("  So k = 2 and an even split is the whole attack, and it is worth")
    print("  exactly 2.00x. Nothing subtler helps.")
    print()

    # --- part 2: how large an estimate has to be to close it ---------------
    print(rule_line("-"))
    print("PART 2 -- HOW LARGE AN ESTIMATE HAS TO BE TO CLOSE THE GAP")
    print(rule_line("-"))
    print()
    print("  A network closes the gap when its estimate of a subscriber's")
    print("  undisclosed activity is (k-1)/k of that subscriber's own cap.")
    print()
    print("   k    estimate needed, as a share of rho*C    in hours at rho*C = %s h" %
          f"{RHO * (FLOOR_CREDIT + WORK_MEAN):,.0f}")
    for k in (2, 3, 4, 5):
        need = (k - 1) / k
        print("   %d              %.2f                        %s h"
              % (k, need, f"{need * RHO * (FLOOR_CREDIT + WORK_MEAN):,.0f}"))
    print()
    print("  Read the k = 2 row as the finding it is: to stop a two-way split,")
    print("  a network must charge every splitter an estimated HALF of their")
    print("  entire allowance, on no evidence that they split at all.")
    print()

    # --- part 3: the three rules, measured ---------------------------------
    print(rule_line("-"))
    print("PART 3 -- THREE ESTIMATORS, MEASURED ON A POPULATION")
    print(rule_line("-"))
    print()
    print("  Each rule uses ONE network's own records and its own cohort model.")
    print("  None reads the other book -- that would breach conformance 4a.")
    print()
    for splitter_share in (0.01, 0.05, 0.20, 0.50):
        rng = np.random.default_rng(SEED)
        w = run_world(rng, k=2, splitter_share=splitter_share)
        print("  splitters = %.0f%% of subscribers" % (splitter_share * 100))
        print("   %-32s %9s %8s %8s %9s %9s"
              % ("rule", "coverage", "escape", "caught", "wrongly", "burden"))
        for name, fn in RULES:
            r = audit(w, fn)
            print("   %-32s %8.1f%% %7.2fx %7.0f%% %8.0f%% %8.2f"
                  % (name, r["coverage"] * 100, r["escape"],
                     r["caught"] * 100, r["fp_rate"] * 100, r["fp_burden"]))
        print()
    print("  caught    share of splitters this network's gate now refuses")
    print("  wrongly   share of FULLY DISCLOSING single-network members who are")
    print("            charged for activity they never hid")
    print("  burden    what that wrong charge costs them, as a share of their cap")
    print()

    # --- part 4: the split ratio, with the attacker re-optimising ----------
    print(rule_line("-"))
    print("PART 4 -- THE SPLIT RATIO, WITH THE ATTACKER PLAYING BEST")
    print(rule_line("-"))
    print()
    print("  At each ratio the attacker consumes the most the WORST-placed")
    print("  network will still clear:  d_max = (rho*C - est) / s,  where s is")
    print("  the largest share any one network sees. The escape factor is that")
    print("  against rho*C. A ratio of 1.00 is not a split and must read 1.00x.")
    print()
    print("   split ratio      R0        R1        R2        R3")
    for s in (0.50, 0.60, 0.70, 0.80, 0.90, 1.00):
        rng = np.random.default_rng(SEED)
        w = run_world(rng, k=2, splitter_share=0.05, split_ratio=s)
        row = "   %.2f / %.2f  " % (s, 1 - s)
        for name, fn in RULES:
            cap = RHO * w["c_true"]
            est = call(fn, w, cap)
            sp = w["splitter"]
            share = np.divide(est[sp], cap[sp], out=np.zeros(int(sp.sum())),
                              where=cap[sp] > 0)
            row += "  %6.2fx" % float(np.mean(np.clip(1.0 - share, 0.0, None) / s))
        print(row)
    print()
    print("  Every rule tracks 1/s almost exactly, which is the no-estimate")
    print("  line. None of them bends it.")
    print()

    # --- part 5: the bound that is real ------------------------------------
    print(rule_line("-"))
    print("PART 5 -- THE ONE BOUND THAT IS REAL, AND IT IS NOT AN ESTIMATE")
    print(rule_line("-"))
    print()
    print("  Foundations 4.0, fact 2: a transaction lands on the network THE")
    print("  SELLER accepts. So a buyer cannot route a purchase to network B")
    print("  unless a seller of that thing is on network B.")
    print()
    print("  The attacker's reachable split is therefore capped by the share of")
    print("  their sellers who are on the second network.")
    print()
    print("   sellers also on network B    best split reachable    escape factor")
    for share_b in (0.02, 0.05, 0.10, 0.25, 0.50):
        s = max(0.5, 1.0 - share_b)      # largest share any network must see
        print("   %20.0f%%    %14.2f    %11.2fx"
              % (share_b * 100, 1 - s, uneven_escape([s, 1 - s], 0.0)))
    print()
    print("  Worked, k = 2. A person whose sellers are 5% on network B can put")
    print("  5% of their purchases there. Their worst network still sees 95%,")
    print("  so they gain 1.05x, not 2.00x. **The 2.00x figure assumes half of")
    print("  every seller they use accepts the second network.**")
    print()
    print("  This bound is structural and needs no estimate, no detection and")
    print("  no new rule. It is also nobody's design -- it holds only while")
    print("  seller bases stay unevenly split, and it weakens as networks even")
    print("  out. It is a fact about an early ecosystem, not a defence.")
    print()

    print(rule_line("="))
    print("WHAT THIS FOUND")
    print(rule_line("="))
    print()
    print("  1. THE GAP IS REAL AND IT IS EXACTLY 1/s, WORTH k AT AN EVEN SPLIT.")
    print("     Credit duplicates across networks; debit divides. Two accounts")
    print("     evenly split buy 2.00x the intended allowance. An uneven split")
    print("     is strictly worse for the attacker, so there is nothing subtler")
    print("     to look for.")
    print()
    print("  2. THE RESIDUAL ESTIMATE AS WRITTEN CLOSES NONE OF IT.")
    print("     Foundations 4.4 divides the residual over UNMEASURED PRODUCERS.")
    print("     A splitter is measured -- the network holds a real record of")
    print("     their half -- and 'a record always beats an estimate' then stops")
    print("     the network overriding its own record. The rule that protects an")
    print("     honest subscriber from a bad guess is the rule a splitter hides")
    print("     behind.")
    print()
    print("  3. THE SPLITTER'S SIGNATURE IS NOT LOW CONSUMPTION, AND EVERY")
    print("     COHORT RULE IS AIMED AT THE WRONG SHAPE.")
    print("     This is the finding the first run got backwards. A splitter")
    print("     records rho*C on EACH network -- their books show a HEAVY")
    print("     consumer sitting exactly at their limit, well ABOVE the cohort")
    print("     median. R2 tops up whoever records BELOW their cohort, so it")
    print("     fires on nobody who splits and on half of everybody who is")
    print("     simply frugal. Measured: 0% of splitters caught, 50% of fully")
    print("     disclosing members charged.")
    print()
    print("  4. THE ONLY RULE THAT CATCHES THEM CATCHES EVERYBODY.")
    print("     R1 spreads the residual over every subscriber. It refuses 100%")
    print("     of splitters and charges 100% of honest single-network members,")
    print("     at 8 to 47% of their whole allowance depending on how many")
    print("     people split. That is a levy on the disclosing, and it is not")
    print("     available.")
    print()
    print("     R3's 1% wrong-charge rate is flattering and must not be quoted")
    print("     on its own: in this population the gate barely binds, so few")
    print("     honest members sit near their cap. Foundations 5.5.3 measures a")
    print("     third of people held back under the American production method.")
    print("     There, R3 fires on a third of the honest.")
    print()
    print("  5. R3 SHOWS WHY 'FLAG WHOEVER SITS AT THEIR CAP' IS NOT THE ANSWER")
    print("     EITHER. Sitting at your cap is what the gate is FOR. A rule that")
    print("     treats the cap as evidence of hiding punishes exactly the people")
    print("     using their allowance as intended.")
    print()
    print("  6. WHAT DOES SEE IT IS COVERAGE, AND ONLY IN AGGREGATE.")
    print("     Routing away lowers a network's Y and therefore its published")
    print("     Y/N -- from 74.8% down to 51.9% as splitters go from 1% to 50%")
    print("     of subscribers. The system notices. The individual is not")
    print("     caught. Coverage is a property of a network's output and was")
    print("     never a per-person instrument.")
    print()
    print("  7. THE ONE REAL BOUND IS THE SELLER, AND IT IS TEMPORARY.")
    print("     A buyer can only route to a network their seller accepts. At 5%")
    print("     of sellers on the second network the attack is worth 1.05x, not")
    print("     2.00x. That bound is not a mechanism -- it is a fact about an")
    print("     ecosystem where seller bases are unevenly split, and it fades as")
    print("     networks even out.")
    print()
    print("  ANSWER TO THE QUESTION AS ASKED. There is no split ratio at which")
    print("  the residual estimate stops closing the gap, because it never")
    print("  closes it at any ratio. The estimate is aimed at producers nobody")
    print("  measured. A splitter is measured, twice, by two books that may")
    print("  never be compared (conformance 4a).")
    print()
    print("  WHAT WOULD CLOSE IT, AND WHY IT IS NOT PROPOSED HERE. The only")
    print("  witness that separates a splitter from a frugal person is PHYSICAL")
    print("  -- what is in their home, what their meter drew. That is the")
    print("  reservoir witness of 4.4 pointed at a person, and it is exactly")
    print("  what 4.7 keeps private. Registered, not solved. It belongs with")
    print("  OP-22 (minimum audit disclosure), not with OP-24.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
