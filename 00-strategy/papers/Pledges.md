# Pledges — what they are, what they buy, and why that is not profit

> **Version:** 1.0
> **Date:** 2026-09-18
> **Status:** Rulings settled. **Not folded** — the core documents still carry the old rules. **Two code jobs remain**; see §16.
>
> **Fourteen author rulings, all 2026-09-18.**
>
> 1. **A pledge may name a person, and the room it grants is consumable** by whoever receives it.
> 2. **The disparity ceiling is withdrawn over consumption and restated over pledge budgets.** The arithmetic is identical, because a pledge budget is earned credit and nothing else. §4.
> 3. **A pledge that names no individual grants no room yet.** A pledge to a fund, a cause, an organisation, or any other mechanism stays **uncommitted** until it is distributed to named people.
> 4. **Dynasties still fail.** Pledges are not transferable once allocated.
> 5. **Every rule here must be derived from the axioms**, never asserted as a convenient choice. §3.1 is the first case.
> 6. **A pledge requires consent.** An infant cannot pledge. §11.4.
> 7. **A child carries no debit.** Care rendered to it credits the carer and debits nobody, exactly as the floor credits a person with no matching debit. §13.1.
> 8. **Who may consent to a property transfer is a trust network's decision**, and belongs in §2.6's list of settings that vary. §13.1.
> 9. **The inflation discussion goes to the research archive.** Foundations gets a few sentences and a pointer. §9, job 5.
> 10. **Aequitas does not write the rules of medical debt, and cannot.** Which treatments a person carries is a network's rule, changeable by it, and sometimes a matter for a court. §15.
> 11. **The contingent reserve is withdrawn and becomes an example.** A pledge names a recipient **or the criteria under which one will be named**; criteria may be any conditional thing; **once a person is named the room is committed and unchangeable.** §8.
> 12. **A pledge costs the pledger time.** Budget is earned credit, IC-7 caps a day at 24 hours, so **budget cannot be manufactured.** §7.1.
> 13. **Coercion is the legal system's problem**, beyond this system's scope. §7.2.
> 14. **Discretionary awarding criteria are permitted, and are how a prize works.** §8.4.

---

## 1. What a pledge is

**Terms used here.**

| Term | What it means |
|---|---|
| **Credit**, `C` | Hours of a person's life the books recorded as work. It never moves between people. |
| **Debit**, `D` | What a person's consumption and holdings are reckoned to have taken from the world, in hours. |
| **The gate** | The rule deciding whether a person may take a thing. Below, it is written out in full. |
| **ρ** ("rho") | The network's debit tolerance. A multiplier the network sets. |
| **Room** | The distance between a person's debit and the gate. Room is what lets you take a thing. |
| **Pledge budget** | A lifetime allowance, equal to the hours a person has earned. Spent once, never returned. |

> **A pledge is a permanent grant of room from one person to a named recipient, drawn from the pledger's lifetime pledge budget.**

A pledge does not move credit. The pledger's credit stays exactly where it was. What the pledger gives up is their own future ability to pledge.

**A pledge may name three kinds of thing, and the difference decides when the room appears.**

| What the pledge names | When it becomes room |
|---|---|
| **A person** — anyone, **including the pledger** | **At once.** §11 is why self-pledging is permitted |
| **A fund, a cause, an initiative, an organisation** | **Only when it is distributed to named people.** Until then it is **uncommitted** and sits in nobody's gate. §3.1 |
| **Criteria under which a person will be named** — *"whoever mitigates harm from this task"* | **When the criteria name somebody.** If they never do, it lapses and nobody's gate ever held it. §8 |

**Once a person is named the room is committed, consumable and unchangeable.** Before that it is uncommitted and grants nothing.

**And a pledge is an act that requires consent.** An infant accrues a budget and cannot spend it (§11.4).

---

## 2. What changed

**Before this ruling, a pledge could only name work.** A task, an asset, or the people staffing one. Room granted by a pledge was earmarked: it offset a named creation-cost and nothing else, and any surplus was never spendable.

**Three sentences in the current documents state the old rule.**

| Where | What it says |
|---|---|
<!-- struck-ok: this paper must quote the withdrawn wordings in order to record that they were withdrawn -->
| `Aequitas_Foundations.md` §4.6 | "The surplus is not a payment to the doer and is not consumable." |
| `Aequitas_Overview.md` §6 | "Nobody gets a bonus for being popular." |
| `06-simulation/statera/statera.py` | The granted offset is capped at the creation-cost, so "ordinary consumption debit is never offsettable by a pledge." |

**All three are superseded.** A pledge now grants room the recipient may spend on anything.

---

## 3. The gate, restated

The core documents write the gate as `D ≤ ρ·C`. That form has no place in it for pledged room, so it cannot be right. The correct form is:

> **`D ≤ ρ·(C + P)`**
>
> `P` is the committed room the account has been granted by other people's pledges.

**Two reasons ρ multiplies `P` as well as `C`, and the second is what decides it.**

**1. A2 (time as measure) says one hour credits as one hour, whoever worked it.** Write the gate `ρ·C + P` and a pledged hour grants 1 hour of room while a worked hour grants 1.2. **That is a rate distinction between two hours, which is what A2 forbids.** Under `ρ·(C + P)` both hours grant the same room.

**2. ρ is the network's only rationing dial, and it must reach the whole gate.** Under `ρ·C + P`, lowering ρ cannot touch accumulated pledged room. In the limit the network sets ρ to zero and still faces `D ≤ P`. **A network that cannot ration is a network with no answer to §5.5.3's upper bound.** §13 works the population case through, where this is the difference between having a dial and not.

> *(This paper proposed `ρ·C + P` at 0.2. The solvency worry behind that form does not hold: backing is still one hour pledged per hour earned, and ρ scales worked and pledged hours alike, so no asymmetry appears.)*

### An example, with the numbers

**A network with `F` = 10 hours a day and ρ = 1.2.** A person aged 40 has done nothing but stay alive.

| | Hours |
|---|--:|
| Credit `C`, 40 years at 10 h/day | 146,000 |
| Committed room granted by 300 people pledging 100 h each, `P` | 30,000 |
| **Their gate, `ρ·(C + P)`** | **211,200** |
| The same gate with no pledges, `ρ·C` | 175,200 |

**Their credit did not change.** Three hundred people spent 30,000 hours of their own lifetime pledge budgets, permanently, and received nothing back.

### 3.1 A pledge that names no individual grants no room yet

> **A pledge to a fund, a cause, an organisation, or any other mechanism is *uncommitted*. It becomes room only when it is distributed to named people.**

**`P` counts committed room only.** An uncommitted pledge sits in no account's gate, so it lets nobody take anything.

**The pledger's budget is still spent at pledge time.** It is not returned, and there is no path that returns it. **This keeps IC-9 exactly as written**, and it keeps pledging a real sacrifice whether or not the money ever reaches anybody.

**Undistributed pledges lapse.** A fund that never distributes has burned its pledgers' budgets and created no room. That is the same rule the documents already apply to an abandoned task.

#### An example, with the numbers

**A community pledges 30,000 hours toward building a clinic.** The clinic is then staffed by **six people**, who work **2,000 hours each** in its first year.

