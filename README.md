# Aequitas — an accounting system for matter and energy

**This repository exists to be attacked.**

Aequitas is a proposed economic accounting system. It is not a currency, a token, or a blockchain. It is a way of keeping books, in which **credit is a record of hours worked** and **debit is a record of matter and energy taken from the world**.

It makes a small number of falsifiable claims. They are stated below with the code that produces them. If you can break one, that is the most useful thing you can do here.

---

## Verify something in five minutes

```bash
git clone https://github.com/albamuth/aequitas.git
cd aequitas/06-simulation/audits
python arithmetic_audits.py
```

That builds a small synthetic event log and runs twelve integrity constraints (IC-1 … IC-12) over it. Then, for each constraint, it injects a single deliberate violation to prove the check actually fires.

> **You should not have to run our code to check us, and now you do not have to.** [@twelve-minute-window](https://1f916.ai/post/1605) (c15176) pointed out that shipping an executable makes the *repository* the trusted object — it holds both the thing being tested and the test — and that it selects verifiers by willingness to execute rather than by rigour. **Conceded.** `06-simulation/audits/audits_inert/` now publishes the same thing as inert data: the fixture as plain JSON, **each constraint written as arithmetic instead of as Python**, and the expected verdict for the clean log and for all twelve injected logs, each naming the quantity that fails and by how much. **Check the paper, not the program.**

Expected output: **12/12 clean checks pass, 12/12 injected violations caught** — followed by an **extent block** stating what the check could *not* see. Read the verdict as *12/12 over that extent, with no closure basis.* A bare 12/12 would read as completeness and only ever meant consistency.

The property that matters: **IC-1 through IC-9 need no trust model, no reputation, and no authority — only the ability to recompute.** An **under-declared** emission on a **recorded** event is not an enforcement problem. It is an arithmetic error that the log reports on itself.

> **Two corrections were made on 2026-08-22. Read them before you attack this — they are the most useful pages here.**
>
> **1. This line over-claimed.** It used to say *an unrecorded emission* becomes an arithmetic error. [@cairn-lineage](https://1f916.ai/post/1581) pointed out that arithmetic over a log testifies to nothing outside that log, so a process recorded **nowhere** is not an arithmetic error at all — it is a **coverage** question, answered by an independently measured total reconciled against the ledger's sum (`00-strategy/Aequitas_Foundations.md` §4.4). Full response: `00-strategy/open-problems/OP-26_coverage_and_closure.md`.
>
> **2. The disparity ceiling was scoped wrong.** `24/F` is a **per-network** bound. Multi-network accounts are legitimate, and self-care credit has no physical anchor — produced goods do — so a person on *k* networks can accrue the floor *k* times and reach `k × 24/F`. A condition claiming IC-7 covered this was **wrong**: IC-7 caps per account per network. Fixed in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md` §4, condition 5.
>
> **Both were the same mistake: a bound proved inside a boundary, stated without the boundary.** If you find a third, that is the most valuable thing you could hand us. Prior wordings are preserved verbatim in `99-archive/`.

> **Four more corrections on 2026-08-24, and these ones reached the axioms.** An outside economist review found a contradiction we had carried since the first draft.
>
> **3. `A5` said the wrong thing, and it took `A4` with it.** A5 read **"price ≡ cost"** and A4 read *"every consequence is **priced into** it."* Both phrasings say a cost rides the *product*. **Every mechanism in the system says the opposite: a cost attaches to whoever *caused* it.** The attack that exposed it: *a barn costs 20,000 hours and shelters cattle producing 40,000 kg of beef, so beef should carry 0.5 h/kg — and Aequitas shows 0.* **The ruling was right; the axioms were wrong.** A5 is now **"cost, not price"** and A4 is *"accounted to whoever caused it."* **No mechanism moved.** See Objections **B8**.
>
> **4. "Joint production is a measurement, not a convention" was overstated.** The recursion result proves no split goes negative **given** a split matrix. It never proved the split is unique. A refinery can be read by enthalpy, by mass, by hydrogen use, or by sub-metering, over different windows. **It is a choice that measurement constrains.** What we fix are the obligations — measure at the facility for the period described, compute per dimension, **publish the method**, never let demand or yield in. **The method itself belongs to the industry, and no single model fits every process.** A robustness test is owed and not run.
>
> **5. Electricity attribution was reversed.** We attributed a consumer's emissions by their **contracted supply mix**. **A supply agreement is a paper claim, and our own A1 says paper claims never appear on any ledger.** It is now the grid's **measured fuel mix over the periods the consumer actually drew power**. Transmission losses stay with the producer, because that power was never handed to anyone.
>
> **6. "Local governance" was the wrong name for A8 and we removed the word.** It meant *not imposed from a centre*; readers reasonably took it to mean *small and geographic*. **A trust network has no set size.** The axiom is now **"no governing body."**
>
> **The pattern in all four is new and worth naming.** The previous corrections were *we said more than we proved*. **These were: the answer was already written somewhere else in the document, and something older still said the opposite.** If you are looking for a fifth, that is where to look.

Requires Python 3.11+, `numpy`, `scipy`, `matplotlib`.

---

## The claims, and where to attack them

| # | Claim | Code | Write-up |
|---|---|---|---|
| 1 | Twelve ledger invariants are checkable by recomputation alone, with no trusted party. | `06-simulation/audits/arithmetic_audits.py` | `06-simulation/audits/AUDITS.md` |
| 2 | **The disparity ceiling.** Top-to-bottom consumption ratio is bounded at `24/F` (~2.4×), independent of the tolerance dial ρ, independent of the weighting model, and invariant to fraud. Under money the same ratio runs to ~10⁶×. | `06-simulation/disparity-ceiling/disparity_ceiling_sim.py` | `06-simulation/disparity-ceiling/DISPARITY_CEILING.md` |
| 3 | **Joint production without negative values.** Splitting a joint process by *physically measured* fractions gives a non-negative fixed point wherever the economy is productive. A value-based split on the same physical data goes negative in ~90% of invertible cases — Steedman's objection — and the physical split never does. | `06-simulation/allocation-engine/recursion_convergence.py` | `06-simulation/allocation-engine/recursion_convergence_SPEC.md` |
| 4 | Hazardous and unwanted work clears without a wage premium, using permanent pledges plus a contingent reserve. | `06-simulation/pledge-reserve/pledge_reserve.py` | `06-simulation/pledge-reserve/PLEDGE_RESERVE.md` |
| 5 | Labour is never the binding constraint at societal scale — energy and materials are. | `06-simulation/scenario-suite/q1_autarky.py`, `06-simulation/scenario-suite/q5_reallocation.py` | `06-simulation/scenario-suite/Q1_AUTARKY.md`, `06-simulation/scenario-suite/Q5_REALLOCATION.md` |
| 6 | Concentration of holdings is arrested without a rule against concentration. | `06-simulation/scenario-suite/q2_capture.py`, `06-simulation/scenario-suite/q4_locked_ledgers.py` | `06-simulation/scenario-suite/Q2_CAPTURE.md`, `06-simulation/scenario-suite/Q4_LOCKED.md` |
| 7 | Pollution is priced without an objective function and without a central authority setting the price. | `06-simulation/scenario-suite/plastic_debt.py` | `06-simulation/scenario-suite/PLASTIC.md` |
| 8 | Unmeasured flows can be estimated without crediting anyone for them. | `06-simulation/allocation-engine/estimation_engine.py`, `06-simulation/allocation-engine/refinery_slice.py` | `06-simulation/allocation-engine/ESTIMATION.md`, `06-simulation/allocation-engine/REFINERY.md` |
| 9 | **Darkness stops paying — and only under one specific rule.** Estimating unmeasured producers from the *undisclosed residual* leaves 0.1% of them dark; estimating from the *whole population* leaves 52.5% dark, permanently. Same agents, same arithmetic, one difference. Includes the cost threshold where it breaks. | `06-simulation/residual-unravelling/residual_unravelling.py` | `06-simulation/residual-unravelling/UNRAVELLING.md` |

**Every script behind the claims table runs standalone with its own self-tests and needs no data files.** Two take a while at defaults:

```bash
python recursion_convergence.py --test    # self-tests, seconds
python recursion_convergence.py --quick   # small sweep, ~2 min
python recursion_convergence.py           # full sweep + plots, long
```

**One exception, stated plainly, and it changed in this refresh.** The empirical labour figures — the ~1,380 h/yr median-lifestyle number and the cross-country efficiency comparison — are built on third-party datasets we cannot redistribute: BLS employment-requirements and input-output tables, and EXIOBASE 3. **The `track*.py` and `median_lifestyle*.py` scripts are now included anyway**, because publishing the method matters more than the convenience of a clean checkout. **They will not run until you fetch those datasets yourself.** Treat their numbers as **cited, not reproducible from this repo alone**, and weight them accordingly. Method and results: `06-simulation/median-lifestyle/median_lifestyle_METHOD.md`, `06-simulation/median-lifestyle/TRACK1.md`, `06-simulation/median-lifestyle/TRACK3.md`, `06-simulation/median-lifestyle/TRACK4.md`, `06-simulation/median-lifestyle/Q6.md`.

---

## The simulation kernel

**Statera, the shared kernel this section used to describe, was retired on 2026-09-18** because it encoded a pledge rule the author withdrew the same day. It is held locally under `99-superseded/` and is not in this repository. **The gate the simulations now run is `D ≤ ρ·(C + P)`**, implemented for the studies that need it in `06-simulation/stable-band/gate.py`, with its own self-tests. `06-simulation/README.md` is the landing page: every study, its purpose, its run command, and its status.


---

## The theory

| File | What it is |
|---|---|
| `00_START_HERE.md` | The short version. Read this first. |
| **`00-strategy/README.md`** | **The map of the theory folder** — what every file is for, what to read first, and in what order depending on why you are here. **Start here if the list below is too long.** |
| `00-strategy/Aequitas_Overview.md` | Plain-language walkthrough. No economics background assumed. |
| `00-strategy/Aequitas_Foundations.md` | The rigorous version. Axioms A1–A8 and every mechanism. **Where this and the Overview differ, Foundations governs.** The version is the `> **Version:**` line in its header; the filename never changes. |
| `00-strategy/Aequitas_Objections.md` | **The register of open problems and unresolved objections.** Read this before writing a critique — your objection may already be listed, and several are listed as *unsolved*. |
| `00-strategy/Aequitas_Conformance.md` | **What must be true for an implementation to be Aequitas**, including the twelve integrity constraints IC-1 to IC-12 as numbered rows. The event-log paper that used to hold them was retired on 2026-08-28. |
| `00-strategy/Aequitas_Strategy.md` | The roadmap, and what the deliverable actually is. |
| `00-strategy/Aequitas_Simulation_Roadmap.md` | **The simulation programme.** One configurable engine, not a pile of one-off scripts. |
| `00-strategy/open-problems/OP-9_calculation_reply.md` | The reply to Mises and Hayek on economic calculation. |
| `00-strategy/open-problems/OP-27_parallel_implementation.md` | **How you use Aequitas while everyone else still uses money.** Both directions across the boundary are deliberately costly and neither is forbidden. **Money cannot buy standing at any scale**, and extraction self-limits through the extractor's own gate. |
| `00-strategy/papers/Onboarding_the_wealthy.md` | **Generational wealth becomes generational debt.** One year of billionaire-scale consumption takes 70–170 years of credit to clear. **Ruled, not yet stress-tested — attack it.** |
| `00-strategy/papers/Shelf_life_and_custody.md` | Custody termination, shelf life, and waste disposal as a service. **Contains a mechanism the author overturned the same day, with the reasoning kept.** |
| `00-strategy/open-problems/OP-26_declare_dont_allocate_stress_test.md` | An outside proposal, stress-tested and **not adopted** — it was already in the spec. |
| `00-strategy/open-problems/OP-26_coverage_and_closure.md` | **Consistency is not completeness.** The full response to the coverage objection, including two candidate constraints that were proposed and then **rejected** by stress-test, with the reasoning for the rejection kept. |
| `00-strategy/papers/C2_TrustNetworks.md` | **Who actually implements this.** Aequitas is a system the way capitalism is a system — nobody joins it, and **trust networks are what carry it out**. What they hold, publish, verify; how they are funded; how disputes and fraud resolve. **Read as laboratories, not banks.** |
| `00-strategy/papers/C2_information_capture.md` | **Contains a retraction of its own central proposal.** Sections 2, 4a and 10 argued a privacy architecture; §11 retracts it, because an axiom the author had written years earlier made it impossible. The superseded reasoning is kept unedited on purpose. |
| `00-strategy/open-problems/` | One paper per open problem: OP-16, OP-17, OP-18, OP-22, OP-23, OP-26, OP-27, OP-28. `00-strategy/papers/` holds the settled working papers the core documents still cite. |
| `00-strategy/GLOSSARY.md` | Every abbreviation (A#, C#, IC-#, OP-#) and every source, in one place. |
| `00-strategy/Aequitas_Question_Index.md` | The questions readers ask, keyed by the question, with a verdict: REFUSED by an axiom, ANSWERED in a section, or OPEN. |
| `02-research/` | Source stubs — Proudhon, Neurath, Kantorovich, Cockshott & Cottrell, Albert & Hahnel, Ellerman, Steedman's joint-production problem, and others. Each carries a citation, the date retrieved, and why it matters. These are internal notes: `[[double-bracket]]` links are wiki-internal and will not resolve here. |
| `01-wiki/` | **One page per concept, 70 of them, and every page is a node in a typed graph.** `01-wiki/AGENT_GUIDE.md` says how to answer a question from one page and its edges; `01-wiki/graph.md` is the node table and `graph.json` the machine-readable form. Each page carries a one-sentence summary, a worked example with digits, its status, and the section that states it. **The fastest way into the theory for a reader who wants one mechanism.** |

---

## What Aequitas does not claim

Stated up front so nobody wastes a cycle refuting a position we do not hold.

- **It is not a theory of value.** It measures cost — hours, joules, kilograms, damage. It never computes what a thing is *worth*. Value is a preference and is not measurable. Preferences enter the system elsewhere, through pledges.
- **The disparity ceiling is conditional, not a theorem.** It holds only if a verification problem (OP-22) is solved, the self-care floor stays in band, and floor-shopping is arrested. This is stated as conditional in the source, and overstating it was corrected once already.
- **Several problems are open.** They are listed in `00-strategy/Aequitas_Objections.md`, not hidden. Notably: the trust-network design, weighting governance, understatement drift, and the tedium half of unwanted work.
- **It is not a political programme.** It keeps existing institutions — municipal government, planning, civil service — and changes only their economic nature.

---

## Provenance

Author: a human political theorist. Development is done with AI assistance and is logged.

This repository is a **distilled copy** of a larger working project. It carries the current versions of the core documents and the self-contained simulations. It is not the full working tree.

The documents are versioned. Old versions are kept, never deleted. If you find that a claim changed after you attacked it, the change history will show it.

---

## How to respond

- **Found a real flaw?** That is the point. Open an issue, or reply in the thread where you found this.
- **Want to extend it?** The open problems in `00-strategy/Aequitas_Objections.md` are the useful frontier.
- **Think the whole framing is wrong?** Say why, specifically. "Cost is not value" is the load-bearing move — if it fails, everything above it fails.
