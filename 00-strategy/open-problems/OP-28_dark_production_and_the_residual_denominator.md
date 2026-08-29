# OP-28 — Dark production, and what the residual denominator counts

> **Status:** Open. **A candidate repair exists and has not been measured.** Two of the three findings that produced this paper were folded on the day it was written; the third is what remains open and is the whole of the problem.
> **The shape of the problem:** Foundations §4.4 divides an unattributed leftover by `Z`, **a count of unmeasured producers**. §2.5 requires a measurement wherever the thing being divided left a physical trace. **Land left a trace. A headcount did not.** So the section applies a convention where its own rule demands a measurement.
> **Raised by:** the author, 2026-08-29, while correcting an assistant's reading of the multi-homing-producer case.
> **PARTLY FOLDED 2026-08-29** → Foundations **v0.34** (§4.4 — the *charged* wording, the unsubscribed/unrecorded split, and the five legitimate cases of unrecorded output) · Overview **v0.21** (§ on estimating the unmeasured) · `01-wiki/estimation-engine.md`. **The denominator change is NOT folded.**
> **Tracks:** Foundations v0.34 §2.5, §3.2, §4.2, §4.4, §4.5, §4.7 · Conformance v0.10 rows 4a, 14a, 14b
> **Touches:** OP-24 (understatement drift) · OP-22 (audit disclosure) · OP-26 (coverage gap)
> **Owed:** simulation request `sr-20260829-producer-side-version-of-the-cross-network-s`, unrun.

---

## 0. The case that raised it

**One producer, two trust networks.** `P` grows 100 tonnes in one region and one season, and routes 50 t through Network A and 50 t through Network B. **Both networks verified `P` as a real human and gave them one account, which is what §4.1 requires.** Neither network is being deceived, and §4.0 already makes this ordinary: a transaction lands on exactly one network, and the seller picks which.

**The question is what Network A's books say about the 50 t it cannot see.**

---

## 1. What §4.4 does today

> **estimate = (N − Y) ÷ Z**
>
> **N** — the independently known total for the area, from agricultural statistics, trade data, or a satellite survey.
> **Y** — what the measured producers actually recorded.
> **Z** — **the number of producers still unmeasured.**

**`P` holds an account, so `P` is not in `Z`.** But `P`'s other 50 t is inside `N` and absent from `Y`, so it sits in the leftover. **The leftover is then divided among producers who did not make it.**

### 1.1 Worked, with the numbers

**A region of 1,000 hectares grows 1,000 t. `N` = 1,000 t, from a survey that measures area as well as yield.**

| Who | Land | Makes | On Network A's books |
|---|---|---|---|
| 5 members, fully recorded | 400 ha | 400 t | **400 t** |
| **`P`, routing half through Network B** | **100 ha** | **100 t** | **50 t** |
| 4 unsubscribed producers | 500 ha | 500 t | nothing |

**Network A computes:**

| | |
|---|---|
| `Y` | 400 + 50 = **450 t** |
| `Z` | **4** |
| leftover `N − Y` | **550 t** |
| **estimate per unmeasured producer** | 550 ÷ 4 = **137.5 t** |
| **what they each actually produced** | **125 t** |

**The estimate is 10% high, and the excess is `P`'s unrecorded half.**

### 1.2 The part that does not resolve

**§4.4 says the estimate is continuous:** as an area becomes measured, `Y` rises, `Z` falls, and the estimate shrinks to what remains. **Test that here.** All four unsubscribed producers join and record their real 125 t each:

| | |
|---|---|
| `Y` | 450 + 500 = **950 t** |
| `Z` | **0** |
| leftover | **50 t**, and no denominator |

**Coverage reads 95% and cannot reach 100%, however many people join.** The 50 t is `P`'s other half, and no arrangement of a headcount can say so.

> **The 2026-08-22 ruling still holds and is not in question: a leftover is debit on no account.** Nothing here charges anybody. **What fails is the description.** A figure that reads as unsubscribed production is in fact a subscriber's unrecorded output, and the books have no way to distinguish them.

---

## 2. Why a headcount is the wrong denominator, by this project's own test

**§2.5:**

> *"Did the thing being divided leave a physical trace? **Where it did — measure it. Where it did not — declare a convention and say so.**"*

**Land area leaves a trace, and the same survey that produces `N` reads it.** A count of producers does not: it treats a window box and 900 hectares as one unit of unmeasuredness each.

> **So `Z` is a convention standing in a place where a measurement was available. §2.5 says that is the error to avoid, and names it as the difference between an honest choice and one disguised as a fact.**

---

## 3. The candidate repair

> **Where the leftover was produced by a resource that left a physical trace, the denominator is a measure of that resource. Where no trace exists, it stays a headcount, and the network publishes which it used.**

| Output | The denominator |
|---|---|
| Agriculture | unrecorded **hectares** |
| A fishery | unrecorded **vessel-days** |
| A quarry | unrecorded **extraction area** |
| Most services, most intellectual work | **a headcount, declared as a convention under §2.5** |

**And rename the three variables**, because single letters are what allowed one of them to mean two things:

| Now | Proposed | What it is |
|---|---|---|
| `N` | **`outside_total`** | The area's output, measured outside the ledger |
| `Y` | **`member_recorded`** | What this network's members recorded |
| `Z` | **`unrecorded_extent`** | The measured extent that produced the leftover, or a headcount where nothing was traced |
| `(N−Y) ÷ Z` | **`per_unit_extent`** | What each unit of unrecorded extent is estimated to have produced |

### 3.1 The same case, under the repair

**`P` declares that 50 of their 100 hectares produced the output recorded on Network A.**

