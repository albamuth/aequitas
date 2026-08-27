# Pledge and Signal

> The two ways credit-earners direct what gets made next. A **pledge** is a *permanent, non-revocable grant of debit-room*, spent from a lifetime allowance equal to earned credit; a **signal** is a free, unbacked "I want this." Together they are the demand side of the economy — with no prices, no planner, and no board.

Aequitas keeps **cost** and **demand** strictly separate (see [material-flow-value](material-flow-value.md)): cost measures what a thing took; pledges and signals reveal who wants it. This page is the demand side.

## Pledge vs. signal

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I put an hour of my credit behind making this happen" | "I want this to exist" |
| Backed by | your earned credit, **1:1** | nothing |
| How much | exactly one hour pledged per hour worked | plenty — signal freely |
| Familiar as | a wishlist that funds; choosing your GP; crowdfunding; commissioning a job | likes, reviews, applause |

**Why pledges are 1:1 and signals are plentiful:** the credit you put behind things can never exceed the credit you earned, or people would back work with room that isn't really there ([IC-8](event-record.md)). Signals carry no such constraint, so they should be abundant — they reveal your *whole* preference ordering, not just the top slice a scarce pledge can express.

## What a pledge actually is *(Foundations v0.14 — pledges made permanent)*

A pledge is **not** a purchase, **not** a spend of your credit, and **not** a promise to buy. It is a **permanent, non-revocable grant of debit-room**:

- **Your credit stays yours, but a separate allowance is spent.** A pledge puts credit *behind* something — like naming a beneficiary, not handing over your balance. What it spends is *pledging-power* — a **lifetime budget equal to your earned credit, drawn down once**. A pledged hour is gone from that budget for good.
- **To the receiver it is virtual credit.** It expands the receiving person's or co-op's [debit-room](debit-tolerance.md) so a fixed cost bites less. The debit itself does not move to the pledger and does not vanish — it stays where it was incurred (e.g. holding-time-split on a facility's holders, [debit-taxonomy](debit-taxonomy.md) §4.5); the pledge only *cushions* the bite.
- **It is permanent — you can't take it back.** The receiver can rely on the granted room and get on with the work; it won't vanish under them. The discipline is *at pledge time* — because a pledge is a real, one-time expense, nobody pledges frivolously or floods the system for free. An unspent pledge to an abandoned task is **burned**, not returned.
- **Buying is a separate act.** Where pledged work yields a held object, taking that object loads its [property-debit](property-debit.md) on **whoever accepts possession** (§3.2) — pledge or no pledge, and not necessarily the pledger.

**A pledge need not involve an object at all.** Pledge two hours toward mowing a public verge; someone mows for an hour, shows proof, and earns an hour of credit — no object changed hands, no debit moved. A pledge simply **summons creditable work into being**.

## The contingent reserve — over-pledging dangerous work

When a task attracts **more pledged hours than it costs**, the surplus is **not** a bonus to the doer and **not** spendable — that would be profit ([cost-not-price](cost-not-price.md)) and would let someone concentrate consumption. Instead it becomes a **contingent reserve**: earmarked, non-spendable room that pays out **only against a verified future cost caused by the task** — the doer's later injury or illness, a site's remediation resurfacing, third-party harm.

- **Split by hours *on the task*** — the cover reaches whoever did *this* work, not whoever's been a co-op member longest.
- **Causation by physical-trace** — a claim draws the reserve only if the harm traces to the task; diffuse/latent harm goes to a cohort convention.
- **Buffer, not shield** — once the reserve is exhausted, residual task-caused debit reverts to the causer, which keeps the doer careful.

This gives *hazardous* unwanted work a demand-gated incentive with no danger-pay and no rating authority — society de-risks the toxic-cleanup worker exactly as much as it pledges for the job. It does **not** help plain *boring* work (no causal tail to fund), which stays open under [[onerousness-gap|OP-16]]. Sim: `06-simulation/pledge-reserve/pledge_reserve.py`.

## What it's for

- **A decentralized demand signal** — the job [prices](cost-not-price.md) do, split back into its two honest halves.
- **A purpose for surplus.** Credit can't be accumulated into wealth ([non-fungibility](non-fungibility.md)), so a high producer directs what gets made instead of hoarding.
- **Funding the front-loaded and the speculative** — education, research, films, and [capital](debit-taxonomy.md); a large enough pool of pledges *is* an X-prize.
- **A universal basic voice.** Because staying alive is credited work, every living person gets some pledging-power simply for being alive — an equal baseline say in what society makes next.

## Who games this

- **Fractional-reserve pledging** — granting more debit-room than your credit backs. Blocked by the 1:1 cap ([IC-8](event-record.md)).
- **Influence pumping** — manufacturing gross fake hours to pump pledging-power. Bounded by the 24-hour cap (IC-7) and a wrecked efficiency ratio — *and* now by permanence: pledging spends a finite lifetime budget, so a pumper can't pledge for free and pledge-farming needs real colluders burning real budget on the public ledger. Narrowed but not fully closed — residual is [[service-to-influence|OP-1]].
- **Signal flooding** — cheap, unbacked signals generated at scale. Projection-side, parked as **OP-6**.

## Depends on

- [material-flow-value](material-flow-value.md)
- [non-fungibility](non-fungibility.md)

## Consequences

- [[the-front-loading-rule]]
- [debit-tolerance](debit-tolerance.md)

## Open questions

- OP-1 — how pledging-power becomes influence without becoming a currency
- OP-6 — signal aggregation without a popularity plutocracy
- ~~C5 — pledge reversion / retraction target~~ **resolved:** pledges are permanent and unspent ones burn, so nothing reverts.


## Pledge mechanics, in full

> **Moved here from Foundations §4.6 on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rule itself stays in Foundations §4.6. This page carries the worked detail.**

<!-- tag: fnd-s6-4 -->
### 6.4 Pledges and signals

Credit-earners direct what gets worked on next. Two distinct instruments, distinguished by one test:

> **Is it backed 1:1 by earned credit?**

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I authorize this creditable work" | "I want this to exist" |
| Backed by | earned credit, 1:1 | nothing |
| Rate | **1 hour pledged per hour earned — a finite lifetime budget, spent once** | *n* per hour earned, or unbounded |
| Permanence | **permanent, non-revocable** | — |
| Analogue | a wishlist that funds a run; choosing a GP; crowdfunding; commissioning a task | likes, ratings, applause |

**A pledge is a 1:1-backed pre-authorization of creditable work — it need not involve an object or move any debit**. The old framing ("I will absorb this debit") was too narrow. Concrete case: a resident earns 4 credit-hours and **pledges 2 toward mowing the public verge on their block**. Someone with a mower sees the pledge, mows for an hour, submits evidence, and **is credited 1 hour** — 1 pledged hour remains for a later mow. *That is the entire transaction: no object changes hands, no property-debit moves, credits and pledges do not cancel.* The pledge simply **summoned an hour of creditable work** and drew an hour from the pledger's lifetime pledging-budget to do it — without spending or transferring the underlying credit, which stays on the pledger's ledger. **A pledge is permanent and non-revocable, and is not a promise to buy.** Where the pledged work *does* yield a held object, taking that object is a *separate* act: whoever accepts possession takes on its property-debit against their own debit-room (§3.2), whether or not they pledged. That is the ordinary possession rule, not what *defines* a pledge. What defines a pledge is the 1:1 credit backing (IC-8).

**Pledging is deliberately messy, and that is fine.** There will be unfulfilled pledges, frivolous pledges toward trivial or unverifiable tasks, and people learning to pledge well. Coordination groups and pledge-influencing politics will emerge around it. None of this is a defect: **pledges are the job-creating demand lever**, and a lever people organize around is a lever that works.

**Why pledges must be exactly 1:1.** A person's pledges are permanent debit-room they confer on receivers, and every hour of it is drawn from a **finite lifetime pledging-budget equal to their lifetime earned credit**; the 1:1 cap (IC-8) holds cumulative pledging to that backing. Let it exceed and you get **fractional-reserve pledging** — more permanent debit-room granted across the network than the grantors' credit can stand behind. This is a solvency constraint, not a preference. It also happens to be the only stationary value: pledging power created per period is *kL* and consumed at most *L*, so any *k* > 1 diverges until pledges filter nothing, and any *k* < 1 shrinks the directed economy to zero. **Because the budget is spent once and never refunded, pledging is itself a real sacrifice — which is what re-arms the influence guard: an influence-pumper can no longer pledge for free (tightening OP-1), and pledge-farming a task now requires real verified colluders each burning their own finite budget, visible on the public pledge ledger (§4.7).**

**Why signals should be plentiful.** Under 1:1 you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. Cheap, abundant signals **reveal the full preference ordering rather than just the top slice.**

**What pledging is for:**

- **A decentralized demand signal.** Cost says what a thing takes; pledges say who wants it. Aequitas obtains this with no prices, no central optimizer, and **no Iteration Facilitation Board** — the standing body Parecon requires and [is attacked as implausible for](https://ejpe.org/journal/article/view/867).
- **A purpose for surplus.** A high producer whose ceiling far exceeds their appetite can *direct what gets made* instead of accumulating, which A3 (non-fungibility) forbids by design.
- **Funding education and speculative work** (§4.5, §4.5).
- **Collective prizes.** An X-Prize needs no oligarch or patron — a large enough pool of pledges is a crowdfunded bounty. Enterprise remains genuinely risky, as it always has been, and innovation has always flourished under that risk.

**Self-care pledging-power — a universal basic voice**. Self-care (§4.5) is credit in full, so like all credit it generates **pledging-power** as well as consumption headroom (§5.5). Every living human therefore directs some share of what society works on next simply by being alive — a **universal basic voice** — and because the self-care floor is equal for all (§0), it compresses the influence distribution to the same bounded ratio as consumption (§5.5). **Its default routing is a trust-network policy choice** (A8): a network may **auto-pledge** a subscriber's self-care pledging-power toward the **basic-needs sectors** (food, water, shelter, care), leave it **unpledged** for the person to direct, or split it. Auto-pledging is the powerful case — the aggregate self-care pledging-power of a whole population, routed to essentials, **mechanically funds essential provision**, turning §5.5's "essential provision is unconditional" from an assertion into a funded demand signal sourced from the very act of staying alive. The trade-off is the network's to make: auto-pledge guarantees essentials but leaves the subscriber less discretionary voice; leaving it unpledged does the reverse. Self-care adds to a person's lifetime pledging-budget like any other credit; unpledged budget simply stays theirs to direct, and once a self-care pledge is made it is permanent like any other (§4.6).

**Approval never gates credit — but *verification* gates its realization**. The work is **always recorded**: an event is logged the moment work is done, so origin closure holds and unpledged wheat still has a grower (A7, IC-3). What a pledge buys is **authorization and demand-room** for the work — a permanent grant, but still not a guaranteed sale; whoever ultimately takes the resulting good uses their own debit-room to hold it (§3.2, §4.6). But a recorded credit **realizes** — begins counting toward the worker's position — only when the output is **verified**, exactly as A7 already gates an estimated position on observation. This is *verification, not approval*: no committee judges the work worthy; the trigger is objective evidence the output exists. See §4.6 for how, for a physical good, that verification *is* the hand-off.

---

## The contingent reserve, in full

> **Moved here from Foundations §4.6 on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rule itself stays in Foundations §4.6. This page carries the worked detail.**

<!-- tag: fnd-s6-4c -->
### 6.4c The contingent reserve — how over-pledging incentivises hazardous work

Because pledges are permanent, a task can attract **more pledged hours than it costs**. The surplus is **not** a payment to the doer and is **not** consumable — treating it as spendable would be a scarcity price (profit), which A5 forbids, and would re-open a channel for concentrating consumption advantage. Instead the surplus becomes a **contingent reserve**: earmarked, non-spendable debit-room that activates **only against a verified future cost causally traceable to the task** — the doer's later injury or illness, site remediation that resurfaces, third-party harm. This is *any* task-caused cost, not only the doer's.

- **Pledge shares split pro-rata by hours *on the task*** (a doer's share of a pledge = their task-hours ÷ total task-hours), so the cover reaches whoever actually did *this* work — not, via a whole-co-op-history denominator, whoever has been a member longest (which would be the P4 seniority-skim).
- **Causation is decided by the physical-trace test** (§3.4a / OP-17): a claim draws the reserve only if the harm left a trace linking it to the task; diffuse or latent harm with no individual trace is handled by a **cohort/actuarial convention** (the §4.4 residual rule), never an open claim.
- **The reserve is a buffer, not a shield: overflow reverts to the causer.** Once a reserve is exhausted, residual task-caused debit falls back on the doer/cooperative under the ordinary rules (§3.2 possession, §3.7 remediation). Without this, third-party/environmental cover would licence carelessness; with it, the care incentive survives.
- **An abandoned task's pledges are burned** — the pledger's finite budget is spent for nothing, which is what disciplines frivolous pledging. Unused reserve on a completed task likewise never becomes consumable and never reverts; it lapses. **This resolves C5's reversion question in the negative: nothing reverts.**

**What it buys.** Onerousness has two halves. This mechanism gives the *hazardous* half a demand-gated incentive **without** wage premium, rate-scaling, or a rating authority: society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work, and the danger internalises as the size of the reserve the task must attract. It leaves the *tedium/indignity* half open (dull but safe work generates no causal tail, so no reserve, no incentive) — that remainder stays with OP-16. Because the reserve only ever *cancels* a task-caused cost and never *adds* spendable room, it creates no consumption advantage. Sim: `06-simulation/pledge-reserve/pledge_reserve.py` (clears the job at coverage ≈ cover-the-tail; overflow-reverts preserves care; integrity rests on physical-trace causation).

---

## Who holds the demand lever, in full

> **Moved here from Foundations §4.6 on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rule itself stays in Foundations §4.6. This page carries the worked detail.**

<!-- tag: fnd-s6-4d -->
### 6.4d Who holds the demand lever

**Terms used here.** The **demand lever** is whatever decides how much of a thing gets made. A **pledge** is a request for work, backed 1:1 by hours the pledger has already earned, spent once from a lifetime budget (§4.6).

#### The objection this answers

> *Cost says what a thing took. It does not rank two people who both want the last one. Without a price, what decides how much gets made and who gets it?*

This is the standard reply from economics, and it rests on three assumptions. **All three are false in a concentrated market.**

| The assumption | What is actually the case |
|---|---|
| **Scarcity is a physical fact the price reports.** | Much scarcity is produced. Supply is held back to hold the number up. |
| **Demand is a fact the price reports.** | Demand is manufactured, at scale. That is what the whole advertising industry is for. |
| **A price is therefore an honest reading of what people want.** | In a concentrated market the same firms set supply *and* work on demand. **The price partly reports its own producer.** |

**This is not a new claim, and it is not a left-wing one.** Fernand Braudel's economic history separates two layers: **market towns**, where many small sellers meet and price settles from below, and above them a small number of large operators who set prices instead of taking them. [Manuel DeLanda's summary](https://nettime.org/Lists-Archives/nettime-l-9610/msg00025.html) of that layer is direct: capitalism *"has always engaged in anti-competitive practices, manipulating demand and supply in a variety of ways."* **He calls the upper layer an *anti*-market, and so does this project.** See `02-research/DeLanda_markets-antimarkets_v0.2.md`.

> **So the objection assumes the price is a clean instrument. It is not. Aequitas is not replacing an honest demand signal with a worse one. It is replacing a signal that is partly written by the seller.**

#### What pledges change

**A pledge cannot be manufactured by a seller.** It is backed by hours the pledger worked, it is spent once, and it is public (§4.7). A firm cannot advertise a pledge into existence, because a pledge costs the pledger something real that only they can spend.

**And the lever is distributed far more evenly, which is measurable.**

| System | How concentrated the demand lever is |
|---|---|
| Money | Top-tail wealth reaches about **10⁶ ×** the median (SCF 2022 + Forbes, §5.5) |
| Aequitas | Pledging power cannot exceed **24 ÷ F ≈ 2.4 ×** at a 10-hour floor — and that is an **absolute maximum nobody reaches.** A very hard working life reaches about **1.6 ×** (§5.5.5) |

**That is the argument in one line: the demand lever moves from a distribution with no upper bound to one bounded at about 2.4 ×.** Every living person holds some, because self-care credits everyone (§4.5).

#### Two examples, with the numbers

**Example 1 — a person wants their grocer to stock radicchio.**

They tell their device. Under presets they set earlier, it pledges **0.5 h** toward getting radicchio to that grocer.

| | |
|---|---|
| Work to put one extra box on the shelf — pick, load, the truck's extra time, unload, stack | **≈ 2 h** |
| Pledges needed | 2 ÷ 0.5 = **4 people** |
| Cost to one person, against a budget growing ~5,450 h a year | **≈ 0.009% of one year** |

**Four wishes fill one box.** A haulier reads the pledge, adds a box, and the grocer accepts it. **Nobody planned this and no price moved.**

**Example 2 — an artist posts a street-art photograph.**

**5,000 people like it.** Their apps convert likes to pledges under presets they chose.

| | |
|---|---|
| Pledged debit-room raised | 5,000 × 0.1 h = **500 h** |
| The artist's next work — materials and travel | **300 h** |
| Surplus | **200 h** |

**The surplus does not become spendable.** Under §4.6 it becomes an earmarked contingent reserve, and unused reserve lapses. **Nobody is paid a bonus for being liked.**

> **⚠️ A design point that matters, found while working these numbers.** A **flat rate per like** does not discipline anything. At 0.1 h a like, a person earning 5,450 h a year could give **54,500 likes a year** before their budget bound. **The sound preset is a share of a budget:** *this like costs (my art budget) ÷ (likes I give this period)*. Allocate 50 h a year and give 500 likes, and each is 0.1 h; give 5,000 likes and each is 0.01 h. **It normalises itself.** A network offering the flat preset is offering a broken one.

#### Two checks against existing rules

- **Does example 2 let feedback buy credit?** **No.** §4.2 forbids *credit* from realising on feedback, which would make likes a currency (OP-8). **A pledge is not credit.** It grants debit-room and is backed 1:1 by hours the pledger already earned. Auto-routing your own pledging budget is the same permitted move §4.6 already describes for self-care.
- **Does it create a popularity contest?** **Yes, and that is the known open problem OP-6 (feedback mechanics), not a new one.** Whoever is already liked attracts the most pledges. The bound is that every pledge costs a real person a real hour from a finite budget, and the ceiling above holds. **Registered, not solved.**

#### What this does **not** answer

> **Two people, one radicchio. Pledges say how many get grown. They do not say who gets the last one.**

That is a distribution question and it has a separate answer: a queue, a lottery, or pledge-priority, decided at the point of distribution (§5.5, §3.4a). **Cost states what a thing took. Who receives a physically scarce output is a different question, and this document deliberately does not settle it.**

**Full statement of the reply, including the Mises and Hayek arguments:** `00-strategy/OP-9_calculation_reply.md`.

---
*Status: settled (permanent grant of debit-room + contingent reserve, Foundations v0.14)*
*Source: `00-strategy/Aequitas_Foundations_v0.19.md` §4.6, §4.6, §4.6, §4.5 · `00-strategy/Aequitas_EventLog_v0.8.md` §4.1, §4.4, IC-8/IC-9*
