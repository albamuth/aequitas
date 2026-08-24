# Distributed Auditing

> Auditing records is itself **credited work**. There is no audit authority — there are competing trust networks, and the people who do the reconciling are paid for it in the same way anyone else is.

## What it is

Aequitas does not appoint verifiers. Because the log is public and recomputable ([[derived-ledger]]), anyone may audit anything, and the work of auditing is ordinary [[service-credit]] like any other.

Consequences of treating it as work rather than as enforcement:

- **Multiple trust networks coexist.** People choose whose audits they credit, the way they choose any other service provider.
- **Auditing scales with adoption.** More participants means more records *and* more people whose work is auditing them. The effort tracks the load automatically.
- **No permission is required to start auditing**, and no body can revoke the ability.

## Arithmetic audits need no trust at all

A large class of checks require no social graph, no reputation, and no judgement — only arithmetic on the log:

- **Nobody can be credited with more than 24 hours of work in a 24-hour period.** Sum an account's agent-intervals across all events in any window; if it exceeds wall-clock, something is wrong. Pure computation, checkable by anyone, no authority involved.
- Mass and energy must balance per event ([[event-record]] IC-1/IC-2).
- Material must resolve to a holder, a transformation, or a named sink (IC-4).
- A parcel cannot be consumed before it exists.

**These are the cheapest and most valuable audits, and none of them need a trust model.** Build them first; they cover the easy fraud for free.

## Why this is the right shape

Designing a central fraud-detection apparatus would recreate the authority A8 forbids ([[protocol-governance]]) — and no security design is permanently unbreakable anyway. An ecosystem of competing auditors has no single point to capture and no single point to fool.

It is also fecund: auditing generates credit, so the system funds its own verification as it grows.

## 🔴 "Networks compete on accuracy" does not survive contact with the record

The tempting claim is that trust networks compete on accuracy because accuracy benefits their subscribers. **It doesn't. Subscribers want a favourable assignment, not an accurate one** — accuracy benefits the *counterparty*.

Every issuer-pays arrangement in history has drifted the same way: [Arthur Andersen](https://en.wikipedia.org/wiki/Arthur_Andersen) was paid by Enron; [credit rating agencies](https://en.wikipedia.org/wiki/Credit_rating_agencies_and_the_subprime_crisis) were paid by the issuers whose products they rated. **Removing the profit motive does not fix it, because the conflict is directional rather than monetary** — a client-owned Andersen would have been worse, not better.

**Two structural answers, neither requiring an authority:**

1. **A network concentrated in the sector it audits is captured by construction.** In Aequitas everyone is both producer and consumer, so a **general-membership** network is dominated by the consuming side for any particular good and its incentives align automatically. Only *sector-specific* networks fail this way — and **membership composition is public in the log, so this is detectable rather than something anyone must police.**
2. **[[rival-sector-audit]]** for the errors rule 1 creates. A consumer-dominated network is biased toward *understating* what its members consume, and nobody funds the correction of an error in their own favour. The rival sector does.

**Read the two together. Neither is safe alone**, and the full shape of trust networks — funding, membership, competition, dispute handling — is deferred to C2.

## Depends on

- [[derived-ledger]] · [[ledger-ecosystem]]

## Consequences

- [[verification-ladder]] — Level 2 is an emergent market of trust networks, not a designed detector
- [[rival-sector-audit]] — the fix for the bias this page's model introduces
- [[co-product-allocation]] — the process-energetics constants trust networks commission

## Open questions

- Who audits the auditors, and does that regress or converge?
- **OP-24 — understatement drift.** Errors favouring subscribers have no funder.
- Onboarding assistance and data-gathering are credited work — **does the network that onboards you also get to audit you?** Unexamined, and it looks like the same conflict again.

## Prior art

- `../docs/GLOSSARY.md#src-auditor-independence` — the issuer-pays record, and why competition alone does not produce accuracy

---
*Status: provisional*
*Source: design session 2026-07-31*
