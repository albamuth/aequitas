# Disparity ceiling — how far apart can two people's consumption get?

> **Version:** 0.1
> **Date:** 2026-09-16

> **Status:** ✅ **Stated, simulated, stress-tested. A conditional result**, on the consumption axis only.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Formal statement:** [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) · **The ρ dial:** [`RHO_SWEEP.md`](RHO_SWEEP.md) · **Change history:** `CHANGELOG.md`

## What this is

Two questions about the same model, which is why they share a folder.

**1. How wide can the gap get?** Under Aequitas the ratio between the most anyone can sustainably consume and a bare-subsistence allowance is **24/F**, where *F* is the network's self-care floor in hours per day. At a 10-hour floor that is **2.40×**. Under money the same ratio runs to about a million times and compounds without limit.

**2. Where should the dial be set?** The gate on discretionary consumption is `D ≤ ρ·C` — you may consume up to ρ times your own earned credit. ρ ("rho") is set by local governance, not by Aequitas. The ceiling does not depend on it. The *absolute level* does, and [`rho_sweep.py`](rho_sweep.py) asks which value clears the market.

`rho_sweep.py` builds on `disparity_ceiling_sim.py` and imports from it, so run them from this folder.

## Run it

```bash
python disparity_ceiling_sim.py            # the population run and the four figures
python disparity_ceiling_sim.py --test     # self-tests only
python rho_sweep.py                        # the rho sweep and its figure
python rho_sweep.py --test                 # self-tests only
```

Needs `numpy`; the figures need `matplotlib`. The default population is 200,000 agents and runs in seconds.

## What is in here

| Path | What it is |
|---|---|
| [`disparity_ceiling_sim.py`](disparity_ceiling_sim.py) | The population model. Four claims, seven self-tests. |
| [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) | The formal statement, its five conditions, and the plain-language explainer in §0. |
| `ceiling_fig1_rho.png` … `ceiling_fig4_frontloading.png` | The four figures the sim writes. |
| [`rho_sweep.py`](rho_sweep.py) | The ρ dial, calibrated against the median-lifestyle anchor. |
| [`RHO_SWEEP.md`](RHO_SWEEP.md) | What ρ is, and what the sweep found. |
| `rho_sweep_fig.png` | The sweep figure. |

## Checkable without running it

**Three of the four claims need no simulation at all.** The ceiling, fraud invariance and front-loading are closed-form arithmetic; the 200,000-agent population demonstrates them, it does not establish them. Only the clearing rate ρ\* needs the random draw.

The arithmetic is written out in [`../audits/audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md), with the parameters in `disparity_ceiling.json` beside it.

## What depends on this

The Statera kernel has to re-derive both headline numbers before any new scenario runs — see [`../99-superseded/statera/RESULTS.md`](../99-superseded/statera/RESULTS.md). It does, exactly.

## Test sources

> **Author ruling, 2026-09-23:** every test that makes a claim about the world, or uses a number we chose, cites a scientific source for its method. **Of this folder's 12 checks, 8 are code checks, 1 is sourced, and 3 are unsourced.** The labels are defined in [`../ceiling-rubric/README.md`](../ceiling-rubric/README.md#test-sources).

**Most of these checks confirm arithmetic.** The author ruled on 2026-09-02 that `24 ÷ F` is simple mathematics and needs no simulation to prove it. **A check that confirms an identity is a code check.** It shows the code does the arithmetic. It is not evidence about any economy.

### `disparity_ceiling_sim.py` — 7 checks

| # | Test | Label |
|---|---|---|
| 1 | The ceiling is at most `24/F` and does not move with ρ | code check. ρ cancels in `ρ·24 ÷ ρ·F` |
| 2 | Synthetic wealth reproduces SCF 2022 percentile ratios | **unsourced.** The median, $192,900, is confirmed. **The p90, p95 and p99 figures are not on the cited Federal Reserve page.** See [`Data_survey-of-consumer-finances-2022.md`](../../02-research/Data_survey-of-consumer-finances-2022.md). The tolerances, 9–11.5 and 62–82, are also our choice |
| 3 | Money's top-to-median ratio dwarfs `24/F` | **unsourced.** The "~$200B" Forbes figure has no dated source. The comparison holds by five orders of magnitude, so a corrected figure is unlikely to change the result |
| 4 | A clearing ρ exists, and a disaster tightens it | code check. Less capacity lowers the clearing ρ by the model's construction |
| 5 | Fraud cannot break the ceiling | code check. IC-7 clips every account at 24, so this cannot fail. Foundations §5.5.7 already says the statistic *"reads no accounts"* |
| 6 | Hoard-then-splurge ends where steady consumption ends | code check. The gate is a ratio checked at each event |
| 7 | Only age adds spread beyond `24/F` | code check. An identity |

### `rho_sweep.py` — 5 checks

| # | Test | Label |
|---|---|---|
| 1 | The baseline has a clearing ρ | code check |
| 2 | More efficient production loosens ρ | **sourced.** The efficiency figures come from Q6, which cites EXIOBASE: [`Data_cross-country-labour-efficiency.md`](../../02-research/Data_cross-country-labour-efficiency.md) |
| 3 | A disaster tightens ρ and growth loosens it | code check. By construction |
| 4 | The median person gets more than 0.7 of a full lifestyle | **unsourced.** `0.7` is our number |
| 5 | Disparity stays within `24/F` in every scenario | code check. `P` = 0 throughout, so it is an identity here |

**This file's credit population is the one `ceiling_rubric.py` scores.** `draw_population()` uses `normal(6.0, 3.0)` with 35% non-workers, and **no source justifies either**. See [`../ceiling-rubric/README.md`](../ceiling-rubric/README.md#test-sources).
