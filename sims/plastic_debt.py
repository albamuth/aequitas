"""
plastic_debt.py -- Q3 of the scenario suite: the labour debt of plastic.

Question (author, 2026-08-10): what is the labour debt of plastic pollution
(cleanup time per ton)? What is the recycling cost?

TYPE: physical feasibility / LCA envelope. Instantiates:
  - Foundations §3.2a  debit is a VECTOR (energy + labour reported separately)
  - Foundations §3.3   a flow is pollution only ABOVE the rate nature clears it;
                       weight = total remediation (removal + resident damage)
  - Foundations §3.6   product-as-pollution, recycling traces material forward
                       but NOT prior producers' pollution; recyclers are credited

We report each stage of a tonne of common plastic as a two-component debit:
  * ENERGY  (MJ/kg)  -- the LCA-measured physical quantity, virgin vs recycled
  * LABOUR  (h/ton)  -- via the project's standard cost->labour bridge:
                        hours = (cost $/ton) x (economy embodied hours per $),
                        the same bridge track3/track4 use. Economy-average
                        ~0.010 h/$ (US ~160M jobs / ~$27T final demand x 1,750
                        h/job / 1e6 -- consistent with track1's ERM).

THE STOCK RULE IS THE HEADLINE (§3.3). Plastic's natural clearance rate over
human timescales is ~0 (persists centuries), so a discarded plastic is ALWAYS
"above baseline": its carried pollution-debit ~= the full remediation cost, and
it stays on the last holder until someone actually cleans it. For macro debris
that is ~ocean-cleanup cost; for MICROPLASTIC there is no scalable remediation,
so the debit is effectively unbounded / near-permanent. That is not a bug in the
model -- it is the quantitative form of "you own the end of a thing's life."

DATA ANCHORS (real, cited in-line):
  - Virgin cumulative energy demand (MJ/kg): PlasticsEurope eco-profiles /
    Franklin Assoc. for APR (2018/2020 LCI). PET ~69, HDPE ~76, PP ~73, LDPE ~78.
  - Mechanical-recycling energy saving vs virgin (Franklin/APR 2018 LCA):
    PET 79%, HDPE 88%, PP 88%.  https://plasticsrecycling.org (APR LCI report)
  - Great Pacific Garbage Patch: ~79,000 t (Lebreton et al. 2018, Sci. Reports
    s41598-018-22939-w); The Ocean Cleanup: $7.5B to clear it
    -> ~$95,000/ton. https://theoceancleanup.com/press/press-releases/
  - US average landfill tipping fee ~$55/ton (EREF).

Run:  python plastic_debt.py
      python plastic_debt.py --test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field


@dataclass(frozen=True)
class PlasticParams:
    # --- virgin cumulative energy demand, MJ/kg (LCA eco-profiles) ---
    virgin_energy: dict = field(default_factory=lambda: {
        "PET":  69.0,   # 2020 revision ~61.4; older ~84; 69 is a defensible mid
        "HDPE": 76.0,
        "PP":   73.0,
        "LDPE": 78.0,
    })
    # --- mechanical recycling energy saving vs virgin (Franklin/APR 2018) ---
    mech_recycle_saving: dict = field(default_factory=lambda: {
        "PET":  0.79,
        "HDPE": 0.88,
        "PP":   0.88,
        "LDPE": 0.88,   # ~PP/HDPE class; APR groups the polyolefins
    })
    # Chemical recycling (pyrolysis) is energy-hungry: net energy well ABOVE
    # mechanical and often a large fraction of virgin. Modelled as a fraction of
    # virgin energy; wide uncertainty, flagged. (Literature spans ~0.4-0.9.)
    chem_recycle_frac_of_virgin: float = 0.55

    # --- cost anchors, $/ton (A5: price == cost) ---
    virgin_price: float = 1_300.0      # representative PET/HDPE/PP ~$1.2-1.6/kg
    mech_process_cost: float = 400.0   # collection/sort/wash/reprocess (processing, not market rPET price)
    chem_process_cost: float = 1_000.0 # pyrolysis operating cost, order of magnitude
    landfill_cost: float = 55.0        # US avg tipping fee $/ton (EREF)
    coastal_cleanup_cost: float = 5_000.0   # beach/coastal cleanup, mid of a wide literature range
    ocean_cleanup_cost: float = 95_000.0    # GPGP: $7.5B / 79,000 t

    # --- the cost->labour bridge (economy-average embodied hours per $) ---
    h_per_dollar: float = 0.010

    # Microplastic remediation: no scalable technology exists. Represented as
    # unbounded (None) -- §3.3 weight stays near-maximal because natural
    # clearance ~ 0. Reported qualitatively, never as a finite headline number.
    microplastic_remediable: bool = False


def _hours(cost_per_ton: float, p: PlasticParams) -> float:
    """Cost->labour bridge: $/ton x economy embodied h/$ = h/ton."""
    return cost_per_ton * p.h_per_dollar


def compute(p: PlasticParams | None = None):
    p = p or PlasticParams()

    # --- energy vector (MJ/kg), virgin vs mechanical-recycled, per resin ---
    energy = {}
    for resin, ve in p.virgin_energy.items():
        rec = ve * (1.0 - p.mech_recycle_saving[resin])
        energy[resin] = dict(virgin=ve, mech_recycled=rec,
                             chem_recycled=ve * p.chem_recycle_frac_of_virgin,
                             saving=p.mech_recycle_saving[resin])
    virgin_avg = sum(v["virgin"] for v in energy.values()) / len(energy)
    mech_avg = sum(v["mech_recycled"] for v in energy.values()) / len(energy)

    # --- labour vector (h/ton) via the $-bridge ---
    labour = dict(
        virgin_production=_hours(p.virgin_price, p),
        mech_recycling=_hours(p.mech_process_cost, p),
        chem_recycling=_hours(p.chem_process_cost, p),
        landfill=_hours(p.landfill_cost, p),
        coastal_cleanup=_hours(p.coastal_cleanup_cost, p),
        ocean_cleanup=_hours(p.ocean_cleanup_cost, p),
    )

    # --- ratios that make the §3.6 incentive gradient explicit ---
    ratios = dict(
        ocean_vs_production=labour["ocean_cleanup"] / labour["virgin_production"],
        ocean_vs_recycling=labour["ocean_cleanup"] / labour["mech_recycling"],
        production_vs_recycling=labour["virgin_production"] / labour["mech_recycling"],
    )

    return dict(energy=energy, virgin_avg=virgin_avg, mech_avg=mech_avg,
                labour=labour, ratios=ratios, p=p)


def report(p: PlasticParams | None = None):
    p = p or PlasticParams()
    r = compute(p)
    W = 78
    print("=" * W)
    print("Q3 -- THE LABOUR DEBT OF PLASTIC   (debit as a vector: energy + labour)")
    print("=" * W)

    print("\n[1] ENERGY debit -- MJ/kg  (LCA-measured; the recycling win is an energy win)")
    print(f"  {'resin':6} {'virgin':>8} {'mech-rec':>9} {'saving':>7} {'chem-rec':>9}")
    for resin, e in r["energy"].items():
        print(f"  {resin:6} {e['virgin']:8.0f} {e['mech_recycled']:9.1f} "
              f"{e['saving']*100:6.0f}% {e['chem_recycled']:9.1f}")
    print(f"  {'avg':6} {r['virgin_avg']:8.0f} {r['mech_avg']:9.1f}")
    print("  -> mechanical recycling uses ~12-21% of virgin energy; chemical (pyrolysis)")
    print("     is far hungrier (~55% of virgin here, wide uncertainty).")

    L = r["labour"]
    print("\n[2] LABOUR debit -- h/ton  (via cost x economy embodied hours/$ = "
          f"{p.h_per_dollar:.3f})")
    print(f"  virgin production     : {L['virgin_production']:8.1f} h/ton")
    print(f"  mechanical recycling  : {L['mech_recycling']:8.1f} h/ton   (recycler is CREDITED, §3.6)")
    print(f"  chemical recycling    : {L['chem_recycling']:8.1f} h/ton")
    print(f"  landfill (managed)    : {L['landfill']:8.1f} h/ton")
    print(f"  coastal cleanup       : {L['coastal_cleanup']:8.1f} h/ton")
    print(f"  OCEAN macro-cleanup   : {L['ocean_cleanup']:8.1f} h/ton   <- GPGP $95k/ton")
    print(f"  MICROPLASTIC          :   UNBOUNDED  -- no scalable remediation (§3.3)")

    R = r["ratios"]
    print("\n[3] THE INCENTIVE GRADIENT (§3.6 falls straight out of the ratios):")
    print(f"  ocean cleanup is {R['ocean_vs_production']:5.0f}x the labour to PRODUCE virgin plastic")
    print(f"  ocean cleanup is {R['ocean_vs_recycling']:5.0f}x the labour to RECYCLE it mechanically")
    print(f"  producing virgin is {R['production_vs_recycling']:4.1f}x recycling it")

    print("\n[4] THE STOCK RULE IS THE ANSWER TO 'labour debt of plastic pollution' (§3.3):")
    print("  Plastic's natural clearance ~ 0 over human timescales -> a discarded")
    print("  plastic is ALWAYS above baseline, so its carried pollution-debt ~= the")
    print("  FULL remediation cost, permanently, on the last holder until cleaned:")
    print(f"     macro debris in the ocean : ~{L['ocean_cleanup']:.0f} h/ton, carried until removed")
    print( "     microplastic              :  effectively unbounded / near-permanent")
    print("  Recycling DISCHARGES that debt for a few h/ton and returns the material")
    print("  as a low-cost co-input carrying none of the driller's pollution (§3.6).")
    print("=" * W)
    return r


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------

def test_recycling_energy_win():
    """Mechanical recycling must use far less energy than virgin, per resin."""
    r = compute()
    for resin, e in r["energy"].items():
        assert e["mech_recycled"] < 0.25 * e["virgin"], f"{resin} recycling not a big win"
    print(f"[ok] mechanical recycling ~{r['mech_avg']:.0f} vs virgin ~{r['virgin_avg']:.0f} MJ/kg")


def test_cleanup_dominates():
    """Ocean cleanup labour must dwarf both production and recycling (the gradient)."""
    r = compute()
    assert r["ratios"]["ocean_vs_production"] > 20, "ocean cleanup should be >>20x production"
    assert r["ratios"]["ocean_vs_recycling"] > 50, "ocean cleanup should be >>50x recycling"
    print(f"[ok] ocean cleanup {r['ratios']['ocean_vs_production']:.0f}x production, "
          f"{r['ratios']['ocean_vs_recycling']:.0f}x recycling")


def test_production_costlier_than_recycling():
    """Producing virgin should cost more labour than recycling (else no incentive)."""
    r = compute()
    assert r["ratios"]["production_vs_recycling"] > 1.0
    print(f"[ok] virgin production {r['ratios']['production_vs_recycling']:.1f}x recycling labour")


def test_microplastic_unbounded():
    """Microplastic must be flagged non-remediable (near-permanent debit, §3.3)."""
    assert PlasticParams().microplastic_remediable is False
    print("[ok] microplastic flagged unbounded / near-permanent (no finite headline)")


def test_bridge_monotone():
    """Higher $ cost -> more labour-hours (the bridge is a positive scaling)."""
    p = PlasticParams()
    assert _hours(p.ocean_cleanup_cost, p) > _hours(p.landfill_cost, p)
    print("[ok] cost->labour bridge is monotone (ocean >> landfill)")


def run_tests():
    test_recycling_energy_win()
    test_cleanup_dominates()
    test_production_costlier_than_recycling()
    test_microplastic_unbounded()
    test_bridge_monotone()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
