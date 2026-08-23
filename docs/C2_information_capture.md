# C2 — Information capture: verify, don't hold

> **Status:** ✅ **CLOSED — see §13.** Information capture is scoped out with recorded reasons: the escape is non-participation and never closes; trust networks are **laboratories, not banks**; and a monopoly earned by better methods is not the monopoly capitalism produces. ❌ **§§2, 4a and 10 are RETRACTED — see §11.** The "verify, don't hold" principle was built on a false premise. **The trust network *is* the database**; holding the records is its function, not a failure mode. What survives: the **uniqueness ≠ identification** split (§3, ruled in §8), the **multi-network Sybil vector** (§9), and the retention-disclosure idea in the corrected form of a **publicity policy** (§11).
> **Read §11 first.** Sections 1–10 are kept unedited because the reasoning error is instructive and the project does not delete superseded work.
> **Answers:** Foundations §5.3a residue (a), sharpened by §5.3b · OP-22 · P4 / OP-10 (capture)
> **Tracks:** Foundations v0.17 §4, §5.3, §5.3a, §5.3b · EventLog v0.8 §4.1a

---

## 1. The problem, as §5.3b left it

A trust network publishes every estimating number, every method, and anonymised data on all its participants. After all that, **one advantage remains**:

> **It holds the linkage** between the anonymised rows and the people.

That linkage is the concentration to worry about. A network that keeps its members' lifetime back-traces (§5.1d) holds an information position comparable to the wealth position this project exists to dissolve. It can be coerced, breached, or can simply defect. **§3.3a's public-membership screen was written for *sector* capture and does nothing about this.** And "you may leave" is a weak exit when what you would leave behind is your life history.

> ❌ **RETRACTED — §§2, 4a and 10 below rest on a false premise. See §11.**

## 2. The axioms already answer most of it

Per the project's own rule — *check the axioms before importing an outside solution* — §5.3 already says this, and has since it was written:

> Account holders keep a **private ledger with provable claims** — zero-knowledge proofs of balances and cost positions when transacting, **not history**.

**The design intent was always self-custody.** The network's job is to *check* a claim, not to *keep* the evidence behind it. Which yields the principle:

> ### Verify, don't hold.
> **A network needs the ability to check a claim. It does not need custody of the data behind the claim. Information capture is not inherent to being a trust network — it is what happens when a network retains what it only needed to verify.**

**This is not a new mechanism. It is a design rule that the existing machinery already permits and nothing currently states.**

### 2.1 It survives the back-trace

§5.1d's lifetime reconstruction looks like it forces the network to hold a dossier. It does not.

- The **estimate** is computed from a published algorithm over **public cohort data** (§5.3b). No personal data needed.
- The person's **deviations** from that estimate — the hybrid car, the shorter commute — are proved, not surrendered. The network checks a proof that evidence supports a deviation. **It never needs the mileage records themselves.**

The dossier is assembled **by the person, about the person, and stays with them.**

### 2.2 It survives cohort estimation

§5.1b's residual rule needs *N* (an external total) and *Y* (the sum of disclosed figures). Market data is public by §5.3, so *Y* is an aggregate of already-public quantities. **Cohort estimation needs aggregates, not linkages.**

## 3. The distinction that does the real work

Most of the fear collapses once two different linkages are separated, because only one of them is required:

| Linkage | Required? | By what |
|---|---|---|
| **"This account is one unique human"** | **Yes** | A8 / C6 identity — hard Sybil resistance is non-negotiable |
| **"This account is Ana, and here is Ana's life"** | **No** | Nothing in the axioms requires it |

**The system needs uniqueness, not identification.** Proof-of-personhood designs that establish uniqueness without a central register are the C6 question, and they are a different problem from the one people fear when they hear "life dossier."

**Stating this split is most of the answer**, and the project has been carrying both under one word.

## 4. The proposal — three parts

**(a) State "verify, don't hold" as a principle in §5.3.** It is already implied; nothing says it.

**(b) Add a retention disclosure to §5.3b's publication set.**

> **A network publishes what it retains** — which categories of data, for how long, and in what form — alongside its numbers and methods.

