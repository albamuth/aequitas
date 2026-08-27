# Privacy is a network choice

> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation.**

> **Moved here from Foundations on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rules stay in Foundations §4.7. This page carries the worked detail and the open questions.**

---

<!-- tag: fnd-s5-3 -->
### 5.3 Privacy — market data public, personal ledgers private

> **The transparency of Aequitas is split by *level*: the market is radically transparent, persons are private.** Pledges, production quantities, hand-offs, and debit-costs — the *supply-and-demand record* — are public (a pledger may be anonymous, like a Kickstarter backer, but the pledge itself is visible). Individual persons' aggregate positions stay private.

This split is **load-bearing, not incidental.** Public market data is what makes §3.3a rival-sector audit and independent economic monitoring *possible at all* — a worker can read how in-demand their product is; an auditor can watch a supply chain; nobody can privately mislabel pledged-vs-speculative work against a public pledge ledger (§4.6). Public flows are the same "make it public so it cannot be gamed in private" move used for co-product splits (§3.4a) and cost constants (§3.3a).

> **⚠️ But transparency *depends on* OP-22 (audit disclosure), it does not bypass it.** Public pseudonymous events can be chain-analysed to de-anonymise a person — the classic ledger-privacy problem. Reconciling **public flows + private persons + unlinkability** is exactly OP-22 (the minimum-disclosure question below). The Kickstarter-anonymous intuition is the right shape; the mechanism is unsolved.

Account holders keep a **private ledger with provable claims** — zero-knowledge proofs of balances and cost positions when transacting, not history.

**This is roughly where society already sits, and that is the point.** People transfer money to each other today knowing their counterparty and nothing about third parties' accounts. Nobody audits those accounts, because validation trust is externalized to banks. **Aequitas does not need more visibility than that; it needs the same visibility with the trust relocated.**

**Aequitas also does not replace existing recourse.** Courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people. The system's contribution is upstream of enforcement: by removing wealth concentration and material insecurity, it **removes most of the motive** for the scams those mechanisms exist to punish.

> **⚠️ The narrow question that remains — OP-22.** The bank analogy has one gap: there is no bank to externalize validation to. Verification is the trust-network ecosystem (Level 2), and an auditor must be able to see *something*. So the live question is not "surveillance or privacy" but **"what is the minimum an auditor must see to verify a claim without seeing a history?"** Zero-knowledge proofs are the right shape of answer and are already specified above; what is missing is the precise disclosure set.

<!-- tag: fnd-s5-3a -->
### 5.3a Privacy is a network choice — Aequitas sets principles, not practice

**The gap in the bank analogy closes by naming what plays the bank's part. It is the trust network.** The network does the tallying and the tracking, so it is the party that holds what is private — and it is therefore the party that decides how privacy works.

> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation. Compatibility between networks is a matter for those networks to negotiate.**

**The working shape is the payment intermediary.** A card network today facilitates a transaction in which **neither party learns the other's private details**. The intermediary knows both sides; the counterparties know a token and an outcome. That is *pseudo-privacy*, it is deployed at planetary scale, and it is the nearest existing analogue of what a Level-2 network does here.

**A network may also choose the opposite.** Radical transparency — no personal privacy at all — is an available and legitimate setting. Nothing in the axioms forbids it. Some communities will want it.

**This is the same move as ρ and the self-care floor `F`.** Aequitas *uses* those dials and never sets their value (§3.5, A8). Privacy is a third dial of the same kind: a network-level choice that the accounting reads and never legislates. **A global privacy constant would be exactly the central authority A8 forbids.**

**Opacity is priced, not forbidden — and that is what stops network-shopping.** A counterparty re-computes a claim through its own model (OP-14) and **discounts what it cannot verify**. So a network that chooses heavy opacity finds its members' claims trade at a discount elsewhere, exactly as a network with thin coverage does (§4.4). **A network's privacy level becomes a priceable property of its output** rather than a rule anyone enforces — the same shape as every other answer in this document: *price the costly path rather than forbidding it at a door somebody has to guard.*

**Three residues, and none of them is small.**

> **⚠️ (a) The network becomes the most information-rich actor in the system.** Whoever tallies, holds. A Level-2 network that keeps its members' lifetime back-traces (§4.4) holds a concentration of *information* comparable to the concentration of *wealth* this project exists to dissolve. §3.3a's public-membership capture screen was written for **sector** capture and does not address **information** capture. **This is P4/OP-10 shaped and it is currently unanswered.** "You may leave" is a weak exit when the thing you would be leaving behind is your life history.

> **🟢 (b) Privacy has a measured coverage cost, and the measured number says the trade-off is not close.** Privacy-preserving verification is dearer than open verification, and that direction is real. **What was wrong was the magnitude, and it was stated backwards.** `06-simulation/residual-unravelling/residual_unravelling.py` sweeps a producer's disclosure cost against a population whose median unit carries about **1.0** in debit. The dark pool still unravels to **0.1% at a cost of 0.40**; it collapses between **0.40 and 0.80**. Realistic disclosure costs sit near **0.002** (§4.3). **So the failure point is roughly 200 times higher than anything a working network would report**, and a privacy practice would have to be some two hundred times dearer than open recording before coverage suffered at all. **A network should still publish what its practice costs (§4.3, §4.7); it does not have to trade coverage away to have one.** *Earlier drafts of this residue said the residual rule "stops unravelling" above 40%. It does not — at 40% it still reaches 0.1%, in 18 rounds rather than 13. Corrected 2026-08-24.*

> **⚠️ (c) A network's choice binds members who did not make it.** Children born into a radically transparent network, and people who joined before a practice changed, did not choose it. Entry, exit, and the portability of a personal record across a privacy boundary are **C2 questions**, and this ruling adds them to C2's list.

**What is settled and what is not.** *Who decides* is settled: the network. *What Aequitas mandates* is settled: principles, not practice. **What remains open is the minimum disclosure set itself** — what an auditor must see to verify a claim without seeing a history — which stays a C7 implementation problem, now with a named holder and a priced trade-off attached.

---


---

## Related

- [ledger-ecosystem](ledger-ecosystem.md) · [distributed-auditing](distributed-auditing.md) · [statistical-coverage](statistical-coverage.md)

---
*Status: provisional — the minimum disclosure set is OP-22 and is unsolved*
*Source: Foundations §4.7. Text moved from Foundations v0.27 in the 2026-08-27 consolidation; section numbers updated to the new scheme.*
