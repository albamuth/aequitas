"""
pledge_reserve.py -- the contingent-reserve pledge incentive (OP-16 hazard half).

CONTEXT (settled ruling, session 2026-08-14; see PLEDGE_RESERVE.md):
Pledges are PERMANENT, non-revocable grants of debit-room. A task's pledges first
cushion its labour/material cost (pro-rata by hours ON THE TASK). Any SURPLUS is
NOT consumable -- surplus-as-profit was rejected on the axioms: banking the
excess as spendable room re-creates a channel for accumulating consumption
advantage, which the system's equality commitments forbid. Instead the surplus becomes a
CONTINGENT RESERVE: earmarked, non-spendable room that only activates against a
VERIFIED future cost causally traceable to the task (the doer's injury/illness,
resurfaced site remediation, third-party harm -- "any task-caused cost").

    reserve R  = surplus pledged hours, held earmarked to the task's causal tail
    coverage c = R / E[tail]            (how much of the expected tail is pre-funded)

Two guards are baked in and TESTED here:
  (G1) Overflow reverts to the causer. The reserve is a BUFFER, not a shield: when
       a reserve is exhausted, residual task-caused debit falls back on the doer/
       co-op (property/consumption debit, Foundations §3.2 / §3.7). Without G1,
       third-party/environmental coverage licenses carelessness (moral hazard).
  (G2) Causation by physical-trace. A claim draws the reserve only if the harm
       left a trace linking it to the task; diffuse/latent harm with no individual
       trace is handled by a cohort/actuarial convention, never by an open claim.
       Modelled as a fraud-leakage knob: padded claims drain the reserve.

WHAT THIS SIM TESTS (two claims + the fraud knob):
  [A] CLEARING. Under flat credit alone (A2 -- same hours = same credit for safe
      or hazardous work), a risk-bearing worker AVOIDS hazardous work because it
      carries an expected future health debit that hits THEIR OWN ledger. Result:
      chronic shortage -- the 45y time-banking finding, and the live OP-16. The
      contingent reserve removes the expected uncovered cost, so the job clears
      once society pledges ~enough to cover the tail. Over-pledging is a
      DEMAND-GATED BOND, not a wage premium.
  [B] CARE. With G1 (buffer+overflow) doers keep care up because they eat the
      residual; a full SHIELD (no overflow) drives care -> 0 and harm -> max.

The reserve is non-consumable BY CONSTRUCTION (it only ever cancels a task-caused
cost, never adds spendable room), so it creates no consumption advantage. That is
a design fact, not a simulated result, and needs no chart here.

Everything here is a STRUCTURAL demonstration with illustrative, clearly-flagged
constants (embodied labour-hours), not a forecast. The results are the SHAPES
(clearing at c~1, shield kills care, contingent respects the ceiling), which are
robust to the constants; the absolute numbers are not claimed.

Run:  python pledge_reserve.py
      python pledge_reserve.py --test
      python pledge_reserve.py --no-plots
"""
from __future__ import annotations

import argparse
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(14)

# --- units: embodied labour-hours. Illustrative, flagged. ---
N = 200_000

# [A] clearing model -----------------------------------------------------------
# A pool of potential workers for a hazardous task. Each carries an expected
# PERSONAL future hazard-cost X_i (health debit that would hit their own ceiling),
# heavy-tailed (most jobs mild strain; rare severe exposure). Each also has an
# intrinsic tolerance t_i -- hours of hazard-disutility they will absorb for free
# (some people genuinely don't mind dangerous work). A worker takes the job iff
# the UNCOVERED expected cost is within their tolerance.
MEAN_HAZARD_COST_H = 300.0     # mean personal expected tail per worker-stint (h)
HAZARD_SIGMA = 1.1             # lognormal shape -> heavy tail (rare severe harm)
MEAN_TOLERANCE_H = 60.0        # mean "will absorb for free" (h); << mean cost
TOLERANCE_SIGMA = 0.9
DEMAND_FRACTION = 0.60         # fraction of the pool needed to staff the work