| | Hours | Whose gate it sits in |
|---|--:|---|
| Pledged to the fund | 30,000 | **Nobody's.** Uncommitted |
| Distributed to the six staff, by hours worked | 30,000 | **5,000 h each**, on six named accounts |
| If the clinic is never built | 30,000 | **Nobody's, ever.** The pledgers' budgets are spent and lapse |

**The pledgers spent 30,000 hours of budget on the day they pledged, in all three rows.**

#### Distribution by hours worked is the only basis the axioms leave standing

**Whoever decides who gets the room holds real power.** A fund sitting on a large uncommitted pool, free to hand room to whoever it likes, is the capture surface this ruling creates.

> **Room distributes by hours worked on the work the pledge named.**

**That is not a preference. It is what is left after four axioms eliminate everything else.**

| Step | The axiom | What it eliminates |
|---|---|---|
| **1** | **A1.** "A flow is attributed to whoever caused it. **Only people act**, so responsibility attaches to people, and never to a tool, a machine, or whoever owns one" | **The fund itself, and whoever runs it.** A fund did not do the work, so room cannot stop there |
| **2** | **A2.** "Labour is never rate-scaled. One hour credits as one hour, whoever worked it" | **Every basis that weighs one worker's hour above another's** — skill, rank, seniority, role, need, hardship. All of them make one hour on the task worth more room than another |
| **3** | **§4.4's rule, and §2.5's test behind it.** *"The leftover is never divided by a count of producers"*, because a head count leaves no physical trace | **An equal split per person.** A head count is the quantity §4.4 already refuses to divide by, for the same reason |
| **4** | **A8.** "No organisation may acquire authority over the core rules" | **Discretion.** A fund choosing recipients on merit needs a published rule saying what merit is, which is an objective function. **Every allocation rule this project has rejected needed one**, and each re-opened OP-10 (weighting governance) |

**What survives steps 1 to 4 is hours worked on the named work, and nothing else does.**

> **⚠️ Read that as the default, not as the only permitted rule.** Ruling 11 (§8) lets a pledge carry **criteria** saying who will be named. **Where a pledge states criteria, the criteria govern. Where it is silent, hours worked applies.**
>
> **Step 4 is narrower than it first reads.** A8 stops a **network** imposing an unpublished discretionary rule. **It does not reach a pledger's own criteria**, because a pledger directing their own budget is the whole point of a pledge. **What A8 does require is that the criteria be published before the pledge is made** (§4.2, §8.4).

**It is also already recorded.** Hours are kept for credit and capped at 24 a day by IC-7, so the basis adds no new lever. **And `Aequitas_Foundations.md` §3.2c and §4.6 already divide by hours worked**, for an organisation's debit and for a task's pledged cover. **This writes no new rule; it applies an existing one to a third case.**

> **Stated honestly: hours worked is a declared convention on a measurable basis, not a measurement** (§2.5). **What the four steps buy is that it is the only candidate left**, which is stronger than declaring it and moving on.

---

## 4. The ceiling moves from consumption to pledge budgets

**Author ruling: `24 ÷ F` is withdrawn over consumption and restated over pledge budgets. The arithmetic does not change.**

### 4.1 What it used to say, and why that failed

**The old claim was about what a person may consume.** It failed because consumption is gated by `ρ·(C + P)`, and `P` has no limit on any one account. **The only limit on `P` is the population**: total committed room across a network can never exceed the total credit its subscribers have earned. That bounds the sum. **It does not bound one person's share, and nothing in the system does.**

### 4.2 What it says now

> **Inside one trust network's books, the ratio between the largest and the smallest lifetime pledge budget *per day lived* cannot exceed `24 ÷ F`.**

**The derivation is three lines and uses nothing new.**

1. **A pledge budget equals the credit a person earned in their life**, and nothing else. `Aequitas_Conformance.md` row 9.
2. **Every living subscriber accrues at least `F` hours a day**, and **IC-7 caps any account at 24 hours of activity in 24 hours.** So credit per day lived sits between `F` and 24.
3. **Therefore pledge budget per day lived sits between `F` and 24**, and the ratio of the largest to the smallest is `24 ÷ F`. **At `F` = 10 that is 2.40.**

**Nothing breaks it the way `P` broke the consumption claim.** Room received does not raise a pledge budget, so there is no term to add.

#### An example, with the numbers

**A network with `F` = 10 h/day. Four whole lives, 80 years each.** These are the same four lives `Aequitas_Foundations.md` §5.5.5 uses, read as pledge budgets instead of as consumption.

| | Lifetime pledge budget | Per day lived | Against a floor-only life |
|---|--:|--:|--:|
| **L — lives only** | 292,000 h | 10.0 h | **1.00×** |
| **P — a very hard working life** | 472,000 h | 16.2 h | **1.62×** |
| **N — maximum, childhood uncredited** | 608,820 h | 20.9 h | **2.09×** |
| **M — the arithmetic maximum** | 700,800 h | 24.0 h | **2.40×** |

**The figure to quote is still about 1.6×, and 2.4× is still the wall nobody reaches.**

### 4.3 Why this is the result the project wanted anyway

**The comparison against money survives, and it is the comparison `Aequitas_Foundations.md` §4.6 was already making.** That section's demand-lever table sets money's top tail at about **10⁶ ×** the median against the ceiling's **2.4×**, and it is arguing about **who gets to say what is made** — not about who eats more.

| What is being compared | Money | Aequitas |
|---|--:|--:|
| **The say over what gets made** | ~10⁶ × the median | **2.40× at `F` = 10, and nobody reaches it** |
| **Material consumption** | ~670 × the median | **No bound.** §5 measures the range instead |

**And every living person holds some of it**, because staying alive is credited work, which is what OP-1 already calls the universal basic voice.

### 4.4 The conditions on it

**The four in `Aequitas_Foundations.md` §5.5.5 carry over unchanged**, and a fifth is added because the whole result rests on it.

| # | The condition |
|---|---|
| 1 | **The value of `F`.** The ceiling **is** `24 ÷ F`, so a 2-hour floor states a 12× ceiling |
| 2 | **Whether the network credits a child's learning time.** Credit none and nobody can exceed 2.085× |
| 3 | **No fraud manufactures hours.** IC-7 caps a day at 24 hours; collusive hand-offs could still inflate gross hours. **This condition binds harder here than it ever did over consumption**, because manufacturing hours is exactly what OP-1 (service → influence) is about |
| 4 | **It is a statement about one network's books.** Nothing else |
| **5** | **Receiving room must never raise a pledge budget.** If it did, `P` would re-enter and the bound would fail the same way the consumption claim did |

**⚠️ The rewrite cascades widely and none of it is done.** `24 ÷ F` appears **22 times in `Aequitas_Foundations.md`**, 12 times in `01-wiki/disparity-ceiling.md`, 8 in `Aequitas_Objections.md`, 6 in `Aequitas_Simulation_Roadmap.md`, 6 in `OP-22_identity_not_disclosure.md`, 4 in `Aequitas_Strategy.md`, 3 in `Aequitas_Overview.md` and 2 in `OP-9_calculation_reply.md`. **Each has to be read to see whether it means consumption or say.** `06-simulation/disparity-ceiling/` tests the arithmetic, which is unchanged, so the simulation stands and its framing does not.

---

## 5. How large pledge-wealth gets

