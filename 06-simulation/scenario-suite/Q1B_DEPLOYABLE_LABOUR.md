# Q1b — Can the labour actually be staffed? (plain-language companion)

> Companion to [`q1b_deployable_labour.py`](q1b_deployable_labour.py). **Run 2026-08-27**, after an author ruling.
> **Question:** Q1 said an autarkic US has 2.28× the labour it needs. Is that true of hours anyone could actually work?
> **Answer: no. At US production efficiency the hours do not close, at any corner of a defensible band.**

## The one-line answer

**The old labour row could not fail, and the row that replaces it does fail. At US production efficiency, deployable hours reach at most 0.87 of what a median lifestyle commands — and that best case already assumes full-time hours for 85% of every working-age adult. At peer-country efficiency it clears.**

---

## Why this was re-run

`Q1_AUTARKY.md` published this row:

| Resource | Available/person | Footprint/person | Ratio | |
|---|---|---|---|---|
| Labour | 3,647 h/yr | 1,600 h/yr | **2.28** | room |

**On 2026-08-27 @alfred-pennyworth showed it cannot fail** (comment c23625 on 1f916.ai post #2466):

> *"One does not lay cable with sleepers. Credited hours are a convention in a ratio's clothes: credit ten hours a day to every living person and 3,647/1,600 cannot bind, however the world is staffed."*

**They are right, and here is the mechanism.** The numerator is **credited** hours. Credited hours include the **self-care floor `F`**, and `F` is a value the trust network sets by rule (Foundations §7.5.1). **So the pass condition is fixed the moment `F` is chosen, before a single worker is counted.**

**A check whose passing condition is set by the checker is not an instrument.** That is @amber's rule (c24446), written the same week, and it fired on this row within hours.

> **Author ruling, 2026-08-27: strike the credited-hours ratio, and run the strict version.** This is the strict version.

---

## What is computed instead

**Only hours a human could actually spend producing.** No self-care, no sleeping, no floor.

```
deployable h/capita  =  working_age_share  ×  participation  ×  hours_per_worker
```

Each of the three is swept across a defensible band, and **all 27 corners** are computed.

| Dial | Band | Where the band comes from |
|---|---|---|
| **Working-age share** | 0.60 – 0.68 | US 15–64 is ~65% and falling with ageing |
| **Participation** | 0.62 – 0.85 | US labour-force participation is ~62–63%; wartime peaks reached ~0.85 of the working-age population |
| **Hours per worker** | 1,600 – 2,080 | US average ~1,750 h/yr ([OECD](https://data.oecd.org/emp/hours-worked.htm)); 2,080 = 40 h × 52 weeks, a full year with no leave |

**That gives 595 to 1,202 deployable hours a year per head of total population.**

**Against what?** The labour a median US lifestyle commands: **1,380 h/yr**, measured in [`../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md`](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md). Q1's own anchor of 1,600 h/yr is run alongside it, because the two figures had never been reconciled.

---

## The result

| Case | Footprint | Ratio band | Ever reaches 1.0? |
|---|---|---|---|
| **US efficiency, measured footprint** | 1,380 h | **0.43 – 0.87** | ❌ **No** |
| **US efficiency, Q1's anchor** | 1,600 h | **0.37 – 0.75** | ❌ **No** |
| Peer efficiency, measured footprint | 897 h | 0.66 – 1.34 | ✅ Yes, in 33% of cases |
| Peer efficiency, Q1's anchor | 1,040 h | 0.57 – 1.16 | ✅ Yes |

**Peer efficiency is 65% of US labour per unit of standard**, from [`../median-lifestyle/Q6.md`](../median-lifestyle/Q6.md): Germany, Sweden, France, Japan and Spain deliver a comparable-or-better material standard, and longer lives, at 55–67% of US hours.

### Read the top row carefully

**The best US case is 0.87, and it is not a plausible world.** It takes a working-age share of 0.68 — higher than today and moving the wrong way — **participation of 0.85**, and **2,080 hours from every one of them**, which is a full-time year with no holiday, no sickness and no part-time work. **Even that is 13% short.**

**The withdrawn row said 2.28. The strict best case is 0.75 on the same footprint. The old row overstated by 3.0×, in the flattering direction.**

---

## This was already known inside the project, in a different file

**[`../median-lifestyle/Q6.md`](../median-lifestyle/Q6.md) reached the same conclusion and nobody read it against Q1.** Its own words:

> A US-efficiency median standard for all 8.1 B people needs **~10.4 trillion labour-h/yr** — ~60% more than the world's ~6.5 T — **i.e. impossible without a ~50–58 h workweek.** Re-run with an efficient production model, **Germany / Sweden / Japan** do it at ~830 h/person for 6.7 T, **≈ break-even.**

**Two of this project's own documents disagreed, and the one being quoted was the flattering one.**

---

## What this changes, and what it does not

**Changed.**

- **Foundations §3.5's callout.** *"Human hours are abundant"* is withdrawn. The claim is now that **the constraint is production efficiency**, with these numbers attached.
- **`Q1_AUTARKY.md`'s labour row** is struck and replaced by a pointer here.
- **`MEDIAN_LIFESTYLE_RESULT.md`'s *"labour never binds"*** is withdrawn — it rested on the same credited-hours comparison.

**Not changed, and this matters.**

> **Q1's headline stands untouched. An autarkic US is bound by the energy transition and critical minerals.**

**Energy sits at 0.19 of what is needed at the current build** — against land at 1.10 and water at 5.22. **Energy binds harder than labour does at every corner of this sweep, and it never depended on a labour figure.** Deployable labour joins the list of real constraints; it does not become the tightest one.

**And the project's positive claim is unharmed, because it was never the hours claim.** The efficient method is **cheaper in the ledger** (A4, A5), so the accounting rewards the efficiency the leaders already demonstrate. **What is no longer available is the shortcut that said hours were simply abundant.**

---

## Self-tests

```bash
python q1b_deployable_labour.py --test
```

**Five, all green.** The first is the one that matters:

| Test | What it proves |
|---|---|
| `test_row_can_fail` | **The row has both a passing and a failing state.** An impossible footprint fails everywhere; a trivial one passes everywhere. **This is what the withdrawn row did not have.** |
| `test_no_credited_hours_anywhere` | Max deployable is 1,202 h/yr — far below the ~3,650 h/yr self-care pool. **No floor credit leaked into the numerator.** |
| `test_us_efficiency_binds` | The US band never reaches 1.0. |
| `test_peer_efficiency_relieves` | The peer band does. |
| `test_direction_of_the_old_error` | The withdrawn row is the more flattering one, **by 3.0×.** |

---

## Honest limits

- **This is a feasibility envelope, not a forecast.** It answers *"is there a staffing configuration that works"*, never *"will this happen"*.
- **The peer-efficiency factor of 0.65 is a single number standing for a range of 55–67%** (Q6). The band would widen if it were swept too.
- **Hours are treated as fungible across occupations.** They are not. A surplus of one trade does not staff another, and this model cannot see that — **so the real position is no better than these figures and may be worse.**
- **Participation at 0.85 is a wartime figure.** It is included to show the claim fails even there, not because it is a target.
