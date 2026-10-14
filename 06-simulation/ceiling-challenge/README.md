# ceiling-challenge — can anything push `max(claimed credit) ÷ F` above `24 ÷ F` without a record over 24 hours?

> **Version:** 0.1
> **Date:** 2026-10-14

> **Status:** ✅ Run 2026-10-14 by the nightly simulation agent (cloud session). Answers `sr-20260901-construct-a-challenge-that-pushes-max-claime`, the open half of the ceiling-rubric finding, written up for outsiders as [`../sim-briefs/SB-01_ceiling-challenge.md`](../sim-briefs/SB-01_ceiling-challenge.md). Bears on Foundations **§5.5.5** (the five conditions) and **§4.4** (the earliest-evidence span rule).
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`ceiling_challenge.py`](ceiling_challenge.py) · **First run, archived:** [`archive/RUN-1_floor-not-extended-over-span.txt`](archive/RUN-1_floor-not-extended-over-span.txt)

## What it answers

> *"Construct a challenge that pushes max(claimed credit)/F UPWARD without breaching the 24-hour cap. If none exists, state why the space is empty."*

**The arithmetic space is empty, and the proof is one line:** an account's credit per day lived is a mean of per-day values each in `[F, 24]`, so it lies in `[F, 24]` and the ratio cannot exceed `24 ÷ F`. **The evaluation space is not empty.** That proof rests on four premises an implementation has to *evaluate*, and this folder builds one construction per premise, with no record in any of them claiming more than 24 hours for one day:

| Premise | What an implementation must do | The construction that breaks it | What it reaches at `F` = 10 |
|---|---|---|---:|
| **P2 cap** | Check the 24-hour cap on the **sum of all records** an account holds for one day, not on each record alone | `k` backdated filings on the same days, each at `24 − F` h/day | `1 + k(24−F)/F` — **3.80** at `k` = 2, unbounded in `k` |
| **P3 span** | Count days lived as the span **extended to cover every dated credit** (Foundations §4.4, condition 3) | 10 years of 24 h/day credit dated before a 40-year declared birth | **3.00** |
| **P4 unit** | Measure days lived as **elapsed time ÷ 24 h**, not local calendar days | A wall worker through 80 DST fall-back days | **2.4003**, an excess of 1.1 × 10⁻⁴ |
| **P1 floor** | Credit the **published duration** on every day in the evaluated span, never measured self-care | A 6-hour sleeper under a 10-hour list | **3.00** on `max ÷ min`; `max ÷ F` unmoved |
| **P4 domain** | Take the minimum over **human subscribers** only | An organisation account in the domain | `max ÷ min` = **∞**; `max ÷ F` unmoved |

**Restore the one broken setting and every row returns to exactly `24 ÷ F`**, or is rejected by IC-7. Under the conforming evaluator a random adversary filing up to eight arbitrary records a trial, backdated, overlapping, pre-birth, with a shortened declared span, never exceeded `24 ÷ F` in 20,000 trials at four floors.

**Two statistics were being called by one name.** The request's `max ÷ F` has the network constant in the denominator and can only be moved by raising a maximum. Foundations §5.5.5's `max ÷ min` can also be moved by lowering a minimum. SB-01's self-tests 1 and 2 are written over the first; its attack (c) reaches only the second. The code reports both.

## Run it

```bash
python ceiling_challenge.py --test     # 13 self-tests, each able to fail
python ceiling_challenge.py            # the run, seed 20261014, 5,000 adversary trials per floor
python ceiling_challenge.py --seed 1 --trials 2000
```

**Standard library only.** The run takes about four seconds.

## The 13 self-tests

| # | Test | What it protects |
|---|---|---|
| 1 | Every account at 24 h/day → `max ÷ F` = `24 ÷ F` exactly and `max ÷ min` = 1.0 | SB-01 §8.1, and that the two statistics differ |
| 2 | Every account at `F` → both exactly 1.0 | SB-01 §8.2 |
| 3 | Inserting a floor-only account leaves both unchanged | SB-01 §8.3, a control |
| 4 | Removing the unique highest account lowers both | SB-01 §8.4 |
| 5 | The account-day evaluator catches two overlapping 18-hour records (36 h) | the conforming cap fires |
| 6 | …and passes two adjacent 24-hour records | no false positive |
| 7 | The per-record evaluator passes the same overlapping pair | the gap is real |
| 8 | The span rule extends **both** the denominator **and** the floor over pre-birth credit | the fault the first run found |
| 9 | Every conforming rate lies in `[F, its own worst day]` | the statistic is a mean |
| 10 | Local-calendar denominator reads above 24; elapsed reads exactly 24 | the unit artefact |
| 11 | An organisation in the domain makes `max ÷ min` infinite and leaves `max ÷ F` alone | the domain trap |
| 12 | The sweep evaluator equals a brute-force per-day sum on 200 random block sets | **protects outcome O1** |
| 13 | A 6-hour sleeper under measured self-care gives `max ÷ min` = 3.000 | reproduces Foundations §5.5.5 condition 1's own figure |

## What the first run found, and why it is kept

The first run's conforming evaluator extended the denominator over pre-birth credit **without extending the floor over the same days**. The random adversary found it at once: a tiny pre-birth filing lengthened the attacker's own span, their rate fell below `F`, and `max ÷ min` read 3.94 at `F` = 10 in 522 accepted trials. **That is premise P1 broken by the evaluator rather than by the filer**, and it is the shape SB-01 attack (c) predicted. The transcript is in `archive/`, the fix is self-test 8, and the outcome for P2 was re-declared for the floor-inclusive form before the second run. Both declarations are in `RESULTS.md`.

## Relation to the neighbouring projects

- [`../ceiling-rubric/`](../ceiling-rubric/README.md) scored the statistic as a detector and found it one-sided. That folder is **void as evidence** and its code is frozen; nothing here imports it.
- [`../audits/arithmetic_audits.py`](../audits/arithmetic_audits.py) implements IC-7 as `check_ic7_agent_time`, which sums every role of an account inside a sliding 24-hour window. **That is the conforming P2 evaluator.** The project's own reference check already aggregates; the gap exists only for an implementation that checks records one at a time.
- [`../sim-briefs/SB-01_ceiling-challenge.md`](../sim-briefs/SB-01_ceiling-challenge.md) is the outsider brief for this question. Its prior was *"empty for attack (b), open for attack (a), and an implementation question rather than an arithmetic one."* This run agrees on all three, and adds that attack (c) is reachable through the span rule and through the domain.
