# Aequitas in one page

Repository: **https://github.com/albamuth/aequitas**


## The idea

Everything anyone makes, uses, or throws away is matter and energy moving through the world. That movement can be recorded. Once it is recorded honestly, most of what we find unjust about the economy stops being possible.

Money is good at one job — letting strangers trade — and bad at another: telling the truth about what things take. A price tells you what someone was willing to accept. It does not tell you how many hours of human life went into a thing, how much fresh water it drank, or what it will cost to clean up afterwards. Those numbers exist. They are simply not written down.

Aequitas writes them down.

## The distinction everything rests on

Aequitas is a theory of **cost**, not of **value**.

- **Cost** is what a thing takes from the world — hours, joules, kilograms, damage. Physical. Measurable.
- **Value** is what someone thinks a thing is worth. A preference. Not measurable, and Aequitas does not try.

Every earlier attempt at an objective economy tried to compute what things are *worth*, and each was demolished with the same sentence: *you have described supply and ignored what people want.* Aequitas makes the narrower claim. What people want still matters — it enters the system through **pledges**, not through prices.

## The whole vocabulary

| Term | Meaning |
|---|---|
| **Credit** | A record that you did some work. An hour of your life, spent on something. |
| **Debit** | A record that something was taken from the world — material, energy, or damage — and who holds the consequence. |

That is all of it. Everything else follows from taking those two seriously and never making an exception.

## The axioms

Abbreviated. Full statements in `docs/Aequitas_Foundations_v0.16.md` §1.

1. Credit and debit **are** material and energy flow. Time is the yardstick, not the substance. Financial instruments are not material and do not appear in the books at all.
2. Labour is never rate-scaled. Hazard and exertion resolve as *material* costs, not as higher pay. Training is front-loaded credited work, never charged downstream.
3. Price ≡ cost. There is no profit in exchange. Credit cannot be transferred, lent, or inherited.
4. Property debit is dischargeable on transfer. Consumption debit is permanent and stays with whoever caused it. Custody follows possession.
5. The ledger is *derived* from an append-only event log, never stored. Debit is a vector, collapsed only on demand.
6. One credit — time worked. Three feedback channels, not three credit types.
7. Verification is a four-level maturity ladder, not an assumption of honesty.
8. One verified human, one account. Non-participants are estimated statistically, never credited.

## The headline result: the disparity ceiling

Money can be piled up without limit. Time cannot. Everyone gets the same 24 hours, nobody can buy anyone else's, and credit — a record of *your* time — never moves.

Staying alive is counted as real work, credited at a floor **F** hours per day. Consumption is gated by a ratio: `D ≤ ρ · C`, where ρ is a tolerance dial set by local government, the same for everyone in a network.

The top consumer takes ρ·24. The bottom takes ρ·F. The ratio is:

> **(ρ × 24) / (ρ × F) = 24 / F**

**ρ cancels.** At F = 10 hours, the ceiling is **2.4×**. Under money, richest-to-median runs to about **1,000,000×** and compounds.

The bound holds **even for a cheater**, because a cheater still only has 24 hours in a day.

**This is stated as a conditional result, not a theorem.** It requires that a verification problem (OP-22) is solved and that self-care floors stay in band. Overstating it as certain was an error, and it was corrected. See `sims/DISPARITY_CEILING.md` §4.

## What the simulations found

- Adding up everything a median US adult consumes in a year — including the share made abroad — comes to about **1,380 hours of other people's labour**. Each person is credited roughly **3,650 hours a year just for staying alive**. A median lifestyle therefore costs about a third of what one person contributes. **There is no labour crunch.**
- The United States is the efficiency outlier: **50–80% more labour and two-to-four times the carbon** per person than Germany, Sweden, France, Japan, or Spain, for a comparable material life and longer lifespans. Under Aequitas the efficient method is automatically the cheaper one, because the hauling, the overhead, and the pollution all appear as real costs.
- Abundance comes from producing **smarter**, not from working **more**.

## Verify it yourself

```bash
cd sims
python arithmetic_audits.py
```

Twelve ledger integrity constraints, each run clean and then run again against a deliberately injected violation. Expected: **12/12 pass, 12/12 violations caught.**

The load-bearing property: **IC-1 through IC-9 need no trust model, no reputation, and no authority — only the ability to recompute.** An unrecorded emission is not an enforcement problem. It is an arithmetic error the log reports on itself.

Every simulation in `sims/` runs standalone with its own self-tests. No external data files.

## The open problems

They are in `docs/Aequitas_Objections_v0.16.md`, listed rather than hidden. The live ones:

- **OP-22** — proving an hours claim is backed by real work without exposing a private life history.
- **OP-10** — who governs the weighting model, and how that avoids becoming a capture surface.
- **OP-24** — systematic understatement drift.
- **C2** — the trust-network design itself is still a straw-man. This is the current work item.
- The **tedium** half of unwanted work. The hazard half is addressed; the boring-and-undignified half is not.

## The best thing you can do

Break one of the claims. Start with the disparity ceiling, or with "cost is not value" — that is the load-bearing move, and if it fails, everything above it fails with it.
