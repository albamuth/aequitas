# C2 — Trust Networks: the implementers of Aequitas

> **Version:** 0.1
> **Date:** 2026-08-22
> **Status:** First assembly. Every ruling here is settled and folded into Foundations v0.17; this document gathers them in one place because they were decided across a dozen separate sections. **One thing remains open and it is named in §11: OP-10 (weighting-model governance).**
> **Depends on:** `Aequitas_Foundations_v0.37.md` §2.6, §3.3, §3.3a, §4, §4.1–§4.8 · `Aequitas_Conformance_v0.11.md`
> **Companion:** `C2_information_capture.md` — the reasoning behind §6 below, including a retracted proposal kept on purpose.

> **⚠️ The event-log paper was retired on 2026-08-28.** References to `EventLog §…` below are historical and no longer resolve. **The arithmetic constraints IC-1 to IC-12 are now conformance rows in [`Aequitas_Conformance_v0.11.md`](../Aequitas_Conformance_v0.11.md) §2**, which carries a label map; everything else it held is in Foundations. The archived paper is `99-archive/Aequitas_EventLog_v0.10.md`.


---

## 1. Why this document exists

**Aequitas is a system in the sense that capitalism is a system** (Foundations §2.6 — the scope boundary). It is not an organisation, a protocol, a piece of software, or a body anyone joins. It is a set of principles about how cost is accounted for.

**Principles do not keep books. Somebody has to.**

> **The trust network is the implementer of Aequitas. Cost accounting is the principle; records and data collection are the praxis, and trust networks are who execute it.**

**Nothing in this project works without them**, and that is easy to miss reading the Foundations, where they appear scattered across a dozen sections. Every mechanism in Aequitas — the event log, the integrity constraints, the estimates, the recomputation, the ratio gate — describes something a trust network *does*. The theory says what is true. **The network is where truth-telling actually happens or fails to.**

---

## 2. What a trust network is

**A laboratory, not a bank.**

> **Its goal is truth. Its motive is consensus rather than competition. A network whose methods let fraud through is *helped* by another network sharing the methods that catch it.** (Foundations §4.8 — federation.)

**This does not rest on anyone being virtuous.** In an interoperating pair, a bad method in one contaminates the books of the other. **The neighbour's interest in helping is selfish.**

The distinction matters more than it sounds, because the wrong analogy generates the wrong safeguards. Banks compete for customers, hoard advantage, and are disciplined by exit. Laboratories publish, replicate, and are disciplined by **replication**. *Reasoning from the banking analogy produced four proposals in one session that all had to be withdrawn — see `C2_information_capture.md` §11.*

**Level 2 of the verification ladder** (Foundations §4) is where trust networks live: *reputation and stake over a social graph, treated as an emergent market of trust networks where auditing is credited work.*

---

## 3. What a trust network does — the eight verifications

Everything a network does reduces to these. For each, what must be shown to check it.

| # | Verifies | Shown to check it |
|---|---|---|
| 1 | **Uniqueness** — this account is one human | A proof of personhood |
| 2 | **Liveness** — this human is alive, for the self-care floor | A proof of life |
| 3 | **Hours ≤ wall clock** — IC-7, the 24-hour cap | Claimed intervals in a window |
| 4 | **Event arithmetic** — IC-1 mass balance, IC-2 energy balance | The event's own inputs and outputs |
| 5 | **Origin closure** — IC-3, every parcel traces to a reservoir or a genesis entry | The parcel's ancestry chain, which travels with the parcel |
| 6 | **Custody** — IC-5, exactly one holder at any instant | A hand-off attested by both sides |
| 7 | **The ratio gate** — `D ≤ ρ·C` at transaction time | The person's totals |
| 8 | **Provenance** — that an estimate cites a real method and tally | `method_ref` and the tally it points at |

