# Subsector candidates — every split considered, with its magnitude

> **Version:** 0.1 · **Date:** 2026-08-23 · **Status:** ✅ **Settled by the author, 2026-08-23.** The rulings are in §0 below; the candidate reasoning is kept underneath as the record of what was considered and why.
> **Parent:** [`STATERA_PLAN_v0.2.md`](STATERA_PLAN_v0.2.md) §5a.

**The rule these are judged against (author, 2026-08-23):**

> **Test 1 — does it move the debit vector *enough to be worth carrying*?** *"If it makes no significant difference, it is not worth making a subsector for."* **A split can be true and still not earn its place.**
> **Test 2 — is it measurable?** The physical-trace test.
> **Stopping rule:** split until the next split is smaller than the model's own uncertainty.
> **And record the rejects, with their magnitude** — or the next person re-proposes them and nobody can tell a tested idea from an untested one.

---

## 0. Settled — the four rulings and the final list

| # | Question | Ruling |
|---|---|---|
| 1 | Whose consumption? | **Everything that materially flowed to the person**, not only what the household paid for. |
| 2 | Healthcare | **Both splits** — by care type *and* by kind. |
| 3 | Housing | **New build vs existing · floor area per person · heating fuel and climate.** Detached-vs-multi-family dropped. |
| 4 | Budget | **~25 categories.** |

### The move that makes ~25 possible: a split that *multiplies* is a modifier, not a category

**Some splits scale a figure. Others name a different thing.** Floor area does not create a new kind of housing — it makes the same housing bigger. **Treat it as a multiplier and it costs one number instead of a whole row of the matrix.**

| Modifier | Multiplies | Cost |
|---|---|---|
| Floor area per person | Housing creation-cost and energy | 1 number per cohort |
| Organic share | Food labour up, food pollution down | 1 |
| Food-away share | Food labour | 1 |
| Air-freight share | Food energy | 1 |
| Powertrain blend | Transport energy and pollution | 1 |

> **This is how all four rulings fit inside the budget.** Every split the author asked for is present. **Five of them are carried as multipliers rather than as categories**, which is what keeps the matrix at 27 rows instead of several hundred.

### The 27 categories

| Chain | Share* | Categories |
|---|---|---|
| **Healthcare** | 32.9% | **8** — preventive×{practitioner, drugs} · acute×{procedures, practitioner} · chronic×{drugs, practitioner} · end-of-life×{procedures, practitioner} |
| **Housing** | 24.0% | **6** — {new build, existing} × {cold, temperate, hot} |
| **Transport** | 12.4% | **5** — car-combustion · car-electric · transit · air · walk-cycle |
| **Food** | 9.4% | **5** — beef · other meat · dairy · plant staples · seafood |
| **Entertainment** | 3.4% | **3** — pets and hobbies · fees and admissions · devices and supplies |
| | **82.1%** | **27 categories + 5 modifiers** |

*\*Shares of the restructured basket — see §0a.*

**Numbers to source: 27 × 8 consumer types × 8 age bands = 1,728.** Within the moderate budget.

### 0a. The restructured basket

**Substituting real healthcare changes every share.**

| Category | Old (household spend) | **New (everything that flowed)** |
|---|---|---|
| Healthcare | 8.0% | **32.9%** |
| Housing | 32.9% | **24.0%** |
| Transport | 17.0% | **12.4%** |
| Food | 12.9% | **9.4%** |
| Entertainment | 4.7% | **3.4%** |
| *Struck by A1 — pensions, insurance, cash given away* | *15.5%* | ***11.3%*** |
| Everything else | 9.0% | 6.5% |
| **Total** | $77,280 | **$106,021** |

> **Coverage improves, not worsens.** Five chains now cover **82.1% of total** and **92.6% of what a person materially consumes**, up from 89%. **Healthcare grew into the gap.**

### 0b. Three other things "everything that flowed" would seem to pull in — and where each actually goes

**The ruling logically reaches beyond healthcare. Three cases, and two of them resolve without a new category.**

