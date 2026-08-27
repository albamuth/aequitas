# Two more sims, as inert data

**Generated file. Do not hand-edit.** Regenerate with:

```
python 06-simulation/audits_inert/generate_bonus.py
```

Generated 2026-08-24T13:57:48Z.

The same three-item answer that [`README.md`](README.md) gives for `arithmetic_audits.py`, applied to two more sims. **One of the two gets a weaker answer, and it says so.**

---

## `disparity_ceiling_sim.py`

Source SHA-256 `52708969a5a81fb3f5d79a60b9ecac46425a32507d572fcaa220f05a084633ea`.

### Three of its four claims need no simulation at all

This is the finding. Claims 1, 3 and 4 are closed-form arithmetic. The 200,000-agent population demonstrates them; it does not establish them.

**Claim 1 — the ceiling.** Credit rate c_i = F + w_i with w_i in [0, 24-F], so c_i is in [F, 24]. Consumption at the gate is d_i = rho * c_i. The disparity is max(d) / (rho * F) = max(c) / F <= 24 / F. rho cancels.

With `F` = 10.0 h/day, the bound is `24 / 10.0` = **2.4×**.

**Claim 3 — fraud invariance.** A fraudster's claimed rate is min(c_i * inflate, 24). IC-7 caps any claim at 24 h per 24 h, so max(claimed c) / F <= 24 / F whatever the fraud rate or the inflation factor.

**Claim 4 — front-loading.** Credit C and debit D are cumulative running tallies. The gate D <= rho*C is re-checked every period and a breaching purchase is clipped to the room that exists. A hoarder who takes nothing for T-1 periods faces room rho*c*T in the final period, which is exactly what the steady consumer already took over T periods. Hoarding changes the timing and not the total.

| quantity | arithmetic | value |
|---|---|---|
| hoarder attempts | `rho * c * T * 10 = 1.5 * 24.0 * 40 * 10` | 14,400 h |
| gate allows | `rho * c * T = 1.5 * 24.0 * 40` | 1,440 h |
| steady vs hoarder, largest gap | — | 2.3e-12 h |
| equal-age disparity | `(rho*24.0*40) / (rho*10.0*40) = 24.0/10.0` | 2.40× |
| 60-year max vs 20-year floor | `(24.0*60) / (10.0*20) = 3 * 24.0/10.0` | 7.2× |

### The one claim that does need the draw

**Claim 2 — the clearing rate ρ\*.** ρ\* is the grid point that minimises `|Σ min(appetite_i, ρ·c_i) − K|`, where `K` is productive capacity. The grid runs 0.5 to 4.0 in 200 steps, so ρ\* is resolved no finer than 0.0176.

| scenario | ρ\* |
|---|---|
| baseline | 1.24 |
| pop -15% | 1.26 |
| disaster -30% capacity | 0.82 |
| pollution +25% debit | 1.19 |

### What is not exported, and why

- Claims 1, 3 and 4 need no random numbers. Their arithmetic is in `closed_form` above and every digit can be redone on paper.
- Claim 2 needs the 200,000-agent draw. That draw is not exported: it is 200,000 numbers and no reader checks those by hand. What is exported is the seed, the distributions, the search grid and the result. This is a weaker answer to the objection than the arithmetic_audits fixture, and it is stated as one.
- The module draws from one generator, np.random.default_rng(42), in call order. The order used here is report()'s. A different order gives different Monte-Carlo digits from the same seed.

### The money comparison

These are ratios to the median, drawn from a synthetic distribution calibrated to the 2022 Survey of Consumer Finances. **This generator does not re-verify the underlying source figures**; it reports what the sim computes and what the sim's own comments cite.

| measure | simulated | SCF 2022 target |
|---|---|---|
| wealth p90 / p50 | 10.3× | 9.96× |
| wealth p99 / p50 | 70.8× | 70.9× |
| income p90 / p50 | 3.0× | — |
| income p99 / p50 | 7.4× | — |
| income p99.9 / p50 | 14.1× | — |
| billionaire / median | 1,036,807× | $200B / $192,900, Forbes and SCF |

---

## `residual_unravelling.py`

Source SHA-256 `9da1df1a9db5c4a48e6c3c6c49775ca6efce7f10cb4fc8d69952bb414e02b99b`.

**This one gets the full answer.** Its 2000-agent fixture is exported whole, under `full_fixture_2000_agents` in [`residual_unravelling.json`](residual_unravelling.json), and its five-farm demo has no random numbers in it at all.

### The rules, in arithmetic

- **estimate** — est(r) = percentile(pool(r), p), linearly interpolated. pool(r) is the true debits of the UNDISCLOSED agents under the residual basis, and of ALL agents under the population basis.
- **books** — carried(r) = SUM over agents of (true_debit if disclosed else est(r))
- **who_moves** — an agent discloses in round r iff true_debit + cost < est(r)
- **stop** — when no agent moves, or after max_rounds

