# External Critique of Aequitas — First Outside Review

**Version:** 0.2
**Type:** third-party review (record)
**Source:** an outside reviewer, supplied by the author, 2026-08-09. Unattributed. Reviewing the Overview v0.5 / Foundations v0.8 versions.
**Retrieved:** 2026-08-09

> **Why it matters.** This is the first substantial read of the theory by someone outside the project. It largely *confirms* problems the project had already flagged for itself — which is itself a good sign — and it drove the schedule changes recorded in `NEXT.md`. Its single stated priority: **write the reply to the classic "you can't run an economy without prices" objection, and add a diagram of how debit is categorised.**
>
> *This note is a faithful re-presentation of the reviewer's comments, with the project's internal shorthand spelled out in plain words so anyone can follow it. Concepts referred to by code in the original are named and briefly defined here.*

## The verdict in one line

"One of the most carefully constructed alternative economic proposals I have encountered." The reviewer praised the *method* (the honest register of unsolved problems, the habit of adversarial stress-testing, the disciplined versioning), the *ideas* (the physical-trace test, paying big costs up front, and credit that can't be transferred), and the *technical work* (the proof that the interlocking cost calculation settles rather than spiralling). The weaknesses: **it's hard to read** (too much jargon), and **it leans heavily on a piece it hasn't built yet** — the "trust networks" that do the checking, which carry a lot of weight but aren't yet specified.

## What the reviewer said works

- **The cost-versus-value distinction** (the opening move: Aequitas measures what things *cost*, never what they're *worth*) — the sharpest entry point, and the thing that heads off the most common attack.
- **The physical-trace test** (did the thing being divided leave a physical trace? If yes, measure it; if no, admit you're choosing a convention) — clean, teachable, and it neatly separates several thorny division problems.
- **The Overview's problem-then-solution structure**, the sandwich lifecycle, and the roof-repair example (working on your own property nets to zero) — concrete and memorable.
- **The format of the objections register** — exemplary, and it signals intellectual honesty.
- **The reply to the "joint production breaks labour accounting" objection** (Sraffa/Steedman) — the strongest technical result; it demonstrates rather than argues.
- **Debit following possession, front-loading big costs, and the "does this need a goal to optimise?" screening question** — all praised.

## Where it's hard to read

1. **Too many abbreviations too fast.** The opening pages are dense with internal codes (for open problems, components, axioms, integrity checks, and section cross-references), with no master glossary to decode them.
2. The "one-sentence theory" is actually a paragraph — relabel it "the core claim."
3. In-text version notes ("new in v0.5") clutter the read for a first-time evaluator — move them to a change appendix.
4. **The debit-categories section carries a lot of weight but is text only** — it wants a diagram.

## Concerns about the arguments themselves

- **The "undesirable work" problem is underrated** and should be treated as top-severity. Forty-five years of time-banking show a chronic shortage of skilled labour when every hour credits the same. All four proposed fixes are speculative; the leading one (shorter maximum hours for grim jobs) quietly reintroduces a rating — *who decides which jobs get the shorter ceiling?* **An honest admission is owed: crediting every hour equally may carry a real cost in getting unpleasant work done.**
- **The defence against "understatement drift"** (costs that are recorded too low, with nobody funding the correction) **relies on rival producers policing each other — which is unproven**, and breaks down for things with no natural rival (water treatment, care work, the baseline for how much carbon the planet absorbs). A simulation of this is load-bearing.
- **The inequality-cap result is more fragile than presented.** It depends on four things all going right: the "cost of staying alive" baseline staying in a narrow band; each party re-checking a claim through their own model so nobody can shop for a generous baseline; the privacy problem being solved (proving your hours are real without exposing your whole record); and no fraud manufacturing fake hours. **It was presented as an arithmetic certainty; it's really a *conditional* result** — *if* the privacy problem is solved, *then* the cap holds.
- **The "no externalities" principle is aspirational.** Understatement drift erodes it in practice without breaking any equation — there's a tension between the confidence of the axioms and the messiness of real measurement.
- **The trust networks are under-developed relative to how much they carry.** Verification, control of the cost model, the lists of always-creditable work, auditing, and dispute resolution *all* route through them — yet their full design is deferred. That's a large unpaid liability, and several live objections depend on it.
- **Verifying "self-care" work (staying alive) is weak.** If simply being alive earns credit *and* full power to back projects, then the incentive to invent phantom people to farm that credit becomes serious.

## Specific improvements requested

**High-impact, low-effort:** (1) a diagram for the debit-categories section; (2) consolidate "front-load big costs" into one clearly named principle; (3) standardise the language for an objection's status into one consistent set of labels; (4) fix a confusing table header in the Overview.

**Medium-effort, high-value:** (5) **write the reply to the "you can't run an economy without prices" objection now** — covering: cost isn't value; pledges reveal what people want; the sums are computationally feasible (per [Cockshott & Cottrell: labour-time](../00-strategy/GLOSSARY.md#src-cockshott-cottrell-labour-time)); and scarcity can be priced as a cost without needing a goal to optimise (per [Kantorovich: shadow prices](../00-strategy/GLOSSARY.md#src-kantorovich-shadow-prices)); (6) expand the **cold-start** problem into its own subsection (how the first pledge happens, how you build a hospital before any trust exists); (7) address the **entropy-economics gap** — the physicist-economist Georgescu-Roegen's work grounds the "the books never balance" principle in thermodynamics; a low-cost academic-credibility win; (8) clarify how **local variation coexists with a universal standard** — networks with different settings need an agreed way to trade across the boundary; write an "interoperability" section.

**Hard but necessary:** (9) **solve or scope the privacy/verification problem before presenting the inequality cap as a result** — state it as conditional; (10) **develop the trust-network model**, even a rough straw-man (how it's funded, how you join and leave, how disputes are resolved), since too many live objections depend on it.

## The reviewer's single priority

> "Write the reply to the classic prices objection, and add a visual diagram of how debit is categorised. The first defuses the most common ideological attack; the second makes the theory's core machinery legible to implementers."

## What the project did in response

Most of the high- and medium-impact items were acted on: the prices reply was written ([`00-strategy/open-problems/OP-9_calculation_reply.md`](../00-strategy/open-problems/OP-9_calculation_reply.md)), the debit-categories diagram was drawn, the inequality cap was re-stated as conditional, and a plain-language glossary layer was begun. The trust-network model and the entropy grounding remain queued.

## Related

- [Cockshott & Cottrell: labour-time](../00-strategy/GLOSSARY.md#src-cockshott-cottrell-labour-time) · [Kantorovich: shadow prices](../00-strategy/GLOSSARY.md#src-kantorovich-shadow-prices) · [Neurath: calculation in kind](../00-strategy/GLOSSARY.md#src-neurath-calculation-in-kind) · [Auditor independence](../00-strategy/GLOSSARY.md#src-auditor-independence)