This makes holding a **visible property of a network** rather than an invisible one. §5.3a's discount mechanism then acts on it exactly as it acts on opacity and thin coverage: **a network that hoards is a bigger target and a bigger liability, and its members can see that before they join.** *Price it, don't forbid it* — the fifth time that has been the answer.

It also makes one strong claim checkable: **a network that holds nothing cannot be coerced into revealing anything.** "We cannot comply, because we do not have it" is only credible against a published retention set.

**(c) Treat holding as a ladder property (§4), not a universal rule.** At **Level 1** there is no cryptography and the record *is* social memory — a village holds its own knowledge and privacy there is a social matter, not a technical one. "Verify, don't hold" is a **Level 3** property. The ladder already exists to accommodate exactly this kind of difference, and the design rule that levels must interoperate applies unchanged.

## 5. Stress test

| Test | Result | Note |
|---|---|---|
| **Universality** | ✅ | One principle, applied at every level, with the ladder accounting for what each level can do. No exception, no special case. |
| **Decentralization** | ✅ | No authority enforces it. Retention is published; members and counterparties price it. |
| **Fecundity** | ⚠️ | Minimal holding pays only if members prefer it and act on the disclosure. Networks compete on it, which is the mechanism — but it depends on members reading a retention disclosure, and most people do not read terms today. |
| **Axioms** | ✅ | A6 (derived, not stored) is exactly this principle at the ledger level. A8 intact. Consistent with §5.3 as written. |

**Who games this — three, honestly:**

1. **The lying network.** Publishes a minimal retention set and holds everything anyway. **Nothing stops it, and you cannot prove a negative.** Partial mitigations: a breach reveals what was held, and members can seed decoy records to detect retention. **Weak. This is the proposal's main hole.**
2. **The operator.** Even a hold-nothing network has people who see traffic. **Metadata — who verified what, when, and how often — is not covered by any of this** and is unsolved in general, here as everywhere else.
3. **The cost attacker.** Zero-knowledge verification is expensive, and `06-simulation/residual_unravelling.py` measured where that matters: past roughly **40% of a median unit's debit**, the residual rule stops unravelling the dark pool. **A maximally private network can price itself out of coverage.** Not an attack so much as a curve — but an attacker who can *raise* verification cost is attacking coverage through privacy.

## 6. What this does and does not do

**Does:** turns "the network is the most information-rich actor" into "a network *may choose* to be, and must say so." Separates uniqueness from identification. Puts the dossier in the hands of its subject.

**Does not:** prevent a network from lying about retention; cover operator metadata; make private verification cheap.

**Honest summary:** this converts an unbounded structural problem into a bounded one with two named holes. That is worth having, and it is not a solution.

## 7. The ruling needed

1. **Adopt "verify, don't hold" as a stated principle?** (§5.3)
2. **Add retention disclosure to the publication set?** (§5.3b)
3. **Is the uniqueness/identification split right** — does anything in the system genuinely need to know *which* human an account is, rather than that it is *one* human? If something does, this proposal is weaker than it looks and the answer must change.

Question 3 is the one that could break it.


---

## 8. RULED 2026-08-22 — and the question was malformed

**Author's ruling:**

> Nothing stops a person from being person A on trust network Alpha and B on trust network Beta. But providing the same records will result in an essentially identical account for both, if both networks have similar standards. A transaction needs to be assigned to one account, and a person needs to be securely identified by the network — like the RFID chip on a credit card, biometric data — in order to facilitate the transaction. **The network must only determine that a person is unique.** However banks verify identity today is a basis, but it is in the interest of the trust network to ensure individuality. If Alpha and Beta merged, they might see that A and B have the same records and collapse it into a single account.
>
> **Aequitas is a system of ideas, not an entity, so it doesn't "know" anything.** It is a system implemented by the trust networks. What they need to know or not is up to them.

**§7's question 3 was badly put and is withdrawn.** It asked whether *the system* needs to know which human an account is. **The system is not a knower.** Only a network knows anything, and §5.3a already settles that what a network knows is its own choice. The well-formed version is: *does anything break if no network identifies?* — and the answer is no.

**So the split in §3 stands, with the wording corrected:**

