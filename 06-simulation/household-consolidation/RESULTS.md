# Household consolidation — results

> **Version:** 0.1
> **Date:** 2026-10-16
> **Code:** [`household_consolidation.py`](household_consolidation.py) · **Declared outcomes:** [`DECLARED.md`](DECLARED.md)
> **Status: the code ran on 2026-10-16 (morning nightcheck). 8 of 8 self-tests pass. The central column below matches the code to two decimals.** The 04:00 run of 2026-10-16 could not run Python, so the tables in §3 were computed by hand first; the sweep output is in [`RUN.txt`](RUN.txt) and summarised in §3a.

---

## 1. The question

> Over a realistic household basket (two adults, one network), how much debit does routing co-products of one joint process (beef and hide, refinery products) to one member save under the max rule for fractional holdings, against the sum rule? Report the saving in hours per year and as a share of the household's debit.

## 2. Declared before running

Full table in [`DECLARED.md`](DECLARED.md). In short:

- **O1 (level):** reproduce Wubbitys: 1.60 h split, 0.80 h merged, saving 0.80 h.
- **O2 (control):** the sum rule saves 0.000 h.
- **O3 (level):** typical household, central saving under 1 h/yr and under 0.1% of debit.
- **O4 (level, ceiling):** every corner under 1% of debit (27.6 h/yr).
- **O5 (direction):** if both adults hold both co-products in like proportions, saving near 0.

## 3. The numbers

**Terms.** `S` is the saving: what A and B carry apart, minus what one account holding all of it carries. `f` is a holding's mass fraction of one co-product's output from one parcel. `q` is the share of a holding that points at the **same** parcels as the other member's co-product. **The household's debit is 2 × 1,380 = 2,760 h/yr** (Foundations §3.5 anchor, one reading).

### The rule, in one line

**For two adults each holding one co-product of one parcel, `S` on each step both co-products passed is `min(f_A, f_B) × the step's hours`.** So `S` can never be more than the smaller holding's carry on the shared steps, and it is zero where the two holdings come from different parcels.

### O1 — Wubbitys reproduced (hand)

8 h one-block steer. A holds 10% of the beef, B 10% of the hide.

| | Hours |
|---|--:|
| A alone, 0.1 × 8 | 0.80 |
| B alone, 0.1 × 8 | 0.80 |
| **Split** | **1.60** |
| One account, max(0.1, 0.1) × 8 | **0.80** |
| **S** | **0.80** |

Under the **sum rule** the merged account carries (0.1 + 0.1) × 8 = 1.60 h, so **S = 0.00 (O2).**

### The household, central parameters (hand)

Default allocation: **separated**, meaning A holds one co-product and B the other. This is the lever's largest setting.

| Household | Where the saving comes from | `S`, h/yr | Share of 2,760 h |
|---|---|--:|--:|
| **Typical**: petrol 900 gal, grill propane 36 kg, shop beef and leather | propane × 7.53 h shared steps × `q` = 0.2 | **0.12** | **0.0045%** |
| Propane-heated home, 1,041 kg | petrol's shared carry 3.29 h × `q` = 0.2 | 0.66 | 0.024% |
| Heating-oil home, 2,000 kg | petrol's shared carry 3.25 h × `q` = 0.5 | 1.63 | 0.059% |
| **Farm share**: one steer's beef and its hide, tanned | min(0.216, 0.20) × 18.75 h, plus 0.12 h refinery | **3.87** | **0.140%** |

**Worked, the typical row.** One 100 bbl crude parcel makes 5,765 kg of petrol and 437 kg of LPG. The household's petrol is 2,521 kg, so `f` = 0.437. Its propane is 36 kg, so `f` = 0.082. Calibrated so the petrol carries 4.1 h, the steps both pass (crude, distillation, cracking, alkylation) hold **7.53 h** per parcel. `S` = 0.082 × 7.53 = **0.62 h** if every litre of propane came from the petrol's own parcels. At `q` = 0.2 it is **0.12 h**.

**Worked, the farm share.** Steer chain 25 h, of which 75% (18.75 h) is raising, kill and hide removal, which beef and hide both pass. The household eats 54 kg of 250 kg beef (`f` = 0.216) and holds 1 kg of the 5 kg of leather from the hide (`f` = 0.20). `S` = 0.20 × 18.75 = **3.75 h**.

### Against the goods themselves (Wubbitys' "halves" framing)

| Household, `q` = 1 | Carry of those goods, split | `S` | `S` as share of those goods |
|---|--:|--:|--:|
| Typical, petrol + propane | 4.72 h | 0.62 h | 13% |
| Farm share, beef + leather | 9.15 h | 3.75 h | 41% |

**In plain words: the lever is large on the goods it touches and small on the household.** Those goods are a few hours out of 2,760.

### O5 — the mixed default (hand)

If each adult holds half the beef and half the leather (or half the petrol and half the propane), each account already takes the max inside itself. A: max(0.108, 0.10) = 0.108. B: the same. Merged: max(0.216, 0.20) = 0.216. **S = 0.** The lever exists only where a household's ordinary use puts different co-products on different people.

