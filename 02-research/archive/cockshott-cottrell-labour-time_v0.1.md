# Cockshott & Cottrell — Computational Labour-Time Planning

**Type:** theory / computational economics
**Author(s):** W. Paul Cockshott, Allin F. Cottrell
**Published:** *Towards a New Socialism*, Spokesman Books, 1993
**Retrieved:** 2026-08-01
**URL:** [Wikipedia overview](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) · [Cockshott's blog — reply to Brewster](https://paulcockshott.wordpress.com/2017/08/28/reply-to-brewster/) · [Mises Institute review (QJAE 7:1)](https://cdn.mises.org/qjae7_1_6.pdf) · [*Towards an Old Socialism* — critique from the labour-time-accounting tradition](https://arbeitszeit.noblogs.org/en-GB/post/2023/09/10/towards-an-old-socialism/)
**Local copy:** none — the Mises review PDF and the noblogs critique are open access. The book is widely available free online; archive next.

## Why this matters to Aequitas

They are the **modern entrants in the socialist calculation debate**, flagged as a follow-up in `02-research/neurath-calculation-in-kind.md`. Their contribution is the one Aequitas most needs and the one it can most directly cite: a demonstration that in-kind calculation at national scale is **computationally tractable**. Their unsolved problem is also Aequitas's unsolved problem, with Aequitas holding one fewer instrument.

## Key findings

- **Labour-time calculation is defensible as a rational procedure** when supplemented by algorithms that let consumer choice guide allocation — and it is now **technically feasible**. Sparse-matrix methods over a national input-output structure run in reasonable time on ordinary hardware. This is the direct answer to the "computationally impossible" version of the Mises objection.
- **The demand-side algorithm.** Consumer goods are marked at a market-clearing price. Where the clearing price sits **above** labour value, expand production; where it sits **below**, contract it. The gap between price and value is the signal that steers production. Labour value is the accounting unit; the price/value ratio is the feedback loop.
- Labour tokens are non-circulating and extinguished on use — structurally similar to Aequitas's [[non-fungibility]] (A3).
- Their scheme remains **centrally computed**, though not centrally commanded in the Soviet sense.

## What we can use

- **Cite them for tractability.** This retires objection #3 in the Neurath note. Mises's argument was in-principle; the empirical scale objection has been answered by people who actually ran the arithmetic. Aequitas's retroactive re-weighting (§3.3) needs this defence and now has a citation for it.
- Their sparse-matrix approach is a concrete methodological precedent for C4 (re-weighting at scale).
- The non-circulating labour token is prior art for A3 and worth citing as such.

## What it gets wrong / limitations — and where Aequitas is exposed

1. **Aequitas cannot use their demand lever.** Their whole feedback mechanism is the *gap* between market-clearing price and labour value. **A5 (price ≡ cost) collapses that gap to zero by construction.** Aequitas therefore inherits their problem while giving up their solution. The standard critique — [calculation in labour values does not factor in demand, and supply without demand is blind](https://arbeitszeit.noblogs.org/en-GB/post/2023/09/10/towards-an-old-socialism/) — lands harder on Aequitas than on them. Registered as **P5**; it is the same wound as **OP-9**.
2. **Value contamination.** Brewster's objection: once market prices feed back into production decisions, the resulting labour values are no longer pure labour values. Cockshott [answers](https://paulcockshott.wordpress.com/2017/08/28/reply-to-brewster/) that the distortion is a short-term artefact of supply/demand imbalance. Aequitas will face the identical charge the moment it uses any price-allocated data — which, per `02-research/joint-production-allocation-problem.md`, it currently must.
3. **Single-substance accounting.** They reduce to labour time; Aequitas reduces to material and energy flow. Both are exposed to the joint-production result (P1) and to the supply-side-only critique (P7).
4. **Centralised computation** — a Hayek target, and the reason Aequitas's decentralised log is a genuine differentiator rather than a restatement.

## To do

- [ ] Archive the full text of *Towards a New Socialism* to `02-research/files/`
- [ ] Read the Mises Institute review closely — it is the best-organised hostile summary available
- [ ] Compare their sparse-matrix method against what C4 will actually need
- [ ] Separate note: **Dapprich** — shadow-price planning, which is the successor to this work

## Related

- [[calculation-in-kind]] · [[material-flow-value]] · [[price-equals-cost]] · [[non-fungibility]] · [[retroactive-reweighting]]
- `02-research/neurath-calculation-in-kind.md` · `02-research/kantorovich-shadow-prices.md`
- Register: `00-strategy/Aequitas_Objections_v0.1.md` — **P5**
