# Objections register audit — 2026-11-07

> **What this is.** A defect list for `Aequitas_Objections.md` v0.49 (2026-11-02), read against `Aequitas_Foundations.md` v0.67 (2026-11-04) and `Aequitas_Conformance.md` v0.24 (2026-10-28), all three read whole. One row per defect. **Nothing in the register was edited.** The register's Status board becomes required reading for the nightly outreach agent (author ruling 2026-11-07), so the board rows are checked first and hardest.
>
> **How the rows are sorted.** By what the fix costs, cheapest first. **Tier 1** is a word, a number or a pointer. **Tier 2** is a sentence or a paragraph rewritten, no ruling needed. **Tier 3** needs several entries changed together, an author ruling, or a fold that reaches Foundations.
>
> **Line numbers** are the register's at v0.49. **Section numbers** are checked against the renumbering map in `Aequitas_Foundations_CHANGELOG.md` v0.28 (2026-08-27: old 4/5/6 became 4.x, old 7 became 5, old 8 became 6) and v0.33 (2026-08-28: old §1.1 became §2.5, old §1.2 became §2.6).

## Summary

| | Count |
|---|--:|
| Tier 1 — cheap | 24 |
| Tier 2 — a paragraph | 11 |
| Tier 3 — expensive | 5 |
| **Total** | **40** |

**What held.** Every ρ\* figure (1.017 / 0.330 / 0.253 at `F` = 2 / 10 / 14), the 1,380 h/yr anchor, the every-payer peer ratios (0.836 / 0.858 / 0.873, band 0.84 – 0.87), the 3.17× figure, the 0.354 shell-chain ratio, the 3.39 h binding point, the 16,667 h / 4.6 year barn figures, the B21 figures (1.76×, 1.83 steers, 2.99 refineries, 0.12 h/yr) and the B22 table all match Foundations. Every "shipped" pointer that names a current section lands on a section that still carries the rule, except where a row below says otherwise. All eleven conformance row numbers cited (2c, 3a, 4a, 6, 6a, 10a–10i, 12, 13, 14, 14a, 14b, 14d, 14e, 15, 16, 16a–16d) exist in Conformance v0.24.

---

## Tier 1 — cheap: a word, a number, or a pointer

