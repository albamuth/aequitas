# Debit Tolerance

> **Version:** 0.1
> **Date:** 2026-09-16

> **A trust network lets a person consume while `D ≤ ρ·C`. That is the consumption gate, and it has two dials: the floor `F`, and the tolerance ρ.** The floor is credit for work a person really did. It is not an allowance, and nothing is issued to anybody.

## The words this page uses

| Term | What it means |
|---|---|
| **`C`** | A person's credit — every hour of their life the books have recorded as work |
| **`D`** | A person's debit — what their consumption is currently reckoned to cost, in hours |
| **The gate** | `D ≤ ρ·C`, checked at the moment of each transaction |
| **`F`**, the floor | The hours a day a network counts as the work of keeping a human being alive |
| **ρ** ("rho"), the tolerance | The multiplier in the gate. At ρ = 1.2 a person may carry debit up to 1.2 times their recorded credit |
| **`E`** | What a year of essentials commands, in hours of other people's labour |
| **IC-7** | The integrity check that stops any account claiming more than 24 hours of activity in 24 hours |

**Both `F` and ρ are each network's own settings. Aequitas uses them and never sets them (A8).**

## What it is

**Three parts, and the first one is the one most often got wrong.**

1. **The floor is credit, not unbacked room.** Sleeping, eating, washing and bodily upkeep are activities a network may recognise as work. Where it recognises them, those hours credit at one hour for one hour, like any other recognised hours. **The evidence is proof of life, which is the strongest evidence in the system and costs almost nothing to check.**
2. **The gate is a ratio, never a balance.** `C` and `D` both only ever rise. A purchase adds to `D` and takes nothing from `C`, because credit is not a currency and never moves ([non-fungibility](non-fungibility.md), A3). **There is no stored lump to draw down and nothing to run out of.**
3. **A restriction reaches non-essentials only.** Where a person's standing does restrict them, essentials still flow. That backstop exists for measurement error, not for poverty. **And the provider is never made to means-test**: a counsellor is credited for the hours they worked, because credit is decided by the network's published evidence rule and never by the recipient's standing ([service-credit](service-credit.md)).

## Why the floor could never have been an allowance

**Credit records that a person spent time on work (A2).** Handing somebody credit for no time worked would be an abstract, issued quantity, **and A1 forbids those anywhere in the system.** So a floor written as a grant would have broken the first axiom.

> **Every living human really does spend those hours. The floor credits them at the ordinary rate, and that is the whole of the derivation.**

**What a network chooses is which activities it recognises and how many hours each takes.** One network counts eight hours of sleep and lands near 10 h/day. Another accepts that four hours suffices and lands near 6. A fourth counts only the hours a body cannot avoid and lands near 2. The sleep evidence a network argues from is public — the [AASM and SRS consensus statement](https://aasm.org/aasm-and-srs-publish-new-sleep-duration-consensus-statement/) says adults aged 18 to 60 should sleep 7 or more hours a night.

**What no network chooses is the rule underneath: time spent on recognised work credits one hour for one hour.**

### An example, with the numbers

**A network at `F` = 10 h/day and ρ = 1.2. Two people, both aged 40.** A median lifestyle commands about **1,380 hours** of other people's labour a year.

| | Credit `C` | Debit `D` | `D ÷ C` | Room left, `ρ·C − D` |
|---|--:|--:|--:|--:|
| **A — stays alive, and works 1,000 h a year** | 40 × (3,650 + 1,000) = **186,000 h** | 40 × 1,380 = **55,200 h** | **0.30** | **168,000 h** |
| **B — stays alive, works nothing, consumes the same** | 40 × 3,650 = **146,000 h** | **55,200 h** | **0.38** | **120,000 h** |

**In plain words: neither person's numbers ever went down, and both sit far inside the gate.** A's extra work did not cancel A's consumption. It widened the gap between two figures that both only grow.

## The floor has a bound at each end, and the band has been measured

**Set `F` too low and people cannot afford what they need. Set it too high and the books stop rationing anything.**

**The lower bound is arithmetic:** `ρ · F · 365 ≥ E`. **Worked at `E` = 700 h/year and ρ = 1.2:**

| | |
|---|---|
| Minimum floor | 700 ÷ (1.2 × 365) = **1.6 h/day** |
| At `F` = 2 h/day, room a year | 1.2 × 2 × 365 = **876 h** — covers 700 h of essentials |
| At `F` = 1 h/day, room a year | 1.2 × 1 × 365 = **438 h** — **short by 262 h** |

**In plain words: a network at `F` = 1 h/day has subscribers who cannot afford to eat, and that network fails.**

**The upper bound was run on 2026-08-28**, sweeping `F` from 1 to 14 hours a day. `E_max` below is the largest essentials basket a floor can carry, `365 · F · ρ*(F)`.

| `F` | ρ*(`F`) | `E_max` | As a multiple of a median American lifestyle |
|---|--:|--:|---|
| **2 h/day** | 3.70 | 2,701 h/yr | **1.96×** — the tightest floor measured |
| 10 h/day | 1.20 | 4,380 h/yr | 3.17× |
| 14 h/day | 0.90 | 4,599 h/yr | 3.33× |

**In plain words: the band exists at every floor from 1 to 14 hours a day and never closes.** What binds it is what an economy can physically deliver, not whether essentials are affordable. **The upper edge turns out to be an artefact of the American production method** — the same material standard costs 1,380 hours by the American method, 883 by the German or Japanese, and 759 by the Spanish.

> **⚠️ ρ\*'s absolute values inherit the weighting model and an illustrative capacity figure. The shape is the result; the numbers are dated readings.** Full method: `06-simulation/stable-band/RESULTS.md`.

## The floor is also the error tolerance of the accounting

**Two separate things make essentials reachable, and they are usually confused.**

| | What it does |
|---|---|
| **The floor's own arithmetic** | A person's credit for staying alive is sized to cover what staying alive costs. **Nobody is assessed, nobody applies, and nobody decides they qualify** |
| **The backstop** | Where a restriction arises from a person's standing, it reaches non-essentials only |

**The backstop exists because of measurement error.** A producer over-assigned for years would suffer real harm before the record was corrected — the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). **It caps that exposure at restricted non-essential consumption for a period, followed by correction**, and it applies on the same terms to somebody found to have committed fraud.

