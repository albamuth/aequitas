<!-- tag: s5-rewrite-draft -->
# Foundations §5 — clarity rewrite, DRAFT

> **Version:** 0.1 · **Date:** 2026-08-25
> **What this is:** a replacement for **§5 of `Aequitas_Foundations_v0.22.md`**, written to the document standard set in v0.22 — state the rule, define every term where it is first used, show it working with numbers, stop.
> **Why:** author ruling, 2026-08-25. *"The whole of section 5 is still written as if Aequitas was a coordinated organization, but really section 5 is about the praxis implemented by a trust network."* Full ruling: [`OP-22_identity_not_disclosure_v0.1.md`](OP-22_identity_not_disclosure_v0.1.md) §8a.
> **Scope of this draft: §5.0 (new) through §5.1d.** §5.2 to §5.5 are the next chunk and are **not** in this file.
> **Nothing is dropped.** Every rule, condition, worked example and warning in the current §5.1–§5.1d appears below. What changed is the wording, the ordering, and the framing.

---

<!-- tag: fnd-s5 -->
## 5. Identity, Coverage, and Onboarding

<!-- tag: fnd-s5-0 -->
### 5.0 What this section is about, and who does the things in it

**This section describes work that a trust network does.** Nothing in it is done by Aequitas, because **Aequitas is not a body and cannot do anything** (§1.2). It is a set of principles about how cost is counted, in the same way that capitalism is a set of principles about how value moves. Banks and firms carry out capitalism. **Trust networks carry out Aequitas.**

**Terms used in this section.**

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods so that others can re-run them. |
| **Subscriber** | A person who holds an account with a trust network. |
| **Event log** | The permanent, append-only record of what happened, from which every position is computed (§3.1, A6). |
| **Estimate** | A figure computed from a published method where no direct record exists. |
| **Record** | A figure taken from an observation or an attestation. A record always beats an estimate (§5.1a). |
| **Onboarding** | The act of a person joining a trust network, which replaces estimates about them with records. |
| **The floor**, written `F` | The hours a day a network counts as the work of keeping a human being alive — sleeping, eating, defecating, keeping clean. The network sets the list and the hours (§7.5.1). |

**Read every rule below as a rule a trust network applies to its own subscribers and its own books.** Where a rule reaches across two networks, this section says so explicitly.

#### Networks keep separate books, and no book is ever added to another

> **Each trust network keeps its own event log. A network's books are never summed with another network's books, because there is nothing that would be summing them.**

Networks are **laboratories, not banks** (§5.3c). Their business is getting the numbers right. They frequently draw on the **same underlying evidence** — a haulier's logistics database, a published scientific paper, a government agency's survey — and it is in every network's interest when they do, because a method that catches a fault in one network's books catches it in the other's.

**What a subscriber sees is one network's best current approximation of the truth**, presented by something shaped like a payment-card application.

#### A transaction happens on exactly one network, and the seller chooses which

A seller decides which networks they will accept, the same way a shop today decides which card schemes it takes. *"We do not take Network B here"* is an ordinary sentence. **The seller's reasons are their own** — they may think B's floor is set too high or too low (§7.5.3), or that B's identity check is too weak.

**That preference is how networks compete for subscribers**, and it is the whole of the discipline on a network's settings. **The transaction is recorded on the accepted network and is absent from the other.**

**A network can also simply end.** If Network A collapses while Network B continues, the transactions recorded only in A are **forgotten**, unless B recovers A's database. Recovering it is the same act as a merge in which all of B's rules were kept (§5.3c).

---

<!-- tag: fnd-s5-1 -->
### 5.1 One account per person, and coverage that does not require consent

#### The two rules

> **1. Within a trust network, one verified human holds exactly one account.**
> **2. Participation is voluntary. Coverage is not.**

**Rule 1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists. A network needs it because an account is where credit accrues and where the consumption gate `D ≤ ρ·C` is checked; two accounts for one person would check the gate twice against one life. **Resisting this is called Sybil resistance**, after the practice of one person presenting as many, and how a network achieves it is that network's design (§4, the verification ladder).

**Rule 2 means a network estimates the people it cannot see.** Leaving a non-participant out of the books entirely would produce a false record — wheat with no grower — so a network estimates both sides of their position:

