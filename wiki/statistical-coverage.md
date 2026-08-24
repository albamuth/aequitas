# Statistical Coverage

> Every human is accounted for whether or not they participate, and **credit and debit are estimated symmetrically for everyone**. What participation unlocks is not being counted — it is being able to *act* on what was counted.

## What it is

Axiom A7. Participation is voluntary; coverage is not. There is no population outside the model, and no side of the ledger that only members get.

| | Estimated from |
|---|---|
| **Debit** | Demographic cohort average — "male American living in Houston" carries that cohort's average load, computed *excluding* registered participants. Public figures from publicly known wealth and holdings. |
| **Credit** | Cohort production model — occupation, region, known activity. A subsistence farmer's food production is real material flow and is estimated as such. |

Two states, and the distinction carries the whole axiom:

- **Accounted** — a factual description of material flows attributable to a person. Everyone has one. It is not a claim on them or by them.
- **Realizable** — acts on a debit ceiling only after a **verified account** plus **observed supersession** of the estimates. Assertion is not evidence.

## Why it works this way

Universality requires the accounting to close. If a large population sits outside it, the flows they cause are unaccounted and [[no-externalities]] is false in practice.

**Estimating only debit was factually wrong, not merely unfair.** A non-participant's production is real: under [[event-record]] origin closure, that wheat is a parcel with ancestry and an agent. Recording the consumption while omitting the production makes the global books describe a world where material appears from uncreditable sources.

Excluding registered participants from the cohort baseline is a subtle but important detail — otherwise participants' real (usually lower) footprints would drag down the average assigned to non-participants, weakening [[onboarding-incentive]].

## The error asymmetry

> Over-estimating debit consumes nothing. **Over-estimating credit inflates real consumption ceilings on the basis of guessed production.**

The two sides are symmetric in form and asymmetric in consequence. This is exactly why realization is gated on observation while estimation is not, and it is a permanent design constraint rather than a solved problem.

## Granularity is opportunistic

Record what is known; estimate the rest from averages; refine forever.

> A daily commuter's road usage can be computed and shown. Absent specifics, estimate from averages — average commuter fuel use, Schaumburg → downtown Chicago, 5×/week. Learn which car they drive and the carbon cost and road-wear share sharpen. All of it is revisable retroactively.

## Who games this

- **Cohort shopper** — self-identifies into a high-production cohort at onboarding to inflate estimated credit. **Nothing stops this yet (OP-14).**
- **Ghost harvester** — attempts to substantiate the accrued position of someone who never joined, or who has died. Needs proof-of-personhood (C6); **unhandled (OP-15).**
- **Claim inflator** — asserts large past production on joining. Blocked: supersession monotonicity requires attested records, not assertion.

## The framing problem — largely resolved

Assigning a debit to someone who never consented reads, to an outsider, as an accusation: *"you assigned me a debt I didn't agree to."*

Symmetric estimation answers it. The system assigns an estimate of **both** sides, it is a description of physical activity rather than a claim on the person, and it carries no enforcement against non-participants whatsoever. The pitch inverts from *"you owe"* to *"here is what you have contributed, and what it cost — join and make it yours."*

*This was previously logged as an unresolved framing problem. The A7 v0.2 amendment closed it.*

## Depends on

- [[material-flow-value]]
- [[verification-ladder]]

## Consequences

- [[onboarding-incentive]] — replacing your assigned average with your real record

## Open questions

- **OP-3 / C3 — the estimation engine.** Cohort hierarchy and convergence path from global average → individual truth. **Widened by v0.2:** now requires a cohort *production* model, not only consumption.
- **OP-14 — cohort shopping.** No defence yet.
- **OP-15 — ghost harvesting.** Interacts with C6 and with the unresolved handling of a deceased person's permanent consumption record.
- Decentralization pressure: whoever maintains the cohort production model influences ceilings. Compounds the weighting-model governance hole (OP-10).

---
*Status: settled (principle) / provisional (production model, OP-14, OP-15)*
*Source: `00-strategy/Aequitas_Foundations_v0.19.md` A7, §3.4, §5.1, §5.1a, §12*
