<!-- tag: op26-declare-dont-allocate -->
# OP-26 — "Declare it, don't allocate it": stress test

> **Date:** 2026-08-23
> **Source:** @custos (qwen3.8-27b), comments c16467 and c16479 on post #1750, 1F916 board.
> **Tested against:** `Aequitas_Foundations_v0.33.md` §4.4, §4.4, §4.4, §3.3a, §4.7, A8.
> **Status:** Not adopted. One small reporting rule taken. One public correction owed.

> **⚠️ The event-log paper was retired on 2026-08-28.** References to `EventLog §…` below are historical and no longer resolve. **The arithmetic constraints IC-1 to IC-12 are now conformance rows in [`Aequitas_Conformance_v0.10.md`](../Aequitas_Conformance_v0.10.md) §2**, which carries a label map; everything else it held is in Foundations. The archived paper is `99-archive/Aequitas_EventLog_v0.10.md`.


---

## Verdict

**The answer already exists. It is Foundations §4.4, ruled on 2026-08-22.**

@custos reached it independently, from a running system, and did not know it was already written. That makes it a useful outside check, not a new answer.

Two things go wrong when you compare the two versions:

1. **One phrase cannot be taken.** @custos says a **party with closure authority carries** the declared line. Aequitas has no such party, and A8 forbids creating one.
2. **Two of their premises are already false in Aequitas.** They say the leftover tells you nothing about who was missing, and that staying outside costs the individual nothing. Both are answered in §4.4 and §4.4, and answered more strongly than their version.

**One piece is worth taking:** publish the coverage figure as a **dated series**, not a single number.

---

## 1. What @custos proposed

Three claims and one receipt.

| # | Claim |
|---|---|
| 1 | Do not allocate the coverage leftover. **Declare it.** |
| 2 | The **party with closure authority carries** it as a standing published line. |
| 3 | Publish it **with its growth**, so its size stays visible. |

**The receipt.** Their own board's treasury page carries **$2,172.29 across 42 transfers** as a declared line of money that arrived from an unknown source, charged to no citizen.

Their argument for it: charging it to nobody hides it; declaring it is the same allocation with the hiding removed.

---

## 2. What Aequitas already says

**Foundations §4.4, folded 2026-08-22:**

> The residual is computed, published, and left unassigned. It is not debit on any account. When a dark producer onboards, their share is back-traced from the records that already exist and assigned to them — the actual causer. Until they onboard, they cannot transact inside the system at all.

It is also in `NEXT.md`, in the **SETTLED — do not re-litigate** table.

### Side by side

| @custos says | Aequitas says | Match? |
|---|---|---|
| Do not allocate it | "not debit on any account" (§4.4) | ✅ Same |
| Declare it publicly | "computed, published" (§4.4) | ✅ Same |
| Publish it **with its growth** | Not stated anywhere | 🟡 **New. Small. Take it.** |
| A **closure authority carries** it | No authority exists (A8, §4.4) | ❌ **Cannot take** |
| It says nothing about **who** was missing | Back-trace names them at onboarding (§4.4, §4.4) | ❌ Aequitas is stronger |
| Staying outside **costs the individual nothing** | Cannot transact at all; the estimate on the dark worsens (§4.4, §4.4) | ❌ Aequitas is stronger |

---

## 3. The six tests

### Test 1 — Universality: **fails as written**

§4.4 lists the three ways a coverage gap can be seen, and gives the authority each one needs:

| Flow type | Closure witness | Authority required |
|---|---|---|
| account → account | The counterparty | **None** |
| account → commons | The reservoir stock | **None — an instrument** |
| fully disjoint chain | `(N − Y) / Z` | **None — an instrument and a tally** |

Every row says none. @custos's version adds a party that has to be appointed. That is an exception where the rule wanted none.

**Read the phrase loosely** — as "the trust network publishing its own coverage figure" — and it passes, because that is §4.4 word for word. So the phrase is either wrong or redundant. It is never new.

### Test 2 — Decentralization: **fails as written**

A8 says no organization may acquire authority over the core rules. A designated party that carries and publishes the leftover is exactly that. §4.4 needs nobody, because the figure is a subtraction anyone with the same instrument can repeat.

### Test 3 — Fecundity: **weaker than what exists**

| | What makes the gap close |
|---|---|
| **@custos** | The line grows in public. Being seen is the pressure. |
| **Aequitas** | Improving the estimate is **credited work** (§3.3). The instrumented producer harmed by cheap undocumented goods **funds the replication** (§3.3a). |

Shame has no maintainer. Credited work pays its own.

### Test 4 — Who games this? **A named publisher is a single point to lean on**

**Worked example, with digits.**

A region grows **100 tonnes** of a crop. The books account for **60 tonnes**. The leftover is **40 tonnes**.

*Under @custos's version:* one party publishes the number "40". Whoever holds that pen can publish **25** instead. Nobody is harmed by the smaller figure except the instrumented grower, and that grower now has to argue with an appointed office rather than re-run a published method. **This is OP-24 (understatement drift) concentrated into one desk.**

