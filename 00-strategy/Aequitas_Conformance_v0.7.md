<!-- tag: cnf-aequitas-conformance -->
# Aequitas — Conformance Requirements

> **Version:** 0.7 · **Date:** 2026-08-28
> **Audience: implementers.** Anyone building a trust network.
> **Companion:** [`Aequitas_Foundations_v0.29.md`](Aequitas_Foundations_v0.29.md) — the system itself, and the argument for every row below. **Where the two differ, Foundations governs.**
> **Version history is kept separately and is not published**, so this document carries only what is currently true.
> **Two numbers are retired and are never reused: the bare `17`, and `14c`.**

---

<!-- tag: cnf-s1 -->
## 1. What this list is for

> **These documents state what must be true. They never state how to build it.**

Aequitas is an economic system, not a data-architecture project. A schema, a storage design, a transport protocol and a choice of cryptography are praxis, and they belong to whoever implements (Foundations §1.2).

**But an implementer is a real audience with a real need. Someone building a trust network has to know which system they are implementing.** That need is met by a list of things that must hold — never by an architecture.

> **The standing screening question is the dial test: if a principle survives at both ends of a dial, the dial is not part of the principle.** Conservation of mass and energy survives at both ends of every dial. A field name does not.

**An implementation is Aequitas if, and only if, every row in §2 holds.** Each is stated as a requirement rather than a design.

> **A requirement is a property an implementation *has*, never a result it must *achieve*.** §4 records the two things kept off this list on that ground, and why. **§5 records the three rows added on 2026-08-27, and the test each had to pass to get on. §6 records the 2026-08-28 review, which took in the arithmetic constraints and deleted one row.**

---

<!-- tag: cnf-s2 -->
## 2. What an implementation must satisfy

An implementation is Aequitas if, and only if, all of the following hold. Each is stated as a requirement rather than a design.

> ### The words rows 13 to 15 and 17a use
>
> **Coverage is the share of the real world's material flow that a network's records actually captured.** As a formula it is `Y ÷ N`.
>
> | Symbol | What it stands for |
> |---|---|
> | **`N`** | The **independently known total** for the extent being described — agricultural statistics, trade data, a satellite survey. Measured **outside** the ledger. |
> | **`Y`** | What the network's **own subscribers recorded**. |
> | **`Z`** | How many producers inside that extent are **still unmeasured**. |
> | **`R`** | The **leftover**, `N − Y`. What was produced by people the network cannot see. |
> | **extent** | The piece of the world a figure is about — a region, a sector, a population. **Never the set of subscribers** (row 17a). |
>
> **A worked example.** A valley grows wheat. A satellite survey puts the crop at **88,000 t** (`N`). The network's own farms recorded **82,000 t** (`Y`). So `R` is **6,000 t**, and coverage is `82,000 ÷ 88,000` = **93%**.
>
> **In plain words:** the network can see 93 of every 100 tonnes that valley grew. Six thousand tonnes were grown by people it holds no records for.

