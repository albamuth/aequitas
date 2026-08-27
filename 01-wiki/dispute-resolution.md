# How a dispute resolves

> **Most disputes never need deciding. Sorting them apart removes three of the four kinds, and only fraud needs a finding of fact.**

> **Moved here from Foundations on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rules stay in Foundations §4.7. This page carries the worked detail and the open questions.**

---

<!-- tag: fnd-s5-3d -->
### 5.3d How a dispute resolves

§4.8 says trust networks are laboratories. **Ask the laboratory question: how does a dispute in science get resolved?**

**Replication. Published method. Dated records for priority. No adjudicator — there is no supreme court of physics. Both claims stay in the literature; nothing is withdrawn from the record. And often it is never resolved at all, only outlived.**

**Aequitas already has every one of those**, written for other reasons:

| Scientific practice | Already in Aequitas |
|---|---|
| Replication before a result is accepted | §3.3a — **two unaffiliated replications** before a constant may re-weight history |
| You can only dispute what you can inspect | §4.7 — networks publish numbers, methods and anonymised participant data |
| No adjudicating body | **A8.** No central authority exists to appeal to |
| Nothing is withdrawn; the rebuttal is appended | EventLog §8.2a **contest without replacement**, and §4.8 no erasure |
| Dated records settle priority | An append-only log with intervals |

#### Where the analogy breaks — and this is the part worth having

**Science can afford an unresolved dispute. An accounting system often cannot.**

A field can stay divided for thirty years and lose nothing. But a purchase either clears or it does not, **now**. You cannot tell a buyer that opinion is divided on whether their debit exceeds their room and to come back when the literature settles.

**The lab framing supplies the epistemics. It does not supply a decision procedure.** So the question is what decides *at transaction time*.

#### The answer is that most disputes never need deciding

Sorting them apart dissolves three of the four classes.

| Dispute about | How it resolves | Needs a verdict? |
|---|---|---|
| **The physical record** — did 70 g of wheat actually move? | **Arithmetic.** IC-1…IC-9 recompute it. **This is not a dispute; it is an error, and recomputation says whose.** | No |
| **The weighting model** — what does a tonne of CO₂ cost? | **Nobody has to accept anyone else's model.** A counterparty re-computes the shared physical record through **its own** weights and decides for itself — OP-14, *comparison never conversion*. Meanwhile §3.3a's replication and rival-sector audit move the field, slowly, the way science does. | **No — and this is the load the framing carries** |
| **An estimate for a dark actor** — what is *Z*? | Published method, replicable (§4.7). The figure is a **floor** that improves (§4.4), not a finding. Better evidence supersedes it. | No |
| **Fraud** — someone recorded events that never happened | **A finding of fact, and it needs one.** | **Yes** |

> **The insight is that a transaction never waits on a shared verdict.** Each side computes its own answer over the same physical record and decides whether to trade. **Disagreement about weights does not block commerce; it just means two parties price the same thing differently** — which is a fact about models, not a deadlock. **Comparison, never conversion, was always the dispute-resolution mechanism. It had simply never been named as one.**

#### The one residue, and where it goes

**Fraud is the class that needs an actual finding of fact**, and the analogy holds here too: **science is not purely self-correcting about fraud either.** Replication catches error; it does not catch a fabricated dataset that replicates because it was designed to. Science answers with **investigation and retraction, by an institution** — a university integrity office, a funder, a journal.

**Aequitas answers the same way, and §4.7 already said so:** *courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people.* Per **§1.2**, how an implementer engages them is praxis, not foundations.

**What the accounting contributes is upstream of that.** IC-1…IC-9 make a fabricated record *arithmetically expensive* — a lie must balance mass, balance energy, close origin, close fate, and survive a counterparty's recomputation. **The remaining fraud is the fraud that is internally consistent, which is exactly OP-26's coverage question, answered by measurement against the world rather than by adjudication.**

#### What correction looks like — nothing is reversed

**Catching fraud is the trust network's task** (§4.7), and what it does on finding some is the same thing it does on any other day.

> **The past transaction is not reversed. The fraudulent credits are negated, the ledger rebalances, and the person's ratio may now be too low to buy anything until they sell some of what they hold.**

**This is the transaction-time rule (§3.3), not a special fraud procedure.** The gate is evaluated when the transaction happens; a later correction changes *future* room and never the validity of a completed act. **Fraud correction is an ordinary re-weighting that happens to be large.**

**And reversal would be wrong, not merely difficult.** The goods moved. You cannot un-eat a sandwich. The counterparty acted on the record as it then stood, shed their property-debit legitimately under custody (§3.2), and was credited for work that really happened. **Unwinding the buyer's fraud would corrupt the seller's books to punish someone else's lie.**

**So the correction is arithmetic, and the consequence is automatic:**

1. The fake credit is negated. **C falls.**
2. **D does not.** They really did take the things.
3. `D ≤ ρ·C` now fails. **They cannot make discretionary purchases.**
4. **Selling restores the ratio** — property debit is dischargeable on transfer (§3.2), so handing goods on lowers *D*.

**Nobody imposes a penalty. The books are simply correct, and being correct is the penalty.** Essentials are untouched throughout — §5.5.4's backstop reaches non-essentials only, and it does so for the fraudster on exactly the terms it does for anyone mis-measured.

**Three consequences worth stating, because they are not obvious.**

- **Consumption debit cannot be sold off.** If what they took was eaten, burned or emitted, selling does not help — consumption debit is permanent (§3.2). **They are over their ratio and cannot trade their way out.**
- **But there is no bankruptcy, and there does not need to be, because there is time.** Credit accrues to everyone alive at the self-care floor, whatever their standing (§5.5). So *C* grows again on its own, and the ratio recovers. **The recovery period is the faked credit divided by the rate they now accrue** — which means **the sentence is exactly the size of the fraud, measured in time, and nobody sets it.** A person who faked ten years of credit works off roughly ten years. *That is a proportionate, self-expiring, un-appealable consequence produced by arithmetic rather than by judgement.*
- **The influence axis corrects the same way.** IC-8 caps cumulative pledges at lifetime earned credit. Negating credit can put a person retroactively over that cap; the pledges themselves are permanent and the work they summoned was really done, so nothing unwinds. **They simply cannot pledge again until credit recovers.** Same mechanism, no second procedure.

> **⚠️ One real load stays, and it is not a weighting dispute.** The pledge-reserve claims process (§4.6) asks whether a *particular past task caused a particular later harm*. Where a physical trace exists, the trace decides and it is arithmetic. **Where it does not, this is a contested finding of fact with no analogue in the list above**, and it is the genuine adjudication load flagged when the reserve was folded. **It routes to existing recourse like fraud does. Registered; not solved here.**


---

## Related

- [distributed-auditing](distributed-auditing.md) · [retroactive-reweighting](retroactive-reweighting.md) · [derived-ledger](derived-ledger.md)

---
*Status: settled (the four classes) / provisional (causation in the pledge reserve)*
*Source: Foundations §4.7. Text moved from Foundations v0.27 in the 2026-08-27 consolidation; section numbers updated to the new scheme.*
