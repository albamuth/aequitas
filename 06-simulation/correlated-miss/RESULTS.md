# Correlated miss — results

> **Run: 2026-08-29.** Answers `sr-20260826-how-far-does-r-n-y-move-under-a-correlated-m`, requested for **@cairn-lineage** (c21187).
> **Code:** [`correlated_miss.py`](correlated_miss.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **6 self-tests, each able to fail. All pass.**

---

## The question

**@cairn-lineage:** *"`N − Y` is not a lower bound when `N` under-detects on the same population `Z` exists to expose."*

**Does the error stay inside any bound conformance row 14a can express?**

## The answer

> **They are right, and no. Row 14a's interval cannot express a shared blind spot, because it is built from two blind spots stated separately.**

---

## 1. The case the documents assume is the only exact one

**A perfect `N` and a blind `Y`.** This is the picture behind the 88,000 / 82,000 / 6,000 example in the conformance list.

| `Y` half-size | `R_obs` | `R_true` | Error |
|---|---|---|---|
| 10 t | 100,954 | 100,954 | **0** |
| 30 t | 415,545 | 415,545 | **0** |
| 50 t | 694,054 | 694,054 | **0** |

**`R_obs` is exact here, not a bound.** When `N` is complete, `N − Y` is precisely what the network could not see, by construction.

## 2. Give `N` a blind spot of its own and the figure flatters

**`Y` fixed at a 30 t half-size. The satellite now misses small plots too, but different ones.**

| `N` half-size | `R_obs` | `R_true` | Error | Label |
|---|---|---|---|---|
| 5 t | 382,646 | 415,545 | −32,899 | `floor` |
| 15 t | 235,690 | 415,545 | **−179,855 (−43%)** | `floor` |
| 25 t | 71,941 | 415,545 | −343,604 (−83%) | `floor` |
| **30 t** | **−6,286** | 415,545 | −421,831 | **negative** |

**Every row reads `floor`: the true dark output is above the published figure.** A smaller leftover means the network claims better coverage than it has — **so the error runs in the flattering direction, which is the one nobody inside is motivated to report.**

## 3. The correlation sweep

**`N` at 15 t, `Y` at 30 t.** `R_true` moves with `ρ`, so **read the coverage columns** — they are comparable and they are what a decision rests on.

| `ρ` | Coverage published | Coverage real | Overstated by |
|---|---|---|---|
| **0.00** | 91.4% | 85.7% | **5.7 pts** |
| 0.50 | 92.5% | 89.2% | 3.3 pts |
| **1.00** | 91.2% | 85.5% | **5.7 pts** |

> **The published coverage overstates the real coverage at every value of `ρ`, including zero.** Correlation makes it worse. **It is not what causes it.** What causes it is that `N` has a blind spot at all, and the documents assume it does not.

## 4. 🔴 The worst case: one blind spot, shared completely

**The satellite and the network have the same detector and the same latent draw.**

| Half-size | `R_obs` | `R_true` | Coverage published | Coverage real |
|---|---|---|---|---|
| 10 t | **0** | 103,074 | **100.0%** | 96.5% |
| 30 t | **0** | 422,414 | **100.0%** | 85.5% |
| 50 t | **0** | 712,014 | **100.0%** | **75.5%** |

> **`R_obs` is zero at every row and the published coverage is 100%, over an extent a quarter of which was never seen.** The arithmetic cannot find its own hole, because the hole was subtracted from both sides.

---

## What this found

**1. They are right, and the direction is the flattering one.** Whenever `N` has a blind spot of its own, `R_obs` comes out **below** the truth. **Their sentence was that `N − Y` is not a lower bound on what the network missed. Measured, it is not.**

**2. At full correlation the leftover reads zero.** Two instruments with one blind spot compute `N − Y = 0` and publish 100% coverage over an extent they have not covered.

**3. 🔴 Row 14a's interval cannot express this.** 14a permits a subtraction when the two figures measure **the same quantity, over the same extent, over the same window, with error bounds smaller than their difference.**

> **A correlated miss passes all four.** Same quantity, same extent, same window — **and the difference is zero, so no error bound is smaller than it.** The interval `R ∈ [N_L − Y_U, N_U − Y_L]` is built from the two blind spots stated **separately**, and a shared blind spot is not two.

**4. What refuses it is row 13's default, and only if it is obeyed.** `not identified` is the default until a stated directional argument exists for **each** operand's blind spot. **A network that cannot say which way its satellite is blind has no such argument**, so no `floor` label may be attached. **The rule already refuses the claim.** What it does not do is tell anyone the figure is worthless.

**5. One case the arithmetic does catch: a negative leftover.** At −6,286 t. **A leftover is an amount of output and cannot be negative**, so this is a hard signal that the subtraction is invalid. **It is the only self-announcing failure here, and it fires only once the shared blind spot is large enough to push past zero.** Below that, the same defect is present and silent.

**6. The test that would find it is not arithmetic.** **Compare the two instruments' size profiles, not their totals.** If both fall off at the same producer size, the leftover between them is uninformative however wide its interval is. **That is a comparison of methods, and nothing in the conformance list asks for one.**

---

## What this does not show

1. **It does not price the fix.** Comparing detector size-profiles needs both instruments to publish one. Whether they do is an empirical question about real satellite surveys and real trade statistics.
2. **It does not model a network that knows its own detector.** The model gives the network no self-knowledge. A network that measured its own subscriber size-distribution against a census would see the gap.
3. **The detector shape is a logistic falloff, chosen as realistic rather than measured.** The direction of the result does not depend on it; the magnitudes do.

## Registered against

**OP-26 (the coverage gap)** and **OP-24 (understatement drift)**. **It is not a defect in row 14a's arithmetic** — the arithmetic is right about what it describes. **It is a limit on what that arithmetic can see**, and row 13's `not identified` default is what stands between it and a false claim.
