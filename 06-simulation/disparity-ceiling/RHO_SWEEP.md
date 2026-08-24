# ρ-sweep — the prime-rate dial, calibrated to the median lifestyle

**Script:** [`rho_sweep.py`](rho_sweep.py) · 5 self-tests green · plot `rho_sweep_fig.png`. Builds on [`disparity_ceiling_sim.py`](disparity_ceiling_sim.py) (which proves the 24/F ceiling) and calibrates the *absolute* level ρ to the Tracks 1–4 median-lifestyle anchor (~1,380 h/yr) and the Q6 efficiency finding.

## What ρ is

Discretionary consumption is gated by **D ≤ ρ·C** (OP-4 shape): you may consume up to ρ times your own earned credit. ρ is an **exogenous "prime-rate" dial** set by local governance (A8) — Aequitas uses it, never sets a global one (§3.5). The disparity *ceiling* (24/F) is ρ-independent; this sim studies the *absolute* level: does a pickable ρ clear the market, where does the median sit, and how does it move?

## The model (calibrated where we have data, flagged where illustrative)

- Credit rate `c_i` = self-care floor F(=10 h/day) + productive work, heterogeneous over [F, 24].
- A real lifestyle `r_i` (median desired = 1.0) costs debit `r_i × INTENSITY`; **INTENSITY_US ≈ 13.8 debit-h/lifestyle-unit**, calibrated so ρ=1 funds one median lifestyle from median credit (matches §3.5). *Absolute — OP-10-dependent, so only ratios/directions are claimed.*
- Physical capacity `R_max = B / INTENSITY`, where B is the fixed **energy/materials budget** (Q1: the binding constraint is physical, not labour). **Efficient production lowers INTENSITY → more real lifestyle from the same budget.**
- Clearing ρ* solves `Σ min(want_i, ρ·c_i/INTENSITY) = R_max`.

## Results

| Scenario | ρ* | Median gets | Constrained | Disparity |
|---|---|---|---|---|
| **US method (baseline)** | **1.20** | 0.92× | 35% | 2.40 |
| **German/JP method** | **post-scarcity** | 1.00× | 0% | — |
| **Spanish method** | **post-scarcity** | 1.00× | 0% | — |
| growth +15% budget | 2.15 | 1.00× | 6% | 2.40 |
| disaster −30% budget | 0.68 | 0.62× | 79% | 2.40 |
| pollution +25% debit | 1.01 | 0.68× | 67% | 2.40 |
| pop −15% | 1.20 | 0.92× | 35% | 2.40 |

**Five findings:**

1. **A pickable ρ clears the market.** Baseline ρ*≈1.2 — a finite, sane value; aggregate demand meets physical capacity, and the median gets ~92% of their desired lifestyle.
2. **ρ moves predictably under shocks — the "prime-rate" behaviour.** Disaster (−30% budget) *tightens* ρ to 0.68; growth *loosens* it to 2.15; a pollution re-weighting (+25% debit) tightens it to ~1.0. Governance turns one dial, in the intuitive direction.
3. **The big one — efficiency, not labour, crosses the scarcity threshold.** The *same* society is mildly scarcity-constrained under the US production method (ρ*=1.2, 35% of people constrained below their wants) but tips into **post-scarcity** — the debit gate stops binding at all, everyone gets their full desired lifestyle — under German/Japanese or Spanish efficiency. This closes the loop: **Q1** (labour is abundant; materials/energy bind), **Q6** (the US is the inefficient outlier), and the ρ mechanism are one story. Cutting waste and producing efficiently, *not* working more, is what delivers abundance.
4. **The median always gets a lifestyle.** Even at the tightest realistic setting the median person's discretionary layer stays positive (0.62–1.00× of desired) — the gate rations the *top tail*, not the typical person.
5. **The 24/F ceiling is invariant throughout.** Real-consumption disparity (top vs the subsistence allowance) is exactly 2.4× in every scenario — ρ sets the *level*, never the *spread* (IC-7; proved in `disparity_ceiling_sim.py`).

## Honest limits

- **ρ* absolute values and the exact post-scarcity crossing are calibration-sensitive** (INTENSITY is OP-10-dependent; the physical-budget fraction CAP=0.85 is illustrative). The **directions** — efficiency loosens, disaster tightens, ceiling invariant, median protected — are robust; the specific numbers are not claims.
- Static one-period clearing; no dynamics/expectations. A multi-period version is a later refinement.
- "Wants" are a lognormal proxy; real preference heterogeneity is richer.

*Tracks Foundations v0.15 (§3.5, §7.5, A8; IC-7). Anchored to `MEDIAN_LIFESTYLE_RESULT.md` and `Q6.md`.*
