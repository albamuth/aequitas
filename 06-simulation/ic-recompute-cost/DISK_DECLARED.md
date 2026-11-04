# Declared before the disk run (2026-11-04, written before `disk_ratio.py` ran for the first time)

Ratio = re-weight seconds ÷ record-check seconds, nine checks (IC-5 sort included) unless marked "eight".
Primary disk arm = **disk-cold** (page cache bypassed, `FILE_FLAG_NO_BUFFERING`). `disk-warm` is reported beside it.

**Level outcomes (statements about the size of a number)**
- L1. The memory arm reproduces the single-generator figure: all-nine ratio **0.27 ± 0.07** (0.20–0.34), eight-check ratio **0.35 ± 0.07**, at k = 3. Outside that band = this stack's memory level disagrees with the project's published level, and the delta cannot be quoted against 0.27.
- L2. ratio_disk (cold, all nine) lies in **[0.27, 1.0)**. Above 1.0 = re-weighting costs more than checking once I/O is shared.
- L3. Cold read of the packed log runs at ≥ 0.5 GB/s of 34 B events (≥ 14.7 M events/s). Below that the device, not the CPU, sets both passes.

**Change outcomes (the request's pre-registered arms, with the spread made concrete)**
- A. |ratio_disk − ratio_memory| < the widest min-to-max range of either arm's repeats → shared I/O does not move the ratio.
- B. ratio_disk ≥ 0.9 → the memory ratio must not be quoted for a stored log.
- C. Between → NO VERDICT; report the interval.

**Size**: 10⁸ and 10⁹ events need 3.4 GB and 34 GB of log at 34 B/event; the budget is 1 GB of new files. They are not run. The largest sizes that fit are run (10⁷ = 340 MB, 2×10⁷ = 680 MB, deleted after each).