*Under §4.4:* the 40 tonnes divides across the producers still dark. `estimate = (N − Y) / Z`. As instrumented growers leave that pool, `Z` falls and each remaining dark producer's estimated share **rises**.

`06-simulation/residual-unravelling/residual_unravelling.py` measures it:

- Estimate on those still dark: **0.995 → 18.23**, rising every round.
- Pool ends at **0.1% dark**.
- Computed over the whole population instead — the rule §4.4 rejects — it stalls at **52.5% dark**, permanently.

### Test 5 — Does this need a Paul Glover? **Yes, as written**

"The party with closure authority" is a designated maintainer. In @custos's own example that party is a **treasury**. Aequitas has no treasury: §5.4 removes taxation, and §4.7 says funding is not a budget but the recognition of work as creditable. A mechanism that needs an appointed publisher has an expiry date, which is what test 5 exists to catch.

### Test 6 — Does this need an objective function? **No. Passes.**

Nothing here has to be maximised, and no allocation rule is being chosen. This test is clean.

### The physical-trace test

**`N − Y` leaves a trace, so measure it.** `N` is a physical total from outside the books (a satellite pass, a harvest total, a port manifest). `Y` is the sum of what the books recorded. The subtraction is a measurement, and Aequitas measures it.

**The `/ Z` is where the convention sits**, and §4.4 already declares it out loud, with a candidate method: `Z ≥ (N − Y) ÷ capacity`, where capacity is the most one actor could physically produce.

So the trace test was already applied correctly, in both directions, before this comment arrived.

---

## 4. The one piece worth taking

> **Publish the coverage figure as a dated series, not a snapshot.**

§4.4 says the figure is computed and published. conformance row 16's extent clause says a passing check must publish what it could detect. **Neither says track it over time.**

**Worked example.**

- Snapshot, as written today: *"These books cover 60% of this region's output."*
- Series, as proposed: *"Coverage was 41% in 2029, 55% in 2030, 60% in 2031."*

A counterparty re-computing under its own model (OP-14) discounts what it cannot verify. A trend tells it whether the network is getting better or worse. A single number does not.

**Cost to add: nothing.** A tally is already an event that credits the measurer (a measurement of a region is work, and is recorded like any other), so the dated series already sits in the log. This is a reporting rule, not a new mechanism. It adds no authority, no lever, and no new constant.

---

## 5. What the bot got wrong, and owes in public

The night agent posted *"who carries the leftover `N − Y`?"* as an **open** question, and listed three bad answers, naming **"nobody"** as one of them, on the grounds that it rewards staying outside.

**"Nobody" is the ruling.** §4.4, 2026-08-22.

**And it does not reward staying outside.** Two things bite a dark producer:

1. **They cannot transact inside the system at all** until they onboard (§4.4).
2. **The estimate on the dark pool worsens** as good producers instrument and leave it — measured at 0.995 → 18.23 (`residual_unravelling.py`).

**Cause:** the ruling is not in `07-outreach/AGENT_BRIEF.md` §6b, the settled list. Fixed on 2026-08-23.

---

## 6. @custos's second comment (c16479) — the three classes of omission

Worth recording, and mostly already answered.

| Class of omission | Their proposed witness | Aequitas |
|---|---|---|
| **Inside the record** — truncation, skipped rows | A second record made by a different path | ✅ **Already §4.4**, the closure-witness table. Same answer. |
| **Of the instrument itself** — a check that never ran | A promised out-of-band schedule | ⛔ **Out of scope, §2.6.** This is about running software, not about accounting for cost. |
| **Of declared health** — a check that quietly degrades | A liveness stream with a staleness budget | ⛔ **Out of scope, §2.6.** Same reason. |

**Their closing line is the useful one, and Aequitas already has the number.** They say every witness has a price, so "what kind of witness" is really "what will you pay to be told."

`06-simulation/residual-unravelling/residual_unravelling.py` measures that price: **once verification costs more than about 40% of a median unit's debit, the dark pool stops shrinking and stabilises at 96.4% dark.** That is Foundations §4.7, item (b), and it was written before this comment.

---

## 7. Bottom line

**Nothing changes in Foundations except one reporting sentence.**

| Item | Action |
|---|---|
| "Declare, don't allocate" | Already §4.4. No change. |
| "A closure authority carries it" | **Rejected.** Fails universality and decentralization (A8). |
| "Publish it with its growth" | **Take it.** One sentence in §4.4, one in the conformance list. |
| The three classes of omission | Class 1 is §4.4. Classes 2 and 3 are out of scope (§2.6). |
| "What will you pay to be told" | Already measured. §4.7 (b), ≈40%. |
| The bot's framing of the question | **Public correction owed.** §6b of the brief updated. |

**The outside check is the real value here.** An unrelated system running an open population reached the same rule from its own books. That is evidence §4.4 is right. It is not evidence the question was open.
