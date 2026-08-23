# Aequitas — an accounting system for matter and energy

**This repository exists to be attacked.**

Aequitas is a proposed economic accounting system. It is not a currency, a token, or a blockchain. It is a way of keeping books, in which **credit is a record of hours worked** and **debit is a record of matter and energy taken from the world**.

It makes a small number of falsifiable claims. They are stated below with the code that produces them. If you can break one, that is the most useful thing you can do here.

---

## Verify something in five minutes

```bash
git clone https://github.com/albamuth/aequitas.git
cd aequitas/sims
python arithmetic_audits.py
```

That builds a small synthetic event log and runs twelve integrity constraints (IC-1 … IC-12) over it. Then, for each constraint, it injects a single deliberate violation to prove the check actually fires.

Expected output: **12/12 clean checks pass, 12/12 injected violations caught** — followed by an **extent block** stating what the check could *not* see. Read the verdict as *12/12 over that extent, with no closure basis.* A bare 12/12 would read as completeness and only ever meant consistency.

The property that matters: **IC-1 through IC-9 need no trust model, no reputation, and no authority — only the ability to recompute.** An **under-declared** emission on a **recorded** event is not an enforcement problem. It is an arithmetic error that the log reports on itself.

> **Two corrections were made on 2026-08-22. Read them before you attack this — they are the most useful pages here.**
>
> **1. This line over-claimed.** It used to say *an unrecorded emission* becomes an arithmetic error. [@cairn-lineage](https://1f916.ai/post/1581) pointed out that arithmetic over a log testifies to nothing outside that log, so a process recorded **nowhere** is not an arithmetic error at all — it is a **coverage** question, answered by an independently measured total reconciled against the ledger's sum (`docs/Aequitas_Foundations_v0.17.md` §5.1b). Full response: `docs/OP-26_coverage_and_closure.md`.
>
> **2. The disparity ceiling was scoped wrong.** `24/F` is a **per-network** bound. Multi-network accounts are legitimate, and self-care credit has no physical anchor — produced goods do — so a person on *k* networks can accrue the floor *k* times and reach `k × 24/F`. A condition claiming IC-7 covered this was **wrong**: IC-7 caps per account per network. Fixed in `sims/DISPARITY_CEILING.md` §4, condition 5.
>
> **Both were the same mistake: a bound proved inside a boundary, stated without the boundary.** If you find a third, that is the most valuable thing you could hand us. Prior wordings are preserved verbatim in `docs/superseded/`.

Requires Python 3.11+, `numpy`, `scipy`, `matplotlib`.

---

## The claims, and where to attack them

| # | Claim | Code | Write-up |
|---|---|---|---|
| 1 | Twelve ledger invariants are checkable by recomputation alone, with no trusted party. | `sims/arithmetic_audits.py` | `sims/AUDITS.md` |
| 2 | **The disparity ceiling.** Top-to-bottom consumption ratio is bounded at `24/F` (~2.4×), independent of the tolerance dial ρ, independent of the weighting model, and invariant to fraud. Under money the same ratio runs to ~10⁶×. | `sims/disparity_ceiling_sim.py` | `sims/DISPARITY_CEILING.md` |
| 3 | **Joint production without negative values.** Splitting a joint process by *physically measured* fractions gives a non-negative fixed point wherever the economy is productive. A value-based split on the same physical data goes negative in ~90% of invertible cases — Steedman's objection — and the physical split never does. | `sims/recursion_convergence.py` | `sims/recursion_convergence_SPEC.md` |
| 4 | Hazardous and unwanted work clears without a wage premium, using permanent pledges plus a contingent reserve. | `sims/pledge_reserve.py` | `sims/PLEDGE_RESERVE.md` |
| 5 | Labour is never the binding constraint at societal scale — energy and materials are. | `sims/q1_autarky.py`, `sims/q5_reallocation.py` | `sims/Q1_AUTARKY.md`, `sims/Q5_REALLOCATION.md` |
| 6 | Concentration of holdings is arrested without a rule against concentration. | `sims/q2_capture.py`, `sims/q4_locked_ledgers.py` | `sims/Q2_CAPTURE.md`, `sims/Q4_LOCKED.md` |
| 7 | Pollution is priced without an objective function and without a central authority setting the price. | `sims/plastic_debt.py` | `sims/PLASTIC.md` |
| 8 | Unmeasured flows can be estimated without crediting anyone for them. | `sims/estimation_engine.py`, `sims/refinery_slice.py` | `sims/ESTIMATION.md`, `sims/REFINERY.md` |
| 9 | **Darkness stops paying — and only under one specific rule.** Estimating unmeasured producers from the *undisclosed residual* leaves 0.1% of them dark; estimating from the *whole population* leaves 52.5% dark, permanently. Same agents, same arithmetic, one difference. Includes the cost threshold where it breaks. | `sims/residual_unravelling.py` | `sims/UNRAVELLING.md` |

**Every `.py` file in `sims/` runs standalone with its own self-tests and needs no data files.** Two take a while at defaults:

```bash
python recursion_convergence.py --test    # self-tests, seconds
python recursion_convergence.py --quick   # small sweep, ~2 min
python recursion_convergence.py           # full sweep + plots, long
```

**One exception, stated plainly.** The empirical labour figures (the ~1,380 h/yr median-lifestyle number and the cross-country efficiency comparison) come from tracks built on third-party datasets — BLS employment-requirements and input-output tables, and EXIOBASE 3. Those inputs are large and not ours to redistribute, so those scripts are **not** in this repo. The method and the results are: `sims/median_lifestyle_METHOD.md`, `sims/TRACK1.md`, `sims/TRACK3.md`, `sims/TRACK4.md`, `sims/Q6.md`, `sims/median_lifestyle_RESULTS.md`. Treat those numbers as **cited, not reproducible from this repo alone**, and weight them accordingly. Everything in the table above is fully reproducible here.

---

## The theory

| File | What it is |
|---|---|
| `00_START_HERE.md` | The short version. Read this first. |
| `docs/Aequitas_Overview_v0.13.md` | Plain-language walkthrough. No economics background assumed. |
| `docs/Aequitas_Foundations_v0.17.md` | The rigorous version. Axioms A1–A8 and every mechanism. **Where this and the Overview differ, Foundations governs.** |
| `docs/Aequitas_Objections_v0.17.md` | **The register of open problems and unresolved objections.** Read this before writing a critique — your objection may already be listed, and several are listed as *unsolved*. |
| `docs/Aequitas_EventLog_v0.8.md` | The data model. Event schema and the twelve integrity constraints. |
| `docs/OP-9_calculation_reply.md` | The reply to Mises and Hayek on economic calculation. |
| `docs/OP-26_coverage_and_closure.md` | **Consistency is not completeness.** The full response to the coverage objection, including two candidate constraints that were proposed and then **rejected** by stress-test, with the reasoning for the rejection kept. |
| `docs/C2_information_capture.md` | **Contains a retraction of its own central proposal.** Sections 2, 4a and 10 argued a privacy architecture; §11 retracts it, because an axiom the author had written years earlier made it impossible. The superseded reasoning is kept unedited on purpose. |
| `docs/OP-16`, `OP-17`, `OP-18`, `OP-23` | Standalone working papers on hazard authorization, co-product allocation, team credit, and capital/pollution. |
| `docs/*_CHANGELOG.md` | Version history for each core document. Every change, dated. |
| `docs/GLOSSARY.md` | Terms and sources. |
| `research/` | Source stubs — Proudhon, Neurath, Kantorovich, Cockshott & Cottrell, Albert & Hahnel, Ellerman, Steedman's joint-production problem, and others. Each carries a citation, the date retrieved, and why it matters. These are internal notes: `[[double-bracket]]` links are wiki-internal and will not resolve here. |
| `wiki/` | Two concept pages referenced by the simulations, plus figures. |

---

## What Aequitas does not claim

Stated up front so nobody wastes a cycle refuting a position we do not hold.

- **It is not a theory of value.** It measures cost — hours, joules, kilograms, damage. It never computes what a thing is *worth*. Value is a preference and is not measurable. Preferences enter the system elsewhere, through pledges.
- **The disparity ceiling is conditional, not a theorem.** It holds only if a verification problem (OP-22) is solved, the self-care floor stays in band, and floor-shopping is arrested. This is stated as conditional in the source, and overstating it was corrected once already.
- **Several problems are open.** They are listed in `docs/Aequitas_Objections_v0.17.md`, not hidden. Notably: the trust-network design, weighting governance, understatement drift, and the tedium half of unwanted work.
- **It is not a political programme.** It keeps existing institutions — municipal government, planning, civil service — and changes only their economic nature.

---

## Provenance

Author: a human political theorist. Development is done with AI assistance and is logged.

This repository is a **distilled copy** of a larger working project. It carries the current versions of the core documents and the self-contained simulations. It is not the full working tree.

The documents are versioned. Old versions are kept, never deleted. If you find that a claim changed after you attacked it, the change history will show it.

---

## How to respond

- **Found a real flaw?** That is the point. Open an issue, or reply in the thread where you found this.
- **Want to extend it?** The open problems in `docs/Aequitas_Objections_v0.17.md` are the useful frontier.
- **Think the whole framing is wrong?** Say why, specifically. "Cost is not value" is the load-bearing move — if it fails, everything above it fails.
