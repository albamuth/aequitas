<!-- tag: ovw-aequitas-overview -->
# Aequitas — Overview

> **Version:** 0.30
> **Date:** 2026-09-19
> **Audience:** everyone. No economics background assumed, none required.
> **Rigorous version:** `00-strategy/Aequitas_Foundations.md`. This document is the plain-language companion; where they differ, the Foundations govern.

*Aequitas* (genitive *aequitatis*) is the Latin word for fairness, evenness, symmetry — the quality of things being level with one another.

---

<!-- tag: ovw-toc -->
## Contents

**The document has two parts.** Part I explains the accounting and what follows from it. Part II answers the questions readers ask once they have it.

- [0 — What this is, in one page](#0--what-this-is-in-one-page)
  - [And who actually does this?](#and-who-actually-does-this)

**Part I — Five problems, and what the accounting does to each**

- [1 — Problem: Inequality](#1--problem-inequality)
  - [Solution: Debit](#solution-debit)
  - [How far apart can two people get?](#how-far-apart-can-two-people-get)
- [2 — Problem: Debt](#2--problem-debt)
  - [Solution: Credit](#solution-credit)
  - [But what counts as work at all?](#but-what-counts-as-work-at-all)
- [3 — Problem: Gambling and Rent](#3--problem-gambling-and-rent)
  - [Solution: Non-fungibility](#solution-non-fungibility)
- [4 — Problem: Externalities](#4--problem-externalities)
  - [Solution: There is no outside](#solution-there-is-no-outside)
  - [You own the end of a thing's life, too](#you-own-the-end-of-a-things-life-too)
  - [And you don't own the land — you owe for occupying it](#and-you-dont-own-the-land--you-owe-for-occupying-it)
- [5 — Problem: Intellectual Property](#5--problem-intellectual-property)
  - [Solution: front-loaded creation, and meme tracing](#solution-front-loaded-creation-and-meme-tracing)

**Part II — The questions readers ask**

- [6 — Who decides what gets made?](#6--who-decides-what-gets-made)
  - ["But a price already tells you what people want"](#but-a-price-already-tells-you-what-people-want)
  - [When does the work actually count?](#when-does-the-work-actually-count)
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

**It is also not a piece of software.** These documents do not specify one, and they never will. What database to use, what a record looks like on disk, which cryptography to pick, how to keep it private — **all of that belongs to whoever builds it**, the same way banks, not capitalism, decide what a banking system runs on. What this project owes a builder is a different thing: **a list of what must be true** for the books to be Aequitas at all. What must be true is here. How to build it is theirs.

Here is the whole idea:

> **Everything anyone makes, uses, or throws away is matter and energy moving through the world. That movement can be recorded. Once it is recorded honestly, most of what we find unjust about the economy stops being possible.**

Money is very good at one job, letting strangers trade. It is very bad at another: telling the truth about what things take. A price tells you what someone was willing to accept. It does not tell you how many hours of human life went into the thing, how much fresh water it drank, or what it will cost to clean up afterward. Those numbers exist. They are simply not written down anywhere.

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

**Think of them as laboratories rather than banks.** Their business is getting the numbers right, and they publish how they got them so that other networks can find their mistakes. **A network that lets fraud through is helped by a rival network sharing the method that catches it** — not out of goodwill, but because two networks often draw on the same outside evidence, so a bad method in one corrupts the books of the other. **Networks share methods and evidence. They never trade with each other, and one network's books are never added to another's.**

**This matters for reading the rest of the document.** When a later section says the books catch an under-declared emission, or that an estimate improves as better data arrives, or that a purchase is refused because someone is over their limit — **a trust network is the thing doing it.** Aequitas says what should be counted. Trust networks are where the counting happens, or fails to.

**Trust networks are not prescribed by this project either.** How a network handles privacy, what technology it runs on, which laws it must satisfy, how it documents its own founding — all of that is theirs to decide. **They compete on one thing only: how close to the truth they can get.** A network people cannot check is a network people will not use.

> **One thing to clear up, because readers keep getting it wrong.** **A trust network has no set size.** It can cover a valley, a trade, a country, several continents, or the world. **Nothing here says networks are small or that they match a town or a region.**
>
> Aequitas does say that no single body may own the rules, and that different networks may run different settings and must publish them. **That is about not having a boss. It is not about being small.** Networks that work together are expected to keep merging over time.
>
> **But be careful with the fairness limit above. It describes one network's own books, and nothing wider.** Books are never added together, and a purchase is checked against one network's books only — the one the seller accepts. **So the limit is not a statement about everything a person can reach in the world.**
>
> **Here is the case that shows why, with the numbers.** One person works 8 hours on a Monday. Network A counts 4 hours a day as the work of staying alive, so it records **12** credited hours. Network B counts 10, so it records **18**. Both figures are right, because each network read the same two facts through its own settings: eight hours worked, one human alive. **Add them and you get 30 hours in a 24-hour day, which the system forbids. Nobody adds them.** No network holds that sum and no purchase is ever checked against it.
>
> **And you cannot add the two figures to work out what the person can "really" reach.** It is tempting and it is not allowed, because an hour in Network A's books and an hour in Network B's books are not the same unit. A debit is a bundle of physical quantities: kilograms, energy, hours, land. It becomes a single number only when a network squashes that bundle down using its own weighting. A and B weigh things differently, so the same basket of goods comes out as a different number in each. Adding them would set one A-hour equal to one B-hour, which is an exchange rate. **An exchange rate between two sets of books is a currency, which is the one thing this system does not have** (§3, and Foundations A3).
>
> **Nor did anyone break the 24-hour rule.** Network A's account holds 12 hours. Network B's holds 18. **Each is under 24, and the rule applies to each account on its own.** There is no account anywhere holding 30.
>
> **What is left is an ordinary thing.** If the person buys something through Network B, Network A cannot see it. A network already publishes how much of its area it actually measured, and it estimates what a subscriber leaves undisclosed in a way that counts against them, so leaving activity dark gets steadily worse for you (Foundations §4.4, and §4.2 on why two networks' figures are compared and never converted). **What nobody has measured is whether that is tight enough against somebody splitting on purpose.** This project says so rather than assuming it.
>
> **Where this document does talk about something local, it means a physical thing being handed to a physical person somewhere** — the queue at a butcher's counter, or a village with one power station. **That is a fact about the object, not about the network.**

*The detail is in `00-strategy/papers/C2_TrustNetworks.md`.*

---

# Part I — Five problems, and what the accounting does to each

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

Now look at the sandwich. Wheat was grown somewhere, drinking irrigation water and fed with fertiliser that ran off into the water table. It was harvested, with some spilled and some rotted, then milled, baked, assembled, wrapped in plastic, and driven to the shop in a truck burning fuel. A mechanic fixed that truck's leaking oil filter, and the old oil went somewhere. The wrapper is now in a landfill, and will still be shedding microplastics into groundwater in a thousand years. Maybe one day something will clean that up. Today, it is simply out there, unpaid for.

**Every one of those is a real, physical, countable event.** Aequitas records them, and calls the whole bundle the sandwich's **debit**.

Here is the reframe:

> **When you take something, you take on its debit. Possessions are not what you are worth. They are what you owe the world for holding them.**

Two kinds of debit behave differently, and the difference matters:

- **Property debit** is the embodied *material* you are holding, and it is *dischargeable*. You carry a house's material debit while you hold the house; hand it on, and it goes with it. You are not punished for owning, but you cannot pile things up for free either.
- **Consumption and pollution debit** is *permanent*, and it stays with **whoever caused it** — it never travels with the object. You ate the sandwich; that is yours for good. But the fertiliser the farmer let run off stays on the *farmer's* record, and the fuel the trucker burned stays on the *trucker's*. You didn't cause those. They did.

**One thing that trips people up:** a thing you have not used yet, like a can of petrol, hasn't polluted anything, so nobody has caused anything. **It carries what it *will* do, and that travels with the can until somebody burns it** (§4).

**So a thing carries its whole story, but not everyone's debt.** Buying the sandwich, you take on its *material* and the fact that you ate it — not the farmer's pollution and not the trucker's fuel. What you *do* receive is the full record of where it came from, so you can prefer the cleaner loaf before you buy. **The debt sits with whoever caused each harm; only the story travels with the bread.** This turns out to be a stronger arrangement than making the shopper pay for the farm's runoff — more on why in §4.

![The debit taxonomy at a glance. A debit splits into property debit and consumption or pollution debit. Property debit has three parts: the material you hold, which travels with the thing; the making-hours, which stay partly with you even after you pass it on; and latent pollution, which is what the thing will emit when used, and which rides the object until somebody uses it. Consumption and pollution debit is permanent and sits on whoever caused it. Two rules cut across everything: working on your own things nets to zero, and cost never passes to someone who did not cause it.](../01-wiki/assets/debit-taxonomy.svg)

*The whole taxonomy on one page. It shows a little more than this section does: the "making" hours of a thing stay partly with you even after you pass it on, which §2 comes back to. The big ideas are all here — what travels, what stays, what waits until you use it, and who is on the hook.*

Suppose you spend a weekend repairing your own roof. You earn credit for the hours, because that is real work really done. But the repair also raises the house's debit by exactly those hours, and you are holding the house. **Net effect on you: zero**, apart from the materials you actually consumed.

That identity is the whole of §7 in one line. **Property cannot be an engine, because working on your own property never gets you ahead.** Nobody has to ban landlords. There is simply nothing there to earn.

**Nobody starves for having a low score.** Everyone earns a baseline just by staying alive (§2), which is the real, counted work of maintaining a human, so there is always something behind your basic needs. On top of that, a network sets one **debit tolerance**, written `ρ` and said "rho", then publishes it. Going past it restricts *luxuries*, never necessities. A nurse is credited for nursing you whatever your books look like.

**This is not charity bolted onto the system, and it is not something an implementation automatically has either.** Whether essentials are genuinely affordable in a given community depends on how generous that community's baseline is, on the value it sets for `ρ`, and on what its economy can physically deliver. **It is a result a community has to reach, not a box a builder ticks.** The reason to reach it is plain: a system where being mis-measured can starve you is a system nobody should adopt.

*The next question is how far apart two people can end up. It has a precise answer, and a precise scope.*

<!-- tag: ovw-s1-disparity -->
### How far apart can two people get?

**Read the scope before the number, because the number is easy to take for more than it is.**

> **What follows is a ceiling on the credit one person can earn by working, and therefore on the influence that credit buys.** Credit is what a pledge is backed by, so a ceiling on credit is a ceiling on how much anyone can put behind the things they want made next.
>
> **It is not a ceiling on what anyone may consume, and there is no ceiling on that.** What you may hold and use depends on your own credit **plus every hour other people have pledged to you**, and **nothing caps how many people pledge to you.** So somebody widely admired can consume far past the figure below. This system does not prevent it.

**The two things move differently, and that is the whole of the scope.**

| | Can it be capped? | What sets it |
|---|---|---|
| **Credit you earn, and so the say it buys** | **Yes, at `24 ÷ F`** | Your own hours. A day has 24 of them and you cannot buy anyone else's |
| **Room to consume** | **No** | Your own credit **plus** hours pledged to you by others, which nothing limits |

**In plain words: working harder than everybody else has a hard ceiling. Being backed by a lot of people does not.** The end of this section says why the second is still a different thing from being rich today.

**With that said, here is why the gap in who gets a say is capped in a way money's is not.** The engine is arithmetic rather than any rule. Money can be piled up without limit. Time cannot. Everyone gets the same 24 hours a day, you cannot buy anyone else's, and credit is a record of *your* time, so it never moves. **How much you can put behind the things you want made is exactly the credit you earned, and no more.**

So the most anyone can out-say anyone else is the ratio between a full day and the baseline everyone already gets for living. Write the baseline `F`, in hours a day.

> **The ceiling is `24 ÷ F`.** That is the whole result. **It is not a single number, because `F` is a community's own choice** — each community sets its baseline and publishes it, and the ceiling moves with it.

**What `24 ÷ F` comes to at three published baselines.**

| The community's baseline `F` | The ceiling, `24 ÷ F` |
|---|--:|
| 2 hours a day — counts only what a body cannot avoid | **12.0 ×** |
| 8 hours a day — counts sleep alone | **3.0 ×** |
| **10 hours a day — 8 sleep, 1 eating, 0.5 washing, 0.5 other upkeep** | **2.4 ×** |

**In plain words: quote the formula, not the number.** The rest of this section works through `F` = 10 because that baseline has published sleep evidence behind it, so its ceiling is 2.4. **A community with a 2-hour baseline has stated a 12-times ceiling, and it is conforming.** Today the top of the money scale runs into the millions of times the bottom, at any baseline.

> **`24 ÷ F` is a wall, not an outcome. Nobody reaches it, and real lives show why.**
>
> Reaching it needs 24 credited hours every single day, birth to death, for eighty years. Here are four whole lives in a community with a 10-hour baseline, where the wall stands at 2.4:
>
> | | Lifetime credit | Against a life spent only staying alive |
> |---|---|---|
> | Only stays alive — 10 h/day for 80 years | 292,000 h | **1.00×** |
> | **A very hard working life** — 12 h of work a day, 300 days a year, ages 20 to 70 | 472,000 h | **1.62×** |
> | The arithmetic maximum, with childhood uncredited | 608,820 h | 2.09× |
> | The arithmetic maximum | 700,800 h | **2.40×** |
>
> **The figure to quote for a real life is about 1.6 times.** A very hard working life reaches 1.6 times a life spent only staying alive. **The wall at this baseline is 2.4, and nobody gets to it.**

**Five conditions, because this is the theory's single biggest claim and it would be easy to overstate.**

| The condition | What it does to the number |
|---|---|
| **How generous the community sets the baseline** | The ceiling **is** `24 ÷ F`, so this is not a condition on the result so much as the result itself. A 2-hour baseline states a 12-times ceiling. The bound is only as tight as baselines are generous (§10). |
| **Whether the community credits a child's learning time** | Credit it and `24 ÷ F` is reachable. Credit none of it and nobody can reach the published ceiling. **At a 10-hour baseline over an 80-year life the most anyone reaches is 2.09 against a stated 2.4.** That shortfall is not a fixed fraction — it moves with the baseline and with how long the person lives. |
| **That nobody manufactures fake hours** | The wall holds by arithmetic for honest and dishonest accounts alike. But people trading fake hand-offs between them could still inflate the totals, and controlling that is a separate open problem. |
| **That it is one network's books** | Not a statement about anything wider, and there is no wider figure to give. Two networks' numbers are read through different weightings, so they cannot be added or compared. See the box in §0. |
| **That room you receive never enlarges what you can pledge** | Your pledge budget is credit *you* earned, and nothing else. **If hours pledged to you also raised what you could pledge onward, the wall would have no top at all** — people could back you on the strength of backing you already had. |

**In plain words: the first four say what the number depends on. The fifth says what would destroy it.**

**Why the fifth one matters, with the numbers.** Take somebody with 146,000 hours of credit and 30,000 hours of room pledged to them by others.

| | Hours |
|---|--:|
| Credit they earned | 146,000 |
| Room others pledged to them | 30,000 |
| **What they may pledge onward** | **146,000 — the earned figure only** |
| What it would be if received room counted | 176,000, and then more, with no top |

**So the rule is that received room grants consumption and grants no say.** Break it and the bound fails the same way the consumption claim did.

> **And one thing the wall is not.**
>
> **The wall does not move when people cheat. That sounds like a security feature, and half of it is.** No amount of faked hours produces somebody beyond 2.4 times, because a day still has 24 hours in it.
>
> **The other half is the same fact seen from the other side: the wall cannot tell you that anybody cheated.** The sum `24 ÷ 10` never looks at a single account, so it answers 2.4 whether the books are honest, half invented, or entirely invented. Add a completely made-up person and the answer is still 2.4, because the sum never looked rather than because anything caught them.
>
> **So it is a limit on what cheating is worth, and it is not a way of finding cheating.** Finding it is a different job, done by a different tool: measure the world from outside and compare (§7). *(This was pointed out to us from outside, and we agreed. We had been publishing the first half without the second.)*

**One thing genuinely unsolved sits underneath all five:** confirming that someone's hours are real without prying open their whole private record (§8). **So the honest version is that inside one network's books, with sane baselines and that verification problem solved, the gap in who gets a say is capped in a way money never is.** That is a conditional result rather than a theorem, and it is stated as one.

#### Does a workable baseline actually exist?

**Condition 1 above invites a fair worry: if the community picks the baseline, can it pick a value that does not work?** A baseline set too low leaves people unable to afford what they need. Set too high, the books stop rationing anything that is genuinely short.

**This was measured rather than argued.** A run in 2026 swept baselines from 1 to 14 hours a day against the tolerance `ρ`, checking both ends at once.

| The baseline `F` | The largest essentials basket that baseline can carry | Against one whole median American lifestyle |
|---|--:|--:|
| **2 hours a day** — the tightest tested | 2,701 h/yr | **1.96 ×** |
| 10 hours a day | 4,380 h/yr | 3.17 × |
| 14 hours a day | 4,599 h/yr | 3.33 × |

**In plain words: even the tightest baseline tested carries an essentials basket costing nearly twice a whole median American lifestyle.** Essentials are a part of that lifestyle, not double it, so **no baseline in that range fails on affordability.** What binds instead is what the economy can physically produce.

**Two limits on that result, stated rather than buried.** The run used published tolerance figures **with no pledging in them**, and pledges can double a community's room, which halves the usable top end. **And at a 1-hour baseline with essentials at 70% of a median lifestyle, the band does close** — the first swept case where it ever has.

### And what is not capped: what a person consumes

People can put their own earned hours behind someone else, which is a pledge (§6), and that gives the receiver room to hold and use more. **Nothing limits how many people back one person.** So somebody widely admired can live well beyond the wall above.

**Why that is a different thing from being rich today.** That room cannot be lent at interest, rented out, charged for, or used to hire anybody. You can hold things and use things. **You cannot turn it into a machine that earns while you sleep**, which is what property does now. And it cannot be conjured: every hour of it is an hour somebody really lived, and nobody has more than 24 in a day.

**One more thing is true before any of that.** Aequitas only ever counts *material* things: what you physically hold, use, and consume. It never counts money-wealth. A share of stock, a bond or a crypto-token is a claim on paper rather than matter or energy, so it simply does not appear. The factory those shares represent *is* counted, but on the people who actually run it, not on the distant shareholder.

**That one fact does something striking on its own, and it has been measured against real distributions.**

| | Top of the scale, against the median |
|---|--:|
| **Money wealth** | about **1,000,000 ×** |
| **Material consumption** — houses, jets, yachts, what is physically used | about **670 ×** |

**In plain words: strip away the paper and the real gap is about a thousand times smaller than the money gap makes it look.** The reason is not a rule. Consuming physically takes time, and nobody has more than 24 hours in a day.

**Running the gate against real US and world wealth data found two things.** Between 0.1% and 2% of Americans would sit past a permanent limit on non-essentials, depending on the tolerance a network sets, and around 0.5% at a tolerance of 1.5. These are the genuine mega-consumers rather than the merely rich, and selling their property does not save them, because what you have already consumed stays consumed. Meanwhile **about two thirds of people sit below their group's average and would gain room by joining.**

**That locked figure is an upper bound and is not final.** The run assumed nobody had been pledged to. Somebody with room behind them is limited later, or not at all, and the figure has not been recomputed with a pledge term in it. The inequality we live under is, to a startling degree, an artefact of counting paper.

### Is there enough human work to go round?

**The honest answer is that it depends entirely on how wastefully things are made, and this project got it wrong once before getting it right.**

**First, the measured cost of an ordinary life.** Add up everything a typical American consumes in a year: food, housing, healthcare, everything they buy, and the share of things made abroad. It comes to about **1,380 hours of other people's work.**

> **One comparison is tempting here and must not be made.** Do not set 1,380 against the roughly 3,650 hours of credit a person earns each year just by staying alive, and call the difference spare capacity. **That sum cannot fail, so it is not evidence.** The bottom number is the community's baseline multiplied by 365, and the community picks the baseline. At a 10-hour baseline the comparison looks comfortable; at a 2-hour baseline the same real economy looks short. **Sleeping is credited work, and it cannot lay cable.** *(This was our own error. An outside critic found it and we withdrew it.)*

**The test that can fail asks about *deployable* hours**, meaning the people of working age, the share of them who work, and the hours each one works. It sets those against the 1,380 that a median lifestyle actually commands.

| Production method | Deployable hours ÷ hours needed | Does it close? |
|---|---|---|
| **United States** | **0.43 – 0.87** | **No, at no corner of the range** |
| Peer countries, at about two thirds of US labour | 0.66 – 1.34 | **Yes, in about a third of cases** |

**In plain words: at the American way of producing things the hours do not close, and the best case assumes full-time work from 85% of every working-age adult.** At the German, Swedish or Japanese way they do. The same result shows up at world scale: a US-efficiency median standard for 8.1 billion people needs about **10.4 trillion labour-hours a year against about 6.5 trillion available**, which is a shortfall no workweek anyone would accept can cover.

**So the claim is not that labour is never the constraint.** It is that **the constraint is production efficiency**, and at the wasteful method the hours are genuinely short.

**What the same measurement shows about method.** The United States uses 50–80% more human labour and 2.5–4 times the carbon per person than Germany, Sweden, France, Japan or Spain, countries that deliver a comparable material life and longer lifespans for far less. Sprawl, fossil fuels and long tangled supply chains are the difference.

| The method supplying you | Hours of other people's work a year |
|---|--:|
| American | **1,380** |
| German or Japanese | **883** |
| Spanish | **759** |

**In plain words: two people can live the same material life and carry very different debit, because one of them is supplied by a wasteful chain.** Under Aequitas the efficient way is automatically the cheaper way, because the pollution, the extra hauling and the bloated overhead all show up as real costs in the books. **The accounting pulls toward the efficient method with nobody enforcing anything and nothing forbidden.** Abundance comes from producing smarter, not from working more.

---

<!-- tag: ovw-s2 -->
## 2 — Problem: Debt

*The world economy now needs ever-growing debt just to stand still.*

Total debt in the United States ran at about 140% of GDP from 1960 to 1980. It is now roughly 300%, and the same curve shows up globally. Not even the 2008 crash bent the line, and that crash was itself caused by too much borrowing.

An economy that needs a constant supply of *new* debt to generate demand is an economy permanently one disruption away from a seizure. That is what happened in 2008 with household debt, and the response was to shift the load onto government debt instead. The trick works while borrowing costs stay below growth. It is not a solution; it is a longer fuse.

<!-- tag: ovw-solution-credit -->
### Solution: Credit

*Work is recorded in time. And the record can never move.*

**A credit is a record that a specific person spent a specific hour doing something.** It is not a claim on anyone. Nobody owes it to you. It is simply a true statement about the past, and true statements about the past do not change owners.

> **And "work" means time *spent*, not effort.** This is the one mental shift Aequitas asks of you. Credit counts the hours of your life you put in, not how hard you strained.
>
> Two people who spend an hour on the same task are credited the same. It does not matter that one breezed through it and the other found it gruelling. A real difference in effort shows up as a material cost instead: the harder worker eats more, and a dangerous job's harm is charged back to the work that caused it. It is never a bigger number for the same hour.
>
> Once you see credit as time spent, something surprising follows: **looking after yourself is work.** Sleeping, eating, resting and keeping yourself going is time spent maintaining a living human. So is looking after a child, and history refused to count that only because nobody was paid for it. So everyone earns a baseline simply by staying alive. That baseline is not a hand-out bolted onto the system. It is the real work of being alive, finally counted, and it is where the floor under everyone (§1) comes from.

#### The one test that decides what you may take

**Everything else in this document about limits is this one rule applied again.**

> **Your ledger is three numbers, and none of them ever goes down.**
>
> **`C`, your credit** — the hours the books recorded as your work.
> **`D`, your debit** — what everything you have consumed is currently reckoned to have taken from the world.
> **`P`, your room** — hours other people have pledged to you by name (§6).

**When you buy something, one test runs.** Is `D` still no more than `ρ` times `C` plus `P`?

> **`D ≤ ρ · (C + P)`**

**`ρ` is the debit tolerance**, a single multiplier the community sets and publishes. **At `ρ` = 1.2 you may carry debit up to 1.2 times your credit plus your pledged room.**

##### Worked, with three people at age 40

A community with a 10-hour baseline and `ρ` = 1.2. A median lifestyle costs 1,380 hours a year, and staying alive earns 3,650.

| | Credit `C` | Room `P` | Debit `D` | Room left |
|---|--:|--:|--:|--:|
| **A — stays alive, works 1,000 h a year** | 186,000 h | 0 | 55,200 h | **168,000 h** |
| **B — stays alive, works nothing, consumes the same** | 146,000 h | 0 | 55,200 h | **120,000 h** |
| **C — like B, but 300 people pledged 100 h each to them** | 146,000 h | 30,000 h | 55,200 h | **156,000 h** |

**In plain words: nobody's numbers ever went down.** A's extra work did not cancel A's consumption — it widened the gap between two figures that only grow. **C's credit did not move either.** Three hundred people spent their own lifetime pledge budgets, permanently, and got nothing back.

**Four things later in this document are this one test.** The barn that needs 16,700 hours behind it (§3). The luxuries that stop when you go past your limit (§1). The much-backed person who consumes past the wall (§1). The extractor whose account shuts them out (§9).

<!-- tag: ovw-what-counts-as-work -->
### But what counts as work at all?

**Something is work if it is at least one of three things.**

| | What it means | An example |
|---|---|---|
| **Production** | Matter or energy is turned into something | Milling wheat into flour |
| **A service** | Something is done for a person, an organisation, or yourself | Setting a broken arm |
| **Enrichment** | Knowledge, skill or culture reaches somebody | Teaching a child to read |

**One is enough, and nobody records which one.** An apprentice plumber's single hour is all three at once — copper becomes plumbing, a customer's pipes work, and a trade gets learned. **It still counts as one hour.** The three names decide *whether* an hour counts, never *how much* it counts for.

**This is why looking after yourself can count, and it is the ordinary rule rather than a special one.** A community writes down what it treats as work. **If it treats sleeping, eating and washing as work, then the hours you spend on them are credited — exactly like any other hours it recognises.** If it does not, they are not. **The list is the community's to write.**

**How is it checked? You are still here.** A living, verified person plainly did the maintaining, and confirming that costs almost nothing.

The medical consensus is that adults need [7 or more hours a night](https://aasm.org/aasm-and-srs-publish-new-sleep-duration-consensus-statement/), and 6 or fewer is not enough to stay healthy and safe. **A community that counts 8 hours of sleep plus roughly 2 hours of eating, washing and other upkeep gets a baseline of 10 hours a day.**

> **Two things this does not mean.** Passing the three-way test is not the same as being credited: a community credits no kind of work it has not written a rule for. And nobody gets extra hours out of it, because **no account may record more than 24 hours of activity in a day.** A person sleeping 8, eating 1, washing 1 and working 8 records **18 hours**, and no reading of the three names makes that number larger.

**The same gate is why some things do not count.** A community cannot decide that being loyal to it is work. **Loyalty is not production, not a service, and not enrichment**, so there is nothing to credit. That is a real limit on what any bookkeeper can invent.

Four things follow.

**1. Everyone's hour counts the same.**

No profession earns at a higher rate. This sounds naïve until you see where the differences actually go:

- **Hard labour** — a labourer eats more. That extra food is recorded as real food-production cost, borne by the work that required it.
- **Dangerous labour** — if a process turns out to damage the people doing it, that harm is charged back to the products that process made. Even decades later.
- **Skilled labour** — and this is the important one.

**Training is work, and it is carried at the time.** A medical student is credited for their hours studying, exactly as a bricklayer is credited for hours laying bricks. The cost of that training is the teachers, the buildings and the equipment. It is carried *during the training years*, cushioned by the people who wanted doctors to exist putting their credit behind it.

Which means: **the doctor's education never appears on any patient's bill.** Your visit costs their time, the clinic's materials, and the medicines you were given. Nothing else. It was already accounted for, up front.

That is a better answer than a pay premium in two ways. It makes becoming a doctor *immediately* worthwhile rather than a decades-long bet. And it puts the cost where the benefit is — everyone benefits from doctors existing, so everyone bears it, rather than charging one unlucky patient in 2044 for a lecture given in 2026.

**This same move solves several problems at once**, and it's worth naming as a rule:

> **A large up-front cost with a spread-out benefit is carried when it happens, cushioned by the people who wanted it. It is never charged on to whoever happens to use the result later.**

Education. Research. Infrastructure. Films. A blockbuster's viewers pay for the *delivery*: the projector, the power, the bandwidth. They never pay for the four years of production. More on this in §5.

**Front-loading is the only thing that lets the books ever close.** Picture charging a hospital's construction to its patients. To do it honestly you would have to fold in the builder's costs, and the cement plant's, and the steel mill's, and the schooling of the engineers who designed the place — back and back, with no end, to the first human who ever built anything. The sum never finishes. Front-loading is what stops the regress: a building's cost is fixed once, up front, and a patient's bill never reaches back past the front door.

**So who carries a building year to year?** The whole cost rides the **building itself**, shared among the people who run it *by how long each has worked there*. A nurse hired on Monday inherits almost none of it, and a thirty-year veteran a little more. **Nobody takes on a whole hospital by walking in the door.** Otherwise that entry cost would scare people away from staffing exactly the places that need it most.

The community's pledges do not erase that cost. They give the staff the *room* to carry it, cushioning the bite. **And a pledge is permanent — it cannot be taken back** (see §6). So the staff can rely on that room and get on with the work. The cost is a one-time expense to whoever pledged, not a loan that can be called in.

**The share you built up stays yours — you can't hand it off by walking away.** The *stuff* of a thing (its material) travels with it when you pass it on. But your share of the *work that made it*, earned by the time you held it, stays on your record. Own a 500,000-hour mansion for ten years and hand it on, and after the next owner has held it as long as you did, roughly half of that making-cost is still on your books. You can't dodge it by giving the thing to someone outside the system either — if there's no record of a hand-off, the record still shows *you* holding it, so you keep the whole weight. The one thing that lightens your load is a *real* new holder taking it on. A useful side effect: **second-hand things start out cheap** for the new owner, who has put in no time yet, and grow heavier the longer they keep them.

**2. Credit cannot move, so nobody can be owed.**

Your credit is a fact about you. It cannot be given, sold, lent, taxed, gambled, or stolen. There is no transfer mechanism, not because transfers are forbidden but because there is nothing coherent to transfer — you cannot hand someone the fact that you worked on Tuesday.

**A debt crisis requires a creditor who must be made whole.** Here there are none. The mechanism that turns a bad year into a spiral simply has no part to attach to.

**3. Your record is two numbers, and they never cancel each other.**

**Your credit is every hour of your life that got counted as work. Your debit is everything your consumption is currently reckoned to have taken from the world.** They sit side by side. **Nothing is subtracted, nothing is spent, and there is no third number.**

**Both only ever go up.** Buying something adds to your debit and takes nothing off your credit, because credit is not a thing you hand over. **So the two are compared as a ratio — is your debit within some multiple of your credit? — never as a balance you could run down to zero.** A ledger here is a way of looking at what one person consumed beside what they did, and that is all it is.

**Neither number is stored anywhere.** Both are worked out fresh from the record of what happened, every time anyone looks. That is why a better measurement can change everybody's figures, backwards (§4).

**4. The books never balance — and they must not.**

Total debit will always exceed total credit, everywhere, permanently. Every real process wastes something; energy dissipates; matter degrades.

**Total debit exceeds total credit because every real process wastes something. A set of books that balanced would be describing something physically impossible.**

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

**That number is narrower than people expect, on purpose.** It carries **what the thing used up**, and nothing else. A farm's barn is not in the beef. A factory's machines are not in what they made.

> **This is the most common objection to Aequitas, so here is the answer with a number in it.**
>
> A barn costs **20,000 hours** to build and shelters cattle for **20 years**, over which the farm sells **40,000 kg** of beef. Split the barn across the beef and you would add **0.5 hours to every kilogram**. Aequitas adds **nothing.**
>
> **The 20,000 hours did not disappear.** They sit on the farmer, for as long as they hold the barn. **At a debit tolerance of 1.2, carrying 20,000 hours of debit needs 20,000 ÷ 1.2 = about 16,700 hours of credit standing behind it** (§2). Against the roughly 3,650 hours a year a person earns from staying alive, that is **4.6 years of one person's entire credit.** That is what stops a barn going up that nobody needs.
>
> **Now do it the other way and watch who pays.** The 20,000 hours come off the one farmer and land on about **40,000 shoppers**, half an hour each. None of them chose to build a barn. **The only person who made the decision is the only person the cost stops bothering.**
>
> **The rule that looks like it is hiding a cost is the rule that keeps the cost pointed at whoever chose it.**

**One honest consequence, and the books say so out loud.** Two farms selling the same beef, one with a big barn and one with a shed, show the **same** number per kilogram. The number tells you what the beef took, not what the farm's whole way of working costs. **What keeps the big barn honest is the farmer's own ledger, not the sticker** — the same way pollution is kept honest by sitting on whoever caused it (§4), rather than by hoping a shopper notices.

**What survives — and it is essential.** Removing profit does not remove competition. Producers still compete, hard, on **quality, craft, and efficiency**: doing the same thing with fewer hours, less material, less waste. That is genuine rivalry with the extraction stripped out, and the system leans on it heavily (see §7).

**Genuine risk survives too.** Building something nobody wants still burns real hours and real material. Enterprise remains a gamble in the honest sense. What disappears is the other kind — the sort where you win by holding an asset while someone else works.

---

<!-- tag: ovw-s4 -->
## 4 — Problem: Externalities

*The costs that nobody pays are the costs that get made.*

An externality is a cost you cause and someone else absorbs: the smoke, the runoff, the depleted aquifer, the worker's ruined back, the wrapper in the ocean. Every economy in history has had them, because they are not a mistake — **they are a competitive advantage.** The producer who dumps outsells the one who cleans up.

**It is worth saying plainly why this is worth fixing, because the rest of this section is machinery.** The person breathing the smoke did not choose the smoke. The family drinking from the aquifer did not choose to have it drained. **A harm you did not cause and cannot avoid is a limit on your life that somebody else put there.** That is what an externality is underneath the economics: one person's choice quietly narrowing another person's options.

> **That is the reason. It is not a rule, and the difference matters.** Nothing in Aequitas orders anybody to clean anything up. There is no authority to give such an order, and no way to measure whether a life has been un-narrowed. **What the system does instead is make cleaning up worth doing.** A pollutant's cost is the work of removing it. Remove some, and the record of everyone who ever emitted it gets lighter — which is the rest of this section. **The reason is moral; the mechanism is arithmetic.** Keeping those two apart is what lets the system work without anybody in charge.

<!-- tag: ovw-solution-there-is-no-outside -->
### Solution: There is no outside

Under Aequitas, **every consequence is recorded against whoever caused it.** Not because a regulator noticed, but because that is what the accounting is: the pollution is a material flow, and material flows are what the ledger records.

Three consequences follow immediately.

**Harmful production penalises the producer, directly.** A factory that pollutes carries the cost of cleaning it up — permanently, on its own record, whether or not any customer ever notices. Exploitative labour carries the cost of the harm it does, borne by whoever imposed it. This is stronger than the usual hope that shoppers will choose the greener product (they mostly don't): the polluter is out of pocket at the source. And because every product still carries its origin record, a buyer who *does* care can see the difference and steer toward the cleaner maker on top of that. **The incentive gradient reverses, with nobody enforcing anything, and it does not wait on anyone noticing.**

**Pollution from *making* a thing stays with the maker. Pollution from *using* it is yours.** That is the whole rule, and it settles cases that look hard.

- The miner keeps the mine's pollution. Buying the ring doesn't move it to you.
- The refinery keeps the refinery's. Buying the petrol doesn't move that to you either.
- **But burning the petrol is you.** The CO₂ from the tailpipe is the driver's, not the carmaker's.

**The thing you bought carries what it *will* do when you use it.** Buy 40 litres of petrol and your record gains **40 litres** — stored as litres, not as a number of hours. Whenever anyone looks at your record, those litres are converted using today's best figure for what cleaning up that carbon takes. **Find a cheaper way to capture carbon and the same 40 litres weighs less, backwards, for everyone.** And if you sell the fuel to somebody else, it goes with the fuel.

**Your electricity is different, and it is the same rule: you never held the fuel.** The power company bought the gas, kept it, and burned it, so the emissions are the company's, shared out among the people who work there by the hours each worked. Your electricity bill in this system is labour — how many engineer-hours per kilowatt-hour delivered, how many driver-hours brought the coal in. That is a very small number, and the company's emissions are a very large one.

A power company today puts the cost of its smoke onto everybody else. **Here it cannot, so it carries it.** That makes a coal plant almost impossible to staff and a wind farm easy. Nobody has to ban anything.

> **One thing you lose, and we will not pretend otherwise.** Shifting your washing to 2am no longer makes your own record lighter. **The reason to clean the grid now sits entirely with the company and with the people who pledge for clean generation**, rather than partly with you.

> **Note what that rules out. No emission is decided by which supplier anyone signed a contract with.** A contract is a piece of paper, and this system never lets paper decide a physical record. **A record of CO₂ has to come from a measurement of CO₂.**

**Regulators become something businesses want.** An environmental agency's job stops being punishment and becomes advice: *here is how to lower your debit.* Every hour they save you is an hour off your product's cost. Enforcement quietly turns into consulting.

**Taxation becomes unnecessary.** Civil servants are credited directly for the work they do — there is no salary that needs funding first. People who use a road carry a share of its debit by using it. There is nothing left to collect, and therefore nothing to argue about collecting.

<!-- tag: ovw-two-things-this-requires-and -->
### Two things this requires, and both are features

**Costs discovered later are applied backwards.** When science improves, say with a cheaper way to capture carbon or a newly proven occupational harm, **every affected record in history recalculates.** Your ledger is not a stored number; it is recomputed from the log of what actually happened, using today's best understanding of what those events cost.

This means **the system permanently pays for better measurement of reality**, forever, which is an unusual thing for an institution to do. It also means **no error is permanent**: an early estimate that turns out wrong is corrected the moment somebody does the science, and the correction reaches all the way back.

**A pollutant's cost rises and falls with how much of it is already out there.** A substance only counts as pollution once there is more of it than the world clears on its own — steel that rusts away as fast as it is made, or carbon the planet reabsorbs at the rate we emit it, is just part of the cycle and costs nothing. Above that line, the more of it in the air or the ground, the more work it takes to deal with, so **every record of it grows heavier together.** The flip side is the good part: when the world cleans some up, *everyone's* past share of it gets lighter, backwards through history. **Cleaning up the commons pays back the people who fund it** — which is, for once, a reason to fund it.

**When one process makes several things, the cost is not divided at all.** A steer yields beef, hide, tallow, bone, manure and methane from one pool of feed and effort. For a century people tried to split such costs by *choosing a rule*: by weight, by energy, by price. Every rule that worked in one industry was nonsense in the next.

**Aequitas doesn't choose, because it doesn't split.** The feed and the effort were not spent partly on the beef and partly on the hide. **Take the hide away and raising the animal costs exactly the same.** So each thing that comes out carries the whole cost of raising the animal, measured against how much of that thing there is. **There is no rule to pick and nothing left to argue about.**

**A quick example.** Say the animal took 8 hours of work, and yields 250 kg of beef and 40 kg of hide. **The beef carries 8 ÷ 250, about 0.03 hours a kilo. The hide carries 8 ÷ 40, about 0.20 hours a kilo.** Both point at the same 8 hours — and if one person bought both, they'd carry 8 hours, not 16. **The record is one record, however many things point at it.**

**Two fair questions, answered.** *Doesn't that make the small output look expensive?* Yes — there's less of it, and the same whole animal stands behind it. **What never moves the number is what anyone wants**: a hide's cost does not go up because leather came into fashion. *And doesn't it double the books?* No. Both figures name the same 8 hours, and naming a thing twice does not make two of it.

**One more good property.** If a butcher can show *when* each thing left, and the hide comes off early while the steak goes through everything, **then the hide stops being charged for the work done after it left.** Better records make things cheaper, never dearer. **So there's nothing to police: a producer who wants a lower figure has to measure more carefully, which is exactly what you'd want them to do.**

**The barn is nobody's share of the hide.** The buildings, the tools and the machinery are the *capital* a business runs on, and they never get sliced up and dribbled into each product either. They are handled the same way a hospital is (§2): carried by the people who run the place, cushioned by pledges made up front. A wafer is not charged a fraction of the factory that made it. This closes a question that quietly defeats ordinary cost accounting. *How much of the fab belongs in one chip?* None of it. The fab belongs to the people who run the fab.

<!-- tag: ovw-you-own-the-end-of -->
### You own the end of a thing's life, too

Most accounting stops when a product is sold. Aequitas doesn't. A thing that has stopped being useful and is sitting in a landfill **is** pollution for as long as it sits there, and that debit rests on whoever last held it — as though they had eaten it. Nobody can dump a worn-out machine on a recycler who doesn't want it; if no one will take it, its last owner has effectively consumed it.

Three ordinary incentives fall out, none of them asking anyone to be virtuous:

- **Buy things that last.** A cheap, unrepairable gadget whose disposal cost you'll be holding is no longer the cheap option.
- **Look after what you have.** A hospital is better off maintaining its equipment than running it to death and replacing it.
- **Fund the clean-up.** Recycling and remediation *lighten your own record*, because the pollution they remove is pollution you were carrying.

Recycling genuinely pays. Recycled material never carried the mine's pollution in the first place, because that stayed with the miner, and reusing it means nobody has to dig up more. **The recycler is credited for the work of making the world's junk useful again.**

<!-- tag: ovw-and-you-don-t-own -->
### And you don't own the land — you owe for occupying it

Here is a consequence that sounds radical and turns out to be simple bookkeeping. **Land can't be owned.** A building doesn't sit on property you hold a deed to; it occupies a patch of the Earth — and occupying it is itself a debt. **Every building carries the cost of putting its patch back the way nature had it:** clearing the contamination, pulling out the foundation and the buried pipes, filling the hole, letting the wildlife return. That debt only clears when the restoring is actually done.

Two things fall out, and both are fair. **You are only on the hook for what you did.** A house built two centuries ago on unrecorded or forced labour does not put that old harm on today's occupant, who carries only what they themselves caused while living there, such as the gas stove's emissions.

**What a plot "was like naturally" is a genuinely hard line to draw** for somewhere that has been a city for centuries. It is the same kind of judgement call as deciding how much of a pollutant the world can absorb on its own, and it is handled the same careful way. **Both are listed as unfinished in §10.**

---

<!-- tag: ovw-s5 -->
## 5 — Problem: Intellectual Property

*Ideas are the one thing in the universe that costs nothing to copy. We have built an entire legal apparatus to pretend otherwise.*

Patents and copyright exist for one purpose: to let a holder charge for reproductions. To do that, they must manufacture scarcity in something that is not scarce. The results are familiar: medicines put beyond the reach of the people who need them, research locked behind paywalls, terms lasting decades and outliving the creator, and litigation as a business model.

<!-- tag: ovw-solution-front-loaded-creation-and -->
### Solution: front-loaded creation, and meme tracing

**Most of the machinery simply evaporates.** With no profit in exchange (§3), there is no revenue stream for exclusion to protect. Copyright without a market for copies is a lock on an empty room.

**So who pays for the making?** The people who wanted it, while it is being made. A film's crew are credited for their hours during production, and the debit is settled then, by those who pledged for it (§6). **The audience pays only for delivery** — the theatre's upkeep, the projectionist, the electricity, the bandwidth.

Note what that removes. **A popular film cannot gouge its audience, because there is no mechanism by which it could.** The production's only return is recognition — which converts into enthusiasm and pledges for the next work. The whole incentive points at making something good rather than something extractive.

**Meme tracing** is the attribution side: ideas are traced as they spread and adapt, so originators are recognised without anyone being blocked from using the idea. That recognition is **never credit** and never converts into it. It is reputation, and reputation's only power here is to attract support for what you do next.

Two honest caveats, because overclaiming here would be easy:

- **The standard is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making — you trust the seller. That is fine at human scale, and provenance only turns vicious in the capitalised art market, which is exactly the layer being removed. Aequitas does not need to solve a problem the current world also hasn't solved and doesn't much suffer from.
- **The obvious argument doesn't generalise.** People say a copied recording advertises the live show — someone can pirate the track but won't play the concert. True for music. Much weaker for novels, software, and research. It's a good illustration, not a rule, and it's presented as one.

---

# Part II — The questions readers ask

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

**A pledge doesn't spend your credit, and it isn't a promise to buy.** Your credit stays yours — a pledge just puts it *behind* something, the way naming a beneficiary doesn't hand over your bank balance. It gives whoever you're backing more room to carry the cost of the work. What it *does* use up is a separate **lifetime allowance**. Over your whole life you can pledge as many hours as you have earned, and **a pledge is permanent: you cannot take it back.** That permanence is deliberate, so the people you back can rely on it and get on with the work. And because a pledge is a real, one-time expense, nobody can pledge frivolously or flood the system for free.

**A pledge summons work — it doesn't have to be about a *thing*.** Say you've earned four hours and you pledge two toward mowing the scrappy public verge on your street. Someone with a mower sees it, spends an hour, shows proof, and earns an hour of credit. That's the whole transaction — no object changed hands, nobody's credit was cancelled, and one pledged hour is still behind the next mow. Where the pledged work *does* make an object, taking that object is a separate step: whoever accepts it takes on its debit with their *own* room, pledge or no pledge. It is deliberately messy. People will pledge for silly things, pledges will go unfilled, and groups will form to coordinate them. That is fine. Messy or not, it's the thing that creates jobs.

**Pledges are the demand side of the economy.** Cost tells you what something takes; pledges tell you who wants it. Together they do the job prices do, with no central optimiser and no board deciding priorities.

They must be strictly one-to-one: the hours you put behind things over your life can never exceed the credit you've actually earned. Let it, and people would be backing work with room that isn't really there — the makers leaning on it would be standing on a promise nobody can keep. That's not a preference, it's arithmetic.

**Signals should be abundant** precisely because pledges are scarce. If pledging is all you have, the system only ever hears your single top priority and learns nothing about the rest. Cheap signals reveal what you actually care about, in order.

Three things this quietly fixes:

- **It gives surplus a purpose.** Since credit cannot be accumulated into wealth, someone who produces far more than they consume would otherwise have no outlet. Instead they get to **direct what the world works on next** — which is a considerably more interesting reward than a larger pile.
- **It funds the speculative.** A prize for solving a hard problem needs no billionaire patron; a large enough pool of pledges *is* the prize.
- **It sets the number of doctors.** Society decides how many to train by pledging for it — no ministry, no quota. Study nobody pledged for still credits your hours, but leaves you carrying the cost.

- **It gets unwanted work done — without danger-pay.** Everyone earns the same credit per hour, so there's no hazard bonus to lure people into a toxic cleanup. Instead, people pledge more for the jobs nobody wants, and that room goes to whoever does them. Society de-risks the worker exactly as much as it wants the job done, and **nobody's hourly credit changed** — what changed is how much room other people chose to put behind them. A pledge can also carry conditions: *"this part goes to whoever cleans up any harm this job causes in the next thirty years."* If nothing goes wrong, that part simply lapses. **This reaches boring work as well as dangerous work**, because a pledge can name whoever does the dull job.

**One honest weakness.** Pledges follow reputation, so a first-time maker attracts none. This is the same cold-start problem unknown creators face with money today. The barrier is much lower, because it is attention rather than capital, but it is real and should not be waved away.

<!-- tag: ovw-demand-lever -->
### "But a price already tells you what people want"

**This is the objection economists bring first, and it hides an assumption nobody states out loud:** that a price is an honest report of how scarce a thing is and how much people want it.

**In a market with a few big sellers, it is not.**

| What people assume | What is actually going on |
|---|---|
| Scarcity is a physical fact, and the price reports it | **A lot of scarcity is made on purpose.** Hold back supply and the number stays up. |
| Wanting is a fact, and the price reports that too | **Wanting is manufactured, on an industrial scale.** That is the entire job of advertising. |
| So the price tells you what people want | **The same firms control supply and work on demand.** The price is partly reporting its own author. |

**This is not a slogan — it is economic history.** Fernand Braudel described two layers, not one: market towns full of small sellers where price settles from below, and above them a handful of operators large enough to *set* prices rather than take them. [Manuel DeLanda](https://nettime.org/Lists-Archives/nettime-l-9610/msg00025.html) sums that upper layer up bluntly: it *"has always engaged in anti-competitive practices, manipulating demand and supply in a variety of ways."* **He calls it an anti-market — and that, not commerce, is what Aequitas is against.**

> **So Aequitas is not smashing a clean instrument and offering a worse one. It is replacing a signal the seller helped write.**

**A pledge cannot be advertised into existence.** It is backed by hours you actually worked, spent once, and visible to everyone. **A seller can make you want something. A seller cannot put more hours in your day.**

**The power to say what gets made is spread far more evenly. Here are both halves of the comparison, including the one where this system has no bound at all.**

| | Money | Aequitas |
|---|---|---|
| **The say over what gets made** | The top reaches about **1,000,000 ×** the middle | **Capped at `24 ÷ F`** inside one network's books — 2.4 × at a 10-hour baseline — and a very hard working life reaches about **1.6 ×**. Everyone alive holds some, because staying alive earns credit |
| **Material consumption** | about **670 ×** the middle | **No cap.** Limited only by how many people pledge to you (§1) |

**In plain words: the say is bounded and stated as one number. Consumption is not bounded, and this document says so rather than leaving it to be found.**

#### Two examples

**Someone wants radicchio at their corner shop.** They tell their phone. Under settings they chose earlier, it puts **half an hour** of pledge behind getting radicchio to that shop.

Putting one extra box on that shelf takes about **two hours of work**: picking it, loading it, the lorry's extra minutes, stacking it. So **four people wishing for it fills one box.** A haulier sees the pledges, adds a box, the shopkeeper takes it. **No price moved and nobody planned it.**

**An artist posts a photo of their street mural.** **Five thousand people like it.** Their apps turn those likes into pledges, at a rate each person set for themselves.

| | |
|---|---|
| Room raised for the artist | **500 hours** |
| What their next mural needs — paint, travel | **300 hours** |
| Left over | **200 hours** |

**The leftover is room the artist can use**, unless the people pledging attached conditions to it. **So yes — somebody well-liked can end up with a lot of room, and Aequitas does not stop that.** What it stops is the thing that makes money-wealth grow: that room **can't be lent at interest, rented out, charged for, or used to hire anyone.** It lets you hold and use things. It is not a machine for getting more.

*(One catch worth knowing: a flat rate per like barely limits anything. Six minutes is 0.1 hours, and a person earns about 3,650 hours a year from staying alive, so the budget only runs out at about **36,500 likes a year** — far more than anybody gives. The sensible setting is a **share of a budget**: "this like costs my art budget divided by the likes I give this month." That balances itself.)*

**Two things this does not do.** It does not let likes buy credit — a pledge is not credit, and no amount of applause turns into earned hours. And **it does not answer who gets the last radicchio when two people want it.** Pledges decide how many get grown. Who gets the last one is a queue, a lottery, or first-in-line at the shop — decided where the thing is handed over, not by this document.

<!-- tag: ovw-when-does-the-work-actually -->
### When does the work actually count?

Your work is written down the moment you do it. But it **counts once the result is checked.** For something you *made*, the check is simple: it counts when the thing **changes hands.** When a workshop hands a batch of toasters to a driver, the driver takes them on and takes on the debt that rides with them. That is what confirms the toasters are real. That confirmation is what turns the makers' hours into credit that counts.

**What "checked" means depends on what you did.** For a *made thing*, it's the hand-off above. For a *service* with nothing to hand over, such as a haircut or an hour of counselling, it is the person you did it for confirming it happened. For *creative or intellectual work*, it's evidence the work was really done — never a tally of how many people *liked* it (approval is not the check, or applause would quietly turn into money). And for the work of *keeping yourself alive*, the check is simply that you're still here: a living, verified person plainly did the maintaining. Different kinds of work, checked in the way that fits each — and the trust networks (§7) are the ones who work out and police exactly how.

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

**Who checks the cost estimates themselves? This is the weakest spot in the whole system, and it is stated plainly here rather than glossed.**

If the recorded cost of beef were set too low, every beef eater benefits and none of them will pay to fix it. **Errors that make something look dearer get corrected fast. Errors that make it look cheaper have nobody.**

**One thing does help, and it is real:** there is **no profit anywhere in the system** to fund a convenient scientific result, so the ordinary way cost science gets corrupted today is closed off at the root.

> **We used to claim more than that, and withdrew it on 2026-08-24.** The old answer was: *plant-protein producers are harmed by cheap beef, so they will pay for the correction.* It does not hold. Paying for that correction is expensive and the benefit is shared with every other plant-protein producer, while getting their own figure set generously is cheap and benefits only them. **So the likely outcome is everyone's numbers drifting low together, not everyone policing each other.** And it fails worst on the biggest setting of all, *how much pollution the world absorbs on its own*. There, everyone benefits from a generous number and there is no rival at all.

**What we say now: this is a job for the bookkeepers, not for this document.** How a trust network checks its own cost figures is theirs to design: who repeats a measurement, what triggers a review, what happens to a figure while it is disputed. That is the same way the specific method for splitting a factory's costs is the industry's.

**But a network is not free to have no answer.** Five things must be true of whichever answer it picks:

1. **Two *unaffiliated* replications** before a figure is allowed to change history. Unaffiliated is the load-carrying word: a network staffed by the industry it checks can repeat a measurement twice and learn nothing.
2. **Every figure published with its method, its version, and how uncertain it is.**
3. **Review aimed at the figures that move the most and benefit the fewest**, not just the biggest ones.
4. **The membership list is public** — a network made mostly of the industry it checks is compromised by construction, and this makes that visible.
5. **A public list of what has *not* been checked**, and how old each check is.

**The honest part: nobody has built one of these yet, so nobody has shown that it works.** Those five are the test a design has to pass. They are not proof it passed.

**One distinction makes the problem smaller than it first looks, though, and it is worth having.** There are two different things to audit, and they are in different shape.

| What is being audited | Is anyone harmed by getting it wrong? |
|---|---|
| **The weight of a thing** — what a tonne of carbon costs in hours | **Nobody.** Everyone benefits from a generous figure, so nobody funds the correction |
| **The extent of the books** — how much of a region's output was actually recorded | **Two parties.** A producer who does keep records is harmed when undocumented produce looks cheaper than it is. And a producer outside the books cannot trade inside the system until they join |

**In plain words: the audit of extent has people with a private reason to get it right. The audit of weight does not.** That asymmetry is the whole of the relief, and it is why this section's worst problem is narrower than it reads.

**Everyone is in the books; only participants can act on their position.** Every human has an estimated credit *and* debit position, whether they have ever heard of Aequitas or not — otherwise the accounting would show wheat with no grower, which is false. But an estimate does nothing until you hold a verified account and real records replace the guesses. **Joining is exactly the act of turning an estimate into a record**, and it is usually to your advantage: most people's real footprint is below their cohort's average, and your estimated contribution does nothing for you until you claim it.

**What the checks can see — and what they cannot.** The arithmetic catches a factory whose declared outputs do not balance its declared inputs: the missing material went somewhere, and the books say so without anyone investigating. What it *cannot* do is see a workshop that never joined at all. Nothing you can compute from a record tells you what was left out of it.

So that half is answered a different way, and it is the ordinary way: **measure the world from outside and compare.** A satellite pass over the valley, a harvest total, a port manifest, a reading of how much of a pollutant is actually in the air. If the region grew a hundred tonnes and the books account for sixty, forty tonnes came from people outside the system — and **that gap is a measurement, not an accusation.** Anyone with the same instrument gets the same number.

Two things follow.

**The estimate for whoever stays outside gets worse as everyone else joins.** The guess for someone still outside is worked out from the pool of what nobody has measured, and never from an average over everybody. So as good producers instrument themselves and leave that pool, the guess applied to whoever remains rises.

> **The forty tonnes are never simply divided by the number of farms missing, and the reason has digits behind it.** A valley of 100 farms: eighty subscribe and record 82,000 tonnes, a satellite says 88,000, so 6,000 tonnes are unaccounted for. **The same satellite also measured the twenty missing farms' land: 5,000 hectares between them, unevenly held.**
>
> | | Head count | Worked out from the land |
> |---|--:|--:|
> | The rate used | 6,000 ÷ 20 farms | 6,000 ÷ 5,000 ha = **1.2 t/ha** |
> | The largest farm, 600 ha | **300 t** | **720 t** |
> | The smallest farm, 100 ha | **300 t** | **120 t** |
> | Total | 6,000 t | 6,000 t |
>
> **Split by head count, a 100-hectare farm and a 600-hectare farm get the same figure. No instrument ever said that.** Both methods add to 6,000 tonnes. **Only one of them describes a farm.**
>
> **A simulation is what settled it.** Two different worlds were put in front of one network, and both handed it identical books to the last decimal — while the truth behind them differed by a fifth. **No sum you can do on those books tells the two worlds apart.**
>
> **And the land method is not settled either, which the documents now say out loud.** Honest errors in measuring land barely move the answer. **A producer who deliberately declares half the land they farm defeats it.** Whether the survey catches that has been argued and never tested, so **a network has to publish its land register as something nobody has audited.**

> **Nobody outside is charged anything, and this is worth being exact about.** The estimate is a statement about material flows in the world, not a bill. **It does nothing at all until the person joins** — and then it is their opening position, which they replace with real records. **So what gets worse is the position you would inherit, not a debt accumulating against you.** Nobody is compelled, and nobody is billed.

**The gap is never handed to somebody else to carry.** The forty tonnes sit against nobody's name until the farms who grew them join and claim them.

> **The reason is one sentence: a gap proves that something is missing; it never proves whose.** Subtracting one measurement from another tells you the difference exists. **It cannot tell you which farm the difference came from**, so any rule that shares it out among the farms you happen to know about is a guess dressed up as a finding. *(An outside critic put it that way to us, and it is a better reason than the one we had been giving.)*

**Staying out of the books is not the same as hiding.** A subscriber can have output that is not in the books — food grown for their own household, work given away, produce kept back for the ordinary money economy, the same crop offered to two networks so it finds a buyer. **None of that is evasion, and the system does not try to capture it.** The discipline is simply that **produce you do not enter into the network cannot be sold on the network.**

#### Two rules keep this from flattering us, and both were earned the hard way

**The first is that the two measurements have to be about the same thing.** The gap only means something if the outside total and the recorded total cover the same quantity, the same piece of ground, over the same stretch of time, with error bars smaller than the gap between them. **On this project's own worked case, skipping that check made the unmeasured pool look three times larger than it was.**

**The second is that a subtraction does not tell you which way it is wrong.** A count can only ever be too low, so better coverage moves it one way. **A subtraction reverses the direction of every error inside it.**

**Worked, on the valley.** The published figures are 88,000 tonnes outside and 82,000 recorded, so the gap reads 6,000.

| What is really going on | The true gap | So 6,000 is |
|---|--:|---|
| The **records** missed 4,000 t | 2,000 t | a **ceiling** — the published figure is **3 times the truth** |
| The **satellite** missed 10,000 t | 16,000 t | a **floor** |

**In plain words: same figure, same incompleteness, opposite meanings.** So every figure of this shape is published as a range carrying one of three labels: **`floor`**, **`ceiling`**, or **`not identified`**. **`not identified` is where every figure starts.** A label has to be argued for, one blind spot at a time, and it is never inherited from the fact that something was incomplete.

**Why the default has to be the unflattering one.** Four figures this project has published were each found wrong **in the direction that favoured us**, and every one was found from outside. A bigger dark pool makes our coverage argument look stronger. A higher coverage percentage makes our books look better kept. **The error is not careless, and it will not be caught by whoever made it.**

**No number here is ever final.** A tally is a citation rather than a verdict. It says who measured, how, over what area, and as of when. When somebody measures better, **every affected record recalculates**, backwards, because balances are derived rather than stored. A wrong figure is never deleted or quietly edited; a note is attached to it and a better record is added beside it. That is how science handles a mistake, and it is the only method that does not need an authority standing at the door deciding what may be written down.

> **One guarantee that has to come with that.** Because figures move, the check on what you may consume is made **at the moment you do it.** If a cost is revised upward next year, that changes what you may do *next year* — it never reaches back and turns something you already did into an offence. A ledger that recalculates must never mean a debt that ambushes you.

**Nobody owns the rules.** There is no foundation, company, or standards body with authority over the core. Local variations are expected and compete openly on their merits; the axioms themselves are not amendable by anyone, including whoever builds the first implementation.

---

<!-- tag: ovw-s8 -->
## 8 — Wouldn't this need total surveillance?

**No, and the reason is worth being precise about.**

The accounting covers **what is claimed and attested.** It does not cover, and does not want to cover, everything a person does.

People spend hours making memes, telling jokes, arguing online, cooking for friends, and messing about. That is real time and real effort. Tracing who shared what to whom in order to assign work-credit for it would be both impossible and grotesque, and any group that proposed it would be laughed at — which is the governance model working exactly as intended.

> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it.** The books cover what's claimed. Everything else is life.

**On privacy specifically, and the order here matters.** The aim is that accounts stay private and that a claim can be checked without exposing a history: you show you are within your limit without handing over a list of everything you have ever done.

> **That mechanism does not exist yet, and this is the project's sharpest open problem.** The right shape is known, which is a proof that reveals nothing but the answer. But **the precise set of what an auditor must be shown has not been specified.** A second difficulty is known too: public records kept under false names can often be analysed to work out who somebody is. **Two things elsewhere in this document lean on this being solved** — the check on a sloppy network (§7), and rebuilding a joining person's life. Neither is safe until it is.

**This is roughly where society already sits.** You transfer money today knowing your counterparty and nothing whatsoever about anyone else's accounts. Nobody audits those accounts because the trust is parked at a bank. **Aequitas does not require more visibility than that — it requires the same visibility with the trust moved somewhere less capturable.**

**The line is drawn between the market and the person.** What is *made*, what is *wanted* and what things *cost* is out in the open. Pledges, production quantities and the figures things carry are public, though whoever backed a pledge can stay anonymous, like a crowdfunding backer. **What stays private is you: your own running tally.**

**That split does real work.** Public market facts are what let anyone audit a supply chain, let a worker see how wanted their product is, and stop anyone from quietly relabelling pledged work as speculative. **None of that needs a single person's private ledger.**

**Getting the combination right is the unfinished part** — open flows, closed persons, and no way to work one out from the other.

---

<!-- tag: ovw-s9 -->
## 9 — Didn't this fail before?

It should. A century of alternative economies died, and pretending otherwise would be dishonest. They died in three distinct ways.

| How they died | What actually happened | Does it reach Aequitas? |
|---|---|---|
| **Circulation** | [Ithaca HOURS](https://en.wikipedia.org/wiki/Ithaca_HOURS) businesses ended up *drowning in Hours* they could not spend; Burlington Bread piled up at cafés. Local scrip flows to whoever buys supplies from outside the network, and stops there. | **No. There is no medium of exchange to pile up.** Credit never moves, so nobody ever receives credit from anyone, so nobody can be stuck holding it. |
| **Valuation** | [Josiah Warren](https://en.wikipedia.org/wiki/Josiah_Warren) could not reconcile hour-for-hour trading with skill and unpleasantness. [Time banks](https://en.wikipedia.org/wiki/Time-based_currency), 45 years on, still report chronic shortages of skilled members from flat-rate crediting. | **Mostly answered.** Paying for training up front deals with skill. **Danger and tedium are both reached by pledges**, because a pledge can name whoever does a job nobody wants (§6). What is not settled is whether enough people will actually pledge for dull work — see §10. |
| **Institutional** | [Wörgl](https://en.wikipedia.org/wiki/W%C3%B6rgl)'s scrip was shut down by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca's system died when its founder moved away. | **The legal weapon doesn't fit** — there is no issuer, no notes, nothing to counterfeit, and no currency to compete with legal tender. **This is the real reason Aequitas must never be called a currency.** Founder-dependence is a live design constraint: every mechanism must pay its own maintainer from inside the system, or it has an expiry date. |

**The "you can't run an economy without prices" objection**. This is the oldest and most cited attack — every economist brings it first, so it deserves a real answer rather than a wave. It comes in two flavours, and they need different replies.

**The first flavour (Mises): without market prices, you can't know what anything is *worth*, so you're allocating blind.** The reply is the distinction this whole document is built on: **Aequitas never computes what things are worth.** It computes what they *cost* in hours, energy, materials and damage, all of which is physical and measurable. The objection assumes its target is trying to price value without a market. Aequitas isn't. It concedes, cheerfully, that you can't measure worth without a market — and then points out it wasn't trying to.

**But that raises the fair question: if cost ignores what people want, who decides what gets made?** Not a committee — that's the failure mode of every planned economy, and the point where the objection would be owed the whole argument. The answer is **pledges** (§6). People spend their own earned credit to call the things they want into being, and cheap signals carry everything milder. A market price secretly does two jobs at once — it tells you what a thing took *and* how much people want it, mashed into one number that can never be pulled apart again. Aequitas keeps the two jobs **separate**: cost measures what a thing took; pledges reveal who wants it. Between them they steer production, with nobody in charge.

**The second flavour (Hayek): the knowledge is scattered and unwritten — no central calculator can gather it.** This one is sharper, and honesty requires only a partial claim. Part of it Aequitas answers. It gathers data *locally*, from the person on the spot and the meter on the machine, and never demands that one authority assemble everything. But the deeper point is that a lot of what people know is a gut feel that never gets written down. A ledger of physical flows genuinely does not capture that, and should not pretend to. The escape is that **Aequitas isn't a plan.** It sets no targets and optimises no grand objective; it just keeps the books under an ordinary decentralised market where the person on the spot still makes their own call. Hayek's objection is to central *planning*. Aequitas isn't one, so it doesn't have to solve his problem — only avoid recreating it.

**The objection that it is too big to compute has been tested and answered.** [Cockshott and Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) showed that calculation in physical units at national scale runs on ordinary hardware with sparse-matrix methods. People ran the arithmetic; it runs. *(The full, rigorous version of all of this, including how genuinely scarce things get rationed without profit, is `00-strategy/open-problems/OP-9_calculation_reply.md`.)*

<!-- tag: ovw-s9-parallel -->
### Can I use it while everyone else still uses money?

**Yes. That is the only way it could ever start**, because for years most of the people you deal with will still be outside.

**Nothing is banned in either direction, and both directions cost you a little on purpose.** The pressure always runs the same way: toward trading with people who are also inside.

**Bringing something in.** You made a chair using timber you bought with money. That chair has no history in the books — nobody recorded where the wood came from. So when you sell it to someone inside, one of two things happens. You write up its history properly, or you use a published standard figure for what a chair of that kind costs, so the sale can go through right now instead of waiting. **The standard figure is deliberately set a bit dear**, because otherwise nobody would ever bother keeping real records. Note what happened to you: you spent money on the timber and got no money back. That is the cost of bringing money-made things in, and it is meant to be there.

**Selling something out.** You baked bread from flour you got inside, and your customer only has money. **Sell it — nobody stops you. But the bread's debt stays on your books.** As far as the accounts are concerned you gave the bread away, and **they never see the money at all.**

**That last part is not a rule someone wrote. It falls out of what the system counts.** The books record matter and energy, and money is neither. A banknote moving from one hand to another is not a physical event the ledger has any way to notice, so it simply is not there. It is not hidden and not ignored on purpose. It is **invisible, in the way a colour is invisible to a set of scales.**

**Two things worth knowing, because they are the ones people assume must be false.**

**Money cannot buy standing here. At all.** Suppose someone wealthy pays a hundred people to make things and sells them into the system. **The hundred workers earn the hours, because credit is a record of who actually did the work.** The person who paid did none of it, so they earn nothing. **You cannot buy someone else's hours, at any price**, and nobody's day has more than 24 of them.

**Buying cheap inside to sell dear outside wrecks the person doing it.** Everything you take on from inside adds to what you owe. Selling it outside never takes that off you. Meanwhile the only thing that grows your side of the ledger is the hours you personally work. **So the account of anyone milking the system gets worse with every load they pull out, until it stops them buying anything more.** No one has to catch them. **The books just stop lending them rope.**

**On what Aequitas deliberately does *not* do:** it does not propose abolishing municipal government, planning departments, courts, or the civil service. Those institutions largely work. **The target is oligarchic capture, not administration.** Only the economic nature of these institutions changes — they stop being funded by extraction and start being credited for the work they do.

---

<!-- tag: ovw-s10 -->
## 10 — What we haven't solved

A proposal that admits nothing is a proposal nobody should trust.

**This project has withdrawn published claims after outside critics showed they did not hold.** Three of them are named in the sections they affected: the rival-producer answer to cost drift (§7), the labour-abundance comparison (§1), and a rule sending a power station's emissions to the household (§4). **In every case the error ran in this project's own favour, and in every case somebody outside found it.** That is the record, and it is the reason to take the list below seriously rather than as decoration.

**The live problems, in order of how much they matter:**

- **Splitting *blame* within a team** *(now answered, and the answer is a declared convention)*. Crediting a team turned out to be a non-problem: everyone is credited **their own hours**, and nobody needs to say "the welder caused 40% of the bridge," because credit was never a share of the output. **When a team jointly causes a harm, that debt divides by the hours each person worked.** The reason is that hours are already recorded, already capped at 24 a day, and so add no new thing to game. **This is a convention we declare rather than a trace we measure, and it is labelled as one** — it was checked in 2026 against the hardest form of the case, a metered delivery tailpipe where one person's hands were on the vehicle.
- **Who controls the cost model.** Whoever sets what a tonne of carbon "costs" influences every ledger in history without touching a single rule. Several defences are in place; the general problem is not closed.
- **Understatement drift.** Errors that make something look *more* costly get corrected by everyone affected. Errors that make it look *less* costly benefit everyone affected, and nobody funds the correction. **We had a proposed answer, that rival producers would police each other, and we withdrew it on 2026-08-24 because it does not hold** (§7). **This is now stated as an unsolved problem that each trust network must design against, held to five published requirements.** It bites hardest on the "how much pollution can the world absorb on its own" line, which is one of the most powerful settings in the whole system and which has no rival at all: everyone benefits from it being drawn too generously.
- **Dumping.** Owning the end of a thing's life (§4) counts correctly for anyone who plays by the rules. But someone could still fly-tip a worthless object to escape its disposal cost. Catching that is the same kind of problem as any other false record, and is left to the verification layer rather than solved here.
- **Unpleasant work** *(the mechanism is now in place; what is open is whether it works)*. Exertion, danger and skill all resolve into material costs. Tedium and indignity leave no physical trace, so for a long time nothing reached them. **A pledge now can**: it may simply name whoever does the dull job, so the room goes to them without anybody's hourly credit changing (§6). What is genuinely unsettled is behavioural rather than structural — whether enough people will choose to pledge for boring necessary work, and what happens in a community where they do not.
- **Turning contribution into influence.** How much say people get, and how it accrues, is unsettled. The leading candidate is that everyone accrues the same influence per hour worked — not a voting scheme, and deliberately not one. One nice consequence already falls out: because staying alive earns credit, *everyone* gets a baseline say in what the world makes next simply for being alive, and since that baseline is equal for all, it would cap the say-gap the same way it caps the wealth-gap — and subject to the same caveats (§1): only if fake hours can be prevented and baselines stay sane. **Two things are still open.** Stopping people from *manufacturing* fake hours to buy extra say, and how generous each community sets its "cost of staying alive" baseline, which quietly sets where the cap lands.
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

*For the rigorous statement of everything above, with the arguments and the open problems in full: `00-strategy/Aequitas_Foundations.md`.*