| # | Entry | Line | What it says | What the current document says | Proposed fix |
|--:|---|--:|---|---|---|
| 1 | Part A notation note | 157 | "analysis sections in this register are numbered **OA0–OA11**" | The register has OA0–OA12 (OA12 is OP-26, the coverage gap). | Change "OA0–OA11" to "OA0–OA12". |
| 2 | Status board, OP-7 | 92 | "§4's design rule requires a Level 1 region and a Level 3 region to be able to trade" | The ladder rule is Foundations §4.3 since v0.28 (old §4 → §4.3). §4 is now the whole trust-network section. | Change "§4's design rule" to "§4.3's design rule". |
| 3 | Status board, OP-22 | 83 | "already handled by §4.4 and §4.4" | Two old sections (5.1b and 5.1c) both became §4.4. | Say "already handled by §4.4 (the coverage figure and the leftover estimate)" once. |
| 4 | Status board, OP-14 | 90 | "§4.4 publishes the coverage gap while §4.4 estimates undisclosed activity" | Same double reference as row 3. | Collapse to one "§4.4" with both halves named. |
| 5 | OA6 | 320 | "**Attacks:** §4.6, §4.6" | Old 6.3 and 6.4 both became §4.6. | Write "§4.6" once. |
| 6 | B3 | 1372 | "**Shipped:** Foundations §4.5, §4.5" | Old 6.1 and 6.2 both became §4.5. | Write "§4.5" once. |
| 7 | B1 | 1348 | "Value enters as feedback and pledges (§6)" | §6 is now the appendix. Pledges and feedback are §4.6; Foundations §0 points there. | Change "(§6)" to "(§4.6)". |
| 8 | B4 | 1393 | "**Shipped:** Foundations §6 (restructured)" | Old §6 became §4.5 and §4.6 (v0.28); the gate is §2.3. | Change to "Foundations §2.3, §4.5, §4.6". |
| 9 | B9 (β) | 1132 | "Credit is *time worked* (§6)" | §6 is the appendix. Credit is defined in §2.3 and credited in §4.5. | Change "(§6)" to "(§2.3)". |
| 10 | B11, Shipped line | 1294 | "Foundations §0, §6, §4.5, §4.6, §4.6→§4.2, §5.5" | §6 is the appendix. | Drop "§6"; the rest already names where the material lives. |
| 11 | B11, 3a section | 1334 | "public membership composition (Foundations §3.3a, conformance row 16)" | Membership composition is conformance row **16b**. Row 16 is the publish-every-method row. | Change "row 16" to "row 16b". |
| 12 | Status board, OP-26 | 77 | "`arithmetic_audits.py` now declares its own extent and blind spots per §5.4" | Foundations §5.4 is "Taxation is unnecessary". The extent and label rules are §4.4. | Change "§5.4" to "§4.4". |
| 13 | OA12, 2026-08-24 table | 503 | @manu's finding landed in "**Foundations §4** (boxed explainer + worked case…)" | The independence-versus-expressiveness box is §4.3. | Change "§4" to "§4.3". |
| 14 | OA12, 2026-08-24 table; Status board OP-26 | 502, 77 | The ladder's cost column and "the ~40% ceiling" are in "**Foundations §4.3**" | §4.3 keeps a three-rung example and says the full table and the measured threshold are in `01-wiki/verification-ladder.md`. The 40% figure is not in Foundations. | Point at "§4.3 and `01-wiki/verification-ladder.md`" for the ceiling figure. |
| 15 | OA12, residue 1 and §C | 526, 1440 | OA12 says "**Owed: a sim** comparing launder-via-genesis against honest recording" (line 531). | §C (Tests not yet run) does not list it, so it can be skipped silently, which §C exists to prevent. | Add it to §C as item 10, or mark it dropped with a reason. |
| 16 | OA12, 2026-08-24 pass | 520 | "`07-outreach/archive/` holds a copy of Foundations" | That folder no longer exists (CLAUDE.md: it was published by mistake and removed). The public copy is `07-outreach/latest-mirror/`, which is also absent in this checkout. | Say "the outreach agent's public copy (then `07-outreach/archive/`)" so a reader does not look for the folder. |
| 17 | B17 heading tag | 735 | `<!-- tag: obj-b16 -->` sits above "## B17" | B16 (line 794) then has no tag, and the knowledge-graph tag for B17 is wrong. | Rename the tag at 735 to `obj-b17` and add `<!-- tag: obj-b16 -->` above line 794. |
| 18 | B12 heading tag | 1181 | `<!-- tag: obj-b11 -->` sits above "## B12" | B11 (line 1291) carries the same tag, so two entries share one tag. | Rename the tag at 1181 to `obj-b12`. |
| 19 | OA9 status glyph | 410 | "**Status:** 🔽 Narrowed from a foundational conflict to an implementation question" | The Status board row for OP-22 (line 83) is 🟠 and calls it "the load-bearing privacy problem of the whole system". | Make OA9's glyph 🟠, matching the board. |
| 20 | OA0, class 1 row | 170 | "**OP-16** hazard half addressed (§4.6), tedium half open" | OA5 (line 290) and the board (line 78): both halves reachable by pledges since 2026-09-18, neither measured. | Change to "both halves reachable by pledges (§4.6), neither measured". |
| 21 | B14, two "owed" items | 1273, 1281, 1285 | "**Owed:** say this in Foundations §3.6 explicitly" · "**Owed:** one sentence in §3.2b" · "Two wording items are still unwritten" | Both shipped in Foundations v0.31 (2026-08-28). §3.6 rule 2 says "recorded once, not twice"; §3.2b has the box "Two things line 3 is not". | Mark both items ✅ shipped v0.31 and delete "still unwritten". |
| 22 | B13, note (3) | 935 | "It **may also close §3.4a's open residue**… **Not claimed until checked.**" | Checked and closed on 2026-09-09 (B17; Foundations §3.2c: "This convention also closes the residue §3.4a used to leave open"). | Change to "Checked 2026-09-09 and closed — B17." |
| 23 | B7, closing line | 1039 | "**labour** (→ OP-18, which now blocks C3)" and "**shared overhead** (→ OP-23)" | Both closed: OP-18 in B9 (2026-08-05), OP-23 in B8. | Change "which now blocks C3" to "closed in B9" and add "closed in B8". |
| 24 | B11, cluster item (4) | 1296 | "routing is a network lever; auto-pledge funds essentials" | B20 (2026-10-13) ruled a route is a standing pledge the subscriber must consent to; no auto-pledge exists (Foundations §4.6). | Change to "routing is a standing pledge a subscriber must accept (B20)". |

