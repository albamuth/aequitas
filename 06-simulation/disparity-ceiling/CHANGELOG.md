# Disparity ceiling — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — moved into its own folder. No behaviour changed.

`disparity_ceiling_sim.py`, `rho_sweep.py`, their write-ups and their five figures moved from the flat `06-simulation/` directory into `06-simulation/disparity-ceiling/`.

**Why the two sims share a folder:** `rho_sweep.py` imports `disparity_ceiling_sim` and calibrates the same model's absolute level. Splitting them would have created a cross-folder import for no gain.

**No code was edited.** Two scripts elsewhere import from this folder and were pointed at it: [`../statera/statera.py`](../statera/statera.py) and [`../audits/audits_inert/generate_bonus.py`](../audits/audits_inert/generate_bonus.py).

**Verified after the move:** both `--test` runs pass — five checks each.

---

### 2026-08-22 — condition 5 added, correcting condition 4

**Condition 4 was wrong.** It claimed that on the consumption axis IC-7 already capped multi-network accrual. IC-7 caps hours **per account per network**. Multi-network accounts are legitimate, and self-care credit has no physical anchor — produced goods have one custody chain each, but proof of life needs no output.

A **fifth condition** was added: cross-network uniqueness attestation. The headline now says **24/F per network**.

**The first fix was itself re-framed the same day.** It was written as `k × 24/F`, which is arithmetic over two ledgers. The author's correction: two networks counting the same person are counting the same thing, and cannot be compatible unless they reach the same ledger for that person. So a compatible pair is one ledger seen from two places, the floor is credited once, and there is nothing to sum. An incompatible pair does not trade, leaving a coverage gap rather than a breached bound.

The same correction went into Foundations §7.5 and §10.

---

### 2026-08-17 — the ρ sweep added

[`rho_sweep.py`](rho_sweep.py) and [`RHO_SWEEP.md`](RHO_SWEEP.md). The ceiling is ρ-independent; this asks about the *absolute* level. Clearing rate ρ\* ≈ 1.20, median at 0.92× of a full lifestyle, 35% held below their wants.

Calibrated against the median-lifestyle anchor of about 1,380 hours per year — see [`../median-lifestyle/`](../median-lifestyle/) — and against the cross-country efficiency finding in [`../median-lifestyle/Q6.md`](../median-lifestyle/Q6.md).

**Stated limit, in the script's own words: static one-period clearing, no dynamics.** That limit is what the Statera kernel was built to remove.

---

### 2026-08-14 — built and stress-tested

[`disparity_ceiling_sim.py`](disparity_ceiling_sim.py) and [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md), 200,000 agents, four claims, five self-tests, four figures. Stress-tested the same day and passed.

Upgraded the wiki page [`../../01-wiki/disparity-ceiling.md`](../../01-wiki/disparity-ceiling.md) from a hypothesis to a stated, simulated, stress-tested conditional result.