| | Estimated from |
|---|---|
| **Debit** | The average for their demographic cohort, computed **excluding** registered subscribers. A public figure is estimated from publicly known holdings. |
| **Credit** | A cohort production model — occupation, region, known activity — computed **excluding** measured producers (§5.1b). |

> **A non-participant can neither draw on their estimated position nor be charged for it.** The estimate is a statement about material flows in the world. It is not a claim on the person, and the person has no claim from it.

#### Why one account per person survives the weakest possible technology

**The rule has to hold on the bottom rung of the verification ladder** (§4, level 1) — people writing in a notebook or a spreadsheet, all of whom know each other. That is where it looks most fragile, so that is where to test it.

**The only way it fails there is a pair of identical twins who deliberately engineer the confusion.** And the arithmetic already refuses it.

##### An example, with the numbers

Twins T1 and T2 each work **8 hours** a day. Their network counts **10 hours** a day as the work of staying alive (§6.1b).

| | T1 claims | T2 claims | Family total |
|---|---|---|---|
| **Honest** | 8 + 10 = **18 h/day** | 8 + 10 = **18 h/day** | **36 h/day** |
| **Faked** — T1 takes both twins' work | 16 + 10 = 26 h → **refused** | 0 + 10 = **10 h/day** | — |
| **Faked, at the most that is allowed** | 14 + 10 = **24 h/day** | 0 + 10 = **10 h/day** | **34 h/day** |

**IC-7 caps any account at 24 hours of activity per 24 hours** (conformance requirement 8). T1 cannot hold 16 worked hours plus a 10-hour floor, because that is 26 hours in a 24-hour day. The most T1 can claim is 14 worked hours.

> **The twins lose 2 hours a day by pretending to be one person — 730 hours a year.**

**T2 keeps accruing the floor either way**, because T2 is alive and is therefore doing the work of staying alive, whatever else they do or fail to do (§6.1b, §7.5.2).

**And there was nothing to win.** Twins sharing a household share the goods, so one twin holding the credit while the other holds the debit reaches the same family position as reporting honestly. **The fraud costs 730 hours a year and buys nothing.**

#### One person, two networks

**A person may hold an account with more than one trust network.** They are two subscriptions, not two lives, and they are not fraud: each network verified a real human and gave them one account, which is exactly what rule 1 requires.

**The two books are not reconciled, and they are not summed.** Each network computes that person's position from the evidence it holds, through its own settings. **Two networks with different settings will report different figures for the same day, and both figures are correct.**

##### An example, with the numbers

One person works **8 hours** on a Monday. They hold an account with each of two networks.

| | Network A | Network B |
|---|---|---|
| The floor `F` | **4 h/day** | **10 h/day** |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| That network's own absolute maximum spread, 24 ÷ `F` | 24 ÷ 4 = **6.0×** | 24 ÷ 10 = **2.4×** |

**Read the last row as a wall, not as an expected outcome.** Reaching it takes 24 credited hours every day of a whole life. **A very hard working life reaches about 1.6× a life spent only staying alive** (§7.5.5).

**Neither network converted the other's figure.** Each read the same physical facts — eight hours worked, one human alive — through its own model. This is §6.4b, **comparison, never conversion**: a counterparty re-computes a claim through its own weighting model rather than importing a number.

**A purchase clears against one book only.** If the seller takes Network A, the gate `D ≤ ρ·C` is checked against A's figures and the event is recorded in A's log. B never sees it. **The same purchase might clear on one network and be refused on the other**, because the two use different floors and different values of ρ.

**Nothing about that is unresolved.** Where a network's records are partial, it publishes a coverage figure saying so (§5.1c), and where a subscriber leaves activity undisclosed, the network estimates it over the undisclosed residual and errs against them (§5.1d). **The gap is measured and declared. It is not hidden.**

---

<!-- tag: fnd-s5-1a -->
### 5.1a How an estimate becomes a record

**A position is realizable — able to act on what a person may consume — after two things are true.**

1. **The person holds a verified account** with the network (C6, identity).
2. **The estimate has been superseded by observation.** A record replaces an estimate; **an estimate may never replace a record.** This one-way rule is called **monotonicity**.