| # | Requirement | From |
|---|---|---|
| 1 | Every credit and debit records a real material or energy flow. **No issued, abstract, or fiat quantity exists anywhere.** | A1 |
| 2 | Flows are attributed to whoever **caused** them. Cost never passes to a party that did not act. | A1, §3.2b, §4.5 |
| 2a | A unit's debit-cost carries **only what that unit consumed.** A durable asset's creation-cost is held by the asset and its holders and is **never amortised into the things the asset was used to make.** The boundary is physical fate, audited by IC-4, never declared by the producer. | A5, §4.5, §4.5 |
| 2b | **Nothing is added to a cost figure.** There is no margin, fee, or spread anywhere in the accounting. | A5 |
| 2c | **No account that is not a verified human is a final holder of debit.** An organisation's debit is at all times its members' debit, divided by hours worked for it. **Closing an organisation moves nothing and clears nothing.** | A1, §3.2c |
| 3 | Labour is **never rate-scaled.** Differences between workers resolve as material costs. | A2 |
| 4 | **Credit is never transferable** — not by gift, sale, loan, inheritance, or theft. Only debit moves, and only with the thing it attaches to. | A3 |
| **4a** | **A position computed under one weighting model is never converted into another.** A network re-computes a claim from the shared physical record through its own model. **No exchange rate between credit-standards exists anywhere in the implementation, and two networks' figures are never added, netted, or compared as if they were one quantity.** | **A3, §4.2, §4.0, §5.6** |
| 5 | Standing is **derived from an append-only record of events, never stored** as an authoritative balance. **A record of what happened holds physical quantities only — never a weight, a cost, a price, or a value.** Cost is produced when the record is read, by applying the current weighting model to it. | A6, A5 |
| 6 | **Records are never destroyed or edited.** A disputed record is annotated; a superseded one is added beside. | §4.4, §4.8 |
| 7 | **Mass and energy conserve across every recorded process**, within a stated tolerance and at one level of detail. **Everything the books track has both an origin and a fate** — it came from an extraction, or from an estimated entry for something that existed before the books did; and at any moment it is held, consumed, or released to a named place in the natural world. **A thing with neither an origin nor a fate is reported as unaccounted, never as absent.** Nothing is recorded as consumed before it exists or after it is gone. | A1, A4 · *IC-1, IC-2, IC-3, IC-4, IC-6* |
| 7a | **A held thing has exactly one holder at any instant, and every change of holder is a recorded event.** This is what makes debit follow possession. | A1, §3.2, §3.2b · *IC-5* |
| 8 | **No account claims more than 24 hours of activity per 24 hours.** | A2, §5.5.5 · *IC-7* |
| 9 | **Cumulative pledges never exceed lifetime earned credit**, 1:1. **The pledging budget is spent when the pledge is made, not when the work happens, and there is no path that returns it.** | §4.6 · *IC-8, IC-9* |
| 10 | A debit is a **vector**. Any division is computed **per dimension, before collapsing** to a single figure. | §3.2a |
| 10a | A joint process's debit divides by **where the process physically sent its inputs**, measured at that facility for the period described, with a model used only where measurement is absent. The **method is published with its version**, so anyone can re-run it. **No split may depend on demand, desirability, or yield.** The method itself is the industry's to set, not this document's. | §3.4a, §1.2, §4.7 |
| 10b | **No output's share of any dimension is negative.** A negative result is a measurement error or a badly drawn process boundary — never a thing containing less than nothing. | §3.4a · *IC-10* |
| 10c | **Per dimension, the outputs' shares add up to exactly what the process took in.** Nothing is created or lost in a split. | §3.4a · *IC-11* |
| 10d | **Splitting a process stage by stage gives the same answer as splitting it whole**, and a divided estimate's parts add up to the coarser figure they came from. **This is what makes a redrawn boundary show up as an arithmetic disagreement rather than an argument.** | §3.4a, §4.4 · *IC-12* |
| 11 | The consumption gate is evaluated **at the moment of the transaction.** A later revision changes future room and never the validity of a completed act. | §3.3 |
| 12 | Every estimate carries its **basis, method, vintage and extent**, and may be superseded only by a **stronger** basis, never a weaker one. **An observation may replace an estimate; an estimate may never replace an observation.** | §3.3, §4.4 |
| 12a | **How sure a figure is, is stated separately from how it was known, and is attributed to whoever assessed it.** An unattributed confidence figure is an authority with no name. **Certainty is never read off the method** — a well-tested model can beat a badly calibrated meter. | A8, §4.4 |
| 12b | **Precision about a group does not carry down to a member of it.** Dividing a figure from a coarser claim to a finer one **lowers** how sure the finer figure is. A perfectly metered factory-month says very little about any one item that left it. | §3.4, §4.4 |
| 13 | A quantity **counted** over incomplete coverage is published as a **floor**, with the gap named. **A quantity DERIVED from two incomplete readings is published as an interval and labelled `floor`, `ceiling` or `not identified`** — and **`not identified` is the default** until a stated directional argument exists for **each** operand's blind spot. **A `floor` label is never inherited from the fact that some input was incomplete.** | §4.4 |
| 14 | Coverage is estimated over the **unmeasured residual** `Z`, never over the whole population. **Where `Z` is uncertain it is under-counted**, which raises each unmeasured producer's estimated share — the direction that prompts them to come forward and prove otherwise. **The error that liquidates itself is the safe one.** | §4.4 |
| 14a | Two figures are **subtracted only when they measure the same quantity, over the same boundary and window, within error bounds smaller than their difference.** Where they do not, the result is reported as an **interval** with the mismatch named — **`R ∈ [N_L − Y_U, N_U − Y_L]`** — never as a bare lower bound. | §4.4, §4.4 |
| 14b | **A coverage figure is warranted by a record made outside the ledger** — a counterparty's own record, a measured reservoir, or an independently known total `N`. **Arithmetic over the ledger alone establishes consistency and never completeness**, so a figure with no outside record behind it is published as `not identified`. | §4.4, §4.3 |
| 15 | The coverage leftover `R` is **computed, published, and charged to no account** until its causer onboards. | §4.4 |
| 16 | **Every estimating number and every method the implementer uses is published**, so anyone can re-run it. **Every published figure states the extent it covers**, so a bare pass is never a result. | §4.7, §4.3 |
| 16a | **Every cost constant carries its method, its version, and its uncertainty interval**, and the implementer **states which constants it has not reviewed and how old each reading is.** | §3.3a, §4.4 |
| 16b | **A constant may re-weight history only after two unaffiliated replications.** Review is triaged by **magnitude × concentration of beneficiary**, never magnitude alone. **Membership composition is public**, so a network concentrated in the sector it audits is detectable. | §3.3a |
| 16c | **The implementer can show how it audits its cost constants.** *How* is its own design (§1.2); **having no answer is not conforming.** | §3.3a, §1.2 |
| **16d** | **For every kind of work it credits, the implementer publishes what evidence that work requires**, before crediting any of it. **It credits no kind of work for which it has published no rule.** *Which* kinds it covers is its own choice (§1.2, A8); **having no published rule for something it credits is not conforming.** | **§4.2, §4.5, §4.7** |
| **17a** | **Every human inside the extent the books claim to cover is in those books, subscriber or not**, with credit **and** debit estimated on both sides. **The extent is a region, a sector or a population — never the set of subscribers.** A non-participant can **neither draw on that position nor be charged for it.** A position becomes **realizable** — able to act on what a person may consume — only on a verified account whose estimates have been superseded by observation. | **A7, §4.1, §4.4, §4.4** |
| **17b** | **When a cost constant, a joint split, or a coverage figure improves, every affected record in history recomputes.** A figure is a dated reading, never a verdict. **This changes future debit-room only, and never the validity of a completed act** (row 11). | **A4, A6, §3.3** |

