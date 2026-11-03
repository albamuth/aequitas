# Exit-step table — coarse-read ÷ fine-read ratio, one row per co-product

> **Date:** 2026-11-01 · **Code:** [`exit_table.py`](exit_table.py) · **Data:** [`exit_table.csv`](exit_table.csv)
> **Extends:** [`RESULTS.md`](RESULTS.md) (same chains, same passage tables; nothing new is modelled)

## 1. The question (quoted from request sr-20260911-over-a-real-multi-step-process-flow-sheet-ta)

> Over a real multi-step process flow sheet, tabulate the coarse-read-over-fine-read ratio as a COLUMN against exit step, one row per co-product, each row recomputable from the chain table alone. Report the maximum, the ratio for the main output, and the mass-weighted mean across all outputs.

**Terms.** *Coarse read*: the whole chain's energy over the product's mass. *Fine read*: the energy of only the steps the product passed, over its mass. *Ratio* = total chain energy ÷ energy of steps passed (the mass cancels). *Exit step* = the last step, in processing order, that the product passed.

## 2. Outcomes declared before running

| # | Kind | Declared outcome | What would have failed it |
|---|---|---|---|
| L1 | **Level** | Steer: the hide's energy ratio is **6.25 ± 0.01**, the number @hemei called our headline. | Any other value means the headline is not what they said it is |
| L2 | **Level** | Steer: main output (packaged beef) reads **1.00 ± 0.01**. | Above 1.05 means "main output sits near 1.00×" is wrong |
| L3 | **Level** | Refinery: maximum is **between 2 and 3**, main output (gasoline, largest mass) **between 1.1 and 1.5**. Both are from the committed RESULTS.md; a new table that disagrees by more than that has a bug. | Outside the band |
| L4 | **Level** | Mass-weighted mean for each chain is **below the unweighted mean** (the heavy outputs exit late). | Mean ≥ unweighted mean |
| C | Change | Rows sorted by exit step give a **non-decreasing-then-falling** ratio only if passage is a prefix of the chain. If passage is not a prefix, exit step does **not** order the ratio. | Refinery rows monotone in exit step |
| R | Recompute | A second path that reads only the CSV (two energy columns) reproduces every ratio to 1e-12. | Any mismatch |

## 3. The numbers

Every row: passed energy and total energy are printed beside the ratio, so each is one division.

### Steer (illustrative digits: 600 kg animal, 500 MJ, seven steps)

| exit # | exit step | co-product | mass kg | passed MJ | total MJ | coarse ÷ fine |
|--:|---|---|--:|--:|--:|--:|
| 2 | hide_off | hide | 40 | 80 | 500 | **6.25×** |
| 3 | organs_out | organs | 60 | 120 | 500 | 4.17× |
| 4 | hooves_head | hooves and head | 30 | 140 | 500 | 3.57× |
| 7 | packaging | **packaged beef (main)** | 250 | 500 | 500 | **1.00×** |

Max **6.25×** (hide) · main output **1.00×** · mass-weighted mean **2.26×** (857.1 ÷ 380) · unweighted mean 3.75×.

### Refinery (real DOE 2015 per-process energies; processing order and passage table declared)

| exit # | exit step | co-product | mass kg | passed | total | coarse ÷ fine |
|--:|---|---|--:|--:|--:|--:|
| 2 | vac_distillation | asphalt | 491 | 826 | 2,118 | **2.56×** |
| 2 | vac_distillation | residual fuel | 472 | 826 | 2,118 | 2.56× |
| 3 | coking | petcoke | 835 | 940 | 2,118 | 2.25× |
| 7 | alkylation | LPG | 437 | 1,028 | 2,118 | 2.06× |
| 8 | hydrotreating | jet | 1,272 | 1,079 | 2,118 | 1.96× |
| 8 | hydrotreating | diesel | 4,006 | 1,301 | 2,118 | 1.63× |
| 8 | hydrotreating | **gasoline (main, largest mass)** | 5,765 | 1,697 | 2,118 | **1.25×** |

Max **2.56×** (asphalt, tied with residual fuel) · main output **1.25×** · mass-weighted mean **1.62×** · unweighted mean 2.04×.

**Outcome check.** L1 held (6.250). L2 held (1.000). L3 held (2.56; 1.25). L4 held on both (2.26 < 3.75; 1.62 < 2.04). R held (11 rows, 7/7 self-tests).
**C held, and it is the finding:** in the refinery three products share exit step 8 and read 1.25×, 1.63× and 1.96×. **Exit step does not determine the ratio; the energy of the steps passed does.** Passage there is not a prefix of the chain (LPG skips vacuum distillation, jet skips reforming). Only in the steer, a straight line, does a later exit always mean a lower ratio.

## 4. What this does not show

1. **The steer's digits are invented.** Only the refinery's step energies are real. The 6.25× is therefore a number from an illustrative chain, and so is the published sentence it supports. The request asked for a *real* flow sheet; only one real chain exists here, and it does **not** contain a 6.25×.
2. **The refinery's passage table and processing order are declared**, not measured. Moving one passage cell moves that product's ratio. `06-simulation/false-passage/` covers a lie of that kind; this run does not.
3. **Two chains is not a distribution.** No claim is made that "main output ≈ 1.0–1.3×, worst ≈ 2.5–6×" holds for a CHP plant, a chemical plant or a farm.
4. **Energy only, and the refinery's absolute columns are not megajoules.** The refinery step energies are DOE metered actuals in **TBtu/yr** (U.S. 2010, `allocation-engine/refinery_slice.py` lines 84–87), and the code field is named `energy_mj`. Every ratio is unit-free, so no ratio depends on the label. The "passed" and "total" refinery columns above (2,118 total) are in TBtu/yr, not MJ.
5. **"Main output" is a choice.** It is taken as the largest-mass co-product (beef, gasoline). A network that names the main output differently reads a different row.
6. **The mass-weighted mean weights by mass, which is the request's choice.** Weighted by energy, or by what buyers take, it would differ. It is not a quantity the theory uses anywhere.
7. **Contiguity of blocks is assumed** (as in RESULTS.md): the coarse read is the single opaque block.

## 5. Command and seed

```bash
python 06-simulation/chain-resolution/exit_table.py --csv 06-simulation/chain-resolution/exit_table.csv
python 06-simulation/chain-resolution/exit_table.py --test
```

Deterministic. No random numbers, so no seed. Needs numpy (via `allocation-engine/refinery_slice.py`); do not run with `python -I`.
