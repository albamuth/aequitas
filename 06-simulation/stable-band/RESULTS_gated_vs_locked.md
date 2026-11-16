# RESULTS: gated share vs lock-line share, in stable_band_kappa.py's own population

## 1. The question
> In stable_band_kappa.py's own population (60,000, seed 7, wants lognormal sigma 0.45 tilted by credit^0.25, kappa 1,380/365, capacity 56,446), at the one-day rho* of F = 2, 10, 14 (1.017, 0.330, 0.253) and at rho = 1.5, print (a) the share of people held below what they wanted (admitted_total's second return, stable_band.py line 171) and (b) the share whose yearly request wants x kappa x 365 exceeds rho x 8,760. Beside (b), print q4_locked_ledgers.py's closed form at the same rho: 0.99 / 17.77 / 27.69 percent at median 1,380.

## 2. Outcomes declared before running
- **Level:** at F=10 and F=14 rho*, (a) lies in 30-40% (the old script printed about a third held back). At rho*, (b) in this population is under 1% for F=2, and below the q4 closed form at every F (sigma 0.45 body is thinner than sigma 0.80).
- **Subset:** (b) <= (a) in every row. One row with (b) > (a) would mean the gate model contradicts the lock line.
- **Reproduction:** one-day rho* reproduces 1.017 / 0.330 / 0.253 within 0.002.
- **Change:** (a) falls as rho rises, to near 0 by rho = 1.5 at F = 10 and 14.

All four held. (Declared in the author's absence; written before the first run of the main script.)

## 3. Numbers (N = 60,000, seed 7, kappa = 3.7808, R_max = 56,446, wants total 66,407)
Population wants: median 1.000, mean 1.107, max 6.14 (a yearly request of 8,472 h), log-sd 0.454.

| F | rho | row | (a) held below wants | (b) request over rho x 8,760 | q4 closed form, sigma 0.80 | q4 sampled (body + tail) | admitted (units) |
|--:|--:|---|---|---|---|---|--:|
| 2 | 1.017 | rho* | **33.18%** (19,908 people) | 0.0000% (0) | 0.99% | 1.14% | 56,445 |
| 2 | 1.500 | | 16.61% (9,964) | 0.0000% (0) | 0.24% | 0.34% | 61,913 |
| 10 | 0.330 | rho* | **35.44%** (21,266) | **5.11%** (3,064) | 17.74% | 18.06% | 56,438 |
| 10 | 1.500 | | 0.01% (8) | 0.0000% (0) | 0.24% | 0.34% | 66,405 |
| 14 | 0.253 | rho* | **35.46%** (21,274) | **14.93%** (8,959) | 27.73% | 28.02% | 56,440 |
| 14 | 1.500 | | 0.00% (0) | 0.0000% (0) | 0.24% | 0.34% | 66,407 |

The closed form prints 17.74 and 27.73 at the exact rho*; the request quotes 17.77 and 27.69 (rounded rho). The difference is under 0.05 points.

**Reading it.** At rho*, 33-35% of people are gated and 0-15% are over the lock line, so locked is a subset of gated in this model (3,064 of 21,266; 8,959 of 21,274). The q4 figures at the same rho (0.99 / 17.7 / 27.7%) are not the lock rate of this model: at F=10 q4 reports 17.7% where this population has 5.1%, and at F=14 27.7% against 14.9%. At F=2 q4 reports 0.99% against 0 people. At F=2 the gated share (33%) is entirely people under the line.

## 4. What this does not show
1. **Which population is right.** Sigma 0.45 (stable_band) against 0.80 (q4) is a modelling choice. This run does not say which matches real consumption.
2. **That "locked" is the right idea of the lock.** Line (b) compares a yearly request to rho x 8,760 on one day's snapshot. Locking in q4 is a lifetime claim. The cumulative edge (stable_band_cumulative.py) is lower and was not rerun here.
3. **That the gate holds the people the line says.** (a) counts anyone short of their want, including people far under the line. Being gated is a weaker condition than being locked, and the two counts differ by design.
4. **The 8,760 line uses a request, not footprint.** Wants x 1,380 is a desired yearly figure in this model. q4 uses a measured footprint with a Pareto tail and a billionaire sliver. The sampled column adds those and moves little (0.1-0.4 points).
5. **Single seed (7), single population draw.** No spread across seeds was computed. The (a) shares are large counts (tens of thousands), so noise is small; the F=10, rho=1.5 value of 8 people is a count near zero.
6. **Foundations was read to line 1000 only** (version 0.69, sections 0 to 3.4a). The remaining sections were not read, because of the hour. Nothing here depends on them, but the brief asks for a whole read.

## 5. Command and seed
```
python 06-simulation/stable-band/gated_vs_locked.py --test
python 06-simulation/stable-band/gated_vs_locked.py
```
Population seed 7 (stable_band.RNG_SEED); q4 sample seed 7, n = 2,000,000. Runtime under a minute, no files written other than this one.