### The `IC-n` labels

**Twelve of the rows above are arithmetic the ledger must never violate. They have been cited as `IC-1` to `IC-12` since 2026-07, and those labels stay valid here** so that older citations still resolve.

| Label | What it is | Row |
|---|---|---|
| **IC-1** | Mass balance | 7 |
| **IC-2** | Energy balance | 7 |
| **IC-3** | Everything has an origin | 7 |
| **IC-4** | Everything has a fate | 7 |
| **IC-5** | One holder at a time | 7a |
| **IC-6** | Nothing is used before it exists | 7 |
| **IC-7** | **The 24-hour cap** | **8** |
| **IC-8** | Pledges are backed 1:1 by earned credit | 9 |
| **IC-9** | A spent pledge budget is never returned | 9 |
| **IC-10** | No negative share | 10b |
| **IC-11** | Shares add up to the input | 10c |
| **IC-12** | Boundary additivity | 10d |

**Two candidates were tested and rejected on 2026-08-22 and stay rejected.** *IC-13 (genesis admissibility)* refused the ordinary case of somebody joining, and was trivially satisfied by whichever network was founded most recently. *IC-14 (citation closure)* demanded *a* citation rather than a true one. **Both checked a self-asserted field against a constant, where every surviving constraint checks one recorded quantity against another.**

