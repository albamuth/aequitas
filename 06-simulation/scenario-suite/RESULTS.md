# Scenario suite — results

> **Read this instead of re-running.** From the five `--test` runs, last verified 2026-08-24.
> This is the summary layer. Each question keeps its own plain-language companion beside it — [`Q1_AUTARKY.md`](Q1_AUTARKY.md), [`Q2_CAPTURE.md`](Q2_CAPTURE.md), [`PLASTIC.md`](PLASTIC.md), [`Q4_LOCKED.md`](Q4_LOCKED.md), [`Q5_REALLOCATION.md`](Q5_REALLOCATION.md) — and those carry the caveats.

---

## Q1 — An America that traded with nobody

> **Autarkic America is not short of labour, land, water or food. Its ceiling is set by two things: finishing the renewable-energy build-out, and a short list of critical minerals it cannot dig at home.**

Complete the transition and everyone can live at roughly today's *average* standard, sustainably. Leave energy where it is and energy per person falls to about **a fifth** of today's.

- **The binding constraint switches** — energy binds on the current build, land binds after the build-out.
- **Mean over median = 1.20.** Levelling consumption costs remarkably little, because the mean is only 20% above the median once paper wealth is excluded.

## Q2 — Labour captured or spent on enforcement

> **Between a fifth and well over a third of all productive labour — about 185 to 396 hours per adult per year — is currently either captured by ownership or spent enforcing and extracting.**

- Combined high estimate **36%**, against a naive sum of **47%**. The two pools overlap and are de-duplicated rather than added.
- **The reframe matters more than the number.** Under Aequitas there is nothing to steal, because credit is a non-transferable fact about who did the work. So "stolen labour" is not an Aequitas quantity. The answerable question is how big the captured pool is *today*.

## Q3 — What plastic costs in hours

> **Cleaning a tonne of plastic out of the ocean costs about 950 hours of human work — roughly 70× the labour to make it new, and 240× the labour to recycle it.**

- **Microplastic has no headline figure, and that is the finding.** No technology removes it at scale, so its debt is effectively unbounded and sits on whoever last held it until someone invents a way.
- The cost-to-labour bridge is monotone: ocean cleanup vastly exceeds landfill.
- Plastic persists for centuries, so its natural clearance rate is about zero. Under Foundations §3.3 that means discarded plastic is **always above baseline**, and carries close to its full remediation cost.

## Q4 — Who is already locked out

> **Strip out paper wealth, which Aequitas does not count, and only about 0.1–2% of Americans are permanently locked out — and they are the ultra-consumers, not the merely rich.**

| | Ratio |
|---|---|
| Wealth of a billionaire against the median | **1,040,000×** |
| Their *consumption* against the median | **≈ 1,320×** |
| Compression | **≈ 788×** |

- **About two-thirds of Americans would gain room by joining.** 66% sit below the mean footprint.
- **Even fully divesting material property does not save the locked-out.** Property debit is dischargeable; consumption debit is not.

## Q5 — Moving labour from wasteful to essential

> **The wasteful labour freed worldwide — roughly 1.1 to 2.4 trillion hours a year — would close the global health-worker shortage 50 to 100 times over, and build adequate housing for everyone now living in a slum within about six months.**

- Still **41× the health shortage** under the sensitivity pass, so the conclusion does not rest on where the line is drawn.
- Health and housing for five years fit inside **one year** of the freed pool.
- **Aequitas decrees none of this.** The shift would come from pledges — people spending their own earned credit on what they want built. The wasteful/essential split is an exogenous dial the reader can move, and every boundary is contestable.

## What would falsify these

- **Q1:** a resource with a ratio below 1 that the model omits. Land and energy bind; something else binding would change the answer.
- **Q2:** the two pools overlapping far more than modelled, which would pull 36% down toward 17%.
- **Q3:** a scalable microplastic remediation technology. That would put a finite number on the one quantity currently unbounded.
- **Q4:** a definition of "locked out" under which the merely rich are caught. The result depends entirely on excluding paper wealth, which is Foundations A1.
- **Q5:** a wasteful/essential taxonomy under which the freed pool no longer covers the shortage. The sensitivity pass says it would have to be very different.

## The shared limit

**All five are single-period.** None has a time axis, so none can say how fast anything happens, or whether a transition is stable. That is what the [Statera kernel](../statera/) was built for.

## Figures

| File | Shows |
|---|---|
| `q4_fig1_locked_vs_rho.png` | The locked-out share against the consumption gate ρ |
| `q4_fig2_compression.png` | Wealth disparity against consumption disparity |
| `q4_fig3_distribution.png` | Where people sit relative to the mean footprint |

Q1, Q2, Q3 and Q5 produce text reports only.
