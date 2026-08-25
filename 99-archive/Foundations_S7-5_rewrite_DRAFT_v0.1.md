<!-- tag: s75-rewrite-draft -->
# Foundations §7.5 — rewrite, DRAFT

> **Version:** 0.1 · **Date:** 2026-08-25
> **What this is:** a replacement for **§7.5 of `Aequitas_Foundations_v0.22.md`**, written to the document standard set in v0.22 — state the rule, define every term where it is first used, show it working with numbers, stop.
> **This is a rewrite in substance, not only in style.** Author ruling, 2026-08-25. Four things changed. They are listed at the end, under *What this draft changed*.
> **It also carries the OP-22 ruling** of the same day: [`OP-22_identity_not_disclosure_v0.1.md`](OP-22_identity_not_disclosure_v0.1.md) §8a. The old condition 5 is struck.
> **Companion:** the §5 rewrite, [`Foundations_S5_rewrite_DRAFT_v0.1.md`](Foundations_S5_rewrite_DRAFT_v0.1.md).

---

<!-- tag: fnd-s7-5 -->
## 7.5 The basic-needs floor

### 7.5.1 What the floor is

**Terms used in this section.**

| Term | What it means |
|---|---|
| **The floor**, written `F` | The hours a day a trust network counts as the work of keeping a human being alive. |
| **Trust network** | The organisation that keeps the books and sets `F` for its own subscribers (§5.0). |
| **ρ** ("rho") | The network's debit tolerance. The multiplier in the consumption gate `D ≤ ρ·C` (§3.5). |
| **`C`** | A person's cumulative credit — the hours of their life the books have recorded as work. |
| **`D`** | A person's cumulative debit — the material and energy the books have recorded against them. |

> **The floor is credit for time a person spends on the activities their trust network counts as essential to staying alive.**

Those activities are **sleeping, eating, defecating, and keeping oneself clean.** A network may count more, or fewer, or hold them to shorter durations. **The list and the hours are the network's to set, and networks will differ.**

**That is why floors differ, and the differences are not arbitrary.** One network counts eight hours of sleep and lands near 10 h/day. Another accepts the argument that four hours of sleep suffices and lands near 6 h/day. A third counts sleep alone and lands near 8 h/day. **A fourth counts only the hours a body cannot avoid and lands near 2 h/day.**

**This is partly a question of opinion and partly a question of fact.** People disagree about how much sleep a human needs. **They are also disagreeing about a number that decides whether the network's economy is stable** — see §7.5.3.

---

### 7.5.2 The floor follows from the axioms. It is not an allowance

**The floor is not a grant, a payment, a benefit, or an income.** Nothing is issued to anybody. **It is the ordinary result of applying two rules the system already has.**

| Step | The rule | Where |
|---|---|---|
| 1 | **Credit is a record that a person spent time on work.** Not effort, not output — time spent. | **A2** (time as measure), §6 |
| 2 | **Maintaining a living human body is work.** Doing it for somebody else is work, so doing it for your own body is the same work. | §6.1, §6.1b |
| 3 | Therefore **a living human accrues credit for the hours spent maintaining themselves.** | §6.1b |
| 4 | **Every human is in the books whether they participate or not**, and a verified living person demonstrably did that maintaining. | **A7**, §6.4b (proof of life) |

> **A person who does nothing else is still doing that work, and the books record it because it happened.**

**The alternative would break A2.** Handing a person credit they did not earn would be credit for no time worked. **That is exactly the "abstract, issued quantity" A1 forbids**, and it is why the floor could never have been written as an allowance.

#### What this rules out saying

| Do not say | Why it is wrong |
|---|---|
| *"a basic income"* | An income is paid by somebody to somebody. **Nothing is paid, and there is no payer.** |
| *"a safety net"*, *"the dole"*, *"an entitlement"* | All three describe a claim on other people. **Credit is a record of the holder's own time and is a claim on nobody** (A3). |
| *"the system supports people who cannot work"* | **Everyone alive is working, by this definition.** The floor does not distinguish between the busy and the idle, because keeping yourself alive takes the same hours either way. |