> **Assertion is not evidence.** Saying a figure is so does not make it a record.

#### The floor rule — the second one-way axis

**Monotonicity governs *basis*: how well a thing is known. The floor rule governs *extent*: how much of the world was looked at.**

> **A quantity computed over incomplete coverage is a floor, never a value.**

Under-recording can only understate a total, so a figure computed from a partial record is a **lower bound** on the true one, and better coverage moves it in one direction only: up. **A partial input downgrades a claim rather than invalidating it.** Where the evidence that would establish closure is missing, the figure is reported as a floor with the gap named (EventLog §7.4).

#### Records are annotated, never deleted

**A record is never purged and never edited.**

- A figure later found wrong is **contested** — a dated, attributed, appended note carrying its own provenance.
- A figure with a better replacement is **superseded** — the better record is added beside it.

**Falsehood is not prevented at the moment of writing. It is made permanent, traceable, and arithmetically exposed the moment any part of its extent is measured** (EventLog §7.2a, §8.2a). This is how a scientific literature handles a wrong result, and it is the only method that does not need an authority standing at the door deciding what may be written down.

---

<!-- tag: fnd-s5-1b -->
### 5.1b The residual rule — an average covers only what was not measured

#### The rule

**A producer nobody has measured still produced something, and the books have to say how much.** The answer is not the average producer's output. It is what is left over once the measured producers are subtracted.

> **estimate = (N − Y) ÷ Z**
>
> **N** — the independently known total for the whole extent. Agricultural statistics, trade data, a satellite survey.
> **Y** — what the measured producers actually recorded.
> **Z** — the count of producers still unmeasured.

#### Why it is the residual and not the whole population

**Compute the estimate over the whole population instead, and the rule creates adverse selection.** Producers who are better than average install instruments to prove it. Producers who are worse than average stay dark and are handed an average that their own absence pushed upward.

**Computed over the residual, the estimate gets *worse* for those who remain as good producers leave the pool.** Darkness stops paying, and stops paying more the longer it lasts.

#### Three conditions

1. **An independently known *N* must exist.** It does for major commodities and does not for everything.
2. **The count *Z* must be defensible.** Under-counting dark producers overstates each one's share.
3. ***N* and *Y* must measure the same quantity, over the same boundary, over the same window, with error bounds small enough that the difference between them is real.**

> ### 📦 WHY THE TWO NUMBERS MUST MATCH BEFORE YOU SUBTRACT
>
> **You may only subtract two numbers that measure the same thing.**
>
> `R = N − Y` looks like arithmetic. It is not arithmetic until four things are true.
>
> | Must match | The question it answers |
> |---|---|
> | **The quantity** | Do both numbers count the same stuff, in the same unit? |
> | **The boundary** | Do both numbers cover the same piece of the world? |
> | **The window** | Do both numbers cover the same stretch of time? |
> | **The error bounds** | Is the difference bigger than the doubt in the two numbers? |
>
> **If any one of these fails, `R` is not a residual.** It is two different measurements pushed together, and the gap is an artefact of the mismatch.
>
> #### An example, with the numbers
>
> A region reports its wheat.
>
> - **N** = 100,000 tonnes — a satellite survey of the whole region, for the 2026 year.
> - **Y** = 82,000 tonnes — recorded by the farms inside the network.
> - **R = 100,000 − 82,000 = 18,000 tonnes**, said to be grown by dark farms.
>
> Now check the four rows.
>
> | Check | What is actually true | Effect on R |
> |---|---|---|
> | Quantity | *N* is **harvested** grain. *Y* is grain **sold**. The farms kept 6,000 t for seed and feed. | R is **6,000 t too big** |
> | Boundary | The satellite covers the whole valley. The network's farms are in the **upper valley only**. | Not comparable at all |
> | Window | *N* is the **crop year**. *Y* is the **calendar year**. | Two months counted wrong |
> | Error bounds | The satellite figure is ±12%, which is **±12,000 t**. | R = 18,000 ± 12,000 |
>
> **Read the last row on its own.** The residual is 18,000 tonnes and the doubt is 12,000 tonnes, so the true residual is somewhere between **6,000 and 30,000 tonnes**. A five-fold range is not a finding.
>
> **Now fix the four rows.** Use sold grain for both. Use the upper valley for both. Use the crop year for both. Use a survey with ±3% error.
>
> - **N** = 88,000 t ± 3,000
> - **Y** = 82,000 t
> - **R = 6,000 t ± 3,000** — between 3,000 and 9,000 tonnes.
>
> **That is a residual.** It is smaller, it is honest, and it can be acted on.
>
> **Note what happened to the number.** The unchecked residual was 18,000 t and the checked one is 6,000 t. **Skipping this check made the dark pool look three times larger than it is**, and every dark producer's estimated share with it.

