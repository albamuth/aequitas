# Ledger Ecosystem

> There is no single authoritative Aequitas database. There is an **ecosystem of record-keeping implementations** that must be reconciled — and any of them may be superseded at any time by a better one.

## What it is

Most material-flow data has to be reconstructed or extrapolated from scientific measurement. No one body holds it, and no one body could. So Aequitas specifies a *record format and a set of rules*, not a server.

What follows:

- **Competing implementations.** In the spirit of open-source software, anyone may build a more accurate credit/debit-tallying ledger and displace the incumbent. Nothing privileges the first one.
- **Reconciliation, not consensus.** Different ledgers will disagree. That disagreement is expected and visible, not a failure state.
- **Averaging services will emerge.** Compare credit bureaus: TransUnion, Equifax and Experian produce different scores, and a bank may average them. Aequitas will likely develop the same layer — subscribable reconciliation metrics — without any of them being *the* authority.

*(The credit-bureau analogy is structural only. Those scores rank people's reliability as borrowers; Aequitas has no borrowing and no ranking of persons.)*

## Ratios matter, absolutes don't

> **The exact numbers of credit and debit matter far less than their ratio and relative scale.**

This is what makes the ecosystem workable. Two ledgers using different weighting models will produce different absolute figures for the same event and *substantially the same relative positions*. Since Aequitas uses standing to determine what someone may hold and consume — never to price a transaction against a fixed unit — relative scale is sufficient.

It also means a disagreement between ledgers is usually a disagreement about precision, not about facts, because the underlying [event-record](event-record.md) log is shared and its physical quantities are not model-dependent.

## Why this is the right shape

It is [protocol-governance](protocol-governance.md) (A8) applied to infrastructure: capture of one implementation gets you one implementation. It is also the only honest response to the state of the data — the measurements genuinely are scattered across science, industry, and estimation, and pretending otherwise would build in a false authority.

## Depends on

- [derived-ledger](derived-ledger.md) — the log is shared; the weighting and tallying are not
- [protocol-governance](protocol-governance.md)

## Consequences

- [distributed-auditing](distributed-auditing.md)
- [retroactive-reweighting](retroactive-reweighting.md) — competing models are how weighting-model capture is resisted

## Open questions

- How do ledgers exchange and reconcile records? Needs a wire format and a reconciliation rule.
- If ratios are what matter, **what is the reference scale**? Something must anchor comparison across ledgers.
- Does an averaging layer become a de facto authority through convenience?

---
*Status: provisional*
*Source: design session 2026-07-31*
