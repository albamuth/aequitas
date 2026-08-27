# Disparity Ceiling

> **Result (conditional):** the maximum sustainable **consumption** disparity under Aequitas is **`24 / F`** — the length of a day divided by the network's self-care floor *F* (hours/day) — independent of the tolerance dial ρ and of the weighting model, and **invariant to fraud**. At *F* = 10 h that is **2.4×**. Under money the same ratio runs to **~10⁶×** and compounds without limit.

This is the **strongest defensive result the project holds**, because it makes fraud-resistance a *structural* property rather than a policing problem: the question stops being "can we catch all cheating?" and becomes "how much does undetected cheating actually get you?" — which has a stable answer.

**Formal statement + plain-language explainer:** [`06-simulation/disparity-ceiling/DISPARITY_CEILING.md`](../06-simulation/disparity-ceiling/DISPARITY_CEILING.md). **Simulation** (7 self-tests green): [`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`](../06-simulation/disparity-ceiling/disparity_ceiling_sim.py).

## The proof — three axioms doing three jobs

A person's sustainable consumption allowance is `ρ · c`, where `c` is their credit *rate* in hours/day. The bound is the ratio of the largest such allowance to the smallest:

- **Upper end `c ≤ 24`** — nobody can be credited for time they don't have. That's [[distributed-auditing|IC-7]], the 24-hour cap, and it holds *even for a fraudster*, who still only has 24 hours in a day.
- **Lower end `c ≥ F`** — staying alive is credited work ([[basic-needs-floor|§5.5]] self-care floor), so nobody sits at zero.
- **No stacking** — [[non-fungibility|A3]]: credit can't be transferred, pooled, lent, inherited, or compounded. This is what makes the bound `24/F` rather than `24·k/F`; one account can't absorb others' hours.

So the top consumes `ρ·24`, the bottom `ρ·F`, and the ratio is **`(ρ·24)/(ρ·F) = 24/F`**. The **ρ cancels** (it scales both ends equally), and the weighting model cancels too (same hours-unit both ends, A2). The bound depends on *neither* — so it does **not** rest on [[weighting-governance|OP-10]].

## Why hoarding can't beat it (credit is not a currency)

Credit and debit are **cumulative running tallies** derived from the event log ([[event-record|A6]]: the ledger is *derived, not stored*). **Credit is never *spent*** — a purchase adds to your *debit*, it never draws your credit down. The rule checked at each purchase is a **ratio**: total debit ≤ ρ × total credit; a purchase that would breach it is blocked.

So there is nothing to "bank and blow." A lifelong hoarder who consumes nothing then splurges is **clipped to their own `ρ·C`** — front-loading rearranges *when* they consume, never *how much*. At **equal age**, two people's cumulative credits stand in ratio ≤ 24/F, so cumulative-consumption disparity is bounded by 24/F too. The only spread beyond it is **age** — time lived, not class, and everyone traverses it.

*(This is the resolution of the "Methuselah" objection from the stress test. It needs no special "rate gate" — it is just A3 + A6.)*

## Stress test (2026-08-14) → PASSES

| Attack | Resolution |
|---|---|
| **Methuselah hoarder** — bank a lifetime, splurge it | Credit is a record, not a balance (above). A splurge can't exceed your own `ρ·C`. |
| **Dynasty / household** — pool N people into one mansion | A household is a co-op: its dwelling-debt splits per occupant by dwelling-time (children included, §4.5). The bound is **per-person**; inheritance *dilutes* the load each generation. One member dominating the rest is coercion ([[service-to-influence|OP-1]]), not accounting. |
| **Collector** — hoard houses, gold, art | Holdings are a **burden**, not income ([[property-debit]]): they raise your *own* debit against a fixed credit, so a hoard self-bounds. |

**Coupled to the pledge ruling:** the one channel that could have breached A3 — a *transferable pledged surplus* — was closed by making pledge surplus a non-consumable [[pledge-and-signal|contingent reserve]] (§4.6). The disparity ceiling and permanent-pledges are one mechanism.

## Why it matters

1. **It reframes security.** "How much does undetected cheating get you?" — answer: never past 24/F. Fraud fills the band (IC-7 caps everyone at 24 h), it can't create an outlier beyond it.
2. **It is the honest reply to "your system can be gamed."** Yes — and money can be gamed far more profitably and entirely legally (real data: money's richest-to-median runs to ~10⁶×).
3. **It rests on axioms, not enforcement.** The bound is arithmetic on IC-7, the floor, and A3 — no institution sets it.

## Conditional, not absolute

- **Consumption axis only.** Influence (pledging-power → agenda-setting) is [[service-to-influence|OP-1]], a separate question.
- **Cross-network guarantee depends on [[weighting-governance|OP-22]]** — proving a claim's backing without exposing the private ledger — plus a narrow-band floor. Within one network the bound is exact; across networks it needs the disclosure mechanism.
- **`2.4×` is illustrative.** The real result is the *form* `24/F` — [[local-governance|A8]] forbids a global floor, so there is no single headline constant.

## Depends on

- [[non-fungibility]] · [[cost-not-price]] · [[property-debit]] · [[distributed-auditing]] · [[basic-needs-floor]] · [[event-record]]

## Consequences

- [[honest-advantage]] — low fraud upside plus high honest return is the whole security model

---
*Status: conditional result (consumption axis; conditional on OP-22 + narrow-band floor). Formally stated, simulated (7 tests), and stress-tested → PASSES 2026-08-14. Folded into Foundations v0.15 §5.5 / Objections v0.16 §C test 8.*
*Source: design session 2026-07-31 · formal statement `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`*
