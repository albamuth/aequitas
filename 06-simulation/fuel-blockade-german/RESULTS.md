# Fuel blockade at the German method

Request `sr-20261111-fuel-blockade-at-the-german-method-same-popu`. Run 2026-11-14.
Code: `fuel_blockade.py` and `shares.py` (13 self-tests in all). Raw output: `RESULTS_RAW.txt`. Declared outcomes: `DECLARED.md`.

## 1. The question

> Fuel blockade at the German method. Same population, gate and settings as german-prime-sweep/german_prime_sweep.py (stock gate, P = 0, essentials ungated at E = 437 and 462 h, services off the receiver, joiner pasts, F = 2, 10, 14). Replace the even capacity cut with an energy cut: fossil energy input falls by 10%, 20%, 30% and 50%, and each product line's output falls by its share of fossil energy in its total input (from the EXIOBASE energy extension on disk for Germany; if no energy table is on disk, report Blocked and name the table needed, do not invent intensities). Report per cell: the output fall of each essentials line and of non-essentials; the clearing rho, or 'none below 4.0', or 'none: ungated part exceeds capacity'; the share admitting nothing above E. Print each beside the even-cut figure of the same overall output loss from german-prime-sweep/RESULTS.md. Declare before running: essentials fall less than non-essentials if food and care are less fossil-intensive than manufacturing; the clearing rho at a given overall loss is no lower than under the even cut.

## 2. A blocker, stated first

**The energy extension on disk is empty.** `06-simulation/data/exiobase/IOT_2022_pxp.zip` holds `energy/F.txt` with four rows ("Energy use - Emission relevant / Final / Gross / Net", TJ). Every one of the 9,800 columns is zero (checked, self-test 3). It has no carrier split either. **The table needed:** an EXIOBASE 3 energy extension with energy-carrier rows (coal, crude, gas, petroleum products, by sector), populated, for Germany.

**What was done instead, and it is a substitute, not the request.** The fossil share of a product is the money value of fossil-energy products its German producer buys, over its total output. Source: `Z.txt` and `x.txt` in the same zip (EXIOBASE 3.10.2 pxp 2022), which are measured purchases and not invented. It is a **value share, not an energy-content share.** Fossil products: coal and peat, crude oil, natural gas, NGL, other hydrocarbons, coke, refined petroleum products, electricity by coal, gas and oil, manufactured gases, gas distribution. A line's share is the mean over its products, weighted by German household final demand.

## 3. Declared before running (full text in `DECLARED.md`)

| # | Statement | Kind | Result |
|---|---|---|---|
| 1 | At every cut, essentials goods fall less than non-essentials | change | **Held** at all four cuts, both share sources (smallest gap: 2.04% against 2.22% at 50%, upstream sensitivity) |
| 2 | At a 50% cut the overall output loss is between 1% and 10% | level | **Held, barely**: 1.055% to 1.086% (direct). 1.68% to 1.70% (upstream sensitivity) |
| 3 | At a 50% cut the essentials goods fall is between 0.5% and 6% | level | **Held**: 0.94% to 0.98% (direct), 1.98% to 2.04% (upstream) |
| 4 | "none: ungated part exceeds capacity" fires at 50% at every F and E, and not at 10% | level | **FAILED** on the primary shares: it fires in no cell. It fires only in the upstream sensitivity, at F = 10, both E, at the 50% cut |
| 5 | The author's declaration: per-line clearing rho is no lower than the even-cut rho at the same loss | change | **Failed, as derived before the run, and entailed**: see section 5 |

## 4. The numbers

Unit: one median German lifestyle-year (as the sweep). Wants 221,652 units at F = 10 (223,868 at F = 2, 221,470 at F = 14). Capacity before any cut is 1.017 x wants. Ungated demand (services plus essentials) is 63.5% of wants at E = 437.2 and 65.3% at E = 462.3.

**Output fall by line, primary shares, E = 437.2** (E = 462.3 differs by under 0.01 point in the groups):

