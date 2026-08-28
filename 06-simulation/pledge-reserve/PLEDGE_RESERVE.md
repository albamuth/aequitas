# Pledge Reserve — the contingent-reserve incentive for hazardous work

**Sim:** [`pledge_reserve.py`](pledge_reserve.py) · **Ruling:** session 2026-08-14 · **Status:** all 5 self-tests green
**Bears on:** OP-16 (onerousness gap, hazard half) · OP-1 · P4 · C5 · C2 · Foundations §4.6/§4.6, §3.2, §3.7 · IC-8

---

## The question

Should over-pledging highly-desired unwanted work (a toxic site everyone wants cleaned but nobody wants to do) give the doer an added benefit? A market pays a **wage premium** for nasty work. Aequitas has no wage and no profit (A5 (cost, not price), A2). So either onerous work goes chronically understaffed (the OP-16 problem, confirmed by 45 years of time-banking), or we find an axiom-clean incentive.

## The ruling being tested

Pledges are now **permanent, non-revocable** grants of debit-room (reversing the v0.13 revocable model — revocability let doers who consumed against a pledge get stranded when it was withdrawn, and was gameable). A pledge first cushions the task's labour/material cost, **pro-rata by hours *on the task*** (not whole-co-op history — that skims pledges to seniority, a P4 surface). Any **surplus is not consumable**. It becomes a **contingent reserve**: earmarked, non-spendable room that activates only against a **verified future cost causally traceable to the task** — the doer's injury/illness, resurfaced site remediation, third-party harm.

Two possibilities were **rejected** first:
- **Surplus as extra credit / wage premium** — breaks A2 (rate-scaling).
- **Surplus as consumable room** — rejected on the axioms: banking the excess as spendable room re-creates a channel for accumulating consumption advantage, which the system's equality commitments forbid. (A scammer over-pledges an easy-but-scary-sounding task, does it, and banks the excess.) The reserve model defeats this by construction — an easy task has ~no causal tail → the reserve sits dormant and **burns** → the scam nets zero. Because this rejection is settled on the axioms, it needs no simulation.

Two guards are baked in and tested:
- **G1 — overflow reverts to the causer.** The reserve is a *buffer, not a shield*: exhaust it and residual task-caused debit falls back on the doer/co-op (§3.2/§3.7). Without G1, third-party/environmental coverage licenses carelessness.
- **G2 — causation by physical-trace.** A claim draws the reserve only if the harm left a trace linking it to the task; diffuse/latent harm goes to a cohort/actuarial convention, never an open claim. Integrity rests here.

## What the sim shows

| Claim | Result |
|---|---|
| **[A] Clearing** | Under flat credit alone only **~16%** of the pool will take the hazardous job (they bear its expected health tail on their own ledger) → **shortage**. Willing supply rises steadily with reserve coverage and **clears at c\* ≈ 0.84** — pledges must roughly cover the tail. Over-pledging is a **demand-gated bond**, not a wage premium. |
| **[B] Care** | A full **shield** collapses care to 0 (harm = max). **Buffer + overflow (G1)** holds care up and **halves the harm**. G1 is the moral-hazard kill-switch. |
| **[G2] Fraud** | With good physical-trace, reserve headroom absorbs even heavy padded-claim volume; weak trace + high fraud exhausts the reserve and **denies real claimants** (20% of the legit tail uncovered). |

Plots: [`pr_fig1_clearing.png`](pr_fig1_clearing.png) · [`pr_fig2_care.png`](pr_fig2_care.png)

## Plain-language guide (what the numbers and charts actually mean)

**The setup, in one breath.** A toxic site needs cleaning; it's dangerous and might make you sick years later. Everyone in Aequitas earns the *same* credit per hour whether the work is pleasant or deadly, so there's no danger-pay to lure anyone in. When lots of people **pledge** toward the cleanup, the pledges *beyond what the job itself costs* don't become a bonus — they become an **insurance fund** for that job, which pays out only if a worker (or a bystander, or the site) is actually harmed later. Protection, not a payday.

**Row [A] — "does the job get staffed?"** Without insurance, only **16 out of 100** people volunteer — not enough, so the site stays dirty. As the insurance fund grows to cover more of the expected danger, more people are willing; once it covers about **84%**, enough sign up. *Society has to collectively pledge enough to cover the risk, or it doesn't get done.*

