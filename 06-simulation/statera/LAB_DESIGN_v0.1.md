# Aequitas Lab — design on paper

> **Version:** 0.1 · **Date:** 2026-08-23 · **Status:** Design only. No code written against this yet.
> **Author sign-off required before Phase 1.**
> **Parent:** [`../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`](../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md) · **Built on:** [`statera.py`](statera.py), [`STATERA.md`](README.md)

---

## 0. What this is

**A shippable simulator of an Aequitas economy that a human can open and run, with a clear screen and no installation.** The code goes on GitHub, and it becomes the thing the outreach agent asks strangers for help with.

**The name.** *Aequitas Lab*, because Foundations §4.8 already calls trust networks **laboratories rather than banks**. Author's call; "Aequitas Simulator" also works and is duller.

---

## 1. The three decisions, made — overrule any of them

### Decision 1 — One kernel, two front doors. The rules live in Python, once.

| Front door | For | Size |
|---|---|---|
| **CLI** — `python statera.py`, `python run_scenario.py my.json` | Research-grade runs, big populations, batch sweeps | N = 200,000 |
| **Browser** — a page on GitHub Pages | Everyone else. Zero install. | N = 5,000 |

**Both load the same `statera.py`.** The browser runs it through Pyodide, which is CPython compiled to run in a web page, numpy included.

> **🔒 The hard rule: the GUI never contains a rule.** Not one. If the screen ever computes a standing, a gate, or a split by itself, there are two implementations of Aequitas and they will drift. **The GUI reads numbers out of the kernel and draws them. That is all it does.**

**Why not rewrite the kernel in JavaScript.** Because then the axioms exist in two languages, and the day they disagree you will not know which one is Aequitas. **A second implementation is a second theory.**

**What this costs, stated honestly.** Pyodide plus numpy is roughly **15 MB on first load**, a few seconds on a normal connection, then cached. A big sweep is slow in a page — the 400-point ρ search over 200,000 agents takes 11 seconds natively and would be minutes in a browser. **So the browser runs smaller populations, and that is fine:** the structural results do not depend on N. At a 10-hour floor the disparity bound came out at exactly 2.4000 with a spread of 8.9 × 10⁻¹⁶, and it is 2.4000 at N = 5,000 too. **Calibrated numbers stay on the CLI, where they already are.**

### Decision 2 — A scenario is a file, and a file is a link

**One JSON format, three uses:** the GUI saves and loads it, the CLI runs it, and the page encodes it into its own URL so a scenario can be sent to someone as a link.

**This is the whole answer to "how does the agent ask for help."** It posts a link. Nobody clones anything, nobody runs a stranger's code, and everyone is looking at the identical run.

> **This directly answers an objection the agent already conceded in public.** @twelve-minute-window's point on 2026-08-23 was that **shipping executable-only selects verifiers on willingness to run a stranger's code, which is uncorrelated with rigour** — and that they themselves declined to run it, on the board's own guidance, and were right to. **A page answers that. A repository does not.**

### Decision 3 — The conformance panel is permanent and always visible

The conformance requirements run as live checks, on screen, every period. **Green while they hold. Red the instant one fails, with the requirement named and the run stopped at the offending event.**

**This is the part no other economy toy has**, and it is the part that makes this Aequitas rather than a generic model. **A simulator that cannot fail cannot teach**, and one that fails silently is worse than one that cannot fail at all.

---

## 2. The screen

**One page. No navigation, no tabs, no modal dialogs in the main loop.**

```
┌───────────────────────────────────────────────────────────────────────────────┐
│  Aequitas Lab      [ Locality vs money, 20y  ▾ ]      [Share] [Load] [Save]   │
├─────────────────┬─────────────────────────────────────────┬───────────────────┤
│  SCENARIO       │  THE WORLD                              │  CONFORMANCE      │
│                 │                                         │                   │
│  Dials          │  ┌─────────────────┬─────────────────┐  │  ● IC-1  mass     │
│   ρ      1.20 ──│──│ Disparity       │ Who gets what   │  │  ● IC-2  energy   │
│   F      10 h ──│──│  over time      │  histogram      │  │  ● IC-3  origin   │
│   method  US  ▾ │  │                 │                 │  │  ● IC-4  fate     │
│   verif  0.10 ──│──└─────────────────┴─────────────────┘  │  ● IC-7  24 h/day │
│                 │  ┌─────────────────┬─────────────────┐  │  ● IC-8  pledges  │
│  Population     │  │ Participation   │ Pollutant stock │  │  ● A3    credit   │
│   N     5,000 ──│──│  over time      │  over time      │  │  ● A6    derived  │
│   growth  0 % ──│──└─────────────────┴─────────────────┘  │  ● §3.2a split    │
│                 │                                         │  ● §3.3  txn-time │
│  World          │  ─── consumption gap, top vs floor ───  │  ● §5.5  floor    │
│   outside money▾│   Aequitas  ▓▓▓ 2.4×  (at F=10 h)        │                   │
│                 │   US money  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 670×      │  ─────────────────│
│  Shocks         │   (SCF 2022 + Forbes, material-only)    │  INSPECTOR        │
│   @120  budget  │                                         │  agent #4,187     │
│         ×0.70   │                                         │   credit  4,380 h │
│   [+ add shock] │                                         │   debit   1,509 h │
│                 │                                         │   ratio    0.34   │
│                 │                                         │  ── event log ──  │
│                 │                                         │  p47 self-care 10 │
│                 │                                         │  p47 work     6.0 │
│                 │                                         │  p47 consume  8.0 │
│                 │                                         │  p46 self-care 10 │
├─────────────────┴─────────────────────────────────────────┴───────────────────┤
│  ⏮   ▶ Play   ⏸   ⏭      period  47 / 240   ──────●───────────    speed ▾    │
└───────────────────────────────────────────────────────────────────────────────┘
```

