<!-- tag: shelf-life-and-custody -->
# Custody termination and shelf life

> **Date:** 2026-08-23
> **Raised and ruled by:** the author.
> **Status:** 🟡 **Two parts confirmed as already-written. One is a new mechanism, built and tested as ruled.** A softer version I proposed was overturned by the author the same day — see §3. **One hole stays open (§4, row 2).**
> **Reads against:** `Aequitas_Foundations_v0.34.md` §3.2, §3.2b, §3.6, §4.4, §4.5, §4.5, A8 · built in `06-simulation/statera/statera.py` and `06-simulation/statera/chains.py`

---

## 0. The three rulings

> **1. The property / consumption debit distinction does not need to be in the ledger.** A loaf of bread comes in a plastic bag. Both took resources. The eater eats one and throws the other away. **No 'eaten' event and no 'thrown away' event is needed: the custody chains ENDING at the consumer is enough to put both on their ledger.** Hand the bread on instead, logged as a resale, and the debit moves like property.
>
> **2. Single-use goods are not spread over time of ownership.** A house occupied for years splits by holding time. **An opened loaf does not.** Opening the bag is putting it into service, nobody resells an opened loaf, and the whole cost lands on the one person who used it.
>
> **3. Goods with a shelf life carry their expiry date in the event log.** Past that date **they cannot be handed on** — they are now part of the last owner's waste stream. This prevents the sale of expired goods.

---

## 1. Rulings 1 and 2 are already written down

**Both were derived independently and both match text that already exists.**

| The ruling says | Where it already is |
|---|---|
| The custody chain ending is enough; no consumption event needed | **§3.6 rule 1, almost word for word:** *"If nobody will accept a worn-out asset, its last holder has consumed it and holds its end-of-life debit forever, **as if it were food**."* |
| Single-use goods land whole on their user | **§4.5's boundary test:** *"capital vs. consumption... told apart by physical fate: does the thing survive the process?"* A drill bit survives; the oil it burned does not |
| A resale moves the debit | **§3.2.** Property debit follows possession |
| Producer-side pollution does not move | **§3.2b.** It stays permanently on its causer, and no resale sheds it |

> **And ruling 1 retires a limitation this project recorded yesterday.** The simulator was flagged as unable to tell property debit from consumption debit. **It does not need to.** Whether a thing was eaten or is merely still owned changes nothing about *whose ledger it sits on*, and whose ledger is the only question the accounting ever asks. **A limitation dissolved rather than solved — which is the cheaper kind.**

**Built and tested.** `test_the_custody_chain_ending_is_the_fate` — the eater holds exactly the 780 kg handed to them, with no consumption event written anywhere. `test_single_use_lands_whole_on_its_user` — a house splits 50/50 by holding time; a loaf lands 100% on whoever opened it, however briefly they held it.

**Worked reason the single-use rule matters, with digits.** Split a loaf by holding time and a shopper who ate it in one day would owe *less* than one who left it on the counter for a week. **The rule that looks fussier is the one that stops the accounting rewarding waste.**

---

## 2. Ruling 3 is a new mechanism, and it is the best kind: a clock on an existing rule

**§3.6 rule 1 already says the last holder eats the debit when nobody will take a thing on. What it never said is *when* that becomes true.** Today it is discovered — you find out nobody wants your rotten stock. **Shelf life makes it automatic and dated in advance.**

> **Expiry is §3.6 rule 1 with a clock on it.** No new principle. The moment "nobody will accept this" stops being a discovery and becomes a fact anyone can read off the log.

**What is recorded:** the last period at which a parcel can still be handed on. `np.inf` means the thing does not spoil.

---

## 3. I proposed a weaker version of the ruling. It was wrong on all three counts.

**The ruling says expired goods become "impossible to hand off custody."** I first built a softer version — the transfer is recorded but does not discharge the sender — on three arguments. **The author overturned all three the same day, and the ruling stands as written.**

| My argument | Why it fails |
|---|---|
| *"A hard block would forbid compost and animal feed."* | **Waste disposal is a service with a cost, not a hand-off of property.** §3.6 already credits recyclers *"for the work of reducing pollutants."* It has its own event shape and never needed the transfer path. |
| *"A food bank might want day-old bread."* | **A food bank relying on gifted bread is a symptom of the exact scarcity Aequitas claims to remove.** §5.5 makes essential provision unconditional. **If somebody needs charity for bread, the system has failed** — and modelling that failure as a feature is backwards. |
| *"A prohibition needs somebody at the door, and A8 forbids that somebody."* | **This confused a rule that forbids with an institution that enforces.** **IC-7 forbids a 25-hour day and no institution guards it.** The check *is* the enforcement, anybody can run it, and a log that breaks it is non-conformant for everyone who recomputes. **That is the A8-clean shape of a prohibition, and this is one.** |

