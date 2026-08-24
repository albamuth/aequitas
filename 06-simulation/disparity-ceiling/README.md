# Disparity ceiling — how far apart can two people's consumption get?

> **Status:** ✅ **Stated, simulated, stress-tested. A conditional result**, on the consumption axis only.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Formal statement:** [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) · **The ρ dial:** [`RHO_SWEEP.md`](RHO_SWEEP.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

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
| [`disparity_ceiling_sim.py`](disparity_ceiling_sim.py) | The population model. Four claims, five self-tests. |
| [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) | The formal statement, its five conditions, and the plain-language explainer in §0. |
| `ceiling_fig1_rho.png` … `ceiling_fig4_frontloading.png` | The four figures the sim writes. |
| [`rho_sweep.py`](rho_sweep.py) | The ρ dial, calibrated against the median-lifestyle anchor. |
| [`RHO_SWEEP.md`](RHO_SWEEP.md) | What ρ is, and what the sweep found. |
| `rho_sweep_fig.png` | The sweep figure. |

## Checkable without running it

**Three of the four claims need no simulation at all.** The ceiling, fraud invariance and front-loading are closed-form arithmetic; the 200,000-agent population demonstrates them, it does not establish them. Only the clearing rate ρ\* needs the random draw.

The arithmetic is written out in [`../audits/audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md), with the parameters in `disparity_ceiling.json` beside it.

## What depends on this

The Statera kernel has to re-derive both headline numbers before any new scenario runs — see [`../statera/RESULTS.md`](../statera/RESULTS.md). It does, exactly.
