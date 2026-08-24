# Stress Test — Credit-Earner Authorization of Future Work

> **Date:** 2026-08-01
> **Mechanism proposed:** credit-earners register wants and authorize which future work is creditable — "like a bank approving a business loan." Four variants.
> **Proposed as:** a solution to **OP-16** (the onerousness gap).
> **Verdict:** **PASSES WITH CHANGES — but not as a solution to OP-16.** It solves OP-19 and most of OP-9. OP-16 stays open.
> **Amended same day** — see §0.5. Two author corrections invalidate one exploit and one recommendation, and improve the P2 result.

---

## 0.5 Amendment — author corrections

Three corrections were issued against the first pass. **All three are accepted**, and two of them break findings below.

### C1 — The three credit types are one substance

Production, service, and enrichment work all credit as **time**. Everyone earns at the same rate and therefore influences at the same rate. The categories describe **how feedback is given**, not what is earned.

**This kills exploit #2 (the producer plutocrat) and the §5 recommendation built on it.** The error was mine: I read "production credit" as credit proportional to material moved. A2 says the opposite — labour credits by *time*, and material enters as the product's **debit**, not as the worker's credit. A carer's hour and a steelworker's hour credit identically. **There is no throughput advantage, so there is no producer plutocracy and nothing to denominate away from.**

The remaining effect is second-order and much smaller: authorization tracks **human hours spent**, so a heavily automated sector accumulates little authorization despite huge output. Whether an automated food or energy sector losing influence over its own inputs is a defect or a feature is worth a look, but it is not plutocracy.

### C2 — The categories have no boundary, so no accounting rule may use them

An apprentice plumber's single hour is simultaneously **enrichment** (learning the trade), **service** (fixing a customer's pipes), and **production** (copper and fittings → working plumbing). The hour is not partitionable.

**Accepted, and it is a universality argument of exactly the right kind.** Partitioning that hour across three categories would require an allocation convention — which is **OP-17 all over again**, one level further in. Co-products, team credit, and now credit categories: *the same failure of division, for the third time.* That recurrence is itself evidence the §0 headline is the right diagnosis.

**🔴 But it has an axiom-level consequence the correction did not follow through, and it must be flagged.**

Foundations **§6.3 states that "Enrichment is not convertible to time or material."** Under C1 and C2 that sentence is **not implementable**: you cannot firewall a category that has no accounting boundary, and enrichment *work* is time, credited as time, therefore convertible by construction. **OP-8** — "exactly where Enrichment must be firewalled" — is asking for a boundary that C2 says cannot exist.

The correction does not break the theory; **it fixes it, and §6 is simply mis-titled.** The consistent statement is:

> **There is one credit: time. There are three feedback channels. Feedback is never credit.**

Enrichment *work* credits as time like everything else. Enrichment *feedback* — likes, ratings, sell-outs — is a **signal**, and it is non-convertible for the sound reason that **it was never credit in the first place**, not because a firewall is holding it back. That is stronger, more universal, and needs no enforcement mechanism.

**Actions:** retitle §6 from "The Three Credit Types" to feedback channels; rewrite §6.3's non-convertibility clause; **OP-8 dissolves in its current form** and is replaced by the much narrower question of whether signals can be *bought* with credit.

### C3 — P2 re-read

The intended reading was always: each hour earned confers *n* hours of **pledging power**, while the worker performing pledged work still earns **1 credit per hour**. Nobody's ledger inflates.

That was reading (b) below, which I treated as the fallback rather than the intent. **Reading (a) was a strawman and is withdrawn.** Reading (b) deserves better than the flat rejection it got — see the revised P2 verdict, which now **splits the mechanism in two and accepts both values of *k*.**

---

## 0. The headline

**Three of these four proposals are good, and none of them solves the problem they were aimed at.**

OP-16 is specifically: *two jobs, identical hours, identical calories, identical training, identical hazard — one of them is miserable. Who does the miserable one?*

Authorization changes **what is permitted**, not **what is preferred**. Under Proposal 1 the sewer job gets authorized — people plainly want it done — and still credits at one hour per hour. The worker still takes the pleasant job. **Approval is a demand signal, and OP-16 is a supply problem.**

That is not a dismissal. Proposal 1 is the most valuable idea to enter the project since the A7 amendment — it is a **decentralized demand signal**, which is precisely what P5 and OP-9 said the system did not have and what Parecon needed an entire Iteration Facilitation Board to fake. It should be adopted. It should just be adopted under its own name.

