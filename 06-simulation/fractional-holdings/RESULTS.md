# Fractional holdings — one account, parts of several co-products

> **Version:** 0.1
> **Date:** 2026-10-13
> **Code:** [`fractional_holdings.py`](fractional_holdings.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **Answers:** nightcheck 2026-10-13, decision 5.3 (`07-outreach/log/PLAN-2026-10-13.md`), and the self-council record `obj-20261010-self-council-union-fractional-take` (post #8335).
> **Status: COMPLETE for the two chain-resolution cases.** 10/10 self-tests pass.

---

## The answer

> **The "max" rule passes every check that can fail. The two rivals fail the bundle check, and max without the consumed-parts change fails the eater check.**

**The rule.** For each parcel (one step of the chain), per dimension, an account carries the parcel's cost times the **largest** mass fraction `f_p` of any co-product `p` that passed that step. `f_p` adds the pieces of one co-product, and it counts what the account holds **and** what it has consumed.

## Terms

| Term | What it means |
|---|---|
| `K` | One step's cost, in one dimension |
| `f_p` | The mass fraction of co-product `p` in the account's set: held now, plus consumed |
| **Independent** | The rival `1 − Π(1 − f_p)`: treats the parts as random, overlapping draws |
| **No-keep** | Max over what is held now only, without the consumed-parts change |
| **n-bundle check** | One holder of a whole output splits it into `n` identical bundles. By conformance row 10c the bundles must add back to the whole |

## The numbers

**Steer, illustrative digits from `chain-resolution/`: 20 h of labour over seven steps. The hide leaves at step 2; the beef passes all seven.**

| Holding | Max | Independent | Sum | No-keep |
|---|--:|--:|--:|--:|
| 10% beef, 10% hide | **2.00 h** | 2.45 | 2.50 | 2.00 |
| 10% beef, 50% hide | **4.00 h** | 4.25 | 4.50 | 4.00 |
| 10% of every co-product | **2.00 h** | 3.65 | 4.00 | 2.00 |
| 50% hide held, 50% beef eaten | **10.00 h** | 11.25 | 12.50 | 2.50 |
| 50% beef eaten, then the hide sold | **10.00 h** | 10.00 | 10.00 | **0.00** |

**In plain words: 10% of a whole steer carries 10% of the steer under max, and 18% under independent overlap.** The last row is the eater: without the consumed-parts change, eating half the beef costs nothing.

**The worked row, digit by digit.** 10% beef and 50% hide. Steps 1 and 2 cost 5 h, and both co-products passed them, so the larger fraction applies: 0.5 × 5 = 2.5 h. Steps 3 to 7 cost 15 h and only the beef passed them: 0.1 × 15 = 1.5 h. **Total 4.0 h.**

**The n-bundle check, both cases.** Ten bundles together, in wholes:

| Case | Max | Independent | Sum |
|---|--:|--:|--:|
| Steer, `n` = 10 | **1.00** | 1.83 | 2.00 |
| Refinery, real DOE energies, `n` = 10 | **1.00** | 2.99 | 3.63 |

## The ten self-tests

| Test | What it checks | Result |
|---|---|---|
| Union | `f` = 1 on every co-product taken equals the existing §3.4a union | 400 random selections |
| Split | One co-product alone carries its mass share of its own steps | 55 cases |
| n bundles | Row 10c on a whole holding | Max exact; independent fails |
| Monotone | Adding mass never lowers a debit | 8,000 random additions |
| A5 ceiling | No holding carries more than each parcel's cost | 8,000 random holdings |
| Eater | Eating changes nothing; selling the hide leaves the beef's share | 10.0 h kept; 0.0 h without the change |
| Order | Shuffled buy, eat and sell sequences reaching one state give one debit | 1,000 states × 4 orders |
| Splitter | One holding divided between two accounts never carries less | 8,000 splits; raised it up to 1.76× |
| Per parcel | The hide does not reach steps it never passed | 82.0 MJ per step against 250.0 MJ per process |
| Resolution | A coarse reading is still a ceiling on a fine one | 600 holding-resolution pairs |

## What this run does not show

1. **The order test checks the bookkeeping, not the rule.** The rule reads only the final state, so any sequence reaching that state gives the same figure by construction. The test confirms the sequences reach it.
2. **Monotonicity is assumed, not derived.** It is the one premise of the derivation that is not already a rule in the documents.
3. **Two cases only.** The steer's digits are illustrative. The refinery uses real DOE process energies and a declared passage table.
4. **Mix and split events are not modelled.** A mixed parcel is one parcel, so the rule applies to it unchanged. That is an argument, not a run.