| Case | Where it goes |
|---|---|
| **Public education** | **Not a consumption category at all.** §4.5: training is **front-loaded credited work** — the student is credited for their time and pledgers underwrite the cost. **It appears on the credit side, not as something a household consumes.** Nothing to substitute |
| **Roads and transport infrastructure** | **Inside the transport chain.** §5.4: *"infrastructure users carry proportional debit by usage."* A usage-proportional term on the transport categories, not a sixth chain |
| **⬜ Policing, defence, public administration** | **Genuinely open. Parked.** §5.4 says civil servants are credited directly and there is nothing to collect — but *who carries the debit of a collectively-consumed service* is not settled anywhere. **Do not invent an answer to fit a simulator.** Registered as an open question |

---

## 🔴 The finding that outranks every split below

**We are about to build cohorts on the wrong basket.**

The Consumer Expenditure Survey records **what a household paid for out of its own pocket.** Aequitas accounts **everything that materially flowed to a person**, because under **A1** money is invisible and under **A7** everyone is accounted. **Those are not the same number, and the gap is enormous.**

**Healthcare is the clearest case.** CE 2023 puts household healthcare at **$6,159**. But US National Health Expenditure runs about **$4.9 trillion a year** — roughly **$14,500 per person**, or about **$34,800 per consumer unit** at 2.4 people. *(NHE figures approximate and to be verified.)*

> **The CE basket sees about one-sixth of the healthcare actually consumed.** The rest was paid by employers and government. **Under Aequitas the care still happened, the hours were still worked, and the debit still lands on whoever received it.**

**Substituting the real figure restructures the whole basket:**

| Category | CE basket | With real healthcare substituted |
|---|---|---|
| Housing | 32.9% | **24.0%** |
| Healthcare | 8.0% | **32.9%** |
| Total spend | $77,280 | **$106,021** |

**And healthcare is not the only case.** Public schooling, roads, policing, defence, public transit — **all consumed, none in the CE basket.**

> **⚠️ But the existing median-lifestyle work may already be right.** [`MEDIAN_LIFESTYLE_RESULT.md`](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md) was built on **PCE**, not CE — and PCE *does* include employer-paid health insurance and government benefits in kind. **So the 1,380 h/yr anchor probably covers this, and only the new cohort work has the gap.**
>
> **This must be settled before step 5, or every cohort profile is wrong in the same direction.** It is question 1 below.

---

## Food — 12.9% of the basket

| Split | What moves, and by how much | Verdict |
|---|---|---|
| **Meat / dairy / vegetables / grains / seafood** | All three dimensions, **one to two orders of magnitude per kilogram.** | ✅ **Take.** The largest split available anywhere |
| **Beef / pork / poultry, inside meat** | Beef runs roughly **5–10× pork or poultry** per kilogram. **Bigger than most splits we are keeping.** | ✅ **Take** |
| **Organic vs conventional** | Pollution down, **labour up**, land up. The direction of the collapsed figure depends on the weighting model. | ✅ **Take** — it is the OP-10 crossover demonstration |
| **Food at home vs food away** | CE: **$6,053 vs $3,933.** Restaurant meals carry far more labour and energy per calorie, and that labour is credited to real cooks. | ✅ **Take** — moves `labour_h` hard |
| **Air-freighted vs not** | Air freight ~**50× sea freight** per tonne-km, concentrated in a few goods. | ✅ **Take** |
| ~~Local (<100 mi) vs non-local~~ | Freight is typically **under ~10%** of a food's footprint; food is 12.9% of the basket. **Moves ~1% of the total.** | ❌ **Dropped 2026-08-23.** True, below the noise |
| Food waste (~30–40% of supply) | Real, and §3.6 says the last holder consumed it. | ⬜ **Not a subsector — a loss factor** applied across food |

---

## Housing — 32.9% of the basket, or 24% if healthcare is substituted

