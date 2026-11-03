# Pledge term on the κ-tied ledger — result

> **Version:** 0.1
> **Date:** 2026-10-31

> **Run:** `python 06-simulation/stable-band/pledge_band_kappa.py` · **Self-tests:** `... --test`, 6 pass
> **Transcript:** [`PLEDGE_KAPPA_RUN.txt`](PLEDGE_KAPPA_RUN.txt) · **Declared before running:** [`PLEDGE_KAPPA_DECLARED.md`](PLEDGE_KAPPA_DECLARED.md)
> **Request:** `sr-20261028-run-pledge-band-py-s-pledge-term-on-the-kapp` · **Seed:** population 7, age seeds 11 and 12, backed-set seed 99

## 1. The question

> Run pledge_band.py's pledge term on the kappa-tied ledger of sr-20261026 (demand 1,380 h/yr, past debit 1,380 h/yr, same ages, all join on day one, M = 100, capacity 56,446): report the publishable upper edge at pledge density p = 0, 0.25, 0.5, 0.75, 1 at F = 2, 10, 14, beside break-even 3.78/F, and state whether the one-day rule edge = rho*(F)/(1+p) still holds.

**Terms.** `p` is the share of the network's earned credit that has been committed as backing, so total backing `P` = p × total credit `C` (IC-8). The **publishable upper edge** is the highest published ρ at which the gate still rations. **Break-even** is 3.78 ÷ F, the ρ at which a year of floor credit balances 1,380 h of consumption. `pledge_band.py` computes the edge as ρ\*(F) ÷ (1 + p) by division. This run puts `P` into the kernel's gate `D ≤ ρ·(C + P)` and finds the edge by bisection.

## 2. Declared before running

Full table in `PLEDGE_KAPPA_DECLARED.md`. Result of each:

| # | Kind | Declared | Result |
|---|---|---|---|
| O1 | **Level** | One-day edge at p = 0: F = 2 in [0.95, 1.10], F = 10 in [0.30, 0.36], F = 14 in [0.23, 0.28] | **1.017, 0.330, 0.253. Held** |
| O2 | **Level** | One-day edge at F = 10, p = 1 in [0.155, 0.175] | **0.165. Held** |
| O3 | Relation (near-entailed) | Arm A cumulative = ρ\*/(1+p) within 0.005, all 15 cells | **Held.** Largest gap 0.0002. Checks the code, not the economy |
| O4 | **Level** | Arm B (frozen pledges) at F = 10, p = 1 in [0.20, 0.32] | **0.192. FAILED.** Below the band. The direction was right (between 0.165 and 0.330); the size was not |
| O5 | Relation | Arm C differs from arm A by more than 0.005 at p = 0.5, F = 10 | **Held.** 0.291 against 0.220 |
| O6 | Relation (cannot fail) | Publishable edge ≤ break-even in every cell | Held, and could not have failed: the p = 0 edge was already below break-even and p ≥ 0 only lowers it |

## 3. The numbers

**Absolute.** R_max = 56,446 real units. People want 66,407. κ = 3.7808, so a year of demand is 1,380 h. Population 60,000.

### 3.1 Publishable upper edge, one day (kernel with P = p × C)

Kernel result equals the rule ρ\*/(1+p) to three decimals in all 15 cells.

| `F` | Break-even 3.78/F | p = 0 | p = 0.25 | p = 0.5 | p = 0.75 | p = 1 | p = 1 ÷ break-even |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 1.890 | 1.017 | 0.814 | 0.678 | 0.581 | 0.509 | 0.27 |
| 10 | 0.378 | 0.330 | 0.264 | 0.220 | 0.189 | 0.165 | 0.44 |
| 14 | 0.270 | 0.253 | 0.202 | 0.168 | 0.144 | 0.126 | 0.47 |

### 3.2 Cumulative edge (all join day one, M = 100), by pledge arm

Age-seed sd is 0.0000 to 0.0002 in every cell. Population seed not varied.

