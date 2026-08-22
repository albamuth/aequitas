"""
q4_locked_ledgers.py -- Q4 of the scenario suite.

Question (author): if every American / everyone were entered honestly into
Aequitas, what fraction already sit past the point of a PERMANENT ledger lockout?

CRITICAL REFRAME (see the §3.5 flag in scenario_suite_METHOD.md).
"Permanently negative ledger" is NOT debit > credit -- that is the universal
condition (second law, §3.5: aggregate debit always exceeds credit for everyone).
The real test is the OP-4 discretionary gate applied over a lifetime:

    discretionary consumption  <=  rho * credit          (OP-4)

Credit accrues in TIME, and no human can earn faster than 24 h/day (IC-7). So the
maximum sustainable rate of discretionary consumption any human can ever command
is  rho * 24 h/day.  Anyone whose sustained consumption footprint exceeds that is
in permanent discretionary deficit -- locked to the basic-needs FLOOR for life, no
matter how much they work or divest. (Nobody starves: the floor is always covered,
§7.5. "Locked" = zero discretionary room, forever.)

    LOCKOUT THRESHOLD   T(rho) = rho * 24 h/day * 365 = rho * 8,760 embodied h/yr

Note T is anchored to the UNIVERSAL 24 h/day, so it is the same absolute number
of hours everywhere on Earth -- floor-independent, network-independent. That is
what makes a world comparison meaningful at all.

MATERIAL-ONLY, per A1. Financial instruments (stocks, bonds, crypto, options) are
abstract/fiat and DO NOT enter the ledger. The previously-wealthy carry only their
real MATERIAL consumption footprint. And per the author's framing we grant them the
best case: assume they DIVEST all material property. Divestment removes the
dischargeable material component but NOT permanent consumption debit (§3.2) and only
dilutes the holding-time creation-cost share (§6.2b) -- so the binding term is the
lifetime consumption footprint, which divestment cannot touch. Modelling on
consumption alone is the most generous possible test; property residue only worsens it.

WHAT THE MODEL PREDICTS (and tests):
  (1) Stripping paper wealth COLLAPSES the tail: wealth runs to ~1e6x the median
      (SCF/Forbes); material consumption is time- and biology-bounded and runs only
      to ~1e3x (Oxfam billionaire personal footprints). Tail compression ~1000x.
  (2) Only a THIN top slice is permanently locked -- the ultra-consumers, not the
      merely rich -- and the % is rho-dependent (sweep it).
  (3) MOST people GAIN discretionary room by joining (they sit below cohort average).

DATA ANCHORS (real, cited in-line):
  - Median US adult consumption footprint ~1,600 embodied labour-h/yr
    (median_lifestyle_RESULTS.md, this project).
  - Carbon-footprint inequality as the proxy for consumption inequality:
    WID 2022 / Chancel -- global top 1% ~110 t, top 0.1% ~467 t, top 0.01% ~2,530 t
    vs ~6.6 t average (https://wir2022.wid.world/chapter-6/). US median ~15-16 t.
  - Billionaire PERSONAL footprint (jets+yachts+estates, excl. investments)
    ~5,000-15,000 t CO2/yr -> ~300-1,000x the US median consumer
    (Oxfam 2023-24, https://www.oxfam.org/en/press-releases/
     billionaires-emit-more-carbon-pollution-90-minutes-average-person-does-lifetime).
  - Wealth tail for the compression contrast: SCF 2022 p99/median 70.9x;
    Forbes billionaire/median ~1.04e6x (disparity_ceiling_sim.py).

Run:  python q4_locked_ledgers.py
      python q4_locked_ledgers.py --test
      python q4_locked_ledgers.py --no-plots
"""
from __future__ import annotations

import argparse
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(7)

MEDIAN_FOOTPRINT_H = 1_600.0     # median US adult, embodied labour-h/yr (this project)
MAX_CREDIT_RATE_H = 24.0 * 365.0  # 8,760 -- physical max lifetime credit rate (IC-7)
N = 2_000_000

