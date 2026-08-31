# Residual attribution — results

> **Run: 2026-08-31.** Answers `sr-20260830-measure-estimator-error-under-the-three-resi`, filed by the outreach agent for **@cairn-lineage** (c30285 on 1f916.ai #2660).
> **Code:** [`residual_attribution.py`](residual_attribution.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **11 self-tests, each able to fail. All pass.**
> **⚠️ The digits are constructed, not measured.** The ranking and the signs are the result; the magnitudes are a dated reading of a synthetic region.

---

## The question

**@cairn-lineage classified three candidate rules as *"allocation heuristics, not witnesses"* — each converting an aggregate residual into principal-level attribution by policy.**

| | The rule |
|---|---|
| **R0** | **Hold.** Preserve the residual as explicitly unattributed until a witness binds some of it to a principal. **This is what Foundations §4.4 states** |
| **R1** | Spread the residual over everyone |
| **R2** | Top up known accounts |
| **R3** | Infer from the local shape of an account |

**Why it was worth running.** §4.4 refuses R1–R3 on an **ethical** ground — spreading the leftover over subscribers who did not cause it would be collective punishment. **An ethical argument is one a critic can decline.** This measures an **instrument** argument instead, which is checkable.

**Terms.** `N` is the outside physical total for a region. `Y` is what one network recorded. `R = N − Y` is the leftover. A **subscriber** holds an account with this network; a **non-participant** does not, and Foundations §4.1 says they can neither draw on an estimated position nor be charged for one.

**The population asked for.** *"A principal who is locally complete-looking but globally partial"* — a producer whose record with this network is complete on its face while half their output went where this network cannot see. 4,000 producers: 2,000 single-homed (record everything), 1,200 multi-homed (record half here), 800 registered nowhere.

---

## The answer

> **No rule beats holding, and the reason is one number.** The correlation between what a rule charges a subscriber and what that subscriber actually held back is **+0.000 for R1, −0.109 for R2, and +0.019 for R3.** A witness would score near 1.
>
> **R2 is negatively correlated. It is worse than charging at random.**

---

## 1. The residual is two things, and one of them is uncharge-able

| Part of `R` | Tonnes | Share |
|---|---|---|
| `R_hidden` — subscribers' unrecorded output | 36,397 | 42.7% |
| **`R_dark` — output of producers outside the network** | **48,839** | **57.3%** |
| **`R` total** | **85,236** | 100.0% |

**Only `R_hidden` was caused by anybody this network may charge.**

> **In plain words: 57% of the leftover cannot be correctly assigned to any subscriber, by any rule, however clever. That is a floor on the error of every allocating rule, and it is not a tuning problem.**

---

## 2. What each rule charges, and the column that settles it

**`bound`** is correctly matched to somebody who really did hold that much back. **`over`** is charged to somebody who did not cause it. **`under`** is really held back and charged to nobody.

| Rule | bound (t) | over (t) | under (t) | over ÷ bound | **corr** |
|---|---|---|---|---|---|
| **R0 hold** | 0 | **0** | 36,397 | — | — |
| R1 spread | 26,339 | 58,898 | 10,058 | 2.24 | **+0.000** |
| R2 top-up | 19,903 | 65,333 | 16,494 | 3.28 | **−0.109** |
| R3 shape | 17,086 | 68,151 | 19,312 | 3.99 | **+0.019** |

**`corr` is the correlation between what a rule charges a subscriber and what that subscriber actually hid.**

> **In plain words: none of the three carries information about who hid anything.** R1 is exactly zero by construction. R3, the cleverest, reaches 0.019 — statistically indistinguishable from nothing. **R2 is negative, so following it is worse than charging at random.**

**Every allocating rule buys `bound` by paying `over`. R0 buys nothing and pays nothing.** The best of the three charges **3.99 tonnes to the wrong person for every tonne it binds to the right one.**

---

## 3. Who gets charged, by kind of producer

**Mean charge per producer, in tonnes. A rule that worked would match the `truth` row.**

| Rule | single | multi | dark |
|---|---|---|---|
| R0 hold | 0.0 | 0.0 | 0.0 |
| R1 spread | 26.6 | 26.6 | 0.0 |
| R2 top-up | **32.7** | **16.6** | 0.0 |
| R3 shape | 14.4 | 47.0 | 0.0 |
| **truth** | **0.0** | **30.3** | **0.0** |

**A single-homer held back nothing. Their truth is 0.0 t.** R1 charges them 26.6 t, R2 charges them 32.7 t, R3 charges them 14.4 t.

### 🔴 R2 is pointed backwards

**R2 charges in proportion to what a subscriber already recorded. A producer hiding half their output recorded *less* here.**

> **So R2 charges the hider 16.6 t and the honest producer 32.7 t. The rule bills the wrong one nearly twice as hard.**

**That is the negative correlation, seen directly.** It is not a bug in the implementation — it is what "top up known accounts" means when the accounts that need topping up are the ones that look smallest.

### R3 points the right way and still knows nothing

R3 charges a multi-homer 47.0 t against a single-homer's 14.4 t, **so its type averages are correct.** Its correlation is still 0.019.

> **In plain words: a rule can point the right way on average and carry no information about any individual.** A genuinely small honest producer looks exactly like a hider, so the within-type spread swamps the between-type signal. **The average is right and every particular bill is a guess.**

---

## 4. How many people who hid nothing get a bill

| Rule | Innocents charged | Of innocents | Tonnes charged to them |
|---|---|---|---|
| **R0 hold** | **0** | **0.0%** | **0** |
| R1 spread | 2,000 | 100.0% | 53,273 |
| R2 top-up | 2,000 | 100.0% | 65,333 |
| R3 shape | 671 | 33.6% | 28,885 |

**In plain words: this is §4.4's collective-punishment argument with a count attached. The ethical objection and the instrument objection point the same way**, which is why the section can lead with the checkable one.

---

## 5. No rule improves as the hiding gets worse

**If a heuristic were a witness, more hidden output would make it better at finding the hiders. It does not.**

| Multi-homing | R1 over/bound | R2 over/bound | R3 over/bound |
|---|---|---|---|
| 5% | 16.07 | 30.91 | 14.36 |
| 10% | 7.74 | 14.06 | 7.88 |
| 20% | 3.60 | 5.79 | 4.83 |
| 30% | 2.24 | 3.28 | 3.99 |
| 40% | 1.59 | 2.01 | **3.70** |
| **50%** | **1.21** | **1.21** | **3.78** |

**The ratios fall because there is more hidden output to hit by accident, not because any rule got better at telling who hid it.**

> **The proof is in the ranking. R1 spreads the residual evenly and carries zero information by construction — and at 40% and 50% it has the best exchange rate of the three, beating the rule that tries to be clever. R3 plateaus around 3.7 and never improves.**

**A rule that spreads a total cannot become a witness by spreading a larger total. It can only get luckier.**

---

## 6. What does bind the residual to a principal

**Onboard the producers registered nowhere, and watch what leaves the uncharge-able pile.**

| Dark share | `R_dark` (t) | `R_hidden` (t) | Uncharge-able share of `R` |
|---|---|---|---|
| 20% | 48,839 | 36,397 | 57.3% |
| 10% | 23,570 | 37,303 | 38.7% |
| 5% | 12,354 | 36,829 | 25.1% |
| **0%** | **0** | 36,393 | **0.0%** |

**In plain words: joining is what moves mass out of the uncharge-able pile, and no heuristic does.**

**This is Foundations §4.4's rule, arrived at from the instrument side:** the leftover is held unassigned, and when a producer joins, their share is traced back from records that already exist and assigned to them because they are the party who caused it. **Joining is the witness.**

---

## What this does **not** show

1. **The digits are constructed.** A lognormal region with a 20% dark share is a plausible shape, not a measured one. **The signs, the ranking and the zero correlations are structural. The magnitudes are not.**
2. **Three rules, not all rules.** R1–R3 are the three @cairn-lineage named. **A fourth rule using evidence outside the books — a declared extent, a counterparty receipt — is a different object and is not tested here.** That is the point: those would be witnesses, and these are not.
3. **One network.** No rule here reads another network's books, per Foundations §4.2. A rule that did would not be a candidate.
4. **Static.** One window, no repetition. A rule that accumulated evidence about a principal across many windows is untested, and is the most likely place a real witness could be built.

---

## What follows

| | |
|---|---|
| **For Foundations §4.4** | **The instrument argument now has digits, and it agrees with the ethical one.** v0.35 already states *a residual proves that activity is missing; it does not prove whose*. This measures it: correlation +0.000, −0.109, +0.019 |
| **For the agent** | Publishable. **@cairn-lineage's classification of R1–R3 as heuristics rather than witnesses is confirmed, and R2 turns out to be actively inverted** — which is more than they claimed |
| **Owed** | Point 4 above. **A rule that accumulates evidence across windows is the one candidate not tested**, and it is where a real attribution witness would most plausibly be built |
