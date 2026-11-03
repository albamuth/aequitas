# attested-share

Answers request `sr-20260913-over-a-simulated-joining-population-what-sha`. For each person, what share of the days they have lived are **attested** (rebuilt before they joined, from their own evidence) rather than **observed** on the network's calendar? How does that share fall as a cohort ages inside the network?

- Code: `attested_share.py` (numpy only, about 20 s).
- Self-tests: `python attested_share.py --test` (13 checks, each able to fail).
- Full run: `python attested_share.py > RUN.txt` (seed 20261103).
- Declared outcomes, written before the first run: `DECLARED.md`.
- Results: `RESULTS.md`. Run 1 transcript, kept because it had a bug: `RUN-1_inverted-init-mask.txt`.