> **Uniqueness is required by the accounting. Identification is a network's own business.** A network must satisfy itself that an account is one human, and secure identification at the point of transaction — a card chip, a biometric, whatever the rung supports — is how it does that. Bank practice today is a working basis. **Ensuring individuality is in the network's own interest**, not a rule imposed on it.

**And multi-network accounts are legitimate.** One person may hold an account on Alpha and another on Beta. Given similar standards and the same supplied records, **the two accounts converge on essentially the same content** — which is what makes a merge tractable: on federation, Alpha and Beta can see that A and B carry the same records and collapse them into one.

---

## 9. ⚠️ What the ruling exposed — the multi-network self-care vector

Legitimate multi-network accounts create a Sybil vector that nobody had named, and it aims at the project's headline result.

**The exploit.** Credit for *produced goods* is anchored physically: a parcel has one custody chain (IC-5) and can be handed off once, so the same output cannot be credited twice across networks without the duplication surfacing wherever the goods travel. **Self-care credit has no such anchor.** It is credited by proof-of-life (§6.1b, §7.5) and needs no output at all.

> A person holding accounts on *k* networks can satisfy proof-of-life on each and accrue the self-care floor **k times**. Consumption room is gated per account, so their total room is **k × ρ·C** — and the disparity ceiling, `24/F`, is computed **per network**. Across *k* networks the effective ceiling is **k × 24/F**.

**Two things to say about it honestly.**

1. **It is inside the ceiling's stated conditions, not outside them.** `DISPARITY_CEILING.md` §4 already makes the bound conditional on *"no fraud manufactures gross hours (OP-1)"*, and this manufactures gross hours. **The result is not broken. But this is a specific, cheap, non-obvious instance of that condition and it deserves naming** — it is a sibling of the floor-shopping case already flagged, and sharper: floor-shopping picks the most generous `F`, this one *sums* `F` across networks.
2. **Point 7 of the ruling is the answer, and it is a good one.** *Merge collapses duplicates.* Federation is the defence, and the incentive runs the right way: a network that accepts inflated credit from a double-claimer **damages its own books**, so cross-checking uniqueness with its peers is in its own interest — OP-14 counterparty re-computation applied to persons rather than to goods. **The more networks interoperate, the more expensive the exploit gets.** Interoperation is individually rational for the honest and costly for the cheat, which is the fecundity property this system keeps wanting.

**What is owed.** The disparity ceiling should state explicitly that `24/F` is a **per-network** bound, and that the global bound is `24/F` **only under cross-network uniqueness attestation**. Right now the doc reads as though the bound were global. **That is an over-claim of exactly the kind OP-26 punished, and it should be corrected before someone else finds it.**

*Routes to:* OP-1 (gross-hours manufacture) · OP-14 (counterparty re-computation) · C6 (identity) · C2 (entry/exit and federation).


---

## 10. Itemised — what is verified, and what would be held

*Added 2026-08-22 in answer to "what are we verifying, what would we be holding?" — the principle in §2 is a slogan until this table exists.*

### 10.1 The eight things a network actually verifies

Everything a Level-2 network does reduces to these. For each: what must be **shown** to check it, and what the network would have to **keep** afterwards.

| # | What is verified | Shown to check it | Must be retained? |
|---|---|---|---|
| 1 | **Uniqueness** — this account is one human (A8/C6) | A proof of personhood | **Yes — a uniqueness token.** Not the biometric, not the identity. Enough to refuse a second enrolment of the same person. |
| 2 | **Liveness** — this human is alive, for the self-care floor (§7.5) | A proof of life | **No** beyond "last checked at T". |
| 3 | **Hours ≤ wall clock** (IC-7) | Claimed intervals in a window | **A per-person counter — see §10.3.** This is the hard one. |
| 4 | **Event arithmetic** (IC-1, IC-2) | The event's own inputs and outputs | **No.** Mass and energy balance is arithmetic on what is in front of you. |
| 5 | **Origin closure** (IC-3) | The parcel's ancestry chain | **No** — see §10.2. |
| 6 | **Custody** (IC-5) — who holds this parcel now | A hand-off attested by both sides | **Yes — a current-holder pointer.** But this is *market data*, public by §5.3, not personal history. |
| 7 | **The ratio gate** — `D ≤ ρ·C` at transaction time | A proof over the person's totals | **A commitment to those totals**, not the totals themselves — §10.3. |
| 8 | **Provenance** of an estimate (§4.1a) | `method_ref` and the tally it cites | **No.** Both are already public by §5.3b. |

