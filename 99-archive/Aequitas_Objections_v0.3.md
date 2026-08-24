# Aequitas — Objections Register

> **Version:** 0.3 *(numbered to track `Aequitas_Foundations_v0.3.md`; v0.1–v0.2 were same-session drafts, never released, nothing to archive)*
> **Date:** 2026-08-01
> **Status:** Working. Derived from a comparative pass over Participatory Economics, Cockshott & Cottrell, Sraffa/Steedman, LCA allocation theory, Kantorovich, Ellerman, Odum, and Sensorica — then extended (§4) with the **field record** of local currencies and time banking.
> **Purpose:** one place holding every serious objection to the Foundations, its source, the axiom it attacks, and its status. Nothing here is settled unless marked settled.
> **Companion:** `Aequitas_Foundations_v0.3.md` §10 · `OP-16_authorization_stress_test.md`

---

## Status board — as of Foundations v0.3

Read this first; the sections below hold the argument.

| | Item | Status |
|---|---|---|
| 🔴 | **OP-17 — Joint production allocation** (P1) | **Open. Blocks C3 and sits on the critical path.** |
| 🔴 | **OP-10 — Weighting-model governance** | Open. Largest hole in A8; entangled with OP-9. |
| 🔴 | **OP-18 — Responsibility is not divisible** (P6) | Open. Hours-worked now *declared* a convention — Foundations §1.1. |
| 🟠 | **OP-16 — Onerousness gap** | **Half solved.** A2 v0.3 makes training paid work → skill half fixed. Tedium half open; leading candidate is hour-ceiling differentiation. |
| 🟠 | **OP-6 — Feedback mechanics** | Promoted. Now also carries signal-flooding, inherited from OP-20. |
| 🟠 | **P4 — Coordinator class** | Open, constrains OP-1. **The *producer*-class variant was withdrawn** — credit tracks hours, not tonnage. |
| 🟢 | **OP-9 / P5 — Preference revelation** | **Substantially answered.** Pledges (§6.4) + scarcity-as-debit. Needs writing up, not inventing. |
| 🟢 | **P7 — "theory of value"** | **Fixed.** §0 and A1 reframed as cost. |
| 🟢 | **W1 — A3 defeats the sink problem** | **Claimed** in §7.6. |
| 🟢 | **P9 — §11 read as a local currency** | **Fixed.** §11 hardened. |
| 🟢 | **S1 — "does this need a Paul Glover?"** | **Adopted** as the fourth screening question, §2. |
| ✅ | ~~OP-11 — Training amortization~~ | **Dissolved** by the A2 amendment. No downstream cost to amortize. |
| ✅ | ~~OP-5 — Education~~ | **Dissolved**, same amendment. |
| ✅ | ~~OP-8 — Enrichment firewall~~ | **Dissolved.** Feedback was never credit. Reframed: *can feedback be bought?* |
| ✅ | ~~OP-19 — Saturated producer~~ | **Resolved** by pledges. |
| ✅ | ~~OP-20 — Unobservable work~~ | **Closed** by IC-7 + conservative weighting + pledges. No new mechanism. |
| ✅ | ~~OP-21 — Media reproduction~~ | **Closed** by front-loading (§6.2a). The division question was malformed. |
| 🔽 | **OP-22 — Provenance vs. privacy** | **Narrowed** to: minimum audit disclosure set. C7 implementation, not foundational. |

**Six problems closed or dissolved; two of the three headline divisions remain.** Note the pattern in what closed: **every dissolution came from removing a division, not from computing one.** Front-loading removed the training and media splits; feedback-is-not-credit removed the category split. What remains open (OP-17, OP-18) are the divisions that **cannot** be removed — which is the register's §0 thesis, confirmed four times over.

---

## 0. The headline finding

**Aequitas's hard problem is division, not measurement.**

Every predecessor that tried to account in physical units died at the same place, and it was never the measuring. Totals are physically well-defined: a refinery consumed *X* joules and emitted *Y* tonnes; a team of nine built the bridge. **The splits are not.** How much of the refinery's debit belongs to the diesel versus the naphtha? How much of the bridge belongs to the welder versus the surveyor? Physics returns no answer, because "belongs to" is not a physical relation.

The Foundations currently assume this away. §3.4 treats granularity as a matter of *resolution* — record what is known, estimate the rest, refine forever. That is true of measurement and false of allocation. **No amount of better instrumentation resolves a co-product split, because the indeterminacy is not epistemic.** Refining forever converges on nothing.

