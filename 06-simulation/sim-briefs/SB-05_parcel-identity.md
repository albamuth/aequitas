# SB-05 — What happens to the books when a flow sheet cannot tell one parcel from two?

> **Request:** `sr-20260905-how-often-does-a-joint-process-flow-sheet-fa` · filed 2026-09-05, from **@custos** at c42203.
> **Status:** open. **Nobody has run this.**
> **This is the sharpest open objection to the current rule.** It attacks a precondition, not a conclusion.

---

## 1. The question

> **Two output paths each name a parcel of input. The rule says a parcel reached twice is counted once. But how does the flow sheet know the two names refer to the same parcel? Sweep an unresolved-identity rate from 0 to 50% and measure how far the books overstate against the true figure.**

## 2. What depends on it, and why the objection is good

**Foundations §3.4a** says a joint process's cost is **not divided**: every co-product carries the **whole** cost of the process, read against its own output mass. **A reader immediately objects that this puts the cost in twice.**

**The answer given is A3, stated as a computation:**

> **A debit is a pointer at an identified parcel, not a quantity.** Co-product A's 100 MJ and co-product B's 100 MJ **point at the same 100 MJ** — one supplier, one delivery window, one record.
> **So a ledger walk is a union over identified parcels, never a sum.**

Carried as **conformance rows 10c and 10e**. Measured across 128 readings of one refinery: **the union returns the chain total every time; a naive sum returns 111 different answers and overstates by up to 7.00×.**

**@custos's objection, and it is precise:**

> **Rows 10c and 10e presuppose that two paths naming a parcel name the *same* parcel.** Where the flow sheet cannot resolve that, **the union has nothing to union over, and the second reading is a fiat quantity — an A1 breach.**

**And the sting is in our own evidence.** The 1,152 product-resolution pairs of `06-simulation/chain-resolution/` **had identified parcels by construction.** The run could not have found this, because the generator never produced the failure.

## 3. Terms

| Symbol | What it means |
|---|---|
| **Parcel** | One identified quantity of input: one supplier, one delivery window, one record. **The thing a debit points at** |
| **Path** | The route one co-product took through the process's steps |
| **Union** | The set of distinct parcels a walk reaches. **A parcel reached twice is counted once** |
| **Naive sum** | Adding what every path carries. **Overstates whenever two paths share a parcel** |
| **`u`** | **The unresolved-identity rate.** The share of parcel pairs where the flow sheet cannot say whether two names are one parcel or two. Swept 0 to 0.5 |
| **Overstatement** | `books figure ÷ true figure` |

## 4. The model

**Build a joint process with a known truth, then hide part of the identity information and see what the books do.**

**Step 1 — generate ground truth.** A process with `S` steps and `P` co-products. Each step consumes a set of input parcels, each parcel with a known physical quantity. **Record which parcels are genuinely the same and which are genuinely distinct.** This is the truth; the books never see it.

**Step 2 — degrade identity.** For a share `u` of parcel pairs, the flow sheet is unable to resolve identity. **This is the whole experiment, and the interesting choice is what the books do then. Three policies, and you must run all three:**

| Policy | What the books do with an unresolved pair | What it is |
|---|---|---|
| **P1 — assume distinct** | Count both | **The conservative reading.** Overstates |
| **P2 — assume same** | Count once | **The flattering reading.** Understates |
| **P3 — refuse** | **Report the figure as `not identified`** and count neither into a point estimate | **Foundations §4.4's own label rule**, applied here |

**Step 3 — measure.** For each `u` and each policy, compute `books ÷ truth`, and for P3 also the share of figures that become unreportable.

### A worked example, with the numbers

**One process, 100 MJ on a parcel `E-8841` that two co-products both passed through, and 100 MJ on a parcel `E-8842` that only one passed through.**

| | True total | P1 assume distinct | P2 assume same | P3 refuse |
|---|--:|--:|--:|---|
| Identity resolved | **200 MJ** | 200 | 200 | 200 |
| **`E-8841` unresolved** | **200 MJ** | 100 + 100 + 100 = **300** | 100 + 100 = **200**, correct by luck | **not identified** |

**In plain words: at one unresolved parcel out of two, the conservative policy overstates by 1.5×.** The flattering policy happened to be right here **and will be wrong in the mirror case**, where two genuinely distinct parcels are collapsed into one.

> **P2 is the dangerous one and it is the one a producer prefers**, because it lowers their figure. **That is OP-24's one-way pressure, arriving in a new place.**

## 5. Inputs

**A generator. No real data needed.** State: `S`, `P`, the parcel count, how paths are assigned to steps, the sweep of `u`, and your seed.

**A second variant worth running:** make identity resolution **correlated with parcel size** — big shipments are documented, small ones are not. **We expect this to matter and have not measured it.**

**Ours, to attack:** `06-simulation/chain-resolution/`. **Its generator is exactly what this brief is testing**, because it produced identified parcels by construction.

## 6. What an answer looks like

| `u` | Policy | Mean `books ÷ truth` | Worst case | Share unreportable |
|--:|---|--:|--:|--:|
| 0.00 | P1 | 1.000 | 1.000 | 0% |
| 0.10 | P1 | | | |
| … | | | | |

**Plus one line: at what `u` does each policy's error exceed the 7.00× that the naive sum reaches?** If a policy is worse than not having the rule at all, that is the finding.

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **P1 (assume distinct) overstates roughly linearly in `u`** and stays well under the naive sum's 7.00× at every `u` ≤ 0.5. **P2 understates and is the one a producer would choose.** **P3 makes a large share of figures unreportable at modest `u`** — we guess more than a quarter by `u` = 0.2, which would make the honest policy impractical |
| **Refutation threshold** | **If P1's overstatement at any `u` ≤ 0.5 exceeds the naive sum's 7.00×**, the union rule is not an improvement under unresolved identity and conformance 10e must say so. **And if P3 makes more than half of figures unreportable at `u` = 0.2**, the label rule cannot be the answer here |
| **What we do if either is crossed** | **§3.4a gains a precondition it does not currently state**: the union rule holds *where parcel identity is resolvable*, and conformance 10e says what an implementation does when it is not. **@custos's A1 point would then be conceded in full** — an unresolvable second reading is a fiat quantity, and A1 forbids those |

**We think @custos is right that the precondition is unstated. What we do not know is how much it costs.** That is what this brief buys.

## 8. Self-tests, each able to fail

1. **At `u` = 0, all three policies return the truth exactly.** If not, the generator or the walk is wrong.
2. **The naive sum reproduces the published 7.00× worst case** on a chain built like the refinery one. **This anchors the model against an existing result.**
3. **P1 never understates and P2 never overstates.** Either violation means the policies are swapped.
4. **Every path's parcels are a subset of the process's parcels.** Closure.
5. **Doubling every parcel's quantity doubles every figure and leaves every ratio unchanged.**

## 9. Out of scope

- **How a real flow sheet resolves identity.** That is an instrumentation question and Foundations §2.6 puts it with the implementer. **This brief measures the cost of failing, not how to succeed.**
- **Whether a producer would lie about identity.** That is a false record, caught by conformance row 7. **This brief is about honest inability, which is the harder case.**
- **The division rule itself.** Withdrawn on 2026-09-03 and not coming back.

## 10. Known ways to get this wrong

- **Generating only resolvable parcels.** That is exactly the flaw in our own 1,152-pair run, and it is why this brief exists.
- **Running P1 alone.** It is the conservative policy and it flatters the rule. **P2 is what a producer would actually do.**
- **Reporting a mean without a worst case.** The union rule's published claim is about the worst case, not the average.
