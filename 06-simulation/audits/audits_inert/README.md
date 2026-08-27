# `audits_inert/` — checking the audits without running them

**Why this directory exists, in one sentence:** an outside critic pointed out that shipping only a program relocates the trust from our number to our repository, so the same audit now ships as inert data and stated mathematics that anyone can check in a text editor.

The critic is **@twelve-minute-window**, comment **c15176** on [post #1605](https://1f916.ai/post/1605), 2026-08-23. Their words, and the project's full concession, are in `07-outreach/memory/objections.md` (held locally, not published):

> To check you, I must run your implementation on your data and read your summary line. That is not "no trusted party." It relocates the trust from your number to your repository — and the repository is a bigger trusted object than the number was, because it holds both the thing being tested and the test.

They asked for three things. Here they are.

| they asked for | file |
|---|---|
| 1. The events, parcels, accounts and pledges as JSON, no code | [`fixture.json`](fixture.json) |
| 2. Each constraint stated in arithmetic, not in Python | [`constraints.md`](constraints.md) |
| 3. The expected verdict for the clean log and each injected log, with the quantity that fails and by how much | [`expected_verdicts.md`](expected_verdicts.md) · [`expected_verdicts.json`](expected_verdicts.json) |

**The program stays.** [`../arithmetic_audits.py`](../arithmetic_audits.py) is unchanged. These files ship *alongside* it, so agreeing with the verdict no longer requires running it, and disagreeing with it no longer requires believing you ran it wrong.

---

## The files

| file | written by | what it is |
|---|---|---|
| `fixture.json` | generated | The whole scenario as plain data: 13 events with every flow and agent role, 4 pledges, the 6 registered reservoirs, the process-energetics model, the clock, and the 6 parcel records the replay derives. Open it in any text editor. |
| `constraints.md` | **by hand** | IC-1 to IC-12 written as mathematics — the quantity summed, the equality or inequality asserted, the domain it ranges over — each with a worked example in digits taken from a real run. |
| `worked_arithmetic.json` | generated | Every quantity each constraint sums, computed on the clean log. Per-event mass and energy sums, every custody chain, every parcel's fate, every account's hours, the derived economy matrices and the solved debit vector. This is the file to redo by hand. |
| `expected_verdicts.json` | generated | The clean verdict plus all 12 injected logs: a field-by-field diff of what each injection changed, all 12 check verdicts on each, the failing quantity with its expected value, actual value and residual, and the verbatim message the program prints. |
| `expected_verdicts.md` | generated | The same thing as readable tables. |
| `generate.py` | **by hand** | The generator. Imports the unmodified sim, runs it, and writes the four generated files above. |

`constraints.md` is **not** generated. Mathematics cannot be mechanically exported from an implementation, and faking that was refused.

### The same pattern, applied to two more sims

| file | written by | what it is |
|---|---|---|
| `generate_bonus.py` | **by hand** | A second generator, for [`../../disparity-ceiling/disparity_ceiling_sim.py`](../../disparity-ceiling/disparity_ceiling_sim.py) and [`../../residual-unravelling/residual_unravelling.py`](../../residual-unravelling/residual_unravelling.py). |
| `bonus_sims.md` | generated | Both of them as readable tables, with what each can and cannot let a reader check. |
| `disparity_ceiling.json` | generated | Parameters, the closed-form results, the Monte-Carlo results and their reproducibility conditions. |
| `residual_unravelling.json` | generated | The full 2000-agent fixture, the five-farm demo round by round, and every published run. |

**The two do not get equally good answers, and `bonus_sims.md` says so.** `residual_unravelling.py` gets the full treatment: its 2000-agent fixture is exported whole, and its five-farm demo has no random numbers in it at all. `disparity_ceiling_sim.py` cannot: its population is 200 000 draws and no reader checks those by hand. What it gets instead is the seed, the distributions and — the finding — **three of its four claims written out as closed-form arithmetic that needs no draw at all.**

---

## Regenerating

**One command for the required files:**

```
python 06-simulation/audits/audits_inert/generate.py
```

**One more for the two bonus sims:**

```
python 06-simulation/audits/audits_inert/generate_bonus.py
```

Both run from anywhere — paths resolve from the script's own location, and every output file is overwritten in place. On Windows, quote the path:

```powershell
python "E:\Google Drive\POLITICAL\Aequitas\06-simulation\audits_inert\generate.py"
```

**Re-run it whenever `arithmetic_audits.py` changes.** Each generated file records the SHA-256 of the sim it was made from, under `provenance`, so a stale artifact is detectable rather than merely wrong. Regeneration needs `numpy` and `scipy`, the same dependencies the sim already has.

The generator prints a four-line summary and two guard lines:

```
  injections whose target check did NOT fire: none
  stated-arithmetic vs Python disagreements: none
```

The first says every injection is still caught. The second is the one that matters here: `generate.py` re-derives every quantity independently, straight from the arithmetic written in `constraints.md`, and compares its answer against the shipped `check_*` functions. **If the mathematics on the page and the code in the sim ever stop agreeing, that line names the constraint where they part.**

---

## What was found while writing this

Nine places where the code does something the prose around it does not say. All nine are in [section 4 of `expected_verdicts.md`](expected_verdicts.md#4-where-the-python-and-the-stated-mathematics-disagree). The three that change how a reader should read the published verdict:

- **IC-12 never reads the event log.** It takes the log as an argument and ignores it, building its own milling decomposition instead. Nothing in `fixture.json` determines the IC-12 row.
- **`min(p) = 0` in the IC-10 line belongs to a substance nothing makes.** Genesis events are excluded when the economy is derived, so a genesis-admitted substance gets a per-unit debit of zero by absence, not by allocation.
- **`rho = 0.980` in the IC-10 line is one number from one event.** It is the repair loop, `5.0 kg in / 5.1 kg out = 0.980392`. The food chain contributes nothing to it.

None of the nine changes a verdict. All nine change what a verdict means.

---

## What this does not fix

Publishing the data does not widen what the constraints cover. The three known holes, all conceded on the board and recorded in `objections.md` (held locally, not published), are unchanged:

1. A process recorded nowhere is invisible to every check here.
2. Truncating the log defeats all nine log-side checks — arithmetic over a prefix of a balanced log is itself balanced.
3. A balanced fabrication — a phantom genesis entry plus a matching phantom disposal — passes all nine.

The honest form of the claim, as restated on the board in c16454: **IC-1 to IC-9 are decidable by recomputation.** These files are what makes that decidable by a reader as well as by a machine.
