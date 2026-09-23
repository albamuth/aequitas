# Data — US wealth distribution, 2022 Survey of Consumer Finances

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** data source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | Aladangady, A., Bricker, J., Chang, A. C., Goodman, S., Krimmel, J., Moore, K. B., Reber, S., Volz, A. H., & Windle, R. A. (2023). Changes in U.S. family finances from 2019 to 2022: Evidence from the Survey of Consumer Finances. *Federal Reserve Bulletin*, October 2023. [federalreserve.gov](https://www.federalreserve.gov/publications/october-2023-changes-in-us-family-finances-from-2019-to-2022.htm) · [PDF](https://www.federalreserve.gov/publications/files/scf23.pdf) |
| **Survey home** | [Federal Reserve — SCF](https://www.federalreserve.gov/econres/scfindex.htm) |

## What was checked on 2026-09-23

`disparity_ceiling_sim.py` calibrates its synthetic wealth to five SCF 2022 figures. **The Bulletin page confirms one of them.**

| Figure in the code | Value | Checked against the Bulletin |
|---|--:|---|
| Median family net worth | $192,900 | ✅ **Confirmed** |
| 90th percentile | $1,920,758 | ⚠️ **Not on the page.** The page gives the *median of the top decile*, $3,794,600, which is a different figure |
| 95th percentile | $3,779,600 | ⚠️ **Not on the page** |
| 99th percentile | $13,666,778 | ⚠️ **Not on the page** |
| Top wealth, "~$200B" | Forbes | ⚠️ **No dated Forbes source in the code.** Unverified |

**The percentile cut-offs probably come from the SCF microdata or the Fed's interactive tables.** Until one is cited with a link, they are **unverified**.

## Why it matters to Aequitas

`disparity_ceiling_sim.py` test 2 (*SCF calibration*) and test 3 (*money dwarfs the ceiling*) rest on these figures. **Both are unsourced until the three percentiles and the Forbes figure are cited.**

**Used by:** `06-simulation/disparity-ceiling/README.md`, *Test sources*.
