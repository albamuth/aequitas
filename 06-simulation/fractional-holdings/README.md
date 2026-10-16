# fractional-holdings

> **Version:** 0.1
> **Date:** 2026-10-13

**What does one account carry when it holds part of several co-products of one joint process?**

Foundations §3.4a states the rule for a whole co-product (a union over parcels) and for part of one parcel (a split by mass). It did not state it for parts of two co-products, such as 10% of the beef and 10% of the hide.

| | |
|---|---|
| **Status** | ✅ **Complete for its two cases.** 10/10 self-tests pass |
| **Result** | **"Max" passes every check.** Per step, an account carries the step's cost times the largest fraction of any co-product that passed it, counting what it consumed |
| **Rivals** | Independent overlap and the sum both fail the n-bundle check (row 10c). Max without the consumed-parts change fails the eater check |
| **Reuses** | The steer and refinery cases from [`../chain-resolution/`](../chain-resolution/) |
| **Full write-up** | [`RESULTS.md`](RESULTS.md) |

## Run it

```bash
python 06-simulation/fractional-holdings/fractional_holdings.py
```

```bash
python 06-simulation/fractional-holdings/fractional_holdings.py --test
```
