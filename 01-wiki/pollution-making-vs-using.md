---
title: Pollution from making stays with the maker
summary: Pollution caused by making a thing stays permanently with the maker and never reaches a buyer; pollution caused by using a thing belongs to whoever used it; a thing that will pollute when used carries that future pollution in physical units, and it moves with the thing until somebody uses it.
type: mechanism
ids: [§3.2b]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: no-externalities}
  - {rel: depends_on, to: cost-not-price}
  - {rel: depends_on, to: debit-vector}
  - {rel: implies, to: consumption-debit}
  - {rel: implies, to: organisation-debit}
  - {rel: implies, to: end-of-life-debit}
  - {rel: implies, to: regulator-inversion}
  - {rel: constrained_by, to: "Conformance row 2"}
  - {rel: constrained_by, to: "Conformance row 2d"}
  - {rel: source, to: "Foundations §2.2"}
  - {rel: source, to: "Foundations §3.2b"}
  - {rel: source, to: "Foundations §5.2"}
  - {rel: source, to: "Overview §4"}
  - {rel: source, to: 02-research/Ellerman_labor-theory-of-property.md}
---
# Pollution from making stays with the maker; pollution from using belongs to the user

> **Version:** 0.1
> **Date:** 2026-10-14

> **Three lines govern every case.**
> **1.** Pollution caused by *making* a thing stays with the maker, permanently. It never attaches to the thing and never reaches a buyer.
> **2.** Pollution caused by *using* a thing belongs to whoever uses it.
> **3.** A thing that will pollute when it is used carries that future pollution as part of its debit, in physical units, and it moves with the thing.

## The words this page uses

| Term | What it means |
|---|---|
| **Pollution debit** | Debit for a substance released into the world. Permanent on whoever caused it ([consumption-debit](consumption-debit.md)). |
| **Parcel** | One holding of one substance, such as 40 litres of fuel in one tank, with one record. |
| **Organisation** | Any account that is not a single verified human. Its debit is at all times its members' debit ([organisation-debit](organisation-debit.md)). |

## The rule, case by case

**Line 1.** The farmer keeps the fertiliser runoff; the grocery buyer does not. The gold mine keeps the mining pollution; the ring's owner does not. The refinery keeps its process emissions; the petrol buyer does not.

**Line 2.** Whoever held the fuel parcel and burned it owns the CO₂. **A driver owns the tailpipe, not the carmaker.** The party the books can read is the party who *held the fuel*, never the party who *benefited from the journey*: a shop that fuels its own van carries every gram it burned, and its customers carry none.

**Line 3 is the bookkeeping that makes line 2 workable.** A purchase is an event the books see; a combustion mostly is not. So the future emission is recorded at the hand-off, in litres, and stays attached to the litres. Sell the fuel on and it goes with the fuel. Burn it and it becomes ordinary consumption debit on the burner, permanently.

**Why this follows from A1.** Only people act. The miner acted to pollute; the ring buyer did not cause the mining. Charging the buyer would misattribute responsibility, which is [Ellerman's imputation principle](../02-research/Ellerman_labor-theory-of-property.md). **Cost never flows to whoever did not cause it**, neither downstream to a buyer nor upstream to the first human who ever built anything ([front-loading-rule](front-loading-rule.md)).

## An example, with the numbers

**A grocery co-op of ten members, each working 2,000 hours a year, buys 40 litres of diesel and delivers 2,000 orders.** It sells 10 litres to another haulier and burns the other 30. Burning a litre releases about 2.31 kg of CO₂. *(The 0.05 h/kg remediation rate is illustrative.)*

| | CO₂ | In hours | Who holds it |
|---|--:|--:|---|
| The 10 litres sold on | 23.1 kg | 1.16 h | **The haulier who took the parcel** |
| The 30 litres burned | 69.3 kg | **3.47 h** | **The co-op, permanently** |
| Each member's share, 2,000 ÷ 20,000 = 10% | 6.93 kg | **0.347 h** | Each of the ten |
| The 2,000 customers who received deliveries | **0 kg** | **0.00 h** | **Nobody. They never held the fuel** |

**In plain words: the debit moves while the fuel is still liquid and stops moving the moment it is burned.** Spreading the 3.47 hours across 2,000 orders would put a cost into goods that did not consume it, which A5 forbids.

**Electricity is the same rule and needs no rule of its own.** A generating company buys fuel, holds it, and burns it, so the emission is the company's, divided among its staff by hours worked. A household drawing 300 kWh a month carries only the labour the plant consumed per kilowatt-hour, about **0.03 hours**; a company burning gas that releases a million tonnes a year carries **50,000,000 hours**, 250,000 on each of 200 staff (Foundations §3.2b). **A coal plant becomes hard to staff and a wind farm easy, and nobody banned anything.**

## What this costs, stated

**A consumer's ledger no longer moves when they shift washing from peak to overnight**, so the accounting has stopped supplying a demand-shaping signal. That signal now lives with the generator and with the people who pledge for clean generation (Foundations §3.2b, registered). **And no emission may be attributed by a supply contract.** A contract is paper, and A1 keeps paper off every ledger: **a record of CO₂ must come from a measurement of CO₂.**

## Two things line 3 is not

- **Not part of the thing's cost.** A litre's creation cost and the CO₂ its burning will release are two separate lines on the debit vector ([debit-vector](debit-vector.md)). A5 is untouched.
- **Not a second charge on top of end-of-life.** For a plastic bottle, line 3 and [end-of-life-debit](end-of-life-debit.md) describe one quantity recorded once: line 3 says how it travels, §3.6 says where it lands.

## Depends on

- [material-flow-value](material-flow-value.md) · [no-externalities](no-externalities.md) · [cost-not-price](cost-not-price.md) · [debit-vector](debit-vector.md)

## Consequences

- [consumption-debit](consumption-debit.md) · [organisation-debit](organisation-debit.md) · [end-of-life-debit](end-of-life-debit.md) · [regulator-inversion](regulator-inversion.md)

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.2 (A1 and A5 answer two different questions), §3.2b (the three lines, the delivery round, electricity), §5.2; `Aequitas_Conformance.md` rows 2, 2d*