**Items 4, 5 and 6 need no trust model at all.** IC-1 through IC-9 are pure arithmetic on the log — no reputation, no authority, only the ability to recompute (Foundations §4.3). **Item 7's gate is evaluated at transaction time**, so a later correction changes future room and never the validity of a completed act (Foundations §3.3 — the transaction-time rule).

---

## 4. What a trust network holds

**Everything. That is the job.**

> **Trust networks build and maintain the databases.** Records of material flows, workplaces, people, events, and world data such as pollution measurements. **Every hand-off of a thing is a transaction record. Each service given and received is a record. Each pledged credit is a record.**

| Class | Contents |
|---|---|
| **Material flows** | extractions, transformations, transport, emissions |
| **Transactions** | every hand-off — custody changes, IC-5 |
| **Services** | given and received; no parcel moves, the record still exists |
| **Pledges** | permanent and non-revocable, drawn from a lifetime budget |
| **People** | accounts, uniqueness, liveness, hours |
| **Workplaces** | the sites and institutions where events happen |
| **World data** | pollution measurements, ambient stocks, reservoir readings, the independently-known totals *N* used to estimate the unmeasured |

**That last class is the one people miss.** A network holds not only its members' records but **measurements of the world**, which is what makes coverage reconciliation computable at all. **The database is not a registry of people. It is a description of a region's material life, of which people are one part.**

*Data minimisation is not available to this system and never was.* A7 (universal accounting) requires the records to be complete; §3.3 recalculates history when science improves; and §4.4 reconstructs a person's position back to birth. **None of that runs over deleted records.**

---

## 5. What a trust network publishes

**To be trustworthy, a network publishes its estimating numbers, its methods, and anonymised data covering all of its participants.** Its books are in the light (Foundations §4.7 — what a network owes).

**Tallying is algorithmic**, and that is what makes the citation requirement enforceable. Against a human process, "cite your method" is an aspiration. **Against a published algorithm it is a version number**, and `method_ref` has something concrete to point at.

**How much to reveal about institutions, co-ops and individual businesses is the network's own call**, balancing the confidence transparency earns against the privacy its members want.

> **The dial is publicity, not retention.** "What do you keep?" has one answer — everything. **"What do you show?" is the real question**, set per record class and published.

**⚠️ And it cuts both ways.** Anonymised participant data becomes *more* re-identifiable the more of it there is. **Publishing more to earn trust also publishes more to de-anonymise.** A network is choosing on that axis whether it means to or not.

---

## 6. Privacy is the network's choice

> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation. Compatibility between networks is a matter for those networks to negotiate.** (Foundations §4.7.)

**The working shape is the payment intermediary.** A card network facilitates a transaction in which neither party learns the other's private details. The intermediary knows both sides; the counterparties know a token and an outcome.

**A network may also choose the opposite** — radical transparency, no personal privacy at all. Nothing in the axioms forbids it.

**This is the third dial of the same kind as ρ (the tolerance rate) and `F` (the self-care floor).** Aequitas reads all three and sets none, because a global privacy constant would be exactly the central authority A8 forbids.

**Opacity is priced, not forbidden.** A counterparty re-computes a claim through its own model and discounts what it cannot verify, so heavy opacity makes a network's members' claims trade at a discount elsewhere.

### 6.1 Identity — uniqueness, not identification

> **The network must determine only that a person is unique.**

Secure identification at the point of transaction — a card chip, a biometric, whatever the rung supports — is *how* a network satisfies itself. **Bank practice today is a working basis, and ensuring individuality is in the network's own interest, not a rule imposed on it.**

**Multi-network accounts are legitimate.** One person may hold an account on Alpha and another on Beta. **That is not two credits; it is one life, counted twice** — and given similar standards and the same records, the two accounts converge on the same content, which is what makes a merge tractable.

---

## 7. How a trust network is funded

**It isn't, in the sense the question usually means.**

> **Funding, in Aequitas, is simply the recognition of an activity as creditable.**