### What each part is for

| Panel | Job | Why it earns its space |
|---|---|---|
| **Scenario rail** | Every dial from the roadmap: ρ, `F`, production method, verification cost, population size and growth, the outside world, and shocks. | **Dials may be moved mid-run.** That is not a convenience — it *is* §3.5's claim that governance turns one dial and the economy responds. Watching ρ move is the demonstration. |
| **The world** | Four charts plus the comparison bar. | Disparity is the headline claim. Participation is the adoption question. The histogram makes "who actually gets what" concrete. |
| **Comparison bar** | Aequitas against the real US distribution. **The figure always carries the floor it assumed** — `24/F` is 2.40× at 10 h and 6.00× at 4 h. | **The one visual that lands in three seconds.** Not a second simulation — the real SCF 2022 plus Forbes distribution already in `disparity_ceiling_sim.py`, material-only, labelled as such on screen. |
| **Conformance rail** | The §9 invariants, live. | See Decision 3. |
| **Inspector** | Click any agent: derived standing **and their actual event log**. | **This is what makes A6 real instead of a slogan.** The reader sees that the balance is not stored anywhere — it is those rows, added up. |
| **Transport** | Play, pause, step, scrub, speed. | See below. |

### The scrubber is exact, and that falls out of the architecture

**Dragging back to period 12 does not undo anything. It re-derives.** The log is append-only and the ledger is a pure function of it (A6), so any past state recomputes exactly rather than approximately.

**So the time control is not a convenience feature. It is A6 made visible**, and it is worth a one-line note on screen the first time someone drags it.

---

## 3. The scenario file

```json
{
  "name": "Locality vs money, 20 years",
  "seed": 7,
  "periods": 240,
  "population": { "n": 5000, "growth_per_period": 0.0 },
  "dials": {
    "rho": 1.20,
    "floor_h": 10.0,
    "method": "US",
    "verification_cost": 0.10
  },
  "economy": { "plug": "toy" },
  "outside":  { "plug": "money" },
  "behaviour": { "join": "compare_position", "consume": "want_capped" },
  "shocks": [ { "at": 120, "target": "economy.budget", "multiply": 0.70 } ],
  "record": ["disparity", "participation", "median_real", "coverage"]
}
```

**Rules for the format, and they are the reason it will still work in a year:**

- **Every dial in §1b of the roadmap appears here, and nothing appears here that is not a dial.** A rule never becomes a setting.
- **A shock is `at` + `target` + an operation.** One shape covers a disaster, a population change, a pollutant discovered late, and an efficiency shift. **If a scenario needs a new shock *shape*, that is a design finding worth writing down.**
- **`seed` is mandatory.** A scenario that cannot be reproduced exactly is not a scenario.
- **Unknown keys are an error, never ignored.** Silent acceptance of a typo is how a scenario quietly stops testing what its author thought.

---

## 4. What ships in version 1, and what does not

**Ship a small honest thing that runs, then grow it.**

| In v1 | Out of v1 |
|---|---|
| The time axis (roadmap step 2) | The real EXIOBASE trade-and-production data (step 5) |
| Four charts and the comparison bar | Multiple networks with different dials |
| The conformance rail, all checks | An editor for behaviour policies |
| The agent inspector with its real event log | Pollutant stocks with remediation baselines |
| Dials: ρ, `F`, method, N | Verification cost as a live dial |
| Shocks: multiply a budget at period *t* | The adoption question, which needs the outside-world plug |
| Share by link, save and load a file | |
| Toy economy only | |