> **The correction worth keeping: "price it, don't forbid it" is not a universal rule of this system.** It applies where the costly path has a legitimate use — selling out for money (§4.8), choosing opacity (§4.7). **Where there is no legitimate use, an invariant is the right shape**, and Aequitas already has several: IC-7, IC-8, IC-1 to IC-4. **I reached for the pattern instead of checking whether the case fitted it.**

**Built and tested.** `test_expired_goods_cannot_be_handed_on` — the hand-off is refused, the loaf stays on the shop, the buyer takes nothing. `test_disposal_is_a_service_not_a_handoff` — the eater keeps 1 kg of waste and pays 0.25 h for collection; the collector is credited 0.25 h. `test_recycling_moves_the_atoms_but_not_the_pollution` — §3.6 rule 3, where matter genuinely does move on. And `test_the_check_catches_a_forged_expired_discharge` — a log that *claims* an expired discharge is caught, so the recorder is not the only thing policing it.

---

## 3a. And one more thing the author confirmed: breathing is on the ledger

> **"Yes, we are counting the CO₂ every human exhales as debits automatically."**

**A1 already reaches that far** — *"down to the oxygen a human inhales and the CO₂ they exhale."* Statera now records roughly **1 kg of CO₂ per person per day** on the self-care row.

**And §3.3 weighs it at nothing.** *"A flow is a pollutant only above the rate at which the natural world remediates it unaided."* Breathing is inside the short carbon cycle: the carbon came out of the air, through a plant, into food, and back. **It is at baseline.**

> **Both are true at once, and that is the cleanest demonstration in the whole kernel of why §3.2a keeps the debit as a vector.** A year of breathing records **365 kg in the log and costs 0 hours**. A system storing one collapsed number could not hold both facts. **The kilograms are permanent; what they cost is a separate question the weighting model answers, and re-answers if the science ever changes.**

---

## 4. Who games this

| Attack | Verdict |
|---|---|
| **Overstate the shelf life** so goods stay tradeable | **This is OP-24 (understatement drift) at the shelf, and it inherits OP-24's answer.** The receiver takes on the debit and eats it if the goods are unusable, so receivers learn. And the honest rival dater is materially harmed by dumped stale goods, so **the rival funds the correction** (§3.3a). |
| **⚠️ Record no expiry at all**, so the goods never expire | **The real hole, and it is genuinely open.** Nothing forces a date, and the incentive is to omit one. **The answer is the buy side, not a rule:** accepting undated perishable goods means taking on debit for something that may already be waste, so **receivers demand dates**. That is §4.7's shape — *opacity is priced* — and OP-14's, *comparison never conversion*. **Whether the demand is strong enough is empirical and should be simulated, not assumed.** |
| **Backdate or relabel** | Caught. The log is append-only and a record is **annotated, never replaced** (§4.4), so the original date persists and the relabel is visible and dated. |
| **Dump goods just before expiry** on someone else | The receiver chose to accept, and **the date is in the log where they can read it.** Not an exploit; a thing to check before signing. |
| **Let goods expire deliberately** | No gain. You keep the debit. |

---

## 5. Screening

| Test | Verdict |
|---|---|
| **Universality** | ✅ One rule. A good either carries a date or it does not, and which goods spoil is a physical fact rather than a list anyone maintains. |
| **Decentralization** | ✅ **Pure arithmetic over the log.** Anyone can check whether a transfer's period exceeds the recorded expiry. No authority, and in the priced version no enforcer either. |
| **Fecundity** | ✅ Mild but real: it creates standing demand for better preservation and for honest dating. |
| **Who games this?** | ⚠️ Named in §4. **One genuinely open hole — nothing compels a date to be recorded.** |
| **Paul Glover?** | ✅ Nothing depends on an enthusiast. |
| **Objective function?** | ✅ None. Nothing is maximised. |
| **Physical trace** | ✅ **Spoilage is measurable, so measure it.** The exact date is a convention with a measurable basis — the same status as §3.3's natural-remediation baseline — and should be declared as one under §2.5 rather than presented as a hard fact. |

---

## 6. What this does not settle

1. **Who sets the date, and under what method.** It is a cost constant in everything but name, so it belongs to **OP-10 / OP-24** and should be published with its method and vintage (§4.7), like every other estimating number.
2. **Nothing compels a date to exist.** §4, row 2. **Registered.**
3. **Whether receivers actually demand dates** is an adoption question and a good candidate for the simulator, which is now able to express it.

> **Recommendation: fold rulings 1 and 2 as clarifications** — they are §3.6 and §4.5 restated, and §3.2 could usefully say plainly that no consumption event is required. **Hold ruling 3 for a stress test before folding**, because §3 above changed its mechanism and §4 leaves a hole open.