This shows up twice, at two levels, and they are the same problem:

| Level | Question | Register entry |
|---|---|---|
| **Product** | Which output of a joint process carries which share of the debit? | **P1** |
| **Person** | Which member of a cooperating team carries which share of the credit? | **P6** |

Everything else in this register is downstream or peripheral by comparison.

---

## 1. Register

Ranked by how much of the theory fails if the objection stands.

---

### P1 — Joint production has no physical allocation
**Attacks:** A1, A5, and the **universality criterion** directly.
**Sources:** [Sraffa/Steedman/Morishima on negative labour values](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) · [ISO 14044 allocation hierarchy critique](https://link.springer.com/article/10.1007/s11367-016-1161-2) · `02-research/joint-production-allocation-problem.md`
**Status:** 🔴 **Open, and the most dangerous item in the project.**

A process yields beef and leather, or mutton and wool, or the full slate of refinery fractions. One physical event, several outputs, one pool of debit. Splitting it by mass, by energy content, by exergy, or by economic value gives **four different answers, and none of them is more physically true than the others.** ISO 14044 ranks the options and then, when the physical ones are "inappropriate," falls back to **market price** — which A5 forbids, since price is supposed to be the *output* of the accounting, not an input to it.

This is not an EEIO artifact. The estimation-engine note already flagged that USEEIO allocates by price; the correct reading is worse. **EEIO allocates by price because there is nothing else to allocate by.** Swapping the data source does not escape it.

The classical result is the sharp form: under joint production, labour values can go **negative** — a commodity whose production "contains" less than zero labour. Any single-substance cost accounting inherits this. Aequitas is a single-substance cost accounting.

**Candidate responses, none yet worked out:**
1. **Refuse to split.** Carry debit as an irreducible *set* attached to the joint output bundle, and only resolve it at the point of consumption, by the consumer's own choice of what they took. Preserves universality; explodes the parcel model in C1.
2. **System expansion / avoided burden.** ISO's preferred escape: credit the co-product with the debit of whatever it displaces. Requires a counterfactual — what *would* have been produced — which is a judgement, not a measurement.
3. **Declare an allocation rule as core protocol** and accept that it is a convention. Honest, but it is an ad-hoc rule, and universality forbids ad-hoc rules. If this is the answer, **say so loudly in §1 rather than hiding it in the estimation engine.**

**Test before adopting anything:** run the same rule over a slaughterhouse, an oil refinery, and a combined-heat-and-power plant. If it needs a different justification in each, it is wrong.

---

### P6 — Responsibility for joint work is not divisible either
**Attacks:** A1's attribution claim ("attributable to the people who caused the movement"), A2, C1's agent field.
**Sources:** [Ellerman, *The Labour Theory of Property and Marginal Productivity Theory*](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf) · `02-research/ellerman-labor-theory-of-property.md`
**Status:** 🔴 Open. Same shape as P1, one level up.

Ellerman is simultaneously **the best philosophical ally the project has** and the source of its second-hardest problem.

The ally half: his labour theory of property grounds attribution in a juridical principle Aequitas already assumes — *impute responsibility to whoever was in fact responsible*. That is a far stronger and more defensible footing for A1 than Marx, and it is the correct citation for why credit follows the doer. It also independently derives the anti-capitalist result: if labour is de facto responsible for production, labour must be de jure responsible, so the employment contract is invalid in the same way a voluntary-slavery contract is.

The problem half: Ellerman is explicit that de facto responsibility for a joint product is **joint and non-decomposable**. The whole team is responsible for the whole output. There is no factual measure that says the welder caused 40% of the bridge. Aequitas needs exactly that number to credit nine people separately.

Note that **hours worked is an allocation convention, not a measurement** — the same category error as splitting a refinery by mass. It is defensible, it may well be the right convention, but it must be *named* as a convention in §1, not presented as a physical fact.

---

### OP-16 — The onerousness gap *(new)*
**Attacks:** A2, and the system's ability to allocate labour at all.
**Sources:** [Hahnel, *In Defense of Participatory Economics*](https://znetwork.org/znetarticle/in-defense-of-participatory-economics-by-robin-hahnel/) · `02-research/participatory-economics.md`
**Status:** 🔴 Open. New — not previously logged.

Parecon remunerates **duration, intensity, and onerousness** of effort. Aequitas explicitly refuses to rate-scale labour (A2) and resolves the differences materially instead: hard work → extra calories, skilled work → training cost, hazardous work → retroactive health debit.

**That resolution is elegant and it is incomplete.** It covers exertion, skill, and hazard. It does not cover **disutility with no material signature.** Tedium, isolation, night shifts, unpleasantness, indignity. Two jobs with identical caloric burn, identical training, and identical health outcomes are credited identically per hour — but one of them nobody wants to do.

Capitalism handles this with a wage premium. Parecon handles it with a peer effort rating. **Aequitas currently has nothing**, and A2 forbids the obvious fix.

The counter-question Aequitas can put to Parecon is real and should be kept: effort ratings are [criticised as unmeasurable and as requiring pervasive surveillance and humiliation](https://znetwork.org/znetarticle/in-defense-of-participatory-economics-by-robin-hahnel/), and Aequitas's material resolution avoids that entirely. But avoiding a bad answer is not having a good one.

**Directions:** (a) accept unfilled onerous roles as a genuine cost and let automation pressure resolve them — the material-flow analogue of "if nobody will do it, it is expensive"; (b) treat volunteered onerous work as **service credit**, routing it to influence rather than to consumption ceiling, which stays inside A2; (c) admit an explicit exception and take the universality hit. **(b) looks most promising and is cheap to test.**

---

### OP-9 — Preference revelation *(previously logged, now sharpened)*
**Attacks:** A5. The Mises/Hayek line of attack.
**Sources:** `02-research/neurath-calculation-in-kind.md` · [Dapprich, *Optimal Planning with Consumer Feedback*](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · `02-research/kantorovich-shadow-prices.md`
**Status:** 🟠 Open, but **there is now a citable answer shape.**

Cost says what a thing takes. It does not rank two people who both want the last one. Under A5 the price of a unique lakeside house equals its material cost, which is absurd — demand is unbounded at that price and nothing rations it.

**Kantorovich's objectively determined valuations** are the answer shape. Shadow prices are the dual values of a constrained optimisation: they measure the **cost of a binding constraint**, not a margin extracted by a seller. Dapprich builds directly on this for scarce natural resources that cannot be reduced to labour time.

Reframed for Aequitas: **scarcity is itself a material cost.** Taking the last unit of a constrained resource imposes a real debit on everyone else — the cost of the next-best substitute, or of relieving the constraint. Recorded as a debit rather than as a margin, this is **compatible with A5 and possibly required by it.** A5 says there is no profit in exchange; it does not say opportunity cost is not a cost.

**Catch:** a dual price requires a primal optimisation, which requires an objective function, which is a social judgement. This collides head-on with the unresolved **OP-10 (weighting-model governance)** — whoever sets the objective sets every scarcity price. The two problems should be worked together, not separately.

---

### P4 — Abolishing property income does not abolish class
**Attacks:** §6.2 / OP-1, and the "surgical, keep functional institutions" positioning in §8.
**Sources:** [Albert & Hahnel on the coordinator class](https://znetwork.org/znetarticle/parecon-and-anarcho-syndicalism-an-interview-with-michael-albert-by-michael-albert/) · `02-research/participatory-economics.md`
**Status:** 🔴 Open. Directly challenges a settled positioning decision.

Parecon's central historical claim is that Soviet-type systems abolished capitalists and produced a new ruling class anyway — a **coordinator class** that monopolised empowering work: planning, decision-making, conceptual labour. Their institutional answer is balanced job complexes, distributing empowering and rote tasks across everyone.

Aequitas is more exposed to this than any other system in the comparison set, for two reasons:

1. **§8 is a deliberate decision to keep existing institutions** — municipal government, planning bodies, civil service — and change only their economic nature. Those are precisely the coordinator-class institutions.
2. **OP-1 converts service credit into influence.** People in empowering roles accumulate service credit; service credit accumulates governance weight; governance weight protects the roles. **That is a coordinator-class flywheel, and the current draft treats it as a feature.**

This does not mean adopting balanced job complexes — they carry [their own critique](http://libcom.org/blog/workers-critique-parecon-11042012) as compulsory labour discipline. It means **OP-1 cannot be designed without an explicit answer to "who games this?", and the answer is: whoever already holds an empowering role.** Of the three candidates in §6.2, *proposal power with universal suffrage* is the only one that structurally separates agenda-setting from deciding, and on this objection it is clearly the strongest of the three.

---

### P7 — "Nothing else is value" is the sentence that killed every predecessor
**Attacks:** §0 and A1 — **as worded.** Not the substance.
**Sources:** [Ayres on emergy ignoring demand](https://www.centre-cired.fr/en/is-emergy-really-a-theory-of-value-2/) · [Sensorica's abandonment of "value accounting"](https://wiki.p2pfoundation.net/Open_Value_Accounting) · `02-research/technocracy-energy-accounting.md`
**Status:** 🟡 **Cheapest fix in the register. Fix it in v0.3.**

Every single-substance objective theory of value has been rejected on one ground: **supply-side only, ignores demand.** Odum's emergy, Technocracy's energy certificates, the labour theory of value. The refutation is a stock move and takes one sentence.

Aequitas is presenting itself as the newest member of that family, **and it does not have to be.** The Foundations open with "Nothing else is value" — which invites the standard refutation — while the actual theory is doing something narrower and much more defensible: **it is a theory of cost, not of value.** Cost is what a thing takes from the world. Value is what someone thinks it is worth, and Aequitas already routes that through Enrichment and voluntary direction of surplus (§6.3), where it belongs.

Confirmation from practice: Sensorica, the most developed real-world contribution-accounting project, **renamed its "value accounting system" to a "contribution accounting system"** on exactly this reasoning — value is a subjective experience and cannot be counted, contributions can.

**Recommended amendment to §0:** *Aequitas is a universal accounting of material flows. Every credit and debit records matter and energy moving through the world, attributable to whoever caused the movement. **Cost is nothing other than this.*** Then state explicitly: **Aequitas is a theory of cost. It makes no claim to be a theory of value, and Enrichment exists precisely because value is not cost.**

This costs nothing, loses no substance, and removes the single easiest attack on the project.

---

### P5 — Cockshott's demand lever is one Aequitas cannot pull
**Attacks:** A5, tractability.
**Sources:** [*Towards a New Socialism*](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) · [Mises Institute review](https://cdn.mises.org/qjae7_1_6.pdf) · `02-research/cockshott-cottrell-labour-time.md`
**Status:** 🟠 Open. Half good news.

**Good news, and it should be cited:** Cockshott & Cottrell's whole contribution is that labour-time calculation at national scale is **computationally tractable** with sparse-matrix methods and modern hardware. That is a direct, citable answer to objection #3 in the Neurath note (tractability of retroactive re-weighting). Mises's argument was in-principle; the empirical scale objection has been answered by people who did the arithmetic.

**Bad news:** their consumer-goods algorithm sets prices to clear the market and then **contracts production wherever market-clearing price falls below labour value.** The gap between price and value is their demand signal. **A5 collapses that gap to zero by definition**, so Aequitas inherits their problem with one fewer instrument than they had. Their critics' central line — [calculation in labour values does not factor in demand, and supply without demand is blind](https://arbeitszeit.noblogs.org/en-GB/post/2023/09/10/towards-an-old-socialism/) — lands on Aequitas harder than on them.

This is the same wound as OP-9. Fixing OP-9 via scarcity-as-debit fixes this too. They should be treated as one problem.

---

### P8 — The Hayek residue
**Attacks:** the decentralization claim.
**Status:** 🟠 Open, unchanged, but the comparison sharpens it.

Parecon's Iteration Facilitation Board is [attacked as implausible](https://ejpe.org/journal/article/view/867) for assuming a body can announce opportunity costs for all goods, resources, labour categories, and capital stocks. **Aequitas's weighting-model maintainer is structurally the same object** and is exposed to the identical objection. The verification ladder answers *data collection* — it gathers locally rather than centrally. It does not answer *model maintenance*, which remains central by default.

Same root as OP-10. The strongest available reply is competing local variance under A8: multiple weighting models, openly published, each recomputable by anyone from the same log. **That reply is asserted in A8 but nowhere specified.** Specify it.

---

## 2. What this changes

*All items below marked ✅ shipped in `Aequitas_Foundations_v0.3.md` on 2026-08-01.*

| Item | Action | Where |
|---|---|---|
| ✅ P7 wording | **Amend §0 and A1 — theory of cost, not value.** Cheap, high value. | Foundations §0, A1 |
| P1 joint production | New open problem, blocking C3. Cannot publish a debit-cost figure without an allocation rule. | OP-17 |
| P6 responsibility split | New open problem. Name hours-worked as a convention, not a measurement. | OP-18 |
| OP-16 onerousness | New open problem. Candidate (b): route onerous work to service credit. | §6.2 |
| OP-9 preference revelation | Promote from "proposed" to live, with the Kantorovich framing. Work jointly with OP-10. | §10 |
| P4 coordinator class | Constrains OP-1. Proposal-power-with-universal-suffrage is now the favoured candidate. | §6.2 |
| P5 tractability | Cite Cockshott & Cottrell in the academic paper as the answer to the scale objection. | Doc 2 |
| Ellerman | Adopt as the philosophical grounding for attribution in place of Marx. | Foundations §1, academic paper |
| **W1 — A3 vs. sinks** | **Claim it in §7.** Retires "these always die" at zero cost. | Foundations v0.3 |
| **P9 — §11 wording** | State that the overlay computes what money cannot. Distinguish from local currencies. | Foundations v0.3 |
| **OP-16 + OP-11** | Merge — one problem. Escalate: field evidence, not theory. | §10 |
| **OP-19 / OP-6** | Promote OP-6. Enrichment is the motivation system, not a garnish. | §6.3, §10 |
| **S1** | Add "does this need a Paul Glover?" as a fourth screening question. | `CLAUDE.md` advisory duties |

---

## 4. The field record — added v0.2

Source: `02-research/local-currency-experiments.md`. Ithaca HOURS, Burlington Bread, time banking, Wörgl, WIR, Sardex, LETS. Roughly a century of people building these things and finding out what breaks — the closest thing the project has to an experimental literature.

**It does not show one failure repeated. It shows three, and they are not the same problem.**

| Class | What breaks | Cases | Aequitas exposure |
|---|---|---|---|
| **1 — Valuation** | Flat-hour crediting cannot recruit skill | Warren; **time banking, 45 years** | 🔴 **Confirms OP-16 empirically** |
| **2 — Circulation** | Scrip pools at sinks and stops moving | **Ithaca, Burlington** | 🟢 **Structurally immune — A3** |
| **3 — Institutional** | Founder dependency, state suppression, obsolescence | Ithaca (Glover); Wörgl (banned) | 🟠 New screening question |

---

### W1 — A3 defeats the sink problem *(a win, currently unclaimed)*
**Status:** 🟢 **Settled in our favour. Write it into §7.**

Ithaca and Burlington both died of the *same specific mechanism*, and it was not valuation. Scrip flowed toward businesses whose own inputs came from outside the network — a café buys coffee in dollars — making them one-way sinks. Ithaca's remaining businesses were **"drowning in Hours"**; Burlington Bread **piled up at Muddy Waters and Sugar Snap** with no way to recirculate. Circulation halted at the enthusiastic early adopters first.

**This failure cannot occur in Aequitas, because there is no medium of exchange.** Credit is non-fungible and never moves (A3); only debit moves, attached to the thing it belongs to. Nobody drowns in credit they cannot spend because nobody ever receives credit *from* anyone.

It costs nothing to claim — it is a consequence of an existing axiom, not a new mechanism — and it retires the most common practical objection to alternative economics ("these always die"). **The correct answer is: those died of circulation, and we do not circulate.**

Corollary, from Wörgl: the scrip was suppressed by Austria's central bank **for working**, under the legal-tender monopoly. Aequitas has no issuer, no notes, and nothing to counterfeit, so that instrument does not fit it. **The `CLAUDE.md` ban on calling Aequitas a currency now has a historical rationale, not just a branding one.**

---

### OP-16 — upgraded from theoretical to empirical
**Status:** 🔴 **Escalated.** The strongest single result in this pass.

Time banking values **every hour identically regardless of who contributes it** — exactly A2's flat hour. The [2025 PLOS One scoping review](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0322760) documents the outcome across the literature: **skill mismatch**, skills in chronic short supply, no guarantee the bank meets anyone's actual demand, plus credit hoarding and poor recognition of diverse skills.

Warren's 1830 failure is dismissible as one man in one storefront. **This is forty-five years, dozens of countries, and a peer-reviewed literature — and flat-hour crediting still fails to recruit skilled labour.**

Aequitas's answer differs from time banking's and must be stated precisely: skill is not rate-scaled, but **training cost flows downstream into the recipient's debit**, so the doctor's hour *costs* more while crediting the same. **That fixes the price side and leaves the supply side untouched.** Why train for ten years if the hour credits identically afterward?

**OP-11 (training amortization) and OP-16 are one problem, not two.** Merge them.

---

### OP-19 — The saturated producer *(new)*
**Attacks:** A3, §6.3. **Status:** 🟠 Open.

Immunity to circulation sinks is not immunity to **saturation**. A high producer eventually holds credit that raises a ceiling they are nowhere near — marginal credit that does nothing for them. Ithaca's businesses drowned in HOURS they could not spend; Aequitas's most productive people can drown in headroom they do not want.

Capitalism's answer is accumulation, which A3 forbids **by design and correctly**. Enrichment (§6.3) is the intended answer: surplus gets *directed* rather than *held*.

**Consequence: Enrichment is not a decorative third credit type. It is the entire motivation system for anyone past their own consumption ceiling** — which is to say, for exactly the people the economy most depends on. **OP-6 (enrichment mechanics) is therefore far more urgent than its §10 ranking implies. Promote it.**

---

### W2 — WIR and Sardex give the MVP a target shape
**Status:** 🟢 Usable now.

The only two long-running successes share a profile the failures lack: **B2B rather than B2C**, trading inside **dense input loops** so no participant is a one-way sink, on **mutual credit** (balances start at zero, created in the act of trade) rather than issued scrip. WIR: 1934–present, ~60,000 businesses, CHF 1.43bn (2013), and demonstrably **countercyclical**. Sardex: 4,000+ businesses, ~€50m/yr, explicitly modelled on early zero-interest WIR.

If §11 ever needs a first *real* deployment rather than an overlay, **a dense B2B supply-chain cluster is the shape the field record endorses, and a downturn is the moment.**

---

### P9 — §11 is one hair from the trap that killed all of them
**Attacks:** §11 (the MVP). **Status:** 🟡 Wording fix, like P7.

Every case here was **pegged to and parasitic on fiat**. One HOUR was *defined* as $10 — the Tompkins County average wage. Bread mirrored dollars in slices. None was ever an independent unit of account; they were national currency with a local-loyalty restriction, which is why they added little and died quietly.

**Foundations §11 proposes "a parallel overlay on existing commerce."** Read cold, that is the same sentence. The saving difference is real — Aequitas's overlay computes a number money *cannot* produce, the true debit-cost — but **§11 does not currently say so**, and it should, explicitly, to distinguish the MVP from the entire failed complementary-currency lineage instead of resembling it.

---

### S1 — "Does this need a Paul Glover?"
**Status:** 🟢 **Adopt as a fourth screening question.**

Ithaca's decline is attributed first to **Glover relocating**. Glover himself said every local currency needs at least one full-time networker to "promote, facilitate and troubleshoot." The system did not maintain itself; it was maintained by one enthusiast, and it died when he moved.

That is precisely criterion 3 (fecundity), in a sharper and more testable form. **Apply it to every proposed mechanism alongside universality, decentralization, and "who games this?"** The existing trust model — *auditing is credited work* — is the right shape of answer, because it pays the maintainer from inside the system rather than from goodwill.

---

## 3. Not yet examined

Named so they are not silently skipped:

- **Ostrom** — polycentric governance, commons design principles. Bears on A8 and OP-10, likely favourably.
- **Georgescu-Roegen** — entropy and the economic process. Bears on whether material flows are conserved quantities at all.
- **Lange–Lerner** market socialism, and why Hayek rejected it. Queued in the Neurath note.
- **Nove**, *The Economics of Feasible Socialism* — the standard practical objection to any comprehensive planning scheme.
- **Graeber**, *Debt* — the anthropology of ledgers and of debt cancellation. Bears on permanent consumption debit.
- **Sensorica** in depth — the closest working implementation; its practical conflicts are worth more than its design docs.
- **WIR + Sardex** on their own — the only long-running successes, and the only cases where the loops actually closed.
- **Banque du Peuple post-mortem** — still outstanding from the Proudhon note. *The Burlington Currency Project: A History* is a rare self-authored post-mortem and the nearest available substitute in the meantime.
- **Utopia OH / Modern Times NY** — Warren's colonies, still outstanding.

---

*End of v0.1.*
