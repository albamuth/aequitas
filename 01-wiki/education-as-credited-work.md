# Education as Credited Work

> **Children are credited for attending school**, and their teachers are credited for teaching them. Schooling is real, materially accounted activity — not unpaid time.

## What it is

Learning enriches the individual and, indirectly, everyone the person later serves. Under [material-flow-value](material-flow-value.md) it is activity like any other: people present, for intervals, consuming materials and energy, producing a change in the world.

So it is credited. Both sides of the room.

Simultaneously, the **cost** of that schooling — the real time and materials it consumed — flows downstream into the services the graduate later provides ([time-as-yardstick](time-as-yardstick.md)). Education is credited to the student *and* carried forward as a cost of what they later do.

## Why it works this way

This is one of the clearest demonstrations of [honest-advantage](honest-advantage.md). Schooling is the largest unpaid contribution most people make in their lives; today it is a cost borne by the student and their family, discharged in the hope of future wages. Under Aequitas it is credited work from the first day.

Crucially it requires **no special rule.** There is no "education exception" — attending school is materially real activity, accounted exactly like farm labor or manufacturing. That satisfies universality; a rule that had to carve out education would fail it.

It is also how [time-as-yardstick](time-as-yardstick.md) escapes the trap that sank [cost-the-limit-of-price](cost-the-limit-of-price.md). Warren could not price skilled labor without a judge. Aequitas prices it by tracing what the skill actually cost to produce — and that requires education to be in the log in the first place.

## Open questions

- **OP-11 — the amortization denominator.** The training cost flows downstream, but over *how many* future service-hours? Unresolved, and it blocks full A2 implementation.
- Does credit for attendance create an incentive to attend without learning? Probably answered by the fact that credit is for the activity, not for an outcome — but worth testing.
- Lifelong learning, retraining, and self-teaching: same treatment, presumably. Unspecified.

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) · [service-credit](service-credit.md)

## Consequences

- [honest-advantage](honest-advantage.md) · [debit-tolerance](debit-tolerance.md) — a child carries tolerance and now also earns


## The front-loading rule, in full

> **Moved here from Foundations §4.5 on 2026-08-27, when §4, §5 and §6 were consolidated into one section. The rule itself stays in Foundations §4.5. This page carries the worked detail.**

<!-- tag: fnd-s6-2a -->
### 6.2a The Front-Loading Rule

Training is the first instance of a general rule, and the rule is worth stating once — and naming — rather than rediscovering per case. It is referenced across the theory as **the Front-Loading Rule**:

> ### 🔒 THE FRONT-LOADING RULE
> **A large up-front cost with a diffuse benefit is carried where it is incurred and cushioned at that time by the debit-room the people who pledged for it grant. It is never amortized downstream onto whoever happens to consume the result.**
>
> **Covers:** education (§4.5), media/creative production, research · infrastructure · tooling, and **capital & overhead** (§4.5 — which is *why* it also closed OP-23).
> **Why it's right:** the downstream window is always arbitrary (that arbitrariness *was* OP-11/OP-21), and downstream amortization triggers an infinite regress to the first human activity — **computational closure** (the upstream face of the §3.2b non-cascade rule).
> **Boundary:** capital vs. consumption, told apart by **physical fate** (does the thing survive the process?), auditable via IC-4 (fate closure) — not by the producer's declaration.
> **Who carries the capital:** the §4.5 waterfall — the full creation-cost is holding-time-split among the asset's holders; community pledges grant debit-room that cushions the bite; basic-needs-floor cap.
> **Dissolved:** OP-11 (training amortization), OP-5 (education), OP-21 (media) as one malformed question (B3); OP-23 (shared overhead), by accruing capital to the asset, never to co-products (B8).
> **Honest residue:** cold start (a first-time creator attracts no pledges); a per-unit debit-cost is therefore *not* a full-lifecycle figure — the capital footprint sits on the asset, never lost (no A4 breach), just located honestly.

Three instances so far:

| Case | Front-loaded cost | What the eventual recipient pays |
|---|---|---|
| **Education** | Teachers' time, facilities, materials | The professional's time, clinic materials, medicines — **not the education** |
| **Media production** | Years of crew time, sets, equipment, post | **Delivery only** — theatre maintenance, projectionist hours, print or bandwidth, power |
| **Research, infrastructure, tooling** | The build | Use, wear, and energy |

**Why downstream amortization is always the wrong answer.** It requires choosing a window (how many patients? how many viewers?) and every candidate window is arbitrary. That arbitrariness *was* OP-11, and it is also what made OP-21 (media reproduction) look hard. **The question was malformed in both cases.** Front-loading removes the division rather than solving it.

