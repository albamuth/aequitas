# Verification Ladder

> A four-level maturity model for establishing that a recorded event actually happened. Each rung is independently viable, so Aequitas can start today at Level 1 and get rigorous later.

## The four levels

| Level | Method | Infrastructure | Weakness |
|---|---|---|---|
| **1** | Peer / witness attestation, multi-party sign-off | None. Works in any village on Earth today. | **Collusion** |
| **2** | Reputation + stake over a social graph; the graph audits attestation patterns | Social-graph data | The hard one — see below |
| **3** | Sensors + cryptographic proof (meters, cameras, GPS, telemetry), signed and tamper-evident | Heavy | Cost; sensor capture |
| **4** | Agentic auditing — autonomous continuous tallying of the full logistical record | Far future | Speculative |

## Design rule

Every level must produce records **interoperable with every other level**, and the system must **degrade gracefully downward**. A Level 3 region and a Level 1 region must be able to trade.

This is not a nicety. Without it, high-verification regions get a systematic advantage over low-verification ones and Aequitas reproduces the development gradient it exists to remove.

## Why it works this way

It is what makes the system adoptable **without permission and without infrastructure**. A theory that requires sensors everywhere before it works is a theory that never starts.

It is also the fecundity engine on the technical side: each rung creates real demand for the next.

## Level 2 is emergent, not designed

Level 2 is **not a fraud detector to be specified in advance.** It is what [distributed-auditing](distributed-auditing.md) grows into: competing trust networks, staffed by people credited for the work of auditing, that participants choose between.

Designing a central detection apparatus would recreate the authority A8 forbids, and no detector stays ahead of attackers permanently. The defensible position instead rests on three things:

1. **Arithmetic audits need no trust model at all** — 24-hour limits, mass/energy balance, provenance closure. Cheap, universal, and they catch the easy fraud for free.
2. **Auditing is credited work**, so verification capacity scales with adoption ([distributed-auditing](distributed-auditing.md)).
3. **The payoff from undetected fraud is structurally tiny** ([disparity-ceiling](disparity-ceiling.md)), so the arms race matters far less than it would in a currency system.

Prior art worth mining when the ecosystem question becomes concrete: EigenTrust, SybilGuard, proof-of-personhood (BrightID, Idena, World ID). See `02-research/`.

*Superseded framing:* earlier drafts treated Level 2 as a designed anti-collusion mechanism and the project's highest risk. That framing put fraud speculation ahead of defining the system, and assumed cheating where the real question is incentive.

## What a check costs, rung by rung

> **Moved here from Foundations §4 on 2026-08-27, when §4, §5 and §6 were consolidated. The rule stays in Foundations §4.3. This page carries the worked detail.**

**A rung has two prices, and they move in opposite directions.**

| Price | What it is | As you climb the ladder |
|---|---|---|
| **Setup** | The tools you must buy once | **Rises** |
| **Marginal** | The work each further check takes | **Falls** |

**Climbing the ladder buys cheaper checking, and you pay for it in tools.** A person must look at every item. A tool looks at every item by itself.

**The setup price never lands on the goods.** Tools are paid for when bought and sit on the asset, shared among its holders by how long each held it. **A tool's cost is never divided into the things it measured.** See [property-debit](property-debit.md).

**And a check is often not an extra act.** For goods the basic check is free, because the hand-off *is* the check: the receiver, by taking the goods and their debit, attests the goods exist.

### The full table

A farm ships **1,000 sacks** in a season. Each sack computes to about **10 hours**, so the season is about **10,000 hours** of grain.

| Rung | What actually happens | Per season | Per sack | Share of the 10 h |
|---|---|---|---|---|
| **1 — the receiver signs for what they take** | This *is* the trade. No second act. | 0 h | 0 h | **0%** |
| **2 — the network checks the method by sampling** | Desk work. Field area × known yield per acre, against the loads the carrier recorded. **It never touches a sack.** | 2 h | 0.002 h | **0.02%** |
| **3 — a scale on the loading dock** | Bought once, sits on the asset, reads every load by itself. Only calibration is labour. | 0.5 h | 0.0005 h | **0.005%** |
| **4 — a machine tallying continuously** | Machine time only. | 0.1 h | 0.0001 h | **0.001%** |

**Read the last column downward. It falls.** Checking gets *cheaper* per unit as you climb, not dearer.

**Note row 2.** A network audit is **cheaper per sack than a person watching sacks**, because it works on totals and cross-checks rather than on items. It reads the size of the fields, what an acre of that crop is known to yield, and what the carrier recorded leaving the gate. **Three numbers that must agree.** Counting sacks would be the expensive way to learn less.

