---
title: Components C1 to C12
summary: The twelve build items of the specification, from the event-log schema to the energetics registry, each with its current status and the wiki page that carries it.
type: hub
ids: []
covers: [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12]
status: provisional
edges:
  - {rel: depends_on, to: protocol-governance}
  - {rel: source, to: 00-strategy/GLOSSARY.md}
  - {rel: source, to: "Strategy §3"}
  - {rel: source, to: 00-strategy/Aequitas_Simulation_Roadmap.md}
---
# Components C1 to C12

> **Version:** 0.1
> **Date:** 2026-10-14

> **The twelve build items of the specification**, listed in `00-strategy/Aequitas_Strategy.md` §3 and indexed in `00-strategy/GLOSSARY.md`. A component is a piece of the system that has to be stated and tested before `Aequitas_System_v1.0` can exist. **This page is the index; the glossary row and the page named in each line are the source.**

## The twelve

| Label | Component | Status | Where it lives |
|---|---|---|---|
| **C1** | Event-log schema | ✅ Retired 2026-08-28 as a document; its arithmetic became conformance rows | [event-record](event-record.md) |
| **C2** | Verification and trust networks | Partial. The shape is stated; the Level-2 market is expected to grow rather than be designed | [trust-network](trust-network.md), [verification-ladder](verification-ladder.md) |
| **C3** | Estimation engine | In progress, on real data (OP-3) | [estimation-engine](estimation-engine.md) |
| **C4** | Re-weighting | Mechanism stated; the recompute cost is measured; governance of the model is OP-10 | [retroactive-reweighting](retroactive-reweighting.md) |
| **C5** | Debit taxonomy | Partial. Property against consumption, transfer rules, latent pollution all stated | [debit-taxonomy](debit-taxonomy.md) |
| **C6** | Identity | Not started as a design. The rule is stated; Sybil resistance is each network's own | [one-account-per-person](one-account-per-person.md) |
| **C7** | Privacy layer | Not started. Who decides is settled (the network); the minimum disclosure set is OP-22 | [privacy-is-a-network-choice](privacy-is-a-network-choice.md) |
| **C8** | Influence mechanics | Partial. Pledges and signals stated; OP-1 and OP-6 open | [pledge-and-signal](pledge-and-signal.md) |
| **C9** | Debit-tolerance formula | Not derived. The band of `F` and ρ was measured (OP-4) | [debit-tolerance](debit-tolerance.md) |
| **C10** | Cross-level trade | Not started; deferred to v2 (OP-7). The design rule, that a rung-1 region and a rung-3 region must be able to trade, is in the ladder | [verification-ladder](verification-ladder.md) |
| **C11** | Arithmetic audits | ✅ Closed. IC-1 to IC-12 as runnable checks | [integrity-constraints](integrity-constraints.md), [distributed-auditing](distributed-auditing.md) |
| **C12** | Energetics registry | New. Per-process constants and the rules for auditing them; home of OP-24 | [retroactive-reweighting](retroactive-reweighting.md), [op-24](op-24.md) |

**The critical path, as `NEXT.yaml` states it:** C3 in progress, then C4. **The unsolved work is governance rather than measurement**: OP-10, OP-24, OP-16.

## How to read a status

| Word | What it means |
|---|---|
| **Closed** | Stated, tested, and folded into the core documents. Nothing is owed. |
| **Partial** | The rule is stated in Foundations; part of the design is deliberately left to trust networks or is still open. |
| **In progress** | Being built on real data in `06-simulation/`. |
| **Not started** | Named, with its open problem, and nothing built yet. |

## Depends on

- [protocol-governance](protocol-governance.md) — what may vary between networks decides what a component may specify

---
*Status: provisional (statuses change as components close)*
*Source: `00-strategy/GLOSSARY.md` components table; `00-strategy/Aequitas_Strategy.md` §3; `00-strategy/Aequitas_Simulation_Roadmap.md`*