**Three cases, all at `F` = 10 h/day and ρ = 1.2.** A life spent only staying alive earns 292,000 hours over 80 years, which gives 350,400 hours of room. The hardest possible life earns 700,800 hours, which gives 840,960 hours of room.

| The recipient | Pledged room `P` | Their total room | Against a life spent only staying alive |
|---|--:|--:|--:|
| **A local figure.** 200 people each pledge 500 h across their lives | 100,000 h | 450,400 h | **1.29×** |
| **A much-liked artist.** 5,000 likes a week for 50 years, routed at 0.1 h a like | 1,300,000 h | 1,650,400 h | **4.71×** |
| **A devotional case.** One person receives 1% of a million-subscriber network's whole lifetime pledging | 2,920,000,000 h | 2,920,350,400 h | **8,333×** |

**Read the three rows together.** Ordinary popularity buys a few times a floor-only life. Extreme devotion buys thousands of times it. **The system does not prevent the third row, and the documents should say so.**

**For scale:** money's top tail reaches about **1,000,000×** the median, and material consumption among today's wealthiest reaches about **670×** the median. The second row sits far below both. The third row does not.

---

## 6. Why this is not profit

**Five differences. The fifth is the one that decides it.**

**1. It is given, not taken.** A profit is a margin added to what a thing took, paid by a buyer who had no other option. A pledge is a deliberate act by one person, spending a thing they can never get back.

**2. It cannot be advertised into existence.** A seller can make somebody want a thing. A seller cannot put hours into somebody else's day, and a pledge is backed by hours the pledger worked.

**3. Its total is bounded by the work society actually did.** Every hour of room in the network stands behind an hour somebody really lived and really worked. Money has no such bound; it is issued.

**4. It is public.** Pledges are visible in the books, and so is who received them. A person's wealth from pledges is readable. A person's wealth from margin is not.

**5. It is not a machine for getting more.** This is the decisive one.

> **Property under capitalism is a machine: you own, so you rent, lend and charge, so you own more.** Pledged room does none of that. It is a one-time grant that lets you hold and consume. **It cannot be lent at interest, rented out, charged for, or used to hire anybody.**

**The reasons are already in the system and need no new rule.** Credit never moves, so a rich recipient cannot pay wages. Nothing may be added to a cost figure, so they cannot take a margin. Working on your own property raises that property's debit by the same hours it credits you, so holding things never gets you ahead.

### An example, with the numbers

**Two people hold a 500,000-hour building.**

| | How they got the room | What they can do with the building |
|---|---|---|
| **A landlord today** | Bought it with money | **Charge rent.** The building earns without them working, and the earnings buy another building |
| **A pledge-wealthy person** | 500,000 h of room granted by 5,000 admirers | **Live in it.** Repairs credit their hours and raise the building's debit by the same hours, so the net is zero. Nobody can be charged for standing in it, because there is no price and no margin |

**The first is an engine. The second is a house.**

---

## 7. What it costs — two attacks, and one withdrawn

**Neither live attack is answered here. They are what a stress test has to work on.**

### 7.1 A pledge costs the pledger time, and cannot be manufactured

**Author ruling, 2026-09-18. The attack is a restatement of an accepted property, not a hole.**

**The claim was that a pledge costs the pledger nothing, so a lifetime budget can be donated free.** The marginal act is indeed costless to the pledger's own consumption. **The budget is not.**

> **A pledge budget equals credit the pledger earned, and credit is time they lived.** IC-7 caps an account at 24 hours of activity in 24 hours, so **nobody can manufacture budget.** To hand somebody a million hours of room you need real, verified humans who each lived a life.

**So the exploit is real as concentration and impossible as creation.** And concentration bounded by the number of willing humans is exactly what §4 already states: *the only limit on `P` is the population.* **Ruling 1 accepted that, and §5 measures it.**

### 7.2 Coercion is the legal system's problem

**Author ruling, 2026-09-18. Beyond the scope of Aequitas.**

**This is the §2.6 move, and `Aequitas_Foundations.md` §4.7 already makes it:** *"it does not replace existing recourse. Courts, small claims, contract law and ordinary social pressure continue to exist and continue to handle fraud between people."* **The accounting is identical whether or not coercion is prevented, so it is not foundational.**

> **⚠️ One asymmetry to state rather than bury.** A coerced money payment can be clawed back by a court. **A coerced pledge cannot be, by this system.** §4.7 says fraudulent credits are negated but *"the pledges themselves are permanent and the work they summoned really happened, so nothing unwinds."*
>
> **So a court can punish the coercer and cannot restore the room.** That is a narrower remedy than money offers, and the documents should say so rather than leaving a reader to find it.

### 7.3 The dynasty attack does not re-open

**This paper raised the dynasty attack at 0.1 and withdraws it here. Two rules already stop it, and they are not the rule `Aequitas_Foundations.md` §5.5.7 cites.**

**1. Room does not raise your pledge budget.** A person's lifetime pledge budget equals the credit **they earned**, and nothing else (Conformance row 9). **Receiving a million hours of room lets you consume. It does not let you pledge one extra hour.** So a dynasty cannot compound: every generation can pass forward at most its own earned credit, which IC-7 caps at 24 hours a day.

**2. Room is not transferable once allocated.** It sits on a named account and there is no event that moves it. **On death it does not pass to anybody.** Heirs take the material things, and they must carry those things against **their own** room under the ordinary possession rule.

#### An example, with the numbers

**`F` = 10 h/day. Every person lives 80 years at the floor, so each earns 292,000 hours of credit and holds a 292,000-hour pledge budget.**

| Generation | Room it receives from two parents | Its own pledge budget | What it can pass on |
|---|--:|--:|--:|
| **1** | 584,000 h | 292,000 h | 292,000 h |
| **2** | 584,000 h | 292,000 h | 292,000 h |
| **3** | 584,000 h | 292,000 h | 292,000 h |

**The column does not grow.** Compare money at a 3% real return: 584,000 becomes about **1,418,000** over the same 30 years, and then keeps going.

> **`Aequitas_Foundations.md` §5.5.7's recorded answer is about debit dilution, and that part is untouched by this ruling.** The two rules above are additional, and they are what stop the room.

---

## 8. The contingent reserve is withdrawn, and becomes one example of a general rule

**Author ruling, 2026-09-18. The reserve is a trust network's ruling, not this system's.** `Aequitas_Foundations.md` §4.6 withdraws its own version and keeps the case **only as an example of the kind of thing a network decides.**

### 8.1 The general rule it collapses into

> **A pledge names a recipient, or names the criteria under which a recipient will be named.**
>
> **Until a person is named, the pledge is uncommitted and grants no room.**
> **Once a person is named, the room is committed, consumable, and unchangeable.**

**Awarding criteria may be any conditional thing.** The reserve was one such condition — *award this to whoever bears a harm this task causes* — written into Foundations as though it were the only one.

**And the criteria decide who is named, which need not be the injured party.** The author's case: **for harm mitigation the pledge may commit to the mitigator rather than to the victim.** Whoever writes the criteria decides.

### 8.2 What withdrawing it removes

**Five pieces of machinery in `Aequitas_Foundations.md` §4.6 and `01-wiki/pledge-and-signal.md` stop being foundational.**

