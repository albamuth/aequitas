# Protocol Governance

> Governance is a property of the protocol, not of any institution. No organization that grows up around Aequitas may acquire authority over its core rules.

## What it is

Axiom **A8 (no governing body)**. Rules evolve as **immutable core + open variance**: everything below the core may differ from one trust network to the next, and those differences compete in public.

- **Core** — the axioms and the conformance requirements. Not amendable by any body, including one calling itself the Aequitas Foundation.
- **Open variance** — everything else: the weighting model, the self-care floor, the privacy practice, the verification rung. **A network must publish what it runs, and anyone must be able to re-compute its claims.**

> **A8 is about who may change the rules. It says nothing about size.** A trust network may cover one valley, one trade, one country, or the world. *(Renamed in Foundations v0.21→v0.22: the axiom was called "local governance", and outside reviewers kept reading "local" as "small and geographic". The word was doing two jobs, so it was removed.)*

## Why it works this way

Every previous attempt at an alternative economic order was destroyed or captured through its *organization*, not its theory. [Technocracy Inc.](energy-accounting.md) collapsed partly into the personality of Howard Scott. Cooperative currencies get captured by their issuing body. The theory is rarely what fails.

Making the core unamendable means capture of any one body cannot alter the system — capturing the Aequitas Foundation gets you a website.

Open variance is also how the system stays empirical: competing implementations produce evidence rather than doctrine.

## Who games this

**"Immutable" is a claim about intent, not physics.** Nothing technically prevents a dominant implementation from shipping a modified core and having everyone adopt it — this is exactly how software forks resolve in practice, by adoption weight rather than principle. Bitcoin's core rules are "immutable" and have changed.

The real defense is that the core is *recomputable and checkable by anyone* from the [event log](derived-ledger.md) — a divergent implementation produces visibly different numbers from the same data. That is a stronger guarantee than declaring immutability, and it should be the way A8 is argued.

Second risk: [service-credit](service-credit.md) converts to influence (OP-1). Whatever mechanism is chosen there is the most likely route by which governance authority regrows.

Third: whoever controls the [retroactive-reweighting](retroactive-reweighting.md) weighting model controls every balance in the world, without touching the core rules at all. **This is the real capture surface and it is not yet defended.**

## Depends on

- [derived-ledger](derived-ledger.md)

## Consequences

- [service-credit](service-credit.md) — OP-1
- [regulator-inversion](regulator-inversion.md)

## Open questions

- Governance of the weighting model *(the largest unaddressed hole in A8)*

---
*Status: settled (principle) / contested (enforcement)*
*Source: `00-strategy/Aequitas_Foundations_v0.39.md` A8, §8*
