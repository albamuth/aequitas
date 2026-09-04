# Rival-Sector Audit

<!-- struck-ok: this box quotes the withdrawn proposal in order to withdraw it -->
> ## ⛔ WITHDRAWN AS A MECHANISM, 2026-08-24
>
> **This page describes a proposal that does not work. It is kept because the reasoning is worth reading and because the problem it was answering is still open.**
>
> **The proposal was:** *the natural auditor of a cost constant is the rival sector, not the consumer.* If beef's energetics are understated, plant-protein producers are harmed and will fund the replication.
> <!-- struck-ok: stating the withdrawn proposal in order to withdraw it -->
>
> **Two objections, and the second sinks it.**
>
> 1. **Rivals are often absent.** A good with no substitute has no rival, and **a constant cutting across every sector equally has no rival by construction.**
> 2. **A rival's best move is not to fund your correction.** Funding a replication costs real hours and the benefit is **shared with every other producer in the rival sector**. Getting their own constant set generously is cheaper and the benefit is private. **So the equilibrium is mutual understatement, not mutual policing.**
>
> **And it failed hardest where the stakes are highest.** The **ambient-stock and baseline constants** are the largest levers in the weighting model, and **they have no rival at all** — everyone benefits from a high pollution baseline and a low stock reading.
>
> **What is true now.** Rival-sector audit is **one pressure among several, not a mechanism.** How a trust network audits its cost constants is a network-design problem held to five published requirements — [Foundations §3.3a](../00-strategy/Aequitas_Foundations_v0.39.md), open problem **OP-24 (understatement drift)**.
>
> **One narrow case survives**, and it is worth knowing: **coverage** has two parties with a private interest in getting it right — the instrumented producer, harmed when undocumented produce prices too cheaply, and the dark producer, who cannot transact until they onboard. **The audit of *extent* has interested parties. The audit of *weight* does not.**

## The problem it solves

[retroactive-reweighting](retroactive-reweighting.md) makes cost constants extraordinarily powerful. Whoever publishes the energetics of a process sets every [co-product-allocation](co-product-allocation.md) split in that sector — **backwards through all of history.** That is a capture surface, and it needs an answer that is not a standards body.

**One channel closes for free, and it is worth claiming.** There is no market-dominating corporation to fund a favourable result, because [cost-not-price](cost-not-price.md) removes the profit that pays for captured science today. Labs are credited by trust networks for doing the work. **The Enron-shaped failure cannot operate the same way here.**

**But the obvious fix introduces its mirror.** A general-membership trust network is dominated by the *consuming* side of any given good — everyone eats beef, few raise cattle. Its members therefore collectively benefit from beef's debit being **understated**. And the incentive to correct runs one way only:

| Error direction | Who wants it fixed | Result |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Corrected |
| Constant **understates** debit | Nobody — correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

**Result: systemic drift toward under-costing** — precisely how every carbon-accounting regime attempted so far has failed. What makes it insidious is that **no equation breaks.** [material-flow-value](material-flow-value.md) tolerates it arithmetically; it simply erodes [no-externalities](no-externalities.md), quietly, forever.

**Aggravating factor: replication cost is asymmetric.** Competing networks discipline *estimates* cheaply — re-interviewing a farmer costs little. They do not discipline *constants*: re-running calorimetry is expensive. So the competitive pressure that works everywhere else in the system is weakest exactly here.

## The mechanism

> If beef's energetics are understated, **plant-protein producers are materially harmed** and will fund the replication.

Every constant has a party who benefits from it reading lower and a party who benefits from it reading higher. Naming the second party turns a one-way asymmetry into a two-sided market.

Three supporting rules:

1. **Two unaffiliated replications before a constant may re-weight history.** Retroactivity is too powerful to trigger from a single source.
2. **Audit triage weights magnitude × concentration of beneficiary**, not magnitude alone. Materiality thresholds by themselves *help* an attacker, whose job then becomes making the falsification look immaterial.
3. **A trust network concentrated in the sector it audits is captured by construction.** Membership composition is public in the log, so this is a **detectable screening property**, not a rule anyone must enforce.

## Why it is the right shape for Aequitas

- **Decentralized.** No authority, no standards body, no appointed reviewer. It is an incentive, not an enforcement rule.
- **Self-funding.** The replication is credited work paid for by a party with a real stake — it passes *"does this need a Paul Glover?"* without help. See [distributed-auditing](distributed-auditing.md).
- **Already implied by an axiom.** [cost-not-price](cost-not-price.md) removes profit *in exchange* while explicitly preserving **competition on quality, artfulness and efficiency** (Foundations §5.1). Rival-sector audit is that competition applied to the cost model itself.

## Why the co-op form is not the fix

A tempting answer: *trust networks are co-ops funded by member pledges, so they have no profit motive to be lenient.*

**The conflict is directional, not monetary.** [Arthur Andersen](https://en.wikipedia.org/wiki/Arthur_Andersen) was paid by Enron; making Andersen a co-op **owned by its clients** would have been worse, not better. Removing the profit motive leaves the leniency motive intact — which is the whole history of issuer-pays arrangements, from audit firms to [credit rating agencies before 2008](https://en.wikipedia.org/wiki/Credit_rating_agencies_and_the_subprime_crisis).

See `../00-strategy/GLOSSARY.md#src-auditor-independence`.

## Where it fails

**It assumes a rival sector exists and is dense enough to fund replication.** For beef versus plant protein, plausible. For a good with no substitute, or a constant that cuts across all sectors equally, **there is no rival and therefore no auditor.**

**Test:** simulate a population of trust networks under this incentive structure and find the rival density at which the drift stops being arrested.

## Depends on

- [retroactive-reweighting](retroactive-reweighting.md) — the thing that makes constants worth capturing
- [cost-not-price](cost-not-price.md) — closes the funding-bias channel, and supplies the rivalry
- [distributed-auditing](distributed-auditing.md) — auditing is credited work

## Consequences

- [co-product-allocation](co-product-allocation.md) — the splits this protects
- [protocol-governance](protocol-governance.md) — a partial answer to the largest hole in A8

## Open questions

- **OP-24 — understatement drift.** The fix above is proposed, not proven.
- What audits a constant with no rival sector?
- Does rival-sector auditing produce its own arms race — two sectors funding duelling constants with no convergence?

---
*Status: **WITHDRAWN as a mechanism, 2026-08-24.** Kept as the record of a proposal that does not hold. See the box at the top. The problem it answered is open — **OP-24**.*
*Source: `00-strategy/Aequitas_Foundations_v0.4.md` §3.3a; `Aequitas_Objections_v0.9.md` OA3, OA10*