| | Now |
|---|---|
| The surplus is non-consumable | **Gone.** Committed room is consumable, whatever named it |
| Shares split pro-rata by hours on that task | **The default where criteria are silent** (§3.1), not a rule about reserves |
| Causation decided by the physical-trace test | **A criterion a network may write**, not a rule this system imposes |
| Diffuse harm handled by a cohort convention | **The same** |
| Buffer-not-shield: overflow reverts to the causer | **The same.** It is a condition, and a network that wants it writes it |

> **This is the §2.6 dial test passing.** The accounting is identical whether or not a network runs a reserve. **So it was never foundational.**

### 8.3 An example, with the numbers

**A toxic cleanup. 200 people pledge 50 hours each.** The pledge carries criteria, published before anyone pledged.

| | Hours |
|---|--:|
| Pledged in total | 10,000 |
| Criteria: *the task's own cost, to whoever does it, by hours worked* | 6,000 |
| Criteria: *the rest, to whoever mitigates any harm this task causes within 30 years* | 4,000 |

| When | What happens | Whose gate |
|---|---|---|
| **Year 1** | Three workers do the cleanup, 2,000 h each | **6,000 h committed**, 2,000 each. Consumable and unchangeable |
| **Year 12** | A worker falls ill. A clinic treats them | **4,000 h commits to the clinic's staff** — the mitigator, not the victim |
| **Year 30, no harm** | Nothing triggered the second criterion | **Nobody's, ever.** It lapses, and the 200 budgets were spent on day one |

**The pledgers spent 10,000 hours of budget in every branch.** What varies is who ends up named.

### 8.4 Discretionary criteria are how a prize works

**Author ruling, 2026-09-18. This is fine, and the documents already have the example.**

**`Aequitas_Foundations.md` §4.6:** *"A prize for solving a hard problem needs no billionaire patron; a large enough pool of pledges is the prize."* **`01-wiki/pledge-and-signal.md` says the same** — *"an X-Prize needs no oligarch or patron."*

> **A panel of judges deciding who solved the problem is a conditional thing, and it is the whole mechanism.** Many people pledge toward a stated technical or scientific achievement. **A panel names the winner. The room commits to them and becomes unchangeable.**

**Take the panel away and the prize cannot exist**, because nobody can write objective criteria in advance for *"solved a problem nobody has solved."*

#### The one containment, and it is not new

> **Criteria must be published before the pledge is made.** §4.2 already requires a network to publish its evidence rules before anyone joins, and A8 already requires it to publish what it runs.

**A pledger choosing a prize fund is choosing a published panel.** A fund that announces criteria, collects pledges and then changes them is visible, because pledge ledgers are public (§4.7), **and it stops attracting pledges.** That is the ordinary discipline and needs no new rule.

**⚠️ What stays registered is the scale of it.** A very large fund with discretionary published criteria is a coordinator with real power over who may consume. **That is P4 (coordinator class), the live blocker** — a new surface, not a new problem.

**And it does not touch §7's two live attacks.** A pledge still costs the pledger nothing material, and coercion still buys material riches.

---

## 9. What must change in the documents

**Nothing has been edited yet. The work sorts into four jobs, and the fourth is much larger than the other three together.**

### Job 1 — the gate

| File | What is wrong |
|---|---|
| `00-strategy/Aequitas_Conformance.md`, the gate definition | States `D ≤ ρ·C`. Needs the `P` term |
| `00-strategy/Aequitas_Foundations.md` §3.0 | Same gate, same fix |
| `00-strategy/Aequitas_Foundations.md` §3.0, the worked example | Two ledgers shown with no `P` column |

### Job 2 — what a pledge names

| File | What is wrong |
|---|---|
| `00-strategy/Aequitas_Foundations.md` §4.6, the pledge table | A pledge must be stated as naming a recipient |
| `00-strategy/Aequitas_Foundations.md` §4.6 | **New: uncommitted until distributed**, and distribution by hours worked (§3.1 above) |
| `00-strategy/Aequitas_Conformance.md` row 9 | Unchanged in substance. **Check that IC-9 still reads correctly** against an uncommitted pledge |

### Job 3 — the contingent reserve

**Withdrawn from Foundations and kept only as a worked example of a network ruling** (§8).

| File | What is wrong |
|---|---|
| `00-strategy/Aequitas_Foundations.md` §4.6, the reserve | **Five pieces of machinery stop being foundational.** Replace with the general rule: a pledge names a recipient **or criteria**, and criteria must be published before the pledge |
| `01-wiki/pledge-and-signal.md` | Two whole sections, and "Nobody is paid a bonus for being liked" |
<!-- struck-ok: this paper must quote the withdrawn wordings in order to record that they were withdrawn -->
| `00-strategy/Aequitas_Overview.md` §6 | "Nobody gets a bonus for being popular" and "The leftover does not become spending money" |
| `06-simulation/statera/statera.py`, `room()` | The granted offset is capped at a creation-cost and is non-spendable |
| `06-simulation/pledge-reserve/pledge_reserve.py` | Tests a mechanism that is now one example among many, not a rule |
| `00-strategy/Aequitas_Objections.md`, **OP-16** | The hazard half was answered *by the reserve*. **It is now answered by criteria a network may write**, and the tedium half is reachable for the first time, because a pledge can simply name whoever does dull work |

### Job 4 — withdrawing the disparity ceiling

**This is the large one.** The ceiling is quoted as a headline result across the whole project.

| File | Mentions |
|---|--:|
| `00-strategy/Aequitas_Foundations.md` — §0, §4.6, §5.5.5, §5.5.6, §5.5.7, §5.5.8 | **22** |
| `01-wiki/disparity-ceiling.md` | 12 |
| `00-strategy/Aequitas_Objections.md` | 8 |
| `00-strategy/Aequitas_Simulation_Roadmap.md` | 6 |
| `00-strategy/open-problems/OP-22_identity_not_disclosure.md` | 6 |
| `00-strategy/Aequitas_Strategy.md` | 4 |
| `00-strategy/Aequitas_Overview.md` — §1, §6 | 3 |
| `00-strategy/open-problems/OP-9_calculation_reply.md` | 2 |
| `01-wiki/honest-advantage.md`, `debit-tolerance.md`, `index.md`, `verification-ladder.md` | 5 |
| `00-strategy/GLOSSARY.md`, `Aequitas_Question_Index.md` | 3 |
| **`06-simulation/disparity-ceiling/`** | **A whole folder built to test it** |

**`00-strategy/STRUCK_PHRASES.md` needs the withdrawn wordings adding**, so `bin/consistency.py` check 3 catches any that survive.

**`00-strategy/Aequitas_Objections.md`** — OP-1, OP-6 and OP-16 all move, and the demand-lever argument in OP-9 keeps its number under §4.3's restatement.

### Job 5 — two further rulings, added at 0.4

| File | What is wrong |
|---|---|
| `00-strategy/Aequitas_Foundations.md` §5.5.7 | **The household attack's stated reason fails.** It says dwelling debit splits per occupant *"children included"*, and a child cannot consent to a transfer. **The conclusion survives; the reason does not.** §13.1 |
| `00-strategy/Aequitas_Foundations.md` §5.5.3 | The band is computed in published ρ with no pledge term. **The publishable upper edge halves.** §14.1 |
| `06-simulation/stable-band/` | The sweep needs re-running with a pledge term |
| `00-strategy/Aequitas_Foundations.md` §4.6 | **Self-pledging is permitted.** The rule to state is person-pledge against work-pledge, not self against other. §11 |
| `00-strategy/Aequitas_Foundations.md` §2.6, the settings table | **Two new rows.** Who may consent to a property transfer, and how a service's cost is attributed. §13.1, §15 |
| `00-strategy/Aequitas_Foundations.md` §3.0, §4.4, §5.5.3, §5.5.5, §5.5.6 | The **1,380 h/yr** anchor is used as a fact about the world. **It is one defensible reading**, like `F` = 10. §15.3 |
| `06-simulation/median-lifestyle/track1_embodied_hours.py` | **Extract healthcare's share of the anchor.** It is named as the largest component and is not published as a figure |