def build_workers(n=N, rng=RNG):
    X = rng.lognormal(mean=np.log(MEAN_HAZARD_COST_H), sigma=HAZARD_SIGMA, size=n)
    X *= MEAN_HAZARD_COST_H / np.mean(X)            # re-anchor mean exactly
    t = rng.lognormal(mean=np.log(MEAN_TOLERANCE_H), sigma=TOLERANCE_SIGMA, size=n)
    t *= MEAN_TOLERANCE_H / np.mean(t)
    return X, t


def willing_fraction(coverage, X, t):
    """Fraction of workers who take the hazardous job at a given reserve coverage.

    Reserve covers fraction `coverage` of each worker's expected tail; a worker
    takes the job iff the uncovered remainder is within their free tolerance."""
    uncovered = X * (1.0 - coverage)
    return float(np.mean(uncovered <= t))


def clearing_coverage(X, t, demand=DEMAND_FRACTION, grid=None):
    """Minimum reserve coverage at which willing supply meets demand (or nan)."""
    grid = np.linspace(0.0, 1.0, 101) if grid is None else grid
    for c in grid:
        if willing_fraction(c, X, t) >= demand:
            return float(c)
    return float("nan")


# [B] care model ---------------------------------------------------------------
# A doer chooses care a in [0,1] at quadratic effort cost k*a^2. Expected
# task-caused harm falls with care: H(a) = H0*(1-a). Reserve R absorbs harm up to
# R. Under BUFFER (G1) the doer eats the residual max(0, H(a)-R); under SHIELD the
# doer eats nothing, so care is pure cost and collapses to zero.
HARM_MAX_H = 500.0             # H0: worst-case expected task-caused harm (h)
CARE_COST_K = 400.0           # k: effort-hours to reach full care (quadratic)


def _harm(a):
    return HARM_MAX_H * (1.0 - a)


def optimal_care(R, regime, k=CARE_COST_K):
    """Grid-search the care level a doer picks to minimise their OWN cost."""
    A = np.linspace(0.0, 1.0, 1001)
    care_cost = k * A ** 2
    if regime == "buffer":
        residual = np.maximum(0.0, _harm(A) - R)
    elif regime == "shield":
        residual = np.zeros_like(A)
    else:
        raise ValueError(regime)
    total = care_cost + residual
    a = float(A[int(np.argmin(total))])
    return a, _harm(a)


