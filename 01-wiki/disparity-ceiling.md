# Disparity Ceiling

> **Version:** 0.2
> **Date:** 2026-09-18

> **Result (conditional):** **inside one trust network's own books**, the maximum disparity in **lifetime pledge budget per day lived** is **`24 / F`** — the length of a day divided by that network's self-care floor *F* (hours/day) — independent of the tolerance dial ρ and of the weighting model. At *F* = 10 h that is **2.4×**. Under money the same lever runs to **~10⁶×** and compounds without limit.

> **⚠️ Restated 2026-09-18. It bounds the say over what gets made. It does not bound consumption.**
>
> A pledge budget is credit the holder earned and nothing else, so `24/F` follows from IC-7 and the floor. **Consumption is gated by `D ≤ ρ·(C + P)`, where `P` is room others pledged to a person by name — and `P` has no per-account limit.** Somebody widely backed can consume far beyond `24/F` times a floor-only life, and Aequitas does not prevent it.
>
> **The only limit on `P` is the population.** Committed room across a network can never exceed the credit its subscribers earned. **That bounds the sum and not one person's share.**
>
> **Why this is still not capitalism's kind of wealth.** Pledged room **cannot be lent at interest, rented out, charged for, or used to hire anybody** — credit never moves ([non-fungibility](non-fungibility.md)), nothing may be added to a cost figure ([cost-not-price](cost-not-price.md)), and working on your own property raises its debit by the hours it credits. **Property under capitalism is a machine for getting more. Pledged room lets you hold and consume.**

**Two limits belong in the same breath as the number.**

**It is a wall nobody reaches.** 2.4× needs 24 credited hours every day from birth to death. **A very hard working life — 12 hours of work a day, 300 days a year, from 20 to 70 — reaches about 1.62×** ([[basic-needs-floor|§5.5.5]]). **Quote 1.6, not 2.4.**

**It is a ratio of daily rates, not of lifetime totals.** A lifetime total carries the person's age inside it, so two accounts of different ages read wider and nothing is wrong. **A 60-year maximum worker against a 20-year floor-only person is 7.20× on lifetime totals and 2.40× per day lived.** Divide each account's credit by its own days lived before taking the ratio.

**It bounds; it does not witness.** The bound does not move under fraud **because the arithmetic never reads the accounts** — `24/F` returns 2.40 whatever the population contains. **That is robustness for the bound and blindness for the detector, and one sentence cannot claim both.** Coverage is established by a different and physical instrument: the outside total `N` of [[statistical-coverage|§4.4]]. *(Found from outside by @cairn-lineage, c33046, conceded 2026-08-31. The general rule was already ours — a check that compares a thing to itself can find a mistake, and cannot find a hole.)*

**Formal statement + plain-language explainer:** [`06-simulation/disparity-ceiling/DISPARITY_CEILING.md`](../06-simulation/disparity-ceiling/DISPARITY_CEILING.md). **Simulation** (7 self-tests green): [`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`](../06-simulation/disparity-ceiling/disparity_ceiling_sim.py).

## The proof — three axioms doing three jobs

A person's **pledge budget per day lived** is their credit *rate* `c`, in hours a day, because a budget is credit the holder earned and nothing else. The bound is the ratio of the largest such rate to the smallest:

- **Upper end `c ≤ 24`** — nobody can be credited for time they don't have. That's [IC-7](distributed-auditing.md), the 24-hour cap, and it holds *even for a fraudster*, who still only has 24 hours in a day.
- **Lower end `c ≥ F`** — staying alive is credited work ([[basic-needs-floor|§5.5]] self-care floor), so nobody sits at zero.
- **No stacking** — [A3](non-fungibility.md): credit can't be transferred, pooled, lent, inherited, or compounded. This is what makes the bound `24/F` rather than `24·k/F`; one account can't absorb others' hours.

So the top budget is `24` and the bottom is `F`, and the ratio is **`24/F`**. **ρ does not appear at all**, because ρ is a dial on consumption and a budget is not consumption. The weighting model does not appear either, because a budget is counted in hours worked. The bound depends on *neither* — so it does **not** rest on [[weighting-governance|OP-10]].

> **⚠️ Corrected 2026-09-21.** <!-- struck-ok: names the withdrawn derivation in order to correct it --> These two paragraphs read *"A person's sustainable consumption allowance is `ρ · c`… So the top consumes `ρ·24`, the bottom `ρ·F`, and the ratio is `(ρ·24)/(ρ·F) = 24/F`."* **That silently sets `P` = 0 for both people.** This page's header was restated on 2026-09-18 and **its derivation was not**, so the summary said pledge budgets while the proof still worked in consumption.

## Why hoarding can't beat it (credit is not a currency)

Credit and debit are **cumulative running tallies** derived from the event log ([A6](event-record.md): the ledger is *derived, not stored*). **Credit is never *spent*** — a purchase adds to your *debit*, it never draws your credit down. The rule checked at each purchase is a **ratio**: total debit ≤ ρ × total credit; a purchase that would breach it is blocked.

So there is nothing to "bank and blow." A lifelong hoarder who consumes nothing then splurges is **clipped to their own `ρ·(C + P)`** — front-loading rearranges *when* they consume, never *how much*. At **equal age**, two people's cumulative credits stand in ratio ≤ 24/F, **and so do their pledge budgets.** The only spread beyond it is **age** — time lived, not class, and everyone traverses it.

> **⚠️ It does not follow that their consumption stands in the same ratio.** Two people of equal credit consume very differently if one has been pledged to and the other has not.

*(This is the resolution of the "Methuselah" objection from the stress test. It needs no special "rate gate" — it is just A3 + A6.)*

## Stress test (2026-08-14) → PASSES

| Attack | Resolution |
|---|---|
| **Methuselah hoarder** — bank a lifetime, splurge it | Credit is a record, not a balance (above). A splurge can't exceed your own `ρ·(C + P)`. |
| **Dynasty / household** — pool N people into one mansion | **Re-answered 2026-09-18.** A pledge budget is credit the holder earned, so **room received never enlarges what anybody can pledge**, and committed room is **not transferable**, so it does not pass on death. A dynasty cannot compound. *(The old reason — dwelling debt splitting per occupant, children included — is withdrawn: a child cannot consent to a property transfer.)* One member dominating the rest is coercion ([[service-to-influence|OP-1]]), and is the legal system's problem. |
| **Collector** — hoard houses, gold, art | Holdings are a **burden**, not income ([property-debit](property-debit.md)): they raise your *own* debit against a fixed credit, so a hoard self-bounds. |

> **⚠️ The channel this page used to say was closed is open, by ruling.** It read: *the one channel that could have breached A3 — a transferable pledged surplus — was closed by making pledge surplus a non-consumable contingent reserve.* **The reserve was withdrawn on 2026-09-18 and committed room is consumable** ([pledge-and-signal](pledge-and-signal.md)).
>
> **A3 is not breached.** No credit moves, and a pledge is not a transfer of credit — it is a one-way, non-refundable grant of room, spent from a budget that cannot be manufactured. **What changed is that the ceiling is now stated over budgets rather than over consumption**, which is where the arithmetic actually holds.

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
*Status: conditional result (**pledge-budget axis**; conditional on OP-22 + narrow-band floor). Formally stated, simulated (7 tests), and stress-tested → PASSES 2026-08-14. Folded into Foundations §5.5 / Objections §C test 8.*
*Source: `00-strategy/Aequitas_Foundations.md` §5.5.5 (the ceiling and its four conditions), §5.5.6 (why hoarding does not beat it) · design session 2026-07-31 · formal statement `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`*