> **Author placement instruction, 2026-09-18.** **Foundations gets a few sentences on inflation and a pointer.** The full discussion lives in [`../../02-research/Problem_pledge-inflation.md`](../../02-research/Problem_pledge-inflation.md) and must not be duplicated into a core document.

---

## 10. Tests against the three criteria

| Criterion | Result |
|---|---|
| **Universality** | **Improved.** The ruling removes a rule rather than adding one: nothing now says what a pledge may name. Withdrawing the contingent reserve removes a second. **Ruling 3 adds one back** — a pledge naming no individual behaves differently from one that does — **but it adds no exception**, because the difference is when the room appears rather than what the rule is |
| **Decentralization** | **Unchanged.** Pledges are public and backing is one for one, checkable by anyone. Proving backing across two networks' weighting models is OP-22, which was already open |
| **Fecundity** | **Unchanged.** A pledge is a record and needs no maintainer |
| **Who games this?** | **Two attacks, neither answered.** §7.1 and §7.2. **The dynasty attack is withdrawn** — §7.3 |
| **Does this need a Paul Glover?** | **No** |
| **Does this need an objective function?** | **Not as proposed, and it would if distribution were discretionary.** §3.1 is where that is decided |

### The axiom question, withdrawn

**This paper flagged pledged room at 0.1 as *"the closest thing this system has to a currency"* and called it the finding a stress test must attack first. The author ruled that wording rather than substance, and the project's own definition of a currency settles it.**

**`Aequitas_Overview.md` Appendix A defines a currency by five properties. Room fails every one.**

| A currency… | Pledged room |
|---|---|
| carries almost no information | **Carries all of it.** Who pledged, when, under what criteria — public (§4.7) |
| belongs to nobody in particular | **Belongs to exactly one named account** |
| fluctuates | **Does not.** It is a count of hours |
| depends on an issuer | **No issuer.** Backed one for one by hours somebody lived |
| stands for something redeemable | **Stands for nothing.** It cannot be cashed, lent, or traded back |

**The second flag goes with it.** §13.4 said room is the only quantity §3.3 cannot re-weight. **Credit cannot be re-weighted either**, because re-weighting converts physical quantities into hours and hours are the unit it converts into. **Room is in the same position as credit, not a special one.**

> **A1 and A3 are not strained.** No credit moves, no issued quantity appears, and nothing is redeemable. **The flag is withdrawn.**

## 11. Can a person pledge to themselves?

> **No axiom forbids it, and no axiom distinguishes it from any other pledge. This paper recommends allowing it.**

### 11.1 A credit and a pledge are two records, not one

**A pledge is generated by a credit and is not the same thing as one.** A credit records an hour a person spent. **A pledge records a separate act: a person committing part of their budget.** Two events, two records.

**So the ledger tally is three columns and one subtraction.**

> **Count the credits. Count the committed pledges received. Then subtract the debits.** What is left is the room.

**`D ≤ ρ·(C + P)` is that sentence written out.** A self-pledge lands in the `P` column like any other, **so it does grant room.**

