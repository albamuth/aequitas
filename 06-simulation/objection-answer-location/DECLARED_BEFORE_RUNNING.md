# Declared before running — 2026-10-22

Written before `answer_location.py` was run for the first time. The hand classes (`hand` in `findings.py`) were also fixed before the run.

| # | Kind | Outcome declared | What it would mean |
|---|---|---|---|
| D1 | **Level** | Of the findings that had a pre-existing answer and can be tested, the share classed (c) at K = 10 lies in **10% to 50%** | Inside: a reader who only searches with the critic's words misses a real share of answers, but not most. Below 10% (zero or one row): the claim "a whole read finds what a search cannot" has no support in this register. Above 50%: search fails more often than it works |
| D2 | **Level** | Findings with any pre-existing answer, over all outside findings in the register, lie between **40% and 70%** | The register's own 2026-08-24 table gave 6 of 10. A figure far outside this range would mean that table was not typical |
| D3 | Level | Hand class and mechanical class agree on **at least 70%** of tested rows at K = 10 | Below 70%: the hand labels cannot be trusted and only the mechanical counts are reported |
| D4 | Change | Moving K from 5 to 10 to 25 changes the class of **at most 3** tested rows | More than 3: the (b)/(c) split depends on a threshold I chose, and the counts are reported as a range, not a point |
| D5 | Control | A random paragraph clears the (b) bar in **under 5%** of draws | At or above 5%: the (b) bar is too easy and (b) counts are inflated |

**Could each have failed?** Yes. D1, D2, D3 and D5 state intervals the run can fall outside. D4 can be exceeded by the table. None of them is set by an input I supply after seeing the numbers.

**Known weakness stated now:** the checker (me) chose the corpus, the table rows, the K values and the "shares at least 2 query terms" rule. That is why D4 and D5 exist.