---

## Tier 2 — a sentence or a paragraph, no ruling needed

| # | Entry | Line | What it says | What the current document says | Proposed fix |
|--:|---|--:|---|---|---|
| 25 | Status board, OP-27 | 74 | "**Two residuals enter open: repeat-shell *entities* (→ OP-25 / C6) and template capture (→ OP-24 / OP-10).**" | B13 (line 923) closed repeat-shell entities on 2026-08-24 (Foundations §3.2c, conformance 2c); only a fake membership list survives, as a C6 verification question. | Rewrite the sentence: one residual open (template capture); shell entities closed 2026-08-24, see B13. |
| 26 | Status board, OP-10; OA2 item 2 | 75, 214 | "cost constants have a mechanism (§3.3a)" and "**Cost constants have a mechanism** — rival-sector audit, §3.3a and OA10" | Rival-sector audit was withdrawn on 2026-08-24 (OA3, line 248). Foundations §3.3a: "It does not supply the answer" and "Rival-sector audit… is not a mechanism". | In both places: "cost constants have five published requirements and no mechanism (§3.3a, conformance 16a–16c)". |
| 27 | OA3 status line and v0.6 box | 229, 233 | "**Status:** 🔴 Open. Fix proposed, unproven." and "Foundations §3.3a places them explicitly under rival-sector audit" | The same entry says the fix was withdrawn and the mechanism scoped out. §3.3a now puts the stock constants under the five requirements. | Status: "🔴 Open. Mechanism scoped to networks; five requirements in §3.3a; unproven." Box: "under §3.3a's five requirements". |
| 28 | Status board, OP-4 | 87 | "at ρ = 1.2 and 700 h/yr of essentials the minimum is 1.6 h/day" | Foundations §5.5.3 measured the baskets: narrow 516 – 655 h/yr gives 1.2 – 1.5 h/day; broad 826 – 965 h/yr gives 1.9 – 2.2 h/day (`06-simulation/essentials-basket/RESULTS.md`). 700 h/yr was the pre-measurement guess. | Replace with the measured baskets and their lowest floors. |
| 29 | B13 residual table | 943 | Template capture "Inherits OP-24's answer: the rival producer is the harmed party who funds the replication (§3.3a)." | OP-24 has no such answer since 2026-08-24; §3.3a says a rival's best move is to get its own constant set generously. | Change to "Inherits OP-24's status: an understated template has no funder; §3.3a's five requirements apply to a template as to any constant." |
| 30 | Status board, OP-9; OA8 | 82, 391 | "the `24/F ≈ 2.4×` ceiling" · "bounded by **24 ÷ F ≈ 2.4 ×**" · "bounded at about 2.4 ×" | Foundations §5.5.5: "Write the bound as `24 ÷ F`, never as its value at one floor… A sentence that states 2.4× as the result has pinned a free setting", and the figure to quote is about 1.6× at `F` = 10 for a very hard working life. | Write "`24 ÷ F` (2.4× at `F` = 10, a wall nobody reaches)". |
| 31 | OA8, worked-examples paragraph | 393 | "**Worked examples in Foundations §4.6** — four 0.5 h pledges… 5,000 likes convert to 500 h of backing… the surplus becoming a non-consumable reserve under §4.6… Design finding recorded there: a flat rate per like… 54,500 likes" | None of it is in Foundations §4.6 now; the examples moved to `01-wiki/pledge-and-signal.md` and `OP-9_calculation_reply.md` in v0.28. The non-consumable reserve was withdrawn 2026-09-18 (OA5, Foundations §4.6: surplus backing commits to whoever the criteria name). | Point the examples at the wiki page and the OP-9 paper, and replace the reserve clause with "the surplus commits to whoever the criteria name". |
| 32 | OA9, "more load-bearing" box | 433 | "That public market data is what makes **§3.3a rival-sector audit**… work at all" | Rival-sector audit is withdrawn. Public data still serves §3.3a's requirement 4 (public membership composition) and conformance 16b. | Change to "what makes §3.3a's public-composition check and independent monitoring work at all". |
| 33 | §0, OA1 and B9 — the team-debit residue | 137, 183, 1132 | "Responsibility across a team… survives only as the apportionment of a jointly-*caused debit*… minor, non-blocking" (three places) | Closed 2026-09-09: Foundations §3.2c divides a jointly caused debit by hours worked, scoped to acting for the organisation; B17 records "§3.4a's residue — Closed." | In all three places: "closed by §3.2c's hours convention, B17". |
| 34 | OA12, "third condition" and Status board OP-26 | 77, 500 | "The residual rule gains its **third condition** — *N* and *Y* must be scope-aligned" | Foundations §4.4 now lists two conditions; scope alignment is condition 2 of two ("Two conditions, and the leftover does not work without both"). | Say "the scope-alignment condition (now condition 2 of Foundations §4.4's two)". |
| 35 | §C test 8 | 1452 | "a −30% capacity disaster tightens clearing ρ\* ~1.25→~0.82" · "Aequitas caps **command-over-resources** at 2.4×, a 5–6 order-of-magnitude compression" | Foundations §5.5.7, anchor-tied: ρ\* = 0.33 at `F` = 10, a −30% shock tightens it to 0.19. "Command over resources" reads as a consumption bound, which §0a of this register forbids; the bound is on pledge budgets per day lived. | Update the two ρ\* figures with the date, and reword to "caps the demand lever (pledge budgets per day lived) at `24 ÷ F`". |