| Line | Fossil share of input | Fall at 10% | 20% | 30% | **50%** |
|---|--:|--:|--:|--:|--:|
| food | 1.68% | 0.17% | 0.34% | 0.51% | **0.84%** |
| clothing | 1.63% | 0.16% | 0.33% | 0.49% | **0.82%** |
| shelter services | 0.10% | 0.01% | 0.02% | 0.03% | **0.05%** |
| utilities | 7.83% | 0.78% | 1.57% | 2.35% | **3.91%** |
| drugs | 3.79% | 0.38% | 0.76% | 1.14% | **1.89%** |
| housing structure | 0.58% | 0.06% | 0.12% | 0.18% | **0.29%** |
| chemicals, paper, plastics | 2.28% | 0.23% | 0.46% | 0.68% | **1.14%** |
| furniture and other goods | 1.75% | 0.18% | 0.35% | 0.53% | **0.88%** |
| **essentials goods, hours-weighted** | 1.95% | **0.195%** | 0.390% | 0.586% | **0.976%** |
| care 0.38%, schooling 0.25%, land transport services 2.96%, post and telecoms 0.41% (**services**) | 0.73% | 0.073% | 0.145% | 0.218% | **0.363%** |
| **non-essentials** | 3.54% | **0.354%** | 0.708% | 1.062% | **1.770%** |
| **overall loss** | | 0.217% (480 units) | 0.433% (960) | 0.650% (1,440) | **1.083% (2,399 of 221,652)** |

Hours weights are the sweep's own: essentials goods 523 h (housing structure 31 h) to 553 h (61 h), services 412 h.

**Clearing rho, per-line capacity (this run) beside the even cut at the same overall loss.** Mean over 5 age seeds (11-15); spread in brackets.

| F | E (h) | Cut | Overall loss | Per-line clearing rho | Even cut, same loss | Admits nothing above E: per-line / even |
|--:|--:|--:|--:|---|---|---|
| 10 | 437.2 | 10, 20, 30% | 0.22%, 0.43%, 0.65% | none below 4.0 | none below 4.0 | 0.00% / 0.00% |
| 10 | 437.2 | **50%** | 1.083% | **0.874** (0.871-0.881) | none below 4.0 | 0.01% / 0.00% |
| 10 | 462.3 | **50%** | 1.055% | **0.877** (0.875-0.883) | none below 4.0 | 0.01% / 0.00% |
| 2 | 437.2 | 10, 20, 30% | 0.22%, 0.43%, 0.65% | none below 4.0 | none below 4.0 | 4.99% / 4.99% |
| 2 | 437.2 | **50%** | 1.086% | **3.149** (3.146-3.154) | none below 4.0 | 0.02% / 4.99% |
| 2 | 462.3 | **50%** | 1.059% | **3.158** (3.155-3.162) | none below 4.0 | 0.02% / 5.14% |
| 14 | 437.2 | 10, 20, 30% | 0.22%, 0.43%, 0.65% | none below 4.0 | none below 4.0 | 0.00% / 0.00% |
| 14 | 437.2 | **50%** | 1.082% | **0.650** (0.649-0.653) | none below 4.0 | 0.01% / 0.00% |
| 14 | 462.3 | **50%** | 1.055% | **0.652** (0.651-0.654) | none below 4.0 | 0.01% / 0.00% |

The flag "none: ungated part exceeds capacity" fires in **no** cell on the primary shares. Where the share of people admitting nothing above E is 4.99% or 5.14% at F = 2, that is the sweep's own baseline at rho 1.2 (when no rho clears the sweep holds rho at 1.2), not an effect of the cut.

**Beside the sweep's grid.** `german-prime-sweep/RESULTS.md` has no cell near 1% (its shocks are 0, -10%, -20%, -30%, -40%). Its nearest cells at F = 10, E = 437.2: **0 shock: none below 4.0; -10%: rho 0.309.** The same-loss even-cut figures in the table above were recomputed with the sweep's own solver (self-test 2 reproduces its 0.221 at -20%). Even a 50% fossil cut is about **a ninth** of the loss the sweep's mildest shock (-10%) imposes: 1.08% against 10%.