**The decisive reason, though, is computational closure**. If a hospital's construction were amortized into each patient's bill, the accounting would have to chase the construction company's costs, then the equipment manufacturer's, then the steelmaker's, then the doctors' education — **an infinite regress to the first human activity.** The accounting would never terminate. Front-loading is what makes it *terminate*: you never chase an asset's own history, because the asset carries whatever creation-cost is knowable within Aequitas and everything upstream is out of scope by construction.

> **This is the upstream face of the non-cascade rule in §3.2b.** Pollution not transferring downstream to a buyer and cost not regressing upstream to the first human are the *same* constraint: **cost attaches only to the causer, and never cascades to anyone who did not act.** Ellerman-imputation and computational closure are one principle read in two directions.

> **The boundary is capital vs. consumption, not temporal.** A cost flows to a unit only if it is *consumed* producing that unit. A durable asset's *acquisition* is capital (front-loaded); only what it *consumes now* — energy, materials used up, wear — is a flow. The two are told apart by **physical fate**: does the thing survive the process? A drill bit that survives is capital; the oil it burned is consumption. Auditable via IC-4 (fate closure), not by the producer's declaration — which closes the *consumption-launderer* (reclassifying a used-up input as capital to move its debit off the unit).

**Corollary — pre-Aequitas assets**. A cooperative taking over a 50-year-old hospital cannot reconstruct the architects' fees or the original currency costs. The asset *enters* Aequitas and accrues history from genesis forward; the pre-genesis past is unrecoverable — the same cutoff, in a new domain. v0.7 makes the entry precise:

- **Recording a "before" object is a *choice*.** Leave it unrecorded → it is invisible to Aequitas, with no registered ownership (a thief inherits no debt; fine for clothing and heirlooms one intends to keep). But an object cannot receive *creditable work* without a record — repairing an old fridge requires the fridge to exist in the ledger so the repairer can be credited.
- **When recorded, the entry is an expert *estimate*, not zero and not a reservoir extraction.** A qualified estimator reconstructs the construction labour and materials **plus all subsequent rehab**, at `basis: modelled`, low confidence, superseded by real records later. **The estimator is credited** for the estimation work. The dollar purchase price is worthless as a basis — estimate the material/labour cost instead.
- **Genesis is a distinct origin-terminus, not a reservoir.** A pre-Aequitas object did not enter *from a commons inside the system*; it enters as an estimated **genesis entry**, which is a legitimate endpoint for backward origin-tracing (IC-3, origin closure, conformance row 7) alongside a reservoir extraction — but it is not dressed up as one.
- **Original-construction harm does not transfer to the current holder** (§3.2b). A 200-year-old building may have been raised with slave or unrecorded labour and its era's pollution; the *current* holder bears only what they effected during their tenure (the gas stove's methane), never the original construction's suffering or emissions.
- **The reconstructed creation-cost is holding-time-split, not dumped whole on whoever holds it now** (§4.5). The estimator's figure — original construction labour and materials *plus* all subsequent repairs and modifications over the asset's life — is the asset's **creation-cost**, and it settles by the ordinary holding-time waterfall: each holder's permanent share = **their holding-duration ÷ the asset's total life**. A person who owned a property for 20 of the 200 years it has existed therefore carries **10%** of its construction-and-rehab debit, not all of it. This is *why* the pre-Aequitas entry cannot bankrupt a new owner: entering an old asset does not import its whole two-century debit onto the person at the door — it imports only their tenure's slice, and earlier holders' shares stay pinned to those holders (estimated on the same terms, §4.1) or ride the asset as an un-attributed remainder until its life completes (no A4 (no externalities) leak). Rehab is split the same way, over the years since *that* rehab, so a repair done a decade before you arrived is mostly not yours either.
- **An auditor may create the record without the owner's consent** (A7 — everyone is accounted). A reluctant owner's mansion can be entered from estimates of its size and construction; if the owner later joins, they may *refine* it (with contractor records, motivated to show the debt is lower than estimated) — but the only route to a favourable credit:debit ratio is to **transfer the debt** to others, not to hide the asset.

**The consequence for media is worth spelling out.** Pledgers replace studios and investors, and **they receive no profit and cannot receive one** — so there is no mechanism by which a popular film gouges its audience at the box office. A production company's only return is recognition, which converts into demand and pledges for the next work. That is the entire incentive, and it points at making something good rather than something extractive.

**⚠️ Cold start.** Pledges follow reputation, so a first-time filmmaker attracts none — structurally similar to the problem unknown creators already face with capital. The barrier is far lower (attention, not money) and the ladder is real: make small unpledged work, accrue feedback (§4.6), then attract pledges. But it should be stated honestly rather than assumed away.

---
*Status: provisional — OP-5, OP-11*
*Source: `00-strategy/Aequitas_Foundations_v0.2.md` §10 OP-5; design session 2026-07-31*