---

## Tier 3 — expensive: several entries together, a ruling, or a fold

| # | Entry | Line | What it says | What the current document says | Proposed fix |
|--:|---|--:|---|---|---|
| 36 | **B22 §2, Status board OP-4, §C test 9 — the every-payer re-run** | 572, 87, 1453 | "A re-run at the every-payer ratios **is requested**." · "a run on those inputs is requested (see B22)" · "Whether an upper edge exists there is not measured (B22)" | **The run landed on 2026-10-30**: `06-simulation/stable-band/RESULTS_PAYERS.md` (commit c18d04a). Germany/Japan: no upper edge at any `F` (entailed by the input, capacity 101.7% of wants). France: one-day ρ\* 2.365 / 0.612 / 0.459, cumulative 1.653 / 0.342 / 0.246. Sweden: 1.823 / 0.496 / 0.374, cumulative 1.656 / 0.337 / 0.242. Broad basket open at every `F` for all three under the scaling assumption. Declared outcome O9 **failed** (cumulative edge 9 – 46% below one-day). Foundations §5.5.3 and §5.5.7 still say "has not been run". | Fold the result into B22, the OP-4 row and §C test 9, and open a Foundations fold for §5.5.3 and §5.5.7. Needs an author ruling because O9 failed and the Germany/Japan "none" is entailed by the capacity input. |
| 37 | **Status board OP-1, B10, §C test 7 — what pledging costs the pledger** | 81, 1177, 1451 | OP-1: "The old 'self-starving' brake **is gone** — pledging no longer costs the pledger what they may carry (Foundations v0.13)". B10: "The 'self-starving' brake is **re-armed** under Foundations v0.14: pledging now spends a permanent, finite lifetime budget". §C 7: "the old brake is gone". | Foundations §3.0 and §4.6: a pledge draws from the pledger's lifetime budget and is spent once, but the pledger's `C` does not fall, so the pledger's own gate `D ≤ ρ·(C + P)` is unchanged. Both sentences are half right and the register says opposite things in three places. | One ruling on the sentence to use ("pledging spends influence budget and never consumption room"), then rewrite the three places to match. |
| 38 | **B7 — the withdrawn split rule is still presented as "The answer"** | 1004 – 1037 | The "NARROWED 2026-08-24" box says "**The mechanism below is unchanged and still closes OP-17**" and lists four obligations as "now stated as such (Foundations v0.22 §3.4a, conformance 10a)". "**The answer.**" then states "A joint process's debit divides according to where the process itself physically sent its inputs", tested on three instruments; the fallout table says manure "in the split" and "A §2.5 row was deleted rather than filled in". | Foundations §3.4a since v0.38: "A joint process's cost is not divided." Conformance 10a says the same. §2.5 now has a row for the case ("Not a convention either. It is refused"). The top box of B7 says the rule is withdrawn, but 35 lines below it the old rule is headed "The answer" with no marker. | Restructure B7: the 2026-09-03 and 2026-09-08 boxes become the entry, and everything from the "NARROWED" box to the "Two rules that were rejected" list moves under one heading "The record of the withdrawn split rule" with a `struck-ok` comment, as B12 already does. |
| 39 | **§0, the headline finding** | 125 – 147 | "OP-17's resolution shows why: a refinery's debit **does** divide across its fractions, because the cracking energy physically went somewhere and a meter can find it. The division was a measurement" · "§2.5 has now lost two rows rather than gaining entries" | §3.4a divides nothing; the refinery case is the worked case for refusing to divide (§2.5, third move). §2.5's table has five rows, two of them added since (an organisation's debit by hours; the floor's durations). The later paragraphs of §0 correct the first, so §0 argues with itself. | Rewrite §0's first two paragraphs around the three moves (measure · refuse · declare) with the refinery as the "refuse" case, and replace the §2.5 row-count sentence with the current five-row table. |
| 40 | **Status board closing paragraph — "Fifteen items closed; six live"** | 100 | "**Fifteen items closed; six live** — and in v0.17 the composition shifted twice… Original note: … Original note follows. **Fifteen items closed; six live.**" | The board above it has eleven live rows (🔴 2, 🟠 9) and seventeen closed items. The paragraph is three generations of revision commentary stacked, which CLAUDE.md sends to the changelog. The outreach agent will read this paragraph as the board's summary. | Replace with one current count (11 live: 2 red, 9 orange; 4 deferred; 17 closed) and one sentence on the pattern; move the three "original note" layers to `Aequitas_Objections_CHANGELOG.md`. |

