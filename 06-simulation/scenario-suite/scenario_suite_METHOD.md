# Societal-Scale Scenario Suite — Method & Plan

> **Status:** planned 2026-08-10. Five societal-scale simulations requested by the author.
> **Anchored on:** the completed median-lifestyle result (`median_lifestyle_RESULTS.md`, ~1,600 h/adult·yr, ~½ foreign; footprint 12.4 t CO₂ / 19 t materials / 2.2 ha / 1,600 m³) and the built disparity-ceiling sim (`disparity_ceiling_sim.py` / `DISPARITY_CEILING.md`).
> **Governing docs:** Foundations v0.11, Overview v0.8, Objections v0.12.

---

## 0. The governing constraint — cost, not value; no planner

Aequitas is a theory of **cost, not value**, and has **no central planner**. "Highest standard of living," "wasteful vs essential," and "stolen labor" are value/planning framings that Aequitas does not natively produce. Every sim in this suite is therefore built as **one of two legitimate object types**, never as an Aequitas verdict:

1. **Physical feasibility envelope** — what is materially *achievable* given labor, energy, and resource stocks (Q1, part of Q3).
2. **Explicit counterfactual with exogenous dials** — what *happens if* the demand side (pledges) shifts, with the shift declared as a scenario knob, not decreed by the system (Q2, Q5, Q4's ρ).

If a sim cannot be cast as one of these, it is smuggling in a planner and fails universality/decentralization — do not ship it.

### Shared architecture
- **Q1 / Q2 / Q5 run on ONE engine:** an EXIOBASE MRIO + embodied-labour-hours + resource/energy-constraint model — a direct extension of the C3 estimation engine (`estimation_engine.py`, `exiobase_loader.py`, forward solver already validated against pymrio to machine precision). Build once, query three ways.
- **Q4 extends** the disparity-ceiling sim (ρ-sweep, IC-7 cap).
- **Q3 is standalone** (a focused LCA→hours calc).

### Sequence (all five, as a programme)
**Q3 → Q4 → [build shared engine] → Q1 → Q2 → Q5.**
Rationale: Q3 is a fast concrete win; Q4 is a cheap striking headline on already-built machinery; then the heavy engine amortizes across Q1/Q2/Q5.

---

## Q3 — Labour debt of plastic pollution (h/ton) + recycling cost

**Type:** feasibility/LCA envelope. Instantiates §3.3 (stock-dependent pollution debit) + §3.6 (recycling, product-as-pollution).

**Method.** For 1 tonne of common polymers (PET, HDPE, PP, LDPE, mixed):
1. **Virgin production debit** — embodied hours (feedstock extraction, cracking, polymerization) via EXIOBASE/refinery slice reuse.
2. **Recycling debit** — hours to collect, sort, wash, reprocess per §3.6 (mechanical vs chemical). Output re-enters as a low-cost co-input; recyclers are **credited**.
3. **Cleanup/remediation debit** — hours to remove and remediate per §3.3 stock rule. Three boundaries, reported as a **range**:
   - (a) **Managed landfill** containment (lowest).
   - (b) **Environmental macro-cleanup** — Ocean Cleanup–class $/ton → hours via wage/margin bridge.
   - (c) **Microplastic remediation** — effectively **unremediable** at current tech → debit is near-permanent and dominates. *This is the headline, not a bug: §3.3 says the weight floats with the stock, and the stock barely clears.*

**Data (mostly on hand / cheap to get):** polymer LCA energy (literature), recycling process energy, Ocean Cleanup cost figures, EXIOBASE plastics sector, wage/margin bridge (already built for Track 3).

**Key decisions flagged (not blocking):**
- Remediation boundary → **report all three; lead with the microplastic near-permanence result.**
- Recycling: mechanical (realistic) vs chemical (energy-hungry) → report both.

**Output:** hours/ton table — virgin vs recycled vs cleanup(×3) — showing (i) recycling is cheap relative to cleanup, (ii) cleanup is cheap relative to letting it become microplastic, (iii) the §3.6 incentive gradient (buy durable, fund recycling) falls straight out of the numbers.

**Effort:** LOW. ✅ First to build.

---

## Q4 — What % are past the point of a permanently locked ledger

**Type:** counterfactual (ρ-dependent). Extends `disparity_ceiling_sim.py`.

**The correct operationalization (see §3.5 flag).** "Permanently negative ledger" ≠ debit > credit (that's everyone, always — second law). It means the **lifetime efficiency ratio D:C sits permanently outside the network's tolerance band ρ**, so discretionary consumption is **locked to the basic-needs floor for the rest of that person's life** — no achievable remaining-lifetime work, plus divesting all material property (which only dilutes via holding-time, and takes years), brings the ratio back in band.

**Material-only, per A1.** Financial instruments (stocks, bonds, crypto, options) are abstract/fiat and **do not enter the ledger**. The previously-wealthy carry only:
- **Lifetime permanent consumption/pollution debit** — their real physical consumption footprint, accumulated (never discharges, §3.2).
- **Material property debit** — estates, land, vehicles, goods: material component dischargeable on transfer; creation-cost/holding-time share permanent per holder (§3.2, §4.5).
- **Credit** — lifetime hours: self-care baseline (large, ≈equal for all — self-care credit ≈4× productive labour per the anchor) + productive work hours.

**Method.**
1. **Build lifetime ledgers** from distributions: consumption footprint by wealth/income percentile (CE + SCF + WID), material-holdings by percentile (SCF, *material only* — strip financial assets), lifetime work + self-care hours.
2. **Divest test** — for the top tail, model transferring all material property; compute residual permanent debit (consumption history + accrued holding-time shares) vs max remaining-lifetime credit.
3. **ρ-sweep** — for each ρ in the band, compute the D:C threshold and the fraction of the population permanently above it. Report US and world (WID global).
4. **Predicted findings to test:** (a) stripping paper wealth collapses the 10⁶× tail toward a **bounded material tail** (~10²–10³×; footprint mean/median ≈1.20 in our data); (b) **most people gain** discretionary room by joining (below cohort average); (c) a **thin top slice** is permanently locked — and the size of that slice is the answer.

**Key decisions flagged:**
- Lifetime vs annual ledger horizon → **lifetime** (the question is about permanence).
- ρ is exogenous → **sweep it; report the % as a function of ρ**, not a single number.
- World data is coarser (WID) → report US (firm) and world (indicative).

**Output:** % of US / world population past the permanent-lock point, as a curve over ρ; plus the tail-compression result (paper→material).

**Effort:** LOW–MED. Second to build.

---

## The shared engine (build after Q4, before Q1)

An extension of the estimation engine: EXIOBASE MRIO → per-sector **embodied labour-hours**, **energy**, and **material/land/water** intensities, with the capacity to (a) drop trade (autarky), (b) re-shore or forgo imported output, (c) reallocate final demand across sectors, and (d) apply resource/energy stock caps. Validated pathway already exists (forward solver = standard EEIO). This single object answers Q1, Q2, Q5.

---

## Q1 — Max autarkic US standard of living (egalitarian, physical)

**Type:** physical feasibility envelope. **Metric chosen by author: the highest level EVERYONE can hold at once, in physical services** (kWh/person, m²/person, kg protein, healthcare access, mobility), bounded by the disparity ceiling — not a dollar figure, not a top-tail max.

**Method.**
1. **Drop imports.** Zero the foreign block of the US MRIO. The median anchor says ~½ of the 1,600 h/adult is currently foreign → the immediate question is what fraction can be **re-shored** at domestic labour/energy/resource cost vs what is simply **forgone** (no domestic substitute — e.g. certain minerals, tropical goods).
2. **Bind by the scarcest input, not hours.** The anchor already found **labour is abundant** (self-care credit ≫ productive labour) and **materials/energy are the binding scarcity**. So the envelope is set by domestic energy (esp. renewable ceiling), arable land, water, and non-substitutable minerals — solve for the max uniform physical bundle each of these permits.
3. **Distribute under the ceiling.** Apply the 24/F disparity bound so the "standard of living" is the *universal* level, not an elite peak.

**Key decisions flagged:**
- Re-shorable vs forgone import split → derive from domestic resource availability; mark non-substitutables explicitly.
- Energy basis: current mix vs renewable-only ceiling → **report both** (renewable-only is the sustainable envelope).
- Timeframe: static snapshot (2023 tech) — note as a limitation.

**Output:** a per-person physical service bundle (energy, housing m², diet, mobility, healthcare) that the continental US can sustain autarkically and egalitarianly, vs today's median and top-decile bundles.

**Effort:** HIGH.

---

## Q2 — Labour-time lost to exploitation / cronyism / capitalism / war

**Type:** counterfactual accounting (size the currently-captured/wasteful pool).

**Reframe (loud, per the axioms).** Aequitas has **no surplus-value and nothing to steal** — credit is non-transferable (A3), so "stolen labor-time" is not an Aequitas quantity. The honest, computable question: **how large is the pool of human hours currently (a) captured by non-working asset-holders or (b) spent on activity that exists only because money is extractable — a pool that is structurally impossible under Aequitas?**

**Components (each an exogenous, itemized bucket):**
- **Capture / rent** — profit + interest + rent share of national income → hours-equivalent (the labour whose product accrues to non-workers).
- **Guard labour** — Bowles & Jayadev: supervisors, security, military, prisons, unemployment as enforcement → hours.
- **FIRE / cronyism** — finance, insurance, legal-adversarial, lobbying, advertising → hours that are pure positional/extractive overhead.
- **War** — military production + service hours (direct + supply chain).

**Method.** BEA income-side accounts → capture share → hours via economy-wide labour intensity; ILO/BLS occupational hours for guard-labour and FIRE buckets; military I-O for war. Report as **% of total employed hours** and **hours/adult/yr** freed.

**Key decisions flagged:**
- Double-counting across buckets (a soldier is both "war" and "guard labour") → **de-dupe explicitly; report a low/high band.**
- Some FIRE/advertising is genuinely coordinative, not pure waste → mark the contestable fraction; do not overclaim.

**Output:** the freed-hours pool (band), US and world, and what §Q5 shows it could instead build.

**Effort:** MED.

---

## Q5 — World SoL if wasteful→essential labour is reallocated

**Type:** explicit counterfactual with an **exogenous taxonomy dial** (author's decision: I propose the buckets, mark every contestable call, and treat the split as a scenario knob — *not* an Aequitas verdict; under Aequitas this shift would be driven by pledges, not decree).

**Proposed taxonomy (v1 — every row is contestable and flagged):**

| Wasteful (candidate to shrink) | Essential (candidate to grow) |
|---|---|
| Warfare / arms | Healthcare |
| Luxury / positional goods | Food & clean water |
| Policing / repression *(⚠ vs legitimate public safety — split needed)* | Housing (durable) |
| Disposable / short-lifespan goods | Quality, durable clothing |
| Fossil-fuel extraction | Renewable energy + grid |
| FIRE / advertising overhead (from Q2) | Education / care |

**Method.**
1. Map ILO/EXIOBASE global sector hours into the two buckets (+ a large **neutral** remainder — most labour is neither).
2. **Reallocate** the wasteful pool (Q2's freed hours) into essential sectors at those sectors' embodied-hour intensities → compute the **additional essential output** (housing units, healthcare-hours, renewable GW, protein) achievable.
3. Distribute under the disparity ceiling → the resulting **universal physical bundle**, vs today's world median.

**Key decisions flagged:**
- The taxonomy is the whole ballgame → **every boundary reported as a dial; run a sensitivity pass** (e.g. reclassify half of "policing" as essential and show how the result moves).
- Reallocation frictions (retraining, capital retooling) → note; the sim is an *upper envelope* on the reallocation gain, labelled as such.

**Output:** world universal physical bundle under the reallocation, with a sensitivity band over the taxonomy dials; the flagship "what the freed hours could build" result.

**Effort:** HIGH (reuses Q1/Q2 engine + Q2 pool).

---

## Cross-suite honesty ledger (things that must stay flagged)
- **No planner.** Q2/Q5's buckets and Q4's ρ are exogenous dials; Aequitas would set them via pledges. Never present them as system outputs.
- **§3.5.** "Negative ledger" is an efficiency-ratio lockout, never debit>credit.
- **A1.** Financial instruments are non-material and excluded throughout.
- **Static snapshots.** All use 2023-vintage tech/data; no dynamic adjustment. Envelopes, not forecasts.
- **World data is coarse.** US results are firm; world results are indicative.
