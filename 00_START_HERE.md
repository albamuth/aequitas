# Aequitas in one page

Repository: **https://github.com/albamuth/aequitas**

## The idea

Everything anyone makes, uses, or throws away is matter and energy moving through the world. That movement can be recorded. Once it is recorded honestly, most of what we find unjust about the economy stops being possible.

Money is good at one job, letting strangers trade, and bad at another: telling the truth about what things take. A price tells you what someone was willing to accept. It does not tell you how many hours of human life went into a thing, how much fresh water it drank, or what it will cost to clean up afterwards. Those numbers exist. They are simply not written down.

Aequitas writes them down.

## The distinction everything rests on

Aequitas is a theory of **cost**, not of **value**.

- **Cost** is what a thing takes from the world: hours, joules, kilograms, damage. Physical. Measurable.
- **Value** is what someone thinks a thing is worth. A preference. Not measurable, and Aequitas does not try.

Every earlier attempt at an objective economy tried to compute what things are *worth*, and each was demolished with the same sentence: *you have described supply and ignored what people want.* Aequitas makes the narrower claim. What people want still matters. It enters the system through **pledges**, not through prices.

## The whole vocabulary

| Term | Meaning |
|---|---|
| **Credit** | A record that a person spent an hour of their life on work. It belongs to that person and never moves. |
| **Debit** | A record that matter or energy was taken from the world, and who is holding the consequence. Nobody collects it and nothing is ever settled. |

That is all of it. Everything else follows from taking those two seriously and never making an exception.

## The eight axioms

Abbreviated. Full statements in `00-strategy/Aequitas_Foundations.md` §1; what follows from each is in §2 onward.

1. **Materialism of cost.** Every debit records a real material or energy flow; every credit records time a person spent. No issued or fiat quantity exists anywhere. A flow is attributed to whoever caused it, and only people act: never a tool, a machine, or whoever owns one.
2. **Time as measure.** Time is a yardstick, not a substance with value. One hour credits as one hour, whoever worked it. Exertion, hazard and skill land as material costs, never as a multiplier.
3. **Non-fungibility.** Every credit and debit is a unique record of one event. Credit can never be transferred, traded, lent or stolen. Only debit moves, and only with the thing it is attached to.
4. **No externalities.** Every consequence stays inside the accounting and is assigned to whoever caused it, including one found decades later. Where causation is unresolved, the consequence is held explicitly unassigned until an attribution witness exists.
5. **Cost, not price.** Possession decides who carries the debit that rides a thing. A thing's cost is the current best estimate of what was consumed to make it; nothing is added, and nothing enters that the thing did not consume. There is no profit in exchange.
6. **Derived, not stored.** A standing is computed from the append-only event log whenever anyone asks, under the current weighting model. The log is authoritative; a balance is not.
7. **Universal accounting.** Every human is in the books whether or not they take part. An estimated position becomes usable only with a verified account and observed records.
8. **No governing body.** Nobody may acquire authority over the core rules. Everything below them may vary between trust networks, must be published, and must be re-computable by anyone. A trust network has no set size.

**Who does this?** Trust networks: the organisations that keep the books, check the arithmetic, estimate what they cannot see, and publish their methods. Laboratories, not banks. `01-wiki/trust-network.md`.

## The headline result, and its scope

Money can be piled up without limit. Time cannot. Everyone gets the same 24 hours, nobody can buy anyone else's, and credit, a record of *your* time, never moves.

Staying alive is counted as work, credited at a floor **F** hours a day that each network sets and publishes. A person's lifetime pledge budget, the hours they may put behind the things they want made, is the credit they earned and nothing else. So per day lived it sits between `F` and 24, and the largest and smallest differ by at most:

> **24 ÷ F**

At `F` = 10 that is 2.4×. **Nobody reaches it**: it needs 24 credited hours every day from birth to death. A very hard working life, 12 hours a day, 300 days a year, from 20 to 70, reaches about **1.6×**. Under money the same lever runs to about 1,000,000× and compounds.

