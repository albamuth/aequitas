"""
disparity_ceiling_sim.py -- the disparity-ceiling proof (queue #8), agent-based.

Establishes three results about consumption inequality under Aequitas, where
discretionary consumption is gated by  D_i <= rho * C_i  (OP-4 shape), credit C
accrues in equally-distributed, non-transferable time (A3), and no account may
claim > 24 h/day (IC-7):

  CLAIM 1 (headline)  -- the consumption disparity is bounded by 24/F and is
                         INDEPENDENT of rho; money's is orders of magnitude larger.
  CLAIM 2 (prime-rate)-- a rho can be chosen so aggregate demand matches productive
                         capacity, and it moves predictably under shocks (tighten in
                         a shortage). rho is exogenous; Aequitas is agnostic to it.
  CLAIM 3 (security)  -- the ceiling is INVARIANT to fraud, because IC-7 caps every
                         account (honest or not) at 24 h/day. Fraud fills the 2.4x
                         band but cannot create an outlier beyond it. Money can.
  CLAIM 4 (Methuselah)-- credit/debit are CUMULATIVE event-log tallies (A6) and credit
                         is never spent (A3): the gate D<=rho*C is a ratio checked at
                         each event. A lifelong hoarder who splurges is clipped to
                         rho*C -- there is no 'banked' lump to blow. Equal-age disparity
                         is exactly 24/F; the ONLY spread beyond it is age.

Model. N agents. Each works w_i in [0, 24-F] discretionary hours/day on top of the
self-care floor F (credited to everyone, A2/§6.1b), so the credit rate is
c_i = F + w_i in [F, 24]. Consumption is d_i = min(appetite_i, rho * c_i). The
disparity CEILING is the most anyone may consume vs a bare-subsistence person's
allowance:  max(rho*c) / (rho*F) = 24/F  -- rho cancels.

Run:  python disparity_ceiling_sim.py            # run all, write plots
      python disparity_ceiling_sim.py --test     # self-tests only
"""
from __future__ import annotations

import argparse
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(42)

F = 10.0            # self-care floor, h/day (credited to all)
DAY = 24.0
CEILING = DAY / F   # 2.4x -- the structural bound
N = 200_000


# ---------------------------------------------------------------------------
# Population
# ---------------------------------------------------------------------------

def draw_population(n=N, rng=RNG):
    """Credit rate c_i in [F, 24] for a heterogeneous population.

    ~35% do little/no paid work (children, retired, unwell, between jobs) -> w~0;
    the rest work a spread centred on a full-ish day. Only the RANGE [F,24] matters
    for the ceiling; the shape only affects the observed (tighter) spread.
    """
    works = rng.random(n) > 0.35
    w = np.where(
        works,
        np.clip(rng.normal(6.0, 3.0, n), 0, DAY - F),   # workers: ~6 h/day discretionary
        rng.uniform(0, 1.5, n),                          # non-workers: little
    )
    return F + w                                         # c_i in [F, 24]


# --- REAL US distributions (all median-normalised) ---
# Wealth: 2022 Survey of Consumer Finances (Federal Reserve). Median family net
# worth $192,900; p90 $1,920,758 (9.96x); p95 $3,779,600 (19.6x); p99 $13,666,778
# (70.9x); mean $1,063,700 (5.5x median). Top-1% wealth share ~32% (Fed DFA).
# The billionaire tail (Forbes) reaches ~$200B ~ 1e6x the median -- the SCF
# under-samples it, so we splice it in explicitly.
SCF_WEALTH_RATIOS = {"p90": 9.96, "p95": 19.6, "p99": 70.9, "mean": 5.51}
SCF_BILLIONAIRE_OVER_MEDIAN = 200e9 / 192_900          # ~1.04e6

# Income: p99/median ~7x, p99.9/median ~30x (US, IRS/CBO shape) -- far tighter than
# wealth, because income can't compound the way holdings do.
INCOME_LOGNORMAL_SIGMA = 0.86                           # Gini ~0.46, US-like


