# Dark production, and what `Z` should be a count of — plan v0.1

> **Written 2026-08-29, after the author's four corrections.**
> **Findings 1, 2 and the legitimate-non-recording cases are FOLDED — Foundations v0.34.**
> **Finding 3, the `Z` denominator, is NOT folded. It waits on the simulation** — steps 5 to 7 below.
> **Read against:** `Aequitas_Foundations_v0.34.md` §2.5, §3.2, §4.2, §4.4, §4.5, §4.7 · `Aequitas_Conformance_v0.10.md` rows 4a, 14a, 14b.

---

## What this is about

**Foundations §4.4 estimates what a network cannot see.** Its rule:

> **estimate = (N − Y) ÷ Z**, where **N** is an independently known total for an area, **Y** is what measured producers recorded, and **Z** is the number of producers still unmeasured.

**Three things are wrong with the section, and one of them is only a word.** They are separable and are listed in the order they should be fixed.

---

## Finding 1 — §4.4 says "charged" of a party it charges nothing

**§4.4, condition 2 on `Z`:**

<!-- struck-ok: quoting the withdrawn wording in order to show what was withdrawn; folded into Foundations v0.34 -->
> *"Under-counting raises each unmeasured producer's estimated share, which is the direction that prompts them to come forward and prove otherwise. **The error that liquidates itself is the safe one, because nobody complains about being charged too little.**"*

**§4.4, eleven paragraphs later:**

> *"The leftover is computed, published, and left unassigned. **It is debit on no account.**"*

**And §4.1:** *"A non-participant can neither draw on their estimated position nor be charged for it."*

**Nobody outside the network is charged anything.** The estimate is a statement about material flows in the world. The word "charged" in condition 2 is loose, it contradicts two other passages, and it is what makes a careful reader conclude that dark producers carry a bill.

### What the incentive actually is, since it is not a charge

**The estimate does nothing to a producer while they stay out. It becomes their opening position on the day they join.** §4.4's reconstruction paragraph says so: *"When an unmeasured producer joins, their share is traced back from records that already exist and assigned to them."*

**So the pull is not a debt. It is that the estimate errs against you and you can replace it with a record.** §4.4's condition 2 in the life-reconstruction subsection already states this correctly — *"an estimate errs against the estimated party, on both sides, so supplying evidence always pays."*

> **The fix is one sentence, not a mechanism.** Condition 2 should say the estimate is unflattering and is replaced by a record on joining. It should not say charged.

---

## Finding 2 — "unmeasured" is doing two jobs

**§4.4 says:**

> *"**"Unmeasured" means outside the network, not low-technology inside it.** Subscribing carries a transparency requirement, so a good moving through the accounting carries records of where it came from."*

**Two other passages contradict it.**

| Where | What it says |
|---|---|
| **§4.5** | *"The accounting covers what is claimed and attested. **Everything else is life.**"* |
| **§3.2, subsistence corollary** | Growing food and eating it yourself: *"the farming labour credits you, the food carries that debit, consuming it returns the debit to you. **Net zero on labour**."* |
| **§4.2** | A network credits no kind of work for which it has published no evidence rule. **So a member's unrecorded activity may have no rule to be recorded under at all.** |

**The word is carrying two different meanings.**

| Term the document needs | What it means |
|---|---|
| **unsubscribed** | The *person* holds no account with this network |
| **unrecorded** | The *output* is not in this network's books |

**A member with a vegetable garden is unrecorded and not unsubscribed.** The drone survey that produces `N` sees the garden. The books do not. §4.4 currently has no way to say that, because it treats the two words as one.

### Kinds of legitimately unrecorded production

**None of these is evasion, and none needs a rule to stop it.**

- **Subsistence.** A farmer feeds themselves and their farmworkers from part of the harvest. §3.2 already nets this to zero on labour.
- **Gifts.** §2.4 rule 3: handing a thing to somebody outside the system is not an event.
- **Barter.** No hand-off is recorded on this network, so the network never sees it.
- **Reserved for the money market.** **During adoption this is the common case.** A producer keeps most of their output for the ordinary currency economy and puts a slice on a trust network. §4.8's money-boundary section already permits both directions.
- **Listed on two networks.** The same output is offered on A and on B so it has a better chance of finding a buyer. **§4.0 fact 2 makes this ordinary:** a transaction lands on exactly one network and the seller picks which.

> **The discipline already exists and needs no addition: if you do not enter produce into the network, you cannot sell it on the network.** Withholding output is withholding it from your own buyers. That is the whole cost, and it is enough.

**So the rule to state is about respecting autonomy, not about closing a hole.** A network does not need to capture everything, and §4.5 already says attempting to would be *"futile and grotesque."*

---

## Finding 3 — `Z` is a headcount where a measurement is available

**This is the substantive one.**

### The project's own test says a headcount is the wrong choice here

**§2.5:**

> *"Did the thing being divided leave a physical trace? **Where it did — measure it. Where it did not — declare a convention and say so.**"*