# fraud knob (G2) --------------------------------------------------------------
def reserve_shortfall(fraud_rate, trace_catch, R, legit_tail):
    """Reserve drained by legitimate claims + LEAKED padded claims. Returns the
    fraction of the legitimate tail left UNCOVERED once the reserve is exhausted.

    fraud_rate  : padded claim volume as a fraction of the legit tail
    trace_catch : share of padded claims the physical-trace test rejects (G2)
    """
    leaked = fraud_rate * (1.0 - trace_catch) * legit_tail
    drain = legit_tail + leaked
    uncovered = max(0.0, drain - R)
    return uncovered / legit_tail if legit_tail > 0 else 0.0


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report():
    W = 78
    X, t = build_workers()
    print("=" * W)
    print("PLEDGE RESERVE -- the contingent-reserve incentive for hazardous work")
    print("  (OP-16 hazard half; permanent pledges; surplus-as-profit rejected)")
    print("=" * W)

    # [A]
    print("[A] CLEARING -- does the toxic job get staffed?")
    print(f"    Need {DEMAND_FRACTION*100:.0f}% of the pool. Willing supply vs reserve coverage c:")
    print(f"    {'c':>6} {'willing %':>11}")
    for c in (0.0, 0.25, 0.5, 0.75, 0.9, 1.0):
        print(f"    {c:6.2f} {willing_fraction(c, X, t)*100:11.1f}")
    c_star = clearing_coverage(X, t)
    print(f"    -> at c=0 (flat credit only): {willing_fraction(0.0, X, t)*100:.1f}% "
          f"willing  => SHORTAGE (the OP-16 / time-banking result).")
    print(f"    -> clears at coverage c* = {c_star:.2f}: pledges must ~cover the tail.")
    print(f"       Over-pledging is a DEMAND-GATED BOND, not a wage premium.")
    print("-" * W)

    # [B]
    print("[B] CARE -- does overflow-reverts (G1) stop moral hazard?")
    R_care = 0.5 * HARM_MAX_H
    a_b, h_b = optimal_care(R_care, "buffer")
    a_s, h_s = optimal_care(R_care, "shield")
    print(f"    Reserve R = {R_care:.0f} h; worst-case harm H0 = {HARM_MAX_H:.0f} h.")
    print(f"    {'regime':>10} {'care a':>9} {'harm (h)':>10}")
    print(f"    {'shield':>10} {a_s:9.2f} {h_s:10.0f}   (no residual -> care collapses)")
    print(f"    {'buffer':>10} {a_b:9.2f} {h_b:10.0f}   (eats residual -> keeps care up)")
    print(f"    -> shield harm is {h_s/max(h_b,1e-9):.1f}x the buffer harm. "
          f"G1 is the moral-hazard kill-switch.")
    print("-" * W)

    # fraud
    print("[G2] FRAUD -- how much padded-claim leakage can the reserve absorb?")
    legit, R = 100.0, 130.0
    print(f"    Legit tail = {legit:.0f} h, reserve R = {R:.0f} h (30% headroom).")
    print(f"    {'fraud rate':>11} {'trace catch':>12} {'legit uncovered %':>18}")
    for fr, tc in [(0.2, 0.9), (0.5, 0.9), (0.5, 0.6), (1.0, 0.9), (1.0, 0.5)]:
        u = reserve_shortfall(fr, tc, R, legit)
        print(f"    {fr:11.2f} {tc:12.2f} {u*100:18.1f}")
    print(f"    -> good physical-trace (high catch) keeps legit claims whole; weak")
    print(f"       trace + high fraud exhausts the reserve and denies real claimants.")
    print("=" * W)
    print("HEADLINE: the contingent reserve clears hazardous work as a demand-gated")
    print("bond (c*~cover-the-tail) and preserves care via overflow-reverts. The")
    print("surplus stays non-spendable, so it creates no consumption advantage. It")
    print("solves the HAZARD half of OP-16 only; tedium/indignity remain open.")
    print("Integrity rests on G2 (physical-trace causation).")
    print("=" * W)


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def test_flat_credit_shortage():
    """At c=0 (flat credit alone) willing supply falls short of demand."""
    X, t = build_workers()
    w0 = willing_fraction(0.0, X, t)
    assert w0 < DEMAND_FRACTION, f"expected shortage at c=0, got {w0:.2f} >= {DEMAND_FRACTION}"
    print(f"[ok] c=0: {w0*100:.1f}% willing < {DEMAND_FRACTION*100:.0f}% demand -> shortage (OP-16)")


def test_coverage_clears_and_is_monotone():
    """Willing supply rises monotonically with coverage and clears by c=1."""
    X, t = build_workers()
    cs = np.linspace(0, 1, 21)
    ws = [willing_fraction(c, X, t) for c in cs]
    assert all(b >= a - 1e-9 for a, b in zip(ws, ws[1:])), "supply not monotone in coverage"
    assert ws[-1] >= DEMAND_FRACTION, "does not clear even at full coverage"
    c_star = clearing_coverage(X, t)
    assert 0.0 < c_star <= 1.0, f"clearing coverage out of range: {c_star}"
    print(f"[ok] supply monotone in c; clears at c*={c_star:.2f} (demand-gated bond)")


