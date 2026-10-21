# Resolution tax — results

> **Date:** 2026-10-19
> **Request:** `sr-20260905-sweep-producers-of-one-good-by-scale-and-by-`
> **Foundations version read:** 0.60

## 1. The question

> Sweep producers of one good by scale and by affordable chain resolution, holding the physical process fixed. Measure the spread in published debit-hours per kilogram between the best-instrumented and the worst-instrumented producer. Report whether the spread widens with the number of steps in the chain.

Source objection: coywolf c40752 on post 3551. §3.4a's "a coarse reading is a ceiling" errs against the producer, so it is a charge on whoever cannot buy instruments. §4.8 registers the watch item.

## 2. Outcomes declared before running

**Honesty note.** These were fixed in my reasoning before the first run. They were written to this file after it. The launcher hash of this file therefore proves the date of the write-up, not of the declaration.

| # | Outcome | Kind | What would count against it |
|---|---|---|---|
| D1 | Equal-cost steps, one good leaving after a uniform step: mean coarse÷fine equals the harmonic number H_n (n=5: 2.28, n=12: 3.10) within 6% | **Level** | A simulation off H_n by more than 6% |
| D2 | The project's printed steer case reads 12.50 coarse, 2.00 fine, 6.25× | **Level** | Any other figure |
| D3 | The best-to-worst spread for a good that leaves early has a **median between 1.5× and 4×** at every n tested, with the default instrument price | **Level** | A median under 1.5× (tax is negligible) or over 4× (tax is large) |
| D4 | The **mean** spread rises with ln(n), with a bootstrap interval that excludes zero | Change | A slope interval containing zero |
| D5 | The **median** spread for early-leaving goods does **not** rise with n (slope within ±0.3 across n=2..30) | Change | A median that climbs past 3× |
| D6 | A terminal good (passes every step) has spread exactly 1.00 | Theorem | Any other value |

## 3. The numbers

Seed 20261019. 500 processes × 200 producers per cell. Four co-products per plant. One good studied per process. Producer scale Q is log-uniform from 10² to 10⁷ kg a year. Instruments cost 40 h per cut. A producer spends 2% of its own labour (0.05 h/kg) on them.

**Spread = worst published figure ÷ best published figure, for the same good from the same process.**

| n steps | mean spread | median | p10 | p90 | best h/kg | worst h/kg | goods that are terminal |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 1.88 | 1.00 | 1.00 | 3.63 | 0.702 | 0.997 | 0.53 |
| 3 | 2.76 | 1.49 | 1.00 | 5.73 | 0.597 | 1.077 | 0.30 |
| 5 | 3.20 | 1.65 | 1.00 | 6.37 | 0.507 | 0.958 | 0.22 |
| 8 | 4.25 | 1.76 | 1.00 | 9.43 | 0.501 | 0.994 | 0.12 |
| 12 | 3.68 | 1.86 | 1.02 | 8.64 | 0.466 | 0.956 | 0.10 |
| 20 | 4.73 | 1.83 | 1.04 | 8.60 | 0.459 | 1.027 | 0.07 |
| 30 | 4.70 | 1.94 | 1.07 | 9.63 | 0.463 | 0.995 | 0.03 |

The h/kg columns are medians over processes. **The worst-instrumented producer always reads about 1.0 h/kg because the chain is fixed at 100 h and the good's mass is drawn around 100 kg.** The best-instrumented producer reads about 0.46 to 0.70 h/kg. That is a gap of about 0.3 to 0.5 h/kg for a good that leaves early.

**Slope of mean spread against ln(n): 1.02, 95% bootstrap 0.74 to 1.34.** From n=2 to n=30 the mean goes from 1.88 to 4.70.

**Early-leaving goods only** (terminal goods have spread 1.00 by theorem):

| n | count of 500 | mean | median |
|--:|--:|--:|--:|
| 2 | 236 | 2.87 | 2.05 |
| 3 | 348 | 3.53 | 2.08 |
| 5 | 391 | 3.82 | 2.05 |
| 8 | 439 | 4.70 | 2.00 |
| 12 | 452 | 3.96 | 1.98 |
| 20 | 467 | 4.99 | 1.96 |
| 30 | 484 | 4.83 | 2.02 |

**Who pays.** At n=12 and the default instrument price, the median producer reads **2.96×** its true figure, and **32%** of producers read more than 1.5× it. Instrument price moves this a lot:

