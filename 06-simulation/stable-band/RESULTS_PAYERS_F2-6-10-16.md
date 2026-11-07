# Stable band at the every-payer peer ratios, at `F` = 2, 6, 10, 16 — results

Author request 2026-11-07, on folding the 2026-10-30 run (`RESULTS_PAYERS.md`): *"Yes to re-running. But also report at F = 2, 6, 10, and 16."* Code: `stable_band_payers.py --floors 2 6 10 16`. Raw output: `PAYERS_F2-6-10-16_RUN.txt`. Same population (60,000 people, seed 7, wants 66,407 real units), same age seeds (11–15), same 100 yearly periods, same capacity formula 778,955 ÷ (h ÷ 100).

**Terms.** `F` is the floor, the hours a day a network credits for staying alive. ρ ("rho") is the debit tolerance in the gate `D ≤ ρ·C` (`P` = 0 throughout). The **upper edge** ρ\* is the highest ρ at which what the gate admits still fits inside capacity; above it the gate stops rationing. **Break-even** is `h ÷ (365·F)`, the ρ at which a year of floor credit balances a year of median consumption `h`. **ρ_sat** is the ρ above which at least 99.9% of wants are admitted. The **lower edge** is `E ÷ (365·F)` for an essentials basket `E`. "none" means admitted ≤ capacity at every ρ from 0.005 to 4.0, the swept range.

## 1. One change to the code, declared

`F` = 16 is above the 14 h/day the population was built for. `build_people` clips paid work at 24 − 14 = 10 h/day, so at `F` = 16 a person working 9 or 10 hours would claim 25 or 26 h. The kernel's IC-7 check refused the run. **The fix is the rule Foundations §2.3 already states: credit per day is `F` + work, capped at 24 by IC-7.** `stable_band.credit_rate` now applies `min(F + work, 24)`, and the cumulative sensitivity arm (`past_work=True`, not used here) caps past work at 24 − `F`. **This changes nothing at any floor up to 14 h/day**, because no one there reaches 24. `F` = 2 and `F` = 10 below reproduce the 2026-10-30 figures to the third decimal, which is the check that it did not.

At `F` = 16, 9,824 of 60,000 people (16.4%) work more than 8 h and are capped at 24 h credited.

## 2. Upper edge ρ\* (capacity edge)

| Peer | h/yr | Capacity, share of wants | `F` | Break-even | One-day ρ\* | Cumulative ρ\* (mean, sd) |
|---|--:|--:|--:|--:|--:|--:|
| **US (control)** | 1,380 | 85.0% | 2 | 1.890 | 1.017 | 1.017 (0.000) |
| | | | **6** | 0.630 | **0.485** | **0.485 (0.000)** |
| | | | 10 | 0.378 | 0.330 | 0.330 (0.000) |
| | | | **16** | 0.236 | **0.228** | **0.228 (0.000)** |
| **Germany, Japan** (0.836) | 1,153.7 | 101.7% | 2 | 1.580 | none | none |
| | | | 6 | 0.527 | none | none |
| | | | 10 | 0.316 | none | none |
| | | | 16 | 0.198 | none | none |
| **France** (0.858) | 1,184.0 | 99.1% | 2 | 1.622 | 2.365 | 1.653 (0.0007) |
| | | | **6** | 0.541 | **0.943** | **0.562 (0.0006)** |
| | | | 10 | 0.324 | 0.612 | 0.342 (0.0005) |
| | | | **16** | 0.203 | **0.411** | **0.217 (0.0004)** |
| **Sweden** (0.873) | 1,204.7 | 97.4% | 2 | 1.650 | 1.823 | 1.656 (0.0000) |
| | | | **6** | 0.550 | **0.755** | **0.558 (0.0001)** |
| | | | 10 | 0.330 | 0.496 | 0.337 (0.0001) |
| | | | **16** | 0.206 | **0.336** | **0.212 (0.0001)** |

**The two new floors sit where the old three said they would.** At the US method the edge falls as the floor rises, and the one-day and cumulative edges agree: 1.017 / 0.485 / 0.330 / 0.228 at `F` = 2 / 6 / 10 / 16, every one below break-even. For Germany and Japan capacity (67,519) is above total wants (66,407) before anyone is simulated, so there is no edge at any floor, including 16. For France and Sweden the one-day edge is well above break-even and the cumulative edge sits just above it: France 0.562 against 0.541 at `F` = 6 (3.9% above), 0.217 against 0.203 at `F` = 16 (7.0% above); Sweden 0.558 against 0.550 (1.5%) and 0.212 against 0.206 (2.9%).