def test_shield_kills_care():
    """A full shield drives care to ~0; the buffer keeps care up and harm down."""
    R = 0.5 * HARM_MAX_H
    a_b, h_b = optimal_care(R, "buffer")
    a_s, h_s = optimal_care(R, "shield")
    assert a_s < 0.01, f"shield should collapse care to ~0, got a={a_s}"
    assert a_b > a_s and h_b < h_s, "buffer should raise care and lower harm"
    assert h_s > 1.5 * h_b, f"shield harm should dominate: {h_s} vs {h_b}"
    print(f"[ok] shield a={a_s:.2f} (harm {h_s:.0f}) vs buffer a={a_b:.2f} (harm {h_b:.0f}) "
          f"-> G1 preserves care")


def test_fraud_erodes_reserve_and_trace_defends():
    """More fraud -> more uncovered legit claims; better physical-trace -> fewer."""
    legit, R = 100.0, 130.0
    u_lo = reserve_shortfall(0.2, 0.9, R, legit)
    u_hi = reserve_shortfall(1.0, 0.9, R, legit)
    u_weaktrace = reserve_shortfall(1.0, 0.5, R, legit)
    assert u_lo <= u_hi, "more fraud should not reduce uncovered legit claims"
    assert u_weaktrace >= u_hi, "weaker trace should uncover more legit claims"
    assert u_lo == 0.0, "reserve headroom should absorb modest well-policed fraud"
    print(f"[ok] fraud erodes reserve (uncovered {u_lo*100:.0f}%->{u_hi*100:.0f}%); "
          f"weak trace worse ({u_weaktrace*100:.0f}%) -> integrity rests on G2")


def run_tests():
    test_flat_credit_shortage()
    test_coverage_clears_and_is_monotone()
    test_shield_kills_care()
    test_fraud_erodes_reserve_and_trace_defends()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def make_plots():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BLUE, ORANGE, RED, GRAY, GREEN = "#2b6cb0", "#dd6b20", "#c53030", "#718096", "#2f855a"
    plt.rcParams.update({"font.size": 11, "axes.titleweight": "bold",
                         "figure.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    X, t = build_workers()

    # Fig 1: clearing -- willing supply vs coverage
    cs = np.linspace(0, 1, 101)
    ws = np.array([willing_fraction(c, X, t) for c in cs]) * 100
    c_star = clearing_coverage(X, t)
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(cs, ws, "-", color=BLUE, lw=2.5, label="willing supply")
    ax.axhline(DEMAND_FRACTION * 100, ls="--", color=RED, label=f"demand ({DEMAND_FRACTION*100:.0f}%)")
    if not np.isnan(c_star):
        ax.axvline(c_star, ls=":", color=GREEN, lw=2,
                   label=f"clears at c*={c_star:.2f}")
    ax.set_xlabel("reserve coverage c = R / expected tail")
    ax.set_ylabel("% of pool willing to take the hazardous job")
    ax.set_title("Flat credit under-staffs hazardous work; the reserve clears it")
    ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "pr_fig1_clearing.png"), dpi=130)
    plt.close(fig)

    # Fig 2: care -- harm vs reserve, shield vs buffer
    Rs = np.linspace(0, HARM_MAX_H, 60)
    harm_b = np.array([optimal_care(R, "buffer")[1] for R in Rs])
    harm_s = np.array([optimal_care(R, "shield")[1] for R in Rs])
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(Rs, harm_s, "-", color=RED, lw=2.5, label="shield (no overflow)")
    ax.plot(Rs, harm_b, "-", color=GREEN, lw=2.5, label="buffer + overflow (G1)")
    ax.set_xlabel("reserve size R (h)")
    ax.set_ylabel("realised task-caused harm (h)")
    ax.set_title("Overflow-reverts (G1) is the moral-hazard kill-switch")
    ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "pr_fig2_care.png"), dpi=130)
    plt.close(fig)
    return ["pr_fig1_clearing.png", "pr_fig2_care.png"]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-plots", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    report()
    if not args.no_plots:
        for f in make_plots():
            print("wrote", f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