# --- material tail anchors (ratio to the US median consumer) ---
US_BILLIONAIRE_FOOTPRINT_RATIO = 670.0   # ~10,000 t personal / ~15 t median (Oxfam mid)
N_US_BILLIONAIRES = 700
US_HOUSEHOLDS = 131e6

# --- wealth tail, for the paper->material compression contrast (SCF/Forbes) ---
WEALTH_P99_OVER_MEDIAN = 70.9
WEALTH_BILLIONAIRE_OVER_MEDIAN = 1.04e6


# ---------------------------------------------------------------------------
# Consumption-footprint populations (embodied labour-h/yr), material-only
# ---------------------------------------------------------------------------

def build_us_footprints(n=N, rng=RNG):
    """US personal consumption footprint in embodied labour-h/yr, median-anchored.

    Lognormal body (sigma ~0.8 -> p99 ~6x median, matching US consumption/carbon
    inequality), a modest Pareto fattening above p99, and an explicit billionaire
    sliver at ~670x from Oxfam personal-footprint data. Consumption is far LESS
    unequal than wealth -- that is the point (test_tail_compression)."""
    f = rng.lognormal(mean=np.log(MEDIAN_FOOTPRINT_H), sigma=0.80, size=n)
    f *= MEDIAN_FOOTPRINT_H / np.median(f)          # re-anchor median exactly
    # fatten the top ~1% into a Pareto tail (personal footprints of the rich)
    top = rng.random(n) < 0.01
    f[top] *= (1 + rng.pareto(2.0, n)[top] * 2.5)
    # explicit billionaire sliver (personal, material-only)
    nb = max(1, int(n * N_US_BILLIONAIRES / US_HOUSEHOLDS))
    idx = rng.choice(n, nb, replace=False)
    f[idx] = MEDIAN_FOOTPRINT_H * US_BILLIONAIRE_FOOTPRINT_RATIO * rng.uniform(0.3, 1.5, nb)
    return f


def build_world_footprints(n=N, rng=RNG):
    """Global personal consumption footprint, embodied labour-h/yr. Median ~0.4x the
    US median (global avg carbon 6.6 t vs US ~15 t), with a FATTER relative tail
    (global inequality > US). Indicative only -- world data is coarse."""
    world_median = 0.40 * MEDIAN_FOOTPRINT_H        # ~640 h/yr
    f = rng.lognormal(mean=np.log(world_median), sigma=1.15, size=n)
    f *= world_median / np.median(f)
    top = rng.random(n) < 0.01
    f[top] *= (1 + rng.pareto(1.6, n)[top] * 4)
    # global billionaire sliver (~2,800 billionaires / ~2.3B households)
    nb = max(1, int(n * 2800 / 2.3e9))
    idx = rng.choice(n, nb, replace=False)
    f[idx] = MEDIAN_FOOTPRINT_H * US_BILLIONAIRE_FOOTPRINT_RATIO * rng.uniform(0.3, 1.5, nb)
    return f


# ---------------------------------------------------------------------------
# The lockout test
# ---------------------------------------------------------------------------

def threshold(rho):
    """Max sustainable discretionary consumption footprint (h/yr) = rho * max credit."""
    return rho * MAX_CREDIT_RATE_H


def pct_locked(footprints, rho):
    """% permanently locked = share whose footprint exceeds T(rho)."""
    return 100.0 * np.mean(footprints > threshold(rho))


def sweep(footprints, rhos=np.linspace(1.0, 3.0, 21)):
    return np.array([(r, pct_locked(footprints, r)) for r in rhos])


def pct_below_mean(footprints):
    """Share sitting below the cohort MEAN -> they gain room by joining (§5.2)."""
    return 100.0 * np.mean(footprints < np.mean(footprints))


# ---------------------------------------------------------------------------
# Report + tests
# ---------------------------------------------------------------------------

