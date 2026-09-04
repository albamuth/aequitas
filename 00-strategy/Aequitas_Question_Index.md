<!-- tag: qidx-aequitas-question-index -->
# Aequitas — Question Index

> **Version:** 0.1
> **Date:** 2026-09-03
> **What this is:** a lookup table keyed by **the question you are about to ask**, so you find the answer that is already written instead of deriving a new one.
> **What this is not:** a summary of the theory. It settles nothing. Every row points at the document that does.
> **Companion:** [`GLOSSARY.md`](GLOSSARY.md) resolves abbreviations. **This file resolves questions.**

---

## 0. How to use this

**Read this file before answering anything about Aequitas. It is short on purpose.**

**Three tables, and the verdict column tells you what you are allowed to do.**

| Table | Verdict | What you may do |
|---|---|---|
| **§1** | **REFUSED** | The proposal contradicts an axiom or a stated rule. **Say which one and stop.** Do not stress-test it, do not look for a version that works |
| **§2** | **ANSWERED** | The answer exists. **Give it, cite the section, and do not re-derive it** |
| **§3** | **OPEN** | Nothing decides it. **Say it is open and name the label.** Do not supply a plausible answer |

> **The failure this file exists to stop.** On **2026-08-22** a whole privacy architecture was proposed, stress-tested and retracted, because **A7 requires the records to be complete** — one sentence in a section nobody had searched. **The same day, two more answers turned out to be already written and unread.** The proposals were not ambiguous. **They were unread.**

**If your question is not in any table, use §5.** Do not assume absence means the question is open.

---

## 1. REFUSED — proposals an axiom already rules out

**Every row is a real proposal that looked reasonable. Naming the axiom is the whole answer.**

| The proposal | Refused by | The one-line reason |
|---|---|---|
| **Minimise data. Record less. Let people delete records** | **A7** · §4.8 | **Coverage is not voluntary.** Every human is in the books whether they take part or not, and *"a log that can be truncated is not a log."* **Participation is the dial. Coverage is not** |
| **Erase a person's record on request** | §4.8 | **There is entry and there is no exit.** Ceasing to participate is always available; **erasure never is.** Re-weighting and lifetime reconstruction are both impossible over deleted records |
| **Pay more per hour for skilled, dangerous or unpleasant work** | **A2** | **Labour is never rate-scaled. One hour credits as one hour.** The three real differences land as **material** costs — extra food, injected harm-debit, front-loaded training |
| **Let likes, citations, reviews or applause create credit** | §4.2 · §4.6 | **Forbidden by name.** Verification asks whether the work happened, never whether anyone valued it. **Feedback is not credit** |
| **Transfer, lend, gift, gamble or inherit credit** | **A3** | A credit records **who was responsible.** Responsibility is a fact about a person, **so there is nothing coherent to transfer** |
| **Convert one network's credit into another's** | §4.2 | **Comparison, never conversion.** A rate between two credit-standards is a medium of exchange, and **A3 forbids one** |
| **Set a global value for ρ, `F`, or the privacy practice** | **A8** | **No organisation may acquire authority over the core rules.** These are network dials, published and competed on |
| **Make a joint process's cost depend on what people want, or on which cut is desirable** | §3.4a | Two identical steers in two towns would carry different figures. **Fails universality, and it is price allocation in costume.** *(**Yield** left this ban on 2026-09-03: output mass is physical and a scale reads it — see §2)* |
| **Divide a joint process's cost among its outputs at all** | §3.4a · §2.5 | **36 methods that all satisfied the four obligations came out 6.31× apart.** The division was withdrawn rather than governed. **Where nothing was divided in the world, refuse to divide it in the books** |
| **Add up what several co-products carry, to get the process total** | **A3** · conformance 10e | **A debit is a unique record, not an amount.** A parcel reached by two paths is counted **once**. Summing overstates a real refinery by **7.00×** and gives a different answer at every level of detail |
| **Amortise a barn, a hospital or a machine into the price of each unit it made** | §4.5 | **The beef did not build the barn.** Charging onward never terminates — it chases the builder, the steelmaker, the doctors' education, back to the first human activity |
| **Charge the buyer for the pollution of making the thing** | §3.2b | **Only the miner acted to pollute.** Pollution from *making* stays with the maker permanently; pollution from *using* belongs to the user |
| **Charge a patient for the doctor's training** | §4.5 | **Training is paid when it happens.** A large up-front cost with a diffuse benefit is carried where it is incurred, never charged onward |
| **Divide the leftover `R = N − Y` among the producers you know are missing** | §4.4 | **Measured, not argued.** Two different worlds give one network **identical books to the last decimal**, so no rule computed from them can separate the two. **A residual proves activity is missing; it does not prove whose** |
| **Require the books to balance** | §3.5 | **Aggregate debit exceeds aggregate credit permanently and by construction.** That is the second law of thermodynamics appearing in the ledger |
| **Record a share, a bond, a currency or a token** | **A1** · §3.1 | Not matter and not energy. **What is recorded is the material the claim is upon**, sitting on whoever physically holds or operates it |
| **Make someone accept an object they do not want** | §2.4, rule 3 | *Custody follows possession* means you cannot take a thing and disclaim its debit. **It does not mean anyone can be forced to take a thing** |
| **Reverse a fraudulent past transaction** | §4.7 | **You cannot un-eat a sandwich.** The fake credit is negated, the ratio fails, and discretionary purchases stop. **Unwinding it would corrupt the honest seller's books** |
| **Add bankruptcy, or forgive accumulated debit** | §4.7 | **There is time.** Everyone alive accrues credit at the floor, so the ratio recovers on its own. **The consequence is exactly the size of the fraud, measured in time, and nobody sets it** |
| **Attribute an electricity emission by a supply contract** | §3.2b | **An agreement is a paper claim.** A record of CO₂ must come from a measurement of CO₂ — the grid's actual fuel mix in the periods the consumer drew |
| **Let a network declare loyalty to itself creditable** | §2.3 | Loyalty is not production, not a service, and not enrichment. **The three categories are the outer wall and they do not vary** |
| **Add a rule, an exception or a special case for an awkward profession or sector** | §2.1 | **Universality.** *"A system with exceptions cannot be shown to be wrong. Any awkward case gets a new exception"* |