There is no treasury, no allocation, no grant. Audit work is work; recording is never gated on approval (A7), so **the credit for doing the work was never scarce and never needed a funder.**

**What *is* scarce is demand and verification.** A **pledge** says someone wants the work done. **Verification** decides when the credit realizes. Participants may pledge toward the network's own infrastructure like any other work.

### 7.1 The bootstrap

A trust network is the basis on which all accounting rests, so it cannot be paid by an accounting that does not yet exist. **The network is created first. Assigning founders credit afterwards is the network's own decision.**

**This is not a special case.** A genesis entry already admits a thing that existed before the ledger, at an estimated cost, open to supersession. **The network's founding is that same move, aimed at the network.**

### 7.2 The founding record

**Aequitas does not prescribe what it must contain.** A network may write it up carefully, document it thinly, say *trust me* and offer nothing, or **take no credit for setting itself up at all.** All four permitted; none equivalent.

> **A network's traction rests on which it chooses. It thrives or dies on its ability to deliver the truth, or the nearest to truth it can manage.**

**It stays bounded regardless:** IC-7 caps founding credit at wall-clock hours × founders, checkable with a calendar; it is publicly recorded and re-computable; and since credit is non-transferable, over-crediting buys only consumption room, bounded by the disparity ceiling like everyone else's. **Taking no credit is a gift, not a gap.**

---

## 8. How disputes resolve

**Ask the laboratory question: how does a dispute in science get resolved?** Replication, published method, dated records for priority, **no adjudicator**, and nothing withdrawn from the record. **Aequitas already has all five.**

**Where the analogy breaks is the useful part: science can afford an unresolved dispute and an accounting system cannot.** A purchase clears or it does not, now.

**The answer is that most disputes never need deciding.**

| Dispute about | Resolves how | Verdict needed? |
|---|---|---|
| **The physical record** | **Arithmetic.** This is an *error*, and recomputation says whose. | No |
| **The weighting model** | **Nobody has to accept anyone else's model.** Each side re-computes the shared physical record through its own weights and decides for itself — *comparison, never conversion.* | **No** |
| **An estimate** | A **floor that improves**, not a finding. Better evidence supersedes it. | No |
| **Fraud** | A finding of fact. | **Yes** |

> **A transaction never waits on a shared verdict.** Two parties can price the same thing differently and still trade. **"Comparison, never conversion" was always the dispute-resolution mechanism; it had simply never been named as one.**

**Fraud is the one class needing a verdict — and science is not self-correcting about fraud either.** It answers with investigation by an institution. Aequitas answers the same way: **courts, small claims, contract law and ordinary social pressure continue to exist** (Foundations §4.7), and per §2.6 how an implementer engages them is praxis.

---

## 9. Fraud, and what correction looks like

**Catching fraud is the trust network's task.** What it does on finding some is what it does on any other day.

> **The past transaction is not reversed. The fraudulent credits are negated, the ledger rebalances, and the person's ratio may now be too low to buy anything until they sell some of what they hold.**

**Reversal would be wrong, not merely difficult.** The goods moved. The counterparty shed their property debit legitimately and was credited for work that really happened. **Unwinding the buyer's fraud would corrupt the seller's books to punish someone else's lie.**

**Nobody imposes a penalty. The books are simply correct, and being correct is the penalty.** Essentials are untouched throughout.

**Two consequences worth knowing.** Consumption debit **cannot** be sold off, so someone who ate or burned what they took cannot trade their way out. **But credit accrues to everyone alive**, so the ratio recovers on its own — and **the recovery period equals the faked credit divided by the accrual rate. The sentence is exactly the size of the fraud, measured in time, and nobody sets it.**

---

## 10. Membership: entry, and no exit

**Entry is onboarding** — the act of turning an estimate into a record. Voluntary, and usually to the joiner's advantage: a lifetime back-trace brings a lifetime of self-care credit with it.

**There is no matching act on the way out.**

