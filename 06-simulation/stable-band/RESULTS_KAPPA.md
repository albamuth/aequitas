# Both edges with κ tied to the measured anchor — result

> **Version:** 0.1
> **Date:** 2026-10-27

> **Run:** `python 06-simulation/stable-band/stable_band_kappa.py` · **Self-tests:** `python 06-simulation/stable-band/stable_band_kappa.py --test`, 6 pass
> **Transcript:** [`KAPPA_RUN.txt`](KAPPA_RUN.txt) · **Declared before running:** [`KAPPA_DECLARED.md`](KAPPA_DECLARED.md)
> **Request:** `sr-20261026-re-run-stable-band-py-with-kappa-tied-to-the` · **Seed:** population 7, age seeds 11–15 (no other randomness)

---

## 1. The question

> Re-run stable_band.py with kappa tied to the measured anchor: each person's yearly demand is 1,380 h/yr at the US method, not the median daily credit x 365 (13.797 h x 365 = 5,037 h/yr, line 187). Report BOTH edges at F = 2, 10, 14: the one-day rho* and the cumulative rho*_L (same ages, joining schedule, M and capacity as sr-20261023), beside break-even 3.78/F. Declare kappa, capacity and population before running. State whether capacity still binds at kappa = 1,380.

**Terms.** κ (kappa) is debit-hours a person asks for per day per unit of median lifestyle. `F` is the floor in hours a day. ρ is the debit tolerance in the gate `D ≤ ρ·(C + P)`. ρ\* is the highest ρ at which admitted demand still fits inside capacity `R_max`. ρ\*_L is that edge when every one of 100 yearly periods must fit. **Break-even** is `3.78 / F`, the ρ at which a floor-only person's yearly room `ρ·F·365` equals one median lifestyle, 1,380 h.

## 2. Declared before running

Inputs: κ = 1,380 / 365 = **3.7808**. Capacity `R_max` = **56,446 real units**, unchanged (0.85 × 66,407 wanted). Population 60,000, seed 7. Ages, joining on day one, M = 100, joiner credit `F × 365 × age`, joiner debit `1,380 × age`: as in `stable_band_cumulative.py`.

| # | Kind | Declared | Result |
|---|---|---|---|
| O1 | **Level** | One-day ρ\* at F = 10 in [0.28, 0.38] | **0.330. Held.** |
| O2 | **Level** | One-day ρ\* at F = 2 in [0.85, 1.20]; at F = 14 in [0.20, 0.30] | **1.017 and 0.253. Held.** |
| O3 | **Level** | Cumulative ρ\*_L at F = 10 in [0.28, 0.38] | **0.330. Held.** |
| O4 | Relation | ρ\*_L within 5% of one-day ρ\* at all three F | **Held.** Ratio 1.000 at all three |
| O5 | Instrument | One-day edge = old edge × 0.274, within 0.03 | **Held.** 1.017 / 0.330 / 0.253 against scaled 1.017 / 0.330 / 0.253 |
| O6 | Capacity | Edge neither censored nor below the grid | **Held.** No flag at any F |

O1–O3 and O5 were stated over levels and each had a band under 0.4 wide. Each could have failed. O4 could have failed if the stored room of joiners mattered, as it did at the old κ.

## 3. The numbers

**Absolute.** `R_max` = 56,446 real units. People want 66,407 in total. κ = 3.7808 h per unit per day, so a year of demand is 1,380 h per median person (old: 5,037 h).

### 3.1 Both edges

| `F` | Break-even 3.78/F | **One-day ρ\*** | **Cumulative ρ\*_L** | Edge ÷ break-even | Old κ: one-day / cumulative (sr-20261023) |
|--:|--:|--:|--:|--:|--:|
| 2 | 1.890 | **1.017** | **1.017** | 0.54 | 3.712 / 1.982 |
| 10 | 0.378 | **0.330** | **0.330** | 0.87 | 1.206 / 0.416 |
| 14 | 0.270 | **0.253** | **0.253** | 0.94 | 0.922 / 0.299 |

