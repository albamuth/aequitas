# Can anything push `max(claimed credit) ÷ F` above `24 ÷ F` without a record over 24 hours? — results

> **Version:** 0.1
> **Date:** 2026-10-14

> **Run: 2026-10-14, 03:14 UTC**, by the nightly simulation agent in a cloud session. Answers `sr-20260901-construct-a-challenge-that-pushes-max-claime`, filed 2026-09-01 from `obj-20260901-ceiling-statistic-one-sided`; the outsider brief is [`../sim-briefs/SB-01_ceiling-challenge.md`](../sim-briefs/SB-01_ceiling-challenge.md).
> **Code:** [`ceiling_challenge.py`](ceiling_challenge.py) · **Transcript:** [`RUN.txt`](RUN.txt) · **13 self-tests, each able to fail, all pass.**

---

## 1. The question

> *"Construct a challenge that pushes max(claimed credit)/F UPWARD without breaching the 24-hour cap. If none exists, state why the space is empty."*

**Why it was asked:** the ceiling-rubric run declared six challenges and none pushed the maximum up. That was asserted rather than proved. @cairn-lineage was invited to build one at c35463.

**The object.** `r_i = C(i) ÷ days lived(i)`, one account's credit per day lived. The request's statistic is **`S_F = max_i r_i ÷ F`**. Foundations §5.5.5 states the bound over **`S_mm = max_i r_i ÷ min_i r_i`**. Both are claimed `≤ 24 ÷ F`. They coincide whenever somebody lives at the floor, and only the second can be moved by lowering a minimum.

---

## 2. Declared before running

**The arithmetic.** If every lived day `t` carries `F ≤ c(i,t) ≤ 24`, then `r_i` is a mean of values in `[F, 24]`, so `F ≤ r_i ≤ 24` and both statistics are `≤ 24 ÷ F`. That proof rests on four premises an implementation evaluates: **P1** the floor is credited on every day in the evaluated span; **P2** the cap is checked on the *sum* of all records per account-day; **P3** every dated credit lies inside days lived; **P4** days lived is elapsed time ÷ 24 h, over human accounts only. **Prediction: no arithmetic construction exceeds `24 ÷ F`; every construction that does breaks exactly one premise.**

| | Outcome, as declared | Kind | Would mean |
|---|---|---|---|
| **O1** | Under the conforming evaluator, the wall construction and ≥ 20,000 random adversarial filings return **`S ≤ 24 ÷ F` to within 10⁻⁹** at `F` ∈ {2, 6, 10, 14}, both statistics; the wall reaches `24 ÷ F` exactly (**2.400 at `F` = 10**) | **level** | A result above `24 ÷ F` refutes §5.5.5 as written, *or* exposes a hole in the evaluator — self-test 12 tells the two apart |
| **O2** | Under a per-record cap, `k` overlapping backdated filings reach **`24k ÷ F` exactly: 4.800 at `k` = 2, `F` = 10**, linear in `k` | **level** | *(As first declared — see the revision below)* |
| **O2′** | **Re-declared before run 2**, after the model made the floor a rule: `k` overlapping work records each at `24 − F` beside the floor reach **`1 + k(24 − F) ÷ F`: 3.800 at `k` = 2, `F` = 10**, linear in `k`, each record alone at or under 24 | **level** | The cap only bounds the statistic if it is evaluated per account-day |
| **O3** | A 40-year declared span with 10 years of 24 h/day credit dated before it reaches **`S` = 3.000** under the declared-span denominator and **2.400** once the span is extended (§4.4 condition 3) | **level** | The bound depends on the span rule, which §5.5.5's five conditions do not name |
| **O4** | A local-calendar denominator over 80 DST fall-back days gives an excess **below 1.2 × 10⁻⁴ relative** (`S` ≈ 2.4003 at `F` = 10); elapsed ÷ 24 h returns exactly 2.400 | **level** | Unit-incommensurable (brief §4c): restate the unit and the check survives |
| **O5** | Measured self-care in place of the published duration: a 6-hour sleeper under the §5.5.1 list gives **`S_mm` = 3.000**, matching the figure Foundations §5.5.5 condition 1 states | **level** | Reproduces the document's own worked number |
| **O6** | An organisation account in the domain sends `S_mm` to **∞** and leaves `S_F` unmoved | level | The statistic's domain must be stated |
| **O7** | Deleting the top account under conforming rules **lowers** `S` (SB-01 §8.4, a control) | change | — |

**Revision, recorded rather than hidden.** Run 1's conforming evaluator extended the denominator over pre-birth credit without extending the floor over the same days, and its O2 construction carried no floor. Run 1 therefore **failed O1** (`S_mm` = 3.94 at `F` = 10 in 522 accepted trials: the attacker lowered its *own* rate below `F`), and self-test 1 failed because it was written over `S_F` while the code computed `S_mm`. Both were the model's faults, not the bound's. The transcript is kept in [`archive/RUN-1_floor-not-extended-over-span.txt`](archive/RUN-1_floor-not-extended-over-span.txt). O2 was re-declared as O2′ **before** run 2; the other outcomes were not changed.

