# Span-estimate generosity across competing networks — RESULTS

Code: `span_generosity.py` in this folder. Raw output: `RUN.txt`, `sweep.csv`, `sweep_summary.json`.

## 1. The question (quoted from request sr-20260919-sweep-span-estimate-generosity-across-compet)

> Sweep span-estimate generosity across competing networks. Each network sets F (published, comparable) and a span-estimation policy (per-person, not published). Measure whether the seller-choice discipline 5.5.5 relies on to arrest floor-shopping also arrests a network that recruits by estimating undocumented spans generously, and report the share of joiners it moves at each generosity level.

## 2. Outcomes declared before running

Network 0 adds g extra years to each joiner's span. Four other networks add none. Baseline share for network 0 is 1/5 = 20%.

| # | Declared outcome | Kind |
|---|---|---|
| D1 | **Level:** with g = 0 network 0 holds 20% ± 3 points of joiners. If not, the model is biased and nothing else counts. | level |
| D2 | **Level:** with joiners fully informed and no seller detection, g = 5 years moves network 0 above 50%. If it does not, there is no lever to arrest, and the question is empty. | level |
| D3 | **Level:** with detection on, g = 5 takes network 0 below 25%. If not, seller choice does not reach spans. | level |
| D4 | **Change:** the smallest g that detection arrests, for a seller sampling 200 new accounts, is no larger than 3 years. | level / threshold |
| D5 | **Arithmetic (not simulated):** inside the rationing band (rho ≤ rho*) an extra declared year gives a joiner *negative* gate slack, so any recruiting lever is pledge budget (say), not consumption. | could fail: if rho·F > 3.78 h/day the gain flips positive |

## 3. The numbers

**Arithmetic, per extra declared year** (Foundations §4.4 table of rho*; 1,380 h/yr median lifestyle):

| F (h/day) | rho* | Budget added, F·365 | Gate slack added, rho*·F·365 − 1,380 |
|--:|--:|--:|--:|
| 2 | 1.017 | +730 h | **−638 h** |
| 10 | 0.330 | +3,650 h | **−176 h** |
| 14 | 0.253 | +5,110 h | **−87 h** |

Break-even rho·F = 3.78 h/day. At rho* all three floors sit below it (2.03, 3.30, 3.54). So a generous span adds pledge budget and takes slack away from the gate. D5 holds.

**Simulation** (20 replications, seeds 20261120..20261139, 500 joiners per round, rounds 21–40 counted; spread across replications is ≤ 0.05 in every cell and ≤ 0.005 where noted). Share of joiners choosing network 0 (baseline 0.20):

| g (extra years) | No detection, phi=0 | No detection, phi=0.25 | No detection, phi=1 | **Detection, phi=0** | Detection, phi=0.25 | **Detection, phi=1** | Share of rounds flagged |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 0 | 0.200 | 0.200 | 0.200 | 0.200 | 0.200 | 0.200 | 0.00 |
| 1 | 0.200 | 0.235 | 0.342 | 0.188 | 0.221 | 0.321 ± 0.021 | 0.07 |
| 2 | 0.200 | 0.279 | 0.519 | 0.062 | 0.087 | 0.162 ± 0.044 | 0.69 |
| 3 | 0.200 | 0.322 | 0.691 | 0.001 | 0.002 | 0.004 | 0.995 |
| 5 | 0.200 | 0.376 | 0.906 | 0.000 | 0.000 | 0.000 | 1.00 |
| 8 | 0.200 | 0.397 | 0.989 | 0.000 | 0.001 | 0.004 | 1.00 |

phi = share of joiners who learn g before joining. Detection = sellers compare the mean backdated-credit years of 200 sampled new accounts across networks (z > 3 flags), flagged network loses half its sellers.

**How many accounts a seller must sample** (smallest g flagged in over half the rounds): 4 accounts: none up to 8 years. 25 accounts: 5 years. 200 accounts: 2 years. 2,000 accounts: 1 year.

**Sensitivity to the cost of being refused** (share at g = 5, phi = 1, detection on): cost 0 → 0.906; 1 → 0.780; 2 → 0.567; 5 → 0.061; 10 → 0.0004; 20 → 0.

**Control (floor-shopping, F = 14 against 10, published):** share 0.823 with no seller discipline, 0.0002 when sellers refuse. This tests the same machinery on the case 5.5.5 says is arrested.

**Declared outcomes against results:** D1 met (0.200 ± 0.005). D2 met (0.906). D3 met only when the seller discipline can *see* the span (0.000). D4 met (2 years at n = 200). D5 met.

## 4. What this does not show

1. **The arrest does not come from F being published. It comes from a second, different signal: backdated credit visible in aggregate on the public log.** That signal is my assumption (ASSUMED 1). If a network's private ledgers hide the dates (§4.7 splits public market data from private ledgers, and OP-22 is open), the detection arm collapses to the "no detection" arm, and a fully informed joiner population moves 34% at g = 1 and 91% at g = 5.
2. **The result is set largely by two numbers I chose:** the cost to a joiner of a refused network (10 units) and the worth of a fabricated year to them (10% of a real one). Cost ≤ 2 leaves the lever alive (share 0.57 at g = 5). The sweep above shows the threshold, not a measured value. Nobody has measured either.
3. **Small inflation slips through.** At g = 1 the network is flagged in 7% of rounds, and informed joiners move 12 points above baseline (0.321). With 200 sampled accounts the arrest starts at about 2 years. Whether 1 extra year of span is a "generous estimate" or an ordinary tolerance is not decided by anything here.
4. **I modelled one cheater among identical networks, one policy dial (extra years).** A network could inflate selectively (only people who cannot be checked), or inflate every account by a little. I did not test either. Both make the aggregate statistic harder to separate from honest spread (my honest spread, mean 8 and sd 6 years, is also a guess).
5. **No behaviour data.** Whether joiners pre-quote, whether sellers read the log, and whether a joiner values pledge budget at all are all untested. phi was swept as an input, not measured.
6. **The gate does not reward the fabricated year** (D5), so the lever modelled is pledge budget. A recruit who wants to consume more gains nothing from generosity inside the rationing band. Above rho* the gate does not ration (§5.5.3) and a fabricated year's slack gain flips sign, but then slack does not bind either.
7. **The 24 ÷ F bound is untouched** because a fabricated year still carries the floor on every day (§4.4 cond. 3, §5.5.5 cond. 4). I did not simulate a defective evaluator.

## 5. Command and seed

```
python 06-simulation/span-generosity/span_generosity.py --test
python 06-simulation/span-generosity/span_generosity.py > 06-simulation/span-generosity/RUN.txt
```
Seed: `BASE_SEED = 20261120`, replication k uses `BASE_SEED + k`, 20 replications.