> *(This paper argued at 0.3 that a self-pledge was null, on the ground that §3.4a's union rule counts an hour reached by two paths once. **That was a category error.** The union rule governs **parcels** — identified matter and energy, where two co-products can point at the same 100 MJ. **A pledge is not a parcel**, so the rule does not reach it.)*

### 11.2 Running it against the axioms

| Axiom | Does a self-pledge breach it? |
|---|---|
| **A1** (materialism of cost) | **No.** The room is backed one for one by real credit, exactly as any pledge is |
| **A2** (time as measure) | **No.** Everyone's budget is their own earned credit, so the capacity is proportional to hours and scales nobody's hour above anybody else's |
| **A3** (non-fungibility) | **No.** No credit moves. It does not even leave the account |
| **A5** (cost, not price) | **No.** Nothing is added to any thing's cost figure |
| **A8** (no governing body) | **No**, provided the network publishes the setting |

> **And no axiom tells a self-pledge apart from any other pledge.** Both spend one hour of budget and create one hour of committed room. **Both add exactly 1 to the network's `P` total.** Barring one and not the other would be an exception with no axiom behind it, which is what the universality test refuses.

### 11.3 The real division is not self against other. It is person against work

**Three destinations, and they behave differently for reasons that have nothing to do with who the pledger is.**

| Where the pledge goes | When the room appears | Does it summon work? | Does it concentrate? |
|---|---|---|---|
| **To yourself** | At once | **No** | **No** |
| **To another named person** | At once | **No** | **Yes** |
| **To a fund, cause or task** | **Only as the work is done and distributed** (§3.1) | **Yes** | **No** — it distributes by hours worked |

> **Only the third ties room to output.** A self-pledge and a person-pledge both create room without calling any work into being. **A self-pledge is simply a person-pledge aimed at the pledger**, and it is the one that concentrates nothing.

### 11.4 Consent is the limit, and it does real work

> **A pledge is a deliberate act and requires the capacity to consent. It is never automatic.**

**Two things follow.**

**An infant cannot pledge.** A newborn accrues a pledge budget from its first day, because staying alive is credited work, **and it cannot spend a single hour of it until it can consent.** §13.1 works the arithmetic through.

**And "everybody self-pledges everything" is a behavioural prediction, not a mechanism.** Pledging is something people choose. §14 is the case where they choose otherwise.

> *(This paper claimed at 0.3 that the rational move is to self-pledge the whole budget on day one and that the demand side would go to zero. **A newborn cannot pledge at all**, and the claim treated a choice as automatic.)*

---

## 12. Is the pledge system inflationary?

> **Yes, by a factor of exactly 2. It cannot produce a price spiral, because there are no prices.**

**The full working is in [`../../02-research/Problem_pledge-inflation.md`](../../02-research/Problem_pledge-inflation.md).** This is the summary.

**The size.** Backing is one hour pledged per hour earned, so `P_total ≤ C_total` and total room reaches at most `2·ρ·C_total`. **The factor is 2 at every value of ρ**, because ρ multiplies both halves.

**Why the usual consequence cannot follow.** Money inflation needs three parts: more claims, the same goods, and a seller who raises the number. **The third is absent.** A5 (cost, not price) makes a figure what a thing consumed, **and you cannot mark up a measurement.** So there is no price for surplus room to bid on.

**What happens instead.** The gate goes slack and rationing moves to the point of distribution — a queue, a lottery, or pledge-priority. **That is a change of mechanism, not a spiral**, because room is granted once and is never re-lent.

**Whether that is good.** `Aequitas_Foundations.md` §5.5.3 already states both halves: a non-binding gate is *"abundance and it is the intended end state"* where the economy can deliver, and *"the accounting has stopped doing the work it was set up to do"* where it cannot. **The pledge system does not change which one a network is in.**

**⚠️ The gap it opens is in §5.5.3's band**, which was computed in published ρ with no pledge term. **A network publishing ρ = 1.2 can run at an effective 2.4, against a measured `ρ*` of 1.20.** §14.1 works the consequence through.

---

## 13. What happens when the population grows or shrinks?

**The two directions are not symmetric, and shrinkage is the dangerous one.**

### 13.1 Growth: a child carries no debit at all

**A newborn accrues credit from its first day**, because staying alive is credited work. **It accrues no debit**, and the documents already said so.

#### The rule was already written

> **`Aequitas_Foundations.md` §4.6, on a pledged verge-mowing: *"No object changed hands and no debit moved."***

**A service moves no debit.** A1 makes a debit a record of a **material or energy flow**, and hours of care are not a flow onto the person cared for. **§2.4 says a hand-off of a physical thing is *"the only kind of sale there is."*** So the carer is credited and nobody is debited.

> *(This paper said at 0.4 that the baby *"is the party the service was done for, so the baby carries the debit."* **That was invented.** It is the sixth time in this project that the answer was already in the documents and unread.)*

**The author's own statement of it: this is the floor's structure repeated.** A person is credited for maintaining themselves and no debit is generated. **A carer maintaining a child is the same accounting with a different pair of hands.**

#### Three things an infant does not carry

| | Why |
|---|---|
| **Debit for the care it receives** | **A service moves no debit** (§4.6, A1) |
| **Debit for food, clothing and medicine** | **It cannot consent to a property transfer.** §2.4 rule 2 says nobody can be made to receive anything, so the goods stay with the guardian who accepted them |
| **A usable pledge budget** | A pledge requires consent (§11.4). The budget accrues and cannot be spent |

> **Who may consent to a property transfer is a trust network's decision.** Author ruling, 2026-09-18. **It belongs in `Aequitas_Foundations.md` §2.6's list of settings that vary**, beside `F`, ρ, the privacy practice and the verification rung. It is not fixed here and must not be.

#### What a child does add, and it lands on the guardians

**A child carries no debit. It still causes real material consumption — extra food, clothing, heating, transport and a larger dwelling — and every hour of that sits on the adults who accepted the goods.**

**The size of it, from a published scale.** The [OECD-modified equivalence scale](https://www.oecd.org/content/dam/oecd/en/data/datasets/income-and-wealth-distribution-databases/idd-tor-2012-onwards.pdf) weights a household at **1.0 for the first adult, 0.5 for each further person aged 14 or over, and 0.3 for each child aged 0–13** ([Equivalisation](https://en.wikipedia.org/wiki/Equivalisation); [ONS, Chapter 3](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/compendium/familyspending/2015/chapter3equivalisedincome)).

| | Equivalence units | Household consumption at 1,380 h per adult |
|---|--:|--:|
| Two adults | 1.5 | 2,760 h/yr |
| **Two adults and one child** | **1.8** | **3,312 h/yr** |
| **What the child adds** | **0.3** | **552 h/yr**, about 276 h on each guardian |

**And the guardians' dwelling share goes *up*, not down.** Under §4.5 a dwelling's creation-cost splits by holding time. **A child holds nothing, so it dilutes nothing.**

**Worked on §4.5's own 500,000-hour house.** Two adults hold it 40 years each; a child would have held it 18.

| | Total holding time | Each adult's permanent share |
|---|--:|--:|
| The withdrawn §5.5.7 rule, children included | 98 years | 40 ÷ 98 = **204,082 h** |
| **The consent rule** | 80 years | 50% = **250,000 h** |
| **What ruling 8 costs each adult** | | **about +46,000 h** |

#### An example, with the numbers

**`F` = 10 h/day, ρ = 1.2. One infant, one carer giving 8 hours a day, two guardians.**

| | Credit | Debit | Room added, `ρ·C` |
|---|--:|--:|--:|
| **The child** — floor only | 3,650 | **0** | **+4,380** |
| **The carer** — credited for 2,920 h of childcare | 2,920 | 0 | **+3,504** |
| **The guardians** — the child's material consumption | — | **552** | — |
| **The household, net** | | | **+7,884 room against 552 h of debit** |

**A child is still a strong net room-adder.** The guardians' 552 hours do not come close to offsetting it.

> **⚠️ Read +7,884 as a ceiling, not a value** (conformance row 13). **It assumes the carer's 2,920 hours are credit the household would not otherwise have earned.** A carer who would have been credited for other work instead is substituting, not adding, and the true figure is lower by however much they substituted. **Nobody has measured the substitution rate.**

*(This paper used an invented figure of ≈500 h at 0.5. The 552 h above is derived from a published scale and can be checked.)*

#### What the 552 hours does and does not contain

**The scale is built from money a household spends. So it contains purchased care and excludes unpaid care.**

| | In the 0.3 weight? | What Aequitas does with it |
|---|---|---|
| **A parent caring at home, unpaid** | **No.** Unpaid domestic labour is outside expenditure data by construction | **Credited to the parent, debits nobody** (ruling 7). This is the labour §4.5 calls *"the largest uncounted labour pool in human history"* |
| **Purchased daycare** | **Yes.** It is an expenditure | **The worker is credited. The care debits nobody.** Only the centre's materials and energy land anywhere |
| **Schooling** | **Yes**, through fees and through taxes | **Front-loaded** (§4.5). Education is carried where it happens and never charged onward |

> **So 552 h/yr is an upper bound on the guardians' Aequitas debit, not the figure.** Two of the three rows lose their labour component when they cross into this system.

**How much comes off is measurable and nobody has measured it.** `06-simulation/median-lifestyle/TRACK1.md` puts **education at 31 h per capita** and **healthcare at 131** against a **612 h** domestic total. **The share of a *child's* marginal basket that is care and schooling is higher than either**, and it is not published. **`track1_by_category.py` already builds a consumer-expenditure category bridge**, which is where the figure would come from.

#### What crediting childcare balances, and what it does not

**It balances the household's room**, which the table above already shows: the carer's 2,920 credited hours become 3,504 hours of room.

> **⚠️ It does not balance deployable labour, and reading it that way would repeat a withdrawn claim.**

**`06-simulation/scenario-suite/Q1B_DEPLOYABLE_LABOUR.md` deliberately counts deployable hours** — working-age share × participation × hours per worker — **and not credited hours.** The reason is in `Aequitas_Foundations.md` §3.5: the earlier comparison used credited labour, which includes the floor, and *"sleeping is credited work under §2.3, and it cannot lay cable."*

**A parent caring for a child cannot lay cable either.** So Q1B's finding stands untouched: **deployable hours reach 0.43–0.87 of what a median US lifestyle commands, and never cross 1.0 at US production efficiency.**

> **Crediting childcare adds credit and room. It adds no deployable hours and no goods.**

> **The anchor's own construction already agrees with ruling 8.** `06-simulation/median-lifestyle/RESULTS.md` reports Track 1 as **612 h per capita** and **772 h per adult**, a ratio of about the adult population share. **Dividing a population total by adults alone loads children's consumption onto adults**, which is exactly what the consent rule requires. **No recomputation is needed for that part.**

> **This is the design, not a fault, and §3.5 already governs it.** *"Aggregate debit therefore exceeds aggregate credit permanently and by construction"* on the material side, while **credited care and the floor add credit with no matching debit.** §4.5 states the intent plainly: crediting childcare *"brings the largest uncounted labour pool in human history onto the books."*
>
> **The instrument that answers it is ρ**, and §13.3 is why ρ has to multiply the whole gate. **A network with many children sets ρ lower.** Nobody has measured how much lower.

#### The correction §5.5.7 needs

<!-- struck-ok: this paper must quote the withdrawn wordings in order to record that they were withdrawn -->
**`Aequitas_Foundations.md` §5.5.7 answers the household attack this way:** *"a household is a co-op; its dwelling debit splits per occupant by dwelling time, **children included**, so the bound is per person and inheritance dilutes it."*

> **Children are not included, so that reason fails. The adults carry the whole dwelling.**

**The conclusion survives on other grounds** — §7.3's two rules, that room does not raise a pledge budget and that room is not transferable once allocated. **Neither depends on the dwelling split.** §5.5.7 needs the reason replaced, not the verdict.

### 13.2 Shrinkage: the room stays and the worker does not

**A pledge is permanent and non-revocable.** `Aequitas_Foundations.md` §4.6 says so, and §4.8 says a person's record closes on death but persists. **Neither death nor departure revokes room already granted to somebody else.**

> **So committed room outlives the people who backed it, and production capacity does not.**

#### An example, with the numbers

**A network of 1,000,000 halves to 500,000 over fifty years.** Each departing subscriber granted about 292,000 hours over a life, and half of it landed on people still alive.

| | |
|---|--:|
| Room granted by the departed, still sitting on survivors | **7.3 × 10¹⁰ h** |
| Per surviving subscriber | **146,000 h** |
| Their own floor credit at 40 | 146,000 h |
| **So `P` now roughly equals `C` for the average survivor** | — |
| Production capacity, against fifty years earlier | **halved** |

### 13.3 The dial is ρ, and it only works under one form of the gate

**`Aequitas_Foundations.md` §5.5.7 already found that ρ is the adjusting instrument:** *"ρ behaves like a prime rate. A ρ can be chosen so that aggregate demand matches productive capacity, and it moves sensibly under shocks."* A −30% capacity disaster tightens it to about 0.68.

**Whether that instrument reaches the pledged half of the gate depends entirely on where ρ sits.**

| The gate | Halving ρ from 1.2 to 0.6 does what? |
|---|---|
| **`ρ·(C + P)`** — this paper's form | **Halves total room.** The dial reaches everything |
| `ρ·C + P` — the 0.2 form | **Leaves 146,000 h of `P` per survivor untouched.** Setting ρ to zero still leaves `D ≤ P` |

> **That is the strongest argument for `ρ·(C + P)`, and it is the reason §3 changed.** A shrinking network under the other form has no working dial.

### 13.4 One property worth naming

**Pledged room is the only quantity in this system that §3.3 cannot re-weight.** Retroactive re-weighting works on physical quantities — kilograms, joules, litres — converting them to hours at today's science. **Room is already in hours, so there is no reading to improve and nothing to re-weigh.**

**This is a fourth way it behaves like a currency**, alongside the three §10 names. **It is registered here and not answered.**

---

## 14. ρ below 1, and what scarcity does to pledging

### 14.1 ρ below 1 is already explored, and it becomes the normal setting

**`06-simulation/stable-band/RESULTS.md` swept the workable band and most of it sits below 1.**

| `F` | The measured band in ρ |
|---|---|
| 2 | ρ ∈ [0.60, 3.70] |
| 6 | ρ ∈ [0.20, 1.75] |
| **10** | **ρ ∈ [0.20, 1.20]** |
| 14 | **ρ ∈ [0.20, 0.90]** — entirely below 1 |

**And `Aequitas_Foundations.md` §5.5.7 already moves ρ below 1 under stress:** a −30% capacity disaster tightens the clearing rate from about 1.20 to about **0.68**.

> **Pledges make ρ below 1 the ordinary published setting rather than a stress case.**

**The reason is §12.1.** Committed pledges can double the gate, so a network's **effective** tolerance runs up to `2ρ`. To stay inside a measured upper edge of 1.20 at `F` = 10, the **published** ρ must sit at **0.60 or below.**

| At `F` = 10 | Upper edge |
|---|--:|
| The band as measured, in effective tolerance | **1.20** |
| **The band a network must publish, once pledges are counted** | **0.60** |

**So the publishable band at `F` = 10 is about ρ ∈ [0.26, 0.60], and every value in it is below 1.**

#### Measured, 2026-09-18

**It was run.** `06-simulation/stable-band/pledge_band.py`, 5 self-tests green, written up in [`../../06-simulation/stable-band/PLEDGE_BAND_RESULTS.md`](../../06-simulation/stable-band/PLEDGE_BAND_RESULTS.md).

**Write `P` = `p`·`C`, where `p` is the pledge density — the share of the population's lifetime budget committed to somebody. Then the gate is `D ≤ ρ·(1 + p)·C`**, so the publishable upper edge is `ρ*(F) ÷ (1 + p)`. **The original sweep ran with no pledges, so its ρ is the effective tolerance.** No kernel change was needed.

| `F` | p = 0 | p = 0.25 | p = 0.50 | p = 0.75 | p = 1.00 |
|---|--:|--:|--:|--:|--:|
| 2.0 | 3.70 | 2.96 | 2.47 | 2.11 | **1.85** |
| **10.0** | **1.20** | **0.96** | **0.80** | **0.69** | **0.60** |
| 14.0 | 0.90 | 0.72 | 0.60 | 0.51 | **0.45** |

> **ρ*(10) = 1.20 and the documented setting is ρ = 1.2. Those are the same number.** So the documented setting sits **exactly at** the publishable edge at `p` = 0 and **above it for every `p` > 0.** Any pledging at all puts it out of band.

**The two edges do not see `p` alike, and that is the substance.** The upper edge is an aggregate question, so the population's `p` belongs in it. **The lower edge must hold for somebody nobody pledged to, so it is read at `p` = 0 and does not move.** Reading it at the population's `p` would make essentials look affordable because *other* people were given room — the flattering direction §4.4 warns about.

> **⚠️ And `RESULTS.md`'s headline does not survive. The band closes.**
>
> | Essentials | `F` | `p` | Lower | Publishable upper |
> |---|--:|--:|--:|--:|
> | 70% of a median lifestyle | **1.0** | **0.75** | 2.647 | **2.286** |
> | 70% of a median lifestyle | **1.0** | **1.00** | 2.647 | **2.000** |
>
> **Two swept cells shut**, both at the tightest floor and the largest essentials basket. **Everywhere else it stays open at every density up to the ceiling.** So *"the band never closes"* becomes a near-miss with a condition on it, not a theorem.

**⚠️ `p` is swept and not measured.** It is behavioural, and no network exists.

### 14.2 Scarcity redirects pledges, and ruling 3 makes that self-correcting

**In a shortage, a blank cheque to a favourite competes with the pledger for the goods that are short.** So pledgers move away from it. **Two places they move to, and they behave differently.**

| Where the pledge moves | What happens to the gate |
|---|---|
| **To themselves** | Room appears at once. **It inflates and concentrates nothing.** The pledger keeps their own claim rather than handing it to somebody else |
| **To a cause that would fix the shortage** | **Room appears only as the remediation work is done and distributed to the people who did it** (§3.1) |

> **The second is the useful one, and it works because of ruling 3.** A cause-pledge is uncommitted until distributed. **So the room materialises at the same time as the output that relieves the shortage.** Room tracks goods instead of running ahead of them.

#### An example, with the numbers

**A network at `F` = 10 loses 30% of its capacity.** 100,000 subscribers each pledge 1,000 hours toward repairing it.

| | Hours | When it reaches a gate |
|---|--:|---|
| Pledged to the repair fund | 100,000,000 | **Never as a lump.** Uncommitted |
| Distributed in year 1, as 2,000 people work 2,000 h each | 4,000,000 | **Year 1**, on 2,000 named accounts |
| Distributed in year 2, same rate | 4,000,000 | Year 2 |
| **Still uncommitted after two years** | **92,000,000** | **Nobody's gate** |

**The pledgers' budgets were all spent on the day they pledged.** What did not arrive is the room.

> **This is the property the design has that a stimulus payment does not.** Money handed out in a shortage chases the goods that are short. **A cause-pledge cannot, because it is not room until somebody has done the work.**

**⚠️ Two things this does not fix.** A **person**-pledge and a **self**-pledge both create room at once, in a shortage as much as in plenty. **Whether people actually move away from them under scarcity is a behavioural claim and nobody has tested it.**

---

## 15. Who carries a service's cost is a network's rule, not this system's

**Author ruling, 2026-09-18.** **Aequitas does not write the rules of medical debt, and cannot.** Which treatments a person carries, how a network treats an unconscious accident victim, and who counts as a child are the network's to set and to change. **Adam Smith did not decide which treatments Blue Cross Blue Shield covers.**

### 15.1 The three places that already settle this

**The ruling is an application of machinery the documents already have. The case had not been worked; the rules had.**

| | What it fixes | What it leaves to the network |
|---|---|---|
| **A4** (no externalities) | **Coverage is absolute.** The flows a treatment consumed — the anaesthetic, the power, the surgeon's hours — are recorded, with no exception | **Attribution.** A consequence goes to whoever caused it. **"Where causation is not yet resolved, the consequence is recorded and held explicitly unassigned, until an attribution witness exists"** |
| **§4.7** | Three of the four kinds of dispute resolve by arithmetic or by each party re-computing | **A finding of fact needs a verdict**, and §4.7 already says a contested one *"routes to existing recourse."* **There is no adjudicator in Aequitas** |
| **§2.6** | The dial test: *"If a principle survives at both ends of a dial, the dial is not part of the principle"* | **The accounting is identical whether or not elective surgery debits the patient.** Conservation holds, the gate runs, the leftover rule runs. **So it is a dial** |

> **§2.6 already writes this sentence for another case:** *"Capitalism does not carry a data-protection chapter. Banks do."* **The ruling adds medicine to the same list.**

### 15.2 The author's three cases, run against A4

**A court verdict is an attribution witness.** §4.4 defines one as *"a record that binds a share of the leftover to a named principal"*, and a finding of fault is exactly that.

| The case | Causation | Where the flows sit |
|---|---|---|
| **Elective cosmetic surgery** | **Resolved.** The patient chose it | **The patient.** No network needs a rule to reach this |
| **Cancer nobody chose, treated by choice** | **Split, and culturally specific.** The disease was not chosen; the treatment was | **The network's rule decides**, and networks will differ |
| **An unconscious accident victim, no fault established** | **Unresolved** | **Held explicitly unassigned** under A4's third line, until a court or an investigation supplies a witness |

#### An example, with the numbers

**A rhinoplasty consumes 12 labour-hours** — 6 surgeon, 4 nursing, 2 anaesthetist — plus materials. **An emergency admission after an unattributed crash consumes 40.**

| | Hours | Whose ledger, at the moment of treatment |
|---|--:|---|
| The elective operation | 12 | **The patient's** |
| The emergency admission | 40 | **Nobody's.** Covered, recorded, held unassigned |
| The same 40, after a court finds a driver at fault | 40 | **The driver's.** The verdict was the witness |

**In all three rows the flows are inside the accounting.** What changes is whose name is on them.

### 15.3 What this does to the 1,380-hour anchor

**The anchor measures one thing and the documents use it as another.**

> **`06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md` measures the labour a median American lifestyle *commands*. How much of that lands on the individual's ledger is a network's attribution rule.**

**Those are two different numbers.** The measurement is robust — BLS employment requirements against the actual consumption mix. **The attributed share is a setting.**

**And healthcare is the largest single labour component in it**, by that document's own words: *"healthcare inverts it — moderate dollars, the most embodied labour, because care is people."* **Its share is not published as a figure**, and extracting it from `track1_embodied_hours.py` is the first job.

> **So 1,380 h/yr is one defensible reading, not the figure**, in the same way `F` = 10 h/day is one defensible floor. **`Aequitas_Foundations.md` uses it in §3.0, §4.4, §5.5.3, §5.5.5 and §5.5.6 as though it were a fact about the world.**

### 15.4 ⚠️ Three findings in this paper all push the same way

**None of them was looked for, and all three loosen the gate.**

| The finding | Where | What it does |
|---|---|---|
| Committed pledges can **double** the gate | §12 | Loosens |
| A child adds room and **no debit** | §13.1 | Loosens |
| Part of the anchor may not be **attributable** to the consumer | §15.3 | Loosens |

**`Aequitas_Foundations.md` §4.4 names this pattern and says it will not be caught from inside:** *"Whoever computes a figure of this shape benefits from a particular one of its two labels. The error is therefore not random, and it will not be caught by whoever made it."*

> **A looser gate makes this project's own affordability results read better.** That is the flattering direction, so **the correction has to come from a party the figures do not flatter.** Registered, not answered.

---
## 16. What is left before this folds

**All fourteen rulings are settled. Nothing is folded.**

| | Status |
|---|---|
| **The fourteen rulings** | **Settled by the author, 2026-09-18** |
| **§7's two attacks** | **Answered by rulings 12 and 13** |
| **The axiom flag** | **Withdrawn** by the project's own definition of a currency (§10) |
| **`06-simulation/stable-band/`** | **Re-run.** `pledge_band.py`, 5 self-tests green |
| **`06-simulation/statera/`** | **RETIRED 2026-09-18**, author ruling. Moved to `06-simulation/99-superseded/statera/` with a banner. **The one study that imported it, `stable-band/`, now runs `stable-band/gate.py`** — a minimal kernel on the current gate, 6 self-tests green. **All 27 floors of `ρ*` reproduce identically after the swap** |
| **The five document jobs in §9** | **Not started. This is all that is left.** |

> **`bin/consistency.py` cannot see the statera problem.** It checks links, versions, struck phrases, the distilled Foundations and `NEXT.md`. **It does not check whether a simulator agrees with the spec.**

---


*Depends on: `00-strategy/Aequitas_Foundations.md` A4, §2.4, §2.6, §3.4a, §4.4, §4.6, §4.7, §5.5.3, §5.5.5, §5.5.7 · `00-strategy/Aequitas_Conformance.md` row 9 · `01-wiki/pledge-and-signal.md` · `06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md` · `00-strategy/open-problems/OP-16_authorization_stress_test.md`*
