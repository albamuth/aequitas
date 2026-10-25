# False passage: how large is the gain, and can any published check see it?

> **Run date:** 2026-10-24 · **Foundations read:** v0.61 (lines 1–1949 read; §4.5 onward not read, see "What this does not show") · **Code:** `false_passage.py`

## 1. The question

> How large is the gain from a FALSE PASSAGE claim, and can any check we publish detect one? Sweep a producer overstating how finely they read their chain. Report the understatement in published debit-hours per kilogram, and whether the totals reconciliation of 3.4a, conformance row 7 closure, or the coarse-reading ceiling can separate a true fine reading from a false one.
> (request `sr-20260909-how-large-is-the-gain-from-a-false-passage-c`; from @coywolf, c48233)

## 2. Outcomes declared before the first run

| # | Kind | Statement | Result |
|---|---|---|---|
| L1 | Level | A one-step-early lie on the steer understates the worst product by 0.5–1.0 MJ/kg and by 20–50% of its true figure | **Held.** 0.750 MJ/kg, 38% |
| L2 | Level | Over all lie depths the worst understatement exceeds 70% of the true figure | **Held.** 90% (75% if only shared-step lies count) |
| C1 | Change | Totals reconciliation flags 0% of lies on a shared step | **Held.** 0/6 |
| C2 | Change | Coarse-reading ceiling flags 0% of lies | **Held.** 0/12 steer, 0/13 refinery |
| L3a | Level | A lie spanning an independent meter, with mass share ≥ 3σ, is caught ≥ 95% | **Held at σ ≤ 2%** (99.7–100%). **Failed at σ = 5%**: 91.3% (n = 2 lies) |
| L3b | Level | Catch rate with no meter spanned equals the honest false-alarm rate, which is < 1% | **Half failed.** Equal, yes. But with a meter on all 6 boundaries the honest false-alarm rate is **1.4–1.7%**, not < 1%. One meter: 0.2–0.3% |
| C3 | Change | Producer's own meter catches no more than 2× the false-alarm rate | **Held.** 0.3–1.7% against 0.2–1.7% |

## 3. The numbers

Steer: 600 kg animal, 7 steps, 20 h labour, 500 MJ, 17 kg pollutant. **Digits are the illustrative ones in Foundations 3.4a.** Product masses sum to 380 kg. Refinery: real DOE 2015 step energies, declared passage table. Native units (TBtu per kg of yield basis), so only the absolute figure beside the share is meaningful within the file.

### 3.1 Gain: understatement per kg (steer, fine reading)

| Product | True exit step → claimed | True MJ/kg | Understated by MJ/kg | By h/kg (labour + 0.05 h/kg pollutant) | Share | Another product also passes the removed steps? |
|---|---|--:|--:|--:|--:|---|
| hide | 2 → 1 | 2.000 | 0.750 | 0.076 | 38% (59% on the h basis) | yes |
| organs | 3 → 2 | 2.000 | 0.667 | 0.037 | 33% | yes |
| organs | 3 → 1 | 2.000 | 1.167 | 0.088 | 58% | yes |
| hooves_head | 4 → 3 | 4.667 | 0.667 | 0.035 | 14% | yes |
| hooves_head | 4 → 2 | 4.667 | 2.000 | 0.108 | 43% | yes |
| hooves_head | 4 → 1 | 4.667 | 3.000 | 0.210 | 64% | yes |
| packaged_beef | 7 → 6 | 2.000 | 0.120 | 0.017 | 6% | no, packaging is the beef's alone |
| packaged_beef | 7 → 1 | 2.000 | 1.800 | 0.075 | 90% | no |

(The MJ share column is the energy share; the h-basis share in `RUN.txt` column "share" uses the labour-plus-pollutant weights with energy at 0.002 h/MJ, which is **not sourced**. Full 12-row table in `RUN.txt`.)

- **One step early:** worst 0.750 MJ/kg (hide), 0.12–0.75 MJ/kg across products, 6–38%.
- **Any depth, shared steps only:** worst 3.000 MJ/kg (hooves_head, claimed to leave at step 1), 64% of its true 4.667.
- **Refinery, 13 lies** (drop one really used shared step): understatement 5% to 36% of the product's figure. Largest: jet, drop hydrotreating, 36% (0.307 of 0.848).

### 3.2 Where the omitted cost goes

| Lie type | What happens to the omitted cost |
|---|---|
| **Shared step** (6 of 12 steer lies, all 13 refinery lies) | Another product still carries the step, so the union over parcels still equals the chain total. **Nobody picks the cost up. The product's buyer carries less and the producer's books are unchanged.** |
| **Orphaning step** (6 of 12 steer lies; all on the beef) | No product is claimed to pass the step. The union falls short of the chain total by 30–360 MJ. **The totals reconciliation fires 6/6**, and the cost stays with the producer (3.2b). **No gain to the producer.** |

