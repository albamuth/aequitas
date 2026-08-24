"""
The same pattern applied to two more sims: `disparity_ceiling_sim.py` and
`residual_unravelling.py`.

`generate.py` handles the sim the objection was actually about. This handles the
two the author asked for next, and the answer it can give is honestly weaker for
one of them. See `bonus_sims.md` for what each file can and cannot let a reader
check without running anything.

Writes, overwriting in place:

    disparity_ceiling.json      parameters, the closed-form results that need no
                                random draw at all, and the Monte-Carlo results
                                with their reproducibility conditions
    residual_unravelling.json   the full 2000-agent fixture, the five-farm demo
                                round by round, and every published run
    bonus_sims.md               both, as readable tables

Run:

    python 06-simulation/audits_inert/generate_bonus.py
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SIMDIR = HERE.parent.parent              # 06-simulation
sys.path.insert(0, str(SIMDIR / "disparity-ceiling"))
sys.path.insert(0, str(SIMDIR / "residual-unravelling"))

import disparity_ceiling_sim as dc      # noqa: E402
import residual_unravelling as ru       # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def jdefault(o):
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON-serialisable: {type(o)}")


def write_json(name: str, obj) -> None:
    (HERE / name).write_text(json.dumps(obj, indent=2, default=jdefault) + "\n",
                             encoding="utf-8")


STAMP = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ===========================================================================
# disparity_ceiling_sim.py
# ===========================================================================

def build_disparity() -> dict:
    """Reproduce `report()` exactly, in its own call order.

    This module draws from ONE module-level generator, `np.random.default_rng(42)`,
    and several functions consume from it. A number therefore depends on what was
    drawn before it. The sequence below is `report()`'s, call for call, in a fresh
    process. Change the order and the Monte-Carlo figures change.
    """
    F, DAY, CEILING = dc.F, dc.DAY, dc.CEILING

    # --- the parts that need no random draw at all -------------------------
    rho4, T4 = 1.5, 40
    _c4, (Cs, Ds, _), (Ch, Dh, att_h) = dc.claim4_frontloading(rho4, T4)
    _c, (_, Dy, _), _ = dc.claim4_frontloading(rho4, 20)
    _c, (_, Do, _), _ = dc.claim4_frontloading(rho4, 60)

    closed_form = {
        "claim_1_ceiling": {
            "statement": ("Credit rate c_i = F + w_i with w_i in [0, 24-F], so "
                          "c_i is in [F, 24]. Consumption at the gate is "
                          "d_i = rho * c_i. The disparity is "
                          "max(d) / (rho * F) = max(c) / F <= 24 / F. "
                          "rho cancels."),
            "F_hours_per_day": F,
            "day_hours": DAY,
            "ceiling_24_over_F": CEILING,
            "needs_a_random_draw": False,
        },
        "claim_3_fraud_invariance": {
            "statement": ("A fraudster's claimed rate is min(c_i * inflate, 24). "
                          "IC-7 caps any claim at 24 h per 24 h, so "
                          "max(claimed c) / F <= 24 / F whatever the fraud rate "
                          "or the inflation factor."),
            "inflation_factor_used": 2.0,
            "ceiling_under_any_fraud_rate": CEILING,
            "needs_a_random_draw": False,
        },
        "claim_4_frontloading": {
            "statement": ("Credit C and debit D are cumulative running tallies. "
                          "The gate D <= rho*C is re-checked every period and a "
                          "breaching purchase is clipped to the room that exists. "
                          "A hoarder who takes nothing for T-1 periods faces room "
                          "rho*c*T in the final period, which is exactly what the "
                          "steady consumer already took over T periods. Hoarding "
                          "changes the timing and not the total."),
            "rho": rho4, "periods_T": T4,
            "top_credit_rate_c": float(dc.DAY),
            "hoarder_attempted_hours": float(att_h.max()),
            "hoarder_attempted_arithmetic": f"rho * c * T * 10 = {rho4} * {DAY} * {T4} * 10",
            "hoarder_allowed_hours": float(Dh.max()),
            "hoarder_allowed_arithmetic": f"rho * c * T = {rho4} * {DAY} * {T4}",
            "steady_vs_hoarder_max_abs_difference": float(np.max(np.abs(Ds - Dh))),
            "equal_age_disparity": float(Dh.max() / Dh.min()),
            "equal_age_arithmetic": f"(rho*{DAY}*{T4}) / (rho*{F}*{T4}) = {DAY}/{F}",
            "cross_age_60y_over_20y": float(Do.max() / Dy.min()),
            "cross_age_arithmetic": f"({DAY}*60) / ({F}*20) = 3 * {DAY}/{F}",
            "needs_a_random_draw": False,
        },
    }

    # --- report()'s call order, exactly ------------------------------------
    d1 = dc.claim1_ceiling_vs_rho()
    inc = dc.real_income()
    wea = dc.real_wealth()
    results, base_rho, _rhos, _dem, K = dc.claim2_market_and_shocks()
    d3 = dc.claim3_fraud()

    ip, wp = float(np.median(inc)), float(np.median(wea))
    monte_carlo = {
        "claim_1_table": {
            "columns": ["rho", "top_over_floor", "p99.9_over_p50", "gini"],
            "rows": d1.tolist(),
            "top_over_floor_min": float(d1[:, 1].min()),
            "top_over_floor_max": float(d1[:, 1].max()),
            "top_over_floor_std": float(d1[:, 1].std()),
        },
        "money_comparison_ratios_to_median": {
            "income_p90": float(np.percentile(inc, 90) / ip),
            "income_p99": float(np.percentile(inc, 99) / ip),
            "income_p99_9": float(np.percentile(inc, 99.9) / ip),
            "wealth_p90": float(np.percentile(wea, 90) / wp),
            "wealth_p99": float(np.percentile(wea, 99) / wp),
            "billionaire_over_median": float(dc.SCF_BILLIONAIRE_OVER_MEDIAN),
            "calibration_targets_SCF_2022": dc.SCF_WEALTH_RATIOS,
        },
        "claim_2_clearing_rho": {
            "scenarios": {k: (None if v is None else float(v))
                          for k, v in results.items()},
            "baseline_rho": None if base_rho is None else float(base_rho),
            "capacity_K": float(K),
            "search_grid": {"low": 0.5, "high": 4.0, "points": 200,
                            "step": (4.0 - 0.5) / 199},
            "note": ("rho* is the grid point minimising |demand - capacity|, so it "
                     "is resolved no finer than one grid step."),
        },
        "claim_3_table": {
            "columns": ["fraud_rate", "top_over_floor", "gini"],
            "rows": d3.tolist(),
            "top_over_floor_max": float(d3[:, 1].max()),
        },
    }

    return {
        "provenance": {
            "generated_utc": STAMP,
            "generator": "06-simulation/audits_inert/generate_bonus.py",
            "source": "06-simulation/disparity_ceiling_sim.py",
            "source_sha256": sha256(SIMDIR / "disparity-ceiling" / "disparity_ceiling_sim.py"),
        },
        "parameters": {
            "self_care_floor_F_hours_per_day": F,
            "day_hours": DAY,
            "structural_ceiling_24_over_F": CEILING,
            "population_N": dc.N,
            "numpy_seed": 42,
            "population_draw": {
                "share_with_little_or_no_paid_work": 0.35,
                "workers_discretionary_hours": "normal(mean=6.0, sd=3.0), clipped to [0, 24-F]",
                "non_workers_discretionary_hours": "uniform(0, 1.5)",
                "credit_rate": "c_i = F + w_i",
            },
            "money_calibration": {
                "income_lognormal_sigma": dc.INCOME_LOGNORMAL_SIGMA,
                "wealth_lognormal_sigma": 1.80,
                "wealth_pareto_tail_exponent": 1.5,
                "wealth_pareto_applied_to_top_fraction": 0.01,
                "billionaires_per_households": "700 / 131e6",
                "SCF_2022_targets": dc.SCF_WEALTH_RATIOS,
                "billionaire_over_median": dc.SCF_BILLIONAIRE_OVER_MEDIAN,
                "sources_not_reproduced_here": (
                    "2022 Survey of Consumer Finances (Federal Reserve) and Forbes. "
                    "Cited in the sim's own comments; not re-verified by this "
                    "generator."),
            },
        },
        "closed_form": closed_form,
        "monte_carlo": monte_carlo,
        "how_to_check_this_without_running_it": [
            "Claims 1, 3 and 4 need no random numbers. Their arithmetic is in "
            "`closed_form` above and every digit can be redone on paper.",
            "Claim 2 needs the 200,000-agent draw. That draw is not exported: it "
            "is 200,000 numbers and no reader checks those by hand. What is "
            "exported is the seed, the distributions, the search grid and the "
            "result. This is a weaker answer to the objection than the "
            "arithmetic_audits fixture, and it is stated as one.",
            "The module draws from one generator, np.random.default_rng(42), in "
            "call order. The order used here is report()'s. A different order "
            "gives different Monte-Carlo digits from the same seed.",
        ],
    }


# ===========================================================================
# residual_unravelling.py
# ===========================================================================

def build_residual() -> dict:
    agents = ru.make_agents()
    demo = ru.demo()

    runs = {}
    for key, basis, pct in (("A_residual_median", "residual", 50),
                            ("B_residual_p75", "residual", 75),
                            ("C_population_median", "population", 50)):
        res = ru.run(basis=basis, pct=pct, agents=agents)
        runs[key] = {
            "basis": basis,
            "percentile": pct,
            "rounds": [{"round": s.round_no, "estimate": s.estimate,
                        "n_disclosed": s.n_disclosed, "n_dark": s.n_dark,
                        "dark_mean_true": s.dark_mean_true,
                        "carried_total": s.carried_total}
                       for s in res.rounds],
            "final_dark_count": res.n_dark,
            "final_dark_fraction": res.dark_fraction,
            "rounds_taken": len(res.rounds),
            "still_dark_true_debits": sorted(a.true_debit for a in res.agents
                                             if not a.disclosed),
        }

    res_a = ru.run(basis="residual", pct=50, agents=agents)
    res_b = ru.run(basis="residual", pct=75, agents=agents)
    res_c = ru.run(basis="population", pct=50, agents=agents)

    truths = sorted(a.true_debit for a in agents)
    return {
        "provenance": {
            "generated_utc": STAMP,
            "generator": "06-simulation/audits_inert/generate_bonus.py",
            "source": "06-simulation/residual_unravelling.py",
            "source_sha256": sha256(SIMDIR / "residual-unravelling" / "residual_unravelling.py"),
        },
        "parameters": {
            "n_agents": ru.N_AGENTS,
            "seed": ru.SEED,
            "rng": "python random.Random(seed), gauss draws in the order below",
            "true_debit": f"exp(gauss(mu={ru.LOG_MU}, sigma={ru.LOG_SIGMA}))",
            "disclosure_cost": f"max(0, gauss(mean={ru.COST_MEAN}, sigma={ru.COST_SIGMA}))",
            "max_rounds": ru.MAX_ROUNDS,
        },
        "rules_in_arithmetic": {
            "estimate": ("est(r) = percentile(pool(r), p), linearly interpolated. "
                         "pool(r) is the true debits of the UNDISCLOSED agents "
                         "under the residual basis, and of ALL agents under the "
                         "population basis."),
            "books": ("carried(r) = SUM over agents of (true_debit if disclosed "
                      "else est(r))"),
            "who_moves": ("an agent discloses in round r iff "
                          "true_debit + cost < est(r)"),
            "stop": "when no agent moves, or after max_rounds",
        },
        "five_farm_demo": {
            "note": ("The whole mechanism on five farms with zero disclosure cost. "
                     "No random numbers. Every row can be redone on paper."),
            "names": ru.DEMO_NAMES,
            "true_debits": ru.DEMO_TRUE,
            "true_total": demo["truth"],
            "residual_basis": demo["residual"],
            "population_basis": demo["population"],
        },
        "full_fixture_2000_agents": [
            {"idx": a.idx, "true_debit": a.true_debit, "cost": a.cost}
            for a in agents
        ],
        "fixture_summary": {
            "n": len(truths),
            "true_debit_min": truths[0],
            "true_debit_median": ru.percentile(truths, 50),
            "true_debit_mean": sum(truths) / len(truths),
            "true_debit_p90": ru.percentile(truths, 90),
            "true_debit_max": truths[-1],
        },
        "runs": runs,
        "verdict": {
            "H1_estimate_rises_monotonically_A": ru.h1_dark_pool_worsens(res_a),
            "H1_estimate_rises_monotonically_B": ru.h1_dark_pool_worsens(res_b),
            "H2_residual_basis_unravels_A": ru.h2_unravels(res_a),
            "H2_residual_basis_unravels_B": ru.h2_unravels(res_b),
            "H3_population_basis_leaves_more_dark": ru.h3_population_basis_is_stable(res_c, res_a),
        },
        "how_to_check_this_without_running_it": [
            "The five-farm demo has no random numbers at all. It is the argument "
            "in full, and every round of it is on this page.",
            "The 2000-agent fixture IS exported, in full, under "
            "`full_fixture_2000_agents`. Nothing about the main run is hidden "
            "behind a seed.",
            "The stated limits of the sim are the sim's own, printed under READ "
            "THIS BEFORE QUOTING THE NUMBERS, and they still stand: market access "
            "is not modelled, agents are myopic, and the disclosure cost is a "
            "guess.",
        ],
    }


# ===========================================================================
# markdown
# ===========================================================================

def render(dcj: dict, ruj: dict) -> str:
    L: list[str] = []
    a = L.append
    a("# Two more sims, as inert data")
    a("")
    a("**Generated file. Do not hand-edit.** Regenerate with:")
    a("")
    a("```")
    a("python 06-simulation/audits_inert/generate_bonus.py")
    a("```")
    a("")
    a(f"Generated {STAMP}.")
    a("")
    a("The same three-item answer that [`README.md`](README.md) gives for "
      "`arithmetic_audits.py`, applied to two more sims. **One of the two gets a "
      "weaker answer, and it says so.**")
    a("")
    a("---")
    a("")
    a("## `disparity_ceiling_sim.py`")
    a("")
    a(f"Source SHA-256 `{dcj['provenance']['source_sha256']}`.")
    a("")
    a("### Three of its four claims need no simulation at all")
    a("")
    a("This is the finding. Claims 1, 3 and 4 are closed-form arithmetic. The "
      "200,000-agent population demonstrates them; it does not establish them.")
    a("")
    cf = dcj["closed_form"]
    a(f"**Claim 1 — the ceiling.** {cf['claim_1_ceiling']['statement']}")
    a("")
    a(f"With `F` = {cf['claim_1_ceiling']['F_hours_per_day']} h/day, the bound is "
      f"`24 / {cf['claim_1_ceiling']['F_hours_per_day']}` = "
      f"**{cf['claim_1_ceiling']['ceiling_24_over_F']}×**.")
    a("")
    a(f"**Claim 3 — fraud invariance.** {cf['claim_3_fraud_invariance']['statement']}")
    a("")
    a(f"**Claim 4 — front-loading.** {cf['claim_4_frontloading']['statement']}")
    a("")
    c4 = cf["claim_4_frontloading"]
    a("| quantity | arithmetic | value |")
    a("|---|---|---|")
    a(f"| hoarder attempts | `{c4['hoarder_attempted_arithmetic']}` | "
      f"{c4['hoarder_attempted_hours']:,.0f} h |")
    a(f"| gate allows | `{c4['hoarder_allowed_arithmetic']}` | "
      f"{c4['hoarder_allowed_hours']:,.0f} h |")
    a(f"| steady vs hoarder, largest gap | — | "
      f"{c4['steady_vs_hoarder_max_abs_difference']:.1e} h |")
    a(f"| equal-age disparity | `{c4['equal_age_arithmetic']}` | "
      f"{c4['equal_age_disparity']:.2f}× |")
    a(f"| 60-year max vs 20-year floor | `{c4['cross_age_arithmetic']}` | "
      f"{c4['cross_age_60y_over_20y']:.1f}× |")
    a("")
    a("### The one claim that does need the draw")
    a("")
    mc = dcj["monte_carlo"]["claim_2_clearing_rho"]
    a("**Claim 2 — the clearing rate ρ\\*.** ρ\\* is the grid point that minimises "
      "`|Σ min(appetite_i, ρ·c_i) − K|`, where `K` is productive capacity. The "
      f"grid runs {mc['search_grid']['low']} to {mc['search_grid']['high']} in "
      f"{mc['search_grid']['points']} steps, so ρ\\* is resolved no finer than "
      f"{mc['search_grid']['step']:.4f}.")
    a("")
    a("| scenario | ρ\\* |")
    a("|---|---|")
    for k, v in mc["scenarios"].items():
        a(f"| {k} | {'— (post-scarcity)' if v is None else f'{v:.2f}'} |")
    a("")
    a("### What is not exported, and why")
    a("")
    for s in dcj["how_to_check_this_without_running_it"]:
        a(f"- {s}")
    a("")
    a("### The money comparison")
    a("")
    a("These are ratios to the median, drawn from a synthetic distribution "
      "calibrated to the 2022 Survey of Consumer Finances. **This generator does "
      "not re-verify the underlying source figures**; it reports what the sim "
      "computes and what the sim's own comments cite.")
    a("")
    m = dcj["monte_carlo"]["money_comparison_ratios_to_median"]
    a("| measure | simulated | SCF 2022 target |")
    a("|---|---|---|")
    a(f"| wealth p90 / p50 | {m['wealth_p90']:.1f}× | {m['calibration_targets_SCF_2022']['p90']}× |")
    a(f"| wealth p99 / p50 | {m['wealth_p99']:.1f}× | {m['calibration_targets_SCF_2022']['p99']}× |")
    a(f"| income p90 / p50 | {m['income_p90']:.1f}× | — |")
    a(f"| income p99 / p50 | {m['income_p99']:.1f}× | — |")
    a(f"| income p99.9 / p50 | {m['income_p99_9']:.1f}× | — |")
    a(f"| billionaire / median | {m['billionaire_over_median']:,.0f}× | "
      "$200B / $192,900, Forbes and SCF |")
    a("")
    a("---")
    a("")
    a("## `residual_unravelling.py`")
    a("")
    a(f"Source SHA-256 `{ruj['provenance']['source_sha256']}`.")
    a("")
    a("**This one gets the full answer.** Its 2000-agent fixture is exported "
      "whole, under `full_fixture_2000_agents` in "
      "[`residual_unravelling.json`](residual_unravelling.json), and its "
      "five-farm demo has no random numbers in it at all.")
    a("")
    a("### The rules, in arithmetic")
    a("")
    for k, v in ruj["rules_in_arithmetic"].items():
        a(f"- **{k}** — {v}")
    a("")
    a("### The five-farm demo, round by round")
    a("")
    d = ruj["five_farm_demo"]
    a(f"True debits: " + ", ".join(f"**{n}** {t:g}" for n, t
                                   in zip(d["names"], d["true_debits"]))
      + f". True total **{d['true_total']:g}**. Disclosure costs nothing here, so a "
        "farm shows its records exactly when its true number is below the estimate.")
    a("")
    for basis, title in (("residual_basis", "Estimate taken from the dark farms only — the rule in §5.1b"),
                         ("population_basis", "Estimate taken from all farms — the rule §5.1b rejects")):
        b = d[basis]
        a(f"**{title}**")
        a("")
        a("| round | still dark | their true numbers | estimate | books say | who shows records |")
        a("|---|---|---|---|---|---|")
        for r in b["rows"]:
            pool = "[" + " ".join(f"{x:g}" for x in r["pool"]) + "]"
            a(f"| {r['round']} | {', '.join(r['dark_names']) or '(none)'} | "
              f"`{pool}` | {r['estimate']:g} | {r['books']:g} | "
              f"{', '.join(r['movers']) or '*nobody moves — stop*'} |")
        a("")
        a(f"Final books **{b['final_books']:g}** against a truth of "
          f"{d['true_total']:g}. **Error {b['error']:g}.** Still dark: "
          f"{', '.join(b['final_dark']) or '(none)'}.")
        a("")
    a("### The 2000-agent runs")
    a("")
    fs = ruj["fixture_summary"]
    a(f"Fixture: {fs['n']} agents, true debit median {fs['true_debit_median']:.4f}, "
      f"mean {fs['true_debit_mean']:.4f}, p90 {fs['true_debit_p90']:.4f}, "
      f"max {fs['true_debit_max']:.4f}.")
    a("")
    for key, r in ruj["runs"].items():
        a(f"**{key}** — basis `{r['basis']}`, percentile {r['percentile']}")
        a("")
        a("| round | estimate | disclosed | dark | mean true of the dark | total carried |")
        a("|---|---|---|---|---|---|")
        for s in r["rounds"]:
            a(f"| {s['round']} | {s['estimate']:.4f} | {s['n_disclosed']} | "
              f"{s['n_dark']} | {s['dark_mean_true']:.4f} | {s['carried_total']:.1f} |")
        a("")
        a(f"Ends with **{r['final_dark_count']} still dark** "
          f"({100 * r['final_dark_fraction']:.1f}%) after {r['rounds_taken']} rounds.")
        a("")
    a("### Verdict")
    a("")
    a("| hypothesis | result |")
    a("|---|---|")
    for k, v in ruj["verdict"].items():
        a(f"| {k} | {'**PASS**' if v else '**FAIL**'} |")
    a("")
    a("### What this still does not settle")
    a("")
    for s in ruj["how_to_check_this_without_running_it"][2:]:
        a(f"- {s}")
    a("")
    return "\n".join(L) + "\n"


def main() -> None:
    dcj = build_disparity()
    ruj = build_residual()
    write_json("disparity_ceiling.json", dcj)
    write_json("residual_unravelling.json", ruj)
    (HERE / "bonus_sims.md").write_text(render(dcj, ruj), encoding="utf-8")
    print(f"wrote {HERE}")
    print(f"  disparity_ceiling.json     ceiling={dcj['closed_form']['claim_1_ceiling']['ceiling_24_over_F']}, "
          f"claim-1 spread {dcj['monte_carlo']['claim_1_table']['top_over_floor_min']:.2f}"
          f"-{dcj['monte_carlo']['claim_1_table']['top_over_floor_max']:.2f}")
    print(f"  residual_unravelling.json  {ruj['fixture_summary']['n']} agents exported in full; "
          f"demo error residual={ruj['five_farm_demo']['residual_basis']['error']:g} "
          f"population={ruj['five_farm_demo']['population_basis']['error']:g}")
    print(f"  bonus_sims.md")


if __name__ == "__main__":
    main()
