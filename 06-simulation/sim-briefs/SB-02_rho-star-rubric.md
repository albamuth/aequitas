# SB-02 — Is the clearing rate ρ\* an instrument, or is it blind too?

> **Request:** `sr-20260901-score-claim-2-of-disparity-ceiling-sim-py-th` · filed 2026-09-01.
> **Status:** open. **Nobody has run this.**
> **Read the format first:** [`README.md`](README.md), especially section 7.

---

## 1. The question

> **Score ρ\*, the clearing rate, on the same three-leg rubric that was applied to the disparity ceiling: sensitivity, specificity, and the coverage witness. Report whether it can see the thing it claims to measure.**

## 2. What depends on it

**Foundations §5.5.7** reports ρ\* as behaving *"like a prime rate"*: a value can be chosen so aggregate demand matches productive capacity, **≈ 1.2 at the baseline**, tightening to ~0.68 under a −30% capacity shock and loosening to ~2.2 under growth.

**Foundations §5.5.3** builds the whole stable band on ρ\*: `E_max = 365 · F · ρ*(F)`, and every row of that table.

> **On 2026-08-31 the other headline claim in the same file was found to be blind.** `24 ÷ F` reads no accounts — Foundations §5.5.7 now says so, conceded in public. **The rubric run that found it scored only that statistic, and named ρ\* as unmeasured in its own "what this does not show" section.**

**ρ\* is the one claim in that file that genuinely varies with the draw. That makes it the one that could be an instrument — and the one nobody has checked.**

## 3. Terms

| Symbol | What it means |
|---|---|
| **`F`** | The floor. Hours a day a network counts as the work of staying alive |
| **`ρ`** ("rho") | The **debit tolerance**. The multiplier in the consumption gate `D ≤ ρ·C` |
| **`C`, `D`** | An account's cumulative credit and cumulative debit. **Both only ever rise** |
| **ρ\*** | The **clearing rate**: the value of ρ at which aggregate committed debit equals productive capacity |
| **Sensitivity** | Does the statistic move when you insert the fault it claims to detect? |
| **Specificity** | Does it stay still when you insert a fault it should *not* respond to? |
| **Coverage witness** | Is there a record made on a **separate path** that could contradict it? |

## 4. The model

**The three legs, and what each does.**

**Leg 1 — sensitivity.** Declare a list of challenges **before running**, each a fault ρ\* ought to respond to. For each, compute ρ\* on the clean population and on the faulted one, and report the move.

**Candidate challenges** *(add your own; this list is not closed)*:

| # | The fault | What we expect ρ\* to do |
|---|---|---|
| **S1** | Capacity falls 30% | **Tighten**, to roughly 0.68 |
| **S2** | Capacity rises 25% | **Loosen** |
| **S3** | Pollution re-weighting raises every debit 25% | **Tighten**, to roughly 1.0 |
| **S4** | **Insert 20,000 fabricated accounts at the floor** | **?** — this is the one that broke `24 ÷ F` |
| **S5** | **Omit 20% of real consumption from the books** | **?** — under-recorded demand should read as spare capacity |
| **S6** | Shift consumption between accounts, holding the total fixed | **No move.** ρ\* is an aggregate |

> **S4 and S5 are the point of this brief.** S1 to S3 are already reported in §5.5.7 and are expected to pass. **A statistic that moves only under the shocks its author chose is not yet shown to be an instrument.**

**Leg 2 — specificity.** For each challenge that leg 1 shows ρ\* *can* respond to, insert a fault it should ignore and confirm it does not move.

> **⚠️ Leg 2 is meaningless on its own.** The 2026-08-31 run recorded this in one line worth repeating: *"a statistic that never moves passes specificity by construction. Read alone, this row looks like precision. It is silence."* **Run leg 1 first.**

**Leg 3 — the coverage witness.** Ask whether anything outside the simulation could contradict ρ\*.

**Here is the honest problem, stated up front.** ρ\* is computed from the same synthetic population it describes. **On a generator, leg 3 is unavailable by construction** — there is no outside total. **On real books the witness is `N`, the independently measured physical total of Foundations §4.4.**

> **So the most a simulation can report on leg 3 is that it cannot report on leg 3.** Say so rather than scoring it.

## 5. Inputs

**A synthetic population is sufficient and is what we used.** State: population size, the credit and debit distributions, the seed, and the capacity figure.

**Ours, to attack rather than to copy:** `06-simulation/disparity-ceiling/disparity_ceiling_sim.py` (N = 200,000) and the rubric machinery in `06-simulation/ceiling-rubric/`. **Section 4 is complete without either.**

## 6. What an answer looks like

**One row per challenge, matching the shape the 2026-08-31 run used:**

| Challenge | Leg | ρ\* clean | ρ\* faulted | Move | Fires? |
|---|---|--:|--:|--:|---|
| S1 | sensitivity | 1.20 | *(yours)* | *(yours)* | yes / no |

**Plus one sentence per leg saying what it establishes, and one saying what it does not.**

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **ρ\* passes S1–S3 and fails S4.** A fabricated account at the floor adds both credit and consumption, so it should move ρ\* a little — **but we expect the move to be smaller than the draw-to-draw noise**, which would make it undetectable in practice even though it is non-zero |
| **Refutation threshold** | **If ρ\*'s move under S4 or S5 is smaller than the standard deviation across 30 seeds of the clean population, ρ\* does not detect that fault.** In that case §5.5.7 must say so in the same sentence that reports ρ\*'s shock behaviour |
| **What we do if it is crossed** | The same repair `24 ÷ F` got: **§5.5.7 states what ρ\* is blind to, in the sentence that reports it.** The stable-band table stands, but is labelled as resting on a statistic that cannot see under-recording |

**And the standing rule this brief exists to obey**, supplied by a critic and now carried in §3.5:

> **A check whose passing condition is set by the checker is not an instrument, and it fails toward flattery.**

## 8. Self-tests, each able to fail

1. **Thirty seeds of the clean population give a ρ\* spread.** Report it. **Every "move" smaller than this spread is noise, not a finding.**
2. **Doubling capacity loosens ρ\*; halving it tightens ρ\*.** If either goes the wrong way, the model is wrong.
3. **S6 — shuffling consumption between accounts at fixed total — moves ρ\* by 0.00.** If it moves, ρ\* is not an aggregate.
4. **Setting every account's debit to zero sends ρ\* to its upper bound**, not to an error.

## 9. Out of scope

- **Whether ρ\* ≈ 1.2 is the right number.** Its absolute value inherits the weighting model and an illustrative capacity figure. **This brief is about whether the statistic can see, not about where it sits.**
- **The `24 ÷ F` ceiling.** Already scored, already conceded blind. That is [SB-01](SB-01_ceiling-challenge.md).
- **Real-network coverage.** Leg 3 is unavailable on a generator and this brief does not pretend otherwise.

## 10. Known ways to get this wrong

- **Running leg 2 before leg 1.** Specificity on an inert statistic is silence dressed as precision.
- **Reporting a move without the seed spread.** A move of 0.02 means nothing until you know the noise is 0.005 or 0.05.
- **Treating leg 3 as scored.** On a generator it is unavailable. **Unavailable is not "passed."**