| `F` | Arm | p = 0 | p = 0.25 | p = 0.5 | p = 0.75 | p = 1 |
|--:|---|--:|--:|--:|--:|--:|
| 2 | **A** proportional | 1.017 | 0.814 | 0.678 | 0.581 | 0.509 |
| 2 | **B** frozen at joining | 1.017 | 1.017 | 1.017 | 1.017 | 0.946 |
| 2 | **C** concentrated | 1.017 | 1.017 | 1.016 | 1.016 | 0.946 |
| 10 | **A** | 0.330 | 0.264 | 0.220 | 0.189 | 0.165 |
| 10 | **B** | 0.330 | 0.303 | 0.254 | 0.218 | 0.192 |
| 10 | **C** | 0.330 | 0.306 | 0.291 | 0.278 | 0.192 |
| 14 | **A** | 0.253 | 0.202 | 0.168 | 0.144 | 0.126 |
| 14 | **B** | 0.253 | 0.217 | 0.182 | 0.156 | 0.137 |
| 14 | **C** | 0.253 | 0.231 | 0.216 | 0.205 | 0.137 |

**Cumulative edge ÷ rule ρ\*/(1+p):** arm A 0.999–1.000 everywhere. Arm B 1.07–1.16 at F = 10, 14, and 1.25–1.86 at F = 2. Arm C 1.09–1.47 at F = 10, 14 (1.16 and 1.09 at p = 1), 1.25–1.86 at F = 2.

**Worked example, F = 10, p = 1, arm B.** The rule gives 0.330 ÷ 2 = 0.165. The kernel gives 0.192, 16% higher. A published ρ of 0.192 passes the capacity test in the frozen arm and would fail it under the rule.

### 3.3 Beside break-even

Arm A (the rule): the edge is 0.27 to 0.94 of break-even. At F = 10 it falls from 0.87 (p = 0) to 0.44 (p = 1). The documented ρ = 1.2 is 3.6× the edge at p = 0 and 7.3× at p = 1.

## 4. Answer to "does the one-day rule edge = ρ\*(F)/(1+p) still hold?"

- **One-day: yes, exactly,** at all 15 cells, through the kernel. This is arithmetic: the gate reads ρ(1+p)C when P = p × C.
- **Cumulative, with backing that tracks credit (arm A): yes,** for the same reason.
- **Cumulative, with backing committed once and not topped up (arm B), or concentrated on some people (arm C): no.** The rule understates the publishable edge, by 7% to 16% at F = 10 and 14, and by up to 86% at F = 2. Using the rule there is conservative: it publishes a lower ρ than the kernel needs.

## 5. What this does not show

1. **Which arm a real network is.** Arm A needs pledges to grow in step with credit forever. Arm B is the opposite extreme. Real backing is committed in lumps (Foundations 4.6) and sits between them. Nobody measured it. The three arms bracket the answer and do not locate it.
2. **That p is measurable.** It is swept. Pledge density is a behavioural quantity.
3. **Why F = 2 barely moves under B and C.** The edge stays at the p = 0 value for p ≤ 0.75. I read this as the capacity test being set by late periods where frozen backing is a small share of credit, and did not test that reading.
4. **The lower edge.** Essentials affordability was not recomputed. By `pledge_band.py`'s own argument it is read at p = 0 and does not move.
5. **Anything beyond the κ run's limits.** One population (seed 7), everyone joins day one, no births or deaths, 1,380 h/yr is today's US-method median and not the essentials basket, capacity fixed at 85% of wants.
6. **That arm C's backed set is realistic.** Backed people get P equal to their joining credit, picked at random. Real backing concentrates on particular people, not random ones, and `P` does not stop at 1× their own credit (Foundations 5.5.5).
7. **That the O3 and O6 rows are evidence.** O3 follows from the gate's form and O6 could not fail. They are reported because the request asked for the beside-columns.

## 6. Re-run

```
python 06-simulation/stable-band/pledge_band_kappa.py --test
python 06-simulation/stable-band/pledge_band_kappa.py > 06-simulation/stable-band/PLEDGE_KAPPA_RUN.txt
```

Seeds: population 7 (`stable_band.RNG_SEED`), age seeds 11 and 12, backed-set seed 99. Run time about 5 minutes. New files under 100 KB.