### O4 — the extreme corners (hand)

Every parameter at the end of its range that raises `S`, with `q` = 1:

| Piece | Corner | `S` |
|---|---|--:|
| Refinery | petrol 16 h carry, 70% crude share, 400 gal petrol (so petrol is the smaller fraction) | petrol's whole shared carry, 16 × 0.88 = **14.1 h** |
| Steer | 40 h chain, 85% shared, quarter steer `f` = 0.25, 2 kg leather `f` = 0.50 | 0.25 × 34 = **8.5 h** |
| **Both** | farm share at every high | **22.6 h = 0.82%** |

### Outcomes, scored by hand

| # | Result | Held? |
|---|---|---|
| O1 | 1.60 / 0.80 / 0.80 | **Yes** (hand) |
| O2 | 0.00 | **Yes** (hand) |
| O3 | 0.12 h, 0.0045% | **Yes** (hand) |
| O4 | worst corner 22.6 h, 0.82% | **Yes, with 0.18 points to spare** (hand) |
| O5 | 0 | **Yes** (hand) |

**Spreads.** None. The sweep that gives them has not run. The corner table is the only range there is.

### Shop-bought beef and leather

`q` for a household's beef and its leather is near zero. Ground beef points back at many steers, so each steer's beef fraction is tiny, and most US hides are tanned abroad. **By count** (≈100 to 10,000 steers touched by a household's beef, 1–3 hides behind its leather, ~3 × 10⁷ US cattle slaughtered a year), the expected `S` is about **2 × 10⁻⁷ h/yr**. This is an estimate and not a run.

### 3a. The code run of 2026-10-16

**Run by the morning nightcheck, not by the 04:00 agent.** `household_consolidation.py --test`: **8 of 8 self-tests pass.** Then the full run, seed 20261016, 20,000 uniform draws over the declared ranges, output in [`RUN.txt`](RUN.txt).

**Terms.** `S` is the saving in hours a year. **Central** uses every parameter at its declared central value. **p5** and **p95** are the 5th and 95th percentiles of `S` over the 20,000 draws. **Max** is the largest `S` any draw reached.

| Household | `S` central, h/yr | % of 2,760 h | `S` p5 | `S` p95 | `S` max | % max |
|---|--:|--:|--:|--:|--:|--:|
| Typical | **0.124** | **0.004%** | 0.082 | 3.299 | 12.425 | 0.450% |
| Propane-heated home | 0.658 | 0.024% | 0.524 | 9.293 | 13.421 | 0.486% |
| Heating-oil home | 1.625 | 0.059% | 0.837 | 8.857 | 13.415 | 0.486% |
| Farm share | 3.874 | 0.140% | 1.948 | 7.693 | 14.854 | 0.538% |

**In plain words: the code agrees with the hand table to two decimals on every central figure (0.12, 0.66, 1.63, 3.87), and no draw of 80,000 reached 1% of household debit.** The largest draw was 0.54%. The hand-computed worst corner of 22.6 h (0.82%) sits above any sampled draw because the sweep draws uniformly and rarely lands every parameter at its extreme at once; both are under the declared 1% ceiling, so O4 holds either way. O1, O2, O3 and O5 hold as declared.

## 4. What this does not show

1. **That the formulas are right.** The code executed on 2026-10-16 (§3a) and agrees with the hand figures, but both follow the same formulas, so a shared error in the formulas would not show here.
2. **`q` is declared, not measured.** No data on disk says what share of a household's propane or heating oil comes from the same refinery parcels as its petrol. The ceiling is `q` = 1 and is reported.
3. **The hour figures are scaled, not measured per process.** Steer hours (15–40 h) and petrol hours (2–16 h) are read off ERM-scale magnitudes in `median-lifestyle/TRACK1.md` and a superseded note of 0.7 jobs per $1M of gasoline. The ERM was not re-run for these cells.
4. **Labour only.** The energy and material dimensions of the debit vector are not swept separately. Fuel's combustion CO₂ rides each litre (§3.2b line 3) and is never a joint cost, so it is not in `S`. That part is a reading of the rule, not a guess.
5. **The denominator is today's median US consumption** (1,380 h/adult). A household with more or less debit moves the percentage, not the hours.
6. **Step costs inside the refinery follow DOE process energy as a proxy for hours.** That is a declared proxy.
7. **Strategic behaviour.** Nobody here goes looking for same-parcel goods. A household that set out to buy co-products of one parcel on purpose is the farm-share row, and it is capped at 8.5 h.

## 5. Command and seed

```
python 06-simulation/household-consolidation/household_consolidation.py --test
python 06-simulation/household-consolidation/household_consolidation.py
```

Seed **20261016**, 20,000 uniform draws over the ranges in `P` at the top of the file. **Run on 2026-10-16**; the output is in [`RUN.txt`](RUN.txt) and summarised in §3a.