---

## 2. ANSWERED — the answer is written, do not re-derive it

| The question | The answer, in one line | Where |
|---|---|---|
| **How is one process's cost divided among several outputs?** | **It is not divided.** Every co-product carries the **whole** process cost against its **own output mass**. No basis, no routing model, no boundary to choose | §3.4a · §2.5 · folded in Foundations **v0.38** · sim [`../06-simulation/chain-resolution/`](../06-simulation/chain-resolution/RESULTS.md) |
| **Then do the books inflate, if two products both carry 100 MJ?** | **No. A3: a debit is a unique record of one specific event** — a pointer at an identified parcel, not an amount. Both point at the **same** 100 MJ. **The ledger walk is a union over parcels, never a sum** | A3 · §3.2b · §3.6 · §4.3 · measured in chain-resolution |
| **Does reading a chain more finely change the figures?** | **Yes, one way only. A coarse reading is a ceiling on a fine reading** — a product carries the steps it passed through ÷ its own mass, and those steps are a subset. **A producer wanting a lower figure must buy more measurement** | chain-resolution `RESULTS.md` |
| **Where does the basic-needs floor come from? Is it a grant?** | **It is not an income, a benefit, a safety net or an entitlement.** Keeping a living human body alive is work, so it credits at the ordinary rate. **Credit for no time worked is the abstract issued quantity A1 forbids** | §5.5.2 · §2.3 |
| **What stops inequality?** | **`24 ÷ F` inside one network's books, and it is an absolute maximum nobody reaches.** A very hard working life reaches about **1.6×**, not 2.4×. Money reaches ~**10⁶×** | §5.5.5 |
| **Who funds the auditors?** | **Nobody. "Funding" imports a question from money that does not survive translation.** Audit work is work, recorded when it happens. **What is scarce is demand and verification, not the credit** | §4.7 |
| **What stops a lax network exporting inflated credit?** | A counterparty **re-computes** the claim through its own model and discounts it. ⚠️ **That guard depends on OP-22 and the mechanism does not exist yet** | §4.2 |
| **Whose are a power station's emissions?** | **The consumer's**, by the grid's measured fuel mix over the periods they drew. Electricity cannot be stored, so flipping the switch commands a generator to burn fuel now. **Transmission losses stay with the producer** | §3.2b |
| **What happens on death?** | The record closes and persists. **Credit does not transfer and nothing is inherited on the credit side.** Material debit moves with the things; consumption and pollution debit does not move | §4.8 |
| **Why will this not die the way local currencies died?** | Three failures. **Circulation cannot occur — there is no medium of exchange.** Institutional suppression does not fit an accounting system. **Valuation is only partly answered** (OP-16) | §5.6 |
| **Is in-kind calculation computationally possible at national scale?** | **Yes, demonstrated.** Cockshott & Cottrell with sparse-matrix methods. Mises's objection was in-principle; the scale objection was answered by people who ran the arithmetic | §3.3 |
| **Does Steedman's negative-value result apply?** | **No.** Each share is a forward measurement of what physically went in, and a deposition cannot be negative. Confirmed across 4,098 economies. **Note the limit: it proves no split is negative, not that a split is unique** | §3.4a |
| **Can identical twins share one account?** | **The arithmetic refuses it.** IC-7 caps an account at 24 h in 24 h, so two twins faking one account reach **34 hours a day against 36 honest** — they lose 730 hours a year and gain nothing | §4.1 · `OP-22_identity_not_disclosure_v0.2.md` |
| **Who owns land?** | **Nobody.** A structure occupies a bounded space, and that occupation is a **remediation debt** discharged only by actually restoring the space | §3.7 |
| **How does someone use Aequitas while the world still uses money?** | Both directions permitted, both dearer than trading inside. **Money is invisible because it is not physical**, so a payment is not an event. **Goods cross the boundary; standing does not — you cannot buy hours** | §4.8 · `OP-27_parallel_implementation.md` |
| **Is a first estimate being wrong a problem?** | **No inaccuracy in this system is irreversible.** Every figure is a dated reading, and better science re-weights every affected ledger backwards through history | §3.3 |
| **Does re-weighting make past purchases retroactively illegal?** | **No. `D ≤ ρ·C` is evaluated at the moment of the transaction.** A revision changes future debit-room and never invalidates a completed act | §3.3 |
| **Does the system need to record everything a person does?** | **No, and attempting it would be "futile and grotesque."** The accounting covers what is claimed and attested. **What a network owes is to say in advance what it does cover** | §4.5 · §4.2 |
| **Who gets the last scarce item?** | **Deliberately not settled here.** A queue, a lottery, or pledge-priority, decided where the physical thing is handed over. **Cost says what a thing took; distribution is a separate question** | §3.4a · §4.6 |
| **How big is a trust network?** | **No set size.** One valley, one trade, one country, or the world. **A8 is about who may change the rules, not about how big anyone is** | §4.0 |

