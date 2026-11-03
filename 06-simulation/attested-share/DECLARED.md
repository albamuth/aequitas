# Declared before the first run (2026-11-03, written before any number was computed)

Request `sr-20260913-over-a-simulated-joining-population-what-sha`.

Definitions used. A person's **days lived** at calendar time T run from birth to T. **Attested** days are those before the join date, rebuilt from the person's own evidence. **Observed** days are those from the join date (or birth, if later) to T. Share = attested days / days lived.

| # | Outcome | Kind |
|---|---|---|
| O1 | Founding wave (everyone alive joins on day 0), at T = 10 y: median person share in **[0.65, 0.85]**; days-weighted network share in **[0.60, 0.85]** | level |
| O2 | Same scenario at T = 40 y: median person share in **[0.00, 0.40]**; days-weighted share in **[0.15, 0.45]** | level |
| O3 | Same scenario at T = 80 y: days-weighted share **below 0.10** | level |
| O4 | Linear 20-year adoption to 100%, at T = 20 y: days-weighted share in **[0.45, 0.80]** | level |
| O5 | Same scenario at T = 20 y: person-level p90 minus p10 is **above 0.50**, so a mean alone hides the shape | shape |
| O6 | A cohort that joins together falls as a / (a + s) (a = age at joining, s = years since joining). Its median share equals 0.5 when s equals the cohort's median joining age, within 2 years | level |

Exclusions. Scaling the reconstruction reach by r scales the attested share by exactly r. That is arithmetic, so no outcome is declared on it (brief 4b: it could not fail).

What would count as failure: any bracket above missed. A miss is reported as a miss.