> **Where does "16 out of 100" come from?** It's not a measured real-world figure — it's what the model's made-up-but-reasonable spread produces, and it stands for *"the minority who'd do dangerous work even with no protection."* Each of 200,000 simulated workers is given two numbers: how much future harm the job is expected to cost *them* (averaging ~300 hours, with a few facing far more), and how much danger they'll shoulder *for free* (averaging ~60 hours — some people genuinely don't mind risk). With no insurance, a person volunteers only if the job's expected harm to them is already inside their free-tolerance. Because the average harm (300) is much bigger than the average tolerance (60), only ~16% clear that bar. Change those two made-up averages and the 16% moves — so treat it as *"a small minority,"* not a hard fact.

**Row [B] — "do workers stay careful?"** If insurance covered *everything*, workers get sloppy — so the rule is it covers only up to the pledged amount, and any damage beyond that the worker eats. The "covers everything" version produces **twice the harm** of the "you're still on the hook for the overflow" version.

> **How does the sim get the care numbers?** A worker picks how careful to be, on a dial from 0 (careless) to 1 (maximally careful). Being careful costs effort (more care = more hours spent being cautious). More care means less expected harm. The sim just asks: *which setting of the dial costs the worker the least, all-in?*
> - **"Covers everything" (shield):** the worker never pays for harm, so care is pure wasted effort → they pick 0 → harm stays at its maximum (500 hours in the run).
> - **"Overflow on the worker" (buffer):** the worker pays for any harm above the insurance amount, so they balance effort against the damage they'd personally eat → they pick the middle of the dial → harm drops to 250. Hence *"halves the harm."* The specific 500-vs-250 depends on the made-up effort-cost and worst-case-harm numbers; the *point* — a full shield kills caution, keeping workers on the hook preserves it — does not.

**Row [G2] — "can people fake injuries?"** The fund only pays with real evidence the job caused the harm. Strong evidence-checks → cheating fails even when many try. Weak checks → cheaters drain the fund and **real injured people go uncovered**. The whole scheme hangs on being able to prove *"this harm came from this job."*

### The two charts

**Chart 1 — [`pr_fig1_clearing.png`](pr_fig1_clearing.png) (staffing).** Left→right: how much of the expected danger the insurance covers (0 = nothing, 1 = fully covered). Up: the share of people willing to do the job. The **blue line climbs** as coverage grows; the **red dashed line** is how many volunteers you need; the **green dotted line** marks where blue crosses red — the point where enough people sign up. *Too few volunteers until the insurance covers most of the danger.*

**Chart 2 — [`pr_fig2_care.png`](pr_fig2_care.png) (carefulness).** Left→right: how big the insurance fund is. Up: how much harm actually happens. The **red line ("covers everything")** stays pinned at maximum harm — workers are careless throughout. The **green line ("workers cover the overflow")** sits lower — they stay careful — and **the gap between the two lines is the damage prevented by keeping workers on the hook.** (Note the honest wrinkle: as the fund gets very large, the green line drifts up toward red, because a near-total fund leaves little overflow left to fear.)

## Headline

> The contingent reserve **clears hazardous work as a demand-gated bond** and **preserves care** via overflow-reverts. The surplus stays **non-spendable**, so it creates no consumption advantage — that is a design fact, not a simulated result. It solves the **hazard half** of OP-16; **tedium and indignity remain open** (boring, safe work generates no causal tail, so no reserve, no incentive). Integrity rests entirely on **G2 (physical-trace causation)**.

## Honest caveats

- **Structural, not forecast.** The constants (hazard-cost distribution, care-cost curve) are illustrative and flagged in-code. The claimed results are the **shapes** — clearing only once the tail is roughly covered, and shield-kills-care — which are robust to the constants. The absolute numbers (16%, c\*=0.84) are not.
- **A real tension the sim exposes.** The insurance fund that *attracts* workers ([A]) is also large enough to *erode* their caution ([B], the green line drifting up). Staffing and carefulness pull in opposite directions as the fund grows; G1 (overflow-reverts) is what stops the erosion from running all the way to the careless "shield" outcome.
- **Scope.** Solves hazardous-onerous only. Tedium/indignity is the still-open remainder of OP-16.
- **New machinery.** A *contingent reserve* is a distinct ledger object (earmarked, non-spendable, converts to cushion only on a verified claim). Claims adjudication over a decades-long reserve **adds weight to the still-deferred C2 trust-network straw-man** (dispute resolution, claim-priority when claims exceed the reserve).
- **Not modelled:** claim-priority ordering when multiple verified claims exceed a finite reserve; the latency-period bookkeeping for reserves held open for decades.
