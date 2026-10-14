# ceiling-challenge — change log

Newest first.

## 2026-10-14 — first run, by the nightly simulation agent

- **Created.** Answers `sr-20260901-construct-a-challenge-that-pushes-max-claime` (SB-01).
- **Run 2** (the result): floor credited as a rule over the evaluated span; both statistics `max ÷ F` and `max ÷ min` reported; 13 self-tests, all passing. Transcript `RUN.txt`.
- **Run 1** (archived, `archive/RUN-1_floor-not-extended-over-span.txt`): the conforming evaluator extended the denominator over pre-birth credit without extending the floor. The random adversary pushed `max ÷ min` to 3.94 at `F` = 10 by lowering its own rate below `F`. Self-test 1 also failed because it was written over `max ÷ F` while the code computed `max ÷ min`. Both faults are recorded in `RESULTS.md` under the declared outcomes, and outcome O2's level was re-declared for the floor-inclusive form before run 2.
