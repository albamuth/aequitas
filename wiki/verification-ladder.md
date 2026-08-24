# Verification Ladder

> A four-level maturity model for establishing that a recorded event actually happened. Each rung is independently viable, so Aequitas can start today at Level 1 and get rigorous later.

## The four levels

| Level | Method | Infrastructure | Weakness |
|---|---|---|---|
| **1** | Peer / witness attestation, multi-party sign-off | None. Works in any village on Earth today. | **Collusion** |
| **2** | Reputation + stake over a social graph; the graph audits attestation patterns | Social-graph data | The hard one — see below |
| **3** | Sensors + cryptographic proof (meters, cameras, GPS, telemetry), signed and tamper-evident | Heavy | Cost; sensor capture |
| **4** | Agentic auditing — autonomous continuous tallying of the full logistical record | Far future | Speculative |

## Design rule

Every level must produce records **interoperable with every other level**, and the system must **degrade gracefully downward**. A Level 3 region and a Level 1 region must be able to trade.

This is not a nicety. Without it, high-verification regions get a systematic advantage over low-verification ones and Aequitas reproduces the development gradient it exists to remove.

## Why it works this way

It is what makes the system adoptable **without permission and without infrastructure**. A theory that requires sensors everywhere before it works is a theory that never starts.

It is also the fecundity engine on the technical side: each rung creates real demand for the next.

## Level 2 is emergent, not designed

Level 2 is **not a fraud detector to be specified in advance.** It is what [[distributed-auditing]] grows into: competing trust networks, staffed by people credited for the work of auditing, that participants choose between.

Designing a central detection apparatus would recreate the authority A8 forbids, and no detector stays ahead of attackers permanently. The defensible position instead rests on three things:

1. **Arithmetic audits need no trust model at all** — 24-hour limits, mass/energy balance, provenance closure. Cheap, universal, and they catch the easy fraud for free.
2. **Auditing is credited work**, so verification capacity scales with adoption ([[distributed-auditing]]).
3. **The payoff from undetected fraud is structurally tiny** ([[disparity-ceiling]]), so the arms race matters far less than it would in a currency system.

Prior art worth mining when the ecosystem question becomes concrete: EigenTrust, SybilGuard, proof-of-personhood (BrightID, Idena, World ID). See `02-research/`.

*Superseded framing:* earlier drafts treated Level 2 as a designed anti-collusion mechanism and the project's highest risk. That framing put fraud speculation ahead of defining the system, and assumed cheating where the real question is incentive.

## Depends on

- [[derived-ledger]]

## Consequences

- [[statistical-coverage]] — estimation is what fills the gaps verification can't reach
- [[regulator-inversion]]

## Open questions

- How competing trust networks reconcile — see [[ledger-ecosystem]]
- **OP-7 — cross-level trade fairness.** Deferred to v2.

---
*Status: settled (the ladder) / provisional (Level 2 as emergent market)*
*Source: `00-strategy/Aequitas_Foundations_v0.19.md` §4*