**Spread.** Five age seeds give identical ρ\*_L to three decimals (sd 0.0000). That is a spread across age draws only. **The population seed was not varied.**

### 3.2 Does capacity still bind at κ = 1,380?

**Yes, and only through ρ.** People want 66,407 units and capacity is 56,446 (85%). The gate admits less than capacity at low ρ, and more at high ρ:

| `F` | ρ = 0.05 | ρ = 0.25 | ρ = 1.0 | ρ = 4.0 |
|--:|--:|--:|--:|--:|
| 2 | 4,838 | 23,740 | 56,151 | 66,319 |
| 10 | 11,186 | 48,788 | 66,328 | 66,407 |
| 14 | 14,358 | 56,172 | 66,400 | 66,407 |

Admitted units in one day, against `R_max` of 56,446. At F = 10, ρ = 1.0 the gate admits 66,328 of 66,407 wanted and capacity decides who gets what; below ρ = 0.330 the gate rations.

### 3.3 What changed from κ = 13.797

- **The one-day edge moves by exactly the ratio of the two κ values (0.274).** Requests scale with κ and capacity is in real units, so admitted units depend on ρ ÷ κ only. This is arithmetic. Self-test 3 checks it.
- **The cumulative edge no longer falls below the one-day edge.** Past debit is now 1,380 h/yr, equal to the yearly request κ × 365. Joiners arrive with the same rate of debit they go on asking for. Admitted demand starts below the one-day level and rises to it (section 3 of `KAPPA_RUN.txt`: F = 10 at the edge, period 1 admits 4,038, period 10 admits 54,064, period 50 admits 56,438). The last period, not the first, sets the edge.
- **Setting past debit back to 5,037 with κ = 3.78 gives 1.894 / 0.489 / 0.362**, above the one-day edge at all three F. The old fall came from a mismatch between past debit (1,380) and flow (5,037), and the size of the fall followed the gap.
- **Both edges now sit below break-even** at every F asked: 54%, 87% and 94% of it. At F = 10 a floor-only person has room `0.330 × 3,650 = 1,205` h a year against 1,380 h for one median lifestyle.

## 4. What this does not show

1. **That 1,380 h/yr is the right demand.** It is the US-method median of today's consumption (Foundations 3.5), one reading with an unreviewed upstream convention in it. It is not the essentials basket `E`. If demand per person is 3.78 h a day for everyone, wants only differ by the lognormal spread of `wants`, which is assumed (σ = 0.45), not measured.
2. **That cumulative equals one-day in a real economy.** The equality is built in: joiners' past debit equals the later rate by declaration. People whose real past consumption differed from 1,380 h/yr, or whose future demand differs from their past, would move the cumulative edge. The 5,037 variant shows the direction.
3. **That capacity is 85% of wants.** `R_max` was held at the old value on purpose (the request says so). Whether 0.85 is right is the open input from `disparity-ceiling/rho_sweep.py`. The edge scales with it; this run did not vary it.
4. **Anything about population-seed noise, deaths, births or later joining.** One population (seed 7), no deaths, everyone joins on day one, M = 100 years.
5. **That a network should set ρ at the edge.** The edge is where capacity stops being rationed by the gate. It is not a recommended setting, and the lower edge (essentials affordable) was not recomputed. Break-even here is for a full median lifestyle, not for essentials.
6. **The return-to-one-day period.** The old metric is degenerate here: the path starts below the one-day level, so "first period at or below 1.01 × one-day" is period 1. It was not reinterpreted.

## 5. Re-run

```
python 06-simulation/stable-band/stable_band_kappa.py --test
python 06-simulation/stable-band/stable_band_kappa.py > 06-simulation/stable-band/KAPPA_RUN.txt
```

Seeds: population 7 (`stable_band.RNG_SEED`), age seeds 11–15. Run time about one minute on this machine. New files: under 100 KB.