---

## Three things checked that are not defects, recorded so nobody re-checks them

- **B9's "Shipped: Foundations v0.6 §2.5, §3.4a, §10"** and **B12's "Foundations v0.10 §3.2b + §12"** name sections that no longer exist (§10 was truncated 2026-08-25; §12 predates v0.28). Both are dated shipped pointers and both entries already say "superseded". Left as history.
- **OA7's "team debit shared by hours, not rank (§4.5)"** matches Foundations §5.1, which also says §4.5. The rule actually lives in §3.2c. That is a Foundations pointer, not a register defect, and Foundations is out of scope here.
- **The Status board's OP-28 row** says "the two rules that get the number right (S1, S2) are the two a network cannot run from one book" and cites Conformance v0.11. All of it still matches Foundations §4.4 and conformance rows 14 and 14d at v0.24.

## Done since the audit was written (same day)

| Row | What happened |
|--:|---|
| 36 | **Author ruled 2026-11-07: fold it, and re-run at `F` = 2, 6, 10, 16.** Run file `06-simulation/stable-band/PAYERS_F2-6-10-16_RUN.txt`; results `RESULTS_PAYERS_F2-6-10-16.md`. **Folded the same day, on "Yes, fold it":** Foundations v0.69 §5.5.3 and §5.5.7, Objections v0.52 (B22 §2, OP-4 row, §C test 9), Overview v0.37 §1. |
| 37 | **Fixed in the register, v0.53.** OP-1 row, B10 and §C test 7 all read "pledging spends influence budget and never consumption room", with the worked case in B10. |
| 1 – 24 | **Fixed in the register, v0.55.** All Tier 1 rows, in one pass. |
| 25 – 35 | **Fixed in the register, v0.56.** All Tier 2 rows, in one pass. **Every row of this audit is now closed.** |
| 40 | **Fixed in the register, v0.54.** The summary paragraph states the board's counts (2 red, 9 orange, 1 green, 5 deferred, 1 paused, 17 closed); the three old layers are in the register's changelog. |
| 38, 39 | **Fixed in the register, v0.51.** B7 restructured and §0 rewritten around the author's 2026-11-07 ruling on why a joint process's cost is not divided. Line numbers below line 125 in the register no longer match the table above. |
| 23 | Fixed inside the B7 rewrite. |
| 33 | Fixed in §0 only. OA1 (line 183) and B9 (line 1132) still carry the residue as open. |

## One follow-up outside this audit

Foundations §5.5.3 ("it has not been run") and §5.5.7 ("rescaled and not run") were contradicted by `06-simulation/stable-band/RESULTS_PAYERS.md` (2026-10-30). **Done: Foundations v0.69, 2026-11-07.**