### 10.2 The chain travels with the parcel, not with the network

Item 5 looks like it forces an archive: to walk a parcel back to a reservoir extraction or a genesis entry, you need the whole chain.

**But §5.1b already says where the chain lives:** *"a good moving through the Aequitas economy **carries records of its origin**."*

**The record travels with the thing.** A buyer receives the chain along with the parcel — that is what makes the debit computable at hand-off and what lets them prefer the cleaner loaf (Overview §1). **The network checks a chain presented to it. It is not the chain's custodian.**

Same for item 4. An event has at least two parties and is held by its participants. **There is no requirement anywhere that a single party holds the whole log.** A6 says the ledger is *derived* from an append-only log; it does not say one actor keeps it.

> **The network is a checker of what is presented, not an archive of what has happened.** That sentence is the whole of "verify, don't hold", and items 4, 5 and 8 fall out of it immediately.

### 10.3 The two that genuinely need state — and it is state, not content

Items 3 and 7 cannot be done on presentation alone, and it is worth being exact about why.

**Item 3, IC-7.** A network that only checks the intervals it is shown can be defeated by showing it 24 of your 30 hours. Catching that needs the network to know *all* the claims a person made in the window — which sounds like holding a history of what they did.

> **It is not. It needs an unforgeable per-person counter of hours claimed — not the claims.** A number that cannot be forked, with no content behind it. The same shape as double-spend prevention: you learn that a total was exceeded without learning what was spent on.

**Item 7, the ratio gate.** Checking `D ≤ ρ·C` needs *C* and *D*. §5.3 already specifies the answer — the person proves the inequality against a commitment, and the network learns the verdict, not the totals.

**So the honest form of the principle is a distinction between state and content:**

> **A network must hold *state*: a uniqueness token, a custody pointer, an hours counter, a totals commitment. It never needs to hold *content*: what the work was, where it happened, who was there, what was bought, or the evidence behind any deviation from an estimate.**

**State is small, bounded, and non-narrative. Content is the life dossier.** Everything people fear about information capture attaches to content, and none of the eight verifications requires it.

### 10.4 What this does not claim