def _pctile_ratios(f):
    m = np.median(f)
    return {p: np.percentile(f, p) / m for p in (90, 99, 99.9, 99.99)}


def report():
    W = 76
    us = build_us_footprints()
    wo = build_world_footprints()
    print("=" * W)
    print("Q4 -- who is PAST the permanent-lockout point?   (material-only, per A1)")
    print("=" * W)
    print(f"Lockout threshold T(rho) = rho * {MAX_CREDIT_RATE_H:,.0f} embodied h/yr")
    print(f"  (rho * 24 h/day -- the max any human can ever earn; floor-independent)")
    print(f"US median footprint = {MEDIAN_FOOTPRINT_H:,.0f} h/yr; so T = "
          f"{threshold(1.0)/MEDIAN_FOOTPRINT_H:.1f}x median at rho=1, "
          f"{threshold(1.5)/MEDIAN_FOOTPRINT_H:.1f}x at rho=1.5, "
          f"{threshold(3.0)/MEDIAN_FOOTPRINT_H:.1f}x at rho=3.")
    print("-" * W)
    print("[1] % PERMANENTLY LOCKED vs rho  (thin slice -- the ultra-consumers):")
    print(f"    {'rho':>5} {'US %':>9} {'World %':>9}")
    for r in (1.0, 1.25, 1.5, 2.0, 2.5, 3.0):
        print(f"    {r:5.2f} {pct_locked(us, r):9.3f} {pct_locked(wo, r):9.3f}")
    print("-" * W)
    print("[2] PAPER -> MATERIAL tail compression (the A1 result):")
    ur = _pctile_ratios(us)
    print(f"    US CONSUMPTION footprint  p99/median = {ur[99]:6.1f}x   "
          f"billionaire/median ~ {US_BILLIONAIRE_FOOTPRINT_RATIO:.0f}x")
    print(f"    US WEALTH (SCF/Forbes)    p99/median = {WEALTH_P99_OVER_MEDIAN:6.1f}x   "
          f"billionaire/median ~ {WEALTH_BILLIONAIRE_OVER_MEDIAN:,.0f}x")
    print(f"    => stripping paper wealth compresses the tail ~"
          f"{WEALTH_BILLIONAIRE_OVER_MEDIAN/US_BILLIONAIRE_FOOTPRINT_RATIO:,.0f}x "
          f"(1e6x -> 1e3x).")
    print("-" * W)
    print("[3] MOST PEOPLE GAIN by joining (sit below cohort average, §5.2):")
    print(f"    US:    {pct_below_mean(us):.1f}% below the mean footprint")
    print(f"    World: {pct_below_mean(wo):.1f}% below the mean footprint")
    print("=" * W)
    print("Headline: material-only, only ~0.1-2% (rho-dependent) are permanently")
    print("locked -- the ultra-consumers, NOT the merely rich. Their edge was always")
    print("PAPER (excluded by A1); their physical over-consumption is bounded by time.")
    print("=" * W)


def test_threshold_universal():
    """T is anchored to 24 h/day -> same absolute hours regardless of floor/network."""
    assert abs(threshold(1.0) - 8760.0) < 1e-6
    assert threshold(2.0) == 2.0 * threshold(1.0)
    print(f"[ok] T(1)={threshold(1.0):,.0f} h/yr (=24h/day), rho-scaled, floor-independent")


def test_thin_slice_locked():
    """Only a small % locked, and it FALLS as rho rises (looser tolerance)."""
    us = build_us_footprints()
    p_lo, p_hi = pct_locked(us, 1.0), pct_locked(us, 3.0)
    assert 0.0 < p_hi < p_lo < 5.0, f"expected a thin, rho-decreasing slice, got {p_lo}->{p_hi}"
    print(f"[ok] US locked: {p_lo:.2f}% at rho=1 -> {p_hi:.2f}% at rho=3 (thin, decreasing)")


