# What share of a person's days lived is attested, not observed? — results

> **Version:** 0.1
> **Date:** 2026-11-03
> **Code:** [`attested_share.py`](attested_share.py) · **Transcript:** [`RUN.txt`](RUN.txt) · **Declared outcomes:** [`DECLARED.md`](DECLARED.md)

## 1. The question

> *"Over a simulated joining population, what share of each person's days lived is ATTESTED (reconstructed back to birth from their own voluntary evidence) rather than OBSERVED on the network's own calendar? Report the distribution, not a mean, and report how the share falls as a cohort ages inside the network."*

Why it was asked: the repaired ceiling's denominator D is attested on the pre-join span (coywolf c56412). The bound is an instrument only on the observed span. Nobody had a figure for how large the attested span is.

## 2. Declared before running

Eight outcomes: seven over a level, one over a shape. Full text in [`DECLARED.md`](DECLARED.md). Examples: founding wave, days-weighted share at 40 years in [0.15, 0.45]; at 80 years below 0.10; linear 20-year adoption at 20 years in [0.45, 0.80]; cohort half-point equals median joining age within 2 years.

## 3. The numbers

**The model.** Person i has birth b, death d, join time j = max(b, J), where J is a draw from an adoption curve. Attested days = j − b (zero if born inside). Days lived = T − b. Share = attested ÷ days lived, over members alive at T. 200,000 people alive at founding (stylised US age pyramid), births replace deaths (Gompertz mortality, mean life 79.5 y), 401,249 people in all. "Days-weighted" = total attested days ÷ total days lived across all members.

**Person-level distribution, full reconstruction back to birth.** Years since founding, T.

| Scenario | T | Members | p10 | p25 | **median** | p75 | p90 | Days-weighted | Share born inside (share 0) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Founding wave (all join day 0) | 0 | 200,000 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0% |
| | 10 | 205,305 | 0.00 | 0.53 | 0.75 | 0.84 | 0.87 | 0.77 | 12% |
| | 20 | 206,030 | 0.00 | 0.02 | 0.52 | 0.68 | 0.74 | 0.58 | 24% |
| | 40 | 202,388 | 0.00 | 0.00 | 0.01 | 0.36 | 0.48 | 0.28 | 49% |
| | 60 | 199,737 | 0.00 | 0.00 | 0.00 | 0.02 | 0.22 | 0.09 | 74% |
| | 80 | 199,087 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.011 | 94% |
| Linear 20-year adoption | 10 | 102,550 | 0.39 | 0.76 | 0.88 | 0.94 | 0.98 | 0.88 | 6% |
| | 20 | 206,030 | 0.00 | 0.52 | 0.76 | 0.88 | 0.95 | **0.78** | 12% |
| | 40 | 202,388 | 0.00 | 0.00 | 0.27 | 0.52 | 0.64 | 0.42 | 37% |
| | 60 | 199,737 | 0.00 | 0.00 | 0.00 | 0.19 | 0.36 | 0.17 | 62% |
| Linear 40-year adoption | 20 | 103,203 | 0.00 | 0.52 | 0.76 | 0.88 | 0.95 | 0.78 | 12% |
| | 40 | 202,388 | 0.00 | 0.01 | 0.52 | 0.76 | 0.90 | 0.60 | 25% |
| | 80 | 199,087 | 0.00 | 0.00 | 0.00 | 0.02 | 0.26 | 0.105 | 74% |
| Logistic, 60% ceiling | 20 | 119,431 | 0.00 | 0.50 | 0.75 | 0.85 | 0.91 | 0.77 | 13% |
| | 40 | 121,275 | 0.00 | 0.00 | 0.27 | 0.53 | 0.63 | 0.42 | 37% |
| Young adopt first (linear 20) | 20 | 206,030 | 0.00 | 0.52 | 0.69 | 0.80 | 0.86 | 0.73 | 12% |
| | 40 | 202,388 | 0.00 | 0.00 | 0.27 | 0.46 | 0.56 | 0.38 | 37% |

