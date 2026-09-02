<!-- tag: cnf-aequitas-conformance -->
# Aequitas — Conformance Requirements

> **Version:** 0.11 · **Date:** 2026-09-02
> **Audience: implementers.** Anyone building a trust network.
> **Companion:** [`Aequitas_Foundations_v0.37.md`](Aequitas_Foundations_v0.37.md) — the system itself, and the argument behind every row below. **Where the two differ, Foundations governs.**
> **Version history is kept separately and is not published**, so this document carries only what is currently true.
> **Two row numbers are retired and are never reused: the bare `17`, and `14c`.**
> **Row 14 no longer requires a per-head slice of the leftover, and no longer tells a network to under-count the producers it cannot see. New row 14d requires an extent register to be published as unaudited.**

---

<!-- tag: cnf-s1 -->
## 1. What this list is for

**Aequitas is an economic system. It is not a software project.** A database schema, a storage design, a transport protocol and a choice of cryptography are all decisions for whoever builds the thing (Foundations §2.6, which sets out what these documents answer and what they leave to implementers).

**But somebody building a trust network has to know which system they are building.** This list is what they need: a set of statements that must be true of the finished thing. It never says how to build it.

> **An implementation is Aequitas if, and only if, every row in §2 holds.**

### Two tests every row on this list had to pass

**1. The dial test.** Turn any implementation choice to one extreme, then to the other. **If the rule is still true at both ends, the choice was not part of the rule.**

Worked: take *how much anyone can see*. At one extreme, every record is public. At the other, only machines ever read the ledger and no human does. **Mass still balances at both ends. A pledge is still backed one-for-one at both ends.** So conservation and pledge-backing are rules, and transparency is a dial. Transparency is not on this list; conservation and pledge-backing are.

**2. The have-versus-achieve test.** A row states something an implementation **has**. It never states something an implementation must **succeed at**.

Worked: *"records are never deleted"* is something you can read off an implementation — either there is a delete path or there is not. *"Essentials are affordable to everybody"* is not, because it depends on the value the network picks for its floor, the value it picks for its debit tolerance, and what its real economy can physically produce. **§4 records the two rules kept off this list on that ground.**

### The standing screen: assume the engineering works

**Read every proposed row against this stipulation:**

> **"Given a trust network with a secure database, 99.999% identity security, and practically unlimited storage…"**

**What survives is an accounting rule and belongs here. What dissolves was an engineering complaint.** *"That would be too much data"* dissolves. *"You could not prove one person holds one account"* dissolves. **Mass must still balance, and a pledge must still be backed one-for-one.**

---

<!-- tag: cnf-s2 -->
## 2. What an implementation must satisfy

**All thirty-seven rows below must hold.** They are grouped so a reader can find one without already knowing its number. **The numbers themselves have not changed and never will** — other documents cite them.

### The words this list uses

| Word | What it means |
|---|---|
| **Credit** | A record that a person spent an hour of their life working. It belongs to that person and never moves. |
| **Debit** | A record that matter or energy was taken from the world, together with who is holding the consequence. Nobody collects it and no account is ever settled. |
| **Weighting model** | The set of numbers that says what a kilogram of a substance, a joule, or a tonne of CO₂ costs in hours. **Each network runs its own.** |
| **Collapse** | Turning a debit's list of physical quantities into one comparable figure, by applying a weighting model. It happens when somebody asks, never in storage. |
| **Record** | A figure that came from an observation or an attestation. |
| **Estimate** | A figure that came from a published method, used where no record exists. **A record always beats an estimate.** |
| **The gate** | The rule `D ≤ ρ·C`. A person's debit `D` may not exceed their credit `C` times the network's debit tolerance **ρ** ("rho"). |
| **The floor**, `F` | The hours a day a network counts as the work of keeping a human being alive. **Each network sets its own.** |
| **Extent** | The piece of the world a figure is about — a region, a sector, a population. **Never the set of subscribers** (row 17a). |
| **Coverage** | The share of an extent's real material flow that a network's records actually captured. As a formula, `Y ÷ N`. |
| **`N`** | The total for the whole extent, measured by something that reaches **everybody in it**, subscriber or not — agricultural statistics, trade data, a satellite survey. |
| **`Y`** | What the network's own subscribers recorded. |
| **`Z`** | How many producers inside that extent are still unmeasured. |
| **`R`** | The leftover, `N − Y`. What was produced by people the network cannot see. |
| **`not identified`** | A label on a published figure meaning **"we cannot say which direction this is wrong in."** |

