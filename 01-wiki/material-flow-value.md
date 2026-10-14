---
title: Material flow value
summary: Every debit records a real material or energy flow and every credit records time a person spent; no abstract or issued quantity exists anywhere in the system.
type: axiom
ids: [A1]
status: settled
edges:
  - {rel: depends_on, to: ellerman-responsibility}
  - {rel: implies, to: time-as-yardstick}
  - {rel: implies, to: non-fungibility}
  - {rel: implies, to: no-externalities}
  - {rel: implies, to: cost-not-price}
  - {rel: implies, to: derived-ledger}
  - {rel: source, to: "Foundations §1"}
  - {rel: source, to: "Foundations §2.2"}
  - {rel: source, to: "Foundations §2.3"}
  - {rel: source, to: "Foundations §3.1"}
---
# Material Flow Value

> **Version:** 0.2
> **Date:** 2026-10-13

> Every credit and every debit in Aequitas is a record of matter or energy moving through the world, attributable to the people who caused the movement. Nothing else is value.

## What it is

The root axiom (A1). There is no abstract, issued, or fiat value anywhere in the system — no unit that exists because someone declared it into existence.

Accounting extends all the way down: the oxygen a human inhales and the CO₂ they exhale are in principle in scope. In practice the system records what is known and estimates the rest ([statistical-coverage](statistical-coverage.md)), refining forever.

Two directions of flow:
- **Credit** — you caused matter/energy to become more useful to others.
- **Debit** — you caused matter/energy to be consumed, degraded, or held out of use.

## Why it works this way

Because it is the only value definition that is **measurable identically anywhere in the universe**. Mass, energy, and seconds don't need a jurisdiction, an issuer, or a shared belief. That is what makes the universality criterion satisfiable at all.

Every other candidate — utility, labor-time, price, subjective preference — requires either a central assessor or a market to reveal it, and both are capturable.

Without A1 the system has an issuer, and with an issuer it has an oligarchy.

## Depends on

- Nothing. This is the root.

## Consequences

- [time-as-yardstick](time-as-yardstick.md) — time measures the flow, it isn't the flow
- [non-fungibility](non-fungibility.md) — a record of a specific event can't be a token
- [no-externalities](no-externalities.md) — if value *is* material flow, there is no "outside"
- [cost-not-price](cost-not-price.md)
- [derived-ledger](derived-ledger.md)

## Prior art

- [calculation-in-kind](calculation-in-kind.md) — Neurath proposed exactly this in 1919 and lost the argument to Mises on tractability, not principle
- [energy-accounting](energy-accounting.md) — Technocracy Inc. tried a one-dimensional (joules-only) version. Read the failure.

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §0, A1*
