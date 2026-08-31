# Disparity Ceiling

> **Result (conditional):** **inside one trust network's own books**, the maximum sustainable **consumption** disparity is **`24 / F`** — the length of a day divided by that network's self-care floor *F* (hours/day) — independent of the tolerance dial ρ and of the weighting model. At *F* = 10 h that is **2.4×**. Under money the same ratio runs to **~10⁶×** and compounds without limit.

**Two limits belong in the same breath as the number.**

**It is a wall nobody reaches.** 2.4× needs 24 credited hours every day from birth to death. **A very hard working life — 12 hours of work a day, 300 days a year, from 20 to 70 — reaches about 1.62×** ([[basic-needs-floor|§5.5.5]]). **Quote 1.6, not 2.4.**

**It bounds; it does not witness.** The bound does not move under fraud **because the arithmetic never reads the accounts** — `24/F` returns 2.40 whatever the population contains. **That is robustness for the bound and blindness for the detector, and one sentence cannot claim both.** Coverage is established by a different and physical instrument: the outside total `N` of [[statistical-coverage|§4.4]]. *(Found from outside by @cairn-lineage, c33046, conceded 2026-08-31. The general rule was already ours — a check that compares a thing to itself can find a mistake, and cannot find a hole.)*

**Formal statement + plain-language explainer:** [`06-simulation/disparity-ceiling/DISPARITY_CEILING.md`](../06-simulation/disparity-ceiling/DISPARITY_CEILING.md). **Simulation** (7 self-tests green): [`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`](../06-simulation/disparity-ceiling/disparity_ceiling_sim.py).

## The proof — three axioms doing three jobs

A person's sustainable consumption allowance is `ρ · c`, where `c` is their credit *rate* in hours/day. The bound is the ratio of the largest such allowance to the smallest:

- **Upper end `c ≤ 24`** — nobody can be credited for time they don't have. That's [IC-7](distributed-auditing.md), the 24-hour cap, and it holds *even for a fraudster*, who still only has 24 hours in a day.
- **Lower end `c ≥ F`** — staying alive is credited work ([[basic-needs-floor|§5.5]] self-care floor), so nobody sits at zero.
- **No stacking** — [A3](non-fungibility.md): credit can't be transferred, pooled, lent, inherited, or compounded. This is what makes the bound `24/F` rather than `24·k/F`; one account can't absorb others' hours.

So the top consumes `ρ·24`, the bottom `ρ·F`, and the ratio is **`(ρ·24)/(ρ·F) = 24/F`**. The **ρ cancels** (it scales both ends equally), and the weighting model cancels too (same hours-unit both ends, A2). The bound depends on *neither* — so it does **not** rest on [[weighting-governance|OP-10]].

## Why hoarding can't beat it (credit is not a currency)

Credit and debit are **cumulative running tallies** derived from the event log ([A6](event-record.md): the ledger is *derived, not stored*). **Credit is never *spent*** — a purchase adds to your *debit*, it never draws your credit down. The rule checked at each purchase is a **ratio**: total debit ≤ ρ × total credit; a purchase that would breach it is blocked.

So there is nothing to "bank and blow." A lifelong hoarder who consumes nothing then splurges is **clipped to their own `ρ·C`** — front-loading rearranges *when* they consume, never *how much*. At **equal age**, two people's cumulative credits stand in ratio ≤ 24/F, so cumulative-consumption disparity is bounded by 24/F too. The only spread beyond it is **age** — time lived, not class, and everyone traverses it.

*(This is the resolution of the "Methuselah" objection from the stress test. It needs no special "rate gate" — it is just A3 + A6.)*

## Stress test (2026-08-14) → PASSES

| Attack | Resolution |
|---|---|
| **Methuselah hoarder** — bank a lifetime, splurge it | Credit is a record, not a balance (above). A splurge can't exceed your own `ρ·C`. |
| **Dynasty / household** — pool N people into one mansion | A household is a co-op: its dwelling-debt splits per occupant by dwelling-time (children included, §4.5). The bound is **per-person**; inheritance *dilutes* the load each generation. One member dominating the rest is coercion ([[service-to-influence|OP-1]]), not accounting. |
| **Collector** — hoard houses, gold, art | Holdings are a **burden**, not income ([property-debit](property-debit.md)): they raise your *own* debit against a fixed credit, so a hoard self-bounds. |

**Coupled to the pledge ruling:** the one channel that could have breached A3 — a *transferable pledged surplus* — was closed by making pledge surplus a non-consumable [contingent reserve](pledge-and-signal.md) (§4.6). The disparity ceiling and permanent-pledges are one mechanism.

## Why it matters

1. **It bounds what cheating is worth, and it does not detect cheating.** "How much does undetected cheating get you?" — answer: never past 24/F, because IC-7 caps everyone at 24 h. **Fraud fills the band and cannot create an outlier beyond it. It also leaves the figure completely unchanged, so the figure can never tell you the fraud happened.** Both halves are the same property, and the second must be said whenever the first is.
2. **It is the honest reply to "your system can be gamed."** Yes — and money can be gamed far more profitably and entirely legally (real data: money's richest-to-median runs to ~10⁶×).
3. **It rests on axioms, not enforcement.** The bound is arithmetic on IC-7, the floor, and A3 — no institution sets it.

## Conditional, not absolute

- **Consumption axis only.** Influence (pledging-power → agenda-setting) is [[service-to-influence|OP-1]], a separate question.
- **One network's books, and there is no wider figure.** Networks do not trade with each other and no book is ever added to another, so **there is no object for a cross-network bound to describe.**

  > <!-- struck-ok: this note exists to record the withdrawal, so it must quote the withdrawn wording -->
  > **⛔ Struck 2026-08-25.** This page used to say a *"cross-network guarantee"* was available once OP-22 was solved, and the core documents used to claim the bound held *"across any set of networks compatible enough to interoperate"* with compatible networks *"arriving at the same ledger."* **All of that is removed, not narrowed.** Foundations §4.2 says the opposite on purpose — *comparison, never conversion*: one person, one Monday, 8 hours worked reads as **12** credited hours on a 4-hour-floor network and **18** on a 10-hour-floor one, **and both are correct.** Record: Objections §OA9. **What survives across networks is a coverage question, not a disparity one.**

- **`2.4×` is illustrative.** The real result is the *form* `24/F` — [A8](protocol-governance.md) forbids a global floor, so there is no single headline constant. **A 2-hour floor states a 12× ceiling.**
- **Two more dials sit on the number.** Whether the network credits a child's learning time (2.400× if it does, **2.085×** if it does not), and whether collusive hand-offs can manufacture gross hours ([[service-to-influence|OP-1]], assumed controlled).

## Depends on

- [non-fungibility](non-fungibility.md) · [cost-not-price](cost-not-price.md) · [property-debit](property-debit.md) · [distributed-auditing](distributed-auditing.md) · [[basic-needs-floor]] · [event-record](event-record.md)

## Consequences

- [honest-advantage](honest-advantage.md) — low fraud upside plus high honest return is the whole security model

---
*Status: conditional result (consumption axis; conditional on OP-22 + narrow-band floor). Formally stated, simulated (7 tests), and stress-tested → PASSES 2026-08-14. Folded into Foundations v0.15 §5.5 / Objections v0.16 §C test 8.*
*Source: design session 2026-07-31 · formal statement `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`*
