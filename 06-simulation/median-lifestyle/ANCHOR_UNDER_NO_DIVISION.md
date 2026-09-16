# Does the 1,380 h/yr anchor move now that a joint process's cost is not divided?

> **Version:** 0.1
> **Date:** 2026-09-16

> **Answered 2026-09-05.** Request `sr-20260904-recompute-the-1-380-h-yr-median-lifestyle-an`.
> **Foundations §3.4a names this as unmeasured in its own text**, and says the direction is not known in advance.
> **Method:** re-ran `track1_embodied_hours.py` and audited every Track for an allocation step.

---

## The answer

> **Neither figure moves. The anchor is 1,380 h/yr and ρ\* is ≈ 1.2, unchanged.**
>
> **The reason is not that the rule does not matter. It is that this measurement never had the resolution the rule operates at.**

**And there is a second half that runs against us, in §4.**

---

## 1. What the anchor is actually computed from

**Terms.** The **ERM** (Employment Requirements Matrix) is a BLS table giving total jobs — direct plus indirect — per \$1M of final demand, by industry. **PCE** (Personal Consumption Expenditures) is the BEA's measured record of what Americans actually bought. A **Leontief walk** multiplies the two to get the labour embodied in a basket.

The computation is one line:

> **hours = colsum(ERM) · PCE**

**at 176-industry resolution**, for 2023.

**Re-run on 2026-09-05, unchanged from the original:**

| | |
|---|--:|
| PCE total (check) | **\$18.82T** |
| PCE-embodied jobs, direct + indirect | **113.9 M** |
| Mean embodied hours per capita per year | **612 h** |
| Mean embodied hours per adult per year | **791 h** |
| **Track 1 headline — median adult, domestic only** | **633 h/yr** |

**5 of 5 self-tests pass.** Track 1 is the domestic floor; Tracks 2, 3 and 4 add durables, imported labour and own-pollution remediation to reach the published **1,380 h/yr**.

## 2. Why the rule change cannot reach it

**§3.4a governs how *one process's* cost is shared among *its several outputs*** — the steer that yields beef and hide, the refinery that yields petrol and asphalt.

**An ERM cell is an industry, and an industry's output is already an aggregate.** There is no steer in the matrix and no hide. There is "Animal slaughtering and processing", one row, one column, one labour coefficient.

> **The co-product rule operates at process resolution. The ERM is measured at industry resolution. The withdrawn division was never performed anywhere in this computation, so removing it changes nothing.**

**Audited, not assumed.** Every allocation-shaped operation in the eight Track scripts:

| What it does | Is it a co-product split? |
|---|---|
| **Trade and transport margin re-allocation** (`track1_by_category.py`, `track1_embodied_hours.py`) — BEA reports retail, wholesale and transport margins as three separate columns, and the bridge reassigns them to the goods they were margins on | **No.** It moves *one commodity's* dollars onto the goods they accompanied. No process is divided among its outputs |
| **Holding-time split** (`track2_housing.py`) — a dwelling's build-hours re-annualised across the years it is held | **No**, and **that rule was not withdrawn.** It is §4.5, and it is a measurement: holding time is a physical trace |
| **Split by region of origin** (`track3_exiobase.py`, `track3_imports.py`) | **No.** Geography, not co-products |

**`track1_labour.py` says it in its own header:** *"no allocation (the ERM measures the whole supply chain) and no invented margins."*

## 3. So ρ\* does not move either

`stable_band.py` takes the anchor as a **constant input** — `MEDIAN_LIFESTYLE_H_YR = 1380.0`, line 92. **Nothing else in that sim reads a co-product rule.**

> **ρ\* ≈ 1.2 is a function of the anchor and the capacity figure. The anchor did not move, so ρ\* did not.**

**In plain words: Foundations §3.4a can drop the sentence saying these two figures are owed a recomputation. It has been done, and they stand.**

---

## 4. ⚠️ The half that runs against us, and it was not in the question

**The anchor is invariant to *our* allocation rule. It is not free of allocation.**

**BEA does not observe an industry directly.** It builds the input-output tables from **make** and **use** tables, and industries produce **secondary products** — a sawmill that also sells wood chips, a dairy that also sells hides. **To get a commodity-by-commodity table, BEA redefines those secondary products out of the producing industry**, under a stated technology assumption.

> **That is a co-product allocation convention. It is upstream of us, it is somebody else's, and this project has never named it.**

**Three things follow, and none of them is comfortable.**

1. **The anchor inherits an allocation assumption after all.** It survives our rule change because our rule never touched it — **not because it is convention-free.**
2. **We do not control it and cannot re-run it.** BEA's choice is fixed in the published matrices. **Under §3.3a's five properties, that makes it a cost constant with a method we did not audit and cannot re-derive.**
3. **The direction of any error is unmeasured.** The `06-simulation/method-spread/` result — **6.31× across 36 honest methods** on a refinery — was measured at *process* resolution. **Nobody has measured how far BEA's redefinition choice can move an industry-resolution figure**, and it is not safe to assume it is small because the aggregation is coarser.

**What this does not do.** It does not put a number on the anchor's uncertainty, and it does not say the anchor is wrong. **It says the anchor's uncertainty has a source nobody had written down.**

> **Not measured. The run that would measure it: how far a defensible change in the secondary-product redefinition assumption moves `colsum(ERM) · PCE`.** Until somebody does, **1,380 h/yr should be published as a dated reading with an unaudited upstream convention in it**, which is what §3.3a requirement 5 asks of every constant a network has not reviewed.

---

## 5. What this run does not show

- **It does not re-derive the anchor from process-level data.** It re-ran the same Leontief walk on the same 2023 matrices and audited the code path. **A process-resolution rebuild would be a different project.**
- **It does not test Tracks 2, 3 or 4 numerically.** Their code paths were audited for an allocation step; only Track 1 was re-executed.
- **It says nothing about whether 1,380 h/yr is right.** It says the co-product ruling of 2026-09-03 does not change it.