**The adoption question is the most interesting thing this will ever show, and it is deliberately not in v1.** It needs the behaviour layer and the outside-world plug, which are roadmap steps 3 and 4. **Putting it in v1 means shipping nothing for two months.**

---

## 5. Build order

**Prove the pipeline before building any interface.**

| Phase | What | Done when |
|---|---|---|
| **0** | **This document.** | The author signs it off or changes it. |
| **1** | **The time axis in the kernel.** Headless, CLI, no screen. | A ten-period run holds every §9 invariant and the bound stays at `24/F` for whatever floor the scenario set. |
| **2** | **The scenario file.** Loader, validator, `run_scenario.py`. | Any of the author's eight example conditions is expressible **with no new code**. This is the acceptance test for the whole design. |
| **3** | **The browser shell.** Pyodide loads the real `statera.py`, runs one scenario, draws **one** chart, play and pause. Nothing else. | The same scenario file gives byte-identical numbers in the page and on the CLI. |
| **4** | **The full screen.** Everything in §2. | A stranger opens it and runs a scenario without being told how. |
| **5** | **Publish.** GitHub Pages, share-by-link, a README a stranger can follow. | The agent posts a link and someone who is not us runs it. |

> **Phase 3 is the risky one and it is deliberately tiny.** If Pyodide cannot load the real kernel and match the CLI exactly, that is discovered in a day, before any interface work exists to throw away.

---

## 6. What the agent can ask for, once this exists

Three asks it cannot make today.

1. **"Open this link and tell me what breaks."** No clone, no install, no running a stranger's code. **The objection it already conceded stops applying.**
2. **"Name a starting condition this cannot express."** A design hole is worth more than a reproduction, and it costs the stranger nothing but thought. **This is the most valuable request available to it.**
3. **"Here a conformance light goes red. Is that a bug in my code or a hole in the theory?"** A genuinely open question, handed over with a link that shows it happening.

---

## 7. Design rules for the screen itself

The author has ADHD and a long day is the normal case. **These are constraints, not preferences.**

- **One screen.** No navigation, no tabs, no modal in the main loop.
- **Every dial shows its number, always.** A slider with no number is a guess.
- **Colour is never the only signal.** Every conformance light carries its name and its state as text.
- **Nothing animates except the simulation.** No transitions, no easing, no decorative motion.
- **A failure says what failed, which requirement, and at which event** — never "something went wrong."
- **The first thing on screen is a running scenario**, not an empty state asking the reader to configure something.

---

## 8. Risks

| Risk | What we do |
|---|---|
| **Pyodide is slow or will not load the kernel** | Phase 3 is one chart and finds out in a day, before any UI exists. |
| **The GUI grows a rule of its own** | The hard rule in Decision 1, plus a test: **the browser and the CLI must produce identical numbers from the same scenario file.** If they ever diverge, the GUI has grown a rule. |
| **This turns into a product** | §1.2. It is an instrument for testing a theory. **It is not a first version of Aequitas**, and the moment it is treated as one, the scope ruling has been breached again. |
| **Scenario sprawl** | A scenario earns its place by naming which axiom, mechanism, or open problem it could falsify. One that cannot fail interestingly is a demo. |
| **The 15 MB first load loses readers** | A real loading state that says what is happening, aggressive caching, and a static screenshot in the README for people who will not wait. |

---

## 9. Author's calls

### ✅ Settled 2026-08-23 — v1 ships without the adoption question

**§4 stands as written.** v1 is the time axis, four charts, the conformance rail, the agent inspector, the dials, one shock shape, share-by-link, and a toy economy. **Adoption — a locality competing with money — is v2**, because it needs the behaviour layer and the outside-world plug, and waiting for it means shipping nothing for about two months.

**What v1 can still show, so this is not a thin thing:** the ceiling holding while ρ moves, a disaster landing at period 120 and the floor absorbing it, a population shift, and every conformance requirement checking itself in public.

### Proceeding on these two unless the author says otherwise

1. **Name: *Aequitas Lab*.** Foundations §4.8 already calls trust networks **laboratories rather than banks**, so the name is doing a small amount of real work. *Aequitas Simulator* remains available and is duller.
2. **Keep the static money-comparison bar in v1.** It is **real data** — SCF 2022 plus Forbes, material-only, the same distribution `q4_locked_ledgers.py` already uses — drawn beside the simulated result and **labelled on screen as a real distribution rather than a simulated one.** Simulating a money economy properly is v2 work, and dropping the bar entirely costs the one visual that lands in three seconds.

---

## 10. Sign-off

| | |
|---|---|
| **Design** | Written 2026-08-23 |
| **Scope of v1** | ✅ Settled by the author, 2026-08-23 |
| **Name and money bar** | Proceeding on the recommendations above |
| **Phase 1** | **Unblocked. Not started — awaiting the author's word to begin.** |