def real_wealth(n=N, rng=RNG):
    """US net-worth distribution calibrated to the 2022 SCF percentiles: a lognormal
    body (sigma chosen to hit p90=9.96x, p99~71x) plus a Pareto top tail and an
    explicit Forbes billionaire sliver. Median-normalised. Self-test verifies the
    fit against the real SCF ratios."""
    sigma = 1.80                                        # ln-body: p90=exp(1.80*1.2816)=9.9x
    w = rng.lognormal(mean=0.0, sigma=sigma, size=n)
    w /= np.median(w)
    # fatten the very top into a Pareto tail (wealth exponent ~1.5) above ~p99
    top = rng.random(n) < 0.01
    w[top] *= (1 + rng.pareto(1.5, n)[top] * 6)
    # explicit billionaire sliver: ~700 US billionaires / ~131M households
    nb = max(1, int(n * 700 / 131e6))
    idx = rng.choice(n, nb, replace=False)
    w[idx] = SCF_BILLIONAIRE_OVER_MEDIAN * rng.uniform(0.02, 1.0, nb)  # $4B..$200B
    return w


def real_income(n=N, rng=RNG):
    inc = rng.lognormal(mean=0.0, sigma=INCOME_LOGNORMAL_SIGMA, size=n)
    return inc / np.median(inc)


def money_capacity(n=N, rng=RNG):
    """Back-compat: (income, wealth) on real US calibration."""
    return real_income(n, rng), real_wealth(n, rng)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def ratio_p999_p50(x):
    return np.percentile(x, 99.9) / np.median(x)


def gini(x):
    x = np.sort(np.asarray(x, float))
    n = len(x)
    cum = np.cumsum(x)
    return (2 * np.sum((np.arange(1, n + 1)) * x) - (n + 1) * cum[-1]) / (n * cum[-1])


# ---------------------------------------------------------------------------
# CLAIM 1 -- ceiling is bounded and rho-independent
# ---------------------------------------------------------------------------

def claim1_ceiling_vs_rho(rhos=np.linspace(1.0, 3.0, 21)):
    c = draw_population()
    # everyone at their ceiling (appetite unbounded) = the WORST-case spread
    out = []
    for rho in rhos:
        d = rho * c                       # consume at ceiling
        # disparity = most anyone consumes vs a bare-subsistence allowance (rho*F)
        top_vs_floor = np.max(d) / (rho * F)
        p999_50 = ratio_p999_p50(d)
        out.append((rho, top_vs_floor, p999_50, gini(d)))
    return np.array(out)


# ---------------------------------------------------------------------------
# CLAIM 2 -- a rho clears the market; shocks move it
# ---------------------------------------------------------------------------

def demand_of_rho(c, appetite, rho):
    """Aggregate consumption demand when each agent may take up to rho*c_i."""
    return np.sum(np.minimum(appetite, rho * c))


def clearing_rho(c, appetite, capacity, rhos=np.linspace(0.5, 4.0, 200)):
    dem = np.array([demand_of_rho(c, appetite, r) for r in rhos])
    if dem[-1] < capacity:
        return None, rhos, dem            # post-scarcity: never binds
    idx = np.argmin(np.abs(dem - capacity))
    return rhos[idx], rhos, dem


def claim2_market_and_shocks():
    c = draw_population()
    # appetite (debit-hours/day): people want ~1.6x their own hours (materials/energy
    # beyond labour), heterogeneous -> aggregate demand can exceed capacity.
    appetite = np.maximum(0.1, rng_appetite(c))
    # productive capacity ~ total labour supplied x productivity
    productivity = 1.15
    K = productivity * np.sum(c)

    base_rho, rhos, dem = clearing_rho(c, appetite, K)
    # shocks
    scenarios = {"baseline": (c, appetite, K)}
    # 1. population decline -15% (fewer workers AND fewer consumers)
    keep = RNG.random(len(c)) > 0.15
    scenarios["pop -15%"] = (c[keep], appetite[keep], productivity * np.sum(c[keep]))
    # 2. disaster: capacity -30% (goods destroyed / supply shock)
    scenarios["disaster -30% capacity"] = (c, appetite, 0.70 * K)
    # 3. pollution: retroactive debit rises -> each unit of consumption costs +25%
    #    debit -> effective appetite (debit-hours) rises 25% for the same real goods
    scenarios["pollution +25% debit"] = (c, 1.25 * appetite, K)

    results = {}
    for name, (cc, aa, KK) in scenarios.items():
        r, _, _ = clearing_rho(cc, aa, KK)
        results[name] = r
    return results, base_rho, rhos, dem, K