**The floor does not require anybody to spend it on essentials.** A person may put their room toward anything. **The guarantee is that they can afford what they need, not that they must buy it.**

> **This is not a conformance requirement and must not be written as one.** Whether essentials are actually affordable depends on `F`, on ρ, and on what the economy can deliver. **It is a result a network achieves, not a property an implementation has.**

## Who games this

**Tolerance farming.** If every account carries a floor, the exploit is fake or marginal accounts harvesting it. **One verified human holds one account, and how a network achieves that is its own design** ([verification-ladder](verification-ladder.md), C6).

**The arithmetic refuses the hardest case on its own.** Two identical twins on the lowest rung of checking, deliberately engineering the confusion, reach **34 hours a day against 36 hours honest**, because IC-7 caps each account at 24 hours of activity in 24 hours. **They lose 730 hours a year and gain nothing**, since twins sharing a household share the goods either way.

**Floor-shopping** — joining the network with the most generous floor — **is arrested by the seller choosing which network a transaction lands on.** A network with an implausible floor loses sellers, and a generous floor cannot be exported, because a counterparty re-computes the backing through its own model.

**Hoarding does not beat the gate either.** Holding a thing raises your own debit, and food, fuel and heat are used up when used, so their debit is permanent and buys no holding. **The only way to the wall is to work 24 hours a day for a whole life.**

## Depends on

- [consumption-debit](consumption-debit.md)
- [production-credit](production-credit.md)
- [service-credit](service-credit.md) — self-continuance passes the gate as a service done for oneself
- [verification-ladder](verification-ladder.md) — proof of life is what the floor is evidenced by
- [statistical-coverage](statistical-coverage.md)

## Consequences

- [no-taxation](no-taxation.md) — no redistribution is needed; the floor is structural
- [disparity-ceiling](disparity-ceiling.md) — the ratio between the largest and smallest credit per day lived is `24 ÷ F`, so **the tighter the floor, the wider the stated ceiling**
- [pledge-and-signal](pledge-and-signal.md) — the floor is credit, and all credit generates pledging power, so every living person directs some share of what gets made next

## Open questions

- **OP-4 — the tolerance formula.** `F` and ρ are still parameterised. The band was measured; the formula was not derived. (C9, not started)
- **The childhood dial belongs with OP-4.** Whether a network credits a child's learning time moves the reachable ceiling, and it was not written down before 2026-09-12.
- **Who defines "essential"?** The network publishes its own list of recognised activities and their durations (A8). **Unassigned beyond that.**

---
*Status: provisional — OP-4*
*Source: `00-strategy/Aequitas_Foundations.md` §3.0 (the gate), §5.5.1 (what the floor is), §5.5.2 (why it is not an allowance), §5.5.3 (the band), §5.5.4 (the error tolerance), §5.5.6 (why hoarding does not beat it)*