> **Once records of a person exist they are never destroyed, only appended to — including after that person's death.**

**Ceasing to participate is always available.** The gift economy exists now, always has, and does not stop existing because an accounting system does. **Erasure is not available, and never was** — non-participants already carry an estimated position, so there is no not-in-the-books state to return to.

> **You can stop transacting. You cannot stop having existed.**

**Permanence is a requirement, not a policy.** Recalculation and back-tracing cannot run over deleted records. **A log that can be truncated is not a log.**

---

## 11. What is still open

**OP-10 — weighting-model governance. Who controls the cost model.**

Everything above supplies part of a **mechanism**: methods are published (§5), replication is the discipline (§2), and no adjudicator exists to capture (§8). **Whether that is sufficient is unproven, and OP-10 remains the top blocking problem in the project.**

> **⚠️ One prop was removed on 2026-08-24 and this section no longer leans on it.** It previously said *"rival-sector audit gives the correction an interested funder."* **Author ruling: that is a weak mechanism and it is withdrawn.** A rival's best move is not to fund your correction — it is to get **their own** constant set generously, which is cheaper and privately beneficial. **The equilibrium is mutual understatement, not mutual policing.** And it fails hardest on the ambient-stock and baseline constants, which have no rival at all. See Foundations §3.3a and Objections **OA3**.

### 🔴 Auditing cost constants — now explicitly a trust-network design problem

**Foundations §3.3a ruled on 2026-08-24 that *how* a cost constant gets audited is out of scope for Foundations and in scope for a network.** Whoever publishes a constant sets every figure in that sector, backwards through history (§3.3), and the pressure on it runs one way: **overstatements get corrected because everyone paying them wants that; understatements have nobody.**

**A network must be able to show its answer.** These five properties are conformance items **16a–16c** — not suggestions:

| # | Requirement |
|---|---|
| 1 | **Two unaffiliated replications** before a constant may re-weight history. |
| 2 | Every constant published with its **method, version, and uncertainty interval**. |
| 3 | Review triaged by **magnitude × concentration of beneficiary**, never magnitude alone. |
| 4 | **Membership composition is public** — a network concentrated in the sector it audits is captured by construction, and this makes that detectable rather than something anyone must police. |
| 5 | A public statement of **which constants have not been reviewed, and how old each reading is**. |

> **This is a requirement on the straw-man, and the straw-man does not yet meet it.** §3 lists eight verifications a network performs; **constant-auditing is a ninth and it has no design here.** Drafting one is the next piece of C2 work.

**And say the honest part: no network has demonstrated a working answer, because no network exists.** The five properties are what a design gets judged against, not evidence the problem is solved.

Three smaller items:

- **The pledge-reserve causation claim** — did *this* task cause *that* harm? Where a physical trace exists the trace decides. Where it does not, it is a contested finding of fact and routes to existing recourse, like fraud.
- **The verification-cost threshold.** `06-simulation/residual-unravelling/residual_unravelling.py` measures where the estimate-the-residual rule stops working: **past roughly 40% of a median unit's debit, darkness becomes stable again.** Privacy-preserving verification costs more than open verification, so **cheap verification is a precondition of coverage, not a nice-to-have.**
- **A merit monopoly can stop being meritorious.** Convergence toward a single network is expected (§4.8). The guard is publication plus replication, not competition — so **if the publication requirement ever weakens, the argument that a merit monopoly is benign weakens with it.**

---

## 12. Provenance

Every ruling in this document was settled on **2026-08-22**, most of them in a single session, and is folded into Foundations v0.17 with entries in `Aequitas_Foundations_CHANGELOG.md`. The reasoning — including a proposal that was built, stress-tested and retracted — is in `C2_information_capture.md` and `03-journal/2026-08-22.md`.

**The session began with an objection raised from outside the project**, by an AI agent on a public forum, against a claim this project had published. That is worth recording: **the trust-network design was largely settled by being argued with.**