### 3.3 Can a published check separate true from false?

| Check | Shared-step lies caught | Why |
|---|--:|---|
| Totals reconciliation (3.4a): union of claimed passages = metered chain total | **0 / 6 steer, 0 / 13 refinery** | The step is still passed by another product, so the union is unchanged |
| Coarse-reading ceiling (coarse ≥ fine) | **0 / 12 steer, 0 / 13 refinery** | It bounds a figure from above. A lie lowers the figure |
| Both, plus the union and every coarse figure: records compared between the true world and the false world | **6 / 6 pairs identical** | There is nothing in these records for the lie to contradict |
| Conformance row 7, balance at the plant's existing level of detail | **0** (no boundary meter is in the model's baseline) | Row 7 balances mass and energy "at one level of detail". A lie inside one block of that detail cannot unbalance it |
| Row 7 **at a finer cut, with an independent mass meter** on a boundary the lie spans | **99.7–100%** at σ = 0.5–2%; 91.3% at σ = 5% (n = 2) | The hide's 40 kg is missing from the claimed flow past the boundary and present on the meter |
| Same meter owned by the producer | **0.3–1.7%**, equal to its false-alarm rate | The reading supports the claim |

### 3.4 Detection by meter placement and noise (z = 3; 4,000 trials per false-alarm cell, 1,000 per lie)

| σ | Meters | Owner | Catch, lie spans a meter, share ≥ 3σ | Catch, lie spans no meter | Honest false alarm |
|--:|---|---|--:|--:|--:|
| 0.5% | one, b = 3 | third party | 100.0% (n=3) | 0.3% (n=3) | 0.30% |
| 0.5% | all 6 | third party | 100.0% (n=6) | — | 1.52% |
| 0.5% | all 6 | producer | 1.6% (n=6) | — | 1.70% |
| 1% | one, b = 3 | third party | 100.0% (n=3) | 0.2% | 0.18% |
| 1% | all 6 | third party | 100.0% (n=6) | — | 1.43% |
| 2% | all 6 | third party | 99.9% (n=6) | — | 1.43% |
| 5% | all 6 | third party | 91.3% (n=2) | — | 1.68% |
| 5% | one, b = 3 | third party | no lie qualifies (share < 15%) | 0.2% | 0.25% |

**Reading:** detection is on or off by whether an independent meter sits on a boundary the lie crosses. With no such meter, a false reading and a true one give the same records.

## 4. What this does not show

1. **Passage truth is only checked here through mass.** The meter model assumes the diverted product physically sits at a boundary on the way. A cheaper lie that moves a product past a step while leaving no mass at any boundary (a step too short to hold anything, or a boundary nobody can reach) is not modelled. The mass argument is a model choice and is the strongest assumption in 3.3.
2. **"Independent" is assumed, not shown.** The third-party meter is given a reading that comes from true mass plus noise. Foundations 4.3 says trust moves from the ledger to the instrument. Who owns a meter at a plant boundary, and what stops the producer owning it, is exactly the open question coywolf asked. This run shows **what a third-party instrument would catch if one existed. It does not show that one can exist.**
3. **Digits are illustrative.** The steer is the 3.4a illustration. The refinery passage table is declared, not measured. Real plants have unrecorded waste and recycle streams, so mass share at a boundary is less clean than in this model. Energy-to-hours weights are not sourced; the 0.002 h/MJ weight is a placeholder and only the energy column is free of it.
4. **One lie at a time, one producer, no repeated game.** I did not model a liar who also falsifies step energies, bills, or the mass flow sheet consistently, nor several lies at once, nor the buyer's incentive. Collusion with the hide's buyer is the case where the gain is realised, and it is not simulated.
5. **Gain size is not the producer's gain.** On a shared-step lie the saving goes to the product's holder. This run does not measure who that is, or what it is worth to them, because Aequitas has no price. The "gain" is the reduction in a published figure.
6. **Foundations §4.5 to the end (about 40% of the document) was not read tonight.** Nothing in 3.4a or conformance row 7 pointed there, but this run cannot rule out a premise in those sections.
7. **Noise model:** Gaussian, independent between meters, z = 3 fixed. Real meter drift is correlated and non-Gaussian.

## 5. Command and seed

```
python 06-simulation/false-passage/false_passage.py
```

Seed 20261024 (default). Tests only: `python 06-simulation/false-passage/false_passage.py --test` (7 tests, all pass). Raw output: `06-simulation/false-passage/RUN.txt`. Runs in about 10 seconds, writes under 100 KB.