**Land area leaves a trace. A count of producers does not.** A headcount is a convention: it says every unmeasured producer is one unit of unmeasuredness, regardless of whether they farm a window box or 900 hectares.

> **So §4.4 currently applies a convention in a place its own §2.5 requires a measurement. That is the defect.**

### The change

> **Where the leftover was produced by a resource that left a physical trace, `Z` is a measure of that resource, not a count of people. Where no such trace exists, `Z` falls back to a headcount, and the network says which it used.**

**For agricultural output the denominator is unrecorded hectares.** For a fishery it is unrecorded vessel-days. For a quarry it is unrecorded extraction area. **Where the trace does not exist — most services, most intellectual work — the headcount stands, declared as a convention under §2.5.**

**Rename the terms while doing it**, because single letters are what let `Z` mean two things:

| Now | Proposed | What it is |
|---|---|---|
| `N` | **`outside_total`** | The area's output, measured outside the ledger |
| `Y` | **`member_recorded`** | What this network's members recorded |
| `Z` | **`unrecorded_extent`** | The measured extent of what produced the leftover — hectares, vessel-days — or a headcount where nothing was traced |
| `(N−Y) ÷ Z` | **`per_unit_extent`** | What each unit of unrecorded extent is estimated to have produced |

### Worked, with the numbers

**A region of 1,000 hectares grows 1,000 t. `outside_total` = 1,000 t, from a drone survey that also measures area.**

| Who | Land | Makes | On this network's books |
|---|---|---|---|
| 5 members, fully recorded | 400 ha | 400 t | **400 t** |
| **P, who routes half through another network** | **100 ha** | **100 t** | **50 t** |
| 4 unsubscribed producers | 500 ha | 500 t | nothing |

#### Under the headcount rule, as written today

P is a member, so P leaves the unmeasured pool entirely.

| | |
|---|---|
| `member_recorded` | 400 + 50 = **450 t** |
| `Z`, a count of unmeasured producers | **4** |
| leftover | 1,000 − 450 = **550 t** |
| **estimate per unmeasured producer** | 550 ÷ 4 = **137.5 t** |
| **What they actually produced** | **125 t each** |

**The estimate is 10% high, and the excess is P's unrecorded half.** Nobody is charged for it — but it is filed against the wrong party, and it never resolves. **Onboard all four and the arithmetic breaks visibly:**

| | |
|---|---|
| `member_recorded` | 450 + 500 = **950 t** |
| `Z` | **0** |
| leftover | **50 t**, divided by nobody |

**Coverage reads 95% and cannot reach 100%, no matter who else joins.**

#### Under the extent rule

**P declares that 50 of their 100 hectares produced the output recorded here.**

| | |
|---|---|
| `member_recorded` | **450 t** |
| Recorded extent | 400 + **50** = **450 ha** |
| **`unrecorded_extent`** | 1,000 − 450 = **550 ha** |
| leftover | **550 t** |
| **`per_unit_extent`** | 550 ÷ 550 = **1.0 t per hectare** |

**Check it against the truth.** The four unsubscribed producers hold 500 ha and made 500 t — **1.0 t/ha, exact.** P's undeclared 50 ha made 50 t — **1.0 t/ha, exact.**

> **The estimate is now right for both, and it is right for the same reason: it is estimating over the thing that physically produced the leftover.**

**Onboard all four and it closes properly.** Recorded extent 950 ha, unrecorded extent 50 ha — **P's own undeclared half, correctly identified as the only unrecorded land left.** Coverage is 95% and the document can say exactly whose 5% it is.

### This answers the open simulation request from its own books

**The open request `sr-20260829-producer-side-version-of-the-cross-network-s` asks whether an event-granular supersession rule — keeping a registered producer in the unmeasured pool for exactly the unseen slice — is computable from one network's books alone.**

> **Yes. The producer's own land declaration is on this network's books, and the survey that produces `outside_total` measures the same hectares.** Nothing from another network is needed.

**And the two-network reading was never forbidden anyway** — see Finding 4.

---

## Who games this

**Per the standing advisory duty, the exploit is named before the mechanism is endorsed.**

**The lever is the declared extent, and it runs one way.** P wants their on-network goods to read light, so the temptation is to **under-declare**: claim 25 ha produced the 50 t, and each tonne carries half the land-area-years of an honest neighbour's.

**Three things already constrain it, and none is new.**

| The constraint | Where it already lives |
|---|---|
| **The same instrument that measures `outside_total` measures the hectares.** A declaration and the survey are made on separate paths, so a false declaration dangles | **§4.3** — *"What defeats a balanced lie is physicality"*; conformance **14b** |
| **Over-declaring is punished by the arithmetic with no rule needed.** Claim 100 ha for 50 t and your goods carry 2.0 ha-y/t against a neighbour's 1.0 — **twice as dear, and a buyer takes on that debit** | **§2.4**, **A5** |
| **A false declaration is a false record, not a permitted choice** | **§4.7** — fraud is a finding of fact and routes to existing recourse |

> **Both directions are constrained, and that is precisely what a headcount cannot do.** There is no instrument that catches a miscounted person, because a person is not a quantity the survey reads.

