<!-- tag: onboarding-the-wealthy -->
# Onboarding the wealthy — generational wealth becomes generational debt

> **Date:** 2026-08-23
> **Raised and ruled by:** the author.
> **Status:** 🟡 **Ruled, partly confirmed against the axioms, one point corrected. Not yet stress-tested, not folded.**
> **Reads against:** `Aequitas_Foundations_v0.34.md` A1, A7, §3.2, §3.2b, §4.1, §4.4, §4.4, §4.4, §4.4, §4.8, §4.7, §4.5, §5.5 · `06-simulation/scenario-suite/q4_locked_ledgers.py` · `06-simulation/residual-unravelling/residual_unravelling.py`

---

## 0. The ruling

**Under capitalism, wealth passes down. Under Aequitas, what passes down is debt.**

A wealthy person deciding whether to join faces a calculation nobody else faces:

> **Join, and a lifetime of consumption arrives with them (§4.4), which for them is a penalty rather than the windfall it is for a median person.**
>
> **Stay out, and nothing is ever charged (§4.1) — but nothing is ever earned either. They start level with anyone who never worked a creditable hour.**

**The author's expectation: most will decline, for their whole lifetime.** They will therefore sit outside the books, holding a disproportionate share of the world's material debt.

**That looks unfair. It is actually the adoption engine.** As low-consuming people onboard, **the debt-load of everyone still outside concentrates.** The transition may take generations, or it may stall at a threshold. **Which is why it must be simulated rather than assumed.**

---

## 1. Three parts of the ruling are already written down, and confirmed

| The ruling says | Already in Foundations | Verdict |
|---|---|---|
| Not joining means never being charged | **§4.1, word for word:** *"Non-participants can neither draw on nor be charged for their estimated position."* | ✅ **Correct** |
| A non-joiner starts level with anyone who never worked a creditable hour | **§4.4.** A position is realizable only on a verified account with observed supersession. An unrealized estimate does nothing, in either direction. | ✅ **Correct** |
| Joining is a windfall for ordinary people and a penalty for heavy consumers | **§4.4.** *"Onboarding is a windfall for a median person... The people for whom a full back-trace is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution. That is correct targeting, not a defect."* | ✅ **Correct, and already argued in exactly these terms** |

---

## 2. The arithmetic, with digits

**Everything below uses figures already established in Foundations §4.4 and §5.5.**

| | Hours per year |
|---|---|
| Self-care credit, every living human (§4.5) | **3,650** |
| Absolute human maximum credit, IC-7, 24 h/day | **8,760** |
| Median US lifestyle consumption (§3.5) | **1,380** |
| Billionaire personal material footprint — ~670× median (§5.5, Oxfam) | **≈ 924,600** |

### The median person onboarding at forty

- Credit: 40 × 3,650 = **146,000 h**
- Consumption: 40 × 1,380 = **55,200 h**
- Ratio `D/C` = **0.38**, against a gate of `ρ` = 1.5.

**They arrive with room to spare. Onboarding pays.**

### One year of billionaire-scale consumption

- Consumption: **924,600 h** in a single year.
- Credit that same year, even at the **physically impossible maximum of 24 hours a day**: 8,760 h.
- Ratio `D/C` = **105.5**, against a gate of 1.5. **They are over by 70×.**
- At the ordinary self-care rate of 3,650 h/yr, the ratio is **253**, over by **169×**.

### How long one year of it takes to clear

To satisfy `D ≤ 1.5 × C` they need 924,600 ÷ 1.5 = **616,400 hours of credit.**

| Accruing at | Years to clear **one year** of that consumption |
|---|---|
| 8,760 h/yr — the human maximum, every hour of every day | **70 years** |
| 3,650 h/yr — the ordinary self-care rate | **169 years** |

> **That is the ruling's title, in numbers. One year of that life takes between seventy and a hundred and seventy years of credit to work off.** Nobody imposed it and nobody can appeal it. **It is arithmetic.**

