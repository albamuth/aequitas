---
title: How a dispute resolves
summary: Disputes about the physical record, the weighting model and an estimate need no verdict, because each party recomputes the shared record under its own model; only fraud needs a finding of fact, made by the trust network, and correction supersedes the false credit without reversing any transaction.
type: mechanism
ids: [§4.7]
status: settled
edges:
  - {rel: depends_on, to: derived-ledger}
  - {rel: depends_on, to: retroactive-reweighting}
  - {rel: depends_on, to: distributed-auditing}
  - {rel: depends_on, to: ledger-ecosystem}
  - {rel: depends_on, to: debit-tolerance}
  - {rel: constrained_by, to: "Conformance row 6"}
  - {rel: source, to: "Foundations §3.3"}
  - {rel: source, to: "Foundations §4.4"}
  - {rel: source, to: "Foundations §4.7"}
---
# How a dispute resolves

> **Version:** 0.2
> **Date:** 2026-10-25

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
| Nothing is withdrawn; the rebuttal is appended | **Contest without replacement** — a disputed record is annotated, a superseded one is added beside it (conformance row 6) — and §4.8, no erasure |
| Dated records settle priority | An append-only log with intervals |

#### Where the analogy breaks — and this is the part worth having

**Science can afford an unresolved dispute. An accounting system often cannot.**

A field can stay divided for thirty years and lose nothing. But a purchase either clears or it does not, **now**. You cannot tell a buyer that opinion is divided on whether their debit exceeds what they may carry and to come back when the literature settles.

**The lab framing supplies the epistemics. It does not supply a decision procedure.** So the question is what decides *at transaction time*.

#### The answer is that most disputes never need deciding

Sorting them apart dissolves three of the four classes.

| Dispute about | How it resolves | Needs a verdict? |
|---|---|---|
| **The physical record** — did 70 g of wheat actually move? | **Arithmetic.** IC-1…IC-9 recompute it. **This is not a dispute; it is an error, and recomputation says whose.** | No |
| **The weighting model** — what does a tonne of CO₂ cost? | **Nobody has to accept anyone else's model.** A counterparty re-computes the shared physical record through **its own** weights and decides for itself — OP-14, *comparison never conversion*. Meanwhile §3.3a's replication and rival-sector audit move the field, slowly, the way science does. | **No — and this is the load the framing carries** |
| **An estimate for a dark actor** — what is *Z*? | Published method, replicable (§4.7). The figure is a **floor** that improves (§4.4), not a finding. Better evidence supersedes it. | No |
| **Fraud** — someone recorded events that never happened | **A finding of fact, made by the trust network.** Its own research supersedes the false records, through the correction procedure it publishes (§4.4). The finding can itself be challenged through that procedure. | **Yes** |

> **The insight is that a transaction never waits on a shared verdict.** Each side computes its own answer over the same physical record and decides whether to trade. **Disagreement about weights does not block commerce; it just means two parties price the same thing differently** — which is a fact about models, not a deadlock. **Comparison, never conversion, was always the dispute-resolution mechanism. It had simply never been named as one.**

#### The one residue, and where it goes

**Fraud is the class that needs an actual finding of fact**, and the analogy holds here too: **science is not purely self-correcting about fraud either.** Replication catches error; it does not catch a fabricated dataset that replicates because it was designed to. Science answers with **investigation and retraction, by an institution** — a university integrity office, a funder, a journal.

**Aequitas answers the same way, and the institution is the trust network.** A journal retracts a faked paper from its own pages. A network supersedes false records in its own books, using its own research and its published evidence rules (§4.2, §4.4). **Courts, small claims and contract law continue to exist** (§4.7), and per **§2.6** how an implementer engages them is praxis, not foundations.

**What the accounting contributes is upstream of that.** IC-1…IC-9 make a fabricated record *arithmetically expensive* — a lie must balance mass, balance energy, close origin, close fate, and survive a counterparty's recomputation. **The remaining fraud is the fraud that is internally consistent, which is exactly OP-26's coverage question, answered by measurement against the world rather than by adjudication.**

#### What correction looks like — nothing is reversed

**Catching fraud is the trust network's task** (§4.7), and what it does on finding some is the same thing it does on any other day.

> **The past transaction is not reversed. The network supersedes the false credit records with its own research, and the person's position is re-derived from the log (A6). If their debit is now above what the gate allows, they may have to sell some of what they hold.**

**This is the transaction-time rule (§3.3), not a special fraud procedure.** The gate is evaluated when the transaction happens; a later correction changes what they may carry in *future* and never the validity of a completed act. **Fraud correction is an ordinary supersession that happens to be large:** the same act as replacing any weakly evidenced record with a better one (§4.4).

