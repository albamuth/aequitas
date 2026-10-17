# honest-label — RESULTS

> **Date:** 2026-10-17 · **Run by:** the nightly simulation agent · **Foundations read:** v0.60
> **Answers:** `sr-20260904-does-a-producer-who-labels-each-published-fi` (SB-04, asked by @coywolf at c39152)

## 1. The question

> Does a producer who labels each published figure metered or modelled out-compete one who does not, or does the honest label only hand rivals a cheaper attack surface? Sweep the share of labelling producers and measure whether labelling is stable under counterparty discounting.

## 2. Outcomes declared before the run

Full table with the failure condition of each: [`DECLARED.md`](DECLARED.md), written before `python labelling_game.py` ran.

| # | Kind | Declared | Result |
|---|---|---|---|
| D1 | **Level** | "Stay" threshold within a factor of 2 of the brief's prior `q·g·m` = 0.024, so in [0.012, 0.048] | **Held.** 0.0256 |
| D2 | **Level** | Transfer-conserving worked example leaves labelling ahead by 1.0–2.0 points | **Held.** 1.49 points |
| D3 | Change | A lone labeller does worse than the unlabelled residents | **Held.** 3.60% against 5.02% of trade |
| D4 | Change | The invade threshold is more than 3× the stay threshold | **Held.** 0.620 against 0.0256, 24× |
| D5 | Refutation | From p = 0.5, labelling collapses below p = 0.5 in more than half the attack-active cells | **My prediction was wrong.** 17.7% (7.1% with collusion). The brief's refutation threshold is **not** crossed |
| D6 | Change | Collusion among rivals lowers both thresholds | **Held.** Stay 0.0256 → 0.0127, invade 0.620 → 0.271 at c = 0.5 |

**Terms.** *Stay* threshold: the smallest discount `d` at which one producer who drops the label loses against an all-labelling market. *Invade* threshold: the smallest `d` at which one lone labeller gains against an all-unlabelled market. *Attack-active cell*: a parameter cell where at least one rival finds an attack on a labeller worth its cost. In every other cell the label cannot lose, so those cells say nothing.

## 3. The numbers

**Model.** One good, `N` = 20 producers, one round repeated. Unlabelled figure × (1 + `d`). Each rival may pay `a` to challenge one producer, aiming at the higher expected prize `q_T·g·s_T`, and challenges only if the prize exceeds `a`. A success moves `g` of the target's remaining trade to the attacker. `q_L = q·m`, `q_U = q·m / ratio`, `a = α·g/N`. Payoff = trade share minus attack costs paid. Closed-form expectation, checked against Monte Carlo.

**Headline cell:** `N`=20, `d`=0.15, `m`=0.4, `q`=0.3, `q/q'`=6, `g`=0.2, `α`=0.05, no collusion. Equal split would be 5.00% each.

| Labellers `n_L` of 20 | Labeller payoff | Unlabelled payoff | Gap (L − U) | Monte Carlo L (±1 SE, 40,000 rounds) |
|--:|--:|--:|--:|--:|
| 1 (lone) | **3.60%** | **5.02%** | **−1.43 points** | 3.599% ± 0.005 |
| 3 | — | — | −0.10 points | — |
| 4 | — | — | +0.09 points | — |
| 5 | 5.11% | 4.90% | +0.21 points | 5.112% ± 0.001 |
| 10 | 5.17% | 4.73% | +0.45 points | 5.174% ± 0.001 |
| 15 | 5.08% | 4.57% | +0.51 points | 5.077% ± 0.000 |
| 19 (one deviant) | **4.98%** | **4.44%** | **+0.53 points** | 4.977% ± 0.000 |

Discount alone (no attacks) at `n_L` = 10 would give 5.35% against 4.65%, a gap of 0.70 points. Attacks eat 0.25 of that 0.70.

**Class: bistable.** Labelling is stable once most producers label, and does not start from one. The labelled share has to pass about **0.20** (4 of 20) before labelling grows.

### Thresholds (headline cell unless stated)

| Quantity | Stay `d*` | Invade `d*` |
|---|--:|--:|
| Headline | **0.0256** (prior `q·g·m` = 0.024) | **0.620** |
| Rival attack aimed blind (uniform target) | 0.0213 | ≈ 0 (labelling starts at once) |
| Collusion `c` = 0.25 / 0.5 / 0.75 / 0.9 | 0.019 / 0.013 / 0.006 / 0.003 | 0.434 / 0.271 / 0.127 / 0.049 |
| `g` = 0.05 / 0.1 / 0.2 / 0.3 / 0.4 | 0.006 / 0.013 / 0.026 / 0.039 / 0.052 | 0.125 / 0.269 / 0.620 / 1.09 / 1.71 |
| `N` = 5 / 10 / 20 / 50 / 200 | 0.031 / 0.027 / 0.026 / 0.025 / 0.024 | 0.119 / 0.266 / 0.620 / **2.41** / **none up to d = 3** |
| `α` = 0 / 0.02 / 0.05 / 0.10 | all 0.0256 | 0.630 / 0.630 / 0.620 / 0.603 |
| `α` = 0.15 (no attack on a labeller pays) | ≈ 0 | ≈ 0 |