---

## 3. What this list does not carry

| Not here | Where it belongs |
|---|---|
| Field names, record shapes, schema versions | The implementer |
| Storage, indexing, backups, key management | The implementer (§1.2) |
| Transport protocol and choice of cryptography | The implementer (§1.2) |
| Privacy practice | A network choice (§5.3a) |
| The values of ρ and the self-care floor `F` | Network dials (§3.5, §6.1b, A8) |
| Corporate form, jurisdiction, compliance posture | The implementer (§1.2) |
| **How a network schedules, staffs or samples its checking** | The implementer (§1.2) |
| **What a verification rung costs to run** | **Already in the log.** Audit work is credited work, so the hours are events and a query returns them (§4.7). **A separate published cost figure is a summary table, and a summary table is database design.** |

> ### The standing screen: assume the engineering works
>
> **Read every proposed row against this stipulation:**
>
> > **"Given a trust network with a secure database, 99.999% identity security, and practically unlimited storage capacity…"**
>
> **What survives the stipulation is an accounting rule and belongs here. What dissolves was an engineering complaint.** *"That would be too much data"* and *"you could not prove one person holds one account"* both dissolve. **Mass must still balance, and a pledge must still be backed 1:1.**

---

<!-- tag: cnf-not-requirements -->
## 4. Two things that are deliberately not on this list

**A requirement here is a property an implementation *has*. It is never a result an implementation must *achieve*.** The difference decides what belongs.

#### Essential provision is not a conformance requirement

**Foundations §5.5.4 rules that essentials are affordable to everyone alive**, because the floor credits the hours of staying alive and is set large enough to cover what staying alive costs. **That is true of the system. It is not a test an implementation passes.**

There was a row 17 saying so, from Foundations v0.18 to v0.23 and briefly here. **It was deleted on 2026-08-25 by author ruling**, on this ground:

> **Requiring it would be like saying that to conform to Aequitas, a network must succeed at a stated political goal.**

**Whether essentials are actually affordable in a given network depends on three things this list cannot check:** the value that network sets for its floor `F`, the value it sets for ρ, and what its real economy can physically deliver. **All three are dials or physical facts, not properties of an implementation** (Foundations §5.5.3, A8). A network can be built exactly to this list and still set `F` too low, and no reading of its code would say so.

**Nothing is lost from the theory.** The rule stands where it belongs, in Foundations §5.5.4, as a statement of how the system works. **Setting `F` and ρ so that it comes true is the network's job**, and the open problem of finding a stable band for them is **OP-4** in the objections register.

*(Every other row was checked against the same test in the same pass. **16c** is the closest call — *the implementer can show how it audits its cost constants* — and it survives, because showing a design is something an implementation either does or does not do. It does not require the audit to work.)*

#### "One verified human = one account" is not here either

Foundations §4.1 states it, and the **OP-22 ruling of 2026-08-25** makes it a rule each network applies to its own members rather than a requirement holding across networks — so it stays in §5.1 and is deliberately absent here. Record: [`OP-22_identity_not_disclosure_v0.2.md`](open-problems/OP-22_identity_not_disclosure_v0.2.md) §11, row 3a.

---

<!-- tag: cnf-s5 -->
## 5. The 2026-08-27 review — three rows added

**Why the review happened.** On 2026-08-27 a project paper — `OP-22_identity_not_disclosure_v0.2.md` §7 — added one network's debit-room to another network's and published the sum as a person's real command of material. **The author refused it.** The list was then checked row by row against the axioms.

