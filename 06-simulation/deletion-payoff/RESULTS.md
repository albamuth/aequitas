# Does deleting a year of declared span pay? — ρ·F sweep across the conforming band

> **Date:** 2026-11-05 · **Request:** `sr-20260914-sweep-rho-f-across-the-conforming-band-f-fro` · **Foundations:** v0.67

## 1. The question

> <!-- struck-ok: quotes the sim request as filed 2026-09-14, before the 2026-10-16 wording ruling --> Sweep ρ·F across the conforming band (F from 1 to 14 h/day, ρ from the affordability floor to ρ\*(F)) and report, for each cell, the net debit-room a filer gains or loses per YEAR of declared span deleted on a 4.4 backdated reconstruction. Report the share of the conforming band in which deleting a year PAYS on the gate as well as on the published credit-per-day statistic. Use the recomputed median-lifestyle anchor, not 1,380 if that figure has moved.

**Terms.** The *gate* is `D ≤ ρ·(C + P)`. What a person *may still carry* is `ρ·(C+P) − D`. A *declared span* is how many years the reconstruction rebuilds (Foundations 4.4, condition 3). The *band* for floor `F` runs from `E/(365·F)`, below which a floor-only person cannot afford essentials basket `E`, up to `ρ*(F)`, above which the gate stops rationing. **Anchor:** it has not moved. Foundations v0.67 still reads 1,380 h/yr. Healthcare coverage makes it 1,162–1,380, and adequate provision about 1,296 (`median-lifestyle/HEALTH_SHARE.md`). All three are run.

## 2. Declared before running

Full table in [`DECLARED.md`](DECLARED.md). Result of each:

| # | Declared | Result |
|---|---|---|
| O1 (level) | E_max = 365·F·ρ\*(F) in [600, 1,350] h/yr for every F in 1..14, CAP 0.85 | **FAILED.** F = 1 gives **558 h**, below 600. The other 26 floors fall inside (664 to 1,291). The top of the range held |
| O2 (level) | Deleting pays in ≥ 95% of the open band, CAP 0.85, d = 1,380, broad-lower basket | **Held: 100%** |
| O3 (level) | Broad band open at 50–90% of the 27 floors | **Held: 23 of 27 (85%)** |
| O4 (relation) | Raising CAP 0.85 → 0.95 never raises the paying share | **Held:** 100% → 78% |
| O5 (relation) | d = 2,760 gives 100%. d = 690 gives less than d = 1,380 | **Held:** 100% and 0% |
| O6 (entailment) | The statistic is positive for any filer with past work, at every ρ and F | **Held, which makes it model-entailed.** See 3.4 |

## 3. The numbers

### 3.1 The gain in one line

Deleting one declared year removes `F·365` h of credit and `d` h of debit. **Gain per year deleted = `d − ρ·F·365`.** It is positive exactly when `ρ·F < d/365`, which is **3.78 h/day at d = 1,380.** Two consequences, both checked in the sweep:

- **At the bottom edge of the band the gain is `d − E`, whatever F is.** Broad-lower basket: 1,380 − 826 = **+554 h per year deleted** at every floor where the band is open.
- **At the top edge it is `d − E_max(F)`.** E_max is the largest basket the floor can carry (`365·F·ρ*`).

### 3.2 The published capacity (CAP 0.85), d = 1,380, broad-lower basket (826 h)

| `F` | band, ρ | break-even 3.78/F | gain at bottom edge | gain at ρ\* | Deleting pays in |
|--:|---|--:|--:|--:|---|
| 1 – 2.5 | closed (bottom edge above ρ\*) | — | — | — | no band |
| 3 | 0.754 – 0.783 | 1.260 | +554 h | +523 h | all of it |
| 5 | 0.453 – 0.552 | 0.756 | +554 h | +372 h | all of it |
| 10 | 0.226 – 0.330 | 0.378 | +554 h | **+174 h** | all of it |
| 14 | 0.162 – 0.253 | 0.270 | +554 h | **+89 h** | all of it |

**Share of the open band where deleting pays on the gate: 100% (23 of 23 open floors, 4,600 of 4,600 cells).** The smallest gain anywhere is **+89 h per year deleted** at F = 14, ρ = ρ\*. The band's top edge sits 6–38% below break-even at every F.

### 3.3 The share depends on capacity, which is an assumed input

CAP is physical capacity divided by wants. **0.85 is an illustrative input, not a measurement** (`stable-band/RESULTS_KAPPA.md`, limit 3). It decides the answer.

Share of the open band where deleting pays, width-weighted, d = 1,380:

