# german-prime-sweep

**Arm 1.** Request `sr-20261109-prime-rate-sweep-at-the-german-method-on-the`. Clearing rho of the stock gate `D <= rho*(C+P)` at the German method, capacity shocks +20% to -40%, F = 2, 10, 14, essentials ungated, services off the receiver, joiner pasts.

Extends `../stock-gate-clearing/` (same population, wants, ages, Kernel).

- Tests: `python german_prime_sweep.py --test` (6 self-tests)
- Run: `python german_prime_sweep.py > RESULTS_RAW.txt` (about 2 min)
- Declared outcomes: `DECLARED.md`. Results: `RESULTS.md`. Raw numbers: `RESULTS_RAW.txt`.

**Arm 2.** Request `sr-20261110-second-arm-of-sr-20261109-prime-rate-sweep-a`. Same cells with demand at Germany's middle fifth (1,048 h per person per year) and capacity base 100% of wants. Re-runs arm 1 inside the script and prints both rho values with their ratio.

- Tests: `python german_arm2.py --test` (6 self-tests, one re-checks arm 1's published 0.221)
- Run: `python german_arm2.py --raw` (a few minutes; writes `RESULTS_ARM2_RAW.txt`)
- Declared outcomes: `DECLARED_ARM2.md`. Results: `RESULTS_ARM2.md`.