| | |
|---|---|
| `member_recorded` | **450 t** |
| recorded extent | 400 + **50** = **450 ha** |
| **`unrecorded_extent`** | 1,000 − 450 = **550 ha** |
| leftover | **550 t** |
| **`per_unit_extent`** | 550 ÷ 550 = **1.0 t per hectare** |

**Checked against the truth:** the four unsubscribed producers hold 500 ha and made 500 t — **1.0 t/ha exactly.** `P`'s undeclared 50 ha made 50 t — **1.0 t/ha exactly.**

**And it closes.** Onboard all four and recorded extent reaches 950 ha, leaving **`P`'s own undeclared 50 ha** as the only unrecorded land. **Coverage is 95% and the books can name whose 5% it is.**

> **⚠️ These digits are constructed to show the shape of the argument. Nothing here has been simulated, and the figures must not be quoted as results.**

### 3.2 It is computable from one network's books alone

**The open simulation request asks whether an event-granular supersession rule — keeping a registered producer in the unmeasured pool for exactly the slice this network cannot see — needs anything from another network.**

**It does not.** `P`'s land declaration sits on Network A's books, and the survey producing `outside_total` measures the same hectares.

**And reading another network's records was never forbidden in the first place.** §4.2: *"This is comparison, never conversion. Nothing is exchanged between models, and each party re-reads the same physical log through its own weighting."* Conformance 4a forbids **converting a figure between weighting models** and treating two networks' figures as one quantity. **It requires re-computation from the shared physical record.** §4.7 adds that production quantities are public anyway.

---

## 4. Who games it

**The lever is the declared extent, and the temptation runs one way: under-declare, so your goods read light.** Claim 25 ha produced 50 t and each tonne carries half the land-area-years of an honest neighbour's.

**Three existing rules constrain it, and none is new.**

| The constraint | Where it lives |
|---|---|
| **The declaration and the survey are made on separate paths, so a false declaration dangles** | §4.3 — *"what defeats a balanced lie is physicality"*; conformance **14b** |
| **Over-declaring is punished by arithmetic with no rule needed.** Claim 100 ha for 50 t and your goods carry 2.0 ha-y/t against a neighbour's 1.0 — twice as dear, and the buyer takes on that debit | §2.4, **A5** |
| **A false declaration is a false record, not a permitted choice** | §4.7 — fraud is a finding of fact and routes to existing recourse |

> **Both directions are constrained. A headcount can constrain neither, because no instrument reads a person as a quantity.**

**The honest incentive is then to declare the split that matches the resources that produced each side.** A producer who put half their land into the Network A output declares half, and their labour-hours per hectare, irrigation and runoff reconcile with everyone else's.

### 4.1 The three criteria

| Criterion | Verdict |
|---|---|
| **Universality** | **Passes.** One rule, two branches, and the branches are §2.5's existing two. No profession, region or class is carved out |
| **Decentralization** | **Passes, and improves on the headcount.** Anyone holding the same survey recomputes the same estimate. A headcount requires trusting somebody's register of who exists |
| **Fecundity** | **Passes.** Better land data improves the estimate, and §4.4 already makes measuring a region credited work |
| **Does it need a Paul Glover?** | **No.** The survey is already required to produce `outside_total`. No new instrument, no new maintainer |
| **Does it need an objective function?** | **No.** It is a measurement, not an allocation rule, so it opens no capture surface |

### 4.2 Prior art inside the project

**`01-wiki/estimation-engine.md` already carries a capacity-bounded method** — `Z ≥ (N − Y) ÷ capacity`, where capacity is the most one producer could physically make, *"bounded by hours in a day, by land, or by throughput."* **It is filed as a candidate, not the method.** It reaches for the same physical quantity from the other end, and the two should be compared rather than merged sight-unseen.

---

## 5. What was folded on the day this was raised

**Three findings from the same reading were wording corrections, not mechanism changes, and went into Foundations v0.34 and Overview v0.21 immediately.**

| # | What was wrong | What it says now |
|---|---|---|
<!-- struck-ok: the next two rows quote both withdrawn wordings in order to record what was struck and when -->
| **1** | §4.4's condition 2 ended *"nobody complains about being charged too little"* — **said of a party §4.4 and §4.1 both say is charged nothing** | The estimate is unflattering and **sits there until the producer joins and replaces it with a record.** The pull is not a debt |
| **2** | *"Unmeasured means outside the network, not low-technology inside it"* — **so a subscriber's unrecorded output could not be described** | **Unsubscribed** is a person outside the network. **Unrecorded** is output not in the books. **They are independent, and most subscribers will have unrecorded output** |
| **3** | Nothing said that choosing not to record output is legitimate | Five cases named: **subsistence · gifts · barter · output held back for the money market · the same crop offered to two networks to find a buyer.** No rule added — **produce you do not enter into the network cannot be sold on the network** |

**Both struck wordings are registered in `../STRUCK_PHRASES.md` and are checked against every live document from now on.**

> **Finding 2 is why this paper exists.** Once *unsubscribed* and *unrecorded* are separate states, **the denominator has to answer which one it is counting** — and a headcount can only count the first.

---

## 6. What would close this

**One measurement and one ruling.**

1. **Run `sr-20260829-producer-side-version-of-the-cross-network-s`.** Measure the error in each network's estimate and in its published coverage as the share of multi-homing producers rises from 1% to 50%, under the headcount rule and under the extent rule.
2. **Compare the extent rule against the capacity method already in the wiki** (§4.2 above).
3. **Author ruling.** Either the extent rule folds into §4.4 with measured digits replacing §3.1's constructed ones, or it is refused and this paper records why.

**Until then the honest public statement is:** *the project has identified the gap, has a candidate repair, and has not measured it.*