def test_median_person_safe():
    """The median person is nowhere near locked at any reasonable rho."""
    us = build_us_footprints()
    assert np.median(us) < threshold(1.0) / 4, "median should be <<threshold"
    print(f"[ok] median {np.median(us):,.0f} h/yr << T(1)={threshold(1.0):,.0f} "
          f"({threshold(1.0)/np.median(us):.1f}x headroom)")


def test_tail_compression():
    """Consumption tail (~1e3x) must be orders below the wealth tail (~1e6x)."""
    us = build_us_footprints()
    cons_bill = np.max(us) / np.median(us)
    assert cons_bill < WEALTH_BILLIONAIRE_OVER_MEDIAN / 100, "consumption tail not compressed"
    print(f"[ok] consumption billionaire ~{cons_bill:,.0f}x vs wealth "
          f"{WEALTH_BILLIONAIRE_OVER_MEDIAN:,.0f}x -- compressed ~"
          f"{WEALTH_BILLIONAIRE_OVER_MEDIAN/cons_bill:,.0f}x")


def test_most_gain():
    us = build_us_footprints()
    assert pct_below_mean(us) > 60, "a right-skewed footprint puts most below the mean"
    print(f"[ok] {pct_below_mean(us):.0f}% of Americans sit below the mean footprint (gain by joining)")


def run_tests():
    test_threshold_universal()
    test_thin_slice_locked()
    test_median_person_safe()
    test_tail_compression()
    test_most_gain()
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
    us = build_us_footprints()
    wo = build_world_footprints()

    # Fig 1: % locked vs rho
    su, sw = sweep(us), sweep(wo)
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(su[:, 0], su[:, 1], "o-", color=BLUE, lw=2, label="United States")
    ax.plot(sw[:, 0], sw[:, 1], "s-", color=ORANGE, lw=2, label="World (indicative)")
    ax.set_xlabel("ρ (tolerance dial — exogenous, local governance)")
    ax.set_ylabel("% permanently locked to the floor")
    ax.set_title("Only a thin top slice is permanently locked — and ρ moves it")
    ax.legend()
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "q4_fig1_locked_vs_rho.png"), dpi=130)
    plt.close(fig)

    # Fig 2: paper -> material tail compression (log bar)
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    cats = ["consumption\np99", "wealth\np99", "consumption\nbillionaire", "wealth\nbillionaire"]
    vals = [_pctile_ratios(us)[99], WEALTH_P99_OVER_MEDIAN,
            US_BILLIONAIRE_FOOTPRINT_RATIO, WEALTH_BILLIONAIRE_OVER_MEDIAN]
    colors = [BLUE, RED, BLUE, RED]
    ax.bar(cats, vals, color=colors)
    ax.set_yscale("log")
    ax.set_ylabel("× the median (log scale)")
    ax.set_title("A1 strips paper wealth: the material tail is ~1000× smaller")
    for i, v in enumerate(vals):
        ax.text(i, v * 1.3, f"{v:,.0f}×", ha="center", fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "q4_fig2_compression.png"), dpi=130)
    plt.close(fig)

    # Fig 3: US footprint distribution with the threshold line
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    ratios = us / MEDIAN_FOOTPRINT_H
    ax.hist(np.clip(ratios, 0, 20), bins=120, color=GRAY, alpha=0.8)
    for r, c in [(1.0, GREEN), (1.5, BLUE), (3.0, ORANGE)]:
        ax.axvline(threshold(r) / MEDIAN_FOOTPRINT_H, ls="--", color=c,
                   label=f"lock threshold at ρ={r}: {threshold(r)/MEDIAN_FOOTPRINT_H:.1f}× median")
    ax.set_xlabel("consumption footprint ÷ median")
    ax.set_ylabel("people")
    ax.set_title("Almost everyone sits far left of the lock line (right tail clipped at 20×)")
    ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "q4_fig3_distribution.png"), dpi=130)
    plt.close(fig)
    return ["q4_fig1_locked_vs_rho.png", "q4_fig2_compression.png", "q4_fig3_distribution.png"]


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