**A worked example of the last five.** A valley grows wheat.

| | |
|---|---|
| A satellite survey puts the valley's crop at | **`N` = 88,000 t** |
| The network's own farms recorded | **`Y` = 82,000 t** |
| So the leftover is | **`R` = 6,000 t** |
| And coverage is 82,000 ÷ 88,000 | **93%** |

**In plain words: the network can see 93 of every 100 tonnes that valley grew. Six thousand tonnes were grown by people it holds no records for.**

---

### 2.1 What a cost is, and what counts as work

| # | Requirement | From |
|---|---|---|
| 1 | **Every entry in the books records something physical that really happened.** A debit records matter or energy that moved. A credit records time a person spent. **Nothing is ever issued, printed, or created by declaring it** — there is no money, no token, and no unit anyone can make more of. | A1 |
| 2 | **A flow is recorded against whoever caused it.** Only people act, so a cost never lands on a tool, a machine, a company, or a buyer who did not do the thing. | A1, §3.2b, §4.5 |
| 2a | **A thing's cost figure contains only what that thing itself used up.** What it cost to build a barn stays with the barn and whoever holds it, and **is never spread across the beef the barn was used to produce.** The test is what physically happened to each input: **did it survive the process?** A drill bit that survives is equipment. The oil it burned is used up. **The producer does not decide which is which** — the record of what happened to each thing decides it, and row 7 checks that record. | A5, §4.5 |
| 2b | **Nothing is ever added on top of a cost figure.** No margin, no fee, no markup, no spread, anywhere, by anyone. | A5 |
| 2c | **A business is never the final holder of a debit. Only people are.** Whatever a business takes on is at every moment its workers' debit, divided by the hours each worked there. **Closing the business moves nothing and clears nothing.** | A1, §3.2c |
| 3 | **An hour is an hour, whoever worked it.** No profession, rank, skill or hazard multiplies it. Real differences between workers show up as **material costs** instead — the extra food a labourer eats, the harm a dangerous process is later found to have caused. | A2 |
| 3a | **Every activity a network credits is at least one of three things: production, a service, or enrichment.** An activity that is none of the three is not work, whatever the network has declared. **Which of the three it is, is never written down and never changes the number.** An hour that is more than one of them credits once. | §2.3, §4.5 |

#### Row 2a, worked

**A barn costs 20,000 hours to build and lasts 20 years. The farm produces 40,000 kg of beef over that time.**

| | Hours carried per kg of beef |
|---|---|
| What a critic expects: 20,000 ÷ 40,000 | 0.5 |
| **What the beef actually carries from the barn** | **0.0** |

**The beef did not build the barn.** The 20,000 hours sit on the people holding the barn, shared by how long each held it. Foundations §4.5 gives the full argument.

#### Row 2c, worked

**Ten people each work 2,000 hours in a year for one co-operative. That year the co-operative takes on 24,000 hours of debit.**

| | |
|---|---|
| Total member hours | 10 × 2,000 = **20,000 h** |
| Each member's share of those hours | 2,000 ÷ 20,000 = **10%** |
| Each member's share of the debit | 10% × 24,000 = **2,400 h** |

**Close the co-operative and open a new one with the same ten people. Each still carries 2,400 h.** Do it ten times and each carries 24,000 h. **The count never resets.**

---

### 2.2 What moves between people, and what never does

