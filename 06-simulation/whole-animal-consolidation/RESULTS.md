# Whole-animal consolidation — results

> **Version:** 0.1
> **Date:** 2026-10-20
> **Code:** [`whole_animal.py`](whole_animal.py) · **Declared outcomes:** [`DECLARED.md`](DECLARED.md) · **Run output:** [`RUN.txt`](RUN.txt)
> **Status:** 7 of 7 self-tests pass. **The hour figures are declared ranges from memory. None was re-read from a source tonight** (no network), so no figure here carries a verified citation.

## 1. The question

> Hours on the shared steps of raising and slaughtering ONE whole lamb (meat and fleece both pass them), with a cited source, and the consolidation saving S = min(f_meat, f_fleece) x shared hours for a two-adult household that buys the whole lamb, one member holding the meat and the other the fleece, as hours a year and as a share of 2,760 h. Repeat for one whole chicken (meat and feathers).

## 2. Declared before running

Full table in [`DECLARED.md`](DECLARED.md). **L1** (level): lamb central S in 5–20 h. **L2** (level, ceiling): under 5% of lamb household-years reach 27.6 h. **L3** (level): chicken under 0.2 h a bird and under 10 h a year. **D1, D2** (direction) and **C1** (control).

## 3. The numbers

**Terms.** `S` is the saving: what the two adults carry apart, minus what one account holding all of it carries. `f` is the fraction of a co-product's output that a holding is. A whole animal has `f = 1` on both co-products, so `S` = the shared hours of one animal. The household's debit is 2 × 1,380 = **2,760 h/yr** (Foundations §3.5, one reading). **Shared hours** are direct labour on the steps both co-products pass, times an indirect multiplier (hours in the input industries) of 1.0 – 2.5, central 1.6.

### One whole lamb

| Piece | Low | Central | High | Basis |
|---|--:|--:|--:|---|
| Whole-flock labour per ewe-year, h | 2 | 7 | 15 | Declared from memory of extension enterprise budgets. Unverified |
| Lambs sold per ewe-year | 1.6 | 1.2 | 0.95 | Declared. Unverified |
| Ewe labour per lamb, h | 1.3 | 5.8 | 15.8 | 7 ÷ 1.2 at central |
| Feed growing, hauling, h | 0.25 | 0.6 | 1.8 | Declared |
| Kill and skin, h | 0.2 | 0.5 | 1.2 | Declared |
| Indirect multiplier | 1.0 | 1.6 | 2.5 | Declared |
| **Shared hours = S, one lamb** | **1.70** | **11.09** | **46.97** | (5.83 + 0.5 + 0.1 + 0.5) × 1.6 |

| Lamb household | `S`, h/yr | % of 2,760 h |
|---|--:|--:|
| Central, one lamb a year | **11.09** | **0.40%** |
| Two lambs a year, both paired | 22.19 | 0.80% |
| Low corner, one lamb | 1.70 | 0.06% |
| High corner, two lambs | 93.95 | 3.40% |
| Fleece shorn live, one lamb (kill not shared) | 10.29 | 0.37% |
| Only 60% of the carcass held as "meat" (rest returned) | 6.66 | 0.24% |

**Spread over 20,000 triangular draws** (mode at the central value, a sweep and not a distribution of truth):

| | p5 | p50 | p95 | max |
|---|--:|--:|--:|--:|
| `S` per lamb, h | 6.89 | 13.01 | 22.31 | 38.05 |
| `S` per household-year, h (1 to 2 lambs) | 8.62 | 17.04 | 31.48 | 59.40 |

**Share of draws at or above the 27.6 h bar (1%):** 0.76% per lamb. **10.24% per household-year**, because the sweep lets a household buy two lambs.

### One whole chicken

