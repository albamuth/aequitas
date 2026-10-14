---
title: Derived ledger
summary: An account's standing is never stored; it is computed on demand from the append-only event log under the current weighting model, and the log alone is authoritative.
type: axiom
ids: [A6]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: implies, to: retroactive-reweighting}
  - {rel: implies, to: non-fungibility}
  - {rel: implies, to: verification-ladder}
  - {rel: implies, to: statistical-coverage}
  - {rel: implies, to: event-record}
  - {rel: implies, to: permanence-and-death}
  - {rel: implies, to: dispute-resolution}
  - {rel: source, to: "Foundations §1"}
  - {rel: source, to: "Foundations §3.0"}
  - {rel: source, to: "Foundations §3.1"}
  - {rel: source, to: "Foundations §3.3"}
---
# Derived Ledger

> **Version:** 0.2
> **Date:** 2026-10-13

> Balances are not authoritative — the append-only event log is. Any account's standing is a pure function of *(its events × the current scientific cost-weighting model)*.

## What it is

Axiom A6. There is exactly one permanent record: **what happened**. Who did what, when, involving which materials and energy, attested by whom.

An account "balance" is a **continuously recomputed projection** of that log. It is a view, not a fact. Change the weighting model and every balance in history changes with it, without a single event being edited.

The same record serves two purposes at once:
1. A person's account history.
2. The global logistical record of human activity.

## Why it works this way

Three things follow only from separating events from balances:

- **[retroactive-reweighting](retroactive-reweighting.md) is possible at all.** If balances were stored, improving the science would require rewriting history. Because they're derived, improving the science is just recomputation.
- **Verification is decentralized.** Anyone can recompute from the log. There is nothing to trust, only something to check.
- **No issuer.** A stored balance implies someone who may set it. A derived balance has no such role.

The event log is why Aequitas is **an accounting system, not a currency, token, or blockchain** — the append-only structure is a data-model requirement, not a consensus mechanism.

## Depends on

- [material-flow-value](material-flow-value.md)

## Consequences

- [retroactive-reweighting](retroactive-reweighting.md)
- [non-fungibility](non-fungibility.md)
- [verification-ladder](verification-ladder.md) — what puts events into the log in the first place
- [statistical-coverage](statistical-coverage.md) — estimated events are just events with a wider error bar

## The record itself

- [event-record](event-record.md) — the four primitives, the single record shape, and the conservation checks. **C1 v0.1 drafted.**

## Open questions

- Amortization of training cost into skilled service ([time-as-yardstick](time-as-yardstick.md)) — blocks full A2 implementation
- Privacy: holders keep a private ledger with provable claims; disclosure is by zero-knowledge proof, not by history dump (C7)

---
*Status: settled (the principle) / open (the schema)*
*Source: `00-strategy/Aequitas_Foundations.md` A6, §3.1*