| # | Requirement | From |
|---|---|---|
| 4 | **Credit never changes hands** — not by gift, sale, loan, inheritance, or theft. **Only debit moves, and only by handing over the thing it is attached to.** | A3 |
| 4a | **A figure computed under one network's weighting model is never converted into another's.** A second network re-computes the claim itself, from the same physical record, through its own model. **No exchange rate between two networks' credit exists anywhere in the implementation, and two networks' figures are never added, netted, or set side by side as though they were one quantity.** | A3, §4.2, §4.0, §5.6 |
| 7a | **A thing has exactly one holder at any moment, and every change of holder is a recorded event.** This is what lets debit follow possession. | A5, A1, §3.2, §3.2b · *IC-5* |

#### Row 4a, worked

**One person works 8 hours on a Monday and holds an account with two networks.**

| | Network A | Network B |
|---|---|---|
| The floor `F` | 4 h/day | 10 h/day |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| Debit-room at ρ = 1.2 | 1.2 × 12 = **14.4 h** | 1.2 × 18 = **21.6 h** |

**Both figures are correct. Neither breaks row 8**, because 12 and 18 are each under 24 and row 8 applies to each account on its own.

**The forbidden line is `14.4 + 21.6 = 36.0`.** A and B run different weighting models, so the same physical basket collapses to a different number in each. **Adding them sets one A-hour equal to one B-hour, and that is an exchange rate.** The two numbers are not two measurements of one quantity. **They are one physical fact read through two models, and there is no third model to express a sum in.**

---

### 2.3 How the record is kept

| # | Requirement | From |
|---|---|---|
| 5 | **A person's standing is never stored. It is computed from the event log every time anyone asks.** The log holds physical quantities only — kilograms, joules, hours — **never a price, a weight, a cost, or a value.** The cost is produced at the moment somebody reads the log, by applying the weighting model then in force. | A6, A5 |
| 6 | **No record is ever deleted or edited.** A record found to be wrong gets a dated, attributed note appended saying so. A record with something better gets the better one added beside it. **Both stay.** | §4.4, §4.8 |
| 11 | **The gate is checked at the moment of the transaction.** A later correction changes how much room a person has in future. **It never makes a completed purchase invalid.** | §3.3 |
| 17b | **When a cost constant, a joint split, or a coverage figure improves, every affected record in history is recomputed.** A figure is a dated reading, never a verdict. **This changes future room only, and never the validity of a completed act** (row 11). | A4, A6, §3.3 |

---

### 2.4 The arithmetic that must always hold

| # | Requirement | From |
|---|---|---|
| 7 | **Matter and energy balance across every recorded process**, within a stated tolerance and at one level of detail. **Everything the books track has a beginning and an end.** It came from an extraction, or from an estimated entry for something that already existed when the books started; and at any moment it is **held by somebody, used up, or released to a named place in the world.** **A thing with neither a beginning nor an end is reported as *unaccounted*, never left out.** Nothing is recorded as used before it exists or after it is gone. | A1, A4 · *IC-1, IC-2, IC-3, IC-4, IC-6* |
| 8 | **No account claims more than 24 hours of activity in 24 hours.** | A2, §5.5.5 · *IC-7* |
| 9 | **A person's pledges never exceed the credit they have earned in their life, one hour for one hour.** The budget is spent **when the pledge is made**, not when the work happens, **and there is no path that gives it back.** | §4.6 · *IC-8, IC-9* |
| 10 | **A debit is a list of physical quantities, not one number.** Any division — across co-products, across a team, across anything — **is computed on each quantity separately, before they are combined into one figure.** | §3.2a |
| 10a | **A joint process's debit divides by where the process physically sent its inputs**, measured at that facility, for the period being described. A model is used **only** where measurement is missing. **The method is published with its version number**, so anyone can re-run it. **A split may never depend on demand, desirability, or yield.** Which method suits an industry is that industry's to settle, not this document's. | §3.4a, §2.6, §4.7 |
| 10b | **No output's share of any quantity is negative.** A negative result is a measurement error or a badly drawn process boundary — never a thing containing less than nothing. | §3.4a · *IC-10* |
| 10c | **For each quantity, the outputs' shares add up to exactly what went into the process.** Nothing is created or lost in a split. | §3.4a · *IC-11* |
| 10d | **Splitting a process stage by stage gives the same answer as splitting it whole**, and a divided estimate's parts add up to the coarser figure they came from. **This is what makes a redrawn boundary show up as an arithmetic disagreement rather than an argument.** | §3.4a, §4.4 · *IC-12* |