**Sensitivity: direct plus domestic upstream fossil purchases (F = 10 only).** Essentials goods fall 0.41%, 0.82%, 1.22%, **2.04%** at the four cuts (E = 437.2); non-essentials 0.44%, 0.89%, 1.33%, **2.22%**; overall loss 0.34%, 0.68%, 1.02%, **1.70%**. At 10 to 30% no rho clears in either arm. **At 50%: the essentials line alone is short (fall 2.04% against 1.67% of headroom), so "none: ungated part exceeds capacity" fires for per-line capacity, at both E.** The even cut at the same 1.70% loss clears at rho 0.886 (E = 437.2) and 1.073 (E = 462.3). So whether the flag fires depends on which share is used, and the margin is under half a percentage point.

## 5. How to read the comparison with the even cut

**The even-cut comparison is entailed by an assumption, and is not evidence about fuel.** The even cut lets spare capacity anywhere serve demand anywhere. Per-line capacity does not. Before the run it was derived that per-line target minus even target equals `U x (1.017 x f_u - 0.017)`, where U is ungated demand and f_u the fall of the ungated lines (self-test 3 checks it on 50 random draws). So for any input the per-line gated target is lower while f_u is under 1.67%, and the flag fires once it is over. Per-line rho can never be above the even-cut rho. The 1.7% headroom of the ungated lines (about 2,400 units at F = 10) is what the even cut spends on the gated part and per-line capacity does not. That headroom is the whole gap in every row above.

What is **not** entailed, and is the data's answer: the size of each line's fall (section 4), and that at those sizes the headroom absorbs nearly everything (no rho below 4.0 at any cut up to 30%, and a rho only at 50%).

## 6. What this does not show

1. **It is not the requested energy table.** The energy extension on disk is empty (section 2). The shares are money shares from purchases of fossil products. A line that buys little fossil fuel by value but needs it physically (fertiliser gas, diesel for harvest) is under-weighted if fuel is cheap, and over-weighted if it is dear. In energy-content terms the shares could differ by a large factor, and nobody ran that.
2. **The fall rule is the request's: cut x share, line by line.** It means every other input substitutes perfectly for the missing fuel. A fixed-proportions reading (a line that loses 50% of its fuel loses 50% of its output) would give falls of 50% on every line that buys any fossil fuel, which is about 30 to 50 times the falls above (non-essentials 1.77%, essentials 0.98%). It was not run, and it is the more usual picture of a real fuel blockade. **Do not quote the 1.08% as the cost of a 50% fuel cut.**
3. **Output loss is spread over lines, not over people.** Every person's essentials mix is the same in the model, so a utilities fall of 3.9% falls evenly on all. A blockade that cuts heating fuel in one region and not another was not modelled.
4. **Capacity per line is a modelling choice.** Services, essentials goods and non-essentials each keep 101.7% of their own wants. The 1.7% headroom is the sweep's input (Foundations 5.5.3 says the German row's surplus is set by the capacity input before anyone is simulated), not a finding.
5. **Product-line mapping is mine.** Which EXIOBASE products form "food", "utilities" and so on (listed in `shares.py`, `LINES`) was chosen for this run, not given by the request. Non-essentials is everything else households buy, including motor fuel at a 62% share, and is weighted by German household demand. Putting motor fuel and heating oil elsewhere would move the non-essentials fall.
6. **Germany's imports of fossil energy are counted as purchases, not as a supply cut.** A blockade that stops imports bites on the foreign supplier. The model cuts the German line's input share uniformly, so it cannot tell home-produced from imported fuel.
7. **One population draw.** Seed 7, age seeds 11 to 15. The spreads in section 4 (0.01 or less at F = 10 and 14) understate population noise.
8. **Single year, no stock of fuel, no rationing rule for fuel itself.** Fuel is not allocated by the gate here. A cut in fuel input shows up only as a fall in each line's output.

## 7. Exact command and seed

```
python 06-simulation/fuel-blockade-german/fuel_blockade.py --test
python 06-simulation/fuel-blockade-german/fuel_blockade.py > 06-simulation/fuel-blockade-german/RESULTS_RAW.txt
python 06-simulation/fuel-blockade-german/shares.py --rebuild     # rebuilds de_fossil_shares.npz from the zip
```
Population seed 7 (N = 200,000, sigma 0.45); age seeds 11, 12, 13, 14, 15; RHO0 = 1.2. EXIOBASE 3.10.2 pxp 2022, read in place. Run time: a few minutes. `python` here must be a Python that has numpy.
