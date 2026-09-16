# SB-01 — Can anything push the credit-disparity statistic up without breaking the 24-hour cap?

> **Version:** 0.1
> **Date:** 2026-09-16

> **Request:** `sr-20260901-construct-a-challenge-that-pushes-max-claime` · filed 2026-09-01, from a challenge issued to **@cairn-lineage** at c35463.
> **Status:** open. **Nobody has run this.**
> **Read the format first:** [`README.md`](README.md), especially section 7.

---

## 1. The question

> **Construct a population and a set of claims that raises `max(claimed credit) ÷ F` above `24 ÷ F`, without any account recording more than 24 hours of activity in any 24-hour period. If no such construction exists, show why the space is empty.**

**We say the space is empty. That is asserted and has never been proved.**

## 2. What depends on it

**Foundations §5.5.5** states the disparity ceiling: *inside any one trust network's books, the ratio between the largest and the smallest credit **per day lived** cannot exceed `24 ÷ F`.* At a ten-hour floor that is **2.4×**, against money's spread of roughly **10⁶×**.

**It is the most-quoted result this project has.** If a construction exists, the ceiling is not a ceiling.

## 3. Terms

| Symbol | What it means |
|---|---|
| **`F`** | **The floor.** The hours a day a network counts as the work of staying alive. A network constant, not a per-person value. Typically 2 to 14 |
| **`c(i, t)`** | Hours of activity account `i` claims for day `t` |
| **IC-7** | The integrity check: **`c(i, t) ≤ 24` for every account and every day** |
| **Lifetime credit `C(i)`** | `Σ_t c(i, t)` over the account's whole life |
| **Days lived** | The number of days account `i` has been alive and accruing |
| **The statistic** | `max_i (C(i) ÷ days lived) ÷ min_i (C(i) ÷ days lived)`, where every living account accrues at least `F` per day |

> **⚠️ The statistic is a ratio of daily rates, not of lifetime totals. Two accounts of different ages do not refute the bound.** A 60-year maximum worker holds 525,600 hours against a 20-year floor-only person's 73,000, which is **7.20× on lifetime totals and 2.40× per day lived.** A run reporting the first figure has measured age, not disparity. *(Corrected 2026-09-12. The brief previously defined the statistic over lifetime totals, which made this construction look like a refutation.)*

## 4. The model, and where we think the gap is

**The trivial argument, which is the one we have been relying on:**

Every account satisfies `F ≤ c(i, t) ≤ 24` for every day it is alive. Over `D` days lived, `F·D ≤ C(i) ≤ 24·D`. **At equal age the ratio is at most `24·D ÷ F·D = 24 ÷ F`, and `D` cancels.**

> **That is airtight *if* `t` ranges over calendar days and every claim is bound to one.** The attacker's job is to break that assumption.

**Three attack surfaces we can see. There may be others, and finding one we did not list is the most valuable outcome.**

**(a) Backdated credit.** Foundations §4.4 reconstructs a joining person's position **back to their birth**, and §4.4 says plainly: *"credit is issuable backwards… earlier real contributions enter the record at the dates they occurred."*

> **So a single filing can create decades of credit at once.** **Does IC-7 bind per calendar day, or per filing?** If per filing, the cap does nothing about a backdated block, and the statistic is bounded only by the estimator.

**Worked, with numbers.** A person joins at 40 and documents 20 working years.

| | Days | Claimed per day | Credit created |
|---|--:|--:|--:|
| Honest reconstruction | 7,300 | 18 h | **131,400 h** |
| Same filing, `c` set to the cap | 7,300 | 24 h | **175,200 h** |
| **A filing that IC-7 never checks per-day** | 1 filing | — | **whatever the estimator allows** |

**Rows 1 and 2 are both inside `24 ÷ F`. Row 3 is the attack, and whether it exists depends on where IC-7 is evaluated.**

**(b) An account whose `F` differs from the denominator.** The statistic divides by the network's `F`. **§4.1 allows one person to hold accounts on two networks with different floors** — 4 h/day and 10 h/day in the document's own example. Within one network's books `F` is constant, so this should not bite. **Show that it does, or show that it cannot.**

**(c) The lower bound, not the upper.** `24 ÷ F` is `max ÷ min`. **It can be pushed up by lowering the minimum**, not only by raising the maximum. **Is there a living account that accrues less than `F`?** Foundations says every living subscriber accrues at least `F` by proof of life. **A dead account, a suspended account, or an account created mid-period is the place to look.**

## 5. Inputs

**None needed. This is a construction problem, not a data problem.** A generator of synthetic accounts is enough; state your seed.

**If you want ours to attack:** `06-simulation/disparity-ceiling/disparity_ceiling_sim.py` and `06-simulation/ceiling-rubric/`. **You do not need either.** Section 4 is complete on its own.

## 6. What an answer looks like

| Construction | Does any account breach IC-7? | `max ÷ min` reached | Where the gap was |
|---|---|--:|---|
| *(yours)* | yes / no | *(number)* | *(one line)* |

**Or:** an argument that the space is empty, of the form *"any construction with property X breaches IC-7, and every construction has property X."*

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **The space is empty for attack (b) and open for attack (a).** We expect backdating to be the real hole, and we expect it to be an implementation question rather than an arithmetic one |
| **Refutation threshold** | **Any construction reaching `max ÷ min > 24 ÷ F` with no per-day IC-7 breach refutes §5.5.5 as written.** There is no margin on this one — the claim is an exact bound, so one counterexample settles it |
| **What we do if it is crossed** | §5.5.5 gains a fifth condition naming where IC-7 must be evaluated, or the bound is restated as conditional on it. **The 2.4× figure does not survive unqualified** |

**And say the unflattering part plainly.** Foundations §5.5.7 already concedes that this statistic **reads no accounts** — *"insert a fabricated account and the figure moves by 0.00."* **A bound is not a detector.** This brief asks whether it is even a bound.

## 8. Self-tests, each able to fail

1. **A population where every account claims exactly 24 h/day returns exactly `24 ÷ F`.** If it returns anything else, the statistic is not what we think it is.
2. **A population where every account claims exactly `F` returns exactly 1.0.**
3. **Inserting an account at the floor into any population leaves the statistic unchanged.** *(This one is expected to pass and is a control — §5.5.7 says the statistic is blind to it.)*
4. **Removing the single highest account lowers the statistic.** If it does not, `max` is not being computed.

## 9. Out of scope

- **Whether the bound matters.** That is §5.5.5's four conditions and is argued elsewhere.
- **Cross-network comparison.** Foundations §4.0 says no book is ever added to another, so the statistic describes one network's books. **A construction spanning two networks does not refute it.**
- **Fraud detection.** The bound does not detect anything and does not claim to.
- **A population of mixed ages.** The statistic divides by days lived, so age is already removed from it. **Building two accounts of different ages is not an attack surface.**

## 10. Known ways to get this wrong

- **Scoring `max(ρ·c) ÷ (ρ·F)` instead of `24 ÷ F`.** We did this ourselves on 2026-09-02 and withdrew the file. **ρ cancels; it is not part of the claim.**
- **Reading "the statistic did not move" as robustness.** It usually means the statistic never looked.
- **Assuming `F` is a per-person value.** It is a network constant.
- **Comparing lifetime totals.** `F·D ≤ C(i) ≤ 24·D` cancels `D` only when both accounts have lived the same number of days. **Divide each account's credit by its own days lived before taking the ratio.**