### The five-farm demo, round by round

True debits: **Ana** 1, **Ben** 2, **Cal** 3, **Dee** 4, **Eve** 20. True total **30**. Disclosure costs nothing here, so a farm shows its records exactly when its true number is below the estimate.

**Estimate taken from the dark farms only — the rule in §4.4**

| round | still dark | their true numbers | estimate | books say | who shows records |
|---|---|---|---|---|---|
| 0 | Ana, Ben, Cal, Dee, Eve | `[1 2 3 4 20]` | 3 | 15 | Ana, Ben |
| 1 | Cal, Dee, Eve | `[3 4 20]` | 4 | 15 | Cal |
| 2 | Dee, Eve | `[4 20]` | 12 | 30 | Dee |
| 3 | Eve | `[20]` | 20 | 30 | *nobody moves — stop* |

Final books **30** against a truth of 30. **Error 0.** Still dark: Eve.

**Estimate taken from all farms — the rule §4.4 rejects**

| round | still dark | their true numbers | estimate | books say | who shows records |
|---|---|---|---|---|---|
| 0 | Ana, Ben, Cal, Dee, Eve | `[1 2 3 4 20]` | 3 | 15 | Ana, Ben |
| 1 | Cal, Dee, Eve | `[1 2 3 4 20]` | 3 | 12 | *nobody moves — stop* |

Final books **12** against a truth of 30. **Error 18.** Still dark: Cal, Dee, Eve.

### The 2000-agent runs

Fixture: 2000 agents, true debit median 0.9951, mean 1.3642, p90 2.7309, max 18.2260.

**A_residual_median** — basis `residual`, percentile 50

| round | estimate | disclosed | dark | mean true of the dark | total carried |
|---|---|---|---|---|---|
| 0 | 0.9951 | 0 | 2000 | 1.3642 | 1990.2 |
| 1 | 1.6541 | 950 | 1050 | 2.0924 | 2268.1 |
| 2 | 2.3475 | 1445 | 555 | 2.8626 | 2442.5 |
| 3 | 3.1526 | 1711 | 289 | 3.7379 | 2559.2 |
| 4 | 3.9904 | 1849 | 151 | 4.7479 | 2614.0 |
| 5 | 5.0114 | 1921 | 79 | 5.9115 | 2657.3 |
| 6 | 6.1604 | 1957 | 43 | 7.2282 | 2682.5 |
| 7 | 7.3351 | 1978 | 22 | 9.0639 | 2690.3 |
| 8 | 9.5950 | 1986 | 14 | 10.5207 | 2715.4 |
| 9 | 14.3556 | 1993 | 7 | 13.3487 | 2735.4 |
| 10 | 15.3661 | 1996 | 4 | 15.8284 | 2726.5 |
| 11 | 17.2599 | 1998 | 2 | 17.2599 | 2728.4 |
| 12 | 18.2260 | 1999 | 1 | 18.2260 | 2728.4 |

Ends with **1 still dark** (0.1%) after 13 rounds.

**B_residual_p75** — basis `residual`, percentile 75

| round | estimate | disclosed | dark | mean true of the dark | total carried |
|---|---|---|---|---|---|
| 0 | 1.7145 | 0 | 2000 | 1.3642 | 3428.9 |
| 1 | 3.3212 | 1482 | 518 | 2.9507 | 2920.3 |
| 2 | 5.2090 | 1866 | 134 | 4.9477 | 2763.4 |
| 3 | 7.6167 | 1965 | 35 | 7.7297 | 2724.4 |
| 4 | 14.4177 | 1990 | 10 | 11.8078 | 2754.5 |
| 5 | 16.7768 | 1996 | 4 | 15.8284 | 2732.2 |
| 6 | 18.2260 | 1999 | 1 | 18.2260 | 2728.4 |

Ends with **1 still dark** (0.1%) after 7 rounds.

**C_population_median** — basis `population`, percentile 50

| round | estimate | disclosed | dark | mean true of the dark | total carried |
|---|---|---|---|---|---|
| 0 | 0.9951 | 0 | 2000 | 1.3642 | 1990.2 |
| 1 | 0.9951 | 950 | 1050 | 2.0924 | 1576.2 |

Ends with **1050 still dark** (52.5%) after 2 rounds.

### Verdict

| hypothesis | result |
|---|---|
| H1_estimate_rises_monotonically_A | **PASS** |
| H1_estimate_rises_monotonically_B | **PASS** |
| H2_residual_basis_unravels_A | **PASS** |
| H2_residual_basis_unravels_B | **PASS** |
| H3_population_basis_leaves_more_dark | **PASS** |

### What this still does not settle

- The stated limits of the sim are the sim's own, printed under READ THIS BEFORE QUOTING THE NUMBERS, and they still stand: market access is not modelled, agents are myopic, and the disclosure cost is a guess.

