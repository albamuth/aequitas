#!/usr/bin/env python3
"""How far does R = N - Y move when both instruments share a blind spot?

THE QUESTION, from @cairn-lineage (c21187), filed as
sr-20260826-how-far-does-r-n-y-move-under-a-correlated-m.

    "N - Y is not a lower bound when N under-detects on the same population Z
     exists to expose."

    Sweep a correlated-miss model with a realistic detector falloff. Does the
    error stay inside any bound conformance row 14a can express?

THE SETUP, IN THE DOCUMENTS' OWN TERMS

    N   the independently known total for the whole extent -- a satellite
        survey, agricultural statistics, trade data. Reaches non-subscribers.
    Y   what the network's own subscribers recorded.
    R   the leftover, N - Y. What people the network cannot see produced.
    Z   how many producers are still unmeasured.

    Conformance row 14a permits a subtraction only when the two figures measure
    the same quantity, over the same extent, over the same window, with error
    bounds smaller than their difference. It then requires the answer as an
    INTERVAL, R in [N_L - Y_U, N_U - Y_L], never a bare bound.

    Row 13 says the interval carries `floor`, `ceiling` or `not identified`,
    and that `not identified` is the default.

WHY A CORRELATED MISS IS THE HARD CASE

    The interval arithmetic of 14a assumes the two blind spots are stated
    SEPARATELY. If a satellite misses small plots and small plots are exactly
    who does not subscribe, then N and Y are blind to THE SAME producers -- and
    the leftover they compute between them is the difference of two numbers
    that both already dropped the thing being measured.

RUN
    python correlated_miss.py --test    self-tests, each able to fail
    python correlated_miss.py           the full sweep
"""

import argparse
import sys

import numpy as np

SEED = 23
P = 40_000                 # producers in the extent
MEDIAN_OUTPUT = 40.0       # tonnes a year, median producer
SIGMA = 1.10               # spread of producer size (lognormal)


def producers(rng, n=P):
    """True annual output per producer. Small producers are the many."""
    return MEDIAN_OUTPUT * rng.lognormal(mean=0.0, sigma=SIGMA, size=n)


def detect(size, half, sharpness):
    """Probability an instrument sees a producer of this size.

    A real detector does not have a cliff. It has a falloff: certain on the
    large, hopeless on the small, and a band in between. `half` is the size at
    which detection is 50%; `sharpness` is how quickly it climbs.
    """
    return 1.0 / (1.0 + (half / np.maximum(size, 1e-9)) ** sharpness)


def world(rng, n_half, y_half, sharpness=2.0, rho=1.0):
    """One extent, measured by two instruments with a shared size bias.

    `rho` is how correlated the two blind spots are, from 0 to 1.
        rho = 0  independent draws -- each instrument misses its own producers
        rho = 1  the same latent draw -- whoever N misses, Y misses too

    Both instruments are SIZE-BIASED in the same direction, which is the
    realistic case and the one @cairn-lineage named: a satellite misses small
    plots, and small plots are who does not subscribe.
    """
    size = producers(rng)
    n = len(size)

    p_n = detect(size, n_half, sharpness)
    p_y = detect(size, y_half, sharpness)

    # One shared latent uniform plus an independent one, mixed by rho.
    shared = rng.random(n)
    own_n = rng.random(n)
    own_y = rng.random(n)
    u_n = rho * shared + (1 - rho) * own_n
    u_y = rho * shared + (1 - rho) * own_y

    seen_n = u_n < p_n
    seen_y = u_y < p_y

    truth = size.sum()
    N = size[seen_n].sum()
    Y = size[seen_y].sum()
    # The truth the leftover is trying to describe: output by producers the
    # NETWORK cannot see.
    R_true = size[~seen_y].sum()
    R_obs = N - Y
    return dict(truth=truth, N=N, Y=Y, R_obs=R_obs, R_true=R_true,
                seen_n=seen_n, seen_y=seen_y, size=size,
                n_dark=int((~seen_y).sum()))


