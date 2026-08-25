<!-- tag: ovw-aequitas-overview -->
# Aequitas — Overview

> **Version:** 0.16
> **Date:** 2026-08-24
> **Audience:** everyone. No economics background assumed, none required.
> **Rigorous version:** `00-strategy/Aequitas_Foundations_v0.22.md`. This document is the plain-language companion; where they differ, the Foundations govern.
> **Version history & what each version superseded:** `00-strategy/Aequitas_Overview_CHANGELOG.md`.

*Aequitas* (genitive *aequitatis*) is the Latin word for fairness, evenness, symmetry — the quality of things being level with one another.

---

<!-- tag: ovw-toc -->
## Contents

- [0 — What this is, in one page](#0--what-this-is-in-one-page)
  - [And who actually does this?](#and-who-actually-does-this)
- [1 — Problem: Inequality](#1--problem-inequality)
- [2 — Problem: Debt](#2--problem-debt)
- [3 — Problem: Gambling and Rent](#3--problem-gambling-and-rent)
- [4 — Problem: Externalities](#4--problem-externalities)
- [5 — Problem: Intellectual Property](#5--problem-intellectual-property)
- [6 — Who decides what gets made?](#6--who-decides-what-gets-made)
- [7 — Who checks any of this?](#7--who-checks-any-of-this)
- [8 — Wouldn't this need total surveillance?](#8--wouldnt-this-need-total-surveillance)
- [9 — Didn't this fail before?](#9--didnt-this-fail-before)
  - [Can I use it while everyone else still uses money?](#can-i-use-it-while-everyone-else-still-uses-money)
- [10 — What we haven't solved](#10--what-we-havent-solved)
- [Appendix A — Where this came from](#appendix-a--where-this-came-from)

---

<!-- tag: ovw-s0 -->
## 0 — What this is, in one page

Aequitas is **an accounting system.** Not a currency, not a token, not a blockchain, not a political programme. It is a way of keeping books.

**And it is not a piece of software.** These documents do not specify one, and they never will. What database to use, what a record looks like on disk, which cryptography to pick, how to keep it private — **all of that belongs to whoever builds it**, the same way banks, not capitalism, decide what a banking system runs on. What this project owes a builder is a different thing: **a list of what must be true** for the books to be Aequitas at all. What must be true is here. How to build it is theirs.

Here is the whole idea:

> **Everything anyone makes, uses, or throws away is matter and energy moving through the world. That movement can be recorded. Once it is recorded honestly, most of what we find unjust about the economy stops being possible.**

Money is very good at one job — letting strangers trade — and very bad at another: telling the truth about what things take. A price tells you what someone was willing to accept. It does not tell you how many hours of human life went into the thing, how much fresh water it drank, or what it will cost to clean up afterward. Those numbers exist. They are simply not written down anywhere.

Aequitas writes them down.

**One crucial distinction, and everything else depends on it.** Aequitas is a theory of **cost**, not of value.

- **Cost** is what a thing takes from the world — hours, joules, kilograms, damage. It is physical. It can be measured.
- **Value** is what someone thinks a thing is worth. It is a feeling. It cannot be measured and Aequitas does not try.

Every previous attempt at an "objective" economy tried to compute what things are *worth*, and every one was demolished with the same sentence: *you have described supply and ignored what people actually want.* Aequitas makes the narrower claim, which is also the defensible one. **What people want still matters enormously — it just enters the system somewhere else** (see §6).

Two words do all the work:

| | |
|---|---|
| **Credit** | A record that you did some work. An hour of your life, spent on something. |
| **Debit** | A record that something was taken from the world — material, energy, or damage — and who is holding the consequence. |

That is the entire vocabulary. The rest of this document is what follows from taking it seriously and never making an exception.

<!-- tag: ovw-s0-who -->
### And who actually does this?

**Aequitas is a system in the sense that capitalism is a system.** Nobody joins capitalism. There is no office, no membership, no headquarters. It is a set of ideas about how value moves, and **banks, firms and governments are what actually carry it out.**

Aequitas is the same shape. It is a set of principles about how cost is counted. **The people who carry it out are called trust networks**, and almost everything in this document is really a description of something a trust network does.

> **A trust network keeps the books.** It records the material flows, the hand-offs, the services, the pledges, and the measurements of the world itself — how much of a pollutant is in the air, how much a region actually grew. **It checks the arithmetic. It publishes its methods so anyone can check them back.**

**Think of them as laboratories rather than banks.** Their business is getting the numbers right, and they publish how they got them so that other networks can find their mistakes. **A network that lets fraud through is helped by a rival network sharing the method that catches it** — not out of goodwill, but because in a system where two networks trade, a bad method in one corrupts the books of the other.

**This matters for reading the rest of the document.** When a later section says the books catch an under-declared emission, or that an estimate improves as better data arrives, or that a purchase is refused because someone is over their limit — **a trust network is the thing doing it.** Aequitas says what should be counted. Trust networks are where the counting happens, or fails to.

**And they are not prescribed by this project.** How a network handles privacy, what technology it runs on, which laws it must satisfy, how it documents its own founding — all of that is theirs to decide. **They compete on one thing only: how close to the truth they can get.** A network people cannot check is a network people will not use.

*The detail is in `00-strategy/C2_TrustNetworks_v0.1.md`.*

---

<!-- tag: ovw-s1 -->
## 1 — Problem: Inequality

*The oldest problem: wealth piles up.*

Nearly every political argument, whatever its flag, is an argument about who controls resources and how they are shared out. Conservatives blame outsiders and regulation; liberals blame tax policy and underfunded services; the left blames capital and class. **What all of them share is an unexamined assumption: that owning things is the same as being wealthy, and that this is simply how reality works.**

It isn't. Property is not a fact of nature. Hobbes and Hume both pointed out that without an authority to enforce it, "mine" means nothing — property is a social arrangement we agreed to, and agreed arrangements can be re-agreed. [Rousseau](https://en.wikipedia.org/wiki/Discourse_on_Inequality) went further and called the first man to fence off land and say *this is mine* the founder of civil inequality. Many Indigenous traditions never adopted the idea at all, framing the relationship to land as stewardship rather than title.

The trouble with ownership as we practise it is that **property is not just a thing you have — it is a machine for getting more.** You own, so you can rent, lend, and charge; you accumulate; you buy influence; you use influence to protect the arrangement. The loop closes on itself.

The traditional answer has been to take the property away and hold it in common. Every serious attempt to do that by force produced a new elite holding the same concentration under a different name. **Concentrating the power to redistribute is still concentrating power.**

<!-- tag: ovw-solution-debit -->
### Solution: Debit

*Stop treating possessions as a score. Start treating them as an obligation.*

Consider an ordinary morning. Someone wakes up, showers, dresses, walks to a train, buys a sandwich, eats it, drops the wrapper in a bin, and goes to work.

Now look at the sandwich. Wheat was grown somewhere, drinking irrigation water and fed with fertiliser that ran off into the water table. It was harvested — some spilled, some rotted — milled, baked, assembled, wrapped in plastic, and driven to the shop in a truck burning fuel. A mechanic fixed that truck's leaking oil filter, and the old oil went somewhere. The wrapper is now in a landfill, and will still be shedding microplastics into groundwater in a thousand years. Maybe one day something will clean that up. Today, it is simply out there, unpaid for.

**Every one of those is a real, physical, countable event.** Aequitas records them, and calls the whole bundle the sandwich's **debit**.

And here is the reframe that changes everything:

> **When you take something, you take on its debit. Possessions are not what you are worth. They are what you owe the world for holding them.**

Two kinds of debit behave differently, and the difference matters:

- **Property debit** — the embodied *material* you are holding — is *dischargeable*. You carry a house's material debit while you hold the house; hand it on, and it goes with it. You are not punished for owning, but you cannot pile things up for free either.
- **Consumption and pollution debit** is *permanent*, and it stays with **whoever caused it** — it never travels with the object. You ate the sandwich; that is yours for good. But the fertiliser the farmer let run off stays on the *farmer's* record, and the fuel the trucker burned stays on the *trucker's*. You didn't cause those. They did.

**So a thing carries its whole story, but not everyone's debt.** Buying the sandwich, you take on its *material* and the fact that you ate it — not the farmer's pollution and not the trucker's fuel. What you *do* receive is the full record of where it came from, so you can prefer the cleaner loaf before you buy. **The debt sits with whoever caused each harm; only the story travels with the bread.** This turns out to be a stronger arrangement than making the shopper pay for the farm's runoff — more on why in §4.

![The debit taxonomy at a glance: a debit splits into property debit (the material you hold, which travels with the thing; and the making-hours, which stay partly with you — see §2) and consumption/pollution debit (permanent, on whoever caused it). Two rules cut across both: working on your own things nets to zero, and cost never passes to someone who didn't cause it.](../01-wiki/assets/debit-taxonomy.svg)

*The whole taxonomy on one page. It shows a little more than this section does — the "making" hours of a thing stay partly with you even after you pass it on, which §2 comes back to — but the two big ideas are here: what travels and what stays, and who is on the hook.*

**A consequence worth sitting with.** Suppose you spend a weekend repairing your own roof. You earn credit for the hours — real work, really done. But the repair also raises the house's debit by exactly those hours, and you are holding the house. **Net effect on you: zero**, apart from the materials you actually consumed.

That identity is the whole of §7 in one line. **Property cannot be an engine, because working on your own property never gets you ahead.** Nobody has to ban landlords. There is simply nothing there to earn.

**And nobody starves for having a low score.** Everyone earns a baseline just by staying alive (§2) — the real, counted work of maintaining a human — so there is always something behind your basic needs. On top of that, an account carries some **debit tolerance**, scaled by age and circumstance, and exceeding it restricts *luxuries*, never necessities. A nurse is credited for nursing you whatever your books look like. This is not charity bolted onto the system; it is a structural requirement, because a system where being mis-measured can starve you is a system nobody should adopt.

**And here is why the gap between most and least is *capped* in a way money's isn't — the engine is arithmetic, not any rule.** Money can be piled up without limit; time cannot. Everyone gets the same 24 hours a day, you cannot buy anyone else's, and credit — a record of *your* time — never moves. So the most anyone can out-earn anyone else is the ratio between a full day's work and the baseline everyone already gets for living. If a community counts, say, 10 hours a day as the cost of simply keeping yourself going, the busiest possible contributor tops out around 24 ÷ 10 — under three times the person who only lives. Set against today, where the top of the scale runs into the *millions* of times the bottom, that is a different universe.

**Two honest caveats, because this is the theory's single biggest claim and it would be easy to overstate.** The number is not a flat certainty — it holds *if* a couple of things go right. It depends on how generous each community sets that baseline (a low baseline loosens the cap — see §10), and on the system being able to confirm that someone's hours are *real* without prying open their whole private record. That last piece — proving a claim is backed by genuine work without exposing a life history — is one of the genuinely unsolved problems (§8). So the honest version is: **if that verification problem is solved and baselines stay sane, the gap is capped in a way money never is.** Still a different universe — just a *conditional* result, not yet a theorem.

**And here's something that's true even before any of that.** Aequitas only ever counts *material* things — what you physically hold, use, and consume. It never counts money-wealth: a share of stock, a bond, a crypto-token is a claim on paper, not matter or energy, so it simply doesn't appear. (The factory those shares represent *is* counted — but on the people who actually run it, not on the distant shareholder.) That one fact does something striking on its own. Today the richest person's *money* is around a million times the typical person's. But their *stuff* — the houses, jets, yachts, the actual physical consumption — is only a few hundred times as much, because you can only physically use so much in a 24-hour day. **Strip away the paper and the real gap is already about a thousand times smaller than the money gap makes it look.** When we ran the numbers on real wealth data, only a fraction of a percent of people — the genuine mega-consumers, not the merely rich — would even be over their limit, and most people would come out *ahead* by joining. The inequality we live under is, to a startling degree, an artefact of counting paper.

**One more thing the simulations kept finding: there is no shortage of work-hours.** Because looking after yourself is counted as work, the total pool of human labour is several times larger than anything an economy actually needs to run. We checked whether the United States could supply *everything* it consumes using only its own people and resources — and labour was never the bottleneck; energy and materials were. We checked what it would take to house and treat everyone on Earth who lacks housing or healthcare — and the hours freed up from waste and enforcement covered it many times over. **"We can't afford to make it / house them / heal them" almost always turns out to be a statement about money, not about human hours.** What's genuinely scarce is materials, energy, and the will to point our work at the right things — never the hands to do it.

**We can now put a number on it.** Adding up everything a typical American consumes in a year — food, housing, healthcare, everything they buy, and the share of things made abroad — comes to about **1,380 hours of other people's work.** Set that against the roughly 3,650 hours of credit each person earns every year *just by staying alive*, and a median lifestyle costs about **a third of what one person contributes**. There is simply no labour crunch.

**And here's the part that surprised us most.** The reason a comfortable life *looks* unaffordable for everyone is not the standard itself — it's the wasteful way it's often produced. When we measured the same kind of middle-class life in other rich countries, the United States turned out to be the big outlier: it uses **50–80% more human labour and two-to-four times the carbon** per person than Germany, Sweden, France, Japan, or Spain — countries that deliver a comparable material life *and longer lifespans* for far less. Sprawl, fossil fuels, and long tangled supply chains are the difference. Under Aequitas the efficient way is automatically the cheaper way — because the pollution and the extra hauling and the bloated overhead all show up as real costs in the books — so **the system quietly rewards exactly the efficiency those countries already prove is possible.** Produced the leaner way, a decent life for everyone on Earth fits comfortably inside the work the world already does. Abundance comes from producing *smarter*, not from working *more*.

---

<!-- tag: ovw-s2 -->
## 2 — Problem: Debt

*The world economy now needs ever-growing debt just to stand still.*

Total debt in the United States ran at about 140% of GDP from 1960 to 1980. It is now roughly 300%, and the same curve shows up globally. Not even the 2008 crash — itself caused by too much borrowing — bent the line.

An economy that needs a constant supply of *new* debt to generate demand is an economy permanently one disruption away from a seizure. That is what happened in 2008 with household debt, and the response was to shift the load onto government debt instead. The trick works while borrowing costs stay below growth. It is not a solution; it is a longer fuse.

<!-- tag: ovw-solution-credit -->
### Solution: Credit

*Work is recorded in time. And the record can never move.*

**A credit is a record that a specific person spent a specific hour doing something.** It is not a claim on anyone. Nobody owes it to you. It is simply a true statement about the past, and true statements about the past do not change owners.

> **And "work" means time *spent*, not effort.** This is the one mental shift Aequitas asks of you. Credit counts the hours of your life you put in — not how hard you strained. Two people who spend an hour on the same task are credited the same, whether one breezed through it and the other found it gruelling; a real difference in effort, if it matters, shows up as a *material* cost (the harder worker eats more; a dangerous job's harm gets priced in) — never as a bigger number for the same hour. Once you see credit as *time spent*, something surprising follows: **looking after yourself is work.** Sleeping, eating, resting, keeping yourself going is time spent maintaining a living human — exactly as looking after a child is, and history refused to count *that* only because nobody was paid for it. So everyone earns a baseline simply by staying alive. That baseline is not a hand-out bolted onto the system; it is the real work of being alive, finally counted — and it is where the floor under everyone (§1) actually comes from.

Three things follow.

**1. Everyone's hour counts the same.**

No profession earns at a higher rate. This sounds naïve until you see where the differences actually go:

- **Hard labour** — a labourer eats more. That extra food is recorded as real food-production cost, borne by the work that required it.
- **Dangerous labour** — if a process turns out to damage the people doing it, that harm is priced back into the products that process made. Even decades later.
- **Skilled labour** — and this is the important one.

**Training is work, and it is carried at the time.** A medical student is credited for their hours studying, exactly as a bricklayer is credited for hours laying bricks. The cost of that training — the teachers, the buildings, the equipment — is carried *during the training years*, cushioned by the people who wanted doctors to exist putting their credit behind it.

Which means: **the doctor's education never appears on any patient's bill.** Your visit costs their time, the clinic's materials, and the medicines you were given. Nothing else. It was already accounted for, up front.

That is a better answer than a pay premium in two ways. It makes becoming a doctor *immediately* worthwhile rather than a decades-long bet. And it puts the cost where the benefit is — everyone benefits from doctors existing, so everyone bears it, rather than charging one unlucky patient in 2044 for a lecture given in 2026.

**This same move solves several problems at once**, and it's worth naming as a rule:

> **A large up-front cost with a spread-out benefit is carried when it happens, cushioned by the people who wanted it. It is never charged downstream to whoever happens to use the result.**

Education. Research. Infrastructure. Films. A blockbuster's viewers pay for the *delivery* — the projector, the power, the bandwidth — never for the four years of production. More on this in §5.

**And this is the only thing that lets the books ever close.** Picture charging a hospital's construction to its patients. To do it honestly you would have to fold in the builder's costs, and the cement plant's, and the steel mill's, and the schooling of the engineers who designed the place — back and back, with no end, to the first human who ever built anything. The sum never finishes. Front-loading is what stops the regress: a building's cost is fixed once, up front, and a patient's bill never reaches back past the front door.

**So who carries a building year to year?** The whole cost rides the **building itself**, shared among the people who run it — and shared *by how long each has worked there*. A nurse hired on Monday inherits almost none of it; a thirty-year veteran a little more. Nobody takes on a whole hospital by walking in the door — which is exactly what would otherwise scare people away from staffing the places that need it most. The community's pledges don't erase that cost — they give the staff the *room* to carry it, cushioning the bite. And because a pledge is **permanent — it can't be taken back** (see §6) — the staff can rely on that room and get on with the work; the cost is a one-time expense to whoever pledged, not a loan that can be called in.

**And the share you built up stays yours — you can't hand it off by walking away.** The *stuff* of a thing (its material) travels with it when you pass it on. But your share of the *work that made it*, earned by the time you held it, stays on your record. Own a 500,000-hour mansion for ten years and hand it on, and after the next owner has held it as long as you did, roughly half of that making-cost is still on your books. You can't dodge it by giving the thing to someone outside the system either — if there's no record of a hand-off, the record still shows *you* holding it, so you keep the whole weight. The one thing that lightens your load is a *real* new holder taking it on. A useful side effect: **second-hand things start out cheap** for the new owner — they've put in no time yet — and grow heavier the longer they keep them.

**2. Credit cannot move, so nobody can be owed.**

Your credit is a fact about you. It cannot be given, sold, lent, taxed, gambled, or stolen. There is no transfer mechanism, not because transfers are forbidden but because there is nothing coherent to transfer — you cannot hand someone the fact that you worked on Tuesday.

**A debt crisis requires a creditor who must be made whole.** Here there are none. The mechanism that turns a bad year into a spiral simply has no part to attach to.

**3. The books never balance — and they must not.**

Total debit will always exceed total credit, everywhere, permanently. Every real process wastes something; energy dissipates; matter degrades.

**This is not a flaw in the accounting. It is the second law of thermodynamics showing up in the ledger, and a set of books that *did* balance would be the ones describing something physically impossible.**

So the sum is meaningless, and two separate numbers matter instead:

- **How much you contributed** — your total credit.
- **How efficiently you live** — how much you consumed per unit contributed.

Neither replaces the other. Efficiency alone is infinite for a newborn and is gamed by an ascetic who does nothing and consumes nothing. Contribution alone ignores waste entirely.

---

<!-- tag: ovw-s3 -->
## 3 — Problem: Gambling and Rent

*Anything interchangeable can be bet, cornered, and rented out.*

A casino is the obvious case, but it is the smallest one. The property that lets you gamble money is the same property that lets you do all of this:

- lend it at interest and earn without working
- own a building and charge people for standing in it
- corner a market, hold a commodity off it, and wait
- speculate on a thing you will never use and do not want
- print more of it and quietly shrink everyone's savings

**Every one of those is the same feature wearing a different hat: money is interchangeable.** One dollar is any dollar. That is precisely what makes it useful for trade, and precisely what makes it extractable.

<!-- tag: ovw-solution-non-fungibility -->
### Solution: Non-fungibility

*Every credit is a record of one specific event, by one specific person.*

There is no chip. There is nothing to push across the table, nothing to lend, nothing to corner, nothing to inflate.

Note that none of the above is *banned*. Nobody writes a rule against usury or rent-seeking, nobody enforces it, nobody can be bribed to look away. **These activities are unavailable in the way that dividing by zero is unavailable.** One structural property closes five doors, which is a much better bargain than five laws.

The same property means **there is no price at all — only a cost.** The number on a thing is a statement of what that thing took, and **you cannot mark up a measurement.** If a shop asks more than a thing cost, the number is just wrong, and the books show it.

**And that number is narrower than people expect, on purpose.** It carries **what the thing used up**, and nothing else. A farm's barn is not in the beef. A factory's machines are not in what they made.

> **This is the most common objection to Aequitas, so here is the answer with a number in it.**
>
> A barn costs **20,000 hours** to build and shelters cattle for **20 years**, over which the farm sells **40,000 kg** of beef. Split the barn across the beef and you would add **0.5 hours to every kilogram**. Aequitas adds **nothing.**
>
> **The 20,000 hours did not disappear.** They sit on the farmer, for as long as they hold the barn. To carry that much debt you need about **16,700 hours** of credit standing behind it — **roughly four and a half years of everything one person earns.** *That* is what stops a barn going up that nobody needs.
>
> **Now do it the other way and watch who pays.** The 20,000 hours come off the one farmer and land on about **40,000 shoppers**, half an hour each. None of them chose to build a barn. **The only person who made the decision is the only person the cost stops bothering.**
>
> **The rule that looks like it is hiding a cost is the rule that keeps the cost pointed at whoever chose it.**

**One honest consequence, and the books say so out loud.** Two farms selling the same beef — one with a big barn, one with a shed — show the **same** number per kilogram. The number tells you what the beef took, not what the farm's whole way of working costs. **What keeps the big barn honest is the farmer's own ledger, not the sticker** — the same way pollution is kept honest by sitting on whoever caused it (§4), rather than by hoping a shopper notices.

**What survives — and it is essential.** Removing profit does not remove competition. Producers still compete, hard, on **quality, craft, and efficiency**: doing the same thing with fewer hours, less material, less waste. That is genuine rivalry with the extraction stripped out, and the system leans on it heavily (see §7).

**And genuine risk survives too.** Building something nobody wants still burns real hours and real material. Enterprise remains a gamble in the honest sense. What disappears is the other kind — the sort where you win by holding an asset while someone else works.

---

<!-- tag: ovw-s4 -->
## 4 — Problem: Externalities

*The costs that nobody pays are the costs that get made.*

An externality is a cost you cause and someone else absorbs: the smoke, the runoff, the depleted aquifer, the worker's ruined back, the wrapper in the ocean. Every economy in history has had them, because they are not a mistake — **they are a competitive advantage.** The producer who dumps outsells the one who cleans up.

<!-- tag: ovw-solution-there-is-no-outside -->
### Solution: There is no outside

Under Aequitas, **every consequence is priced into the thing that caused it.** Not by a regulator noticing, but because that is what the accounting *is*: the pollution is a material flow, and material flows are what the ledger records.

Three consequences follow immediately.

**Harmful production penalises the producer, directly.** A factory that pollutes carries the cost of cleaning it up — permanently, on its own record, whether or not any customer ever notices. Exploitative labour carries the cost of the harm it does, borne by whoever imposed it. This is stronger than the usual hope that shoppers will choose the greener product (they mostly don't): the polluter is out of pocket at the source. And because every product still carries its origin record, a buyer who *does* care can see the difference and steer toward the cleaner maker on top of that. **The incentive gradient reverses, with nobody enforcing anything, and it does not wait on anyone noticing.**

**The pollution from your electricity is *yours*.** There's one case worth spelling out because it surprises people. Most pollution stays with the producer who caused it — the miner keeps the mine's, the factory keeps the factory's, and buying the product doesn't move it to you. But **electricity is different, because it can't be stored**: the power is generated the *instant* you draw it, so flipping your switch is what commands a generator to burn the fuel. That makes the generation pollution *yours* — the same way your car's tailpipe is yours, not the carmaker's. You carry the emissions of **the supply you signed up for**, so buying from a cleaner provider genuinely lowers your own record and pushes generators to compete on being clean. (This lines up electricity with how driving and home heating already work — it isn't a special case, it's the same "whoever burns it, owns it" rule.)

**Regulators become something businesses want.** An environmental agency's job stops being punishment and becomes advice: *here is how to lower your debit.* Every hour they save you is an hour off your product's cost. Enforcement quietly turns into consulting.

**Taxation becomes unnecessary.** Civil servants are credited directly for the work they do — there is no salary that needs funding first. People who use a road carry a share of its debit by using it. There is nothing left to collect, and therefore nothing to argue about collecting.

<!-- tag: ovw-two-things-this-requires-and -->
### Two things this requires, and both are features

**Costs discovered later are applied backwards.** When science improves — a cheaper way to capture carbon, a newly proven occupational harm — **every affected record in history recalculates.** Your ledger is not a stored number; it is recomputed from the log of what actually happened, using today's best understanding of what those events cost.

This means **the system permanently pays for better measurement of reality**, forever, which is an unusual thing for an institution to do. It also means **no error is permanent**: an early estimate that turns out wrong is corrected the moment somebody does the science, and the correction reaches all the way back.

**And the cost of a pollutant rises and falls with how much of it is already out there.** A substance only counts as pollution once there is more of it than the world clears on its own — steel that rusts away as fast as it is made, or carbon the planet reabsorbs at the rate we emit it, is just part of the cycle and costs nothing. Above that line, the more of it in the air or the ground, the more work it takes to deal with, so **every record of it grows heavier together.** The flip side is the good part: when the world cleans some up, *everyone's* past share of it gets lighter, backwards through history. **Cleaning up the commons pays back the people who fund it** — which is, for once, a reason to fund it.

**When one process makes several things, the process itself says how the cost divides.** A steer yields beef, hide, tallow, bone, manure, and methane from one pool of feed and effort. For a century, people tried to split such costs by *choosing a rule* — by weight, by energy, by price — and every rule that worked in one industry was nonsense in the next.

Aequitas doesn't choose. **It measures where the animal's own biology sent the feed.** The instrument changes with the process — tissue chemistry for livestock, cracking energy for a refinery, the heat-and-power trade-off for a turbine — but the question is always the same one, and it always has a physical answer. A hide's share does not go up because leather came into fashion.

**And the barn is nobody's share of the hide.** The buildings, the tools, the machinery — the *capital* a business runs on — never get sliced up and dribbled into each product either. They are handled the same way a hospital is (§2): carried by the people who run the place, cushioned by pledges made up front. A wafer is not charged a fraction of the factory that made it. This closes a question that quietly defeats ordinary cost accounting — *how much of the fab belongs in one chip?* — by answering: none of it. The fab belongs to the people who run the fab.

<!-- tag: ovw-you-own-the-end-of -->
### You own the end of a thing's life, too

Most accounting stops when a product is sold. Aequitas doesn't. A thing that has stopped being useful and is sitting in a landfill **is** pollution for as long as it sits there, and that debit rests on whoever last held it — as though they had eaten it. Nobody can dump a worn-out machine on a recycler who doesn't want it; if no one will take it, its last owner has effectively consumed it.

Three ordinary incentives fall out, none of them asking anyone to be virtuous:

- **Buy things that last.** A cheap, unrepairable gadget whose disposal cost you'll be holding is no longer the cheap option.
- **Look after what you have.** A hospital is better off maintaining its equipment than running it to death and replacing it.
- **Fund the clean-up.** Recycling and remediation *lighten your own record*, because the pollution they remove is pollution you were carrying.

And recycling genuinely pays: recycled material never carried the mine's pollution in the first place — that stayed with the miner — and reusing it means nobody has to dig up more. **The recycler is credited for the work of making the world's junk useful again.**

<!-- tag: ovw-and-you-don-t-own -->
### And you don't own the land — you owe for occupying it

Here is a consequence that sounds radical and turns out to be simple bookkeeping. **Land can't be owned.** A building doesn't sit on property you hold a deed to; it occupies a patch of the Earth — and occupying it is itself a debt. **Every building carries the cost of putting its patch back the way nature had it:** clearing the contamination, pulling out the foundation and the buried pipes, filling the hole, letting the wildlife return. That debt only clears when the restoring is actually done.

Two things fall out, and both are fair. You're only on the hook for what *you* did — a house built two centuries ago on unrecorded or forced labour doesn't put that old harm on today's occupant; they carry only what they themselves caused while living there (the gas stove's emissions, say). And what a plot "was like naturally" is a genuinely hard line to draw for somewhere that's been a city for centuries — it's the same kind of judgement call as deciding how much of a pollutant the world can absorb on its own, and it's handled the same careful way (§4, §10).

---

<!-- tag: ovw-s5 -->
## 5 — Problem: Intellectual Property

*Ideas are the one thing in the universe that costs nothing to copy. We have built an entire legal apparatus to pretend otherwise.*

Patents and copyright exist for one purpose: to let a holder charge for reproductions. To do that, they must manufacture scarcity in something that is not scarce. The results are familiar — medicines priced beyond the people who need them, research locked behind paywalls, decades-long terms outliving the creator, and litigation as a business model.

<!-- tag: ovw-solution-front-loaded-creation-and -->
### Solution: front-loaded creation, and meme tracing

**Most of the machinery simply evaporates.** With no profit in exchange (§3), there is no revenue stream for exclusion to protect. Copyright without a market for copies is a lock on an empty room.

**So who pays for the making?** The people who wanted it, while it is being made. A film's crew are credited for their hours during production, and the debit is settled then, by those who pledged for it (§6). **The audience pays only for delivery** — the theatre's upkeep, the projectionist, the electricity, the bandwidth.

Notice what that removes. **A popular film cannot gouge its audience, because there is no mechanism by which it could.** The production's only return is recognition — which converts into enthusiasm and pledges for the next work. The whole incentive points at making something good rather than something extractive.

**Meme tracing** is the attribution side: ideas are traced as they spread and adapt, so originators are recognised without anyone being blocked from using the idea. That recognition is **never credit** and never converts into it. It is reputation, and reputation's only power here is to attract support for what you do next.

Two honest caveats, because overclaiming here would be easy:

- **The standard is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making — you trust the seller. That is fine at human scale, and provenance only turns vicious in the capitalised art market, which is exactly the layer being removed. Aequitas does not need to solve a problem the current world also hasn't solved and doesn't much suffer from.
- **The obvious argument doesn't generalise.** People say a copied recording advertises the live show — someone can pirate the track but won't play the concert. True for music. Much weaker for novels, software, and research. It's a good illustration, not a rule, and it's presented as one.

---

<!-- tag: ovw-s6 -->
## 6 — Who decides what gets made?

This is the question every planned economy failed. If prices don't direct production and no committee does, what does?

**The answer is that people put their credit behind the things they want made.** Two instruments, separated by one test: *is it backed, one-for-one, by credit you actually earned?*

| | **Pledge** | **Signal** |
|---|---|---|
| Means | "I'll put an hour of my credit behind making this happen" | "I want this to exist" |
| Backed by | your earned credit, one-for-one | nothing |
| How much | exactly one hour pledged per hour worked | plenty — signal freely |
| Familiar as | a wishlist that funds; choosing your GP; crowdfunding; commissioning a job | likes, reviews, applause |

**A pledge doesn't spend your credit, and it isn't a promise to buy.** Your credit stays yours — a pledge just puts it *behind* something, the way naming a beneficiary doesn't hand over your bank balance. It gives whoever you're backing more room to carry the cost of the work. What it *does* use up is a separate **lifetime allowance** — you can pledge, in total over your life, as many hours as you've earned, and **a pledge is permanent: you can't take it back.** That permanence is deliberate — the people you back can rely on it and get on with the work — and because a pledge is a real, one-time expense, nobody can pledge frivolously or flood the system for free.

**A pledge summons work — it doesn't have to be about a *thing*.** Say you've earned four hours and you pledge two toward mowing the scrappy public verge on your street. Someone with a mower sees it, spends an hour, shows proof, and earns an hour of credit. That's the whole transaction — no object changed hands, nobody's credit was cancelled, and one pledged hour is still behind the next mow. Where the pledged work *does* make an object, taking that object is a separate step: whoever accepts it takes on its debit with their *own* room, pledge or no pledge. It's deliberately messy — people will pledge for silly things, pledges will go unfilled, groups will form to coordinate them — and that's fine. Messy or not, it's the thing that creates jobs.

**Pledges are the demand side of the economy.** Cost tells you what something takes; pledges tell you who wants it. Together they do the job prices do, with no central optimiser and no board deciding priorities.

They must be strictly one-to-one: the hours you put behind things over your life can never exceed the credit you've actually earned. Let it, and people would be backing work with room that isn't really there — the makers leaning on it would be standing on a promise nobody can keep. That's not a preference, it's arithmetic.

**Signals should be abundant** precisely because pledges are scarce. If pledging is all you have, the system only ever hears your single top priority and learns nothing about the rest. Cheap signals reveal what you actually care about, in order.

Three things this quietly fixes:

- **It gives surplus a purpose.** Since credit cannot be accumulated into wealth, someone who produces far more than they consume would otherwise have no outlet. Instead they get to **direct what the world works on next** — which is a considerably more interesting reward than a larger pile.
- **It funds the speculative.** A prize for solving a hard problem needs no billionaire patron; a large enough pool of pledges *is* the prize.
- **It sets the number of doctors.** Society decides how many to train by pledging for it — no ministry, no quota. Study nobody pledged for still credits your hours, but leaves you carrying the cost.

- **It gets dangerous work done — without danger-pay.** Everyone earns the same credit per hour, so there's no hazard bonus to lure people into a toxic cleanup. Instead, when lots of people pledge to see it done, the pledges *beyond* what the job costs become an **insurance fund** for that job: it only pays out if the work later harms whoever did it (their medical care, cleaning up a mess that resurfaces, harm to bystanders). Society de-risks the worker exactly as much as it wants the job done. Because that fund can only ever cover real harm — never be pocketed as a treat — it rewards the nasty work without making anyone richer than anyone else. (It helps with *dangerous* unwanted work; plain *boring* work is still an open problem.)

**One honest weakness.** Pledges follow reputation, so a first-time maker attracts none. This is the same cold-start problem unknown creators face with money today, and the barrier is much lower — attention rather than capital — but it is real and shouldn't be waved away.

<!-- tag: ovw-when-does-the-work-actually -->
### When does the work actually count?

Your work is written down the moment you do it — but it **counts once the result is checked.** For something you *made*, the check is simple: it counts when the thing **changes hands.** When a workshop hands a batch of toasters to a driver, the driver — by taking them on, and taking on the debt that rides with them — is confirming the toasters are real. That confirmation is what turns the makers' hours into credit that counts.

**What "checked" means depends on what you did.** For a *made thing*, it's the hand-off above. For a *service* with nothing to hand over — a haircut, an hour of counselling — it's the person you did it for confirming it happened. For *creative or intellectual work*, it's evidence the work was really done — never a tally of how many people *liked* it (approval is not the check, or applause would quietly turn into money). And for the work of *keeping yourself alive*, the check is simply that you're still here: a living, verified person plainly did the maintaining. Different kinds of work, checked in the way that fits each — and the trust networks (§7) are the ones who work out and police exactly how.

This has three quietly powerful effects:

- **Nobody can hold your pay hostage.** You're credited as soon as *anyone* takes the goods off you — you never have to wait on one particular buyer's say-so. And because whoever holds a thing holds its debt, a middleman who sits on goods is just sitting on debt: they're pushed to pass them along, not to block them.
- **The count checks itself.** Nobody accepts more toasters than actually arrived, because they'd be taking on debt for goods they didn't get. So the numbers can't be quietly inflated — the person on the other side has every reason to count honestly. No inspector required.
- **Bosses have nothing to extract.** There's no wage to pay (credit can't be handed over), no profit to skim (price is just cost), and the debt of a shared job is split by *hours worked*, not by rank — so no one can push the risk of unsold goods down onto the people who did the work. What's left of a "boss" is a coordinator, credited for their own hours like everyone else.

*(If you make things nobody has pledged for, you're taking a real gamble — you hold the goods and their debt until someone wants them, exactly as an entrepreneur does today. Make things people **have** pledged for and the gamble is much smaller — there's committed interest behind the run, and since pledges are permanent that backing can't vanish under you. It still isn't a guaranteed sale, so it softens the risk rather than erasing it.)*

---

<!-- tag: ovw-s7 -->
## 7 — Who checks any of this?

Fair question. A ledger nobody verifies is a wish.

**Verification is a ladder, and every rung is compatible with every other.**

1. **Neighbours.** People who were present confirm what happened, and sign off together. This requires no technology at all and works in any village on Earth today.
2. **Reputation and trust networks.** Verifiers stake their own standing on what they attest; patterns get audited. **Auditing is credited work** — it pays for itself from inside the system, rather than depending on volunteers.
3. **Sensors.** Meters, scales, and instruments producing signed, tamper-evident records.
4. **Automated auditing.** Continuous, machine-scale tallying. Far future.

**A region on rung one must be able to trade with a region on rung four**, with the lower-resolution record simply marked as lower-confidence. The ladder is not a barrier to entry; it is a gradient that rewards climbing.

**A few structural points that make this hold up:**

**Balances are not stored — they are derived.** There is no account file with a number in it that someone could edit. There is a permanent, append-only record of events, and your standing is computed from it on demand. Change the record and everyone can see what changed.

**Poorly-supported claims are worth little.** A claim with no witness, no instrument, and no material trace is recorded faithfully and weighed at the pessimistic end — which for a credit claim is near zero. Nobody has to catch a liar. **Vagueness is cheap to assert and cheap to hold.** No account may claim more than 24 hours in a day, either.

**Cost estimates are audited by rivals, not consumers.** If the recorded cost of beef were understated, every beef eater benefits and none of them will fund the correction — but plant-protein producers are directly harmed, and will. **Consumers police one direction; rivals police both.** Notice also what is missing: there is no profit anywhere in the system to fund a convenient scientific result, so the ordinary way cost science gets corrupted today is closed off at the root.

**Everyone is in the books; only participants can act on their position.** Every human has an estimated credit *and* debit position, whether they have ever heard of Aequitas or not — otherwise the accounting would show wheat with no grower, which is false. But an estimate does nothing until you hold a verified account and real records replace the guesses. **Joining is exactly the act of turning an estimate into a record**, and it is usually to your advantage: most people's real footprint is below their cohort's average, and your estimated contribution does nothing for you until you claim it.

**What the checks can see — and what they cannot.** The arithmetic catches a factory whose declared outputs do not balance its declared inputs: the missing material went somewhere, and the books say so without anyone investigating. What it *cannot* do is see a workshop that never joined at all. Nothing you can compute from a record tells you what was left out of it.

So that half is answered a different way, and it is the ordinary way: **measure the world from outside and compare.** A satellite pass over the valley, a harvest total, a port manifest, a reading of how much of a pollutant is actually in the air. If the region grew a hundred tonnes and the books account for sixty, forty tonnes came from people outside the system — and **that gap is a measurement, not an accusation.** Anyone with the same instrument gets the same number.

Two things follow, and they are the point.

**The estimate for whoever stays outside gets worse as everyone else joins.** The figure is shared out across the ones still unmeasured, so as good producers instrument themselves and leave that pool, the guess applied to those remaining rises. **Staying dark stops paying, and stops paying more the longer it lasts.** Nobody is compelled; the books simply become expensive to stay out of.

**And no number here is ever final.** A tally is a citation, not a verdict — it says who measured, how, over what area, and as of when. When somebody measures better, **every affected record recalculates**, backwards, because balances are derived rather than stored. A wrong figure is never deleted or quietly edited; a note is attached to it and a better record is added beside it. That is how science handles a mistake, and it is the only method that does not need an authority standing at the door deciding what may be written down.

> **One guarantee that has to come with that.** Because figures move, the check on what you may consume is made **at the moment you do it.** If a cost is revised upward next year, that changes what you may do *next year* — it never reaches back and turns something you already did into an offence. A ledger that recalculates must never mean a debt that ambushes you.

**Nobody owns the rules.** There is no foundation, company, or standards body with authority over the core. Local variations are expected and compete openly on their merits; the axioms themselves are not amendable by anyone, including whoever builds the first implementation.

---

<!-- tag: ovw-s8 -->
## 8 — Wouldn't this need total surveillance?

**No, and the reason is worth being precise about.**

The accounting covers **what is claimed and attested.** It does not cover, and does not want to cover, everything a person does.

People spend hours making memes, telling jokes, arguing online, cooking for friends, and messing about. That is real time and real effort. Tracing who shared what to whom in order to assign work-credit for it would be both impossible and grotesque, and any group that proposed it would be laughed at — which is the governance model working exactly as intended.

> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it.** The books cover what's claimed. Everything else is life.

**On privacy specifically:** accounts are private, and claims are proven without exposing history — you demonstrate that you are within your position without handing over a list of everything you have ever done.

**This is roughly where society already sits.** You transfer money today knowing your counterparty and nothing whatsoever about anyone else's accounts. Nobody audits those accounts because the trust is parked at a bank. **Aequitas does not require more visibility than that — it requires the same visibility with the trust moved somewhere less capturable.**

**The line is drawn between the market and the person.** What's *made*, what's *wanted*, and what things *cost* is out in the open — pledges, production, and prices are public (though who backed a pledge can stay anonymous, like a crowdfunding backer). What stays private is *you*: your own running tally. This split is the point, not an accident. Public market facts are what let anyone audit a supply chain, let a worker see how wanted their product is, and stop anyone from quietly fudging whether work was really asked for — all without exposing a single person's private ledger. Getting that combination exactly right — open flows, closed persons, and no way to reverse-engineer one from the other — is the honest open problem below.

*(What exactly an auditor must be shown to verify a claim without seeing a history is still being specified. It is an engineering question with a known shape, not an unsolved contradiction.)*

---

<!-- tag: ovw-s9 -->
## 9 — Didn't this fail before?

It should. A century of alternative economies died, and pretending otherwise would be dishonest. They died in three distinct ways.

| How they died | What actually happened | Does it reach Aequitas? |
|---|---|---|
| **Circulation** | [Ithaca HOURS](https://en.wikipedia.org/wiki/Ithaca_HOURS) businesses ended up *drowning in Hours* they could not spend; Burlington Bread piled up at cafés. Local scrip flows to whoever buys supplies from outside the network, and stops there. | **No. There is no medium of exchange to pile up.** Credit never moves, so nobody ever receives credit from anyone, so nobody can be stuck holding it. |
| **Valuation** | [Josiah Warren](https://en.wikipedia.org/wiki/Josiah_Warren) could not reconcile hour-for-hour trading with skill and unpleasantness. [Time banks](https://en.wikipedia.org/wiki/Time-based_currency), 45 years on, still report chronic shortages of skilled members from flat-rate crediting. | **Partly.** Paying for training up front deals with skill. **Work that is merely tedious or degrading is still an open problem** — see §10. |
| **Institutional** | [Wörgl](https://en.wikipedia.org/wiki/W%C3%B6rgl)'s scrip was shut down by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca's system died when its founder moved away. | **The legal weapon doesn't fit** — there is no issuer, no notes, nothing to counterfeit, and no currency to compete with legal tender. **This is the real reason Aequitas must never be called a currency.** Founder-dependence is a live design constraint: every mechanism must pay its own maintainer from inside the system, or it has an expiry date. |

**The "you can't run an economy without prices" objection**. This is the oldest and most cited attack — every economist brings it first, so it deserves a real answer rather than a wave. It comes in two flavours, and they need different replies.

**The first flavour (Mises): without market prices, you can't know what anything is *worth*, so you're allocating blind.** The reply is the distinction this whole document is built on: **Aequitas never computes what things are worth.** It computes what they *cost* — hours, energy, materials, damage — which is physical and measurable. The objection assumes its target is trying to price value without a market. Aequitas isn't. It concedes, cheerfully, that you can't measure worth without a market — and then points out it wasn't trying to.

**But that raises the fair question: if cost ignores what people want, who decides what gets made?** Not a committee — that's the failure mode of every planned economy, and the point where the objection would be owed the whole argument. The answer is **pledges** (§6). People spend their own earned credit to call the things they want into being, and cheap signals carry everything milder. A market price secretly does two jobs at once — it tells you what a thing took *and* how much people want it, mashed into one number that can never be pulled apart again. Aequitas keeps the two jobs **separate**: cost measures what a thing took; pledges reveal who wants it. Between them they steer production, with nobody in charge.

**The second flavour (Hayek): the knowledge is scattered and unwritten — no central calculator can gather it.** This one is sharper, and honesty requires only a partial claim. Part of it Aequitas answers: it gathers data *locally* — the person on the spot, the meter on the machine — never demanding one authority assemble everything. But the deeper point — that a lot of what people know is a gut feel that never gets written down — a ledger of physical flows genuinely doesn't capture, and shouldn't pretend to. The escape is that **Aequitas isn't a plan.** It sets no targets and optimises no grand objective; it just keeps the books under an ordinary decentralised market where the person on the spot still makes their own call. Hayek's objection is to central *planning*. Aequitas isn't one, so it doesn't have to solve his problem — only avoid recreating it.

**And "it's too big to compute" has been tested and answered.** [Cockshott and Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) showed that calculation in physical units at national scale runs on ordinary hardware with sparse-matrix methods. People ran the arithmetic; it runs. *(The full, rigorous version of all of this — including how genuinely scarce things get rationed without profit — is `00-strategy/OP-9_calculation_reply.md`.)*

<!-- tag: ovw-s9-parallel -->
### Can I use it while everyone else still uses money?

**Yes. That is the only way it could ever start**, because for years most of the people you deal with will still be outside.

**Nothing is banned in either direction, and both directions cost you a little on purpose.** The pressure always runs the same way: toward trading with people who are also inside.

**Bringing something in.** You made a chair using timber you bought with money. That chair has no history in the books — nobody recorded where the wood came from. So when you sell it to someone inside, one of two things happens. You write up its history properly, or you use a **published standard figure** for what a chair of that kind costs, so the sale can go through right now instead of waiting. **The standard figure is deliberately set a bit dear**, because otherwise nobody would ever bother keeping real records. And notice what happened to you: you spent money on the timber and got no money back. **That is the cost of bringing money-made things in, and it is meant to be there.**

**Selling something out.** You baked bread from flour you got inside, and your customer only has money. **Sell it — nobody stops you. But the bread's debt stays on your books.** As far as the accounts are concerned you gave the bread away, and **they never see the money at all.**

**That last part is not a rule someone wrote. It falls out of what the system counts.** The books record matter and energy. **Money is neither.** A banknote moving from one hand to another is not a physical event the ledger has any way to notice, so it simply is not there. Not hidden, not ignored on purpose — **invisible, in the way a colour is invisible to a set of scales.**

**Two things worth knowing, because they are the ones people assume must be false.**

**Money cannot buy standing here. At all.** Suppose someone wealthy pays a hundred people to make things and sells them into the system. **The hundred workers earn the hours, because credit is a record of who actually did the work.** The person who paid did none of it, so they earn nothing. **You cannot buy someone else's hours, at any price**, and nobody's day has more than 24 of them.

**And buying cheap inside to sell dear outside wrecks the person doing it.** Everything you take on from inside adds to what you owe. Selling it outside never takes that off you. Meanwhile the only thing that grows your side of the ledger is the hours you personally work. **So the account of anyone milking the system gets worse with every load they pull out, until it stops them buying anything more.** No one has to catch them. **The books just stop lending them rope.**

**And on what Aequitas deliberately does *not* do:** it does not propose abolishing municipal government, planning departments, courts, or the civil service. Those institutions largely work. **The target is oligarchic capture, not administration.** Only the economic nature of these institutions changes — they stop being funded by extraction and start being credited for the work they do.

---

<!-- tag: ovw-s10 -->
## 10 — What we haven't solved

A proposal that admits nothing is a proposal nobody should trust. The live problems, in order of how much they matter:

- **Splitting *blame* within a team** *(the credit half is now settled)*. Crediting a team turned out to be a non-problem: everyone is simply credited **their own hours** — nobody needs to say "the welder caused 40% of the bridge," because credit was never a share of the output. What's genuinely left is narrower: when a team *jointly causes* a harm (a shared spill, damage found years later), splitting *that* debt among them is still a convention we choose rather than a fact we measure. Small, and honestly labelled.
- **Who controls the cost model.** Whoever sets what a tonne of carbon "costs" influences every ledger in history without touching a single rule. Several defences are in place; the general problem is not closed.
- **Understatement drift.** Errors that make something look *more* costly get corrected by everyone affected. Errors that make it look *less* costly benefit everyone affected, and nobody funds the correction. Rival-sector auditing is the proposed answer and it is unproven — and it now has more to guard, since the "how much pollution can the world absorb on its own" line is one of the most powerful settings in the whole system and everyone benefits from it being drawn too generously.
- **Dumping.** Owning the end of a thing's life (§4) is priced correctly for anyone who plays by the rules — but someone could still fly-tip a worthless object to escape its disposal cost. Catching that is the same kind of problem as any other false record, and is left to the verification layer rather than solved here.
- **Unpleasant work.** Exertion, danger, and skill all resolve into material costs. **Tedium and indignity leave no physical trace**, and nothing currently makes anyone do the boring, necessary jobs. The leading idea is shorter hour-ceilings for such work rather than a higher rate — paying the premium in *time off*, not in a multiplier.
- **Turning contribution into influence.** How much say people get, and how it accrues, is unsettled. The leading candidate is that everyone accrues the same influence per hour worked — not a voting scheme, and deliberately not one. One nice consequence already falls out: because staying alive earns credit, *everyone* gets a baseline say in what the world makes next simply for being alive, and since that baseline is equal for all, it would cap the say-gap the same way it caps the wealth-gap — and subject to the same caveats (§1): only if fake hours can be prevented and baselines stay sane. What's still open is exactly that — stopping people from *manufacturing* fake hours to buy extra say — and how generous each community sets that "cost of staying alive" baseline, which quietly sets where the inequality cap lands.
- **Feedback mechanics.** How appreciation aggregates without turning into a popularity contest, and whether it can be bought. If it can be bought, it is a currency by the back door.

**Some of these will change the theory. That's the point of writing them down.**

---

<!-- tag: ovw-appendix-a-where-this-came -->
## Appendix A — Where this came from

Aequitas is the successor to the **Open Fair Credit Standard (OFCS)**. What carries over:

- **It is a standard, not a product.** A set of requirements that many implementations can satisfy, not one piece of software.
- **Three tests any such system must pass:** it must work **universally** (no special cases for professions, nations, or classes), it must be **independently verifiable** (no trusted authority anywhere), and it must be **self-sustaining** (it should encourage its own growth and pay for its own upkeep).
- **A universal yardstick.** Whatever the system measures in must mean the same thing everywhere — seconds, joules, grams.
- **Currency vs. credit.** Currency carries almost no information, belongs to nobody in particular, fluctuates, depends on an issuer, and stands for something redeemable. **Credit is only information**, belongs irrevocably to one person, does not fluctuate, needs no issuer, and *is* its own content.
- **Full-cost accounting** across a whole life-cycle: making and moving it, using it, and disposing of it.
- **The free market is not capitalism.** A free market means you decide what to do with the value of your own labour. Capitalism means private ownership of capital goods, which tends to aggregate into hierarchies — and a hierarchy is the opposite of a free market.

What was deliberately dropped:

- **The word "syndicate."** Say business, institution, or co-op.
- **Growing like a local currency.** The historical record on that approach is unambiguous and it is in §9.
- **Loose self-regulation by participants.** Replaced by fixed axioms with local variation competing openly.

---

*For the rigorous statement of everything above, with the arguments and the open problems in full: `00-strategy/Aequitas_Foundations_v0.22.md`.*

*End of v0.16.*