#### Row 9, worked

**A resident has earned 4 hours of credit in their life. They pledge 2 hours toward mowing the public verge.**

| | |
|---|---|
| Lifetime earned credit | **4 h** |
| Pledged so far | **2 h** |
| Still available to pledge | **2 h** |
| Someone mows for an hour and is credited | **1 h** |
| Pledge budget returned to the resident | **0 h** |

**One pledged hour remains against the mowing, and the resident's remaining budget is still 2 hours.** The mower's credit was created by the work, not taken from the pledger. **Spending the budget is permanent, which is what makes pledging a real sacrifice.**

#### Rows 10 and 10a, worked

**A farmer spends 8 hours on one steer. The animal yields beef, hide, tallow and bone.** The hours left no physical trace saying which output they went to, so they follow the material split, which was measured.

| Output | Measured share of the feed | Hours it carries |
|---|---|---|
| Beef | 78% | 6.24 h |
| Tallow | 9% | 0.72 h |
| Hide | 7% | 0.56 h |
| Bone | 6% | 0.48 h |
| **Total** | **100%** | **8.00 h** |

**The farmer is credited 8 hours whatever the split says** (row 3). The split decides only what each output's debit-cost reads.

---

### 2.5 What a figure must say about how sure it is

| # | Requirement | From |
|---|---|---|
| 12 | **Every estimate says four things about itself: what it is based on, what method produced it, when it was made, and what extent it covers.** It may be replaced only by something with a **stronger** basis, never a weaker one. **An observation may replace an estimate. An estimate may never replace an observation.** | §3.3, §4.4 |
| 12a | **How sure a figure is, is stated separately from how it was arrived at, and carries the name of whoever assessed it.** A confidence figure with nobody's name on it is an authority nobody can question. **How sure a figure is, is never read off its method** — a well-tested model can beat a badly calibrated meter. | A8, §4.4 |
| 12b | **Being precise about a group does not make you precise about a member of it.** Taking a figure from a coarse claim down to a fine one **lowers** how sure the fine figure is. A perfectly metered factory-month says very little about any one item that left the factory. | §3.4, §4.4 |
| 12c | **Every record names the evidence it came from, and that name is stored with the record.** It names **which published evidence rule the record satisfied** (row 16d), not free text. **A record whose only backing is the claimant's own word says so**, and is a record of an assertion rather than of an observation. **This does not gate recording** — the event is logged either way; the pointer says what stands behind it. | A1, §4.2, §4.4 |
| 13 | **A quantity counted over incomplete coverage is published as a `floor`** — the true number can only be higher — **with the gap named.** **A quantity worked out by combining two incomplete readings is published as a range, labelled `floor`, `ceiling`, or `not identified`.** **`not identified` is what such a figure gets** until somebody states an argument about the blind spot in **each** input. **A `floor` label is never inherited just because an input was incomplete.** | §4.4 |
| 14a | **Two figures are subtracted only when they measure the same quantity, over the same extent, over the same stretch of time, and their error bars are smaller than the difference between them.** Where that does not hold, the answer is published as a **range** — `R ∈ [N_L − Y_U, N_U − Y_L]` — with the mismatch named, and never as a single bound. | §4.4 |

#### Row 12c, worked

**A network publishes two evidence rules: translation needs the text plus a client confirmation; unwitnessed thinking-time is recorded on the claimant's word alone.**

| The record | What it points at | What it is |
|---|---|---|
| 20 h of translation, text delivered, client confirmed | **rule TRANS-2** | a record of an **observation** |
| 20 h of thinking, no text, no witness | **rule SELF-1** | a record of an **assertion** |

**Both are in the log. Neither was refused at the door.** The difference is that a stranger reading the second one **knows what stands behind it without being told**, and a network weighting it near zero (Foundations §4.5) is applying a published rule rather than a private judgement.

> **What this rules out: a record that is silent about its own backing.** Without the pointer, the two rows above are the same twenty hours, and the only party who knows the difference is the network.

