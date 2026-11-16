# Declared before running (2026-11-15)

Request `sr-20261111-lost-crop-at-the-german-method-same-populati`. Written before `german_lost_crop.py` was run and before `fruitveg_share.py` returned.

**Model in one paragraph.** Same population, wants, age pyramid, services, essentials and gate as `german-prime-sweep/german_prime_sweep.py` (German method 0.836, capacity 101.7% of wants, N 200,000, F = 2, 10, 14, E = 437.2 and 462.3 h). The lost line is fresh fruit and vegetables (EXIOBASE product 4). Its share of one lifestyle unit is `g`, measured by `fruitveg_share.py`. The line's baseline capacity is 101.7% of its demand; it loses 50%, so its supply is 0.5 x 1.017 = 50.85% of its demand. Every other line stays at 101.7%. Surplus in another line cannot make fruit.

| # | Statement | Kind | Could it fail? |
|---|---|---|---|
| 1 | The line's shortfall is **49.15% of the line's demand** (1 - 0.5 x 1.017). | Level | Only if the code mis-sets capacity. Arithmetic of the input, so it is a check on the code, not a finding. |
| 2 | **g is between 0.5% and 2.5%** of one lifestyle unit (US fresh produce is about 7 to 18 h of 1,398 h). | Level, on the measurement | Yes. If g comes back above 2.5%, this fails. |
| 3 | **Aggregate capacity after the loss stays above total wants, so there is no clearing rho below 4.0, at every F, both E, every age seed.** The loss falls below that line only if g exceeds g* = 2 x (1 - U4 / (1.017 x W)), where U4 is admitted units at rho 4.0 and W is total wants. I expect g* near 3.3%. | Level (the size of g against g*) | Yes. It fails if g > g*. |
| 4 | **Under the essentials-first rule (food is inside E, ungated), the line is admitted in full at rho = 0.** No rho changes the line's supply or its demand. | Level | Yes. If any request in the line exceeded E the line would be cut at rho = 0. |
| 5 | **Pro rata: 100% of people get less than their want of the line** (everyone gets 50.85% of it). | Level | No. Arithmetic of "pro rata". Reported, not counted as a finding. |
| 6 | **Smallest wants first: between 25% and 40% of people get less than their want of the line.** My estimate is about 32% (lognormal sigma 0.45: the smallest 68% of people hold 50.85% of total wants). | Level | Yes. |
| 7 | If the line were treated as gated non-essential (E = 0), a clearing rho for the line alone exists, and reaching it cuts **at least 10 times more** units elsewhere than the line's own shortfall. | Ratio | Yes. It fails if the cut elsewhere is under 10x the line shortfall. |
| 8 | The declared claim in the request ("no clearing rho below 4.0, because the lost line is a small share of output") **holds**. | Verdict | Yes. Outcome 3 failing falsifies it. |

If outcome 3 fails, the report says "a clearing rho exists" and gives it. The request's own prediction is not protected.