**What it bounds, and what it does not.** It bounds the **say over what gets made**, inside **one network's books**. It does **not** bound consumption: consumption is gated by `D ≤ ρ·(C + P)`, where `P` is the backing other people have pledged to you by name, and nothing caps how many people pledge to you. Someone widely backed can consume far past the wall. What that backing cannot do is earn: it cannot be lent at interest, rented out, or used to hire anybody.

**And it is blind.** The bound never reads an account, so it returns the same figure for an honest population and an invented one. It limits what cheating is worth. It does not find cheating; a physical total measured from outside does that. An adversarial search of 20,000 filings never pushed it past `24 ÷ F`; the four implementation settings that can are listed, with their cost, in `06-simulation/ceiling-challenge/RESULTS.md`.

## What the simulations found

- A median US lifestyle commands about **1,380 hours** of other people's labour a year. **At the American production method the hours do not close**: deployable hours reach 0.43 to 0.87 of what that needs. The German, Japanese or Spanish method delivers the same material life for far fewer hours, and under Aequitas the efficient method is the cheaper one, because the hauling, the overhead and the pollution all appear as real costs. **The constraint is the method, not human hours as such.**
- Strip the financial layer and the top of the wealth distribution collapses by about **1,000×**, from about 10⁶× the median to about 670×, because consuming physically takes time.
- A workable floor exists at every `F` from 1 to 14 hours a day. What binds it is physical capacity, not affordability.
- A joint process's cost cannot be divided honestly: 36 methods that all satisfied the published obligations came out **6.31×** apart. So nothing is divided; every co-product carries the whole process cost against its own mass.

## Verify it yourself

```bash
cd 06-simulation/audits
python arithmetic_audits.py
```

Twelve ledger integrity constraints, each run clean and then run again against a deliberately injected violation. Expected: **12/12 pass, 12/12 violations caught**, with an extent block saying what the check could not see.

**You do not have to run our code.** `06-simulation/audits/audits_inert/` publishes the fixture, each constraint written as arithmetic, and the expected verdict for every injected case as plain data. Running our program only tells you our program is self-consistent.

**The honest limit.** Arithmetic over a log testifies to nothing outside that log. A process recorded nowhere is a coverage question, answered by a total measured from outside: `R = N − Y`, published whole, charged to nobody. [@cairn-lineage](https://1f916.ai/post/1581) showed this on 2026-08-22, and it is in `00-strategy/Aequitas_Foundations.md` §4.4.

Every simulation in `06-simulation/` runs standalone with its own self-tests, except the empirical labour work, which needs third-party datasets we cannot redistribute; those scripts say so.

## The open problems

In `00-strategy/Aequitas_Objections.md`, listed rather than hidden, and one page each in `01-wiki/`. The live ones:

- **OP-10** — who governs the weighting model, what a kilogram or a tonne of CO₂ costs in hours. **The top blocker.**
- **OP-24** — understatement drift: a cost error that flatters subscribers has nobody who wants it fixed. The proposed fix was withdrawn; a network is held to five published requirements and none has shown a working answer.
- **OP-16** — dull work. A pledge can name whoever does it; whether enough people pledge is unmeasured.
- **OP-22** — the least an auditor must be shown to check a claim without seeing a person's history.
- **OP-4** — where the floor and the tolerance should sit, and whether a network credits a child's learning time.
- **OP-28** — the extent register that estimates for unmeasured producers are distributed by, which a producer declaring half their real land defeats.
- **P4** — the coordinator class. The extractive employer is foreclosed; coordination power is not.
- **OP-1** — fake hours. No account may record more than 24 hours a day, but people trading fake hand-offs could still inflate their totals. The `24 ÷ F` bound assumes this is controlled.
- **OP-6** — feedback mechanics. Whoever is already liked attracts the most pledges, and backing can be consumed, so popularity is a route to consumption. Each pledge costs a real person a real hour from a budget nobody can manufacture.

## The best thing you can do

Break one of the claims. Start with the disparity ceiling, with the refusal to divide a joint cost, or with *cost is not value*, which is the move everything rests on.