**Where the check happens.** Both *N* and *Y* already carry the fields this needs — extent, vintage and error bounds sit in the provenance block that every estimated record must have (EventLog §4.1a). EventLog §7.2a carries the check.

**What to publish when the check fails.** A mismatch downgrades the claim rather than invalidating it, exactly as the floor rule downgrades a partial count. **Report the residual as a lower bound, and state the boundary and window actually observed.** A residual is attributed to a named person only on attribution evidence, never on membership of a cohort (§5.1c).

#### The closure witness

***N* is a closure witness: a physical total measured outside the ledger and reconciled against the ledger's own sum.** It asserts nothing about anyone's honesty. Anyone holding the same instrument computes the same residual.

**The same reconciliation runs on any conserved quantity against any physical reservoir**, and §3.3's ambient-stock measurement is already such a reading — it has simply been used as an input to a weight rather than as a statement about coverage.

| Flow type | Closure witness | Authority required |
|---|---|---|
| account → account | **The counterparty.** A hand-off has two sides, so a one-sided omission dangles on the other party's record. The witness is a party with the opposite interest. | None |
| account → commons | **The reservoir stock.** Measured depletion or accumulation, minus the sum of recorded flows. | None — an instrument |
| a fully disjoint chain | **(N − Y) ÷ Z.** No shared edge and no shared parcel, so only an independent total can see it. | None — an instrument and a tally |

> ### 📦 THE ONE QUESTION THAT SORTS EVERY CHECK
>
> **Ask this about any check and you will know at once what it can find:**
>
> > **Does this check compare two things made on separate paths? Or does it compare a thing to itself?**
>
> A check that compares a thing to itself can find a **mistake**. It cannot find a **hole**. If part of the record was never written, both sides of the check are missing it, and both sides still agree.
>
> A check that compares two things made on separate paths can find a hole — **if** the second thing is able to say so (§4, expressiveness).
>
> #### An example, with the numbers
>
> A farm records 8 sacks in and 8 sacks out. Someone then deletes the last 2 sacks from **both** halves of the record.
>
> | Check | What it compares | Sum | Does it fire? |
> |---|---|---|---|
> | Mass balance on the log | The log against itself | 6 in − 6 out = **0** | ❌ No |
> | Origin closure on the log | The log against itself | every sack has a source | ❌ No |
> | Fate closure on the log | The log against itself | every sack has an end | ❌ No |
> | **The buyer's own receipt** | **A record made on a second path** | **buyer holds 8, farm says 6** | ✅ **Yes — short by 2** |
>
> **The first three checks are arithmetic over one log, and cutting a log never breaks arithmetic over that log**, because what is left is still balanced. Only the fourth check reaches outside.

#### Three further rules on the estimate

- **When *Z* is uncertain, under-count it.** Under-counting raises each dark producer's estimated share, which is the direction that prompts them to surface and prove otherwise. Over-counting dilutes the estimate and feeds **OP-24 (understatement drift)**. **The self-liquidating error is the safe one**, because nobody complains about being charged too little.
- **The estimate is continuous, not a single event.** As part of an extent becomes measured, *Y* rises, *Z* falls, the estimate shrinks to what remains, and the parts must reconcile against the coarser figure they came from (EventLog §7.2a). Grapes tallied as one region become one measured region and one still estimated. **This is also what catches a fabricated total, because a fabricator does not control which sub-extent is measured next.**
- **One method for *Z* that needs no headcount:** `Z ≥ (N − Y) ÷ capacity`, where *capacity* is the most one producer could physically make, bounded by hours in a day, by land, or by throughput. Using that minimum assigns each dark producer the most they plausibly could have made, which is the conservative direction. **This is a candidate method, not the method** — the capacity ceiling is itself a constant under §3.3a, though one bounded by physics.

