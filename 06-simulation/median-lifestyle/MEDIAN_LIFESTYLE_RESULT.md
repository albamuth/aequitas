# What a median US adult's lifestyle costs, in Aequitas credit (labour-hours)

**The bottom-up estimate, all four tracks (2022–23 data).** Supersedes the top-down `median_lifestyle.py`/`MEDIAN_LIFESTYLE.md` (kept only as a sanity bracket). Each track is a separate, tested script; this assembles them.

## Headline

> **A median US adult's yearly consumption embodies ≈ 1,350–1,400 hours of human labour.**

Against the **≈ 3,650 h/yr** every person earns just by being alive (self-care credit, ~10 h/day), **the median lifestyle commands only about ⅓ of one person's annual credit.** That is the disparity-proof anchor: the median sits *far* below the ceiling, and labour is abundant.

## The four tracks

| Track | What it counts | h / median adult / yr | Script |
|---|---|---|---|
| **1** | Domestic embodied labour in consumption (BLS ERM × PCE) | ~633 | [`track1_embodied_hours.py`](track1_embodied_hours.py) |
| **3** | Foreign labour in imports (EXIOBASE MRIO) | ~690 | [`track3_imports.py`](track3_imports.py) |
| **2** | Housing structure, annualised (§6.2b holding-time) | ~31–61 | [`track2_durables.py`](track2_durables.py) |
| **4** | Own-pollution remediation labour (nature→DAC) | ~1–32 | [`track4_pollution.py`](track4_pollution.py) |
| | **TOTAL** | **≈ 1,350–1,400** | |

*(Tracks 1+3 are computed jointly per-capita as 1,276 h and normalised to the median adult; EXIOBASE's domestic 671 h independently corroborates Track 1's ERM 633 h. Track 2 adds only housing structure — vehicles/appliances/furniture are already inside Tracks 1+3 as PCE, so re-annualising them would double-count. Track 4 is basis-dependent and small.)*

## What the exercise revealed (the parts worth keeping)

1. **Imports roughly double the labour bill.** Nearly half (47%) of the labour Americans consume is performed abroad, at far higher hours-per-dollar (low wages). Money hides this; cost-accounting surfaces it. **India alone embodies ~121 h/capita/yr in US consumption; China ~101 h.**

2. **Dollar bills and labour bills disagree — and that vindicates cost≠value.** Housing has the biggest CE dollar tab ($25k/yr) but modest labour (rent/finance are transfers, A1: no debit); **healthcare inverts it** — moderate dollars, the most embodied labour, because care is people. Under Aequitas (price ≡ labour+material), today's "expensive" categories collapse and honestly-costed care/food surface.

3. **Two datasets, two methods, one domestic answer.** ERM (payroll) → 612–633 h; EXIOBASE (all-labour) → 671 h. The domestic piece is solid.

4. **Own-pollution remediation is the cheap, reversible half.** ~1–32 h/yr. The expensive, near-*permanent* debit is the stock kind (Q3 microplastics, landfill) that no remediation retires — not this flow.

5. **Labour never binds.** The full ~1,380 h a median lifestyle commands is a third of one person's self-care credit alone. Consistent with Q1/Q5: the scarce factors are materials and energy, never human hours.

## Honest limits (all flagged in the track docs)

- **Two big single-number assumptions:** `1,800 h/job` and `median/mean 0.80`. Both refinable.
- **EXIOBASE foreign hours include informal/subsistence labour** → treat the 605-h foreign figure as upper-ish; direction (≈ doubling) is robust.
- **Track 4 carbon basis** (nature vs DAC) is the genuine §3.3 baseline choice, reported as a range (~14× swing).
- **⚠️ Axiom discrepancy found:** the method doc (Foundations v0.9-era) says exclude electricity; **v0.15 §3.2b real-time-dispatch includes it** (the consumer's emission). Track 4 follows the current axiom; **the method doc should be updated.**
- **Housing build-hours** (~3,500 on-site, ×2 for materials) is a Level-1 order-of-magnitude figure.

## Next

Feed ~1,380 h/median-adult as the calibration point into the **ρ-sweep sim** — where does the median sit inside the `[F, 24/F·F]` band as ρ varies, and does a pickable ρ keep committed debit ≈ productive capacity across growth/decline/disaster?