*Order-of-magnitude only: the 670× is an Oxfam estimate of personal footprint and the 1,380 h/yr is a US median. Foundations §5.5 already pairs these two figures; this note does not introduce a new pairing.*

---

## 3. ⚠️ One point is wrong as stated, and correcting it makes the ruling stronger

**The ruling says:** *"To avoid being locked out, they can simply not claim most of their property when being onboarded."*

**Three passages say otherwise.**

1. **§4.4 condition 1.** Estimates for undisclosed holdings are computed **over the undisclosed residual**, not over the whole population — *"without it, a person who documents only their flattering years free-rides forever on an average their own silence inflates."*
2. **§4.4 condition 2.** An estimate **errs against the estimated party**, so supplying evidence always pays. **Silence is the expensive option, by construction.**
3. **§4.5.** *"An auditor may create the record without the owner's consent (A7 — everyone is accounted). A reluctant owner's mansion can be entered from estimates of its size and construction."*

> **So not declaring an asset does not hide it. It forfeits the right to argue the estimate down.**

### But the escape the ruling is reaching for does exist — and it is narrower

**Property debit is dischargeable on transfer (§3.2). Consumption and pollution debit never is (§3.2b).**

So a wealthy person who genuinely **divests before joining** — sells the estate for money to a non-participant — holds no atoms, and there is no property debit to charge. **That half of the escape is real.**

**The other half is not, and it is the half that matters:**

> **You can shed the property. You can never shed having consumed.** Decades of that lifestyle are permanent debit on the person who caused it, and §4.4 back-traces them to birth.

**And Foundations already knew this.** [`q4_locked_ledgers.py`](../../06-simulation/scenario-suite/q4_locked_ledgers.py), quoted in §5.5: *"even fully divesting material property does not save them (permanent consumption debit, §3.2)."*

> **This is the sixth time in this project that the answer was already written down and unread.** The standing rule holds: **check the axioms before importing an outside solution**, and a grep would not have found this — §5.5's callout does not mention onboarding.

**Net effect on the ruling: the lockout is *more* certain than the ruling assumed, not less.** The decision the wealthy face is therefore sharper, and the author's prediction that most decline is better supported.

---

## 4. What is genuinely new — and it is correct

**The ruling identifies an adoption dynamic nobody had written down:**

> *"As more low-consuming people onboard with Aequitas, the debt-load of the remainder starts to concentrate."*

**This is §4.4's residual rule, running in the adoption direction.** The rule is `estimate = (N − Y) / Z` — the independently-known total, minus what measured participants recorded, divided among those still dark.

**As people join: `Y` rises and `Z` falls. So `(N − Y)/Z` rises for everyone still outside.**

**Worked, with round numbers.** A region's independently-measured total is 1,000 units. 100 dark actors, none measured:

| Participants | `Y` measured | `Z` still dark | Estimate per dark actor |
|---|---|---|---|
| 0 | 0 | 100 | **10.0** |
| 40 low-consumers | 200 | 60 | **13.3** |
| 80 low-consumers | 440 | 20 | **28.0** |

**The last twenty face nearly three times the first estimate — and none of them did anything.** They simply stayed while the well-documented left.

**§4.4 already calls this by name:** *"the estimate worsens as good producers exit — so darkness stops paying."* **The ruling has rediscovered adverse selection reversing, one level up, applied to adoption rather than to production.**

### One precision the ruling needs

**Nobody receives a bill.** §4.4: **the residual is computed, published, and charged to no account** until its causer onboards.

> **So the pressure is not a debt collector. It is a published number that gets worse the longer you wait, in public, where everyone can read it.** The bite lands only on the day you join — and it is bigger every year you do not.

**That is a stronger incentive than a charge would be, and it needs no enforcement.**

---

## 5. The stall already has a measured threshold

**The ruling says the transition "may even stall out at a certain threshold." It does, and the number exists.**

[`residual_unravelling.py`](../../06-simulation/residual-unravelling/residual_unravelling.py), recorded in §4.7 residue (b):

