# deletion-payoff

Sweeps the conforming band (F 1–14 h/day, ρ from the affordability floor to ρ\*(F)) and reports what a filer gains per year of declared span deleted: `d − ρ·F·365` of what they may still carry. Reuses `../stable-band` for ρ\*(F); changes nothing there.

- `python deletion_payoff.py --test` — 8 self-tests, each of which can fail
- `python deletion_payoff.py` — full sweep (about 1 minute)
- `python critical_cap.py` — the capacity at which the band's top edge reaches break-even
- Results: [`RESULTS.md`](RESULTS.md). Declared outcomes: [`DECLARED.md`](DECLARED.md).