| Instrument price (h per cut) | spread | median producer ÷ truth | share above 1.5× |
|--:|--:|--:|--:|
| 4 | 4.29 | 1.03 | 21% |
| 40 | 4.29 | 3.71 | 34% |
| 400 | 4.29 | 4.29 | 47% |

(The spread does not move with price. Price only moves how many producers sit at the bad end.) Random cut placement instead of greedy placement changes the spread from 4.29 to 3.98. Co-product count m=2, 4, 8 gives spread 5.99, 4.29, 3.97.

**What the published figure leaves out** (§4.3: setup price sits on the asset). At n=12 a producer of 10⁵ kg a year pays 2 cuts, 0.0008 h/kg. A producer of 10⁷ kg pays 11 cuts, 0.00004 h/kg. These are 0.1% or less of the 0.5 to 1.0 h/kg that the figure moves.

## 4. Declared outcomes against what came back

| # | Result |
|---|---|
| D1 | **Passed.** Self-test: mean matches H_n at n=5 and n=12 within 6% |
| D2 | **Passed.** Reads 12.50, 2.00, 6.25× |
| D3 | **Passed on the median, failed on the mean.** Median for early-leaving goods is 2.0× at every n (range 1.96 to 2.08). The **mean** is 2.9× to 5.0× and is pulled up by a long tail (p90 about 8.6 to 9.6 at n ≥ 8) |
| D4 | **Passed.** Slope 1.02, interval 0.74 to 1.34 |
| D5 | **Passed.** Median for early-leaving goods: 2.05, 2.08, 2.05, 2.00, 1.98, 1.96, 2.02 |
| D6 | **Passed.** Terminal-good test, all resolutions |

**Answer to "does the spread widen with n?"** The **typical** early-leaving good: no. Its best-to-worst ratio is about 2× at every chain length. The **average** and the **worst cases**: yes, with ln(n). A longer chain lets a good leave very early, and a good leaving at step 1 of 30 carries 30× more than it consumed when read coarsely. The mean is dominated by these.

The mean series is not smooth (n=8 gives 4.25, n=12 gives 3.68, n=20 gives 4.73). With 500 processes per cell the mean has a wide spread because the tail is heavy. Read the slope, not any one point.

## 5. What this does not show

1. **The affordability rule is mine, and it decides who pays.** A producer here buys cuts only up to 2% of its labour. A producer taxed at 0.5 h/kg × 10⁴ kg = 5,000 h would rationally spend 40 h on a cut. If producers bought a cut whenever the saving exceeds its price, almost every producer above a few hundred kg a year would instrument and the share paying more than 1.5× would fall toward zero. **The result measures the cost of a budget cap, not of instrument prices alone.** The sensitivity row for price shows this: at 4 h per cut, 21% still pay more than 1.5×, but only because of the cap.
2. **The tax lands on the buyer's ledger, not the producer's.** A producer's incentive to instrument is indirect. Nothing here models how a buyer's refusal to take a heavy-reading good reaches the producer, and §4.8's offset (helping someone join is credited work the network bears) is not modelled at all. **Whether the offset is enough is not tested.**
3. **Exit steps are uniform on 1..n and step costs are lognormal, both invented.** The shape of the spread depends on where real co-products leave a real chain. The refinery and steer chains in `chain-resolution/` are real or illustrative single cases, not a population. No real producer-by-producer instrumentation data was used. The "mean rises with ln(n)" result is the harmonic-number effect of uniform exits and would vanish if goods left at a fixed fraction of the chain cost.
4. **A passage claim is taken as true.** A producer claiming a false early exit would lower its figure. That is the open verification question Foundations §3.4a already lists, and not measured here.
5. **Scale enters only through the cut budget.** Real scale also brings multi-site plants, shared instruments across a trade, and contract measurement services. A co-operative or a measurement service that sells readings would flatten the spread, and none is modelled.
6. **The good is one of m co-products, so a plant-wide cut is shared.** Cut cost is charged per cut with no sharing across the products it helps. Under §4.3 the setup price lands on the asset anyway.
7. **Not run:** more than one good per plant at a time, correlated step costs, and real prices for instruments.

## 6. Command and seed

```bash
python 06-simulation/resolution-tax/resolution_tax.py          # full run, then 7 self-tests
python 06-simulation/resolution-tax/resolution_tax.py --test   # self-tests only
```

Seed `20261019`, fixed in the file. Full run takes under a minute on the author's machine; it writes `run_output.txt` only if redirected.
