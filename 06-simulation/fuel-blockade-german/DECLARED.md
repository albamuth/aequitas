# Declared before running (2026-11-14)

Request `sr-20261111-fuel-blockade-at-the-german-method-same-popu`. Written before `shares.py` or `fuel_blockade.py` was run.

**Fossil share of a product** = value of fossil-energy products bought as inputs by the German producer of that product, over its total output (EXIOBASE 3.10.2 pxp 2022, `Z.txt` and `x.txt`). Fossil products: coal and peat (19-26), crude oil, natural gas, NGL, other hydrocarbons (27-30), coke and coal tar (63-65), refined petroleum products (66-83), electricity by coal, gas and oil (127, 128, 132), manufactured gases (141-144), gas distribution (146). The energy extension on disk (`energy/F.txt`) has four total rows ("Energy use - Emission relevant / Final / Gross / Net", TJ) and **no carrier split**, so it cannot give a fossil share. It is used only as an independent cross-check (self-test).

**Output fall of a line** = cut x fossil share of the line (the request's rule), weighted by German household final demand inside the line.

**Capacity is per line.** Services, essentials goods and non-essential goods each keep 101.7% of their own wants, times (1 - their own fall). Spare capacity in one line cannot serve another line.

| # | Statement | Kind |
|---|---|---|
| 1 | At each of the four cuts, the essentials goods line falls less than the non-essentials line | change (ordering) |
| 2 | At the 50% cut, the overall output loss is between 1% and 10% | **level** |
| 3 | At the 50% cut, the essentials goods fall is between 0.5% and 6% | **level** |
| 4 | The flag "none: ungated part exceeds capacity" fires at the 50% cut at every F and both E, and does not fire at the 10% cut | **level** (it fires when the ungated fall passes 1.67%, see below) |
| 5 | The author's declaration: clearing rho at a given overall loss is no lower than under the even cut | change |

**Outcome 5 is expected to FAIL, by algebra written down before the run.** Let U = ungated demand (services plus essentials), N = gated demand, W = U + N, C = 1.017. Even cut: the gated part may admit C·W·(1-L) - U. Per-line cut: it may admit C·N·(1-f_n). The difference (per-line minus even) is **U·(C·f_u - 0.017)**, where f_u is the fall of the ungated lines. So when f_u is under 1.67% the per-line target is lower and the clearing rho is lower; when f_u is over 1.67% the ungated lines are short and the flag fires first. **No value of the inputs gives a per-line rho above the even-cut rho.** Under the section 4c rule of the brief this comparison is model-entailed: the verdict is fixed by the line-separate capacity assumption, not by the German data. It is reported, marked entailed, and not counted as evidence about fuel. The even cut at the same overall loss equals a per-line cut with pooled capacity (identity, self-test 4).

Statement 4 is the one with data in it: it depends on whether the German ungated lines' fall crosses 1.67% at a 50% cut.
