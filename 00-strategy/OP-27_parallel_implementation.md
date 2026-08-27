<!-- tag: op27-parallel-implementation -->
# OP-27 — Parallel implementation: living in both economies at once

> **Date:** 2026-08-23
> **Raised by:** the author. **Ruled by the author the same day.**
> **Status:** 🟢 **Ruled and stress-tested. Passes.** One capture surface named and routed; one residual flagged.
> **Reads against:** `Aequitas_Foundations_v0.28.md` A1, A2, A3, A5, A7, §3.2, §3.2b, §3.6, §4.1, §4.4, §4.8, §4.6, §5.5, §11 · `Aequitas_EventLog_v0.10.md` §12.3a
> **Supersedes the open version of this paper**, which argued §3.2 and §3.2b contradict each other at the boundary. **They do not. The objection is answered in §3 below.**

---

## 0. The ruling

**Two directions across the boundary, and both are deliberately costly.**

> ### Selling **into** Aequitas, from money-made goods
> A good whose inputs never passed through an Aequitas hand-off is **dark until it is sold into Aequitas.** At that hand-off the maker either **onboards the good properly** — full origin-chain records — **or applies a pre-approved template** that assigns it a debit-cost immediately, so the transaction can complete without delay.
>
> The maker spent money making it and **receives no money for it.** They lose money. **That is the disincentive, and it is on purpose.**

> ### Selling **out** of Aequitas, for money
> The seller may do it. **The debit stays with them.** To the trust network the seller **made a gift**, and **the network does not acknowledge the money changing hands at all.**
>
> **That is also the disincentive, and it is also on purpose.**

**Neither direction is forbidden. Both are dearer than trading inside.** That is the adoption gradient, and it is the same shape every other answer in this project takes: *price the costly path rather than forbidding it at a door somebody has to guard.*

---

## 1. Nothing here is a new rule

Both halves fall out of axioms that were already written.

| The ruling says | Which is already | Where |
|---|---|---|
| The network does not acknowledge the money | **A1's corollary, word for word.** Financial instruments are not matter or energy, so they *"never appear on any ledger."* | A1 |
| A good with no origin records is estimated | **§12.3a, already settled 2026-08-22.** No records ⇒ cost estimated exactly as all dark production is. | EventLog §12.3a |
| The template is that estimate, pre-computed | **§4.4's estimation rule, cached** so a transaction need not wait for a reconstruction. | §4.4 |
| Handing a good outside keeps its debit on you | **§3.2, unchanged.** *"There is no exit through a non-participant."* | §3.2 |
| Selling outward reads as a gift | **§4.8.** The gift economy always exists and never closes. | §4.8 |

**So the only genuinely new object is the template**, and it is a cache of an existing rule rather than a new mechanism. **No axiom moved.**

---

## 2. Why the template matters more than it looks

**Without it, every cross-boundary sale would need an origin-chain reconstruction before the trade could clear.** That is a delay at the exact moment a stranger is deciding whether this system is usable. **A pre-approved, published, per-class figure means the transaction completes now** and the good's cost is honest-but-coarse rather than absent.

**Two rules it must carry, both inherited rather than invented:**

1. **It errs against the seller.** §4.4's conservative-count rule: under-count the dark, because *"the self-liquidating error is the safe one."* A template must be **dearer than a real record** — otherwise onboarding properly never pays and the template becomes the preferred route.
2. **It is published, with its method and its vintage.** §4.7. A template nobody can re-derive is an authority assertion.

---

## 3. The objection I raised, and why it fails

**I argued** that §3.2 and §3.2b give opposite answers, and that keeping the debit on an outward seller creates an anti-adoption gradient: outbound debit scales with output, credit is capped at 24 h per person per day (IC-7), **so any producer selling mostly outward eventually crosses `D > ρ·C` and is locked out "for succeeding."**

**The arithmetic is right and the conclusion is wrong, for three reasons.**

**1. They are not contradictory, because they govern different debits.** §3.2 governs **property** debit — the atoms you hold — which is dischargeable on transfer. §3.2b governs **consumption and pollution** debit, which never transfers. An outward sale is a property question, and §3.2 answers it. §3.2b was never in play.

**2. A locked-out seller is not a deprived seller. They got money.** The gate restricts *discretionary consumption inside Aequitas* and never touches essentials (§5.5). Someone who sells everything for money has a money income and can spend it in the money economy. **They have not been impoverished; they have declined to be inside.** That is what a parallel system means, and it would be strange for it to mean anything else.

**3. The lock-out is reversible, and reversing it is exactly the behaviour the system wants.** Property debit discharges the moment a real holder takes the thing on (§3.2). **Sell one batch inward and the ledger lightens.** So it is a gradient, not a trap — pressure toward inside trade, applied continuously, with the exit always open.

> **The dumping counter also disappears**, because it only ever existed under the A7 reading this ruling rejects. **If handing a thing outside never discharges its debit, there is nothing to dump.** §3.2 does the anti-dumping job it was written for, and OP-25 is untouched.

---

## 4. Stress test

### The strongest result: money cannot buy Aequitas standing

**Follow the money through the inbound case and watch it fail to buy anything.**

A wealthy person pays 100 workers **in money** to produce goods, then sells those goods into Aequitas.

- **The workers** are credited for **their own hours** — credit records who was responsible, and responsibility is a fact about a person (A2, A3, Ellerman imputation under A1).
- **The financier** did not work the hours. **They are credited nothing.**
- The goods' property debit passes to whoever takes them.
- The financier is out the money and holds no credit.