| Piece | Low | Central | High | Basis |
|---|--:|--:|--:|---|
| Grow-out labour, h/bird | 0.003 | 0.006 | 0.020 | Declared, contract-grower scale. Unverified |
| Catching and hauling, h | 0.001 | 0.003 | 0.008 | Declared |
| Hatchery and breeders, h | 0.001 | 0.003 | 0.006 | Declared |
| Feed (≈4.5 kg a bird), h | 0.003 | 0.006 | 0.012 | Declared |
| Kill, scald, pluck, h | 0.008 | 0.020 | 0.040 | Declared; plant ≈ 0.04 h/bird in all (1,300 workers, 1.2 M birds a week), about 40% before evisceration |
| **Shared hours = S, one bird** | **0.016** | **0.061** (3.65 min) | **0.215** | (0.038 direct) × 1.6 |

| Chicken household | `S`, h/yr | % of 2,760 h |
|---|--:|--:|
| Central, one bird a week (52) | **3.16** | **0.115%** |
| Low corner, 26 birds | 0.42 | 0.015% |
| High corner, 104 birds | 22.36 | 0.81% |
| Draws: p5 / p50 / p95 / max | 2.37 / 4.54 / 8.25 / 16.13 | 0.09% / 0.16% / 0.30% / 0.58% |

**No draw of 20,000 reached the 27.6 h bar.** The high corner, every parameter at its top, reached 0.81%.

### Outcomes, scored

| # | Result | Held? |
|---|---|---|
| L1 | Lamb central S = 11.09 h, inside 5–20 h | **Yes** |
| **L2** | **10.24% of lamb household-years reach 27.6 h, against a bar of under 5%** | **No, failed.** The cause is the two-lamb households (a quarter of draws). Per lamb it is 0.76% |
| L3 | Chicken 0.061 h a bird (under 0.2); 3.16 h a year (under 10) | **Yes** |
| D1 | Lamb year 11.09 h > chicken year 3.16 h | **Yes** |
| D2 | 10.29 h < 11.09 h | **Yes** |
| C1 | Sum rule S = 0.000 | **Yes** |

**In plain words:** one whole lamb a year is about 11 h, or 0.4% of the household's 2,760 h. That is below the public guess of 1% (27.6 h) by a factor of 2.5. The guess is reachable, not typical: it takes about two lambs a year, or the high end of the labour ranges. One chicken a week is about 3 h, 0.1%.

## 4. What this does not show

1. **That any hour figure is right.** Every range is from memory of published numbers, not re-read tonight. The request asked for a cited source. **No source was opened.** Sources to check, all **unverified**: USDA NASS *Sheep and Goats* annual report (lambs per ewe); university extension sheep enterprise budgets (labour per ewe-year); the National Chicken Council broiler key-facts page (bird weight, feed); BLS OEWS for poultry processing, NAICS 311615 (plant workers). A reviewer should replace the declared ranges with read ones.
2. **That "shared" is the right set of steps.** The request puts slaughter on the shared path. Fleece is usually shorn from the live sheep, so it does not pass slaughter. The shorn-live variant (10.29 h) shows it changes little for a lamb, because the ewe's year dominates. For a chicken, feathers do pass the plant's kill, scald and pluck, so that holds.
3. **The indirect multiplier.** 1.0 – 2.5 is declared. The BLS employment-requirements matrix on disk (`data/erm_full/`) has only "Animal production" as one sector, covering cattle, poultry and sheep together, so it could not check a lamb. It was not used.
4. **Labour only.** The energy and material dimensions of the debit vector were not swept. Combustion CO₂ rides the fuel and is never a joint cost (§3.2b).
5. **A household that buys a whole lamb and all its fleece is rare.** The request stipulates it. US lamb eating is about a pound a head a year (from memory, unverified), so one whole lamb is already a lamb-heavy household. The sweep's two-lamb draws are not typical.
6. **Same-flock identity is assumed.** `S` needs both holdings to point at the same flock-year (`q = 1`). A fleece bought from a different flock than the meat gives `S = 0`.
7. **The denominator is 2,760 h**, today's median US reading. A different household debit moves the percentage and not the hours.

## 5. Command and seed

```
python 06-simulation/whole-animal-consolidation/whole_animal.py --test
python 06-simulation/whole-animal-consolidation/whole_animal.py
```

Seed **20261020**, 20,000 triangular draws per species over the ranges at the top of the file. Output in [`RUN.txt`](RUN.txt).
