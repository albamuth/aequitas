"""
Exit-step table -- the coarse-read / fine-read ratio as a COLUMN against exit
step, one row per co-product, each row recomputable from the chain table alone.

Request sr-20260911-over-a-real-multi-step-process-flow-sheet-ta (hemei c52152).

DEFINITIONS (all from chain_resolution.py; nothing new is modelled).
  coarse figure of product p  = (energy of ALL steps)     / mass_p   one opaque block
  fine figure of product p    = (energy of steps p passed) / mass_p   one block per step
  ratio_p = coarse / fine = TOTAL_ENERGY / PASSED_ENERGY_p     (mass cancels)
  exit step of p = the LAST step in processing order that p passed.

RECOMPUTABILITY. Each row prints: exit step, passed energy, total energy, ratio.
A reader holding only the chain table (step energies + passage matrix, printed
first) can redo every row with one division. `recompute_from_csv` does exactly
that from the written CSV alone, with no import of the model, and the self-test
compares it with the model path.

Run:  python exit_table.py            # both chains, then self-tests
      python exit_table.py --test
      python exit_table.py --csv exit_table.csv
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from chain_resolution import build_steer, build_refinery, Chain  # noqa: E402


def energy(chain: Chain, name: str) -> float:
    return chain.step(name).energy_mj


def table(chain: Chain, main_output: str) -> list[dict]:
    order = chain.step_names
    total = sum(energy(chain, n) for n in order)
    rows = []
    for p in chain.products:
        passed = [n for n in order if n in chain.passes[p]]
        exit_step = passed[-1]
        passed_e = sum(energy(chain, n) for n in passed)
        rows.append({
            "chain": chain.name,
            "product": p,
            "mass_kg": chain.mass_kg[p],
            "exit_index": order.index(exit_step) + 1,
            "exit_step": exit_step,
            "passed_steps": "+".join(passed),
            "passed_energy_mj": passed_e,
            "total_energy_mj": total,
            "coarse_mj_per_kg": total / chain.mass_kg[p],
            "fine_mj_per_kg": passed_e / chain.mass_kg[p],
            "ratio": total / passed_e,
            "is_main_output": p == main_output,
        })
    rows.sort(key=lambda r: (r["exit_index"], r["product"]))
    return rows


def summary(rows: list[dict]) -> dict:
    mx = max(rows, key=lambda r: r["ratio"])
    main = next(r for r in rows if r["is_main_output"])
    mw = sum(r["ratio"] * r["mass_kg"] for r in rows) / sum(r["mass_kg"] for r in rows)
    un = sum(r["ratio"] for r in rows) / len(rows)
    return {"max": mx["ratio"], "max_product": mx["product"],
            "main": main["ratio"], "main_product": main["product"],
            "mass_weighted_mean": mw, "unweighted_mean": un}


def print_chain_table(chain: Chain) -> None:
    print(f"  CHAIN TABLE: {chain.name}  ({chain.note})")
    order = chain.step_names
    head = f"  {'#':>2} {'step':<18}{'MJ':>10}  passed by"
    print(head)
    for i, n in enumerate(order, 1):
        who = ", ".join(p for p in chain.products if n in chain.passes[p])
        print(f"  {i:>2} {n:<18}{energy(chain, n):>10,.1f}  {who}")
    print(f"     {'TOTAL':<18}{sum(energy(chain, n) for n in order):>10,.1f}")
    print()


def print_rows(rows: list[dict]) -> None:
    print(f"  {'exit#':>5} {'exit step':<17}{'product':<15}{'mass kg':>9}"
          f"{'passed MJ':>11}{'total MJ':>10}{'coarse÷fine':>13}")
    for r in rows:
        star = "  <- main output" if r["is_main_output"] else ""
        print(f"  {r['exit_index']:>5} {r['exit_step']:<17}{r['product']:<15}"
              f"{r['mass_kg']:>9,.0f}{r['passed_energy_mj']:>11,.1f}"
              f"{r['total_energy_mj']:>10,.1f}{r['ratio']:>12.2f}x{star}")
    s = summary(rows)
    print(f"\n  max {s['max']:.2f}x ({s['max_product']}) · main output "
          f"{s['main_product']} {s['main']:.2f}x · mass-weighted mean "
          f"{s['mass_weighted_mean']:.2f}x · unweighted mean {s['unweighted_mean']:.2f}x\n")


def write_csv(rows: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def recompute_from_csv(text: str) -> dict[tuple[str, str], float]:
    """Second path: sees ONLY the CSV text. Redoes ratio = total / passed from
    the two energy columns, and ignores the stored ratio column."""
    out = {}
    for r in csv.DictReader(io.StringIO(text)):
        out[(r["chain"], r["product"])] = float(r["total_energy_mj"]) / float(r["passed_energy_mj"])
    return out


CASES = [(build_steer, "packaged_beef"), (build_refinery, "gasoline")]


# --------------------------------------------------------------------------
# Self-tests. Each can fail.
# --------------------------------------------------------------------------

def test_ratio_at_least_one() -> str:
    n = 0
    for b, m in CASES:
        for r in table(b(), m):
            assert r["ratio"] >= 1.0 - 1e-12, f"{r['product']} ratio {r['ratio']} < 1"
            n += 1
    return f"ratio >= 1 on all {n} rows"


def test_csv_recompute_matches_model() -> str:
    n = 0
    for b, m in CASES:
        rows = table(b(), m)
        got = recompute_from_csv(write_csv(rows))
        for r in rows:
            assert abs(got[(r["chain"], r["product"])] - r["ratio"]) < 1e-12
            n += 1
    return f"{n} rows recomputed from the CSV alone match the model path"


def test_recompute_can_fail() -> str:
    """Negative control: corrupt one passed-energy cell; the recompute must disagree."""
    rows = table(build_steer(), "packaged_beef")
    text = write_csv(rows).replace("80.0,500.0", "90.0,500.0", 1)
    got = recompute_from_csv(text)
    bad = [r for r in rows if abs(got[(r["chain"], r["product"])] - r["ratio"]) > 1e-9]
    assert bad, "corrupting a cell changed nothing -- the recompute is not reading it"
    return "a corrupted cell is caught by the recompute"


def test_terminal_product_is_one() -> str:
    rows = table(build_steer(), "packaged_beef")
    beef = next(r for r in rows if r["product"] == "packaged_beef")
    assert abs(beef["ratio"] - 1.0) < 1e-12 and beef["exit_index"] == 7
    return "steer main output exits at step 7 and reads exactly 1.00x"


def test_mass_cancels() -> str:
    """The ratio must not depend on any mass (universality guard, as in chain_resolution)."""
    for b, m in CASES:
        c = b()
        before = {r["product"]: r["ratio"] for r in table(c, m)}
        for q in c.products:
            c.mass_kg[q] *= 3.7
        after = {r["product"]: r["ratio"] for r in table(c, m)}
        for p in before:
            assert abs(before[p] - after[p]) < 1e-12, f"{p} ratio depends on mass"
    return "no ratio depends on any mass; only the weighted mean does"


def test_weighted_mean_moves_with_mass() -> str:
    c = build_steer()
    a = summary(table(c, "packaged_beef"))["mass_weighted_mean"]
    c.mass_kg["hide"] *= 10
    b = summary(table(c, "packaged_beef"))["mass_weighted_mean"]
    assert abs(a - b) > 0.1, "mass-weighted mean ignored mass"
    return "mass-weighted mean responds to mass (it is not secretly unweighted)"


def test_matches_chain_resolution_results() -> str:
    """Level check against the committed 6.25x energy figure for the hide."""
    hide = next(r for r in table(build_steer(), "packaged_beef") if r["product"] == "hide")
    assert abs(hide["ratio"] - 6.25) < 1e-9, f"hide {hide['ratio']}"
    ref = {r["product"]: r["ratio"] for r in table(build_refinery(), "gasoline")}
    assert abs(ref["gasoline"] - 1.25) < 0.005 and abs(ref["asphalt"] - 2.56) < 0.005
    return "hide 6.25x, refinery gasoline 1.25x and asphalt 2.56x agree with RESULTS.md"


TESTS = [test_ratio_at_least_one, test_csv_recompute_matches_model,
         test_recompute_can_fail, test_terminal_product_is_one, test_mass_cancels,
         test_weighted_mean_moves_with_mass, test_matches_chain_resolution_results]


def run_tests() -> int:
    print("\nSELF-TESTS\n" + "-" * 78)
    failed = 0
    for t in TESTS:
        try:
            print(f"  PASS  {t()}")
        except AssertionError as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print("-" * 78 + f"\n  {len(TESTS) - failed}/{len(TESTS)} passed\n")
    return failed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--csv", metavar="PATH")
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)
    allrows = []
    for b, m in CASES:
        c = b()
        print("=" * 78)
        print_chain_table(c)
        rows = table(c, m)
        print_rows(rows)
        allrows += rows
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            fh.write(write_csv(allrows))
        print(f"  wrote {a.csv} ({len(allrows)} rows)")
    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