**Three rows came out of it: 4a, 17a and 17b.** All three state rules Foundations already carried in prose. **None is new theory.**

> **The finding underneath all three: a rule that lives only in prose does not bind.** §6.4b's sentence about exchange rates was in front of the reader who broke it. **The conformance list is not a summary of Foundations — it is the part of Foundations that has to survive contact with somebody in a hurry.**

### 5.1 Requirement 4a — comparison, never conversion

**The rule already existed.** Foundations §4.2 states it, and gives the reason:

> *"Converting a balance from one model into another would be an exchange rate between credit-standards — a medium of exchange, which A3 and the circulation-failure analysis (§7.6) forbid."*

**It was not on this list, and that omission is why the error was publishable.** An implementation could satisfy every one of the sixteen rows as they stood and still publish a conversion table between its own credit and a neighbouring network's. **That creates a medium of exchange** — the single failure mode Foundations §5.6 claims Aequitas is structurally immune to, and the substantive reason it must never be described as a currency.

#### An example, with the numbers

One person works **8 hours** on a Monday and holds an account with two networks.

| | Network A | Network B |
|---|---|---|
| The floor `F` | 4 h/day | 10 h/day |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| Debit-room at ρ = 1.2 | 1.2 × 12 = **14.4 h** | 1.2 × 18 = **21.6 h** |

**Both figures are correct, and neither breaches IC-7**, because 12 and 18 are each under 24 and **IC-7 binds each account separately.**

**The forbidden line is `14.4 + 21.6 = 36.0`.** A debit is a vector — kilograms, joules, labour-hours, land-area-years — and it becomes a single figure only when a network **collapses** it through its own weighting model (§3.2a). **A and B run different models**, so the same physical basket collapses to a different number in each. **Adding the two sets one A-hour equal to one B-hour, which is an exchange rate.**

> **The two numbers are not two measurements of one quantity. They are one physical fact read through two models, and there is no third model to express a sum in.**

**Requirement 4a passes the §1 dial test and the §4 have-versus-achieve test.** An implementation either holds a conversion path between models or it does not. **That is a property, readable from the implementation, and it survives at both ends of every dial.**

> **Why it is numbered 4a and not 17.** **Requirement 17 was deleted by author ruling on 2026-08-25 and the number is retired**, so re-using it would make two different rules share one label across versions. **4a sits beside row 4 because both are A3**: credit does not move between people, and a position does not move between models. **They are the same axiom seen twice.**

---

### 5.2 Requirements 17a and 17b — two axioms that no row made checkable

> **Proposed on 2026-08-27 and ruled in the same day. They are requirements, not proposals.**

**The problem they fix, in one sentence: §1 claims *"an implementation is Aequitas if, and only if, every row in §2 holds"*, and two axioms were cited by no row at all.** A1, A2, A3, A5 and A6 all appeared in the **From** column. **A4, A7 and A8 did not.**

| Was missing | The axiom | What an implementation could have done and still passed every row |
|---|---|---|
| **17a** | **A7 (universal accounting)** — *"Every human is accounted for whether or not they participate, with credit and debit estimated symmetrically for everyone."* | **Account only for its own subscribers.** Rows 14 and 15 govern the residual once a network estimates one, but **no row required a network to have non-participants in its books at all.** §4.1's *"participation is voluntary, coverage is not"* was on no row, and neither was A7's accounted-versus-realizable distinction. |
| **17b** | **A4 (no externalities)** with **§3.3** — *"including consequences discovered decades later."* | **Freeze its weighting model forever.** Row 5 makes recomputation *possible*; rows 11 and 16b both *presuppose* re-weighting happens. **No row required that a better constant actually re-weighs history.** |

#### 17a — one sentence was added during the ruling, and it matters

**The drafted wording said *"within the extent the implementation's books claim to cover."*** Read alone, that is gameable: **a network could declare its extent to be its own membership**, and the requirement would be satisfied by covering nobody but subscribers.