---

## 3. OPEN — say so, and do not supply an answer

**These have labels. Use the label. A plausible answer offered here is the most expensive mistake available.**

| Label | The question | Status |
|---|---|---|
| **OP-10 (weighting governance)** | Who governs the weighting model | 🔴 **Top blocker** |
| **OP-24 (understatement drift)** | A cost error that flatters subscribers has **nobody** who wants it fixed. **The observed failure mode of every carbon-accounting regime so far** | 🔴 Fix proposed, unproven. **§3.3a states the problem and deliberately does not solve it** |
| **OP-16 (onerousness gap)** | Tedium and indignity leave no material signature. **The hazardous half is answered by the pledge reserve; the dull-but-safe half is not** | 🔴 Unsolved |
| **OP-22 (audit disclosure)** | The minimum an auditor must see to check a claim **without seeing a history** | 🔽 **Load-bearing.** Gates the disparity ceiling and the anti-arbitrage guard |
| **OP-4 (debit tolerance)** | Where ρ should sit, and the second dial: **whether a network credits a child's learning time** | Open |
| **OP-25 (illicit dumping)** | Attributing abandonment back to the abandoner | 🔽 Minor, Level-2 |
| **OP-28 (residual denominator)** | What `R = N − Y` is distributed by. **Honest noise barely moves it; a producer declaring half their real land defeats it** | 🟠 Candidate repair unmeasured |
| **P4 (coordinator class)** | The extractive employer is structurally foreclosed. **Coordination power is not** | 🔴 Live blocker |
| **Can feedback be bought?** | A purchasable signal is a back-door currency | Registered, not solved (§4.6) |
| **The "natural state" baseline** | What the natural state of an already-urban plot is | Open sub-question of §3.7 |
| **Real-time against batch** | Grid storage and on-demand services sit between the two poles | Registered open edge (§3.2b) |
| **Whether a network can be trusted with what it holds** | A network keeping lifetime reconstructions holds a concentration of **information** comparable to the concentration of **wealth** this project removes | **Unanswered** (§4.7) |