---

## 1. Proposal-by-proposal

### P1 — Authorization at 1:1. "Every credit worked creates new credit."

**Verdict: adopt, with one structural change.**

**What it actually is.** Cost tells you what a thing takes. This tells you **who wants it**. It generates that signal with no prices, no central optimizer, and no Iteration Facilitation Board — from information the log already holds. Compare `GLOSSARY.md#src-participatory-economics`: Parecon needs a standing body to announce indicative prices for every good, resource, labour category and capital stock, and [is attacked as implausible for exactly that](https://ejpe.org/journal/article/view/867). **P1 gets a demand signal without the body.** That is a genuinely strong result.

**The 1:1 ratio is not arbitrary — it is the only stable one.** See §2 below. This is worth knowing: the conservation property is derivable, not stipulated, which is exactly the kind of thing universality likes.

**🔴 The structural problem — it collides with A7 as written.**

If work must be pre-approved to be creditable, then unapproved work is **uncredited** work. A subsistence farmer grows wheat that nobody authorized. Under P1 as stated, that wheat has no creditable producer.

**This is the repealed A7 v0.1, returning through a side door.** The v0.2 amendment record (§12) rejected exactly this on the grounds that it made the books "describe a world in which material is produced and no one produced it" — a contradiction with A1, not a fairness complaint. Any mechanism that gates *credit* on approval re-introduces it.

**The fix, and it makes the mechanism better rather than weaker:**

> **Approval does not gate credit. Approval is a pre-commitment to absorb the resulting debit.**

You are always credited for what you materially did — A1, A7, universality all preserved. What approval buys is a **guaranteed counterparty for the property debit**. Authorized work ships its debit to the requester on completion; unauthorized work leaves the producer holding it until someone takes it.

This is strictly better than the original:
- It is **exactly the user's bank-loan analogy**, and closer to it than the original was. A loan does not grant permission to work. It supplies a counterparty who has committed in advance.
- It creates no new value from nothing, so **A1 is untouched**.
- It needs no new primitive. It is **custody acceptance**, already queued as a C1 residue *("can a transfer be refused? Without it, debit dumping works")*. **Approval is the affirmative case of the same rule.** One mechanism, two uses — the opposite of an ad-hoc addition.
- It fuses P1 with P3 into a single coherent object.

**~~⚠️ The serious remaining problem — authorization weight tracks material throughput.~~ — WITHDRAWN, see §0.5 C1.**

*The first pass argued that production-denominated authorization would let high-throughput sectors steer the economy while carers and teachers got no voice, and recommended denominating in service credit instead. Both the exploit and the fix were wrong: **credit tracks hours, not tonnage** (A2), and there is no separate service credit to denominate in (C1). A carer's hour and a steelworker's hour confer identical pledging power. Retained here only so it is not re-proposed.*

**What survives is much smaller.** Pledging power tracks **human hours spent**, so a heavily automated sector accumulates little of it despite enormous output. An automated food or energy sector would hold little sway over its own inputs. Worth a look — it may even be desirable, since it ties influence to participation rather than to capital — but it is a second-order effect, not a capture vector.

**And OP-1 still gains from this.** Even without a separate service-credit denomination, *"pledging power accrues per hour worked, equally for everyone"* is a concrete, non-hand-wavy answer to how contribution becomes direction — and it is **not a voting scheme**, which is what made the three §6.2 candidates awkward. It is a fourth candidate and it is the strongest of the four.

---

### P2 — Pledging power at 1.5x, 2x, or *n* — **revised after C3**

**Verdict: ✅ ACCEPT — by splitting the mechanism in two. Both *k*=1 and *k*>1 are correct, for different objects.**

*(Reading (a) — a worker receiving 2 credits per hour — was never proposed and is withdrawn. It would have been fiat under A1 and a rate multiplier under A2, but it is not on the table.)*

The divergence argument below is sound **and it only bites one of the two jobs this mechanism is doing.** The first pass rejected P2 because it applied that argument to both.

**The mechanism is trying to be two things at once:**

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I will absorb this debit" | "I want this to exist" |
| Backed by | earned credit | nothing |
| Scarce? | **Must be** | **Must not be** |
| ***k*** | **exactly 1** | ***n*, or unbounded** |
| Existing analogue | pre-order, choosing a GP | likes, ratings, sell-outs |

**The author's own examples already split along this line.** A pre-order for a shoe production run and choosing a primary care doctor are **commitments** — real future consumption, real debit absorbed. Thumbs-ups on a video and restaurant ratings are **signals** — free, plentiful, and informative precisely *because* they cost nothing.

**Where *k*=1 is forced.** A pledge that commits debit-absorption cannot exceed the credit backing it, or you get **fractional-reserve pre-ordering**: more debit committed than can be honoured, so when the goods arrive some pledger cannot take them and the producer is left holding it. That is the P3 failure inflicted on someone who did nothing wrong. *k*=1 is not an aesthetic preference — it is a solvency constraint.

**Where *k*>1 is right, and where the first pass was wrong.** For unbacked signals, the divergent backlog **is not a bug — it is the point.** Under *k*=1 you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. Letting people express preference across more things than they can fund **reveals the full ordering instead of just the top slice.** That is strictly more information. I under-weighted this.

**The unifying test, and it needs no new primitive:**

> **Does this commit debit? If yes, *k*=1. If no, *k* is unbounded.**

Note what falls out: the unbacked signal **is** §6.3's enrichment feedback. Pledging and enrichment feedback are not two mechanisms — they are the two ends of one spectrum, and the axis is *whether debit moves*. That is consistent with C1/C2 and it is why §6 should be describing feedback channels rather than credit types.

**Open, and non-trivial:** if signals are free and unbounded, what stops signal inflation and vote-buying? Sybil resistance carries part of it (C6), but **whether signals may be purchased with credit is now the live form of OP-8** and it is the real firewall question.

*Caveat on the pledge side:* at exactly *k*=1 with leakage — expired pledges, people who never allocate — the pool drifts down. **Needs an expiry/reversion rule.** Unspent pledging power reverting to a commons pool is the obvious candidate.

---

### P3 — Unsold bread is a hard lesson; producers seek a good debit:credit ratio

**Verdict: ✅ Correct, already implied by §3.2, and worth stating explicitly.**

- The existing model handles this natively. Property debit discharges **only on transfer** (§3.2), so unwanted goods are a live drag on the maker until someone takes them. If the bread rots, fate closure converts dischargeable property debit into **permanent consumption debit**. Waste self-penalizes with no new rule. Good.
- **It is the answer to the wash-crediting exploit** (below), which is why P1 and P3 must be adopted together rather than separately.

**⚠️ What it costs, and it should be named:** this allocates demand risk to the producer **exactly as capitalism does — minus the upside.** Producers bear the full downside of guessing wrong and receive no profit for guessing right. The predictable consequence is **risk-averse underproduction and a strong preference for pre-authorized work.**

That is mostly desirable — it is an anti-overproduction mechanism, and overproduction is a real pathology of the current system. But it has a sharp edge: **nobody makes the thing nobody asked for**, and that is how most genuinely new things arrive. Combined with P1's authorization gate, the speculative innovator is squeezed from both sides.

**This is where Enrichment must carry weight.** §6.3 grants debit-room retrospectively to makers people appreciate. That is the correct home for speculative work — and note it is the **dual** of P1: Enrichment is retrospective and voluntary, authorization is prospective and committed. **The system needs both halves, and only one is currently written down.**

---

### P4 — Entropy means debits always outpace credits; judge by ratio, not sum

**Verdict: ✅ Correct, important, and not currently written down anywhere. Promote it to the Foundations.**

**The claim is true and load-bearing.** Every real process dissipates. If credit records useful work and debit records material and energy consumed plus pollution, then **aggregate debit exceeds aggregate credit permanently and by construction.** The global books never balance and must never be expected to. That is not an accounting defect; **it is the second law showing up in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Consequences, all of which should be stated:
1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds.
2. **A3 is what makes this survivable, and this is the reason the user's instinct is right.** In a currency system, aggregate debt exceeding aggregate money is a solvency crisis — debt-deflation, spiral, collapse. Here there is **no creditor to be made whole**, because credit is non-fungible and never moves. Permanent aggregate net-debit is simply the correct description of an economy running on a thermal gradient. **This is a genuinely strong result and it belongs in §7 next to W1.**

**⚠️ But "ratio not sum" is too simple as stated, and breaks in three places:**

1. **It is brutal at the edges.** A newborn is all debit and no credit — infinite ratio. The retired, the sick, the disabled all degrade monotonically. These are exactly the people §7.5's basic-needs floor protects. **Ratio can only govern the discretionary layer; debit tolerance (OP-4) must sit underneath it.**
2. **It rewards asceticism over contribution.** A hermit who produces almost nothing and consumes almost nothing posts an excellent ratio. Under ratio-judgement, **withdrawal dominates productivity** — a direct inversion of fecundity. A pure-ratio metric is gamed by doing less of everything.
3. **0/0 is undefined**, and the non-participant case hits it immediately.

**Fix: two numbers, not one.** Ratio measures *efficiency*; absolute credit measures *contribution*. They answer different questions and neither substitutes for the other. "We judge by ratio" should become **"sums are thermodynamically meaningless; efficiency is a ratio and contribution is an absolute."**

---

## 2. Why 1:1 is the only stable ratio

Let *A* = outstanding authorization, *L* = labour hours performed per period, *k* = authorization created per hour worked.

Each period: authorization is consumed at *L* (work performed against requests) and created at *kL*. So **Δ*A* = (*k* − 1)·*L***.

- ***k* > 1** → *A* grows without bound. Authorization becomes free, therefore uninformative. **The signal dies of abundance.**
- ***k* < 1** → *A* → 0. The directed economy shuts down.
- ***k* = 1** → conservative. *A* is stationary; authorization stays scarce and therefore keeps carrying information.

Scarcity is what makes the signal mean anything. **P2 destroys the signal in order to strengthen it.**

---

## 3. Exploit hunt

**1. The wash-crediting ring.** Two participants authorize each other's work reciprocally and both accumulate credit indefinitely. Legitimate by construction — the approval is real, so no collusion detector fires.
→ **Stopped by P3, and only by P3.** A1 forces them to actually move matter, and the matter they move is stuff nobody wants, which leaves them holding the debit. **This is why P1 and P3 must ship together.** P1 alone is exploitable; P3 alone is inert.

**2. ~~The producer plutocrat.~~ — WITHDRAWN (§0.5 C1).** Credit tracks hours, not tonnage, so no sector can out-accumulate another by moving more matter. The exploit does not exist.
→ **Replaced by a weaker relative: the labour-intensive bloc.** A sector can gain pledging power by employing more people for longer, and automating *reduces* your voice. Marginal and arguably correct — it ties influence to participation — but worth a sim once C3 exists.

**3. The authorization cartel.** A group pools authorization and refuses to approve work outside its bloc, starving rivals of guaranteed counterparties.
→ Weakly stopped: under the corrected form, unapproved work is still creditable, so a boycott raises rivals' *risk* without excluding them. **This is the strongest argument for the corrected form over the original** — the original would make this a total exclusion, which is a fatal centralization vector under A8.

**4. The pre-order launderer.** Authorize work you intend to do yourself, or that a household member will do, to guarantee your own debit counterparty.
→ Not obviously harmful — it is a household coordinating its own production, which is fine. Becomes harmful at scale with fake identities, so it **reduces to proof-of-personhood (C6)** and needs no separate defence.

**5. The ascetic** (against P4). Minimize both sides to post an unbeatable ratio while contributing nothing.
→ Stopped only by keeping absolute contribution as a second, separately reported number.

---

## 4. Scorecard

| Test | P1 (corrected) | P2 (split) | P3 | P4 |
|---|---|---|---|---|
| **Universality** | ✅ — reuses custody acceptance, no new primitive | ✅ one test: does debit move? | ✅ | ✅ — thermodynamics is universal by definition |
| **Decentralization** | ✅ | ⚠️ signal inflation / vote-buying open | ✅ | ✅ |
| **Fecundity** | ✅ gives surplus a purpose (OP-19) | ✅ signals reveal the full preference ordering | ⚠️ chills speculative work | ✅ |
| **Axioms** | ✅ once approval gates debit, not credit | ✅ no ledger inflates | ✅ | ✅ |

*Scorecard revised after §0.5. P2 moves from ❌ to ✅ once pledges and signals are separated; P1's decentralization warning is withdrawn.*

---

## 5. What changes

| # | Action | Target |
|---|---|---|
| 1 | **Adopt P1 in the corrected form:** approval = pre-commitment to absorb debit, never a gate on credit. | Foundations v0.3, C5 |
| 2 | ~~Denominate authorization in service credit.~~ **Withdrawn (C1).** Replaced by: *pledging power accrues per hour worked, equally for all* — **OP-1's fourth and strongest candidate**, and not a voting scheme. | §6.2 |
| 3 | **Accept P2 by splitting it.** Pledges commit debit at ***k*=1**; signals commit nothing at ***k*=n***. One test: **does debit move?** | C5, §6.3 |
| 3a | **🔴 Retitle §6 — "three feedback channels," not "three credit types."** There is one credit: time. Rewrite §6.3's non-convertibility clause: feedback is non-convertible because **it was never credit**, not because a firewall holds it. | **Foundations v0.3** |
| 3b | **OP-8 dissolves in its current form.** Replaced by the narrower live question: **can signals be bought with credit?** | Register |
| 4 | Specify an **expiry/reversion rule** for unspent pledging power. | C5 |
| 5 | **Promote P4 into the Foundations:** aggregate debit exceeds credit permanently; this is the second law, and **A3 is why it is survivable.** | §7, next to W1 |
| 6 | **Split the metric:** ratio = efficiency, absolute credit = contribution. Ratio governs the discretionary layer only; OP-4 sits underneath. | §7.5, OP-4 |
| 7 | Note that **authorization and Enrichment are duals** — prospective/committed vs. retrospective/voluntary. Both needed. | §6.3, OP-6 |
| 8 | **OP-19 → largely resolved** by P1: surplus directs production. | Register |
| 9 | **OP-9 / P5 → substantially answered.** A decentralized demand signal, with no IFB. **Flag for the academic paper — this is the reply to Mises on preference revelation.** | Register, doc 2 |
| 10 | **OP-16 remains OPEN.** | Register |

---

## 6. OP-16 — still open, and the honest options

Since the proposals do not close it, here is what actually might, in order of preference:

**~~1. Service credit for onerousness.~~ — DEAD.** This was the first pass's favoured fix and **C1 kills it.** There is no separate service credit to pay a premium in; all work credits as time at one rate. The correction removed the best answer on the table, so OP-16 is now *more* exposed than it was this morning, not less.

**Replacement candidate — hour-ceiling differentiation. Currently the strongest surviving option.**

Pay the premium in **hours, not in rate.** A sustainable shift of sewer maintenance is 4 hours; a sustainable shift of pleasant work is 8. Both credit **1 hour per hour** — no multiplier anywhere — but the onerous worker reaches a full credit-day sooner and keeps the remaining time.

Why this survives A2 where a rate premium does not:
- **It is not rate-scaling.** The credit-per-hour is identical. What differs is how many hours of that work a human can sustain.
- **The justification is material**, which is exactly A2's intended resolution path. Occupational limits on night work, heat exposure, diving, and repetitive strain are real, measured, and already regulated in the existing world. This is a physiological fact about the job, not a judgement about how unpleasant it feels.
- **It needs no new primitive** — just a per-activity sustainable-duration figure, which the estimation engine has to carry anyway for hazard purposes.

**Weaknesses, both real:** who sets the ceilings → **OP-10 governance**, again; and everyone will claim their job is onerous, so the ceilings need an evidentiary basis rather than a self-report. That makes it a measurement problem, which is the kind this project is built to handle.

**Next:**
2. **Audit how much of OP-16 is unmeasured hazard.** Night shift, isolation, repetitive strain and chronic stress all have documented health costs. A2's third clause **already** injects those retroactively. It is likely that a real fraction of "jobs nobody wants" is hazard the model has simply not measured yet. **This deflates OP-16 without changing anything — check it before designing.**
3. **Automation as the intended answer.** Here P1 *does* contribute: accumulated unfilled authorization is exactly the visible, quantified signal that says *automate this*, and it identifies which jobs and how badly. It does not staff the sewer tonight; it funds the machine that ends the job. **A partial credit to the proposal, on the long horizon.**
4. **Rotation** (Parecon's balanced job complexes). Available, works, and carries [the compulsory-labour critique](http://libcom.org/blog/workers-critique-parecon-11042012). Last resort.

**Test to run before choosing:** take three jobs with near-identical material profiles and wildly different desirability — night-shift office cleaner, day-shift office cleaner, and rural postal carrier. Compute their debit-cost under the current model. **If the numbers come out identical, OP-16 is confirmed as real and option 2 is eliminated.** Cheap to run once C3 exists, and it decides between the options rather than arguing about them.

---

*Related:* `00-strategy/Aequitas_Objections_v0.18.md` (OP-16, OP-19, OP-9, P4, P5, W1) · `GLOSSARY.md#src-participatory-economics` · `GLOSSARY.md#src-local-currency-experiments`
