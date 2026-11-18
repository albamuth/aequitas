---
title: Pollution from making stays with the maker
summary: Pollution goes with the thing that causes it, to whoever uses that thing up; pollution from what a maker uses up stays permanently with the maker; pollution caused by using a thing belongs to whoever used it; a thing that will pollute when used carries that future pollution in physical units; and pollution that a thing's own material gives off in becoming that thing moves with the thing to whoever holds it.
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

> **Four lines govern every case, and one idea is behind all four: pollution goes with the thing that causes it, to whoever uses that thing up.**
> **1.** Pollution from what a maker *uses up* to make a thing stays with the maker, permanently. Fuel, power and chemicals are the usual cases. That pollution never attaches to the thing the maker sells, and it never reaches a buyer.
> **2.** Pollution caused by *using* a thing belongs to whoever uses it.
> **3.** A thing that will pollute when it is used carries that future pollution as part of its debit, in physical units, and it moves with the thing.
> **4.** Pollution that a thing's own material gives off in becoming that thing is part of the thing's debit, and it moves with the thing.

## The words this page uses

| Term | What it means |
|---|---|
| **Pollution debit** | Debit for a substance released into the world. Where it came from something a person used up, it is permanent on that person ([consumption-debit](consumption-debit.md)). Where it belongs to a thing, it moves with the thing (lines 3 and 4). |
| **Parcel** | One holding of one substance, such as 40 litres of fuel in one tank, with one record. |
| **Organisation** | Any account that is not a single verified human. Its debit is at all times its members' debit ([organisation-debit](organisation-debit.md)). |
| **Uses up** | Consumes a thing so that it is gone afterwards. A kiln uses up its fuel. A farmer uses up fertiliser. |
| **Make-up** | What a material consists of, by weight. Limestone is CaCO₃, and 44% of its weight is CO₂ that leaves when it is fired. |

## The rule, case by case

**Line 1.** A maker is the last user of its fuel, its power and its chemicals, so line 1 is line 2 applied to a maker.

- The farmer spread the fertiliser, so the farmer used it up. The farmer keeps the runoff, and the grocery buyer does not carry it.
- The gold mine keeps the pollution of the fuel, the explosives and the chemicals it uses up. The ring's owner does not carry it. The waste rock is a different record, and line 4 covers it.
- The refinery keeps the emissions of running the refinery. The petrol buyer does not carry them.

**Line 2.** Whoever held the fuel parcel and burned it owns the CO₂. **A driver owns the tailpipe, not the carmaker.** The party the books can read is the party who *held the fuel*, never the party who *benefited from the journey*: a shop that fuels its own van carries every gram it burned, and its customers carry none.

**Line 3 is the bookkeeping that makes line 2 workable.** A purchase is an event the books see; a combustion mostly is not. So the future emission is recorded at the hand-off, in litres, and stays attached to the litres. Sell the fuel on and it goes with the fuel. Burn it and it becomes ordinary consumption debit on the burner, permanently.

**Line 4 puts a thing's own pollution on the thing.** Cement is made by firing limestone. The limestone breaks down in the kiln: CaCO₃ → CaO + CO₂. By the weights of the atoms, **100 kg of limestone gives 56 kg of lime and 44 kg of CO₂.** The kiln also burns fuel. *(The fuel figure is illustrative.)*

| The CO₂ | Amount | Who holds it |
|---|--:|---|
| Given off by the limestone as it becomes lime | **44 kg** | **The cement, and then whoever holds what is built with it** (line 4) |
| Given off by the fuel that heats the kiln | 30 kg | **The kiln's people, permanently** (line 1) |

**In plain words: the maker chose the fuel and could have chosen another, so the fuel's pollution is the maker's. No maker can turn this limestone into lime without making the 44 kg, so that pollution belongs to the product.** A maker has a reason to run a process that pollutes less. A buyer has a reason to choose a product that pollutes less by its nature.

## The test for line 4

> **A release is the thing's own when it is made of the thing's own material, and the make-up of that material fixes the amount.** What a maker uses up to run the process is the maker's (line 1).

| | The rule | Why |
|---|---|---|
| **The ceiling** | The amount is at most what the material's make-up fixes: 44 kg of CO₂ for every 100 kg of limestone. A release above that came from something the maker used up, and it falls under line 1 | Without a ceiling, a maker could report its fuel's pollution as the product's |
| **The record** | What rides the thing is what was measured as released. A release that a maker captures is not recorded | A record of CO₂ must come from a measurement of CO₂ |
| **Counted once** | The part that rides the thing is not also on the maker | A ledger walk counts a parcel once ([co-product-allocation](co-product-allocation.md)) |
| **Where the make-up fixes no amount** | The amount is a number the network publishes, with its method and its uncertainty | It is a cost constant, and it has the weakness of every cost constant ([op-24](op-24.md)) |

**Four cases against the test.**

| The release | Made of the thing's own material | Does the make-up fix the amount | Whose |
|---|---|---|---|
| CO₂ from limestone as it becomes cement | Yes | Yes: 44 kg for every 100 kg | **The cement's** |
| CO₂ from coke in a blast furnace | No. The carbon is the coke's, and the coke is used up | — | **The steel maker's** (line 1) |
| Waste rock from gold ore | Yes | Yes: the weight of the ore, less the weight of the gold | **The gold's** |
| Methane from cattle | Yes. Its carbon is the feed's, and the feed becomes the animal | No. It changes with feed and breed | **The beef's, at a number the network publishes** |

**Worked, for the gold.** Ore that holds 1 gram of gold in every tonne leaves about 1 tonne of waste rock for every gram. A ring of 10 grams has about **10 tonnes** of waste rock in its record, and that record goes to whoever holds the ring. The mine's fuel and chemicals stay with the mine's people. *(Illustrative ore grade.)*

**The name of a product does not enter the test.** A steel maker cannot pass it by calling the product "blast-furnace steel". The test reads where the carbon came from.

## Why the lines fall where they do

**Lines 1 and 2 follow from A1 (materialism of cost).** Only people act. The miner burned the fuel, and the ring buyer did not. Charging the buyer for it would misattribute responsibility, which is [Ellerman's imputation principle](../02-research/Ellerman_labor-theory-of-property.md). **The cost of what a person used up never flows to somebody who did not use it up**, neither onward to a buyer nor back to the first human who ever built anything ([front-loading-rule](front-loading-rule.md)).

**Lines 3 and 4 follow from A5 (cost, not price).** A4 (no externalities) asks who caused a consequence. A5 asks what a thing is made from, and who holds it. The 44 kg are 44% of the limestone that went into the kiln, so they are part of the material the cement consumed. They ride the cement as its material does, and a buyer takes them on by accepting the cement (Foundations §2.4a, the consent rule). **Line 4 never rests on the buyer having caused the firing.** A customer who orders a delivery carries none of the van's fuel, because the customer never held that fuel.

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
*Source: `00-strategy/Aequitas_Foundations.md` §2.2 (A1 and A5 answer two different questions), §2.4a (consent), §3.2b (the four lines, the test for line 4, the delivery round, electricity), §5.2; `Aequitas_Conformance.md` rows 2, 2d*