---

## 3. What came back

**All seven outcomes landed as declared (O2 in its re-declared form O2′).** Every figure below is at `F` = 10 h/day unless a floor is shown. Lives are 80 years (29,200 days) unless shown. Every ratio has its absolute figures beside it.

### O1 — the conforming evaluator: nothing crosses `24 ÷ F`

Account-day IC-7, span extended with the floor following, elapsed denominator, human domain. The adversary files 1–8 random records per trial, hours drawn from {uniform(0, 24), 24, 24 − F}, spans reaching up to 20 years before birth, declared span shortened on half the trials; a trial is accepted when IC-7 passes.

| `F` | `24 ÷ F` | Wall construction `S_F` | Best accepted `S_F` = `S_mm`, seed 20261014 (5,000 trials) | accepted | Best, seed 1 (2,000 trials) | accepted | min rate, h/day | max rate, h/day |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 12.0000 | **12.000000** | 11.964530 | 622 | 11.943770 | 252 | 2.0000 | 24.0000 |
| 6 | 4.0000 | **4.000000** | 3.971093 | 510 | 3.976016 | 219 | 6.0000 | 24.0000 |
| **10** | **2.4000** | **2.400000** | **2.397151** | 448 | 2.367070 | 171 | **10.0000** | **24.0000** |
| 14 | 1.7143 | **1.714286** | 1.708010 | 418 | 1.704199 | 156 | 14.0000 | 24.0000 |

**Every accepted construction, both statistics, `≤ 24 ÷ F`: true on both seeds.** The wall is deterministic (spread 0); the search's best is below the wall on every row because random filings rarely fill every day to 24. **O1 holds.**

### O2′ — premise P2 broken: the cap checked per record

`k` backdated work records on the same 29,200 days, each at `24 − F` = 14 h/day, beside the 10-hour floor. No record exceeds 24 h for any day.

| `k` | per-record IC-7 | account-day IC-7 | worst day, h | `S_F` | `1 + k(24−F)/F` | any record > 24 h? |
|--:|---|---|--:|--:|--:|---|
| 1 | passes | passes | 24.0 | 2.4000 | 2.4000 | no |
| **2** | **passes** | **fails** | **38.0** | **3.8000** | 3.8000 | **no** |
| 3 | passes | fails | 52.0 | 5.2000 | 5.2000 | no |
| 5 | passes | fails | 80.0 | 8.0000 | 8.0000 | no |

Random adversary under the per-record cap: best `S_F` = `S_mm` = **8.7717**, all 5,000 trials accepted. **O2′ holds, exactly.** The project's own IC-7 in `audits/arithmetic_audits.py` sums every role inside a sliding 24-hour window, so this gap does not exist against the reference check; it exists against an implementation that validates filings one at a time.

### O3 — premise P3 broken: the declared span as denominator

A filer declares 40 years (14,600 days), works at the wall through them, and files 10 further years (3,650 days) dated before the declared birth.

| pre-birth records at | denominator rule | IC-7 | worst day, h | max rate, h/day | `S_F` | any record > 24 h? |
|--:|---|---|--:|--:|--:|---|
| **24 h/day** | **declared span (14,600 d)** | passes | 24.0 | **30.000** | **3.0000** | **no** |
| 24 h/day | extended (18,250 d) | **fails** — the floor now covers those days too | 34.0 | *(rejected)* | *(rejected)* | no |
| 14 h/day | declared span | passes | 24.0 | 27.500 | 2.7500 | no |
| 14 h/day | extended (18,250 d) | passes | 24.0 | **24.000** | **2.4000** | no |

**O3 holds: 3.000 as declared, and 2.400 once the span follows the evidence.** This is the one construction that needs **no per-day IC-7 breach of any kind**; what stops it is §4.4 condition 3 (*back to the earliest date the evidence permits*, with the floor credited over the whole span), a rule in a different section from the bound.

### O4 — premise P4 (unit) broken: local calendar days

A wall worker through 80 years with one 25-hour fall-back day a year: 80 extra honest clock hours over 29,200 days.

| denominator | max rate, h/day | `S_F` | excess over 2.4 |
|---|--:|--:|--:|
| local calendar (29,200 d) | 24.002740 | 2.400274 | **+2.74 × 10⁻⁴, or +1.14 × 10⁻⁴ relative** |
| elapsed ÷ 24 h (29,203.33 d) | 24.000000 | 2.400000 | 0 |

**O4 holds.** Deterministic, spread 0. Unit-incommensurable, repaired by restating the unit.