**So the row now says the extent is a region, a sector or a population, never the set of subscribers.** That is not a new rule. **§5.1b measures a residual as `N − Y`, where `N` is an independently known total for a whole extent** — agricultural statistics, trade data, a satellite survey — **and §5.1c publishes coverage as *"these books cover 60% of this region's measured output."*** **Both already define extent against the world rather than against membership.** The row states what those two sections already assume.

##### An example, with the numbers

A network covers one valley. A satellite survey puts the valley's wheat at **88,000 t** for the crop year. The network's own farms recorded **82,000 t**.

| | |
|---|---|
| `N` — independently known total for the extent | **88,000 t** |
| `Y` — recorded by measured producers | **82,000 t** |
| `R = N − Y` — grown by producers nobody measured | **6,000 t** |

**Under 17a the extent is the valley, so the 6,000 t exists in the books** — computed, published, and charged to no account until its causer onboards (row 15). **If the extent were allowed to be "our members", `N` would equal `Y`, the residual would be zero, and a real 6,000 tonnes would sit outside the accounting.** That is the *"outside"* A4 says there is none of.

#### 17b — what it does and does not require

**It requires that recomputation happen.** Row 5 makes it possible; nothing made it obligatory. **A network could have derived every position from its log using a weighting model frozen in its founding year and passed every row**, while A6 says *"improve the science, and all history re-weighs automatically"* and A4 reaches *"consequences discovered decades later."*

**It does not weaken two rows that constrain recomputation, and both still bind.**

| Row | What it still does |
|---|---|
| **16b** | A constant may re-weight history **only after two unaffiliated replications.** 17b says recomputation must happen; 16b says what must be true before it may. |
| **11** | The gate is evaluated **at the moment of the transaction.** A re-weight changes future debit-room and **never the validity of a completed act.** 17b restates this in its own words so the two cannot be read apart. |

#### Both pass the two screening tests

**The §4 have-versus-achieve test.** A book either covers non-participants or it does not. A system either recomputes history or it does not. **Neither asks anyone to succeed at anything** — 17a does not require the estimate to be accurate, and 17b does not require the science to be right.

**The §1 dial test.** Both survive at both ends of every dial: the machine-governed society with zero transparency and the fully transparent one both cover non-participants and both recompute (Foundations §1.2).

#### A8 still needs no row

Its variance half is in §3 — ρ, `F` and privacy are network dials. Its *"anyone else must be able to re-compute its claims"* half is requirement **16** plus **4a**. **Nothing further is checkable inside one implementation**, because A8 is a statement about the ecosystem rather than about a network.

> **Every axiom is now cited by at least one row.** A1 · 1, 2, 2c — A2 · 3 — A3 · 4, 4a — A4 · 17b — A5 · 2a, 2b — A6 · 5, 17b — A7 · 17a — A8 · §3, 16, 4a.

---

### 5.3 Rows 13 and 14a — repaired in v0.5, after the subtraction defect

**This section said, in v0.3 and v0.4, that rows 13 and 14a were *ahead of an open ruling* and must move when Foundations §4.4 was repaired. It was repaired on 2026-08-27 and they have moved.**

**The defect.** §5.1b said *"report the residual as a lower bound"*, unqualified. **`R = N − Y`, and if `Y` is under-recorded while `N` is sound, `R_obs ≥ R_true` — an upper bound.** The sentence came from carrying §5.1a's floor rule through a subtraction. **A floor rule holds for a count; a subtrahend reverses it.** Found by @cairn-lineage (c23607 on 1f916.ai #2259) and conceded in public at c25746.

**Worked on the published numbers** — `N` = 88,000 t, `Y` = 82,000 t, `R` = 6,000 t:

| Blind operand | True `R` | 6,000 t is |
|---|---|---|
| `Y` under-records by 4,000 t | **2,000 t** | a **ceiling**, 3× the truth |
| `N` under-observes by 10,000 t | **16,000 t** | a **floor** |

**What changed in the two rows.**

- **Row 13** now separates a **counted** quantity from a **derived** one. A count over incomplete coverage is still a floor. **A figure derived from two incomplete readings is an interval with one of three labels**, and **`not identified` is the default.**
- **Row 14a** now requires the **interval** — `R ∈ [N_L − Y_U, N_U − Y_L]` — rather than *"a bound"*, which was the word that let a bare floor through.

> **`not identified` is a third landing state the documents did not have.** They had *value* and *floor*. **An implementation with no way to express "I cannot say which direction this is wrong in" will label everything, and the labels will be wrong in the flattering direction.**

---

### 5.4 What the review found nothing wrong with

**Every other row was checked against the axiom it cites and against the axioms it does not.** No contradiction was found. Three pairs look like they might collide and do not:

| Looks like a collision | Why it is not |
|---|---|
| **2c** divides an organisation's debit among its members, but **4** says credit never moves | §3.2c divides **debit only.** Members are credited their own hours whatever the organisation does. |
| **7** requires mass and energy to conserve, but §3.5 says the books never balance | **Different quantities.** Conservation is per process, on matter and energy. §3.5 is about aggregate debit exceeding aggregate credit, which is the second law appearing in the ledger. |
| **2a** keeps the barn out of the beef, but **10a** divides a joint process's debit among its outputs | **Different debits.** Capital accrues to the asset (§6.2b); a joint split divides the **consumables** the process physically sent into each output (§3.4a). |

---

### 5.5 Requirement 16d — a published evidence rule for every kind of work credited

**Added 2026-08-27 by author ruling**, answering a question the drafting council raised on 2026-08-22 and nobody had answered: **IC-7 and IC-8 encode a shape of a life — who consents to that denominator?**

**The worry.** IC-8 bounds a person's lifetime pledging power by their lifetime **measured** credit. Foundations §4.5 weighs unwitnessed work near zero until corroborated. **Put together, a person whose work a network measures badly appeared to get little credit and little voice, with nobody having agreed to it.**

**The ruling removes the case rather than softening it.**

> **A trust network publishes, for every kind of work it credits, what evidence that work requires. That published set is its contract with the subscriber. A network should therefore never credit a kind of work it cannot get evidence about.**

**So a kind of work is either covered by a published rule — evidence exists, hours credit in full — or it is not covered, and nobody was promised credit for it.** *"Credited but measured badly"* is not a state the design produces.

#### An example, with the numbers

A network publishes its rule for translation: **the text exists and the client confirms receiving it.**

| | Hours worked | Rule | Credited |
|---|---|---|---|
| **A** delivers, client confirms | 20 h | met | **20 h** |
| **B** asserts 20 hours, no text, no client | 20 h | not met | **0 h** |

**B knew before starting, because the rule was published.** And if translating for someone who cannot confirm is work the network wants, **it writes a rule for that case — and then B's 20 hours credit at 20 hours**, not at 0.4 because a vague claim was weighted cautiously.

#### Why it is a requirement and not advice

**It passes both screening tests.** An implementation either publishes a rule for each kind of work it credits or it does not — **a property, readable from the implementation** (§4's have-versus-achieve test). And it survives at both ends of every dial: the transparent society and the machine-governed one both either publish the rule set or do not (§1's dial test).

**What it does not do.** It does not require the rules to be good, or generous, or complete. **A network may credit few kinds of work, and conform.** What it may not do is credit something with no published rule behind it.

#### What bounds the cost to a person

| | |
|---|---|
| **Subsistence is never at risk** | Self-care is verified by proof of life, which every living human meets at near-zero burden (Foundations §4.2). |
| **Bad rules lose people** | Sellers choose which networks they accept (§5.0), and counterparties discount credit they cannot check. |
| **Nobody is enclosed** | Non-participation is always available (§5.3c). |

