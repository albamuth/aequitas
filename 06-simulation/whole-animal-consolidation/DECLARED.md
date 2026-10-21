# Whole-animal consolidation — outcomes declared before running

> **Date:** 2026-10-20
> **Request:** `sr-20261017-hours-on-the-shared-steps-of-raising-and-sla`

**Written before the first run.** One disclosure: while choosing the parameter ranges I did the central-case arithmetic by hand (lamb about 11 h, chicken about 0.06 h a bird). The code's `test_hand_values` fixes those numbers, so a code error would fail it. The *ranges* come from my memory of published figures and were not looked up (no network tonight).

## The quantity

`S = min(f_meat, f_fleece) × shared hours`, from the imported max rule. A household buying a whole animal has `f = 1` on both, so `S` = the shared hours of one animal. Reported per animal, in hours a year, and as a share of 2,760 h.

## Outcomes

| # | Kind | Statement | What a failure means |
|---|---|---|---|
| **L1** | **Level** | Lamb, one animal a year, central S lies in **5 – 20 h** (0.18% – 0.72% of 2,760 h) | Outside it, my range choices or the model are far from my own prior |
| **L2** | **Level, ceiling** | Over the draws, **fewer than 5%** of lamb households reach 27.6 h (1%) | If 5% or more reach it, the public guess of "passes 1%" is not a corner case |
| **L3** | **Level** | Chicken, central S per bird is **under 0.2 h** (12 min), and a bird a week gives **under 10 h** a year (0.36%) | Over that, a chicken household is material |
| **D1** | Direction | Per year, the lamb household's S exceeds the weekly-chicken household's S | If not, "bigger animal, bigger lever" is wrong at these hours |
| **D2** | Direction | Dropping the slaughter step from the shared steps (fleece shorn before slaughter) lowers lamb S | If not, slaughter is not on the shared path |
| **C1** | Control | Under the sum rule S = 0.000 h | The code is wrong |

**Excluded as evidence, kept as code self-tests.** *"S equals min(f) × shared hours"* and *"S halves when a holding halves"* follow from the algebra of `max`. No input could fail them in the world, so under brief §4b they test the code only.

**Not declared, on purpose.** I declare no outcome over whether the hour figures are *right*. They are declared ranges, and nothing in this run can check them.