**Cohort ageing inside the network.** Founding-wave cohort, survivors only; each cell is the median share, with p10–p90 beside it (absolute survivors in the last column).

| Joined at age | s = 5 y | s = 10 y | s = 20 y | s = 30 y | s = 40 y | s = 50 y | Survivors at s = 20 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 18–29 | 0.83 [0.79, 0.85] | 0.71 [0.66, 0.74] | 0.55 [0.49, 0.59] | 0.44 | 0.37 | 0.32 | 31,389 |
| 30–49 | 0.89 | 0.80 [0.76, 0.83] | 0.66 [0.61, 0.71] | 0.56 | 0.48 | 0.42 | 47,867 |
| 50–69 | 0.92 | 0.86 [0.84, 0.87] | 0.74 [0.72, 0.77] | 0.65 | 0.57 | 0.51 | 29,781 |
| All adults | 0.90 [0.83, 0.94] | 0.81 [0.70, 0.87] | 0.66 [0.53, 0.76] | 0.54 [0.42, 0.65] | 0.44 [0.34, 0.54] | 0.36 [0.28, 0.44] | 112,131 |

A cohort's share falls as a ÷ (a + s), where a is age at joining and s is years since joining. Worked: age 40 at joining, 20 years later: 40 ÷ 60 = 0.67. The table agrees (0.66 for ages 30–49).

**Declared outcomes: 7 of 8 held, 1 missed.** O1, O2, O3, O4, O5 held. O4 held narrowly (0.781 against an upper bound of 0.80). **O6 missed:** the adult cohort's median share reached 0.5 at s = 34.0 y, while the cohort's median joining age was 47.3 y. I expected them within 2 years. The reason is survivors: by s = 34 the oldest joiners have died, so the survivors are younger than the starting median.

**Reach sensitivity.** If joiners rebuild only part of their pre-join life (reach drawn Beta(2,2), mean 0.5), linear 20-year adoption at T = 20 gives a days-weighted attested share of **0.39**, and another **0.39** is estimated-only (in the books by A7, but backed by no evidence of the person's own). Observed share is unchanged at 0.22. This scaling is arithmetic, and no outcome was declared on it.

**The observed share, which is what the bound is an instrument on.** One minus the days-weighted figures above. Linear 20-year adoption: 0.22 at T = 20, 0.58 at T = 40, 0.83 at T = 60. Founding wave: 0.42 at T = 20, 0.72 at T = 40, 0.99 at T = 80.

## 4. What this does not show

1. **The result is conditional on joining age, and joining age is an assumption.** No adoption data exists. The age pyramid is stylised and typed from memory, not retrieved. Five adoption shapes agree on the broad outline but a network that recruits mostly the very young would give far lower attested shares.
2. **The model makes everyone join when they are alive and eventually joins everyone.** Ceilings below 100% appear only in the logistic scenario. People who join late and keep a strong tie to a non-member world, or leave and rejoin, are not modelled.
3. **"Attested" here means the days before the join date, full stop.** It does not measure how well each pre-join day is evidenced. Under Foundations §4.4, an undisclosed day is estimated, not attested. Only the reach scenario touches this, and its Beta(2,2) reach is invented.
4. **A newborn who joins at birth has 0% attested.** That assumes a child's account starts at birth. Who consents for a child is the network's rule (§4.6) and could change this.
5. **It does not say what the bound does on the observed span.** It gives the size of the span the bound can be an instrument on, not whether the bound works there.
6. **Mortality is a simple Gompertz curve, population is held roughly stationary,** and migration, war and age-dependent leaving are not modelled.
7. **Days are counted as calendar time,** not weighted by credit, so a day of 24 hours and a day of 10 hours count the same.

## 5. Command and seed

```
cd 06-simulation/attested-share
python attested_share.py --test
python attested_share.py > RUN.txt      # seed 20261103
```

Run 1 contained a bug (the initial-population flag was inverted). It changed only the "young adopt first" scenario and the cohort table, which came back empty. The self-test "init mask = born before day 0" was added and run 2 is the one reported. Run 1 is kept in `RUN-1_inverted-init-mask.txt`. No declared outcome was changed between runs.