def rng_appetite(c):
    # appetite scales with a person's own scale plus heterogeneous wants
    return c * RNG.lognormal(mean=np.log(1.6), sigma=0.5, size=len(c))


# ---------------------------------------------------------------------------
# CLAIM 3 -- fraud-invariance (IC-7 caps everyone at 24 h/day)
# ---------------------------------------------------------------------------

def claim3_fraud(rho=1.5, fraud_rates=np.linspace(0, 0.4, 9), inflate=2.0):
    c = draw_population()
    out = []
    for phi in fraud_rates:
        cheat = RNG.random(len(c)) < phi
        c_claim = c.copy()
        # fraudsters inflate claimed hours -- but IC-7 caps the claim at 24 h/day
        c_claim[cheat] = np.minimum(c[cheat] * inflate, DAY)
        d = rho * c_claim
        out.append((phi, np.max(d) / (rho * F), gini(d)))
    return np.array(out)


# ---------------------------------------------------------------------------
# CLAIM 4 -- the cumulative-ledger / Methuselah test.
#
# Credit C and debit D are CUMULATIVE running tallies from the event log (A6:
# derived, not stored), in hours. Credit is NEVER spent -- a purchase adds to D,
# it never draws C down (A3: credit is not a currency). The gate  D <= rho*C  is
# re-checked at each event; a purchase that would breach it is BLOCKED (clipped).
#
# This kills the "hoard 70 years of credit, splurge it in one lump" attack WITHOUT
# any separate "rate gate": a splurge can only front-load a person's OWN allowance
# (bounded by rho*C), never exceed it. At EQUAL AGE the disparity is exactly 24/F;
# the ONLY spread beyond 24/F is age (time lived, not class).
# ---------------------------------------------------------------------------

def _ledger_run(c, rho, T, strategy):
    """Run a running-tally ledger for agents with per-period credit rates `c` over
    T periods. Credit and debit are cumulative; the dynamic gate D(t) <= rho*C(t)
    is enforced every period (a breaching purchase is clipped). Credit is never
    spent. Returns (C_final, D_final, attempted_final)."""
    c = np.asarray(c, float)
    C = np.zeros_like(c)          # cumulative credit (only ever grows, absent fraud)
    D = np.zeros_like(c)          # cumulative debit
    attempted = np.zeros_like(c)  # cumulative UNCLIPPED attempt (to detect blocking)
    for t in range(1, T + 1):
        C += c                                    # credit accrues at the rate
        want = strategy(c, rho, t, T)             # attempted consumption this period
        attempted += want
        room = np.maximum(0.0, rho * C - D)       # dynamic gate on the running tallies
        D += np.minimum(want, room)               # purchase blocked above the ratio
    return C, D, attempted


def steady(c, rho, t, T):
    """Consume at your own rate every period."""
    return rho * c


def hoarder_then_splurge(c, rho, t, T):
    """Consume NOTHING for a lifetime, then try to blow the entire hoard in the
    final period -- attempting 10x more than the gate could ever allow."""
    return np.where(t == T, rho * c * T * 10.0, 0.0)