#### Rows 13 and 14a, worked

**Published figures: `N` = 88,000 t and `Y` = 82,000 t, so `R` = 6,000 t. Which figure is blind decides which way that 6,000 t is wrong.**

| Which input is blind | What is really true | True `R` | So 6,000 t is |
|---|---|---|---|
| **`Y` under-records** by 4,000 t | `Y` = 86,000 t | **2,000 t** | a **ceiling** — the published figure is **three times the truth** |
| **`N` under-observes** by 10,000 t | `N` = 98,000 t | **16,000 t** | a **floor** |

**Same printed figure, same incompleteness, opposite labels.** This is why a subtraction cannot inherit a floor label from its inputs, and why `not identified` has to be available as an answer. **An implementation with no way to say *"I cannot tell which direction this is wrong in"* will label everything, and the labels will be wrong in the direction that flatters it.**

---

### 2.6 Counting what the network cannot see

| # | Requirement | From |
|---|---|---|
| 14 | **An unmeasured producer's estimated share is worked out over the producers still unmeasured, never over everybody**, and it comes from a production model for their occupation, region and known activity. **The leftover `R` is never divided by a count of producers.** Two worlds with different truths hand one network identical books, so no per-head figure computed from those books can describe either. | §4.4, §4.1 |
| 14d | **Where a network works an estimate out over a measured extent** — hectares, vessel-days, throughput — **it publishes that extent register as unaudited.** Honest error in an extent reading barely moves the estimate. **A producer who deliberately declares half their real extent returns it to the accuracy of the rule this replaced.** Whether the survey behind `N` catches that has been argued and never tested. | §4.4, **OP-28** |
| 14b | **A coverage figure rests on a measurement that reaches past the network's own membership** — a physical stock somebody went and measured, or an independently known total `N` for the whole extent. **Adding up subscribers' own records proves the books are *consistent*.** **It can never prove they are complete**, because a producer nobody recorded is missing from both sides of every internal sum and every sum still balances. **A coverage figure with nothing behind it that reaches non-subscribers is published as `not identified`.** | §4.4, §4.3, A7 |
| 15 | **The leftover `R` is computed, published, and charged to no account** until the person who caused it joins. | §4.4 |
| 17a | **Every human inside the extent the books claim to cover is in those books, subscriber or not**, with credit **and** debit estimated on both sides. **The extent is a region, a sector or a population — never the set of subscribers.** A non-participant can **neither draw on that position nor be charged for it.** A position starts acting on what a person may consume **only** once they hold a verified account and observations have replaced the estimates. | A7, §4.1, §4.4 |

#### Row 14b, worked — why evidence quality is not the same as reach

**A valley has 100 farms. Eighty of them subscribe to the network, and every one of those eighty keeps perfect records** — weighbridge tickets, buyer receipts, the lot.

| | |
|---|---|
| The eighty subscribers' records add up to | **82,000 t** |
| Quality of the evidence behind every one of those records | **perfect** |
| What the network could publish from its own books alone | *"coverage: 100%"* |
| What the satellite survey says the valley actually grew | **88,000 t** |
| Grown by the twenty farms that do not subscribe | **6,000 t** |

**No improvement in the eighty farms' evidence will ever reveal the twenty.** A measurement that only reaches members can only ever describe members. **This is A7 in arithmetic form, and it is the same rule row 17a states in words:** the extent is the valley, not the membership.

> **One witness in Foundations §4.4 does not appear in this row, and the omission is deliberate.** A **counterparty's own record** catches a hand-off one side failed to write down, because a hand-off has two sides. **It cannot establish coverage**, because a counterparty inside the network is itself a subscriber. **It is a check on flows between accounts, not a measurement of an extent.**

#### Rows 14 and 14d, worked

**Twenty unmeasured farms are left. The leftover is 6,000 t, and the same survey measured their land at 5,000 hectares.**

| | |
|---|---|
| The leftover's rate over measured extent, 6,000 ÷ 5,000 ha | **1.2 t/ha** |
| A 600-hectare farm's estimate | **720 t** |
| A 100-hectare farm's estimate | **120 t** |
| **What the withdrawn per-head rule gave each of them** | **300 t** |

