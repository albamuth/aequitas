# Struck phrases — wordings that must not appear in a live document

> **Read by [`bin/consistency.py`](../bin/consistency.py). The table below is the machine-readable part; everything else on this page is for people.**

## Why this file exists

**When a rule is withdrawn, the sentence stating it is rewritten in the place somebody noticed. It survives everywhere else.**

That is not a hypothetical. **It happened three times in a single day, 2026-08-28:**

| What happened | How long it lasted |
|---|---|
| The Overview kept publishing *"you carry the emissions of the supply you signed up for"* after Foundations struck the contracted-supply rule | **Six versions** |
| The Objections register kept a withdrawn fix in an exploit list, **under a box saying it had been withdrawn** | Four days |
| Foundations §3.5 struck a comparison as circular and then made it again, forty lines further down | One version |

> **A correction is not finished when the rule is rewritten. It is finished when every paragraph that leaned on the old rule has been read.** This file is the machine's half of that.

## How to add a row

**When a fold withdraws a rule, add the withdrawn wording here in the same fold.** Pick a phrase that is:

- **distinctive** — it should not appear by accident in an unrelated sentence,
- **short** — six to twelve words, so a paraphrase still trips it,
- **the claim, not the topic** — `the supply you signed up for` is good; `electricity` is useless.

**Match is case-insensitive and ignores runs of whitespace.** Test a new row by running `python bin/consistency.py` before you commit it.

## Where it is checked, and where it is not

**Checked:** `00-strategy/` (not the changelogs), `01-wiki/`, `04-use-cases/`, `05-marketing/`, `07-outreach/AGENT_BRIEF.md`, `07-outreach/memory/records/`.

**Not checked, deliberately:** `99-archive/`, every `*_CHANGELOG.md`, `03-journal/`, `07-outreach/log/`, and this file. **Those are dated records. A struck phrase is supposed to appear in them** — that is what a record is for.

---

## The registry

| Struck phrase | Struck on | Why | What is true instead |
|---|---|---|---|
| `the supply you signed up for` | 2026-08-24 | A commercial supply agreement is a paper claim, and A1 forbids a paper claim deciding a physical record | A consumer carries **the grid's actual measured fuel mix over the periods they drew power** — Foundations §3.2b |
| `attribute by the consumer's contracted supply mix` | 2026-08-24 | Same ruling, second wording | As above — Foundations §3.2b, Objections B12 |
| `the labour dimension has enormous slack` | 2026-08-28 | Credited hours include the floor, and the floor is a value the network sets by rule, so the comparison cannot fail | Compare **deployable** hours, not credited ones — Foundations §3.5 |
| `across every network that can trade with every other` | 2026-08-25 | Networks do not trade with each other and no book is ever added to another, so there was no object for the claim to describe | The `24 ÷ F` bound describes **one network's own books** — Foundations §5.5.5 condition 4 |
| `compatible enough to interoperate` | 2026-08-25 | **Same ruling. This is the wording the documents actually carried**, and the row above was written from the ruling rather than from the text, so it matched nothing for six days | As above — Foundations §5.5.5 condition 4 |
| `arrive at the same ledger` | 2026-08-25 | Same ruling, second half. Compatible networks are **expected** to reach different figures | **Comparison, never conversion** — each party re-reads the shared record through its own model. 12 h and 18 h are both correct — Foundations §4.2, §4.1 |
| `land on the same ledger` | 2026-08-25 | Same claim, third wording | As above — Foundations §4.2 |
| `cross-network guarantee` | 2026-08-25 | There is no cross-network bound and none is available; no book is ever added to another | What survives across networks is a **coverage** question, not a disparity one — Foundations §4.0, §4.4 |
| `every credit and debit is a record of a real material or energy flow` | 2026-08-28 | A credit was never a material flow | **Every debit** records a material or energy flow; **every credit** records time a person spent — Foundations A1 |
| `competition happens on quality, artfulness, and efficiency` | 2026-08-28 | Reworded, not withdrawn. Listed because two documents quoted it verbatim | *"Producers compete on quality, artfulness, and efficiency"* — Foundations §5.1 |
| `the process allocates itself` | 2026-08-22 | Overstated: measurement constrains the choice of split without determining it | A joint split is **a choice that measurement constrains**, with four published obligations — Foundations §3.4a |
| `unmeasured means outside the network, not low-technology inside it` | 2026-08-29 | One word was doing two jobs, so the rule could not describe a subscriber with output they never recorded | **Unsubscribed** is a person outside the network; **unrecorded** is output not in the books. **They are independent** — Foundations §4.4 |
| `nobody complains about being charged too little` | 2026-08-29 | Said of unmeasured producers, who are charged nothing at all. The leftover is debit on no account | An unflattering estimate **sits there until the producer joins and replaces it with a record** — Foundations §4.4, §4.1 |
| `the natural auditor of a cost constant is the rival sector` | 2026-08-24 | A rival's cheapest move is to get its own constant set generously, not to fund your correction | Rival-sector audit is **one pressure, not a mechanism**. Constant-auditing is an open network-design problem — Foundations §3.3a, **OP-24** |