| CAP | E_max at F = 10 | Narrow-lower (516 h) | Broad-lower (826 h) | Broad-higher (965 h) |
|--:|--:|--:|--:|--:|
| 0.70 | 847 h | 100% | 100% | band closed at every F |
| **0.85** | **1,206 h** | **100%** | **100%** | **100%** |
| 0.95 | 1,753 h | 85.9% | 78.2% | 71.1% |

**Critical capacity.** E_max reaches 1,380 h, so the top of the band reaches break-even, at **CAP = 0.964 (F = 2), 0.923 (F = 6), 0.894 (F = 10), 0.874 (F = 14)** (`critical_cap.py`). **Below those capacities the whole band pays. Above them the high-ρ end stops paying.** At CAP ≥ 1.0 the gate never rations (E_max(10) = 14,600 h, censored at the ρ = 4.0 end of the sweep), the band's top is not bounded by capacity, and every ρ above 3.78/F is in it.

### 3.4 The filer's own consumption

If the deleted year is one where the filer consumed less than the anchor, the gain shrinks. CAP 0.85, broad-lower basket:

| Filer's yearly debit `d` | Share of band where deleting pays |
|--:|--:|
| 690 h (half the median) | **0%** |
| 1,162 h | **91.3%** |
| 1,296 h | 100% |
| 1,380 h | 100% |
| 2,760 h (twice the median) | 100% |

The payoff therefore reaches **filers who consumed about 1,300 h a year or more**, which is the median and above. It does not reach a filer who consumed 690 h.

### 3.5 The credit-per-day statistic

Deleting a floor-only year changes the filer's published credit per day by `365·(a − F) / (days − 365)` where `a` is their lifetime average. **It is zero for a filer who never worked and positive for any filer who did.** It does not depend on ρ or on F. Examples (every F gives the same change):

| Filer | Average before | Change from deleting a floor-only year |
|---|--:|--:|
| 40 years, 20,000 h of work | F + 1.37 | **+0.035 h/day** |
| 40 years, 50,000 h of work | F + 3.42 | **+0.088 h/day** |
| 60 years, 100,000 h of work | F + 4.57 | +0.077 h/day |

**So "pays on both" equals "pays on the gate" for every filer who ever worked.** The statistic side cannot fail for such a filer. Under the project's own rule (Foundations 3.5, brief 4b) it is **model-entailed**, so it is reported and not counted as a second test. The disparity ceiling itself is untouched: a 24 h/day filer and a floor-only filer both keep their per-day figure, and `24 ÷ F` holds (self-test 6).

## 4. What this does not show

1. **That CAP is 0.85.** It is an illustrative input held from `stable-band`. The whole answer turns on it: 100% below CAP ≈ 0.87, 78% at 0.95, and the gate does not ration at all at 1.0. Nobody has measured the real ratio.
2. **That the filer's saving can be realised.** The gain is a change in what the filer may carry. It assumes the deleted years carry no evidence that contradicts the deletion. A span is a record and an unevidenced one is set by the earliest-date rule (4.4, condition 3). **This run measures the incentive and not whether the filer can act on it.** The cost of being found out is not modelled.
3. **How many years can be deleted.** The sweep is per year. It does not bound the total. Each deleted year gains the same amount, so the gain is linear in years, and nothing in the arithmetic stops at the filer's actual age. The `24 ÷ F` and IC-7 caps are on the numerator and denominator together and do not stop it.
4. **That d is the filer's real consumption in the deleted years.** The sweep treats it as a free parameter at five values. A real filer's early-life debit is unknown and is itself estimated at the unfavourable end (4.4, condition 2), which could raise d above the median and widen the gain.
5. **That ρ\*(F) is the right top edge.** It comes from a 60,000-person population with a lognormal wants spread assumed at σ = 0.45, the anchor tied to 1,380 for everyone, and the US production method. Other methods have not been measured (Foundations 4.4).
6. **A pledge term.** P is held at 0 and unchanged by deletion. Backing pledged to the filer is independent of span, so it adds to slack on both sides equally. A pledge-doubled effective ρ (`2ρ`, 4.6) would put more cells above break-even. The pledge-band run for the upper edge was not re-run here.
7. **The population seed.** One seed (7). Spreads in this run are across CAP, basket and d, not across populations.

## 5. Command and seed

```
python 06-simulation/deletion-payoff/deletion_payoff.py --test     # 8 self-tests
python 06-simulation/deletion-payoff/deletion_payoff.py            # sweep, writes RUN.txt (stdout), sweep_cells.csv, sweep_summary.json
python 06-simulation/deletion-payoff/critical_cap.py               # critical capacity
```

Seed: population 7 (`stable_band.RNG_SEED`), N = 60,000. No other randomness. Run time about 1 minute. Output: `RUN.txt`, `CRITICAL_CAP_RUN.txt`, `sweep_cells.csv` (one row per cap, basket, d, F), `sweep_summary.json`.