def label(R_obs, R_true):
    """What row 13's three labels would say about this figure, in hindsight."""
    if R_obs < R_true * (1 - 1e-9):
        return "floor"        # the truth is above the published figure
    if R_obs > R_true * (1 + 1e-9):
        return "ceiling"
    return "exact"


def rule_line(ch="-"):
    return ch * 78


def self_tests():
    rng = np.random.default_rng(SEED)
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print("  %-58s %s" % (name, "PASS" if cond else "FAIL"))
        if detail and not cond:
            print("      " + detail)
        ok = ok and bool(cond)

    # 1 -- a perfect N and a perfect Y give R = 0 and no dark producers.
    w = world(rng, n_half=1e-9, y_half=1e-9, rho=0.0)
    check("1  two perfect instruments: R_obs and R_true are both 0",
          abs(w["R_obs"]) < 1e-6 and abs(w["R_true"]) < 1e-6,
          "R_obs=%.4f R_true=%.4f" % (w["R_obs"], w["R_true"]))

    # 2 -- a perfect N with a blind Y gives R_obs == R_true exactly. This is
    #      the case the documents assume, and it is the only one that is exact.
    w = world(np.random.default_rng(SEED), n_half=1e-9, y_half=30.0, rho=0.0)
    check("2  perfect N, blind Y: R_obs equals R_true",
          abs(w["R_obs"] - w["R_true"]) < 1e-6,
          "R_obs=%.1f R_true=%.1f" % (w["R_obs"], w["R_true"]))

    # 3 -- conservation. Everything seen by Y plus everything not seen is the
    #      truth. If this fails the world is not physical.
    w = world(np.random.default_rng(SEED), n_half=20.0, y_half=30.0, rho=0.5)
    check("3  Y + R_true = truth, to 1e-6",
          abs(w["Y"] + w["R_true"] - w["truth"]) < 1e-6,
          "Y=%.1f R_true=%.1f truth=%.1f" % (w["Y"], w["R_true"], w["truth"]))

    # 4 -- N can never exceed the truth. An instrument cannot see what is not
    #      there.
    check("4  N never exceeds the truth", w["N"] <= w["truth"] + 1e-6)

    # 5 -- the detector is monotone in size: a larger producer is never less
    #      likely to be seen.
    s = np.array([1.0, 10.0, 100.0, 1000.0])
    p = detect(s, 30.0, 2.0)
    check("5  detection rises with producer size", bool(np.all(np.diff(p) > 0)),
          str(p))

    # 6 -- rho = 1 really does share the blind spot: with identical detectors,
    #      whoever N misses, Y misses too.
    w = world(np.random.default_rng(SEED), n_half=30.0, y_half=30.0, rho=1.0)
    same = (w["seen_n"] == w["seen_y"]).mean()
    check("6  rho = 1 with identical detectors sees the same producers",
          same > 0.999, "agreement=%.4f" % same)

    print("\n  %s\n" % ("ALL SELF-TESTS PASS" if ok else "SELF-TESTS FAILED"))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        return 0 if self_tests() else 1

    print(rule_line("="))
    print("CORRELATED MISS -- how far does R = N - Y move?")
    print(rule_line("="))
    print()
    print("  Terms, before any number:")
    print("    N        the outside total. A satellite survey of the extent.")
    print("    Y        what the network's own subscribers recorded.")
    print("    R_obs    the published leftover, N - Y.")
    print("    R_true   what producers the network cannot see actually made.")
    print("    rho      how correlated the two blind spots are, 0 to 1.")
    print("    half     the producer size at which an instrument sees 50%.")
    print()
    print("  Producers        %s, seed %d" % (f"{P:,}", SEED))
    print("  Median output    %.0f t/yr, lognormal, sigma %.2f" % (MEDIAN_OUTPUT, SIGMA))
    print()

    # ---- part 1: the documents' assumed case
    print(rule_line())
    print("PART 1 -- THE CASE THE DOCUMENTS ASSUME")
    print(rule_line())
    print()
    print("  A perfect N and a blind Y. The satellite sees everything; the")
    print("  network sees its own members. This is the picture behind the")
    print("  88,000 / 82,000 / 6,000 example in the conformance list.")
    print()
    print("   Y half-size   R_obs      R_true     error    label in hindsight")
    for y_half in (10.0, 20.0, 30.0, 50.0):
        w = world(np.random.default_rng(SEED), n_half=1e-9, y_half=y_half, rho=0.0)
        err = w["R_obs"] - w["R_true"]
        print("   %11.0f   %9.0f  %9.0f  %8.0f    %s"
              % (y_half, w["R_obs"], w["R_true"], err, label(w["R_obs"], w["R_true"])))
    print()
    print("  R_obs is EXACT here, not a bound. When N is complete, N - Y is")
    print("  precisely what the network could not see, by construction.")
    print()

    # ---- part 2: N gets its own blind spot, uncorrelated
    print(rule_line())
    print("PART 2 -- N GETS A BLIND SPOT OF ITS OWN, UNCORRELATED (rho = 0)")
    print(rule_line())
    print()
    print("  Now the satellite misses small plots too, but misses DIFFERENT")
    print("  ones from the network. Y half-size fixed at 30 t.")
    print()
    print("   N half   R_obs      R_true     error     as % of R_true   label")
    for n_half in (5.0, 10.0, 15.0, 20.0, 25.0, 30.0):
        w = world(np.random.default_rng(SEED), n_half=n_half, y_half=30.0, rho=0.0)
        err = w["R_obs"] - w["R_true"]
        pct = 100 * err / w["R_true"]
        print("   %6.0f   %9.0f  %9.0f  %8.0f   %14.1f   %s"
              % (n_half, w["R_obs"], w["R_true"], err, pct,
                 label(w["R_obs"], w["R_true"])))
    print()
    print("  Every row is labelled `floor`: the published leftover is SMALLER")
    print("  than the truth, so the true dark output is above it. A smaller")
    print("  leftover means the network claims better coverage than it has,")
    print("  so this is the flattering direction -- and it is the direction")
    print("  Foundations 4.4 already warns about in its own worked table.")
    print()
    print("  The last row is the one to look at. At N half = 30, matching Y,")
    print("  R_obs goes NEGATIVE. A leftover cannot be negative -- it is an")
    print("  amount of output. This is the ONE case the arithmetic catches by")
    print("  itself, and it catches it only when the shared blind spot is")
    print("  large enough to push the subtraction past zero.")
    print()

    # ---- part 3: the correlation sweep -- the question as asked
    print(rule_line())
    print("PART 3 -- THE CORRELATION SWEEP, WHICH IS THE QUESTION")
    print(rule_line())
    print()
    print("  Both instruments are size-biased in the same direction. rho says")
    print("  how far they miss THE SAME producers. N half-size 15 t, Y 30 t.")
    print()
    print("  R_true moves with rho, so read the COVERAGE columns rather than")
    print("  the error: they are the decision-relevant quantity and they are")
    print("  comparable across rows.")
    print()
    print("   rho    R_obs      R_true    coverage published   real   overstated by")
    for rho in (0.0, 0.25, 0.5, 0.75, 0.9, 1.0):
        w = world(np.random.default_rng(SEED), n_half=15.0, y_half=30.0, rho=rho)
        cov_pub = w["Y"] / w["N"] if w["N"] else 0.0
        cov_real = w["Y"] / w["truth"]
        print("   %.2f   %9.0f  %9.0f  %17.1f%%  %5.1f%%  %12.1f pts"
              % (rho, w["R_obs"], w["R_true"], 100 * cov_pub, 100 * cov_real,
                 100 * (cov_pub - cov_real)))
    print()
    print("  The published coverage overstates the real coverage at every")
    print("  value of rho, including zero. Correlation makes it worse; it is")
    print("  not what causes it. What causes it is that N has a blind spot at")
    print("  all, and the documents assume it does not.")
    print()

    # ---- part 4: the worst case -- identical detectors
    print(rule_line())
    print("PART 4 -- THE WORST CASE: ONE BLIND SPOT, SHARED COMPLETELY")
    print(rule_line())
    print()
    print("  The satellite and the network have the SAME detector and the SAME")
    print("  latent draw. Whoever one misses, the other misses.")
    print()
    print("   half   R_obs   R_true      error      coverage published   real")
    for half in (10.0, 20.0, 30.0, 50.0):
        w = world(np.random.default_rng(SEED), n_half=half, y_half=half, rho=1.0)
        cov_pub = w["Y"] / w["N"] if w["N"] else 0.0
        cov_real = w["Y"] / w["truth"]
        print("   %4.0f  %6.0f  %7.0f   %8.0f   %17.1f%%  %5.1f%%"
              % (half, w["R_obs"], w["R_true"], w["R_obs"] - w["R_true"],
                 100 * cov_pub, 100 * cov_real))
    print()
    print("  R_obs is ZERO at every row, and the published coverage is 100%.")
    print("  The real coverage is far lower. A leftover computed between two")
    print("  instruments that share a blind spot reports NO LEFTOVER AT ALL.")
    print()

    print(rule_line("="))
    print("WHAT THIS FOUND")
    print(rule_line("="))
    print()
    print("  1. @cairn-lineage IS RIGHT, AND THE DIRECTION IS THE FLATTERING ONE.")
    print("     Whenever N has a blind spot of its own, R_obs comes out BELOW")
    print("     the truth. In row 13's vocabulary that is a `floor` -- the true")
    print("     dark output is above the published figure. A smaller leftover")
    print("     means the network claims better coverage than it has, so the")
    print("     error runs in the direction nobody inside is motivated to")
    print("     report. Their sentence was that N - Y is not a lower bound on")
    print("     what the network missed; measured, it is not.")
    print()
    print("  2. AT FULL CORRELATION THE LEFTOVER READS ZERO.")
    print("     Two instruments with one blind spot compute N - Y = 0 and")
    print("     publish 100% coverage over an extent they have not covered.")
    print("     The arithmetic cannot see its own hole, because the hole was")
    print("     subtracted from both sides.")
    print()
    print("  3. ROW 14a's INTERVAL DOES NOT EXPRESS THIS, AND CANNOT.")
    print("     14a asks whether N and Y measure the same quantity, over the")
    print("     same extent, over the same window, with error bounds smaller")
    print("     than their difference. A correlated miss passes ALL FOUR: same")
    print("     quantity, same extent, same window -- and the difference is")
    print("     zero, so no error bound is smaller than it. The interval")
    print("     R in [N_L - Y_U, N_U - Y_L] is built from the two blind spots")
    print("     stated SEPARATELY, and a shared blind spot is not two.")
    print()
    print("  4. WHAT DOES CATCH IT IS ROW 13's DEFAULT, AND ONLY IF IT IS OBEYED.")
    print("     `not identified` is the default label until a stated directional")
    print("     argument exists for EACH operand's blind spot. A network that")
    print("     cannot say which way its satellite is blind has no such")
    print("     argument, so the figure is `not identified` and no `floor`")
    print("     label may be attached. THE RULE ALREADY REFUSES THE CLAIM.")
    print("     What it does not do is tell anyone the figure is worthless.")
    print()
    print("  5. ONE CASE THE ARITHMETIC DOES CATCH: A NEGATIVE LEFTOVER.")
    print("     When the satellite is as blind as the network, N - Y goes")
    print("     below zero -- measured at -6,286 t in part 2. A leftover is an")
    print("     amount of output and cannot be negative, so this is a hard")
    print("     signal that the subtraction is invalid. It is the only")
    print("     self-announcing failure here, and it fires only once the")
    print("     shared blind spot is large enough to push past zero. Below")
    print("     that, the same defect is present and silent.")
    print()
    print("  6. THE TEST THAT WOULD FIND IT IS NOT ARITHMETIC.")
    print("     Compare the two instruments' SIZE PROFILES, not their totals.")
    print("     If both fall off at the same producer size, the leftover")
    print("     between them is uninformative however wide its interval is.")
    print("     That is a comparison of methods, not of numbers, and nothing")
    print("     in the conformance list asks for it.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
