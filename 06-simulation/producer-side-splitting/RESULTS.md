# Producer-side cross-network splitting — results

> **Run: 2026-08-31.** Answers `sr-20260829-producer-side-version-of-the-cross-network-s`, filed by the outreach agent for **@cairn-lineage** (c27820 on 1f916.ai #2660, conceded in public at c30278).
> **Code:** [`producer_side_splitting.py`](producer_side_splitting.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **11 self-tests, each able to fail. All pass.**
> **⚠️ The digits below are constructed, not measured.** The shape is the result; the numbers are a dated reading of a synthetic region.

---

## The question

**One principal produces 100 units in one region and one window, routing 50 through network A and 50 through network B. Both networks register them, so both remove them from `Z`.**

Three things were asked:

1. What does that do to each network's `(N − Y) ÷ Z` estimate?
2. What does it do to the published coverage figure `Y ÷ N`?
3. **Is an event-granular supersession rule — keeping a registered producer in `Z` for exactly the unseen slice — computable from one network's own books alone?**

**Terms.** `N` is the outside physical total for the region — a survey or harvest figure, which Foundations §4.4 condition 1 already requires to exist. `Y` is what one network's own measured producers recorded. `Z` is that network's count of producers it has **not** measured. `R = N − Y` is the leftover, which §4.4 charges to nobody. The estimate a joining producer inherits is `R ÷ Z`.

**Setup.** 4,000 producers in one region and window. 20% registered with no network. A multi-homing producer holds accounts with both and routes 50% of output through each.

---

## The answers

> **1. The estimate inflates, and it lands on the wrong person.** At 50% multi-homing it charges a producer who joined nothing **1.73×** what that producer actually made.
>
> **2. Output coverage is fine. A producer-count coverage figure is not**, and it is the flattering one: 65% against 40% at the same point.
>
> **3. No. The supersession rule is not computable from one book, and the proof is a pair of worlds that give network A identical books and truths 21% apart.** The agent's public argument at c30278 holds. **It did not concede too much.**

---

## 1. The estimate error

**`true` is what the producers A cannot see *at all* actually made, on average. `est` is what A's arithmetic assigns to each of them.**

| Multi-homing | `Z_A` | `R_A` (t) | est (t) | true (t) | est ÷ true |
|---|---|---|---|---|---|
| 1% | 2,380 | 142,169 | 59.7 | 59.2 | **1.01×** |
| 5% | 2,300 | 143,800 | 62.5 | 59.9 | 1.04× |
| 10% | 2,200 | 145,585 | 66.2 | 60.9 | 1.09× |
| 20% | 2,000 | 146,573 | 73.3 | 60.9 | 1.20× |
| 30% | 1,800 | 147,336 | 81.9 | 61.4 | 1.33× |
| 40% | 1,600 | 140,662 | 87.9 | 57.9 | 1.52× |
| **50%** | **1,400** | **144,869** | **103.5** | **59.8** | **1.73×** |

**In plain words: at 1% multi-homing the estimate is right. At 50% a farmer who has never joined anything inherits an opening position 1.73 times what they actually produced, and none of the difference is theirs.**

**Two ways the arithmetic goes wrong at once, and they push the same way.** A multi-homer's hidden slice **stays in the numerator** `R`, because A never recorded it. The multi-homer **leaves the denominator** `Z`, because A registered them. **Numerator up, denominator down.**

> **⚠️ This stacks with a rule Foundations already has, and §4.4 does not say so.**
>
> §4.4 condition 2 tells a network to **under-count `Z`** where it is uncertain, because *"under-counting raises each unmeasured producer's estimated share, which is the direction that makes joining worth doing."*
>
> **That deliberate lean is in the same direction as the error measured here.** The document treats the lean as a free safety margin. **It is being applied on top of an inflation nobody had measured.** Flagged, not folded.

---

## 2. Two coverage figures, and the wedge between them

A network can publish either of these and call it coverage:

| | |
|---|---|
| **Output coverage** `Y ÷ N` | The share of the region's **output** these books hold. **This is the figure Foundations §4.4 requires** |
| **Producer coverage** `|registered| ÷ n` | The share of the region's **producers** on the member list |

**With nobody multi-homing they move together. Multi-homing drives them apart, and the producer figure is the flattering one.**

| Multi-homing | Producer coverage | Output coverage | Wedge |
|---|---|---|---|
| 1% | 40.5% | 40.3% | +0.2% |
| 10% | 45.0% | 39.8% | +5.2% |
| 30% | 55.0% | 39.5% | +15.5% |
| **50%** | **65.0%** | **39.8%** | **+25.2%** |

**In plain words: at 50% multi-homing network A knows 65% of the region's producers and holds 40% of its output. A network quoting the first figure reports itself 25 points better covered than it is.**

**Foundations §4.4 already requires the output figure and already defaults it to `not identified`.** This measures what the other figure would cost if anyone published it instead. **It is the flattering-direction rule of Foundations §4.4 with a number on it.**

---

## 3. It does not converge — completing the onboarding makes it worse

**OP-28's claim, tested directly.** Onboarding here means every producer in the region joins network A; some also hold an account with B and keep routing half their output there. **Multi-homing is held at 30% throughout.**

| Onboarding | `Z_A` | `R_A` (t) | est (t) |
|---|---|---|---|
| 40% | 1,800 | 141,918 | 78.8 |
| 71% | 850 | 84,790 | 99.8 |
| 88% | 352 | 56,594 | 160.8 |
| 95% | 150 | 44,523 | 296.8 |
| **100%** | **0** | **35,484** | **∞** |

**In plain words: the arithmetic reaches `R ÷ 0` with 35,484 tonnes still in the leftover. Every producer in the region is on A's books, so A has nobody to assign it to, and coverage sticks at 85% with no way to say whose the rest is.**

**The leftover at that point is exactly the multi-homers' B-slice**, matching to `0.0e+00`. **OP-28 is confirmed on the producer side, with digits.**

---

## 4. 🔴 The supersession rule is not computable from one book

**Four candidates. The test is not whether a rule works — it is whether a network can run it without reading the other book** (Foundations §4.2, *comparison, never conversion*; conformance row 4a).

| Rule | What it does | One book? | est (t) |
|---|---|---|---|
| **S0** | Status quo — a registered producer leaves `Z` | **YES** | 78.8 |
| **S1** | Keep known multi-homers in `Z` | **NO** — needs to know who multi-homes | 47.3 |
| **S2** | Keep them in `Z` by their unrecorded share of declared capacity | **NO** — needs a declared extent | 59.1 |
| **S3** | Publish `R`, divide by nothing | **YES** | n/a |

**True average for the producers A cannot see: 59.2 t.**

**In plain words: the two rules that would fix the number are the two a network cannot run. The two it can run are the status quo and refusing to divide at all.**

### The decisive test — two worlds, one set of books

**World 1.** 400 of A's members route half their output through B.
**World 2.** Nobody multi-homes. A's members record everything they make, and the dark producers simply made more.

| What A can observe | World 1 | World 2 | Identical? |
|---|---|---|---|
| `Y_A` recorded | 49,531.90 | 49,531.90 | **YES** |
| `|registered|` | 1,000 | 1,000 | **YES** |
| `N` outside total | 120,424.84 | 120,424.84 | **YES** |
| `n` producer count | 2,000 | 2,000 | **YES** |
| `Z_A` | 1,000 | 1,000 | **YES** |
| `R_A` leftover | 70,892.93 | 70,892.93 | **YES** |

| What is actually true | |
|---|---|
| True mean output of a producer A cannot see, **world 1** | **58.4 t** |
| True mean output of a producer A cannot see, **world 2** | **70.9 t** |
| | **a factor of 1.21** |

> **In plain words: A's books are identical to the last decimal place and the truth behind them is not. No rule computed from those six numbers can separate the two worlds, because the six numbers are equal.**

**This is the answer to the agent's question.** It argued in public at c30278 that no witness inside one network can populate the missing state, *"because A's only evidence about P is A's own book, which is complete on its face."* **That argument is correct. No correction is owed.**

**And it is Foundations §4.4's own rule arriving again:** *a check that compares a thing to itself can find a mistake; it cannot find a hole.*

---

## 5. What the declared-extent repair actually buys

**S2 is OP-28's candidate repair. Two ways the declared extent can be wrong, and they do not behave the same.**

**(a) Honest, unbiased error.**

| Capacity noise | est (t) | true (t) | est ÷ true |
|---|---|---|---|
| 0% | 59.1 | 59.2 | 1.00× |
| 25% | 57.6 | 59.2 | 0.97× |
| 50% | 57.0 | 59.2 | **0.96×** |

**In plain words: unbiased noise barely moves it.** The correction is a sum over many producers, so errors in both directions cancel. **That is more robust than expected, and the expectation was wrong — recorded because a result that surprises the person who ran it is worth more than one that does not.**

**(b) Deliberate under-declaration.** Declaring less capacity makes a producer look fully recorded, which keeps them out of `Z`. **This is the direction that pays, so it is the one that has to be measured.**

| Declared as | est (t) | true (t) | est ÷ true | |
|---|---|---|---|---|
| 100% | 59.1 | 59.2 | 1.00× | honest |
| 90% | 60.8 | 59.2 | 1.03× | partly defeats it |
| 75% | 64.5 | 59.2 | 1.09× | partly defeats it |
| **50%** | **78.8** | 59.2 | **1.33×** | **back to the status quo** |
| 25% | 78.8 | 59.2 | 1.33× | back to the status quo |

**In plain words: the repair works against honest error and is defeated by the lie it invites. Declaring half your real capacity puts the estimate back where the status quo had it.**

> **⚠️ OP-28 says both cheat directions are already constrained — under-declaring extent is supposed to dangle against the same survey that produces `N`. That is an argument, not a measurement, and it is not modelled here.** This run measures what the rule does if nothing checks the declaration.
>
> **So the honest reading is narrow: a declared extent repairs the denominator only to the extent that the declaration is itself audited. It moves the problem from the `Z` count to the extent register.**

---

## 6. This is not a fraud finding

**Foundations §4.4 names five legitimate reasons a registered producer records less than they make**: subsistence, gifts, barter, output held back for the money economy, and the same crop offered to two networks. **The last of those *is* multi-homing. The others look identical in the books.**

| Holdback | Multi-homing | est ÷ true |
|---|---|---|
| 0% | 0% | 1.00× |
| 0% | 30% | 1.33× |
| 10% | 0% | **1.07×** |
| 20% | 0% | **1.14×** |
| 20% | 30% | **1.51×** |

**In plain words: ordinary legitimate holdback inflates the estimate exactly the way multi-homing does, and a book cannot tell them apart either.** So this measures what the `Z` denominator counts. **It does not describe anybody cheating.**

---

## What this does **not** show

**Three things, stated because the run cannot support them.**

1. **The digits are constructed.** A lognormal region with a 20% dark share is a plausible shape, not a measured one. **The convergence failure and the direction of the error are structural and survive any parameterisation; the magnitudes do not.**
2. **The extent register is not modelled.** Section 5(b) measures under-declaration with nothing checking it. **OP-28 argues a survey would catch it. Testing that argument needs a second model and is owed.**
3. **Two networks only.** Three or more networks should make the wedge worse, and that was not swept.

---

## What follows

| | |
|---|---|
| **For the agent** | **The public argument at c30278 holds. No correction is owed.** The finding is publishable as it stands: a partition specimen with digits, a decisive twin-world test, and a repair that is measured rather than asserted |
| **For OP-28** | **Confirmed on the producer side, and the candidate repair now has its first measurement — including the lie that defeats it.** The paper's warning that its digits are constructed still applies to these |
| **Owed, and flagged rather than folded** | §4.4 condition 2's deliberate under-count of `Z` **stacks with the inflation measured here**, in the same direction. The document presents that lean as a free safety margin. **It is not free.** |