> **So there is no channel from money to credit, at any scale.** You cannot buy hours, because credit is *a record that a specific person spent a specific hour* and IC-7 caps every account at 24 hours per day regardless of who paid. **The boundary is permeable to goods and impermeable to standing.**

### Exploit 1 — extract at cost, sell at market

**The real attack, and the one worth taking seriously.** Aequitas prices at cost (A5). The money economy prices at market. **Anything whose market price exceeds its Aequitas cost is an arbitrage:** buy inputs inside cheaply, sell outputs outside at a profit, and shrug at the ledger penalty because you do not care about your Aequitas standing.

**It self-limits, and the limit is proportional to the extraction.**

- Buying inside **takes on** the property debit of what you bought.
- Selling outside **never discharges it** (§3.2, the ruling above).
- So `D` grows monotonically with every unit extracted, while `C` grows only with the extractor's own hours, capped at 24 per day.
- **`D ≤ ρ·C` fails, and the extractor can no longer acquire the inputs they were extracting.**

> **The extractor's own gate shuts them out of the supply they are draining, and it shuts faster the harder they pull.** Nobody enforces it and nobody has to notice.

### Exploit 2 — a chain of shells

Extractor A buys inside and sells to shell B, also inside; B sells outward and absorbs the ruined ratio; A stays clean; spin up a new shell.

**Partly answered, and the remainder is flagged.** Each shell must be a real verified account, and **one verified human is one account** (§4.1) — so a chain of shells is a chain of real people each burning their own standing, in public, on a ledger anyone can read. Membership and flows are visible (§4.7).

> **⚠️ Residual, and it is genuinely open: entities are not persons.** Whether a *co-op* can be spun up repeatedly the way an account cannot is a **C6 (identity)** question and a sibling of **OP-25 (illicit dumping)**. **Registered, not solved here.**

### Exploit 3 — template capture

**Whoever sets the templates sets the price of entry for every dark good in that class.** Set them low and money-economy goods flood in cheap, undercutting the instrumented Aequitas producer who paid to measure their own supply chain.

**This is OP-24 (understatement drift) at the boundary, and it inherits OP-24's answer** (§3.3a): the natural auditor is **the rival producer**, who is materially harmed by cheap undocumented goods and will fund the replication. Templates are published with method and vintage (§4.7), and two unaffiliated replications are required before a constant re-weights history.

> **⚠️ Name it plainly: the template list is a capture surface, and it is OP-10 shaped.** It is disciplined by the same machinery as every other cost constant, and it should be worked with OP-10 and OP-24 rather than treated as separate.

### Exploit 4 — template shopping across networks

Pick whichever network publishes the cheapest template for your good. **This is OP-14 (cohort shopping) exactly**, and it is arrested the same way: a counterparty re-computes through its own model and discounts what it cannot verify (§4.2, *comparison never conversion*).

---

## 5. Screening

| Test | Verdict |
|---|---|
| **Universality** | ✅ **Pass, and this is the strong part.** No special rule for cross-boundary trade exists or is needed. Money is invisible because it is not matter (A1); the good left the records, so §3.2 applies. **The ordinary rules already cover it.** |
| **Decentralization** | ✅ Templates are published and re-derivable. No authority decides whether a sale was "genuine". |
| **Fecundity** | ✅ **Both directions push toward inside trade, continuously, with the exit always open.** This is the adoption engine the parallel phase needed. |
| **Who games this?** | ✅ Named above. The extractor self-limits; the shell chain is flagged as a C6 residual; template capture routes to OP-24/OP-10. |
| **Paul Glover?** | ✅ Template maintenance is credited work like any audit (§4.7: funding is recognition, not a budget). It pays its own maintainer. |
| **Objective function?** | ✅ None. Nothing is maximised. |
| **Physical trace** | ✅ The good physically left, and the trace is what the template prices. **The money left no trace in matter or energy, which is exactly why the ledger cannot see it.** |

---

## 6. What a simulation must now express

The outside-world plug (roadmap step 4) needs:

- **A boundary with agents on both sides**, and trade in both directions.
- **Inbound sales priced by template**, with the template's conservatism as a dial — because §4.4 says it must err against the seller, and *how much* is the question.
- **Outbound sales that keep the debit**, so a participant's ratio degrades with outward trade.
- **A supplier graph with tunable loop density**, since OP-27 predicts that **which industries start inside matters more than how many participants there are.** WIR and Sardex started business-to-business inside dense input loops; Ithaca HOURS died with businesses holding scrip their suppliers would not take.
- **An extractor policy**, to watch Exploit 1 self-limit and measure how fast.

---

## 7. What is settled and what is not

**Settled.** Both directions across the boundary, the template as the mechanism that lets a cross-boundary sale clear immediately, money's invisibility to the ledger, and that the disincentives are deliberate.

**Open, and both routed rather than orphaned.**

1. **Repeat-shell entities** — a co-op is not a person, and §4.1's one-human-one-account does not obviously bound how many can be created. **C6 / OP-25.**
2. **Template capture** — who sets the entry price for dark goods. **OP-24 / OP-10.**

**Recommendation: fold §0–§3 into Foundations** as the parallel-implementation section it does not yet have, with the two open items registered rather than buried. **The stress test in §4 is what earns the fold; it is not a formality, and the extraction exploit is the reason the fold is safe rather than merely tidy.**
