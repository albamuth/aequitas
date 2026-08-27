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

Universality requires the accounting to close. If a large population sits outside it, the flows they cause are unaccounted and [no-externalities](no-externalities.md) is false in practice.

**Estimating only debit was factually wrong, not merely unfair.** A non-participant's production is real: under [event-record](event-record.md) origin closure, that wheat is a parcel with ancestry and an agent. Recording the consumption while omitting the production makes the global books describe a world where material appears from uncreditable sources.

Excluding registered participants from the cohort baseline is a subtle but important detail — otherwise participants' real (usually lower) footprints would drag down the average assigned to non-participants, weakening [onboarding-incentive](onboarding-incentive.md).

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

- [material-flow-value](material-flow-value.md)
- [verification-ladder](verification-ladder.md)

## Consequences

- [onboarding-incentive](onboarding-incentive.md) — replacing your assigned average with your real record

## The three landing states — `floor`, `ceiling`, `not identified`

> **Moved here from Foundations §4.4, §4.4 and §4.4 on 2026-08-27, when §4, §5 and §6 were consolidated. The rule stays in Foundations §4.4.** It is conformance requirement **13**.

### The rule

> **A `floor` label is earned by the arithmetic that produced the figure. It is never inherited from the fact that some input was incomplete.**

**A quantity *counted* over incomplete coverage is a floor.** Under-recording can only understate a count, so better coverage moves the figure in one direction only, which is up.

**That holds for a count. It does not survive a subtraction.** A subtrahend reverses the direction of every error inside it.

### Which label a leftover gets

| Which operand is blind | Effect on `R = N − Y` | The correct label |
|---|---|---|
| **`Y` under-records**, `N` sound | `R` comes out **too big** | **`ceiling`** |
| **`N` under-observes**, `Y` sound | `R` comes out **too small** | **`floor`** |
| **Both, or neither direction defensible** | Unknown | **`not identified`** |

**Publish the interval, always:** **`R ∈ [N_L − Y_U, N_U − Y_L]`**.

**`not identified` is the default.** A label is earned by a stated directional argument about **each** operand's blind spot. **It is never inherited from *"some coverage is incomplete."***

### Worked, on the valley wheat case

After the four alignment rows are fixed (see [estimation-engine](estimation-engine.md)): `N` = 88,000 t, `Y` = 82,000 t, `R` = **6,000 t**.

| Case | What is really true | True `R` | 6,000 t is |
|---|---|---|---|
| The registry misses 4,000 t of on-farm sales | `Y` = 86,000 t | **2,000 t** | a **ceiling** — the published figure is **3× the truth** |
| The satellite cannot see 10,000 t under canopy | `N` = 98,000 t | **16,000 t** | a **floor** |

**Now do it properly.** Suppose the satellite is known to under-detect, by an unquantified amount, and the registry is audited and sound. So `N ∈ [88,000, 100,000]` and `Y` = 82,000 ± 0.

`R ∈ [88,000 − 82,000, 100,000 − 82,000] =` **[6,000, 18,000] t**, labelled **`floor`** at 6,000 t — **because there is a stated directional argument about `N`.** The detector misses under canopy and cannot over-count.

**Take that argument away and the same numbers are `not identified`**, published as the interval with no label. **A three-fold range is not a finding, and saying so is the honest output.**

### The coverage percentage carries the same problem

**A published coverage figure is `Y ÷ N`**, built from the same two incomplete readings.

| Which operand is blind | What happens to a published *"60% covered"* |
|---|---|
| **`Y` under-records** — real measured output the registry missed | Coverage is **understated.** The books are better than they say. |
| **`N` under-observes** — real output the survey cannot see | Coverage is **overstated.** The books are worse than they say, **and this is the direction that flatters the network.** |

**Same three labels, same default.** A network publishing a bare percentage with no direction on it is publishing a number nobody can use.

### Where this came from, and why it survived so long

**Found from outside on 2026-08-27** by @cairn-lineage (comment c23607 on 1f916.ai post #2259), and conceded in public the same night.

Foundations carried the unqualified sentence — *"report the residual as a lower bound"* — **for six versions**. It was produced by carrying the floor rule through a subtraction.

> **The error ran in the project's own favour.** An overstated leftover makes the unmeasured pool look **larger**, which is the direction both the adverse-selection argument and the deliberate under-count of `Z` already want. **A wrong number that flatters the theory is the class least likely to be caught from inside, and this one was not caught from inside.**

## A check on one log finds mistakes, not holes

> **Moved here from Foundations §4.4. The rule stays in Foundations §4.4** and is conformance requirement **14b**.

> **Ask this about any check and you will know at once what it can find. Does this check compare two things made on separate paths, or does it compare a thing to itself?**

**A check that compares a thing to itself can find a mistake. It cannot find a hole.** If part of the record was never written, both sides of the check are missing it and both sides still agree.

### Worked

A farm records 8 sacks in and 8 sacks out. Someone then deletes the last **2 sacks** from **both** halves of the record.

| Check | What it compares | Sum | Does it fire? |
|---|---|---|---|
| Mass balance on the log | The log against itself | 6 in − 6 out = **0** | ❌ No |
| Origin closure on the log | The log against itself | every sack has a source | ❌ No |
| Fate closure on the log | The log against itself | every sack has an end | ❌ No |
| **The buyer's own receipt** | **A record made on a second path** | **buyer holds 8, farm says 6** | ✅ **Yes — short by 2** |

**The first three are arithmetic over one log, and cutting a log never breaks arithmetic over that log**, because what is left is still balanced. **Only the fourth reaches outside.**

**And a second record is not enough on its own.** It must also be *able* to hold a value that contradicts the fault — see [verification-ladder](verification-ladder.md) on independence and expressiveness.

---

## Open questions

- **OP-3 / C3 — the estimation engine.** Cohort hierarchy and convergence path from global average → individual truth. **Widened by v0.2:** now requires a cohort *production* model, not only consumption.
- **OP-14 — cohort shopping.** No defence yet.
- **OP-15 — ghost harvesting.** Interacts with C6 and with the unresolved handling of a deceased person's permanent consumption record.
- Decentralization pressure: whoever maintains the cohort production model influences ceilings. Compounds the weighting-model governance hole (OP-10).

---
*Status: settled (principle) / provisional (production model, OP-14, OP-15)*
*Source: `00-strategy/Aequitas_Foundations_v0.2.md` A7, §3.4, §4.1, §4.4, §12*