**In plain words, at `F` = 6.** A floor-only person at the US method may carry 0.485 × 6 × 365 = **1,062 h** of debit a year at the edge, against the 1,380 h a median US lifestyle takes. At the French method, cumulative, the same person may carry 0.562 × 6 × 365 = **1,231 h** against the 1,184 h that lifestyle takes by the French method: 47 h a year of room. At the German or Japanese method the gate never has to ration, because the envelope delivers more than people want.

## 3. ρ_sat, where the gate stops holding anyone back

| Peer | `F` = 2 | `F` = 6 | `F` = 10 | `F` = 16 |
|---|--:|--:|--:|--:|
| US (control), one-day | ≥ 4.0 (censored) | 1.608 | 1.023 | 0.683 |
| US, cumulative | 3.962 | 1.499 | 0.952 | 0.633 |
| Germany, Japan, one-day | 3.501 | 1.344 | 0.855 | 0.571 |
| Germany, Japan, cumulative | 3.312 | 1.253 | 0.796 | 0.529 |
| France, one-day | 3.593 | 1.380 | 0.878 | 0.586 |
| France, cumulative | 3.399 | 1.286 | 0.817 | 0.543 |
| Sweden, one-day | 3.655 | 1.404 | 0.893 | 0.596 |
| Sweden, cumulative | 3.459 | 1.308 | 0.832 | 0.552 |

Where an upper edge exists, ρ_sat is far above it. Between the two, the gate holds some people below their wants while total admitted is already above capacity, so capacity is rationed by the gate in that range. Above ρ_sat everyone is admitted and shortage is settled at distribution (Foundations §5.5.3).

## 4. Is the band open?

**Assumption A, declared and not measured:** each essentials basket scales by the same ratio as the median lifestyle. Narrow 516–655 h and broad 826–965 h become 431–548 / 691–807 h at 0.836, 443–562 / 709–828 h at 0.858, 450–572 / 721–842 h at 0.873. Nobody has measured a peer's essentials basket. The lower edge below uses the **top** of each basket range, which is the hard case.

| Peer | `F` | Narrow lower edge | Broad lower edge | Upper edge (one-day / cumulative) | Narrow | Broad |
|---|--:|--:|--:|--:|---|---|
| US | 2 | 0.897 | 1.322 | 1.017 / 1.017 | open | **closed** |
| US | 6 | 0.299 | 0.441 | 0.485 / 0.485 | open | open |
| US | 10 | 0.179 | 0.264 | 0.330 / 0.330 | open | open |
| US | 16 | 0.112 | 0.165 | 0.228 / 0.228 | open | open |
| Germany, Japan | 2, 6, 10, 16 | 0.750 / 0.250 / 0.150 / 0.094 | 1.105 / 0.368 / 0.221 / 0.138 | none | open, no upper edge | open, no upper edge |
| France | 2 | 0.770 | 1.134 | 2.365 / 1.653 | open | open |
| France | 6 | 0.257 | 0.378 | 0.943 / 0.562 | open | open |
| France | 10 | 0.154 | 0.227 | 0.612 / 0.342 | open | open |
| France | 16 | 0.096 | 0.142 | 0.411 / 0.217 | open | open |
| Sweden | 2 | 0.783 | 1.154 | 1.823 / 1.656 | open | open |
| Sweden | 6 | 0.261 | 0.385 | 0.755 / 0.558 | open | open |
| Sweden | 10 | 0.157 | 0.231 | 0.496 / 0.337 | open | open |
| Sweden | 16 | 0.098 | 0.144 | 0.336 / 0.212 | open | open |

**In plain words: the only closed cell in the whole table is the US method at `F` = 2 on the broad basket, exactly as on 2026-10-30.** At `F` = 6 the US band is open on both baskets with 0.485 − 0.441 = **0.044** of ρ to spare on the broad one. At `F` = 16 it is open with 0.228 − 0.165 = **0.063** to spare. At the three peer methods every cell is open at every floor asked.

## 5. What this run does not show

- **Germany and Japan's "none" is entailed by the input.** Capacity 67,519 is above wants 66,407 before a single person is simulated. A different capacity figure moves it; the people do not.
- **The peer essentials baskets are scaled, not measured** (assumption A).
- **`P` = 0.** The pledge term halves a publishable upper edge (Foundations §5.5.3); it is not in this run.
- **The `F` = 16 cap touches 16.4% of the population** and only there. Whether a network would credit a 16-hour floor at all is a network choice (§5.5.1); the run says what the gate does if one did.
- **The level inherits the weighting model and an illustrative capacity figure.** The ordering across floors and methods is the result; the digits are dated readings.

## Reproduce

```
python 06-simulation/stable-band/stable_band_payers.py --test
python 06-simulation/stable-band/stable_band_payers.py --floors 2 6 10 16     # about 3 minutes
```