**Both methods add to 6,000 t across the twenty. Only one of them describes a farm.**

**Now watch the pool as producers leave it. Five of the twenty install scales. They hold 1,000 hectares and record 1,000 t.**

| | |
|---|---|
| New leftover | 6,000 − 1,000 = **5,000 t** |
| Extent still unmeasured | 5,000 − 1,000 = **4,000 ha** |
| **New rate** | 5,000 ÷ 4,000 = **1.25 t/ha** |
| The 600-hectare farm's estimate now | **750 t**, up from 720 |

**The five that came forward produced less per hectare than the pool assumed, so the fifteen who stayed carry more.** Staying unmeasured gets worse the longer it lasts, and nobody had to enforce anything.

> **⚠️ Row 14d is why the right-hand figures are not settled.** The 5,000-hectare reading is a declaration a network holds and nobody has shown how to audit. **A farm declaring 300 hectares instead of 600 halves its own estimate and pushes the difference onto its neighbours**, and the arithmetic above cannot see it.

---

### 2.7 What the network must publish

| # | Requirement | From |
|---|---|---|
| 16 | **Every estimating number and every method the network uses is published**, so anyone can re-run it. **Every published figure states the extent it covers**, so a bare *"passed"* is never a result. | §4.7, §4.3 |
| 16a | **Every cost constant carries its method, its version, and its uncertainty interval**, and the network **states which constants it has not reviewed, and how old each reading is.** | §3.3a, §4.4 |
| 16b | **A constant may re-weight history only after two unaffiliated replications.** Which constants get reviewed is decided by **how large the figure is, multiplied by how concentrated its beneficiaries are** — never by size alone. **Membership composition is public**, so a network concentrated in the sector it audits can be spotted from outside. | §3.3a |
| 16c | **The network can show how it audits its cost constants.** *How* it does so is its own design (§2.6). **Having no answer is not conforming.** | §3.3a, §2.6 |
| 16d | **For every kind of work it credits, the network publishes what evidence that work requires, before crediting any of it.** **It credits no kind of work for which it has published no rule.** *Which* kinds it covers is its own choice (§2.6, A8). **Having no published rule for something it credits is not conforming.** | §4.2, §4.5, §4.7 |

#### Row 16b, worked — why size alone is the wrong trigger

**A network reviews any constant whose effect exceeds 5,000 hours across its books.**

| | Total effect | Who benefits | Reviewed? |
|---|---|---|---|
| Constant A, understated | 6,000 h | spread across 300,000 subscribers | **Yes**, on size |
| Constant B, understated | 4,000 h | **one producer** | **No**, on size alone |

**An attacker's job under a size-only rule is to keep each falsification just under the threshold.** Multiplying by concentration of beneficiary fixes it: constant B's 4,000 hours landing on a single party outranks constant A's 6,000 hours spread across 300,000.

#### Row 16d, worked

**A network publishes its rule for translation work: the translated text exists, and the client confirms receiving it.**

| | Hours worked | Against the published rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation, client confirms | 20 h | met | **20 h** |
| **B** asserts 20 hours, with no text and no client | 20 h | not met | **0 h** |

**B is not being judged and B is not being punished. B knew the rule before starting.** And if translating for someone who cannot confirm is work this network wants, **it writes a rule for that case — after which B's 20 hours credit at 20 hours**, not at some fraction because a vague claim was weighted cautiously.

---

<!-- tag: cnf-ic-labels -->
### The `IC-n` labels

**Twelve of the rows above are arithmetic the ledger must never violate.** They have been cited as `IC-1` to `IC-12` since 2026-07, and **those labels stay valid** so older citations still resolve.

