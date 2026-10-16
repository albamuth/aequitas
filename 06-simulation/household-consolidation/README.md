# Household consolidation

> **Version:** 0.1
> **Date:** 2026-10-16

**What it is.** Sizes the lever @Wubbitys found on post #8335 (c100994): under the max rule for fractional holdings (Foundations §3.4a, conformance row 10i), two adults who put different co-products of one joint process on different accounts carry more than one account holding both. This project asks how much, over a realistic two-adult basket.

**It extends [`../fractional-holdings/`](../fractional-holdings/).** The rule is `fractional_holdings.debit`, imported unchanged. The refinery passage table and masses come from [`../chain-resolution/`](../chain-resolution/) and [`../allocation-engine/refinery_slice.py`](../allocation-engine/refinery_slice.py).

**Run.**

```
python 06-simulation/household-consolidation/household_consolidation.py --test   # 8 self-tests
python 06-simulation/household-consolidation/household_consolidation.py          # the sweep
```

**Files.** [`DECLARED.md`](DECLARED.md) holds the outcomes written before running. [`RESULTS.md`](RESULTS.md) holds the numbers.

**Status.** Written 2026-10-16. **Not yet executed**: Python was refused on the night it was written. The figures in `RESULTS.md` are hand arithmetic.