**By `q/q'` with rivals who aim at the best prize:** stay `d*` is 0.0256 for every ratio from 2 to 24 and ≈ 0 at ratio 1. Invade `d*` is 0.60–0.63 at every ratio. **The ratio drops out because the rival aims at one type only.** With **blind** aim the ratio matters: stay `d*` = 0.0127 / 0.0170 / 0.0213 / 0.0235 / 0.0245 at ratio 2 / 3 / 6 / 12 / 24, climbing towards `q·m·g` = 0.024.

### The brief's worked example, three ways (2 producers, `m`=1, `d`=0.15, `q`=0.3, `q'`=0.05, `g`=0.2, free attack)

| Reading | Labelled | Unlabelled | Gap |
|---|--:|--:|--:|
| Discount only | 53.5% | 46.5% | 7.0 points |
| Brief's arithmetic (attack losses subtracted, gains dropped) | 50.3% | 46.0% | 4.2 points; the two shares sum to 96.3% |
| **Attack gains returned to the attacker** | **50.7%** | **49.3%** | **1.5 points**; sums to 100% |

### Grid over the brief's suggested ranges

`d` ∈ {0, .05, .1, .15, .2, .3, .4, .5} × `m` ∈ {.1, .25, .4, .6, .9} × `q` ∈ {.05, .15, .3, .45, .6} × `q/q'` ∈ {1, 3, 6, 12} × `g` ∈ {.05, .1, .2, .3, .4} × `α` ∈ {.02, .05, .1, .2} = 16,000 cells per setting. 8,500 have `d` > 0 and an attack on a labeller worth launching.

| Setting, attack-active cells with `d` > 0 | Start at p = 0.5 ends below 0.5 | All-labelling resists one deviant | Lone labeller can invade | Bistable | Label wins everywhere | Label collapses everywhere | Median critical mass |
|---|--:|--:|--:|--:|--:|--:|--:|
| N=10 | 17.7% | 92.3% | 40.8% | 51.5% | 40.8% | 7.7% | 0.30 |
| **N=20** | **17.7%** | **92.6%** | **22.9%** | **69.7%** | 22.9% | 7.4% | 0.20 |
| N=20, half the rivals collude | 7.1% | 97.9% | 40.2% | 57.7% | 40.2% | 2.1% | 0.15 |
| N=50 | 17.7% | 92.6% | **7.7%** | **84.9%** | 7.7% | 7.4% | 0.16 |

**The two readings of the brief's refutation threshold disagree.** Started at p = 0.5, labelling collapses in under a fifth of cells, so the threshold ("more than half") is not crossed. Started with one labeller, labelling fails to start in 77% of cells at N = 20 and 92% at N = 50.

## 4. What this does not show

1. **Not that labelling is stable in a real market.** The discount `d` is a fixed input. In life it would move with the labelling share (if nearly everyone labels, an unlabelled figure reads worse), which would change the stay threshold. Total demand is also held at 1, so a discount never shrinks the market.
2. **Not that a challenge finds anything.** The success chance `q` is an input and does not depend on whether the modelled part is actually wrong. A producer whose model is right would repel challenges, and the label would cost them nothing. This model charges every labeller the same exposure.
3. **Not what Aequitas's own rule does.** §4.4's label is required, not chosen, and `not identified` is the default. This run covers a label producers may drop. The result that matters for a required rule is the stay threshold: 0.0256 at these settings, so dropping the label does not pay once the discount exceeds about 2.6%.
4. **The attack prize is private.** The attacker keeps the traded share it wins. §3.3a says the benefit of auditing a shared constant goes to every rival. If it is shared, attacks pay less, and the invade threshold falls. Collusion (c) is only a rough stand-in. Not run.
5. **The rivals are myopic and independent.** Each attacks if its first hit pays, whatever the others do. It gives the lone labeller its 19 attackers at N = 20. Rivals that see the prize falling after each hit would stop earlier. One good, one round repeated, no entry or exit, no reputation, no multi-good play.
6. **The invade threshold is driven by a modelling choice.** With value-aimed attacks and q = q', the lone labeller is still swamped (invade `d*` = 0.596), because it holds the largest share and so is the best prize. That is not the label's fault. Read the invade threshold as "when rivals can single out one producer".
7. **The grid fractions are not probabilities.** They count cells in a grid I chose, and the cells where no attack pays (5,500 of the 14,000 cells with `d` > 0, about two fifths) are excluded from the headline fractions. Counting them would push the "label wins" share up and say nothing new.
8. **One seed matters little here.** The tables are closed-form; the seed (20261017) only feeds the Monte Carlo cross-check and the self-tests.

## 5. Exact command and seed

```
cd 06-simulation/honest-label
python labelling_game.py --test      # 9 self-tests, about 3 s
python labelling_game.py             # writes results.json, about 25 s
```

Seed `20261017`. Python 3.14.3, numpy. Writes about 11 KB.

**Self-tests (each can fail):** T1 at d = 0 labelling cannot gain · T2 at q = q' with blind aim, labelling wins for every d > 0 · T3 at m = 0 no attack happens · T4 shares sum to 1 · T5 first and last of four identical producers earn the same, and a fixed attack order is caught (z = 33) · T6 closed form against Monte Carlo (worst z = 3.55, worst gap 1.9e-4) · T7 the brief's worked example · T8 a deliberately wrong model (attack cost ignored) is rejected by T6's tolerance.
