# The stable band with a pledge term — result

> **Run:** 2026-09-18 · `pledge_band.py` · 5 self-tests green · N = 60,000
> **Against:** [`RESULTS.md`](RESULTS.md), which computed the same band with **no pledges in it**.
> **Ruling it tests:** a pledge grants consumable room, so the gate is `D ≤ ρ·(C + P)` — author, 2026-09-18, written up in [`../../00-strategy/papers/Pledges.md`](../../00-strategy/papers/Pledges.md).

---

## The headline

> **`RESULTS.md` said the band never closes. With a pledge term, it closes.**

**Two swept cells shut**, both at the tightest floor and the largest essentials basket:

| Essentials | `F` | Pledge density `p` | Lower edge | Publishable upper edge |
|---|--:|--:|--:|--:|
| 70% of a median lifestyle | **1.0 h/day** | **0.75** | 2.647 | **2.286** |
| 70% of a median lifestyle | **1.0 h/day** | **1.00** | 2.647 | **2.000** |

**Everywhere else the band stays open**, at every density up to the one-for-one ceiling. **So the old headline survives as a near-miss rather than as a theorem**, and it now carries a condition it did not have.

---

## What was computed, and why it needs no kernel change

**Terms.** **`p`, the pledge density**, is the share of the population's lifetime pledge budget that has been committed to somebody. Backing is one hour pledged per hour earned (conformance row 9, IC-8), so `P_total ≤ C_total` and **`p` runs from 0 to 1.**

Write `P = p·C`. Then the gate is:

> **`D ≤ ρ·(C + P)` = `D ≤ ρ·(1 + p)·C`**

**So the effective tolerance is `ρ·(1 + p)`.** `stable_band.py` was run with no pledges, so **the ρ it swept is the effective tolerance.** This script reuses its measured upper edge and reports the ρ a network may actually **publish**.

**This is exact, not an approximation.** No kernel change was needed, and `06-simulation/statera/`'s own pledge path — which still encodes the withdrawn earmarked-grant rule — **is never exercised.**

---

## The asymmetry between the two edges, which is the substance

**The edges do not see `p` the same way, and treating them alike would flatter the result.**

| Edge | The question it asks | Which `p` belongs in it |
|---|---|---|
| **Upper** — does the ledger still ration? | **An aggregate question** about the whole population's demand against capacity | **The population's own `p`.** Publishable upper = `ρ*(F) ÷ (1 + p)` |
| **Lower** — can a person who only stays alive afford essentials? | **A question about one person**, and it must hold for somebody **nobody pledged to** | **Zero, always.** Their own `p` is 0 whatever the average is. The lower edge does not move |

> **Reading the lower edge at the population's `p` would make essentials look affordable because *other people* were given room.** That is the flattering direction, and `Aequitas_Foundations.md` §4.4 says errors of this shape are not caught by whoever made them.

---

## The publishable upper edge

**`ρ*(F) ÷ (1 + p)`. `p` = 0 reproduces `RESULTS.md` exactly; `p` = 1 halves every entry.**

| `F` (h/day) | p = 0 | p = 0.25 | p = 0.50 | p = 0.75 | p = 1.00 |
|---|--:|--:|--:|--:|--:|
| 2.0 | 3.70 | 2.96 | 2.47 | 2.11 | **1.85** |
| 6.0 | 1.75 | 1.40 | 1.17 | 1.00 | **0.87** |
| **10.0** | **1.20** | **0.96** | **0.80** | **0.69** | **0.60** |
| 14.0 | 0.90 | 0.72 | 0.60 | 0.51 | **0.45** |

### What it costs at the documented setting

**`ρ*(10) = 1.20`, and the documented setting is `ρ` = 1.2.**

> **Those are the same number. So `ρ` = 1.2 sits exactly *at* the publishable edge when `p` = 0, and above it for every `p` > 0.**

**Any pledging at all puts the documented setting out of band.** At `p` = 0.5 a network at `F` = 10 may publish **0.80**, and at the ceiling **0.60**.

**Every publishable value at `F` = 10 is below 1 once `p` > 0.25.** `ρ` below 1 stops being the stress case `Aequitas_Foundations.md` §5.5.7 treats it as — where a −30% capacity disaster tightens the clearing rate to about 0.68 — and becomes the ordinary setting.

---

## Self-tests

**Five, each able to fail.**

| | |
|---|---|
| `p` = 0 reproduces `stable_band.py`'s upper edge exactly | ✅ |
| `p` = 1 halves the publishable upper edge | ✅ |
| The publishable upper edge falls monotonically in `p` | ✅ |
| The lower edge ignores `p`, and still moves with `F` and `E` | ✅ |
| **The closure check fires when it should** — at an absurd `E`, lower 7.56 > upper 0.60 | ✅ |

**The last one matters most.** Without it, "the band never closes" would be decoration rather than a finding.

---

## What this does not show

| | |
|---|---|
| **`p` is swept, not measured** | Nobody knows what pledge density a real network would run at. **It is a behavioural quantity and no network exists** |
| **The upper edge is inherited** | Including `stable_band.py`'s own censoring. Rows whose `ρ*` ran off the top of the swept range are floors, not values (conformance row 13), and are **excluded here rather than reported** |
| **Uncommitted pledges are not in `p`** | A pledge to a fund grants no room until it names somebody. **The room that matters is committed room only** |
| **The anchor behind `E` is a reading** | 1,380 h/yr is one defensible figure, not a fact about the world. See `papers/Pledges.md` §15.3 |
| **Nothing here tests the two live attacks** | A pledge costing the pledger nothing material, and coercion. Those are `papers/Pledges.md` §7 |

---

*Run command: `python pledge_band.py` · tests only: `python pledge_band.py --test`*