def claim4_frontloading(rho=1.5, T=40):
    """Equal-age population, credit rates spanning [F, 24]. Steady consumer vs a
    lifelong hoarder who splurges at the end -- both under the cumulative gate."""
    c = np.linspace(F, DAY, 1000)
    return c, _ledger_run(c, rho, T, steady), _ledger_run(c, rho, T, hoarder_then_splurge)


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

    # Fig 1: ceiling vs rho, with REAL US money reference lines (SCF / Forbes)
    d1 = claim1_ceiling_vs_rho()
    inc, wea = real_income(), real_wealth()
    inc_p99 = np.percentile(inc, 99) / np.median(inc)
    wea_p99 = np.percentile(wea, 99) / np.median(wea)
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(d1[:, 0], d1[:, 1], "o-", color=BLUE, lw=2,
            label=f"AEQUITAS consumption ceiling = {CEILING:.1f}× (flat)")
    ax.axhline(inc_p99, ls=":", color=ORANGE,
               label=f"US income, top 1% / median ≈ {inc_p99:.0f}×")
    ax.axhline(wea_p99, ls=":", color=RED,
               label=f"US WEALTH, top 1% / median ≈ {wea_p99:.0f}×  (SCF 2022)")
    ax.axhline(SCF_BILLIONAIRE_OVER_MEDIAN, ls="-.", color="black",
               label=f"US billionaire / median ≈ {SCF_BILLIONAIRE_OVER_MEDIAN:,.0f}×  (Forbes)")
    ax.set_yscale("log")
    ax.set_ylim(1, 5e6)
    ax.set_xlabel("ρ (tolerance ratio — the exogenous dial)")
    ax.set_ylabel("disparity vs the median (log scale)")
    ax.set_title("Aequitas caps command-over-resources at 24/F — money runs to 10⁶×")
    ax.legend(fontsize=8.5, loc="center right")
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "ceiling_fig1_rho.png"), dpi=130)
    plt.close(fig)

    # Fig 2: demand(rho) vs capacity + shocks
    results, base_rho, rhos, dem, K = claim2_market_and_shocks()
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    ax.plot(rhos, dem / K, color=BLUE, lw=2, label="demand(ρ) / baseline capacity")
    ax.axhline(1.0, ls="--", color=GRAY, label="capacity (market clears)")
    if base_rho:
        ax.axvline(base_rho, ls=":", color=GREEN, label=f"clearing ρ* = {base_rho:.2f}")
    ax.set_xlabel("ρ (tolerance ratio)")
    ax.set_ylabel("aggregate demand ÷ capacity")
    ax.set_title("A ρ clears the market — and shocks move it (the 'prime-rate' dial)")
    txt = "clearing ρ* under shocks:\n" + "\n".join(
        f"  {k}: {'—' if v is None else f'{v:.2f}'}" for k, v in results.items())
    ax.text(0.98, 0.05, txt, transform=ax.transAxes, ha="right", va="bottom",
            fontsize=8.5, family="monospace",
            bbox=dict(boxstyle="round", fc="white", ec=GRAY))
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "ceiling_fig2_clearing.png"), dpi=130)
    plt.close(fig)

    # Fig 3: fraud invariance
    d3 = claim3_fraud()
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    ax.plot(d3[:, 0] * 100, d3[:, 1], "o-", color=BLUE, label="disparity ceiling")
    ax.axhline(CEILING, ls="--", color=GREEN, label=f"24/F = {CEILING:.1f}×")
    ax.set_ylim(0, CEILING * 1.4)
    ax.set_xlabel("fraud rate (% of accounts inflating claimed hours ×2)")
    ax.set_ylabel("consumption disparity ceiling")
    ax.set_title("Fraud CANNOT break the ceiling — IC-7 caps every account at 24 h/day")
    ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "ceiling_fig3_fraud.png"), dpi=130)
    plt.close(fig)

    # Fig 4: cumulative ledger — hoard-then-splurge is clipped to the ρ·C envelope
    rho4, T4, cc = 1.5, 40, DAY                       # a max-rate (c=24) worker
    yrs = np.arange(1, T4 + 1)
    env = rho4 * cc * yrs                              # the ρ·C(t) ceiling envelope
    d_steady = np.cumsum(np.full(T4, rho4 * cc))      # consume at your rate each year
    d_hoard = np.zeros(T4); d_hoard[-1] = rho4 * cc * T4   # nothing, then splurge (clipped)
    d_hoard = np.minimum(np.cumsum(d_hoard), env)     # gate clips the splurge to the envelope
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(yrs, env, "--", color=RED, lw=2, label="ρ·C(t) — the gate ceiling")
    ax.plot(yrs, d_steady, "-", color=BLUE, lw=2, label="steady consumer")
    ax.step(yrs, d_hoard, where="post", color=GREEN, lw=2, label="hoard 39 yrs, then splurge")
    ax.annotate("splurge clipped to ρ·C\n(no 'banked' lump to blow)",
                xy=(T4, env[-1]), xytext=(T4 * 0.42, env[-1] * 0.82),
                fontsize=9, ha="left", arrowprops=dict(arrowstyle="->", color=GRAY))
    ax.set_xlabel("age (years worked)")
    ax.set_ylabel("cumulative consumption (embodied h)")
    ax.set_title("Credit isn't a balance: a lifelong hoarder can't beat ρ·C — or 24/F")
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "ceiling_fig4_frontloading.png"), dpi=130)
    plt.close(fig)
    return ["ceiling_fig1_rho.png", "ceiling_fig2_clearing.png", "ceiling_fig3_fraud.png",
            "ceiling_fig4_frontloading.png"]


# ---------------------------------------------------------------------------
# Report + tests
# ---------------------------------------------------------------------------