> **Once verification costs more than roughly 40% of a median unit's debit, the residual rule stops unravelling the dark pool, and darkness becomes stable again.**

**So there are two competing forces, and the simulator's job is to find where they cross:**

| Force | Direction |
|---|---|
| The concentrating residual (§4.4) | **Pulls people in**, harder the more who have joined |
| The cost of verifying (§4.7) | **Holds people out**, and above ~40% it wins |

**Neither is speculative. Both are already in the documents. Nobody has ever run them against each other.**

---

## 6. Who games this

| Attack | Verdict |
|---|---|
| **Stay out forever** | **Not an exploit. It is the declared option** (§4.1, §4.8 — the gift economy never closes). The system prices the path rather than guarding a door. |
| **Join, take the windfall, then re-acquire** | **Bounded.** Property debit re-attaches the moment they take possession (§3.2), and consumption debit accrues as they consume. The windfall is a one-off reconciliation, not a renewable resource. |
| **⚠️ Hold assets through a low-consuming proxy** | **Registered, not solved.** A wealthy non-participant puts assets in the name of a relative who onboards clean. This is **not new** — it is the **repeat-shell entity** problem from §4.8, and a **C6 (identity)** question. **Route it there; do not open a new problem for it.** |
| **Wait for the estimate to be litigated down** | Self-defeating. §4.4 condition 2 errs against the silent party, so waiting worsens the figure. |

---

## 7. Screening

| Test | Verdict |
|---|---|
| **Universality** | ✅ **No special rule for the wealthy exists or is needed.** The same back-trace, the same gate, the same floor. Their outcome differs because their consumption differs. |
| **Decentralization** | ✅ No authority decides who is rich. The residual is computed from a public total by a published method. |
| **Fecundity** | ✅ **This is the strong part.** The concentrating residual makes joining more attractive the more people have joined. **The mechanism recruits.** |
| **Who games this?** | ✅ Named in §6. One residual, routed to C6. |
| **Paul Glover?** | ✅ Nothing depends on an enthusiast. |
| **Objective function?** | ✅ None. Nothing is maximised. |
| **Physical trace** | ✅ Consumption left a trace — a person ate, burned, and emitted. **Measure it.** No convention is being declared here. |

---

## 8. What a simulation must express

**This is the scenario the adoption work was missing, and it is now specified.**

1. **A non-participant pool** whose estimated share is recomputed each period by `(N − Y) / Z`.
2. **A published residual that charges nobody** (§4.4) — visible on screen, not on a ledger.
3. **A join decision per cohort**, comparing the back-trace they would inherit against the credit they would realise.
4. **A verification cost dial**, so the ~40% stall threshold can be crossed from both sides.
5. **A wealth distribution with a real tail** — the SCF-2022 and Forbes material-only distribution already in [`q4_locked_ledgers.py`](../../06-simulation/scenario-suite/q4_locked_ledgers.py). **And the 1% coverage cut must be OFF**, or the tail is invisible by construction.
6. **Generational time.** Seventy to a hundred and seventy years is the timescale in §2, so a ten-period run cannot see this. **A two-hundred-year run at cohort scale can.**

---

## 9. Status

**Settled:** that non-participation is never charged, that onboarding is a windfall for the median and a penalty for the heavy consumer, that the residual concentrates on those who wait, and that the whole thing is an adoption gradient rather than a punishment.

**Corrected:** undeclared property is estimated against you, not ignored. **Property can be shed; consumption cannot** — which makes the lockout more certain, not less.

**Open and routed:** proxy asset-holding → **C6 / OP-25 / §4.8 repeat shells.**

> **Recommendation: stress-test before folding.** The arithmetic is sound and three parts are already in the documents, but §4's adoption dynamic has never been attacked, and the interaction between the concentrating residual and the verification-cost stall is exactly the kind of two-force claim this project has been wrong about before. **Simulate it, then fold.**