**The praxis varies. The derivation does not.** A network chooses which activities count and how many hours each takes. **No network chooses whether staying alive is work, because A2 already decided that.**

---

### 7.5.3 The floor's value is an economic setting, with a bound at each end

**Setting `F` is not an act of generosity.** It is the network deciding how much consumption room the act of being alive creates, and the number has to work.

> **Set it too low and people cannot afford what they need. Set it too high and the books stop rationing anything. Finding the value that balances the economy is the network's job.**

#### The lower bound, with the numbers

**A year of essentials commands some quantity of other people's labour.** Call it `E`. The floor must be large enough that a person doing nothing else can still take that much.

`ρ · F · 365 ≥ E`

**Worked, with `E` = 700 h/year** *(illustrative — the real figure is the network's to measure against its own basket)* **and ρ = 1.2:**

| | |
|---|---|
| Minimum floor | 700 ÷ (1.2 × 365) = **1.6 h/day** |
| At `F` = 2 h/day, room per year | 1.2 × 2 × 365 = **876 h** — covers 700 h of essentials |
| At `F` = 1 h/day, room per year | 1.2 × 1 × 365 = **438 h** — **short by 262 h** |

**A network at `F` = 1 h/day has subscribers who cannot afford to eat. That network fails.**

#### The upper bound, with the numbers

**Compare the floor's room against what a year of ordinary life actually commands.** A median lifestyle commands about **1,380 hours** of other people's labour a year (§3.5).

| Floor | Room from the floor alone, `ρ·F·365` at ρ = 1.2 | As a multiple of a median lifestyle |
|---|---|---|
| 2 h/day | 876 h | **0.63×** |
| 4 h/day | 1,752 h | **1.27×** |
| 8 h/day | 3,504 h | **2.54×** |
| 10 h/day | 4,380 h | **3.17×** |

**At `F` = 10 and ρ = 1.2, being alive entitles a person to over three times a median material standard before they do a single hour of anything else.**

> **The gate then stops binding on almost everybody.** `D ≤ ρ·C` still holds, but it is not the thing deciding who gets what. **Where the economy can actually deliver that much, this is abundance and it is the intended end state** (§3.5, Q6). **Where it cannot, physical shortage is decided at the point of distribution instead — by a queue or a lottery** (§3.4a, §6.4d) — **and the accounting has stopped doing the work it was set up to do.**

#### What the project owes here

**Aequitas does not set `F` and must not** (A8). **What this project owes is a demonstration that a stable value exists** — that for a given economy there is a band of `F` and ρ inside which essentials are affordable and the ledger still rations what is genuinely short.

> **⚠️ Owed: a simulation showing the stable band, and its width.** Registered with **OP-4 (debit tolerance)**, which already holds the floor's magnitude and the ceiling's denominator. **Nothing in this section claims the band has been found.**

---

### 7.5.4 Essentials are always affordable, by arithmetic first

**Two separate things make essentials reachable, and they are usually confused.**

> **1. The floor's own arithmetic. A person's credit for staying alive is sized to cover what staying alive costs.** This is the ordinary case and it covers everybody, however little else they do. Nobody is assessed, nobody applies, and nobody decides they qualify.

> **2. A backstop for the abnormal case. A restriction arising from a person's standing reaches non-essentials only.**

**The second exists because of measurement error, not because of poverty.** A producer over-assigned for years would suffer real harm before §3.3 corrected the record — the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). **The backstop caps that exposure at restricted non-essential consumption for a period, followed by correction.** It applies on the same terms to somebody found to have committed fraud (§5.3d).

**The floor does not require anybody to spend it on essentials.** A person may put their room toward anything they like. **The guarantee is that they can afford what they need, not that they must buy it.**

> **The floor is therefore not only a welfare provision. It is the error tolerance of the whole accounting.**

*(Note for review: conformance requirement 17 currently states this as a restriction rule only. It should be split to carry both mechanisms, or reworded to point at the arithmetic first.)*

---

### 7.5.5 The disparity ceiling — an absolute maximum, not an expected spread