def report():
    W = 74
    print("=" * W)
    print(f"DISPARITY-CEILING SIM   (F={F:.0f} h/day  ->  24/F ceiling = {CEILING:.1f}×)")
    print("=" * W)
    d1 = claim1_ceiling_vs_rho()
    print("CLAIM 1 — ceiling vs ρ (should be flat at ≤ 2.4×):")
    print(f"  Aequitas consumption ceiling: {d1[0,1]:.2f}×  (flat across ρ∈[1,3]; "
          f"range {d1[:,1].min():.2f}-{d1[:,1].max():.2f})")
    inc, wea = real_income(), real_wealth()
    ip = np.median(inc); wp = np.median(wea)
    print("  vs REAL US disparity (ratio to the median):")
    print(f"    money INCOME  p90={np.percentile(inc,90)/ip:5.1f}×  p99={np.percentile(inc,99)/ip:5.1f}×  p99.9={np.percentile(inc,99.9)/ip:5.1f}×")
    print(f"    money WEALTH  p90={np.percentile(wea,90)/wp:5.1f}×  p99={np.percentile(wea,99)/wp:5.1f}×  "
          f"(SCF real: 10× / 71×)")
    print(f"    billionaire / median = {SCF_BILLIONAIRE_OVER_MEDIAN:,.0f}×  (Forbes ~$200B / SCF median $192,900)")
    print(f"  => Aequitas caps command-over-resources at ~{d1[0,1]:.1f}×; money runs to ~10^6×.")
    print("-" * W)
    results, base_rho, *_ = claim2_market_and_shocks()
    print("CLAIM 2 — clearing ρ* (baseline) and under shocks:")
    for k, v in results.items():
        print(f"  {k:<26}: ρ* = {'— (post-scarcity)' if v is None else f'{v:.2f}'}")
    print("-" * W)
    d3 = claim3_fraud()
    print("CLAIM 3 — ceiling under fraud (should stay ≈ 2.4× — IC-7 caps at 24h):")
    print(f"  0% fraud: {d3[0,1]:.2f}×   20%: {d3[4,1]:.2f}×   40%: {d3[-1,1]:.2f}×")
    print("-" * W)
    print("CLAIM 4 — cumulative ledger: hoarding can't beat 24/F; only AGE adds spread:")
    rho4, T4 = 1.5, 40
    _, (_, Ds, _), (_, Dh, att_h) = claim4_frontloading(rho4, T4)
    print(f"  hoarder attempted {att_h.max():,.0f}h at the top; gate clipped it to "
          f"{Dh.max():,.0f}h (= ρ·C)")
    print(f"  steady vs hoarder end identical: max|D_steady−D_hoard| = {np.max(np.abs(Ds-Dh)):.1e}")
    print(f"  equal-age disparity (either strategy): {Dh.max()/Dh.min():.2f}× = 24/F")
    _, (_, Dy, _), _ = claim4_frontloading(rho4, 20)
    _, (_, Do, _), _ = claim4_frontloading(rho4, 60)
    print(f"  only AGE exceeds it: 60y-max / 20y-subsistence = {Do.max()/Dy.min():.1f}× "
          f"(= 3×·24/F, time lived not class)")
    print("=" * W)


def test_ceiling_bounded_and_rho_independent():
    d1 = claim1_ceiling_vs_rho()
    assert d1[:, 1].max() <= CEILING + 1e-6, "ceiling exceeded 24/F"
    assert d1[:, 1].std() < 1e-6, "ceiling should be rho-INDEPENDENT (flat)"
    print(f"[ok] ceiling flat at {d1[0,1]:.2f}× for all ρ (bound 24/F={CEILING:.1f})")


def test_scf_calibration():
    """The synthetic wealth must reproduce the real 2022 SCF percentile ratios."""
    wea = real_wealth()
    p50 = np.median(wea)
    p90 = np.percentile(wea, 90) / p50
    p99 = np.percentile(wea, 99) / p50
    assert 9 < p90 < 11.5, f"p90/p50 {p90:.1f} off SCF 9.96"
    assert 62 < p99 < 82, f"p99/p50 {p99:.1f} off SCF 70.9"
    print(f"[ok] wealth calibrated to SCF 2022: p90={p90:.1f}× (real 10.0) "
          f"p99={p99:.1f}× (real 70.9)")