> **Foundations §4.5 already carried the other half**: *"the accounting covers what is claimed and attested. Everything else is life."* **That says the system need not capture everything. 16d says a network must state in advance what it does capture.**

---

---

<!-- tag: cnf-s6 -->
## 6. The 2026-08-28 review — the arithmetic came in, and one row went out

**Why the review happened.** The event-log paper that carried the arithmetic constraints was retired by author ruling on 2026-08-28. **The constraints themselves are not database design — they are arithmetic the accounting requires**, so they moved here rather than going with it.

### 6.1 What came in

**Nine constraints had no row.** Three already did: IC-1 to IC-4 sat inside row 7, IC-7 was row 8, IC-8 was row 9.

| Now | Was | Why it is an accounting rule and not an operations one |
|---|---|---|
| **7a** | IC-5 | **Debit follows possession** (§3.2b). If a thing can have two holders at once, or a holder can change with no record, the rule that makes property debit move has nothing to stand on. |
| **10b** | IC-10 | **No output's share is negative.** This is the answer to [Steedman's negative-value result](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063). Without it, §3.4a's joint-production rule is not safe. |
| **10c** | IC-11 | **Shares add up to the input.** A split that loses or invents material breaks A1. |
| **10d** | IC-12 | **Boundary additivity.** §3.4a leaves the split method to the industry and relies on this to stop a producer redrawing the boundary until the answer flatters them. |
| Folded into **7** | IC-6 | Nothing is used before it exists. It is one clause of origin-and-fate closure, not a rule on its own. |
| Folded into **9** | IC-9 | A spent pledging budget is never returned. It is one clause of the 1:1 backing rule. |

### 6.2 What went out — row 14c

**Row 14c required a network to publish what each verification rung costs to run.**

> ### AUTHOR RULING, 2026-08-28 — deleted
>
> **The cost is already in the log.** A network doing verification audits is **crediting people for doing those audits**, which is credited work like any other (§4.7 — *funding is recognition*). **Those hours are already events.** A query over the log returns every audit for a kind of item or a category of work.
>
> **The work of verification does not need its own data structure.** Requiring a second, separately-published cost figure asks a network to keep a summary table, and that is database design.

**Nothing is lost from the theory.** Foundations §4.3 still carries the cost table, the worked farm example, and the warning that a large checking cost is a sign to audit the producer rather than a design to accommodate. **What is removed is the requirement that a network publish a separate figure for it.**

**One citation moves with it.** The register credits @custos (c16467, c16479 on 1f916.ai #1750) with the cost column. **That credit stands** — the finding was real and it is in Foundations §4.3. It is no longer a conformance row.

### 6.3 What was checked and kept

**Rows 14, 14a and 14b were re-read against the stipulation in §3 and all three survive**, because none of them tells a network how to run.

| Row | Why it is not operations |
|---|---|
| **14** | It decides **whose** estimated share is whose. Computed over the whole population instead of the leftover `Z`, the rule pays people to stay unmeasured. **That is an accounting outcome, not a workflow.** |
| **14a** | It says when a subtraction is **valid arithmetic**. Two figures that measure different things, over different areas, over different periods, do not subtract. |
| **14b** | It says what a coverage figure is **warranted by**. Reworded in this version from *"a check compares two records made on separate paths"* to a statement about the figure, so that it constrains the published number rather than the checking machinery. |

**Row 16 absorbed the extent rule** — *every published figure states the extent it covers, so a bare pass is never a result.* **It was a separate rule in the retired paper and it is one clause here**, because it is the same obligation as publishing the method.

### 6.4 What this does not change

**No axiom moved. No mechanism changed. Nothing was added that was not already binding somewhere.** The arithmetic constraints have been cited by Foundations §5.5.5 and by the simulator since 2026-07. **This version gives them a home that outlives the paper they were written in.**

---

*End of v0.7.*
