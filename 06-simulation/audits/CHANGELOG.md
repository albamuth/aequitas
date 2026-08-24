# Arithmetic audits — change history

> Newest entry first. Read this only when tracing **when and why** something changed. For what the project is, see [`README.md`](README.md); for what it found, see [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — N3, N4 and N5 fixed; IC-3 now checks every reservoir

The three latent defects found while writing `audits_inert/` are closed. No verdict on the shipped fixture changes; all twelve checks still pass on the clean log and all twelve violations are still caught.

- **N3 — `computed_theta` unit mismatch.** The mass split divided *every* parcel output by a denominator that summed only the `kg` outputs. It now takes the numerator from the same `kg`-filtered list, so an output carried in joules takes no share of the mass dimension instead of a wrong one. `constraints.md` states that restriction, because the stated mathematics changed with the code.
- **N4 — IC-3 checked only the first reservoir.** `Parcel.origin_reservoir: str | None` became `origin_reservoirs: tuple[str, ...]`, holding every non-parcel input of the creating event, and IC-3 requires all of them to be in the registry. An event drawing on two reservoirs with the second unregistered used to pass; it now fails. The unreachable `has_reservoir_in and not parent_parcels` branch in `traces` was deleted. `constraints.md` rule 4 for IC-3 was reworded from *that reservoir* to *every reservoir input*. `fixture.json` renames the parcel key to `origin_reservoirs` and carries a list.
- **N5 — comment arithmetic.** `violate_ic1` said "+0.5 kg" for a change of +1.0 kg. Comment only.

`IMPLEMENTATION_NOTES` in `generate.py` drops N3, N4 and N5. The remaining ids were **not** renumbered, so N1, N2 and N6–N9 still mean what they meant.

**Three stale paths fixed in passing.** The folder move fixed the *import* lines in `audits_inert/` but not the lines that hash the source files, so both generators crashed before writing anything:

- `generate.py` hashed `SIMDIR / "recursion_convergence.py"`; it now hashes `../allocation-engine/recursion_convergence.py`.
- `generate_bonus.py` hashed `SIMDIR / "disparity_ceiling_sim.py"` and `SIMDIR / "residual_unravelling.py"`; those are now `disparity-ceiling/` and `residual-unravelling/`.

The run command in `generate.py`'s docstring was updated to `06-simulation/audits/audits_inert/generate.py`.

**Verified:** `python arithmetic_audits.py --test` passes. `python audits_inert/generate.py` prints *injections whose target check did NOT fire: none* and *stated-arithmetic vs Python disagreements: none*. A hand-built log with a second, unregistered reservoir on E1 now returns IC-3 FAIL, and a joule-carried extra output on E3 leaves the mass split at 0.7 / 0.3 summing to 1.

---

### 2026-08-24 — moved into its own folder; change history pulled out of the code

`06-simulation/` was a flat directory of about 94 files and is now one folder per project. `arithmetic_audits.py` and `AUDITS.md` moved to `06-simulation/audits/`, and `audits_inert/` moved with them, unchanged.

**Two path fixes, no behaviour change:**

- `arithmetic_audits.py` imports the solver from `recursion_convergence`, which now lives in `../allocation-engine/`. Four lines were added to put that folder on the import path.
- `audits_inert/generate_bonus.py` imports `disparity_ceiling_sim` and `residual_unravelling`, which now live in `../../disparity-ceiling/` and `../../residual-unravelling/`. Its existing path line was pointed at those two folders. Nothing else in `audits_inert/` was touched.

**The module docstring lost its change log.** It opened with *"Reworked to EventLog v0.4 / Foundations v0.7 (the credit-realization session)"* followed by five bullets. The bullets stayed, because they explain how the model works and a reader of the code needs them. The framing that made them a change record moved here, as the 2026-08-07 entry below.

**Verified after the move:** `python arithmetic_audits.py --test` — twelve checks pass on the clean log, twelve violations caught, extent block prints.

---

### 2026-08-24 — `audits_inert/` added

The audits published as data rather than as a program. `fixture.json` (the scenario), `worked_arithmetic.json` (every quantity each constraint sums, on the clean log), `expected_verdicts.json` and `expected_verdicts.md` (the clean verdict plus all twelve injected logs), `constraints.md` (the constraints in prose), and two bonus fixtures carrying the disparity-ceiling and residual-unravelling results.

**Why:** a critic on [1f916.ai](https://1f916.ai/) argued that shipping executable-only relocates trust to the repository — to check a claim you must first run a stranger's code. This removes that step.

---

### 2026-08-22 — the extent block

`print_extent_block()` added, and the self-tests now assert it. Every verdict emits `(result, domain, extent, closure-basis)`.

For the shipped scenario the closure basis is **NONE on every axis**, two origin termini are declared un-re-derivable, and **five blind spots are named** — the first being that a process recorded nowhere is invisible to every check here.

**Why:** the specification had over-claimed. IC-1 and IC-2 catch an *under-declared* emission on a *recorded* event. A process recorded nowhere is a coverage question and always was. The claim now travels with its own caveat.

---

### 2026-08-07 — C11 closed. All twelve constraints runnable, all twelve violations caught.

The original build, and the session that reworked it to the then-current event-log and Foundations versions. Five modelling rules were settled here and still govern the fixture:

1. **Survival is entity-record continuity**, not a "same identifier on both sides of one event" match. Parcels are persistent records with a lifecycle.
2. **The co-product split is not stored on the event.** It is computed at projection time, from the event's own measured output masses, with the published process-energetics model only as a fallback for a dimension the event did not measure. There is no field for an allocation fraction, so a self-serving split has nowhere to live — which is why the projection-side violations live in the energetics model, the only place a chosen number exists.
3. **Genesis is an origin terminus, not a reservoir.** A pre-Aequitas object enters at an estimated creation cost with no reservoir input and no parcel ancestry, and its estimator is credited.
4. **A pledge is a permanent, non-revocable grant of debit-room**, drawn one-for-one from the pledger's lifetime pledging budget — not a promise to buy. It moves no debit by itself and cannot be withdrawn. An undischarged pledge that reaches expiry burns. When the summoned work yields a held object, that object's debit follows possession to whoever accepts it, not necessarily the pledger.
5. **Credit realises on verification of the output.** For a good, the hand-off is the verification. A deployment marker starts holding time.

Journal entry: [`../../03-journal/2026-08-07.md`](../../03-journal/2026-08-07.md).