### O5 — premise P1 broken: measured self-care

| sleeps | list `F` | min rate, h/day | `S_mm` | `S_F` |
|--:|--:|--:|--:|--:|
| 8.0 h | 10 | 10.000 | 2.4000 | 2.4000 |
| 7.0 h | 10 | 9.000 | 2.6667 | 2.4000 |
| **6.0 h** | **10** | **8.000** | **3.0000** | **2.4000** |
| 4.0 h | 10 | 6.000 | 4.0000 | 2.4000 |

**O5 holds: 3.000, the figure §5.5.5 condition 1 gives.** `S_F` does not move, which is the clearest demonstration that the two statistics are different objects.

### O6 — premise P4 (domain) broken

An organisation account (floor 0, credit 0, A3) in the domain: min rate **0.000**, `S_mm` = **∞**, `S_F` = 2.4000. Humans only: min rate 10.000, `S_mm` = 2.4000. **O6 holds.**

### O7 — control

200 random accounts capped at 12 h of work plus the wall: `S_F` 2.4000 with the wall, **2.1981** without it, delta −0.2019. **The control fires in the expected direction.**

### What the first run found

Run 1's evaluator broke P1 on its own: after a span extension the floor was not credited over the added days. The adversary found it in 522 of 5,000 accepted trials at `F` = 10 (`S_mm` = 3.937, min rate 6.09 h/day) and 627 at `F` = 2 (`S_mm` = 15.11). **That is the first of the four gaps to be found by search rather than by hand, and it was in this project's own code.** Self-test 8 now pins it.

---

## 4. What this does **not** show

1. **O1 is a proof restated as a search, and a search cannot refute a true theorem.** Its value is that it would have caught an evaluator that mis-states a premise — and in run 1 it did exactly that. It says nothing about whether any real implementation evaluates the premises correctly; that is a conformance question for each network.
2. **The constructions are over a daily-rate ledger, not an event log.** Records here are blocks of days at a constant hourly rate. A real log carries timed intervals, and the project's IC-7 (`check_ic7_agent_time`) runs a sliding 24-hour window over them. The sweep here is the calendar-day form of that check; it was not run against the audits module's own event schema, and sub-day placement (two 13-hour roles straddling midnight) is not exercised.
3. **The four premises are the ones this run could see.** SB-01 said *"finding one we did not list is the most valuable outcome"*, and run 1 did find one the first draft had not listed (the floor failing to follow the span). There is no argument here that the list of four is complete.
4. **The pledge budget is assumed equal to earned credit** (conformance row 9, §5.5.5 condition 5). The request is about *claimed credit*, so room `P` is out of scope here; an implementation that let room enlarge the budget would move `S` without touching anything this run measures.
5. **Nothing here says the bound matters.** That is §5.5.5's five conditions and the ceiling-rubric finding that the statistic reads no accounts. This run asks only whether it is a bound.
6. **The DST artefact is modelled, not measured.** One 25-hour day a year is a stand-in for whatever a local-calendar implementation would actually do with fall-back days, leap seconds, and travel across zones; the figure 1.1 × 10⁻⁴ is the size of the stand-in.

---

## 5. The exact command and the seed

```bash
cd 06-simulation/ceiling-challenge
python3 ceiling_challenge.py --test                  # 13 of 13 pass
python3 ceiling_challenge.py                         # seed 20261014, 5,000 adversary trials per floor  -> RUN.txt
python3 ceiling_challenge.py --seed 1 --trials 2000  # the second-seed column in O1
```

Python 3.11 or later, standard library only. Run time about 4 s. The deterministic constructions (wall, overlap, pre-birth, DST, measured floor, organisation) do not depend on the seed; the population behind them does, and does not change any figure above.

---

## 6. What follows

| | |
|---|---|
| **For the request** | **Answered.** The space is empty for the arithmetic, by the one-line mean argument. It is non-empty for the evaluation, in exactly four places, and the cost of each is measured above. **No construction reaches `S > 24 ÷ F` with the four premises evaluated as Foundations states them.** |
| **For §5.5.5** | Its five conditions name `F` as convention (P1), fraud under IC-7 (P2, loosely), one network's books, and the pledge budget. **They do not name the span rule (P3) or the denominator's unit and domain (P4).** O3 is the construction that needs no cap breach at all, and the rule that stops it lives in §4.4. A sixth condition, or a cross-reference, is the author's call. **Nothing is edited here.** |
| **For SB-01** | The brief's prior — *empty for (b), open for (a), an implementation question* — stands. Its self-tests 1 and 2 are over `max ÷ F`; its §3 statistic is `max ÷ min`. **The brief should say which it means**, because attack (c) reaches only the second. |
| **Owed** | The audits module's sliding-window IC-7 against the overlapping-filing and pre-birth constructions in its own event schema (point 2 above). |