| Split | What moves | Verdict |
|---|---|---|
| **New build vs existing stock** | **Probably the single biggest determinant of housing debit under Aequitas.** A new build carries full creation-cost; a 100-year-old house leaves the new holder a tiny holding-time share (§4.5). **This is "used goods enter cheap," and nobody has ever simulated it.** | ✅ **Recommend take** |
| **Floor area per person** | Multiplies creation-cost *and* energy directly. **US ~700 sq ft per person, Europe ~400, much of the world far less. The biggest single lever between locales.** | ✅ **Recommend take** |
| **Heating fuel and climate zone** | Energy per sq ft varies enormously (EIA RECS). **And it is the case that tests §3.2b's real-time-dispatch rule** — electricity follows the consumer's *contracted supply mix*, not the grid average. | ✅ **Recommend take** |
| **Detached vs multi-family** | Shared walls cut energy per unit sharply, and creation-cost per person falls. **But much of it is already captured by floor area per person.** | ⬜ **Ask** — take only if it moves separately |
| **Own vs rent** | **I believe this dissolves.** §3.2 puts property debit on the *holder*, and a renter holds the dwelling — they occupy it. **Rent does not exist under Aequitas (§5.1).** Same physical building, same energy, same holding time. | ⬜ **Recommend: no split — but record it as tested-and-dissolved.** That is a publishable finding in itself |
| **Remediation debt by site type** (§3.7) | Greenfield vs brownfield vs already-urban. | ❌ **Not v0.2.** §3.7 flags the "natural state baseline" as an *open theory question*. Modelling it would be inventing an answer |

---

## Transport — 17.0%

| Split | What moves | Verdict |
|---|---|---|
| **Mode: car / transit / walk-cycle / air** | Enormous per-passenger-km differences. **Air is the outlier by far.** | ✅ **Recommend take** |
| **Purchase vs operation** | **Not really a subsector — it is the §4.5 capital/consumption boundary.** The car is capital, holding-time split; the fuel is consumption. **Mandatory anyway under IC-4 fate closure.** | ✅ **Take as a required field, not a category** |
| **Powertrain: combustion / hybrid / electric** | Moves `energy_mj` and pollution hard — **and it is the cleanest test of the real-time-dispatch rule**, where an electric car's emissions follow the contracted supply mix. | ✅ **Recommend take** |
| **Distance travelled per person per year** | Suburban vs urban, a 2–3× spread. | ⬜ **A cohort attribute, not a subsector** |

---

## Healthcare — 8.0%, or 32.9% if the real figure is substituted

| Split | What moves | Verdict |
|---|---|---|
| **Insurance premium vs care delivered** | See the red finding above. **The premium is a financial instrument and vanishes under A1; the care does not.** | 🔴 **Question 1** |
| **Preventive / acute / chronic / end-of-life** | Very different intensities **and very different age profiles.** **This is what makes the ageing cohort model earn its place** — healthcare is where age actually bites. | ⬜ **Ask** |
| **Drugs / procedures / practitioner time** | Different dimensions entirely. **And drug development is a textbook Front-Loading Rule case (§4.5)** — R&D front-loaded and pledged, never amortised onto the patient. | ⬜ **Ask** — high theory value |

---

## Entertainment — 4.7%

| Split | What moves | Verdict |
|---|---|---|
| **Pets, toys, hobbies ($1,057) vs fees and admissions ($951) vs supplies and equipment ($653)** | **These behave under completely different rules.** A cinema ticket is delivery-only (§4.5). **A pet is ongoing material consumption — closer to food than to media.** | ✅ **Take. Effectively forced** |
| **Physical media and devices vs streamed** | Devices are capital (§4.5); streaming is bandwidth and power, real-time dispatched, so the consumer's under §3.2b. | ⬜ **Small share, clean test.** Ask |

---

## Cross-cutting — required everywhere, not a subsector

| Field | Why it is mandatory |
|---|---|
| **Durable vs consumable** | **IC-4 fate closure** and §4.5's capital/consumption boundary. *"Does the thing survive the process?"* — a drill bit is capital, the oil it burned is consumption. **This is what closes the consumption-launderer**, so it cannot be optional |

---

## Running total, if every ✅ and every ⬜ is taken

| Chain | Subsectors |
|---|---|
| Food | 5 types × 2 organic × 2 home/away × 2 air-freight = **up to 40**, realistically ~12 after pruning empties |
| Housing | 2 build-age × 3 size bands × 3 climate = **~18** |
| Transport | 4 modes × 3 powertrains = **~12**, most combinations empty |
| Healthcare | 4 care types × 3 kinds = **~12** |
| Entertainment | **~4** |
| | **≈ 58 categories** |

> **⚠️ And each one needs a want per cohort per age band.** At 8 consumer types × 8 age bands × 58 categories that is **3,712 numbers to source.** **This is the real constraint on the design, and it is question 4.**
