# Aequitas Overview — Change History

> Version-by-version change log for `Aequitas_Overview_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the main document so it is read only when tracing **when and why** something changed. The main doc's header carries a one-line summary of the current version. Superseded full versions live in `99-archive/`.

---
<!-- tag: ovw-v0-15-2026-08-23 -->
### v0.15 (2026-08-23) - section 9 answers "can I use this while everyone else still uses money?"

Reader-facing form of Foundations v0.19 5.5 (OP-27). One addition; nothing else changed.

1. **New subsection in section 9.** **Yes, and both ways of crossing the line cost you something on purpose.** Bringing in a thing made with money: it has no history, so it is priced from a **published standard figure** for that kind of thing, **deliberately set a bit dear** so keeping real records is always worth more - and you spent money on it and got none back. Selling out for money: allowed, but **you keep the thing's debt**, and the books count it as a **gift**.
2. **Why the money is invisible, in plain words.** The books record matter and energy; **money is neither**. A banknote changing hands is not a physical event the ledger has any way to notice - *"invisible, in the way a colour is invisible to a set of scales."* Not a rule anyone wrote, but a consequence of what the system counts.
3. **Two things stated plainly because readers assume they must be false.** **Money cannot buy standing** - pay a hundred people to make things and *they* earn the hours, because credit is a record of who actually did the work; **you cannot buy someone else's hours at any price**. And **buying cheap inside to sell dear outside wrecks the person doing it** - everything taken on from inside adds to what you owe, selling it outside never removes it, so their account worsens with every load pulled out until it stops them buying more. **Nobody has to catch them; the books just stop lending them rope.**

**Why it was needed.** *Can I use this while everybody around me still uses money?* is roughly the third question a normal reader asks, and the document had no answer anywhere.

<!-- tag: ovw-v0-14-2026-08-23 -->
### v0.14 (2026-08-23) - section 0 says what Aequitas is not

Reader-facing form of the Foundations v0.18 scope fold. Conforms to Foundations v0.18 1.2/9. One addition; nothing else changed.

1. **New passage in section 0, directly under "not a currency, not a token, not a blockchain":** *and it is not a piece of software.* States that these documents do not specify one and never will - database, record shape, cryptography and privacy practice all belong to whoever builds it, **the same way banks, not capitalism, decide what a banking system runs on.** What the project owes a builder is named instead: **a list of what must be true** for the books to be Aequitas at all. *What must be true is here. How to build it is theirs.*

**Why it was needed.** Two consecutive sessions of work drifted into record-keeping detail and away from the economics, traced to Foundations 9 and 11 contradicting the 1.2 scope ruling. Appendix A already said the right thing - *a standard, not a product* - but that sits at the end of the document and section 0 said nothing.

<!-- tag: ovw-v0-13-2026-08-22 -->
### v0.13 (2026-08-22) - section 7 gains the honest limit of the checks

Reader-facing fold of OP-26. Conforms to Foundations v0.17 3.3/5.1b.

1. **New section-7 passage: "What the checks can see - and what they cannot."** States plainly that the arithmetic catches a factory that under-declares and cannot see a workshop that never joined, and that the second half is answered by ordinary outside measurement - a satellite pass, a harvest total, a census - reconciled against the books. The gap is framed as **a measurement, not an accusation**.
2. **Two consequences added in plain language:** the estimate applied to whoever stays outside **gets worse as everyone else joins**, so staying dark stops paying; and **no number here is ever final** - a tally is a citation, better measurement recalculates every affected record backwards, and a wrong figure is annotated rather than deleted. Framed as how science handles a mistake, and as the only method that needs no authority at the door.
0. **New in §0: "And who actually does this?"** Added at the author's instruction — **the importance of the trust network as the implementer of Aequitas cannot be understated**, and the Overview did not mention them until far too late. States plainly that **Aequitas is a system in the sense capitalism is a system**: nobody joins capitalism, and banks and firms are what carry it out. **Trust networks are the equivalent here.** They keep the books, record flows, hand-offs, services, pledges and measurements of the world itself, check the arithmetic, and publish their methods so anyone can check them back. **Framed as laboratories rather than banks** — a network that lets fraud through is helped by a rival, not from goodwill but because a bad method in one corrupts the books of the other. Notes that they are **not prescribed by this project** (privacy, technology, law, founding record are theirs), and that **they compete on one thing: how close to the truth they can get.** Points to `C2_TrustNetworks_v0.1.md`.
3. **New guarantee stated for the first time:** the check on what you may consume is made **at the moment you do it** - a later revision changes what you may do next, never whether what you already did was allowed. *A ledger that recalculates must never mean a debt that ambushes you.*

---

### v0.12 (2026-08-17) — labour-abundance gets numbers; efficiency (not more work) creates abundance

Conforms the Overview to **Foundations v0.16 §3.5/§7.5**. Reader-facing additions to §1's labour-abundance passage (no mechanism change):

1. **A measured number.** A median US lifestyle commands ≈ **1,380 hours** of others' work per year — about a third of the ~3,650 h everyone earns just by staying alive. States the "no labour crunch" claim quantitatively for the first time.
2. **The new finding, in plain language.** The US is a global efficiency outlier — **50–80% more labour and 2–4× the carbon** per person than Germany/Sweden/France/Japan/Spain for a comparable, longer-lived standard. Sprawl, fossil fuels, and long supply chains are the difference; Aequitas makes the efficient way automatically cheaper (the waste shows up as real cost), so a decent life for everyone fits inside the work the world already does. **Abundance comes from producing smarter, not working more.**
3. **Header pointer** re-threaded to Foundations v0.16; stale footers fixed (`End of v0.10` → `End of v0.12`; rigorous-version pointer → v0.16).

---

### v0.11 (2026-08-14) — pledges made permanent; the insurance-pool incentive for dangerous work

Conforms the Overview to **Foundations v0.14**. Two reader-facing changes:

1. **Pledges are permanent.** Everywhere the old text said you could "take it back" or "withdraw" a pledge (§4 pledge box, §6 speculative-vs-pledged aside, the 1:1 explanation), it now says a pledge is a permanent, one-time spend from a lifetime allowance equal to your earned credit — the backing can't vanish under the people you support, and nobody can pledge frivolously for free.
2. **New plain-language item: dangerous work gets done without danger-pay.** Added an explanation of the contingent reserve — when a nasty job is over-pledged, the surplus becomes an insurance fund that pays out only if the work harms whoever did it, rewarding hazardous work without a bonus and without making anyone richer. Notes the honest limit (helps with *dangerous* unwanted work, not plain *boring* work).
3. Cross-references re-threaded to Foundations v0.14.

### v0.10 (2026-08-11) — pledge-mechanics correction + presentation cleanup

Conforms the Overview to **Foundations v0.13**. No new reader-facing ideas; one mechanism is corrected and the document is tidied.

1. **A pledge is a revocable grant of backing, not a spend or a promise to buy.** Fixed the test in §6 ("*is it backed one-for-one by credit you earned?*", replacing the stale "does it commit you to absorbing the debit?"), the Pledge/Signal table, the "spending your credit" language, the one-to-one paragraph (reframed from "goods arrive and nobody can take them" to "backing with room that isn't there"), and the end-of-§6 aside ("a buyer is already lined up" → "committed interest, but withdrawable"). Added the plain statement that a pledge leaves your credit with you, gives the receiver room to carry a cost, is withdrawable at any time, and that taking the finished good is a separate step paid with your own room.
2. **§2 / §4 front-loading language** ("settled/paid up front by pledgers") reworded to "carried up front, cushioned by pledges" — the cost rides the asset and its holders; pledges cushion the bite and re-expose it if withdrawn.
3. **Presentation:** inline version-notes stripped; a Contents list added after the header; the header's multi-version "Prior:" recap removed; change history moved here. Foundations pointer re-threaded to v0.13.

### v0.9 (2026-08-10) — scenario-suite fold (§1)

Two reader-facing additions from the societal-scale simulations: **(1) money wealth isn't material wealth** — Aequitas never counts stocks, bonds, or crypto, and once you look only at what people physically hold and consume, the richest-to-poorest gap is already ~1,000× smaller than the money picture; **(2) there's no shortage of hands** — because looking after yourself counts as work, human labour is far more abundant than any economy needs, so what limits a society is materials and energy, not hours.

### v0.8 (2026-08-10) — electricity attribution (§4)

The pollution from your electricity is *yours*, the person who draws it (power can't be stored, so flipping the switch is what commands the generator to burn fuel), attributed by the supply mix you signed up for. Aligns electricity with the "whoever burns it, owns it" rule already used for driving and home heating.

### v0.7 (2026-08-09) — legibility fold (§1)

Embedded the debit-taxonomy schematic and reframed the inequality-cap claim as **conditional** (it holds only if the fake-hours/verification problem is solved and community baselines stay sane) rather than a flat certainty.

---

*Earlier history (v0.1–v0.6) is recorded in `NEXT.md` (RECENTLY DONE) and the `03-journal/` entries.*