**And reversal would be wrong, not merely difficult.** The goods moved. You cannot un-eat a sandwich. The counterparty acted on the record as it then stood, shed their property-debit legitimately under custody (§3.2), and was credited for work that really happened. **Unwinding the buyer's fraud would corrupt the seller's books to punish someone else's lie.**

**Four rules govern what happens** (Foundations §4.7):

1. **The network supersedes the false credit records with its own research.** How it ranks evidence is its own published choice (§4.2). The finding is itself a dated record and can be challenged through the network's correction procedure (§4.4).
2. **Finding the fraud is the network's ordinary work.** The people who do it are credited for their hours whatever the finding, and its cost stays with the network like any of its operating costs (§3.2c).
3. **Correcting what the fraud caused is debit on the person who committed it** (A4). Where a legal system that keeps its books in Aequitas spends time and materials on the case, those may land on them too.
4. **A thing handed on during its working life keeps the seller's holding-time share of its creation cost** (§3.2, §4.5). Only the material leaves with it.

**So `C` falls and `D` does not.** If `D ≤ ρ·(C + P)` now fails, discretionary purchases stop. Selling lowers `D` by the material that leaves, and who buys does not matter. After a small fraud that leaves the person within the gate, nothing need be sold. Essentials are untouched throughout: §5.5.4's backstop reaches non-essentials only, and it does so for the fraudster on exactly the terms it does for anyone mis-measured.

#### An example, with the numbers

**A network with ρ = 1.2.** A person's records show `C` = 50,000 h, `P` = 0 and `D` = 52,000 h. **The network finds that 10,000 h of the credit describe work that never happened.** Part of their debit is a boat they have held for 5 years: **6,000 h** of material, and the **8,000 h** that made it, all of it theirs while they are its only holder.

| Step | `C` | `D` | `ρ·(C + P)` | May still carry |
|---|--:|--:|--:|--:|
| Before the finding | 50,000 h | 52,000 h | 60,000 h | 8,000 h |
| The network supersedes 10,000 h of false credit (rule 1) | 40,000 h | 52,000 h | 48,000 h | −4,000 h |
| Correcting what the fraud caused takes 300 h of work and materials (rule 3) | 40,000 h | 52,300 h | 48,000 h | −4,300 h |
| They sell the boat; its 6,000 h of material leaves with it (rule 4) | 40,000 h | 46,300 h | 48,000 h | +1,700 h |

**Their share of the 8,000 h that made the boat stays with them.** It falls as the next holder keeps the boat, and settles at 5 years of the boat's 20-year life: 8,000 × 5 ÷ 20 = **2,000 h** (§4.5). **Had the network found 2,000 h of false credit instead**, the gate would read 1.2 × 48,000 = 57,600 h against 52,300 h, and nothing need be sold.

**In plain words: the false credit comes off, the cost of correcting it goes on, and the person sells only as much as they need to get back within the gate.** No fine is added. The correction debit is work that was really done.

**Three things follow.**

- **Consumption debit cannot be sold off.** If what they took was eaten, burned or emitted, selling does not help — consumption debit is permanent (§3.2). **They are over their ratio and cannot trade their way out.**
- **There is no bankruptcy, because there is no creditor.** A debit is not a bill and nobody collects it (§2.2), so there is nothing to discharge (§3.5).
- **The influence axis corrects the same way.** IC-8 caps cumulative pledges at lifetime earned credit. Superseding false credit can put a person retroactively over that cap; the pledges themselves are permanent and the work they summoned was really done, so nothing unwinds. **They cannot pledge again until their earned credit passes what they have already pledged.** Same mechanism, no second procedure.

> **⚠️ One real load stays, and it is not a weighting dispute.** The pledge-reserve claims process (§4.6) asks whether a *particular past task caused a particular later harm*. Where a physical trace exists, the trace decides and it is arithmetic. **Where it does not, this is a contested finding of fact with no analogue in the list above**, and it is the genuine adjudication load flagged when the reserve was folded. **It routes to existing recourse. Registered; not solved here.**


---

## Related

- [distributed-auditing](distributed-auditing.md) · [retroactive-reweighting](retroactive-reweighting.md) · [derived-ledger](derived-ledger.md)

---
*Status: settled (the four classes) / provisional (causation in the pledge reserve)*
*Source: Foundations §4.7. Text moved from Foundations v0.27 in the 2026-08-27 consolidation; section numbers updated to the new scheme.*