def test_money_dwarfs_ceiling():
    assert SCF_BILLIONAIRE_OVER_MEDIAN > 1e5 * CEILING, "billionaire ratio should dwarf 2.4x"
    print(f"[ok] real billionaire/median {SCF_BILLIONAIRE_OVER_MEDIAN:,.0f}× >> "
          f"Aequitas {CEILING:.1f}×  ({SCF_BILLIONAIRE_OVER_MEDIAN/CEILING:,.0f}× the compression)")


def test_clearing_rho_exists_and_shifts():
    results, base_rho, *_ = claim2_market_and_shocks()
    assert base_rho is not None, "baseline should have a clearing rho"
    assert results["disaster -30% capacity"] < base_rho, "disaster must tighten rho"
    print(f"[ok] clearing ρ*={base_rho:.2f}; disaster tightens to "
          f"{results['disaster -30% capacity']:.2f}")


def test_fraud_cannot_break_ceiling():
    d3 = claim3_fraud()
    assert d3[:, 1].max() <= CEILING + 1e-6, "fraud broke the ceiling — IC-7 failed"
    print(f"[ok] ceiling holds at {d3[-1,1]:.2f}× even at 40% fraud (IC-7 caps at 24h)")


def test_frontloading_cannot_beat_ceiling():
    """A lifelong hoarder who splurges ends at the SAME cumulative consumption as a
    steady consumer (rho*c*T): the splurge is clipped to rho*C. Equal-age disparity
    is exactly 24/F under both strategies -- there is no 'banking' to blow."""
    rho, T = 1.5, 40
    _, (Cs, Ds, _), (Ch, Dh, att_h) = claim4_frontloading(rho, T)
    # timing is irrelevant: hoard-then-splurge lands at the same total as steady
    assert np.allclose(Ds, Dh, rtol=1e-9), "hoarder's total must equal the steady consumer's"
    # no agent's cumulative debit exceeds its OWN rho*C (front-loading is bounded)
    assert np.all(Dh <= rho * Ch + 1e-6), "a splurge exceeded rho*C — the gate failed"
    # the splurge WAS attempted and blocked: attempt far exceeds what was allowed
    assert att_h.max() > Dh.max() * 5, "hoarder should have attempted a blocked splurge"
    disp = Dh.max() / Dh.min()
    assert abs(disp - CEILING) < 1e-6, f"equal-age disparity {disp:.4f} != 24/F={CEILING}"
    print(f"[ok] hoard-then-splurge clipped to ρ·C (attempted {att_h.max():,.0f}h → "
          f"allowed {Dh.max():,.0f}h); equal-age disparity {disp:.2f}× = 24/F")


def test_only_age_exceeds_ceiling():
    """Within any equal-age cohort the disparity is exactly 24/F; the ONLY spread
    beyond it is age, and it is exactly separable as age_ratio × 24/F."""
    rho = 1.5
    _, (_, Dy, _), _ = claim4_frontloading(rho, T=20)
    _, (_, Do, _), _ = claim4_frontloading(rho, T=60)
    # equal-age disparity is 24/F at BOTH ages
    assert abs(Dy.max() / Dy.min() - CEILING) < 1e-6, "young cohort disparity != 24/F"
    assert abs(Do.max() / Do.min() - CEILING) < 1e-6, "old cohort disparity != 24/F"
    # cross-age exceeds 24/F, but only by the age ratio (separable, benign)
    cross = Do.max() / Dy.min()
    assert cross > CEILING, "cross-age should exceed 24/F"
    assert abs(cross - CEILING * (60 / 20)) < 1e-6, "cross-age spread should be age × 24/F"
    # and it is monotonic in age for the same person (same rate)
    assert Do[500] > Dy[500], "older = more cumulative consumption at the same rate"
    print(f"[ok] equal-age disparity = {CEILING:.1f}× at every age; only AGE adds spread "
          f"(20↔60y = {cross:.1f}× = 3×·24/F, time lived not class)")


def run_tests():
    test_ceiling_bounded_and_rho_independent()
    test_scf_calibration()
    test_money_dwarfs_ceiling()
    test_clearing_rho_exists_and_shifts()
    test_fraud_cannot_break_ceiling()
    test_frontloading_cannot_beat_ceiling()
    test_only_age_exceeds_ceiling()
    print("\nAll self-tests passed.")


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