> **Inside any one trust network's books, the ratio between the largest and the smallest lifetime credit cannot exceed `24 ÷ F`.**

**Why the arithmetic gives that.** IC-7 caps any account at **24 hours of activity per 24 hours** (conformance requirement 8). Every living subscriber accrues at least `F`. **Highest ÷ lowest = 24 ÷ F.** At `F` = 10 h/day that is **2.4**.

#### It is an extreme, and nobody reaches it

**`24 ÷ F` requires one person to hold 24 credited hours every single day of their life, from birth to death, without exception.** That means `24 − F` hours of work a day, 7 days a week, 365 days a year, for eighty years.

**No ordinary life comes near it.** An astronaut on an unceasing duty schedule is the shape of thing that approaches it, and only while the schedule lasts.

##### An example, with the numbers

**A network with `F` = 10 h/day. Four whole lives, 80 years each.**

| | How the credit accrues | Lifetime credit | Against a floor-only life |
|---|---|---|---|
| **L — lives only** | 10 h/day, birth to death | 10 × 365 × 80 = **292,000 h** | **1.00×** |
| **M — the arithmetic maximum** | 24 h/day, birth to death | 24 × 365 × 80 = **700,800 h** | **2.400×** |
| **N — maximum, but childhood not credited** | 10 h/day to age 18, then 24 h/day | 65,700 + 543,120 = **608,820 h** | **2.085×** |
| **P — a very hard working life** | 12 h work/day, 300 days a year, ages 20 to 70 | 362,500 + 109,500 = **472,000 h** | **1.616×** |

**Person P's working years, shown in full:** 300 working days × (12 + 10) = 6,600 h, plus 65 rest days × 10 = 650 h, giving **7,250 h a year** for 50 years. The 30 years outside that run at the floor: 30 × 3,650 = **109,500 h**.

> **The figure to quote is not 2.4×. It is that a very hard working life reaches about 1.6× a life spent only staying alive, and that 2.4× is the wall nobody gets to.**

#### The ceiling depends on two network choices, not one

**Person N shows the second one.** An infant learning to speak is spending time on something. **A network may count all of that non-floor time as learning, or none of it, or some.** §6.1 already says learning is work; §10.1 already leaves the list of always-creditable activities to the network.

**The choice moves the reachable maximum:**

| The network's choice on childhood | Highest reachable lifetime ratio |
|---|---|
| Credit a child's learning time in full | **2.400×** — the arithmetic ceiling is reachable |
| Credit none of it | **2.085×** — nobody can reach the stated ceiling, ever |

> **A network that does not credit childhood has a stated ceiling of 2.4× that no subscriber can reach, and its most industrious subscriber falls short of it for a reason that has nothing to do with how hard they worked.**

**This is a second dial on the same number, and it was not written down before.** It belongs with `F` under **OP-4 (debit tolerance)** and with the always-creditable list under §10.1.

#### Four conditions on the bound

1. **The value of `F`.** The ceiling **is** `24 ÷ F`, so a network with a 2 h floor states a 12× ceiling. **The result is only as tight as floors are generous.** `F` is a network choice (§6.1b, A8).
2. **The network's treatment of childhood**, per the table above.
3. **No fraud manufactures hours.** IC-7 caps a day at 24 hours, but collusive hand-offs could still inflate gross hours (**OP-1**, service → influence). The bound assumes that channel is controlled.
4. **It is a statement about one network's books.** Nothing else.

#### What condition 4 replaces, and why

**Through v0.22 this section carried a fifth condition claiming the bound held *"across any set of networks compatible enough to interoperate"*, on the ground that compatible networks *"arrive at the same ledger for the same person."* Both halves are withdrawn** (author ruling, 2026-08-25).

- **Networks do not trade with each other, and no book is ever added to another book** (§5.0). There was no object for a cross-network bound to describe.
- **Compatible networks do not arrive at the same figure, deliberately.** §6.4b is **comparison, never conversion**: each party re-reads the shared physical record through its own model. Two networks with different floors report different credit for the same day, and both are right.
- **A merge requires consensus on every rule, identity included** (§5.3c, §5.0). Networks that cannot confirm two pseudonymous accounts belong to one person cannot merge.