### A large checking cost is a warning sign, not a design regime

Suppose a producer reports that self-tracking costs **40%** of what they produce. On this farm that is **4,000 hours** to keep records on 10,000 hours of grain.

**The network does the same job in 2 hours. That is a 2,000-fold gap.**

**No honest process costs that.** Overheads of that size belong to bureaucracy, not to measurement. **A network seeing such a figure should audit the producer, not redesign the ladder around them.**

**And the system already reaches it.** Verification work is credited work, so inflating it is a way to claim hours — the unobservable-work problem, answered by weighting a weak claim near zero and by the 24-hour-a-day cap. **The party harmed is the rival producer whose own overhead is 0.02%.**

### The measured threshold, and how to read it

`06-simulation/residual-unravelling/residual_unravelling.py` sweeps a producer's disclosure cost against a population whose median unit carries about **1.0** in debit.

| Disclosure cost | What happens to the dark pool |
|---|---|
| **0.002** — the row-2 figure above, and what a working network would report | Unravels to 0.1% |
| **0.40** | Still unravels to 0.1%, in 18 rounds rather than 13 |
| **between 0.40 and 0.80** | Collapses |

> **The measured failure point is roughly 200 times higher than anything a working network would report.**

**Read that as reassurance about the mechanism, not as a live constraint on it.** The estimation rule keeps working across the whole range of realistic costs, and it fails only in a regime that would itself be evidence of something wrong. **Earlier drafts read this backwards and said the rule "stops working above 40%". It does not.**

---

## A second record only helps if it can disagree

> **Moved here from Foundations §4 on 2026-08-27. The rule stays in Foundations §4.3.**

**A second record must have two properties. Most people ask for only the first.**

1. **Independence.** The fault that hit the first record did not reach the second. The two were made on different paths.
2. **Expressiveness.** The second record is *able* to hold a value that contradicts the fault.

**A record can be fully independent and still useless.** If it can only say the same thing the first record says, it agrees no matter what.

### The balanced lie, worked

An attacker adds two false records at once. They invent **2.0 kg** of a good arriving from nowhere, and **2.0 kg** of the same good going to waste. This is a **balanced pair**.

| What the check adds up | Answer | Does it fire? |
|---|---|---|
| Mass in − mass out, first record | 2.0 − 2.0 = **0.0 kg** | ❌ No |
| Mass in − mass out, second record, made by a different party | 2.0 − 2.0 = **0.0 kg** | ❌ No |
| Mass in − mass out, a third record, also independent | 2.0 − 2.0 = **0.0 kg** | ❌ No |

**Adding more independent records never helps here.** Every one of them adds up to zero, because the lie was built to add up to zero. The check looks for a gap and there is no gap.

Now weigh the actual pile of grain in the actual barn:

| What the instrument reads | Answer | Does it fire? |
|---|---|---|
| Recorded stock | 2.0 kg | — |
| Weighed stock | **0.0 kg** | ✅ **Yes — short by 2.0 kg** |

**The scale fired because it can say a number the records cannot argue with. It is expressive. The other records were only independent.**

> **What defeats a balanced lie is physicality, not independence.** This is why the outside total used in [statistical-coverage](statistical-coverage.md) is a **physical** total and not a second set of books. **Matter does not agree to be counted twice.**

### Where the trust went

**Rung 3 does not remove trust. It moves trust from the ledger to the instrument.**

An attacker who controls the scale wins completely, and nothing further along the chain can tell. **That is a better place for trust to sit — a rival can re-calibrate a scale, and cannot re-calibrate a lie — but it is not "nothing to trust", and the documents should never say it is.**

Registered with **OP-22** (minimum audit disclosure) and **OP-10** (weighting governance). **A mis-calibrated constant is the same attack arriving at specification time rather than at reading time.**

---

## Depends on

- [derived-ledger](derived-ledger.md)

## Consequences

- [statistical-coverage](statistical-coverage.md) — estimation is what fills the gaps verification can't reach
- [regulator-inversion](regulator-inversion.md)

## Open questions

- How competing trust networks reconcile — see [ledger-ecosystem](ledger-ecosystem.md)
- **OP-7 — cross-level trade fairness.** Deferred to v2.

---
*Status: settled (the ladder) / provisional (Level 2 as emergent market)*
*Source: `00-strategy/Aequitas_Foundations_v0.2.md` §4*