**"Dark" means outside the network, not low-technology inside it.** Subscribing carries a transparency requirement: a good moving through the accounting carries records of where it came from. **Gathering data on non-participants, and helping a producer bring their supply chain into the record, are both credited work.**

---

<!-- tag: fnd-s5-1c -->
### 5.1c The residual is held, and charged to nobody

**A coverage gap is real material that really moved. The question is whose books it sits on.**

> **The residual is computed, published, and left unassigned. It is debit on no account. When a dark producer joins, their share is back-traced from records that already exist and assigned to them — the party who actually caused it. Until they join, they cannot transact inside the network at all.**

**Why this respects A4 (no externalities) rather than dodging it.** A4 requires every cost to be accounted to whoever caused it. Here the cost is **pending**, not written off: it is held as a computable claim waiting for a claimant. **Assigning it to subscribers who did not cause it would contradict §3.2**, which keeps consumption and pollution debit on its causer, and would be collective punishment of the kind §3.3 already rejects.

**Nothing extra has to be built for the back-trace.** Both records already exist and are kept for other reasons — the ambient-stock measurement of regional pollution (§3.3), and the independently known production total of §5.1b. **A producer's share is derivable from those the moment there is a producer to derive it for.**

**And the damage is not unpriced meanwhile.** Because a pollutant's weight floats with the **ambient stock** (§3.3), dark producers' emissions are already in the stock that everyone is weighed against. **A subscriber pays a rate that reflects the total damage, while being charged only for their own units.** That is proportionality, not collective punishment. **The residual is felt correctly without being allocated.**

**What the gap is instead of a debit: a published coverage figure.** *"These books cover 60% of this region's measured output."* That is the extent rule (EventLog §7.4) at regional scale, and it does real work: a counterparty re-computing under its own model discounts goods from a thinly covered region. **Coverage becomes a quality of a network's own output rather than a charge against its members.**

---

<!-- tag: fnd-s5-1d -->
### 5.1d The back-trace reaches birth, and it runs on both sides

**When a person joins, their position is reconstructed back to their birth** — not to the network's founding, and not to the joining date. A whole life.

That sounds punitive and is the opposite, for one reason that has to come first.

> **The back-trace is symmetric. Both sides are reconstructed — the debit and the credit.**

§5.1 already estimates non-participants on both sides, and §7.5 credits every living human for the hours they spend keeping themselves alive. **Everyone alive is doing that work, whatever else they do** (§7.5.2). **So a lifetime back-trace brings a lifetime of floor credit with it.**

#### An example, with the numbers

| | |
|---|---|
| Labour a median lifestyle commands, per year (§3.5) | **1,380 h** |
| Credit earned per year simply by being alive (§6.1b) | **3,650 h** |
| Ratio, credit to consumption | **2.6×** |

**A person joining at forty arrives with roughly 3,650 × 40 = 146,000 hours of estimated credit against roughly 1,380 × 40 = 55,200 hours of estimated consumption.**

> **Joining is a windfall for a median person.** That is not a coincidence — it is §5.2's adoption incentive, computed. **The people for whom a full back-trace is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution.** That is correct targeting.

#### What the joining person supplies, and why they bother

**The estimate is the default. Evidence is voluntary and moves you off it.** A person supplies whatever narrows the estimate — where they were born, how long they lived in each place, which jobs they held, how far they commuted, which vehicles they owned and the mileage on them — and **accepts the cohort estimate for every period and activity they leave dark.** Nothing is compulsory.

**Evidence moves the figure in either direction, which is why people supply it.** Mileage records plus a vehicle model may show a hybrid driven below the commuter average, and the debit falls. The same records could raise it. **The estimate is not a verdict.**

**Details may arrive years later and the position re-derives.** No new machinery is needed: the position is derived from the log and never stored (A6), and §3.3 already recalculates every affected record when the science improves. **A life is refined the same way a cost constant is.** Supersession stays one-way (§5.1a) — an observation is never replaced by an estimate.

#### Two conditions, and without either this breaks