> **The comparison against money is unchanged, and it is a fair one.** Money's spread reaches about **10⁶ ×** the median **within one country's own statistics** (SCF 2022 and Forbes). The bound above is the spread within one network's own books. **Two sets of books, compared like for like.**

*(Note for review: old conditions 2 and 3 — floor-shopping arrested by counterparty re-computation, and that guard's dependency on **OP-22** — are narrowed by the ruling rather than removed. Under §5.0 a seller chooses which network a transaction lands on, so a network with an implausible floor loses sellers. What remains of the OP-22 dependency is proving a **pledge's** backing across a model boundary, §6.4b. **Flagged for the author rather than settled here.**)*

---

### 7.5.6 Why hoarding does not beat the bound

**Credit `C` and debit `D` are cumulative running tallies derived from the event log** (A6), and **credit is never spent** — a purchase adds to `D` and never subtracts from `C`, because credit is not a currency (A3).

**So `D ≤ ρ·C` is a ratio re-checked at every event, not a balance drawn down.** A person who consumes nothing for decades and then spends heavily can only bring forward their own allowance, which is bounded by `ρ·C`. **There is no stored lump to release.**

**At equal age, two people's cumulative credits stand in a ratio of at most `24 ÷ F`, so their cumulative consumption does too.** The only spread beyond it is age — time lived, not class. **A 60-year maximum worker against a 20-year floor-only person is 3 × 2.40 = 7.20×**, confirmed in the simulator (`06-simulation/statera/`).

---

### 7.5.7 What the simulations found