- **The mechanisms are not built.** Unforgeable counters and commitment-based gates are the right *shape* and are ordinary cryptography, but the specific construction is **C7 / OP-22 and unspecified**. This section says what is needed, not how.
- **Cost is real.** Proving instead of showing is more expensive than showing, and `residual_unravelling.py` puts a threshold on how expensive verification can get before coverage collapses (~40% of a median unit's debit). **State-only verification is not free, and the cost lands exactly where the sim said it would.**
- **Level 1 has none of this.** In a village the counter is social memory and the commitment is a neighbour's word. **"Verify, don't hold" is a Level 3 property** (§4c); the ladder exists for exactly that difference.
- **Retention is still a choice.** Nothing here *prevents* a network holding content. It establishes that a network does not *need* to — which is what makes the retention disclosure of §4b meaningful rather than rhetorical.


---

# 11. RETRACTION AND CORRECTION — the network *is* the database

*2026-08-22. This section supersedes §§2, 4a and 10.*

## 11.1 What I got wrong

**Author's correction:**

> Trust networks are the ones building and maintaining the databases. They need to keep the records of material flows, workplaces, people, events, and world data like measurements of pollution and such. Every hand-off of things is a transaction record. Each service given and received is a record. Each pledged credit is a record. **How public these records are is up to the network.**

**"Verify, don't hold" is wrong, and the error was in the premise, not the detail.** I imported a data-minimisation principle from privacy engineering — *hold as little as possible* — into a system whose foundational requirement is the opposite: **A7 (universal accounting) demands that the records exist and are complete.** A ledger derived from an append-only log (A6) requires the log, and **maintaining that log is what a trust network is for.**

The distributed reading I built in §10 — chains travelling with parcels, events held only by their participants, the network as a stateless checker — is not the system. Goods *do* carry their provenance (§5.1b), and that is true and useful; **it does not follow that nobody keeps the database.** Both are true at once, and I treated the first as replacing the second.

**The state-versus-content distinction goes with it.** Content is not a liability to be avoided. **Content is the product.**

## 11.2 What a trust network actually holds

Records, comprehensively. At least these classes:

| Class | Examples |
|---|---|
| **Material flows** | every extraction, transformation, transport, emission |
| **Transactions** | **every hand-off of a thing is a record** — custody changes, IC-5 |
| **Services** | **each service given and received is a record** — no parcel moves, the record still exists |
| **Pledges** | **each pledged credit is a record**, permanent and non-revocable (§6.4) |
| **People** | accounts, uniqueness, liveness, hours |
| **Workplaces** | the sites and institutions where events happen |
| **World data** | pollution measurements, ambient stocks (§3.3), reservoir readings, the independently-known totals *N* of §5.1b |

**That last class is worth noticing.** A network holds not only its members' records but **measurements of the world** — which is what makes the coverage reconciliation of §5.1c computable at all. The database is not a registry of people; it is a description of a region's material life, of which people are one part.

## 11.3 The dial is publicity, not retention

§4b proposed a *retention disclosure*. Under the corrected model that is close to meaningless — the answer to "what do you retain?" is "everything, that is the job."

**The real dial is the one the author has now named three times, and it is publicity.**

> **How public each class of record is, is the network's own decision.** §5.3a said it for persons. §5.3b said it for institutions and businesses. It generalises: **a network sets a publicity policy per record class, and publishes that policy.**

This is the same dial as ρ and the floor `F`, and it lands where §5.3a already put it. **What §4b was reaching for survives in corrected form: not "declare what you keep" but "declare what you show."**

## 11.4 So what is left of information capture?

Restated correctly, and it is a smaller and more honest problem than either of my two previous framings.

**The risk is not that a network holds records. It is a network that holds comprehensively *and* publishes little.** Holding is universal; opacity is the variable. Which means:

- **The exposure is visible.** A network's publicity policy is published (§5.3b), so how much it discloses is a known property, and §5.3a's discount mechanism acts on it — a counterparty discounts what it cannot verify. **Priced, not forbidden.** Again.
- **The protection is horizontal, not architectural.** Aequitas does not reduce capture by making each database smaller. It reduces capture by **there being many networks, none of them global**, each holding its own region's life, none holding everyone's. **Decentralisation here means *many holders*, not *less held*.** That is consistent with A8 and with every other structure in the project, and I should have reached it first.

  > ⚠️ **This protection has an expiry date, and §5.3c names it.** The expected trajectory is **convergence** — networks federate, then merge, toward a single network rather than permanent regional isolation. **A protection that depends on there being many networks weakens exactly as the ecosystem succeeds.**
  >
  > The distinction that may save it: **what merges is the *method*, not necessarily the *custodian*.** Many holders can share one algorithm set the way many operators share one protocol — one accounting domain, many databases. **If that holds, this protection survives convergence. If convergence means one operator, it does not, and the end state of the design is the largest information concentration in the system.** Unresolved; registered against OP-10 and C2.
- **⚠️ And the irreducible part, stated plainly.** Comprehensive records are a requirement, not a choice, so **the databases are comprehensive by design and the breach-and-coercion surface is real and permanent.** No mechanism proposed anywhere in this project removes it. What bounds it is scale — a network holds a region, not a world — and publicity, which removes the *differential* advantage of holding without removing the holding. **This is a genuine residual cost of the system and should be stated as one rather than argued away.**

## 11.5 What survives from §§1–10

- **§3's split — uniqueness ≠ identification.** Intact and ruled (§8). A network must establish that an account is one human; whether it identifies which human is its own business.
- **§9's multi-network Sybil vector.** Intact, and it forced a correction to `DISPARITY_CEILING.md`.
- **§4b, in corrected form** — as a **publicity policy** rather than a retention disclosure (§11.3).
- **§4c's ladder point.** Intact: what a Level 1 network can hold and publish differs from Level 3, and the ladder exists for that.

**Dead:** §2's "verify, don't hold" principle, §10's eight-row table, and the state/content distinction.

## 11.6 The lesson worth keeping

**I solved an architecture problem the project did not have, because I recognised a pattern from outside instead of reading what was already written.** Data minimisation is correct advice for systems that collect more than they need. **Aequitas collects exactly what it needs, and what it needs is everything** — that is what "no externalities" means at the record level.

The project's own rule says *check the axioms before importing an outside solution.* **I checked the axioms for a mechanism and found one; I did not check them for the premise.** A7 was sitting there the whole time saying the records must be complete.


---

## 12. CORRECTION to §9 — compatibility means one ledger

*Same day. §9 framed multi-network accounts as a Sybil vector reaching `k × 24/F`. **The framing was wrong.***

**Author's correction:**

> A person can hold an account on two networks, but those networks are counting the same thing. **The networks cannot be compatible unless they can arrive at the same ledger for a single person.**

**Two networks counting the same person are counting the same thing.** Compatibility is not a property bolted on afterwards — **it is the ability to re-derive each other's numbers and land on the same ledger** (OP-14, comparison never conversion).

So:

- **Compatible networks produce one ledger for that person, seen from two places.** The self-care floor is credited **once**, because it is one life. **There is nothing to sum, and `k × 24/F` was arithmetic on two things that are the same thing.**
- **Incompatible networks do not interoperate.** Goods and claims do not cross. Each holds a **partial** record of that person's material life.

**What survives is not a breached bound but a coverage gap** — and that is machinery already built: §5.1c (the residual is held, not allocated) and EventLog §7.4 (a verdict declares its extent). An incompatible pair leaves two partial ledgers, each obliged to say it is partial.

**Federation is therefore not a defence against an exploit. It is what interoperation means.**

§9's finding still did real work — it exposed that condition 4 of the ceiling wrongly claimed IC-7 covered the multi-network case, and that correction stands. **The error was in what replaced it.** Both docs are now re-framed: Foundations §7.5 condition 5, `06-simulation/DISPARITY_CEILING.md` §4 condition 5.


---

# 13. CLOSED — scoped out, with reasons (2026-08-22)

**Author's ruling.** Information capture is not a problem this project addresses, and the reasons are good ones.

**First, the escape never closes.** §12 worried that convergence removes exit. **It mistook which exit matters.** The way out of Aequitas is **not participating** — the gift economy exists now, always has, and does not stop existing because an accounting system does. **Nobody is enclosed.**

**Second, exit was never the discipline anyway.** Leaving does not fix a bad method; it removes the person who left. **What fixes a method is replication** — which §3.3a already required, as *two unaffiliated replications*, before anyone called it that.

**Third, and this is the reframe that does the work:**

> **Trust networks are laboratories, not banks. Their goal is truth and their motive is consensus rather than competition. A network whose methods let fraud through is *helped* by another network sharing the methods that catch it.**

**It does not rest on virtue.** In an interoperating pair, **a bad method in one contaminates the books of the other**, so the neighbour's interest in helping is selfish. Same logic as OP-14, aimed at methods instead of claims.

**Fourth, the four reasons this is out of scope:**

1. **Hypothetical.** Convergence is a prediction, not an observation.
2. **Unknown timing and technology.** A safeguard designed now against conditions we cannot describe is decoration.
3. **A monopoly earned by better methods is not the monopoly capitalism produces.** Capitalist monopolies come from exclusion and anti-market practice, **not** from serving people better. A single Aequitas network would arrive because its methods are the best ones. **That is good service.**
4. **Data security and backups are a technology problem**, outside this project's scope.

**The strongest form of point 3, and why it holds: methods are published (§5.3b) and replicable. The monopoly is over *which method is used*, never over *who may propose one*. No exclusion, no moat** — which is precisely what a capitalist monopoly has and this does not.

> **⚠️ One watch item, not a defence.** A monopoly earned on merit can stop being meritorious and keep the position. **The guard is publication plus replication, not competition.** If §5.3b's publication requirement ever weakens, the merit argument weakens with it. **The two are load-bearing for each other.**

**Status of this paper: closed.** §§2/4a/10 retracted (§11), §9 re-framed (§12), and the underlying question scoped out here. **What it leaves behind that is still live:** the uniqueness ≠ identification split (§3, ruled §8), and the correction it forced to `DISPARITY_CEILING.md` condition 4.
