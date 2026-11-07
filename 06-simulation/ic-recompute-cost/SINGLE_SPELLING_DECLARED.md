# Declared before the run (2026-11-07, written before `single_spelling.py` ran for the first time, self-tests only)

Ratio = re-weight seconds ÷ record-check seconds, k = 3. "Nine" = IC-5's sort included; "eight" = the streaming checks only. Every arm uses ONE packed 34-byte record that BOTH passes parse. Primary disk arm = cache-bypassed.

**What I expect, from the 2026-11-04 run on this machine (memory 0.355 nine / 0.416 eight; disk 0.457 / 0.522 at 2×10⁷):** the memory level will NOT reproduce 0.27, because that run already showed the packed-record parse costs the re-weight proportionally more. I am declaring the level cells anyway, because a cell that cannot fail is not a cell.

**Level outcomes (statements about the size of a number)**
- **L1.** mem-fresh at ~10⁸, nine checks: ratio in **[0.22, 0.32]** (0.27 ± 0.05). Outside it = the published 0.27 does not reproduce under one spelling on this stack. **I predict outside, at about 0.33–0.38.**
- **L2.** mem-fresh at ~10⁸, eight checks: ratio in **[0.30, 0.40]** (0.35 ± 0.05).
- **L3.** Length: |ratio(~10⁹) − ratio(~10⁸)| < **0.03** in the mem-fresh arm, both nine and eight. Outside = the 0.27 is a length-dependent reading.
- **L4.** disk-cold, nine checks, lies in **[0.40, 0.52]** at both lengths (the 2×10⁷ run read 0.457).
- **L5.** Replay control: |mem-replay − mem-fresh| at ~10⁸ < **0.03** (nine and eight). If it fails, the replay is not a valid stand-in for a stored log of distinct events, and the disk figures at 10⁸ and 10⁹ are a proxy that must be labelled so.

**Change outcomes**
- **A.** delta (disk-cold − mem-replay, same bytes) at ~10⁸, nine checks: **≥ +0.05 and larger than the widest min–max range** of either arm. Else shared I/O does not move the ratio.
- **B.** ratio_disk (nine) ≥ 0.9 → the memory ratio must not be quoted for a stored log.
- **C.** Between A and B → report the interval, no verdict on "the" disk ratio.

**Sizes.** 10⁸ ≈ 49 chunks = 100,352,000 events; 10⁹ ≈ 488 chunks = 999,424,000 events. Neither is a stored 3.4 GB or 34 GB log: the budget is 1 GB of new files. The disk arm replays one 836 MB file (12 chunks). The memory-fresh arm generates and packs each chunk untimed and streams it through RAM.
