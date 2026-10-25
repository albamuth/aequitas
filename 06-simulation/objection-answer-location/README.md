# objection-answer-location

> **Version:** 0.1
> **Date:** 2026-10-22

**Takes every outside finding in the objections register and asks where its answer actually lived: in the section the critic named, elsewhere but reachable by a search built from the critic's own words, or somewhere a search from those words does not reach.**

| | |
|---|---|
| **Status** | ✅ Run 2026-10-22 |
| **Answers** | `sr-20260906-over-the-project-s-own-objection-register-cl`, from `obj-20260905-self-council-axioms-not-self-sufficient` |
| **Result** | See [`RESULTS.md`](RESULTS.md) |
| **Run** | `python answer_location.py` (writes `results.json`) |
| **Self-tests** | `python answer_location.py --test` (10 checks, each of which can fail) |

## Files

| File | What it is |
|---|---|
| `findings.py` | The hand-coded table: 28 outside findings, the critic's words, the sections they named, and the pre-existing answer text |
| `answer_location.py` | Loads Foundations and Conformance line by line, ranks every line against each critic's words (BM25), classifies |
| `DECLARED_BEFORE_RUNNING.md` | The five outcomes, written before the first run |
| `results.json`, `run_output.txt` | The raw output of the run in RESULTS.md |

## What it reads

`00-strategy/Aequitas_Objections.md` for the findings and `00-strategy/Aequitas_Foundations.md` and `00-strategy/Aequitas_Conformance.md` for the answers. It reads critic wording from `07-outreach/memory/records/` where a verbatim record exists. It writes only here.