---

## 4. Four words that do not mean what they usually mean

| Word | Here it means | Not |
|---|---|---|
| **Debit** | A record that matter or energy was taken, **and who holds the consequence** | A bill. **Nobody collects it and nothing is ever settled** |
| **Credit** | A record that a person spent an hour of their life on work | Money, a balance, or anything spendable. **A purchase adds to `D` and takes nothing from `C`** |
| **Cost** | What a thing took from the world, physically | Value, worth, or price. **Aequitas is a theory of cost and deliberately not a theory of value** |
| **Funding** | **Recognition of an activity as creditable** | A budget, a grant, or an allocation. **There is no treasury** |

> **Banned terminology:** never call Aequitas a **currency**, a **token** or a **blockchain** — it is an **accounting system**. Never say **"syndicate"** — say business, institution, or co-op.

---

## 5. If your question is not listed

**Run these three, in order. They are the document's own sorting rules.**

| # | The test | Where |
|---|---|---|
| **1** | **Did the thing being divided leave a physical trace?** **Trace → measure it. No trace → first ask whether it has to be divided at all**, and only then declare a convention and say so | §2.5 |
| **2** | **If a principle survives at both ends of a dial, the dial is not part of the principle.** Storage technology, jurisdiction, corporate form, privacy level and network size are all dials | §2.6 |
| **3** | **Does this check compare two things made on separate paths, or a thing to itself?** **A check that compares a thing to itself can find a mistake and cannot find a hole** | §4.4 |

**Then the three criteria every mechanism is tested against:** **universality** (no exceptions), **decentralization** (a stranger can re-check without permission), **fecundity** (it pays its own maintainer from inside the system). §2.1.

> **And the standing warning.** **Five times the answer or the refutation was already written and unread** — A3 for circulation failure, A2 for joint production, §4.4 for the coverage witness, §4.7 for self-custody, and **A7 for why data minimisation is not available to this system at all.** **A search finds a mechanism. Only a read finds the premise you are about to contradict.**

---

## 6. What to read, and in what order

| If you are | Read |
|---|---|
| Answering one question | **This file.** If it is not here, §5 |
| Proposing a new mechanism | **[`Aequitas_Foundations_v0.38.md`](Aequitas_Foundations_v0.38.md) whole**, then §2.1's three criteria |
| Implementing | [`Aequitas_Conformance_v0.12.md`](Aequitas_Conformance_v0.12.md) — what must be true, never how to build it |
| Checking whether an objection is new | [`Aequitas_Objections_v0.28.md`](Aequitas_Objections_v0.28.md) |
| Checking the arithmetic without running code | [`../06-simulation/audits/audits_inert/constraints.md`](../06-simulation/audits/audits_inert/constraints.md) — IC-1 to IC-12 as mathematics |