| Label | What it is | Row |
|---|---|---|
| **IC-1** | Mass balance | 7 |
| **IC-2** | Energy balance | 7 |
| **IC-3** | Everything has a beginning | 7 |
| **IC-4** | Everything has an end | 7 |
| **IC-5** | One holder at a time | 7a |
| **IC-6** | Nothing is used before it exists | 7 |
| **IC-7** | **The 24-hour cap** | **8** |
| **IC-8** | Pledges are backed one-for-one by earned credit | 9 |
| **IC-9** | A spent pledge budget is never returned | 9 |
| **IC-10** | No negative share | 10b |
| **IC-11** | Shares add up to what went in | 10c |
| **IC-12** | Boundary additivity | 10d |

**Two more were proposed, tested, and rejected on 2026-08-22.** *IC-13 (genesis admissibility)* refused the ordinary case of somebody joining, and was satisfied trivially by whichever network was founded most recently. *IC-14 (citation closure)* demanded **a** citation rather than a **true** one. **Both checked a self-asserted field against a constant, where every surviving constraint checks one recorded quantity against another.**

---

<!-- tag: cnf-s3 -->
## 3. What this list does not carry

| Not here | Where it belongs |
|---|---|
| Field names, record shapes, schema versions | The implementer |
| Storage, indexing, backups, key management | The implementer (§2.6) |
| Transport protocol and choice of cryptography | The implementer (§2.6) |
| Privacy practice | A network choice (§4.7) |
| The values of ρ and the floor `F` | Network dials (§3.5, §5.5.3, A8) |
| Corporate form, jurisdiction, compliance posture | The implementer (§2.6) |
| **How a network schedules, staffs or samples its checking** | The implementer (§2.6) |
| **What a verification rung costs to run** | **Already in the log.** Audit work is credited work, so those hours are events and a query returns them (§4.7). **A separate published cost figure would be a summary table, and a summary table is database design.** |

---

<!-- tag: cnf-not-requirements -->
## 4. Two things that are deliberately not on this list

**A row here states something an implementation *has*. It never states something an implementation must *succeed at*.** That difference decides what belongs.

### Essential provision is not a requirement

**Foundations §5.5.4 says essentials are affordable to everyone alive**, because the floor credits the hours of staying alive and is set large enough to cover what staying alive costs. **That is true of the system. It is not a test an implementation passes.**

There was a row 17 saying so, from Foundations v0.18 to v0.23 and briefly here. **It was deleted on 2026-08-25 by author ruling**, on this ground:

> **Requiring it would be like saying that to conform to Aequitas, a network must succeed at a stated political goal.**

**Whether essentials are actually affordable in a given network depends on three things this list cannot read:** the value that network sets for `F`, the value it sets for ρ, and what its economy can physically deliver. **All three are dials or physical facts** (Foundations §5.5.3, A8). **A network can be built exactly to this list and still set `F` too low, and no reading of its code would say so.**

**Nothing is lost from the theory.** The rule stands in Foundations §5.5.4 as a statement of how the system works. **Setting `F` and ρ so that it comes true is the network's job**, and finding a stable band for the two is **OP-4** in the objections register.

*(Row **16c** is the closest call on this test — *the network can show how it audits its cost constants* — and it survives, because showing a design is something an implementation either does or does not do. It never requires the audit to work.)*

### "One verified human = one account" is not here either

Foundations §4.1 states it, and the **OP-22 ruling of 2026-08-25** makes it a rule each network applies to its own members rather than one holding across networks. **So it stays in Foundations and is deliberately absent here.** Record: [`OP-22_identity_not_disclosure_v0.2.md`](open-problems/OP-22_identity_not_disclosure_v0.2.md).

---

<!-- tag: cnf-s5 -->
## 5. Why six of these rows exist

**Most rows restate something Foundations argues at length, and the *From* column points at the argument.** Six rows need a note here, because what they rule out is not obvious from reading them.

> **The finding underneath the first five: a rule that lives only in prose does not bind.** Foundations §4.2's sentence about exchange rates was in front of the reader who broke it. **This list is not a summary of Foundations. It is the part of Foundations that has to survive contact with somebody in a hurry.**

### 4a — what an implementation could have done without it

**Satisfy every other row and still publish a conversion table between its own credit and a neighbouring network's.** That creates a medium of exchange — the one failure mode Foundations §5.6 says Aequitas is structurally immune to, and the substantive reason it must never be called a currency. **A project paper made exactly that error on 2026-08-27 and it was refused the same day.** The worked case is under row 4a above.

