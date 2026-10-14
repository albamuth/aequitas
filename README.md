# Aequitas — an accounting system for matter and energy

**This repository exists to be attacked.**

Aequitas is a proposed economic accounting system. It is not a currency, a token, or a blockchain. It is a way of keeping books, in which **credit is a record of hours a person spent on work** and **debit is a record of matter and energy taken from the world, together with who is holding the consequence**.

It makes a small number of falsifiable claims. They are stated below with the code that produces them and the section that states the rule. If you can break one, that is the most useful thing you can do here. **Eleven claims have been withdrawn or narrowed since August 2026, every one of them found from outside; the list is below, with dates.**

---

## Verify something in five minutes

```bash
git clone https://github.com/albamuth/aequitas.git
cd aequitas/06-simulation/audits
python arithmetic_audits.py
```

That builds a small synthetic event log and runs twelve integrity constraints (IC-1 to IC-12) over it. Then, for each constraint, it injects a single deliberate violation to prove the check fires.

Expected output: **12/12 clean checks pass, 12/12 injected violations caught**, followed by an **extent block** stating what the check could *not* see. Read the verdict as *12/12 over that extent*. A bare 12/12 reads as completeness and only ever meant consistency.

**You do not have to run our code to check us.** `06-simulation/audits/audits_inert/` publishes the same thing as inert data: the fixture as plain JSON, each constraint written as arithmetic instead of as Python, and the expected verdict for the clean log and for all twelve injected logs. **Check the paper, not the program.** That was [@twelve-minute-window](https://1f916.ai/post/1605)'s point: a shipped executable makes the repository the trusted object. Conceded.

**The property that matters:** IC-1 to IC-9 need no trust model, no reputation and no authority, only the ability to recompute. An under-declared emission on a **recorded** event is an arithmetic error the log reports on itself. **A process recorded nowhere is not**: arithmetic over a log testifies to nothing outside that log, so coverage is a separate question, answered by a physical total measured from outside and reconciled against the ledger's sum (`00-strategy/Aequitas_Foundations.md` §4.4).

Requires Python 3.11+, `numpy`, `scipy`, `matplotlib`; the request picker needs `PyYAML`.

---

## The claims, and where to attack them

Every rule below is stated in `00-strategy/Aequitas_Foundations.md` (v0.55 at this refresh; the version is in the file's header, the filename never changes). Every figure is a dated reading at a stated setting, never a verdict.

| # | Claim | Code | Write-up |
|---|---|---|---|
| 1 | **Twelve ledger invariants are checkable by recomputation alone**, with no trusted party. Nine check the log; three check what an output carries. | `06-simulation/audits/arithmetic_audits.py` | `06-simulation/audits/AUDITS.md` · `00-strategy/Aequitas_Conformance.md` §2.4 |
| 2 | **The disparity ceiling.** Inside one network's books, the largest and smallest **lifetime pledge budget per day lived** differ by at most `24 ÷ F`, where `F` is the hours a day the network counts as the work of staying alive. ρ cancels and the weighting model does not enter. **It bounds the say over what gets made. It does not bound consumption**, because room pledged to a person has no per-account limit. It is a wall nobody reaches: at `F` = 10 a very hard working life reaches about **1.6×**, against a stated 2.4×. **And it is blind:** the arithmetic never reads an account, so it returns the same figure for honest and invented populations alike. An adversarial search of 20,000 filings under a conforming evaluator never crossed it; the four ways an implementation can let it slip (a cap checked per record, a declared rather than evidenced span, a calendar-day denominator, measured self-care) are each measured, and restoring the setting returns every one to 2.400. | `06-simulation/disparity-ceiling/disparity_ceiling_sim.py` · `06-simulation/ceiling-challenge/ceiling_challenge.py` | `06-simulation/disparity-ceiling/DISPARITY_CEILING.md` · `06-simulation/ceiling-challenge/RESULTS.md` · Foundations §5.5.5 |
| 3 | **A joint process's cost is not divided.** Every co-product carries the whole cost of the steps it passed through, against its own output mass. **36 honest division methods, all satisfying the published obligations, came out 6.31× apart on real refinery energies**, so the division was withdrawn rather than governed. Reading a chain more finely can only lower a figure, confirmed on 1,152 product-resolution pairs with no exception. A ledger walk unions parcels; a naive sum overstates a real refinery by up to 7.00×. | `06-simulation/method-spread/method_spread.py` · `06-simulation/chain-resolution/chain_resolution.py` | `06-simulation/method-spread/RESULTS.md` · `06-simulation/chain-resolution/RESULTS.md` · Foundations §3.4a |
| 4 | **No negative values.** Nothing is divided and nothing is inverted, so Steedman's negative-value result has nothing to attach to. Under the division since withdrawn, 4,098 productive economies gave no negative share while a value-based split went negative in 94.7% of them; the result survives a fortiori with no division performed. | `06-simulation/allocation-engine/recursion_convergence.py` | `06-simulation/allocation-engine/RECURSION_RESULTS.md` |
| 5 | **A workable floor exists.** For every `F` from 1 to 14 hours a day there is a band of ρ inside which essentials stay affordable and the gate still rations what is short; the band never closes and what binds it is physical capacity. A year of essentials for one US person commands **516 to 965 hours** of other people's labour depending on the basket. **Pledging halves the band's upper edge**: at `F` = 10 it falls from 1.20 with no pledging to 0.60 at the one-for-one ceiling. | `06-simulation/stable-band/stable_band.py` · `06-simulation/stable-band/pledge_band.py` · `06-simulation/essentials-basket/essentials.py` | `06-simulation/stable-band/RESULTS.md` · `06-simulation/stable-band/PLEDGE_BAND_RESULTS.md` · `06-simulation/essentials-basket/RESULTS.md` · Foundations §5.5.3 |
| 6 | **At the American production method, the hours do not close.** A median US lifestyle commands about **1,380 hours** of other people's labour a year. Deployable hours (working-age share × participation × hours per worker) reach **0.43 to 0.87** of what that needs, at no corner of the band 1.0. Peer countries at about two thirds of US labour reach it in about a third of swept cases. **The binding constraint is production efficiency, and energy is the tightest physical one** (0.19 of a median standard's need for an autarkic US). | `06-simulation/scenario-suite/q1b_deployable_labour.py` · `06-simulation/scenario-suite/q1_autarky.py` | `06-simulation/scenario-suite/Q1B_DEPLOYABLE_LABOUR.md` · `06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md` · Foundations §3.5 |
| 7 | **Strip the financial layer and the top of the distribution collapses by about 1,000×.** Money wealth reaches about 10⁶ × the median; material consumption about 670 ×. Material-only, **0.1 to 2% of Americans** sit past a permanent lockout on non-essentials, depending on ρ, and selling property does not save them because consumption debit is permanent. The run assumed nobody was pledged to, so the locked fraction is an upper bound. | `06-simulation/scenario-suite/q4_locked_ledgers.py` | `06-simulation/scenario-suite/Q4_LOCKED.md` · Foundations §5.5.8 |
| 8 | **Darkness stops paying, under one specific rule.** Estimating unmeasured producers over the *undisclosed leftover* leaves 0.1% of them dark; estimating over the whole population leaves 52.5% dark, permanently. **The leftover is published whole and divided by nothing**: two worlds whose truths differ by 1.21× hand one network identical books, so no per-head rule computed from those books can tell them apart. The surviving open half is the extent register, which a producer declaring half their real land defeats. | `06-simulation/residual-unravelling/residual_unravelling.py` · `06-simulation/producer-side-splitting/producer_side_splitting.py` | `06-simulation/residual-unravelling/UNRAVELLING.md` · `06-simulation/producer-side-splitting/RESULTS.md` · Foundations §4.4 |
| 9 | **A full re-weighting pass is cheap.** On one ordinary machine, a billion-event log re-checks all nine log constraints in about **100 seconds** and re-weights in about **26**, at `k` = 3 weighting dimensions; the ratio is about 0.012 + 0.122 × `k`, so the two passes cost the same near `k` = 10. First measured from outside, on hardware this project does not control. | `06-simulation/ic-recompute-cost/ic_recompute_cost.py` · `06-simulation/ic-recompute-cost/reweight_ratio.py` | `06-simulation/ic-recompute-cost/RESULTS.md` · `06-simulation/ic-recompute-cost/KSWEEP_RESULTS.md` · Foundations §3.4a |

**Every script behind the table runs standalone with its own self-tests and needs no data files**, with one exception stated plainly. The empirical labour figures, the 1,380 h/yr anchor and the cross-country efficiency comparison, are built on third-party datasets we cannot redistribute: BLS employment-requirements and input-output tables, and EXIOBASE 3. The `track*.py` and `median_lifestyle*.py` scripts are included anyway, because publishing the method matters more than a clean checkout, **and they will not run until you fetch those datasets yourself.** Treat their numbers as cited, not reproducible from this repository alone. Method: `06-simulation/median-lifestyle/median_lifestyle_METHOD.md`.

**Two figures the table does not carry.** The cross-country gap (the US using 50 to 80% more labour than Germany, Sweden, France, Japan or Spain) was computed from household spending only; counting every payer the gap shrinks to 13 to 20%, and Spain's data is missing its retail work. Both are parked for one fold and the core documents still carry the old figures. And `06-simulation/pledge-reserve/` tests **one example of what a trust network may write into a pledge's criteria**, not a rule of the system; the reserve it was built for was withdrawn on 2026-09-18.

---

## What we have withdrawn, in order

Every row was found from outside, and every error ran in this project's own favour. That is the record, and the reason to take the open problems below seriously.

| Date | What we said | What is true now |
|---|---|---|
| 2026-08-22 | An **unrecorded** emission becomes an arithmetic error | Arithmetic over a log testifies to nothing outside the log. Coverage is a physical total measured from outside, `R = N − Y`, published whole (§4.4). [@cairn-lineage](https://1f916.ai/post/1581) |
| 2026-08-22 | The disparity ceiling held across any set of networks that interoperate | **One network's books only.** No book is ever added to another; two networks' figures are not in the same unit (§4.0, §4.2) |
| 2026-08-24 | A5 read "price ≡ cost"; A4 said a consequence is "priced into" the thing | A cost attaches to whoever **caused** it, never to the thing. A5 is now *cost, not price*; a barn is never in the beef (§4.5). Objections B8 |
| 2026-08-24 | A rival sector would fund the correction of an understated cost constant | Withdrawn. A rival's best move is a generous constant of its own. How a network audits its constants is its design, held to five published requirements, **and no network has shown one that works** (§3.3a, OP-24) |
| 2026-08-24 | "Local governance" named A8 | *No governing body.* A trust network has no set size (§4.0) |
| 2026-08-27 | Credited labour (3,647 h/yr) against needed labour (1,600 h/yr) showed slack | **That comparison cannot fail**, because the floor is a value the network sets. Struck. The deployable-hours test replaced it, and at the US method the hours do not close (§3.5). [@alfred-pennyworth] |
| 2026-09-03 | A joint process's cost divides between co-products, by where its inputs physically went | **Nothing is divided.** 36 honest methods came out 6.31× apart. Every co-product carries the whole process cost against its own mass (§3.4a) |
| 2026-09-04 | A4 required every cost to land on *a* ledger | The leftover lands on none. A4 now states the unassigned case by name, until an attribution witness exists (§2.2, §4.4). [@cairn-lineage] |
| 2026-09-09 | A power station's emissions were the consumer's, in proportion to the fuel the grid burned | **The generating company's**, divided among its staff by hours worked. A kilowatt-hour carries only the labour and materials the plant consumed; the consumer never held the fuel (§3.2b) |
| 2026-09-18 | The gate was `D ≤ ρ·C`; a task's surplus pledges were a non-consumable contingent reserve; the ceiling bounded consumption | The gate is **`D ≤ ρ·(C + P)`**. A pledge names a person or the criteria that will name one, and committed room is consumable. The ceiling is restated over pledge budgets and **consumption is not bounded** (§3.0, §4.6, §5.5.5) |
| 2026-08-31 | "Still 2.4× at 40% fraud" was reported as robustness | The bound never reads an account, so it is also **blind**. A check that compares a thing to itself can find a mistake and cannot find a hole (§5.5.7). [@cairn-lineage] |

**The pattern.** The early corrections were *we said more than we proved*. The later ones were *the answer was already written in one section, and an older section still said the opposite*. If you are looking for the next one, that is where to look.

---

## The theory

| File | What it is |
|---|---|
| `00_START_HERE.md` | The short version. Read this first. |
| **`00-strategy/README.md`** | **The map of the theory folder**: what every file is for, and what to read first depending on why you are here. |
| `00-strategy/Aequitas_Overview.md` | Plain-language walkthrough. No economics background assumed. |
| `00-strategy/Aequitas_Foundations.md` | The rigorous version: eight axioms and every mechanism, each with a worked example. **Where this and the Overview differ, Foundations governs.** Its version is the `> **Version:**` line in its header; the filename never changes. |
| `00-strategy/Aequitas_Conformance.md` | **What must be true for an implementation to be Aequitas**, including IC-1 to IC-12 as numbered rows. What must be true, never how to build it. |
| `00-strategy/Aequitas_Objections.md` | **The register of open problems and answered objections.** Read it before writing a critique: your objection may already be listed, and several are listed as *unsolved*. |
| `00-strategy/Aequitas_Question_Index.md` | The questions readers ask, keyed by the question, with a verdict: REFUSED by an axiom, ANSWERED in a section, or OPEN. |
| `00-strategy/GLOSSARY.md` | Every abbreviation (A#, C#, IC-#, OP-#) and every source, in one place. |
| `00-strategy/Aequitas_Strategy.md` · `00-strategy/Aequitas_Simulation_Roadmap.md` | The roadmap, and the simulation programme. |
| `00-strategy/open-problems/` | One paper per open problem: OP-9 (the reply to Mises and Hayek), OP-16, OP-17, OP-18, OP-22, OP-23, OP-26 (two papers), OP-27 (using Aequitas while the world still uses money), OP-28. |
| `00-strategy/papers/` | Settled working papers the core documents still cite: `C2_TrustNetworks.md` (who carries this out: laboratories, not banks), `C2_information_capture.md` (contains a retraction of its own central proposal, kept unedited), `Onboarding_the_wealthy.md`, `Pledges.md`, `Shelf_life_and_custody.md`. |
| `01-wiki/` | **One page per concept, 70 of them, each a node in a typed graph.** Every page carries a one-sentence summary, a worked example with digits, its status, and the section that states it. `01-wiki/AGENT_GUIDE.md` says how to answer a question from one page and its edges; `graph.md` is the node table and `graph.json` the machine-readable form. **The fastest way in for a reader who wants one mechanism.** |
| `02-research/` | Source stubs: Proudhon, Warren, Neurath, Kantorovich, Cockshott and Cottrell, Albert and Hahnel, Ellerman, Steedman's joint-production problem, the local-currency field record, and the datasets. Each carries a citation, the date retrieved, and why it matters. |
| `06-simulation/` | Every simulation, one folder each, with its own `README.md`, `CHANGELOG.md` and `RESULTS.md`. `06-simulation/README.md` is the landing page. The nightly simulation agent's brief and queue are here too. |

---

## What Aequitas does not claim

Stated up front so nobody wastes a cycle refuting a position we do not hold.

- **It is not a theory of value.** It measures cost: hours, joules, kilograms, damage. It never computes what a thing is *worth*. Preferences enter the system elsewhere, through pledges.
- **The disparity ceiling bounds the say over what gets made, in one network's books, and nothing else.** It does not bound consumption. It depends on the floor the network sets, on whether that network credits a child's learning time, on fraud not manufacturing hours, and on OP-22. It cannot detect fraud.
- **Labour is not simply abundant.** At the American production method the hours do not close. The claim is that the constraint is the method.
- **Several problems are open.** They are listed in `00-strategy/Aequitas_Objections.md` and summarised in `01-wiki/open-problems.md`: who governs the weighting model (OP-10), understatement drift (OP-24), whether anyone pledges for dull work (OP-16), what an auditor must be shown (OP-22), the floor formula (OP-4), the extent register (OP-28), and the coordinator class (P4).
- **It is not a political programme.** It keeps existing institutions, municipal government, planning, the civil service, and changes only their economic nature.
- **It is not a piece of software.** These documents never specify one. What database, what cryptography, how private: all of that belongs to whoever builds a trust network.

---

## Provenance

Author: a human political theorist. Development is done with AI assistance and is logged. Two nightly agents work on the project: one posts and answers critics on [1f916.ai](https://1f916.ai) as `cost-is-not-value` and never runs a simulation; the other runs one simulation a night from `06-simulation/SIM_QUEUE.yaml` and pushes a `sim-nightly/<date>` branch, and never posts.

This repository is a **mirror** of a larger working project. It carries the current documents, the wiki, the research notes and the self-contained simulations. Superseded versions and change histories are held locally and are not published; every live document states what is currently true and nothing about what it used to say.

---

## How to respond

- **Found a real flaw?** That is the point. Open an issue, or reply in the thread where you found this.
- **Want to extend it?** The open problems in `00-strategy/Aequitas_Objections.md` are the useful frontier.
- **Think the whole framing is wrong?** Say why, specifically. *Cost is not value* is the move everything rests on. If it fails, everything above it fails.
