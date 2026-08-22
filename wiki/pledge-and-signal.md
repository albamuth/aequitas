# Pledge and Signal

> The two ways credit-earners direct what gets made next. A **pledge** is a *permanent, non-revocable grant of debit-room*, spent from a lifetime allowance equal to earned credit; a **signal** is a free, unbacked "I want this." Together they are the demand side of the economy — with no prices, no planner, and no board.

Aequitas keeps **cost** and **demand** strictly separate (see [[material-flow-value]]): cost measures what a thing took; pledges and signals reveal who wants it. This page is the demand side.

## Pledge vs. signal

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I put an hour of my credit behind making this happen" | "I want this to exist" |
| Backed by | your earned credit, **1:1** | nothing |
| How much | exactly one hour pledged per hour worked | plenty — signal freely |
| Familiar as | a wishlist that funds; choosing your GP; crowdfunding; commissioning a job | likes, reviews, applause |

**Why pledges are 1:1 and signals are plentiful:** the credit you put behind things can never exceed the credit you earned, or people would back work with room that isn't really there ([[event-record|IC-8]]). Signals carry no such constraint, so they should be abundant — they reveal your *whole* preference ordering, not just the top slice a scarce pledge can express.

## What a pledge actually is *(Foundations v0.14 — pledges made permanent)*

A pledge is **not** a purchase, **not** a spend of your credit, and **not** a promise to buy. It is a **permanent, non-revocable grant of debit-room**:

- **Your credit stays yours, but a separate allowance is spent.** A pledge puts credit *behind* something — like naming a beneficiary, not handing over your balance. What it spends is *pledging-power* — a **lifetime budget equal to your earned credit, drawn down once**. A pledged hour is gone from that budget for good.
- **To the receiver it is virtual credit.** It expands the receiving person's or co-op's [[debit-tolerance|debit-room]] so a fixed cost bites less. The debit itself does not move to the pledger and does not vanish — it stays where it was incurred (e.g. holding-time-split on a facility's holders, [[debit-taxonomy]] §6.2b); the pledge only *cushions* the bite.
- **It is permanent — you can't take it back.** The receiver can rely on the granted room and get on with the work; it won't vanish under them. The discipline is *at pledge time* — because a pledge is a real, one-time expense, nobody pledges frivolously or floods the system for free. An unspent pledge to an abandoned task is **burned**, not returned.
- **Buying is a separate act.** Where pledged work yields a held object, taking that object loads its [[property-debit]] on **whoever accepts possession** (§3.2) — pledge or no pledge, and not necessarily the pledger.

**A pledge need not involve an object at all.** Pledge two hours toward mowing a public verge; someone mows for an hour, shows proof, and earns an hour of credit — no object changed hands, no debit moved. A pledge simply **summons creditable work into being**.

## The contingent reserve — over-pledging dangerous work

When a task attracts **more pledged hours than it costs**, the surplus is **not** a bonus to the doer and **not** spendable — that would be profit ([[price-equals-cost]]) and would let someone concentrate consumption. Instead it becomes a **contingent reserve**: earmarked, non-spendable room that pays out **only against a verified future cost caused by the task** — the doer's later injury or illness, a site's remediation resurfacing, third-party harm.

- **Split by hours *on the task*** — the cover reaches whoever did *this* work, not whoever's been a co-op member longest.
- **Causation by physical-trace** — a claim draws the reserve only if the harm traces to the task; diffuse/latent harm goes to a cohort convention.
- **Buffer, not shield** — once the reserve is exhausted, residual task-caused debit reverts to the causer, which keeps the doer careful.

This gives *hazardous* unwanted work a demand-gated incentive with no danger-pay and no rating authority — society de-risks the toxic-cleanup worker exactly as much as it pledges for the job. It does **not** help plain *boring* work (no causal tail to fund), which stays open under [[onerousness-gap|OP-16]]. Sim: `06-simulation/pledge_reserve.py`.

## What it's for

- **A decentralized demand signal** — the job [[price-equals-cost|prices]] do, split back into its two honest halves.
- **A purpose for surplus.** Credit can't be accumulated into wealth ([[non-fungibility]]), so a high producer directs what gets made instead of hoarding.
- **Funding the front-loaded and the speculative** — education, research, films, and [[debit-taxonomy|capital]]; a large enough pool of pledges *is* an X-prize.
- **A universal basic voice.** Because staying alive is credited work, every living person gets some pledging-power simply for being alive — an equal baseline say in what society makes next.

## Who games this

- **Fractional-reserve pledging** — granting more debit-room than your credit backs. Blocked by the 1:1 cap ([[event-record|IC-8]]).
- **Influence pumping** — manufacturing gross fake hours to pump pledging-power. Bounded by the 24-hour cap (IC-7) and a wrecked efficiency ratio — *and* now by permanence: pledging spends a finite lifetime budget, so a pumper can't pledge for free and pledge-farming needs real colluders burning real budget on the public ledger. Narrowed but not fully closed — residual is [[service-to-influence|OP-1]].
- **Signal flooding** — cheap, unbacked signals generated at scale. Projection-side, parked as **OP-6**.

## Depends on

- [[material-flow-value]]
- [[non-fungibility]]

## Consequences

- [[the-front-loading-rule]]
- [[debit-tolerance]]

## Open questions

- OP-1 — how pledging-power becomes influence without becoming a currency
- OP-6 — signal aggregation without a popularity plutocracy
- ~~C5 — pledge reversion / retraction target~~ **resolved:** pledges are permanent and unspent ones burn, so nothing reverts.

---
*Status: settled (permanent grant of debit-room + contingent reserve, Foundations v0.14)*
*Source: `00-strategy/Aequitas_Foundations_v0.17.md` §6.4, §6.4a, §6.4c, §6.2b · `00-strategy/Aequitas_EventLog_v0.8.md` §5.1, §5.1c, IC-8/IC-9*