**Why it is numbered 4a.** Row 17 was deleted by author ruling and its number is retired, so re-using it would make two different rules share one label across versions. **4a sits beside row 4 because both come from A3:** credit does not move between people, and a position does not move between models.

### 17a — what an implementation could have done without it

**Account only for its own subscribers.** Rows 14 and 15 govern the leftover once a network estimates one, but **no row required a network to have non-participants in its books at all.**

**One phrase in the drafting mattered.** An earlier wording said *"within the extent the implementation's books claim to cover"*, which a network could satisfy by **declaring its extent to be its own membership** — `N` would equal `Y`, the leftover would be zero, and a real 6,000 tonnes would sit outside the accounting. **That is the "outside" A4 says there is none of.** So the row names what an extent may be: a region, a sector, or a population.

### 17b — what an implementation could have done without it

**Freeze its weighting model forever.** Row 5 makes recomputation *possible*; rows 11 and 16b both *assume* it happens. **No row required that a better constant actually re-weighs history**, while A6 says improving the science re-weighs everything and A4 reaches consequences discovered decades later.

**It does not weaken the two rows that constrain recomputation.** Row 16b still requires two unaffiliated replications before a constant may re-weight history. Row 11 still says a re-weight changes future room and never the validity of a completed act.

### 16d — what it removes

**The worry it answers:** row 9 bounds a person's lifetime pledging power by their lifetime *measured* credit, and Foundations §4.5 weighs unwitnessed work near zero until something corroborates it. **Put together, a person whose work a network measures badly would get little credit and little voice, with nobody having agreed to it.**

**16d removes the case rather than softening it.** A kind of work is either covered by a published rule — in which case evidence exists and the hours credit in full — or it is not covered, and nobody was promised credit for it. ***"Credited but measured badly"* is not a state this design produces.**

**Three things bound what it costs a person.** Self-care is verified by proof of life, which every living human meets at almost no cost (Foundations §4.2). Sellers choose which networks they accept (§4.0), so bad rules lose a network its members. And non-participation is always available (§4.8).

### 12c — what an implementation could have done without it

**Record everything and say nothing about why any of it was believed.**

**The gap was one word in row 16.** It requires every estimating number and method the network **uses** to be published. **A record is not an estimating number**, and nothing anywhere required a record to carry a pointer to its own evidence. Row 12 covers **estimates** only. Row 16d says what evidence a **kind of work** needs, in advance, but never ties an individual record back to the rule it satisfied.

> **So an implementation could hold a twenty-hour record backed by a client confirmation and a twenty-hour record backed by nothing, store them identically, and conform.** The only party able to tell them apart is the network.

**It is not a new burden.** Row 16d already makes the network publish the rule before it credits anything, so the rule the record satisfied is a value the network already had. **12c requires it to be written down.**

**And it does not gate recording.** Foundations §4.6 says the work is always recorded and §4.4 says a falsehood is made permanent and traceable rather than prevented at the door. **12c adds a field, never a refusal.**

### 3a — what an implementation could have done without it

**Declared *"loyalty to this network"* creditable**, published an evidence rule for it under 16d, credited it at one hour per hour under row 3, and satisfied every other row. **16d requires a published rule. It never required the thing being credited to be work.**

**A8 already names the always-creditable list as a capture surface** and leaves *which* activities a network credits to the network. **Row 3a does not touch that.** It fixes the outer boundary and leaves every choice inside it where A8 put it.

> **⚠️ The honest limit. Enrichment is broad, so 3a is a weak filter rather than a tight one.** A network determined to credit something worthless can argue it is enrichment. **What the row rules out is the plain case** — crediting loyalty, crediting holding an asset, crediting being popular — **and those are the cases that turn a network into an issuer.** The rest of the defence is structural and written elsewhere: competing networks and ratio-based evaluation (Foundations §3.5), and public membership composition (row 16b, Foundations §3.3a).

---

*End of v0.10.*
