---
title: End-of-life debit
summary: An object nobody will take on has been consumed by its last holder, who carries its end-of-life debit permanently; a discarded object is itself a pollutant for as long as it persists; recycled material carries its property debit forward but never the original producer's process pollution.
type: mechanism
ids: [§3.6]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: cost-not-price}
  - {rel: depends_on, to: pollution-making-vs-using}
  - {rel: depends_on, to: retroactive-reweighting}
  - {rel: implies, to: consumption-debit}
  - {rel: implies, to: land-and-remediation}
  - {rel: constrained_by, to: IC-4}
  - {rel: constrained_by, to: "Conformance row 7"}
  - {rel: open_under, to: OP-25}
  - {rel: source, to: "Foundations §2.4"}
  - {rel: source, to: "Foundations §3.6"}
  - {rel: source, to: "Overview §4"}
  - {rel: source, to: 02-research/Data_plastic-lca-cleanup.md}
---
# End-of-life, recycling, and product-as-pollution

> **Version:** 0.1
> **Date:** 2026-10-14

> **An object's life does not end when it stops being useful.** Three rules govern what happens then.
> **1.** If nobody will accept a worn-out thing, its last holder has consumed it and holds its end-of-life debit forever, as if it were food.
> **2.** A discarded object is itself a pollutant for as long as it persists, borne by its final holder, weighted by the ambient stock.
> **3.** Recycled material carries its property debit forward, and never the original producer's process pollution.

## The words this page uses

| Term | What it means |
|---|---|
| **Property debit** | The debit of a thing you hold. Its material moves with the thing ([property-debit](property-debit.md)). |
| **Consumption debit** | Debit for what you used up, burned or released. Permanent on the causer ([consumption-debit](consumption-debit.md)). |
| **Stock rule** | A pollutant's weight floats with how much of it is already in the world above what nature clears unaided ([retroactive-reweighting](retroactive-reweighting.md)). |
| **Custody follows possession** | Taking a thing means taking the debit that rides with it. **Nobody can be made to receive anything** (Foundations §2.4). |

## The rule

**Rule 1 turns three ordinary incentives on, and none of them asks anyone to be virtuous.**

- **Prefer durable, repairable goods.** A cheap gadget whose disposal cost you will be holding is not the cheap option.
- **Maintain what you hold.** A co-operative is better off servicing its equipment than running it to failure.
- **Pledge toward remediation and recycling.** Doing so lightens your own accumulated pollution debt, because the stock everyone is weighed against falls.

**Rule 2 is one mechanism, not two.** Atmospheric CO₂ and a bottle in a landfill are the same stock-dependent rule. A compostable object generates none of it, because nature remediates it unaided. **This is the same quantity that rode the object as latent pollution while it was held** ([pollution-making-vs-using](pollution-making-vs-using.md), line 3), arriving at the end of its journey. It is recorded once, not twice.

**Rule 3 is why recycling pays.** Recycled steel never carried the miner's tailings, because that pollution stayed permanently on the miner, and using it commissions no new extraction. The recycler is credited for the work of making waste useful again, and the recycled material re-enters as a low-cost input.

## An example, with the numbers

**A washing machine of 60 kg of steel and 10 kg of plastic reaches the end of its life.** *(Hour rates illustrative.)* Remediating steel in the environment is read at 0.02 h/kg and plastic at 0.30 h/kg.

| What the last holder does | What they carry afterwards |
|---|---|
| Hands it to a recycler who accepts it | **0 h of end-of-life debit.** The 70 kg of property debit moved with the machine. |
| Nobody will take it, so it goes to landfill | 60 × 0.02 + 10 × 0.30 = **4.2 h, permanently**, floating with the stock. They have consumed the machine. |
| Dumps it in a field | **4.2 h, permanently, if the abandonment is traced to them.** Tracing it is OP-25. |

**Now the recycler.** They spend 1.5 hours dismantling it and recover 58 kg of steel.

| | |
|---|---|
| Credit to the recycler | **1.5 h** |
| Property debit the 58 kg carries forward | the steel's accumulated material and making, **plus 1.5 h** |
| The original mine's process pollution carried by that steel | **0 h.** It stayed on the miner |
| The 2 kg of steel lost and the 10 kg of plastic with no taker | **consumption debit on the recycler**, who last held it |

**In plain words: whoever is holding a thing when it runs out of takers has eaten it.** The way out is a real new holder, never a fence or a stranger's doorstep.

## What stays open

**Rules 1 to 3 price lawful disposal correctly. They do not by themselves stop illicit dumping**, abandoning an object in the environment to escape its end-of-life debit. Attributing an abandonment back to the abandoner is a trust-and-provenance problem at the second rung of the [verification-ladder](verification-ladder.md), registered as **OP-25**.

## Depends on

- [material-flow-value](material-flow-value.md) · [cost-not-price](cost-not-price.md) · [pollution-making-vs-using](pollution-making-vs-using.md) · [retroactive-reweighting](retroactive-reweighting.md)

## Consequences

- [consumption-debit](consumption-debit.md) — an unwanted object becomes permanent consumption debit
- [land-and-remediation](land-and-remediation.md) — a building's occupation debt behaves the same way and clears only by remediating

---
*Status: settled (rules 1 to 3) · OP-25 open (illicit dumping)*
*Source: `00-strategy/Aequitas_Foundations.md` §2.4 (nobody can be made to receive anything), §3.6; `Aequitas_Conformance.md` row 7 (everything the books track has an end)*
