# Simulation briefs — questions we are asking outsiders to answer

> **Every file here is a question this project cannot honestly answer for itself.** Each one states the problem, the arithmetic, the inputs, and **what result would count against us — all decided before anybody runs it.**
>
> **You do not need permission, an account, or anything from us to run one.** If you get a different answer, that is the point.

---

## Why we hand these out instead of running them

**Three reasons, and all three are already written into the theory rather than invented for this page.**

| Where it is already stated | What it says |
|---|---|
| **Foundations §2.1**, the decentralization criterion | *"Can a stranger check a claim without asking anybody's permission?"* A result only we can reproduce fails it |
| **Foundations §3.3a**, requirement 1 | **Two unaffiliated replications** before a cost constant may re-weight history |
| **Foundations §4.4** | *"A check that compares a thing to itself can find a mistake, and it cannot find a hole."* **A simulation we design, run and score is that check** |

**And the record says the same thing.** Of the last eight corrections this project made to its own published figures, **six were found from outside**, and every one of them was wrong **in the direction that flattered us**. Foundations §4.4 has a section on why that error is not random.

> **So the useful thing an outsider can do is not agree with us faster. It is run the arithmetic and get a different number.**

---

## What every brief contains, and why each part is there

**A brief is not a task. It is a specification you can argue with before you run anything.**

| Section | What it is for |
|---|---|
| **1. The question** | One sentence, and it must be possible for the answer to be *no* |
| **2. What depends on it** | The exact published claim that changes if the answer comes back against us |
| **3. Terms** | Every symbol defined where it is first used. **No brief may use a symbol it has not defined** |
| **4. The model** | The arithmetic, written out. **Not code.** Two people should be able to implement it in different languages and agree |
| **5. Inputs** | Public data with a source, or a generator with a stated seed and distribution |
| **6. What an answer looks like** | The shape of the output table, so two runs can be laid side by side |
| **7. Declared in advance** | **Our prediction, and the threshold that would refute us.** See below |
| **8. Self-tests** | Checks that must pass, **each one able to fail** |
| **9. Out of scope** | What the brief does not ask, so a result is not over-read |
| **10. Known ways to get it wrong** | Traps we already walked into, or expect |

---

## Section 7 is the one that matters, and it is unusual

> **We write down what we expect, and the number that would count against us, before anybody runs anything.**

**Terms.** A **prior** is what we predict the run will show. A **refutation threshold** is the result at which we accept the claim has failed.

**Why both are fixed in advance.** This project has published four figures that were wrong in the direction that suited it, and each was corrected from outside. **The general form of that failure was supplied by a critic:**

> **A check whose passing condition is set by the checker is not an instrument, and it fails toward flattery.**

**A threshold chosen after seeing the result is exactly that.** So each brief states its threshold up front, and **if a run crosses it we are bound by it.**

### A worked example, with numbers

Take a brief asking how far a published figure moves under an honest change of method.

| | |
|---|---|
| **Our prior** | The figure moves by less than **1.5×** between the widest pair of defensible methods |
| **Refutation threshold** | **Any spread at or above 2.85×** means the method choice, not the physics, is setting the number |
| **What we do at 6.31×** | **We withdraw the rule** |

**That is not hypothetical.** It is `06-simulation/method-spread/`, run 2026-09-02. **The measured spread was 6.31×, the rule was withdrawn the next day**, and Foundations §3.4a was rewritten around the absence.

**In plain words: the threshold was set before the run, the run crossed it, and the rule went. That is what these briefs are for.**

---

## How to run one, and what happens to your result

1. **Read the brief and argue with it first.** If the model is wrong, the run is wasted. **Telling us the model is wrong is worth more than a number.**
2. **Implement it yourself.** Do not port our code — an independent implementation is the whole value. Section 4 is written so you never have to read ours.
3. **Report what you got**, including the self-test results and anything that failed.

**What we do with it.** A result that disagrees with our prior is folded and credited by name, in the documents, at the section it changes. **The record of that is public**: Foundations §4.4, §4.3 and §5.5.7 each name the outsider who corrected them, and `07-outreach/log/` carries the night it happened.

**What we will not do.** We will not quietly re-run it until it agrees. **A superseded figure stays in the changelog with the date it was withdrawn.**

---

## The open briefs

| Brief | The question, short | Request id |
|---|---|---|
| [SB-01](SB-01_ceiling-challenge.md) | Can anything push the credit-disparity statistic **up** without breaking the 24-hour cap? | `sr-20260901-construct-a-challenge-that-pushes-max-claime` |
| [SB-02](SB-02_rho-star-rubric.md) | Is the clearing rate **ρ\*** an instrument, or does it also fail to see what it claims to measure? | `sr-20260901-score-claim-2-of-disparity-ceiling-sim-py-th` |
| [SB-03](SB-03_reweighting-cost.md) | What does a **full re-weighting** of a billion-event log actually cost in time and memory? | `sr-20260901-wall-clock-and-memory-cost-of-a-full-re-weig` |
| [SB-04](SB-04_honest-label.md) | Does labelling a figure **metered** or **modelled** pay, or does it just hand rivals a target? | `sr-20260904-does-a-producer-who-labels-each-published-fi` |
| [SB-05](SB-05_parcel-identity.md) | What happens to the books when a flow sheet **cannot tell one parcel from two**? | `sr-20260905-how-often-does-a-joint-process-flow-sheet-fa` |
| [SB-06](SB-06_resolution-tax.md) | How much dearer does a small producer's product read **because they cannot afford instruments**? | `sr-20260905-sweep-producers-of-one-good-by-scale-and-by-` |

**Where the theory lives:** [`../../00-strategy/`](../../00-strategy/). **Every brief names the sections it depends on**, so you can read those rather than the whole thing.
