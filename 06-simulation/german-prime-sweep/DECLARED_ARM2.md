# Outcomes declared before the first arm-2 run (2026-11-12)

Request `sr-20261110-second-arm-of-sr-20261109-prime-rate-sweep-a`. Arm 2 = demand 1,048 h/person/yr (Germany's middle fifth), capacity base = 100% of wants. Everything else as arm 1.

Predicted by pure scaling: rho should scale with kappa, so arm2/arm1 = 703.6 / 809.2 = 0.87 if nothing else changed. Two things push it lower: E is not scaled (essentials are a bigger share of a smaller request), and capacity base 1.000 instead of 1.017 makes each shock step 1.7% deeper relative to wants.

| # | Statement | Kind | Fails if |
|---|---|---|---|
| 1 | Arm-1 reproduction: the new code, run with arm-1 inputs, gives rho 0.221 +/- 0.005 at F=10, -20%, E=437.2 (age seed 11) | LEVEL (against arm 1's published 0.221) | outside 0.216-0.226 |
| 2 | At +20%, +10%, 0: no clearing rho at any F ("gate never binds below rho = 4.0"). This is set by the input (capacity = demand), not a finding | LEVEL of the cell | any seed returns a rho |
| 3 | At F=10, -20%, E=437.2: arm-2 rho lies in [0.10, 0.30] | LEVEL | outside |
| 4 | At F=10, -20%, E=437.2: ratio arm2/arm1 lies in [0.55, 0.95] | LEVEL on the ratio | outside |
| 5 | Ratio arm2/arm1 is below 0.87 (the pure-scaling value) at F=10, -10%, -20% | CHANGE | at or above 0.87 |
| 6 | At F=10, E=437.2, -30%: "none, ungated part alone exceeds capacity" (arm 1 cleared 0.158 there) | LEVEL of the cell | a clearing rho appears |
| 7 | At F=10, -20%, E=437.2: share admitting nothing above E is higher than arm 1's 26.08% | CHANGE | at or below 26.08% |
| 8 | Year 2 at rho 1.2 (capacity restored) admits within 1% of the unshocked baseline year at rho 1.2 | CHANGE | differs by more than 1%. If rho 1.2 does not bind, this cannot fail and is reported as not evidence |

Choices made unattended (all stated in RESULTS_ARM2.md):
- Services removed = 412 x 0.836 = 344.4 h (the arm-1 US-method service hours, German-scaled). No German per-service hours exist in the repo's tables; this keeps arm 2 comparable to arm 1.
- kappa_before = 1,048 h/yr; kappa_after = 1,048 - 344.4 = 703.6 h/yr. s = 344.4 / 1,048 = 0.3286.
- E, essentials rule, floors, past rule, shocks, age seeds, baseline rho 1.2: unchanged from arm 1.
- Unit = one middle-fifth German lifestyle-year per person, all ages, applied to every person's want w exactly as arm 1 applied the 1,380 x 0.836 figure.