1. **An estimate for an undisclosed period is computed over the undisclosed residual, not over the whole population.** This is §5.1b's rule applied to periods and dimensions inside one life. Without it, a person who documents only their flattering years free-rides forever on an average their own silence inflates. With it, the pool of the undisclosed worsens as the well-documented leave it. **Selective disclosure is expected and is not an exploit, provided the residual rule holds.**
2. **An estimate errs against the estimated party, on both sides.** Debit is estimated at the unfavourable end and credit at the conservative end, so **supplying evidence always pays**, whichever direction the truth lies.

> **The floor is exempt and must stay exempt.** The floor is not an estimate. **It is credit for hours that were really spent**, attested by proof of life (§6.1b, §6.4b, §7.5.2). **So condition 2 never reaches subsistence, and a person who cannot document a life is not thereby impoverished by this rule.**

#### Why this does not contradict two rules it looks like it contradicts

| Looks like it breaks | Why it does not |
|---|---|
| **§5.1** — a non-participant is never charged for an estimated position | **Nothing is charged until they join, and joining is voluntary.** |
| **§3.3's transaction-time rule** — a revision never invalidates a completed act | **That rule protects acts the system gated at the time.** Acts before joining were never gated by any network, so no permission is being withdrawn. **A position is reconstructed; no verdict on past conduct is passed.** |

> ⚠️ **This raises the stakes on OP-22 (minimum audit disclosure), and that is the strongest objection to it.** A full back-trace is a life dossier — birthplace, every residence, employment history, commuting distance, vehicles owned, mileage. **Disclosure is voluntary, but the incentive runs toward disclosing**, so the arrangement puts steady pressure on people to assemble exactly the record a surveillance state would want. §5.3's split of public market data from private personal ledgers now has to hold across a lifetime. **Registered, not solved.**

---

## What this draft changed, for review

| # | Change | Why |
|---|---|---|
| 1 | **New §5.0.** Names the trust network as the thing that does everything in §5, defines six terms, and states that books are never summed, that a transaction lands on one network chosen by the seller, and that a network can end. | Author ruling, 2026-08-25. §5 read as though a central body applied these rules. |
| 2 | **§5.1 retitled and restated.** *"One verified human = one account"* now says **within a trust network**, and names Sybil resistance in plain words instead of assuming it. | Same ruling. The old sentence read as a claim about a global register. |
| 3 | **New worked example: the twins.** IC-7 makes the fraud lose 730 hours a year. | The document standard requires a worked example with digits. This is also the answer to the strongest form of the objection. |
| 4 | **New subsection: "One person, two networks."** Two networks with different floors report 12 h and 18 h for the same Monday, both correct; a purchase clears against one book only. | Author ruling. The old §7.5 condition 5 handled this and handled it wrongly. |
| 5 | **§5.1a and §5.1b restructured**, boxes kept, wording plainer, all three conditions and both boxed examples retained unchanged in substance. | Clarity pass. No rule moved. |
| 6 | **§5.1d gains a numbers table** for the 1,380 / 3,650 / 2.6× arithmetic, and a table for the two "looks like it breaks" cases. | Digits and structure instead of prose. |

**Not in this draft, and owed:**

- **§5.2 through §5.5** — the next chunk.
- ~~**§7.5 condition 5**~~ — **done.** Struck in [`Foundations_S7-5_rewrite_DRAFT_v0.1.md`](Foundations_S7-5_rewrite_DRAFT_v0.1.md) §7.5.5.
- **Overview §0** — the box beginning *"One thing to clear up"* states that the 2.4× cap holds *"across every network that can trade with every other."* Same defect, same fix.

**Cross-references to §7 in this draft, checked 2026-08-25 against the §7.5 rewrite:** §5.0's term table and §5.1's two-network table now point at **§7.5.1** for what the floor counts and **§7.5.3** for how its value is bounded. The two-network table now says plainly that `24 ÷ F` is an absolute maximum and points at **§7.5.5**. Every place that said the floor *"qualifies on being alive"* now says that **everyone alive is doing the work**, matching **§7.5.2**, and the phrase *"self-care credit"* is replaced by *"floor credit"* where it described the quantity rather than the section.

---

*End of draft v0.1.*
