# The Disparity Ceiling — formal statement (queue #8, Part 1)

**Sim:** [`disparity_ceiling_sim.py`](disparity_ceiling_sim.py) — 5 self-tests green · **Tracks:** Foundations v0.14 · the conformance list · Objections §C test 8
**Status:** **Conditional result** (on OP-22 + **five** conditions in §4 — the fifth added 2026-08-22, correcting an error in the fourth, then re-framed the same day), **consumption axis only**, within-model. **Stress-tested 2026-08-14 → PASSES** (§3a). Upgrades the [`01-wiki/disparity-ceiling.md`](../../01-wiki/disparity-ceiling.md) sketch from *hypothesis* to *stated, simulated, stress-tested, conditional result*. **New readers: start at §0 (plain-language explainer).**

> **📄 Checkable without running it — [`audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md).** Regenerate with `python 06-simulation/audits/audits_inert/generate_bonus.py`.
>
> **Three of the four claims need no simulation at all.** Claims 1 (the ceiling), 3 (fraud invariance) and 4 (front-loading) are closed-form arithmetic — the 200,000-agent population demonstrates them, it does not establish them. Only **claim 2**, the clearing rate ρ\*, needs the draw, and its ρ\* is resolved no finer than one grid step of 0.0176. This follows @twelve-minute-window (c15176 on [#1605](https://1f916.ai/post/1605)), who conceded-in-full point was that shipping executable-only relocates trust to the repository.

> **The claim, in one line.** Under Aequitas the ratio between the most anyone can sustainably consume and a bare-subsistence allowance is **24/F** across any set of networks compatible enough to interoperate — and networks counting the same person are compatible only if they arrive at the same ledger for that person (§4 condition 5) (where *F* is the network's self-care floor in hours/day) — a small number, independent of the tolerance dial ρ and of the weighting model, and **invariant to fraud**. Under money the same ratio runs to **~10⁶×** and compounds without limit.

---

## 0. Plain-language explainer — read this first

**The one big idea:** under money the gap between the richest and poorest person is about **a million to one**; under Aequitas it is about **2.4 to one**. This section explains, from scratch, why — and what every symbol means. No math background assumed.

### Every variable, in plain words

| Symbol | Name | What it actually means | Example |
|---|---|---|---|
| **24** | hours in a day | The one resource shared out *perfectly equally* — everyone alive gets exactly 24 hours today, and no one can get more. | 24 h |
| **F** | self-care floor | Hours per day you're credited *just for keeping yourself alive* — sleeping, eating, washing, staying healthy. Aequitas counts staying alive as real work (§5.5), so **nobody earns zero**. Each network picks its own F. | ~10 h |
| **wᵢ** | discretionary work | The *extra* hours person *i* chooses to work on top of self-care. Ranges 0 (does nothing extra) to 24−F (works every waking hour). | 0–14 h |
| **cᵢ** | credit *rate* | Total hours/day person *i* is credited = F + wᵢ. Everyone lands somewhere in **[F, 24]**. | 10–24 h |
| **ρ** ("rho") | tolerance dial | How much you may consume relative to what you produce. ρ=1 → consume exactly what you earn; ρ=1.5 → society lets you run at 1.5× (a deliberate slack). Set by local government like a **central-bank interest rate**, the *same* for everyone in a network. Aequitas never picks a global ρ. | ~1.2–1.5 |
| **C, D** | credit, consumption | What you've earned, and what you take. | — |
| **24/F** | **the ceiling** | The biggest possible ratio between the top consumer and a bare-survival consumer. At F=10 → **2.4**. | 2.4× |

### The rule that ties them together
Aequitas lets you consume up to your tolerance times your credit:
> **D ≤ ρ × C** — *"you may consume up to ρ times what you earn."*

The subtle-but-crucial part: **C is a running *record*, not a spendable balance.** It is the sum of every hour you have ever worked, and a purchase adds to your *debit* — it never subtracts from your credit. The rule is a **ratio checked at each purchase**: if a purchase would push your total debit past ρ times your total credit, it is blocked. Nothing is "banked" and spent — credit is not a currency (that is **A3**). (Why that closes the hoard-and-splurge attack is #1 below.)

### The whole proof in one paragraph
The most anyone can earn is **24 hours a day** — you cannot be credited for time you do not have. That is **IC-7**, the 24-hour cap, and it holds *even for a cheater*, because a cheater still only has 24 hours in a day. The least anyone earns is the floor **F**, because staying alive is credited to everyone (**§5.5**). So the top consumer takes ρ×24 and the bottom takes ρ×F, and the ratio between them is:
> (ρ × 24) / (ρ × F) = **24 / F**

The **ρ cancels out** — it makes no difference how generous or tight the dial is set; the *ratio* between top and bottom is fixed by the length of a day against the survival floor. That is the entire result.

### Why money is a million-to-one and this is 2.4-to-one

| | Money | Aequitas |
|---|---|---|
| What you accumulate | **net worth** — compounds, no ceiling | **credit = hours** — capped at 24/day |
| Can you pool others' share? | yes — buy, inherit, invest | **no** — credit can't be transferred, lent, or inherited (**A3**) |
| Richest ÷ median (real data) | **~1,000,000×** | **2.4×** |

The money figures are real. 2022 [Survey of Consumer Finances](https://www.federalreserve.gov/publications/files/scf23.pdf): median US household net worth **$192,900**; the top 1% hold ≈ **71×** the median; a [Forbes](https://www.forbes.com/billionaires/) ~$200 B fortune is ≈ **10⁶×** the median. The gap is astronomical because money **compounds** (holdings earn more holdings) and **transfers** (one person can command millions of *other* people's output). Aequitas credit does neither: it is your own time — and everyone gets exactly 24 hours, which you cannot hand to anyone else.

### The three attacks the stress test threw at it (and why each fails)
1. **"Can't a lifelong hard worker bank 70 years of credit and blow it in one splurge?"** No — because credit is not a spendable balance. It is a *running record* of every hour you have ever worked, and a purchase adds to your *debit*; it never draws your credit down (that is what **A3** means by "credit is not a currency"). The rule checked at every purchase is a *ratio* — total debit ≤ ρ × total credit — so there is nothing to bank and blow. A splurge only front-loads your *own* lifetime allowance; at the same age, the hardest worker's total still sits at most 24/F above a subsistence person's. (The only reason an older person can have consumed more is that they have lived and worked longer — which everyone does in turn.)
2. **"Can't a dynasty pool a whole household into one mansion?"** A household is treated like a co-op: the home's debt splits across everyone living there **by how long each lives there** (children included). Per person it's still ≤ 24/F, and passing a house down *lightens* the load each generation — a reason to maintain it, not demolish it. One relative dominating the rest is a coercion problem (OP-1), not an accounting hole.
3. **"Can't someone hoard houses, gold, art?"** They can try, but **holding things is a burden, not an income** here — a held asset carries permanent debit that eats into your *own* consumption gate. The hoard bounds itself. This isn't a leak Aequitas patches; it's one it fixes by design.

---

## 1. Setup and definitions

Consumption in Aequitas is governed by four already-settled facts:

- **Credit is time (A2).** A person's credit accrues at a rate `c_i` = hours credited per day. It is `c_i = F + w_i`, where **F** is the [self-care floor](../../01-wiki/pledge-and-signal.md) credited to *every verified living human* by proof-of-life (Foundations §4.5 / §5.5) and `w_i ∈ [0, 24−F]` is discretionary worked hours.
- **The wall-clock cap (IC-7).** No account may be credited more than **24 hours per 24 hours** — honest or fraudulent, no exceptions (IC-7). So `c_i ∈ [F, 24]` for everyone, always.
- **Non-transferability (A3).** Credit cannot be transferred, pooled, lent at interest, inherited, compounded, or converted to a medium of exchange. A person's command over resources derives **only from their own `c_i`**, never anyone else's.
- **The discretionary gate (OP-4 shape, settled) — a dynamically-checked ratio on two running tallies.** Both credit `C_i` and debit are **running tallies derived from the event log** (A6 — the ledger is *derived, not stored*), in hours: `C_i` is the sum of every hour *i* has ever been credited for working (it decreases *only* if an auditor unwinds a fraudulent claim), and debit is the running sum of consumption/property burden. The gate `D_i ≤ ρ · C_i` is re-checked **at each new event**: a purchase that would push the debit past ρ times the credit is **blocked**. **Credit is never *spent*** — a purchase adds to debit, it does not decrement credit — so there is no spendable balance to "bank" and later blow. That is precisely A3 ("credit is not a currency"). ρ is an exogenous dial (§3.5/A8), identical within a network; Aequitas never sets a global one. Lifetime credit *does* accumulate, but its only outlet is **pledging-power** (influence — Foundations §4.6), never consumption. See §3a for why this dissolves the hoard-and-splurge attack.

A person's **sustainable consumption allowance** is therefore `a_i = ρ · c_i`.

---

## 2. The theorem

> **Within-model consumption-disparity bound.** For any network with self-care floor *F* and tolerance dial ρ, the ratio of the largest sustainable consumption allowance to the bare (floor-only) allowance is
>
> **R = max_i(ρ·c_i) / (ρ·F) = (ρ·24) / (ρ·F) = 24 / F**,
>
> **independent of ρ and of the weighting model.**

**Proof.**
- **Numerator.** `max_i c_i ≤ 24` by IC-7 — no one is credited more than 24 h/day. The bound is approached by someone who works every waking hour (`w_i → 24−F`, so `c_i → 24`).
- **Denominator.** The smallest sustainable allowance belongs to the floor-only person, `c = F`. Because the self-care floor is credited to *every* living human (proof-of-life, §5.5), **no one sits below F** — the denominator can fall no lower.
- **The ratio.** Both allowances are `ρ·c`, so the extremal ratio is `(ρ·24)/(ρ·F) = 24/F`. **ρ cancels** — the dial that sets how tolerant the system is scales numerator and denominator equally. The **weighting model** converts person-hours into debit-room, but by A2 it applies the *same* hours-unit to both extremes, so it cancels too. ∎

**The cumulative form (why hoarding cannot beat it).** Because credit and debit are *running tallies* (§1), the same bound holds on lifetime totals: at **equal age**, two people's cumulative credits stand in ratio ≤ 24/F (their rates lie in `[F, 24]`, integrated over equal time), and each may carry cumulative debit up to `ρ·C`. So cumulative consumption disparity is also ≤ 24/F. A "splurge" (hoard, then buy a mansion) merely **front-loads a person's own allowance** — it can never exceed their `ρ·C`. **The one cross-sectional spread beyond 24/F is age** — a longer-lived person has worked more total hours — which is time lived, not class, is bounded at every age, and is traversed by everyone.

**Corollary (fraud-invariance on the consumption axis).** A fraudster can inflate *claimed* hours, but IC-7 caps the claim at 24 h/day exactly as it does for the honest. Fraud can therefore fill the `[F, 24]` band — it cannot manufacture a `c_i > 24`, so it **cannot breach 24/F**. Money has no analogue of IC-7: holdings compound with no wall-clock cap, which is why its tail is unbounded.

---

## 3. Why each bound is *hard* (and where the danger was)

The result rests entirely on the two ends of the interval being nailed down and on the interval not being stackable:

| Ingredient | Bounds | Provided by |
|---|---|---|
| Upper end `c ≤ 24` | numerator | **IC-7** — physical wall-clock, applies to fraud too |
| Lower end `c ≥ F` | denominator | **§5.5 self-care floor**, credited to every living human |
| **No stacking** | the whole bound | **A3 non-transferability** — you cannot pool many people's 24 h into one account |

**Non-transferability is the load-bearing axiom.** The bound is `24/F`, *not* `24·k/F`, precisely because one account cannot absorb others' credit. If it could — by transfer, inheritance, lending, or **a convertible pledged surplus** — the numerator would scale with the number of accounts a person controls, and the bound would collapse. A3 forbids the first three outright.

> **The one live gap — and its closure this session.** A *pledged surplus* acting as transferable consumption capacity was the single channel that could have routed around A3. It was **closed on 2026-08-14**: pledge surplus is now a **non-consumable contingent reserve** (Foundations §4.6) — pledged hours can never become the recipient's spendable room, they only pre-fund verified task-caused costs. **So pledges add nothing to any account's `c_i`, and the transfer channel is shut.** The disparity-ceiling proof and the pledge-permanence ruling are thus coupled: the reason surplus was *not* made spendable is exactly this bound.

---

## 3a. Adversarial pass (2026-08-14) — three attacks, three resolutions

The stress test hunted for channels that beat 24/F despite A3. All three resolve; the first *sharpened the proof*.

1. **The Methuselah hoarder** — *"bank 70 years of credit, spend it as one splurge → disparity ≫ 24/F."* **Dissolved — and it corrected the model.** There is no "banking": credit and debit are **cumulative running tallies** from the event log (§1), the gate is the ratio `D ≤ ρ·C` re-checked at each event, and **credit is never *spent*** — a purchase adds to debit, it does not draw credit down (A3 — not a currency). So a "splurge" can only **front-load a person's own cumulative allowance** (bounded by `ρ·C`); it can never exceed it. At **equal age** two people's cumulative credits stand in ratio ≤ 24/F, so cumulative-consumption disparity is bounded by 24/F. The only spread beyond 24/F is **age** (time lived, not class; bounded at every age; traversed by all). *(An earlier draft framed this as "rate-gate vs stock-gate" — a false split. The real mechanism is a dynamically-checked ratio on an immutable cumulative record, which is just A3 + A6.)*
2. **The dynasty / household** — *"N adults pool into one mansion → N×24/F lived."* **Resolved: a household is a cooperative.** The dwelling's debit-load holding-time-splits across its occupants **by dwelling-time, children included** (§4.5) — per person still ≤ 24/F. Inheritance *dilutes* the load each generation (an incentive to maintain, not demolish; and family mobility, since debit only accrues from move-in on an existing property). The residual — one member dominating others' consumption — is coercion/influence (**OP-1**), not an accounting breach. **The bound is therefore per-person, not per-household** — stated as such.
3. **The collector** — *"amass durable goods — houses, gold, art."* **Not an exploit; a thing Aequitas fixes.** Holdings are a **burden**, not income: a held asset carries permanent property-debit that eats the holder's *own* consumption gate (§4.5 / §3.2). The hoard bounds itself. (This couples to resolution 1: property-debit-as-burden bites because the gate is a live ratio on the running debit tally — holding more raises your debit against a fixed credit.)

**Verdict: PASSES** (was PASSES-WITH-CHANGES; the required change — stating that credit is an immutable cumulative *record*, gated as a ratio, not a spendable balance — is applied above; A3 + A6). The cumulative-ledger self-test that demonstrates it is now in the sim (Claim 4, §6).

## 4. Why the result is CONDITIONAL, not absolute

The `24/F` bound is a **within-model** statement — true inside one network's books. It becomes a **cross-network / real-world guarantee** only under four conditions (all recorded in Foundations §0 / §5.5):

1. **F sits in a narrow band across networks.** Otherwise a person compares a generous network's allowance against a stingy network's floor, and the effective ratio drifts above 24/F.
2. **Floor-shopping is arrested by counterparty re-computation (OP-14).** Each counterparty re-reads a claim through its *own* F and ρ (comparison, never conversion), so a low floor cannot be *exported*.
3. **OP-22 is solved.** That re-computation requires proving "backed by *X* hours under model *M*" **without revealing the private ledger** (zero-knowledge disclosure). The guard is only as real as this mechanism — **OP-22 is the load-bearing dependency**, and it is unsolved.
4. **No gross-hour fraud beyond IC-7.** *Within one network*, IC-7 caps this on the consumption axis; the residual "fake gross hours → influence" pump is **OP-1**, on the influence axis, out of scope here.
5. **Networks counting the same person must arrive at the same ledger for that person — that is what compatibility *is*.** ⚠️ **Added 2026-08-22; supersedes an earlier draft of this condition that got the framing wrong.** Multi-network accounts are legitimate (Foundations §4.7). **That is not two credits. It is one life, counted twice.** Two networks counting the same person are counting the same thing, so **being compatible means being able to re-derive each other's numbers and land on the same ledger** (OP-14, comparison never conversion). Where they can, the self-care floor is credited **once** and there is nothing to sum.

   **Where they cannot, they are not compatible and their credits do not interoperate** — goods and claims do not cross. What remains is **a coverage gap, not a breached bound**: each network holds a partial record of that person's material life, and the extent rule (the retired record model §7.4) requires each to declare it as partial. **The earlier draft treated this as `k × 24/F`, which was arithmetic on two ledgers that, if compatible, are the same ledger.**

   *Federation is not a patch bolted onto the ceiling. It is what interoperation means.*

---

## 5. Scope and honesty

- **Consumption axis only.** Influence (pledging-power → agenda-setting) is **OP-1** and explicitly *not* claimed here. The influence distribution is separately compressed by the equal self-care floor, but its fraud-resistance is a different question.
- **`24/F` is illustrative, never universal.** At *F* = 10 h it is **2.4×**; at *F* = 8 h, 3×; at *F* = 2 h, 12×. The bound is `24/F` for whatever floor a network sets — **A8 forbids a global F**, so there is no single headline constant, only the *form* of the bound.
- **Within-model.** Absent OP-22, the cross-network claim is not yet secured.

---

## 6. Evidence — the simulation

[`disparity_ceiling_sim.py`](disparity_ceiling_sim.py), 200k-agent, 5 self-tests green:

- **Claim 1 (theorem, numerically):** the ceiling is **flat at 2.40×** across ρ ∈ [1, 3] — ρ-independence confirmed (`std < 1e-6`).
- **Claim 3 (fraud-invariance):** the ceiling **holds at 2.40× even at 40 % fraud** (accounts inflating claimed hours ×2) — IC-7 caps every claim at 24 h.
- **Claim 4 (Methuselah / front-loading):** on the cumulative ledger with the ratio gate re-checked each period, a lifelong hoarder who attempts a **14,400 h splurge is clipped to 1,440 h (= ρ·C)** and lands at *exactly* the steady consumer's total; **equal-age disparity = 2.40×** under both strategies; the **only** spread beyond it is age (a 60-yr max-worker vs a 20-yr subsistence person = 7.2× = 3×·24/F). Plot: [`ceiling_fig4_frontloading.png`](ceiling_fig4_frontloading.png).
- **Comparison (Part 3):** US net worth calibrated to the [2022 Survey of Consumer Finances](https://www.federalreserve.gov/publications/files/scf23.pdf) (p90 ≈ 10×, p99 ≈ 71× the median) with a [Forbes](https://www.forbes.com/billionaires/) billionaire tail at **~10⁶× the median** → **compression ≈ 4×10⁵**.
- **Claim 2 (bonus — ρ behaves as a prime rate):** a clearing ρ\* exists (~1.24) and **tightens under a capacity shock** (→0.82), confirming ρ acts as an exogenous, shock-responsive dial, never an Aequitas verdict.

---

## 7. What remains (to finish queue #8)

1. **This document = Part 1 (formal statement) + §0 explainer + §3a stress test.** ✅ done, PASSES.
2. **Cumulative-ledger / front-loading self-test** ✅ **done** — `disparity_ceiling_sim.py` Claim 4 (`test_frontloading_cannot_beat_ceiling`, `test_only_age_exceeds_ceiling`), both green + a trajectory plot. Makes the equal-age argument a number and shows credit-as-record needs no separate "rate gate."
3. **Part 2 (simulation)** exists and is green (**7 self-tests**). *Optional polish:* an in-sim note that Claim 1 is the *within-model* bound, conditional on OP-22 cross-network.
4. **Part 3 (like-for-like vs the Pareto wealth tail)** is embedded in the SCF/Forbes calibration; *optional:* promote to its own figure.
5. **▶ Ready to fold** — into Objections §C test 8 (open test → conditional result, PASSES) and the wiki page. This is the next step.

*Parked sim (author-proposed 2026-08-14):* **family housing-mobility** — under the dwelling-time holding-time-split, what is the average family age before they accrue the debit-room to move into a new (larger) home, and what size? Explores whether the §4.5 household model gives realistic mobility.