**The remaining honest incentive is the one the author identified: declare the split that matches the resources that produced each side.** A producer who put half their land into the A-side output declares half, and their figures — labour-hours per hectare, irrigation, runoff — reconcile with everyone else's. **A producer who declares otherwise has to explain why their inputs do not match their output, against records the network already holds.**

### The three screens

| Screen | Result |
|---|---|
| **Universality** | **Passes.** One rule with two branches, and the branches are §2.5's existing two branches. No profession, region or class is carved out |
| **Decentralization** | **Passes, and improves.** Anyone holding the same survey recomputes the same estimate. A headcount requires trusting somebody's register of who exists |
| **Fecundity** | **Passes.** Better land data improves the estimate, and §4.4 already makes measuring a region credited work |
| **Does it need a Paul Glover?** | **No.** The survey is already required to produce `outside_total`. No new instrument, no new maintainer |
| **Does it need an objective function?** | **No.** It is a measurement, not an allocation rule. No capture surface is created |

---

## Finding 4 — a shorthand in the task queue contradicts §4.2

**The documents are right. The shorthand is wrong, and the outreach agent has published under it.**

| Source | What it says |
|---|---|
| **Foundations §4.2** | *"**This is comparison, never conversion.** Nothing is exchanged between models, and **each party re-reads the same physical log** through its own weighting."* |
| **Conformance 4a** | *"A second network **re-computes the claim itself, from the same physical record**, through its own model."* |
| **`NEXT.md:479`** | *"AUTHOR RULING — **never add or compare** two networks' figures"* |
| **`NEXT.md:399`** | *"conformance 4a (**never convert or compare** two networks' figures)"* |

**What 4a forbids is setting two collapsed credit figures side by side as one quantity** — the 12 hours and the 18 hours of §4.1. **What it requires is reading the other party's physical records.** The shorthand lost the distinction and inverted the operative word.

**This is live, not archival.** The agent's memory record `rul-20260827-no-cross-network-arithmetic` carries the wrong shorthand, and `NEXT.md` records that the agent argued from it in public.

**And §4.7 makes the point sharper still:** *"Pledges, production quantities, hand-offs and the figures things carry are **public**."* **A multi-homing producer's output on another network is public market data.** There was never an access problem to solve.

---

## The plan, in order

**Each step is done when its own test passes. Nothing later depends on a step being skipped.**

| # | Step | Done when |
|---|---|---|
| **1** | **Correct the shorthand.** `NEXT.md:399` and `:479`, and the agent's memory record. The rule is *never convert; comparison is required* | The agent's brief and memory say *comparison, never conversion*, matching §4.2 verbatim |
| **2** | **Fix the one word.** §4.4 condition 2 stops saying "charged". It says the estimate is unflattering and is replaced by a record on joining | No sentence in §4.4 implies a non-participant carries a debt |
| **3** | **Split the two meanings.** §4.4 defines **unsubscribed** and **unrecorded** separately, and the line *"unmeasured means outside the network"* is struck | A member's vegetable garden can be described in the document's own vocabulary |
| **4** | **State that voluntary non-recording is legitimate**, with the five cases above, and that the discipline is already sufficient: unrecorded produce cannot be sold on the network | §4.4 and §4.5 agree. The autonomy point is stated once, in §4.4 |
| **5** | **Change the denominator.** `Z` becomes a measured extent where a physical trace exists and a declared headcount where it does not, under §2.5's existing test. Carry the worked example above | Conformance gains a row; §4.4 carries one worked example with digits; the §2.5 link is explicit |
| **6** | **Rename the three variables** to `outside_total`, `member_recorded`, `unrecorded_extent` | §4.4, Conformance row 14a's worked example, `01-wiki/estimation-engine.md`, `01-wiki/statistical-coverage.md`, and the simulation roadmap all agree |
| **7** | **Run the open simulation** with the extent rule as the candidate answer, not as an open question | The error under the headcount rule and under the extent rule are both measured, across multi-homing shares from 1% to 50% |

**Files this touches:** `Aequitas_Foundations_v0.34.md` §4.4 · `Aequitas_Conformance_v0.10.md` rows 14a and 14b and its worked example at line 262 · `01-wiki/estimation-engine.md` · `01-wiki/statistical-coverage.md` · `Aequitas_Simulation_Roadmap_v0.2.md` line 41 · `NEXT.md` · the agent's memory. **The distilled Foundations is regenerated, never edited.**

---

## What is not proposed, and why

**No new mechanism.** Every part of this is an existing rule applied where it already should have been. §2.5 supplies the trace test, §4.3 supplies the physical check on the declaration, §2.4 and A5 supply the over-declaration penalty, §4.7 supplies the public market data.

**No rule against multi-homing.** It is ordinary commerce, it is prudent, and §4.0 fact 2 already makes it the seller's choice. **What changes is that the books can now describe it.**

**No change to who carries the leftover.** It is still debit on no account, per the 2026-08-22 ruling. **What changes is that the leftover is attributed to the right extent, so it converges instead of stalling at a number nobody can explain.**