> **Formally stated, simulated, and stress-tested.** The formal statement and a plain-language explainer are in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`. The adversarial pass of 2026-08-14 answered all three attacks — **Methuselah** (§7.5.6 above), **dynasty and household** (a household is a co-op; its dwelling debit splits per occupant by dwelling time, children included, so the bound is per person and inheritance dilutes it, §6.2b), and **collector** (holdings raise your own debit, so a hoard bounds itself).

`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`, N = 200,000, gate `D ≤ ρ·C`, credit in `[F, 24]` h/day, 7 self-tests green:

- **The `24 ÷ F` ceiling is exact and does not move with ρ**, because ρ cancels in `ρ·24 ÷ ρ·F`. It also does not move with the weighting model, so **the headline result does not depend on OP-10.** On the same synthetic population, money's spread is 14× on income and roughly 700–950× on wealth.
- **ρ behaves like a prime rate.** A ρ can be chosen so that aggregate demand matches productive capacity, and it moves sensibly under shocks. Against the median-lifestyle anchor the baseline clears at **ρ\* ≈ 1.2**, a −30% capacity disaster tightens it to ~0.68, growth loosens it to ~2.2, and a +25% pollution re-weighting tightens it to ~1.0. *(Absolute values are illustrative and depend on OP-10; the directions are robust.)*
- **Efficiency, not extra labour, is what reaches abundance.** The same population is mildly short under the wasteful US production method and reaches everyone's full desired standard under German, Japanese or Spanish efficiency (Q6). **The binding constraint is physical throughput** (§3.5).
- **The ceiling is fraud-invariant.** IC-7 bounds every account, honest or not, so the most a fraudster reaches is `ρ·24` — the honest maximum. **Fraud fills the band and cannot create an outlier beyond it.**

> **What the simulations have not yet done, and it is now the more important of the two:** find the **stable band of `F` and ρ** described in §7.5.3. The existing runs take `F` as given. **Owed, with OP-4.**

---

### 7.5.8 The real-distribution comparison

`06-simulation/scenario-suite/q4_locked_ledgers.py` applies the bound to real US and world distributions under the **material-only** rule (A1's corollary), asking what fraction of people would sit past a permanent lockout — non-essential consumption held at the floor for life because their sustained footprint exceeds `ρ · 24 h/day`, the most any human can earn.

- **Stripping the financial layer collapses the top of the distribution by about 1,000×.** Money wealth reaches ~10⁶× the median, but material **consumption** only ~670× (Oxfam billionaire personal footprints), because consuming physically takes bounded time. **The spread the bound has to cap is far smaller than the monetary one.**
- **Only a thin slice is locked.** Material-only, about **0.1–2%** of Americans are permanently locked, ρ-dependent, around 0.5% at ρ = 1.5. **These are the ultra-consumers, not the merely rich**, and fully divesting material property does not save them, because consumption debit is permanent (§3.2). **Meanwhile about two-thirds sit below their cohort average and would gain room by joining** (§5.2).

---

## What this draft changed, for review

| # | Change | Substance or style | Author's instruction |
|---|---|---|---|
| 1 | **§7.5.1 defines the floor as credit for named activities** — sleeping, eating, defecating, hygiene — **and says the list is the network's to set.** The old text defined the floor by what it protects, not by what it counts. | **Substance** | *"must be a credit for time spent in activities that trust network considers essential to keeping a human being alive"* |
| 2 | **§7.5.2 derives the floor from A2 and A7 in four steps, and states in a table what it must not be called.** The old text said *"it is not a grant"* once, in a clause, and then read like an entitlement for the rest of the section. | **Substance** | *"The framing must be that the floor credits are a logical outcome of the Axioms, even though the praxis may vary."* |
| 3 | **§7.5.3 is new.** `F` has a lower bound (essentials must be affordable) and an upper bound (the gate must still ration what is short), both worked with digits. **The project owes a simulation showing a stable band exists.** | **Substance** | *"If a Trust Network doesn't set their floor high enough, the network can fail. If they set the floor too high, it could also fail… Our job is just to run simulations to show that it is possible to find the right number."* |
| 4 | **§7.5.4 replaces the enforcement sentence.** Essentials are affordable because the floor's arithmetic makes them so. The non-essentials restriction is demoted to a backstop for mis-measurement and fraud. **Adds that nobody is required to spend the floor on essentials.** | **Substance** | *"the entire point of the floor credit is that no matter how lazy or disabled a person is, they will be able to afford the essentials, but not be forced to consume them"* |
| 5 | **§7.5.5 states 2.4× as an unreachable extreme and gives the realistic figure, ~1.6×.** Four whole lives worked out in a table. | **Substance** | *"we need to be clear this is an extrema, and the absolute maximum"* |
| 6 | **§7.5.5 names childhood crediting as a second dial on the ceiling** — 2.400× if credited, 2.085× if not — and routes it to OP-4 and §10.1. **This was not written down anywhere.** | **Substance** | *"how much of their non-floor time would a network credit that infant… could be all counted as all learning, or none at all"* |
| 7 | **Old condition 5 struck.** The cross-network clause and the *"arrive at the same ledger"* claim are withdrawn, and the money comparison is restated as one set of books against one set of books. | **Substance** | OP-22 ruling, same day |
| 8 | Terms defined in a table at the top; every claim carries digits; the section is split into eight numbered parts. | Style | Document standard, v0.22 |

**Three things flagged rather than settled:**

1. **Conformance requirement 17** states the essentials rule as a restriction only. It needs to carry the arithmetic first. **Your call on the wording.**
2. **Old conditions 2 and 3** — floor-shopping and its OP-22 dependency — are narrowed by the ruling, not removed. §7.5.5 says what is left. **Check I have not narrowed it too far.**
3. **The 700 h/year essentials figure in §7.5.3 is illustrative and not sourced.** It should either be measured from the median-lifestyle data or left explicitly as a network's own measurement. **It is labelled as illustrative in the text.**

**Cascades this creates, owed:**

- **§6.1b** — its list of self-care activities should match §7.5.1's, and its *"≈10 h is a defensible physiological figure"* line should point at §7.5.3's two bounds.
- **§0, §6.4d, §10 (OP-1, OP-4)** — every one of these quotes 2.4× without saying it is unreachable.
- **Overview §1 and §6** — same, plus the *"across every network that can trade with every other"* box in §0.
- **Objections OA8 and C-test 8** — same figure, same fix.

---

*End of draft v0.1.*
