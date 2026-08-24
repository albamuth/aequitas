# Expected verdicts — `arithmetic_audits.py`

**Generated file. Do not hand-edit.** Regenerate with:

```
python 06-simulation/audits_inert/generate.py
```

Source: `arithmetic_audits.py`, SHA-256 `06e3af74e9df7c6fa7600effe0bf46a6cb2a5ca41044edcae8edc3315ff8b329`.
Generated 2026-08-24T13:57:21Z.

The constraints these verdicts test are written out in [`constraints.md`](constraints.md). The data they run over is [`fixture.json`](fixture.json). Every quantity summed on the clean log is in [`worked_arithmetic.json`](worked_arithmetic.json).

---

## 1. The clean log

| IC | name | verdict | what the program prints |
|---|---|---|---|
| IC-1 | mass balance | **PASS** | `all events mass-balance` |
| IC-2 | energy balance | **PASS** | `all events energy-balance` |
| IC-3 | origin closure | **PASS** | `every parcel traces to a reservoir or a genesis entry` |
| IC-4 | fate closure | **PASS** | `every parcel is held/consumed/released` |
| IC-5 | custody continuity | **PASS** | `custody chains are single-valued and continuous` |
| IC-6 | interval sanity | **PASS** | `no event acts on a parcel outside its lifetime` |
| IC-7 | agent-time cap | **PASS** | `no account exceeds 24h work per 24h` |
| IC-8 | pledge backing | **PASS** | `no account over-pledges its lifetime earned credit` |
| IC-9 | pledge discharge | **PASS** | `discharges reference real events, none after a burn; no object forced on the pledger` |
| IC-10 | non-negative allocation | **PASS** | `theta>=0 and recursive min(p)=0.0000>=0 (rho=0.980)` |
| IC-11 | exhaustive allocation | **PASS** | `every joint split is exhaustive (theta sums to 1) in each dim` |
| IC-12 | boundary additivity | **PASS** | `whole==staged: flour 0.80000, bran 0.80000 (max d=0.0e+00)` |

---

## 2. The twelve injected logs

One row per injection. **Fires** is the constraint that is supposed to catch it. **Also fires** lists any other constraint that happens to fail on the same corrupted log — a corruption is not obliged to break exactly one thing.

| # | target | what was changed | fires | also fires |
|---|---|---|---|---|
| INJ-1 | IC-1 | E6 (baking) bread output raised from 9.5 kg to 10.5 kg. | **FAIL** | — |
| INJ-2 | IC-2 | E6 (baking) declared dissipation dropped from 200 J to 0 J. | **FAIL** | — |
| INJ-3 | IC-3 | E6's flour input renamed to a parcel no event creates, and E5's output renamed too so the chain is broken rather than merely relabelled. | **FAIL** | — |
| INJ-4 | IC-4 | E4 sends the bran to 'void:unregistered-sink', an endpoint absent from the reservoir registry. | **FAIL** | — |
| INJ-5 | IC-5 | E3 (milling) declares its grain input was held by 'stranger'. | **FAIL** | — |
| INJ-6 | IC-6 | E6 (baking) moved back one day, so it consumes flour before milling produces it. | **FAIL** | — |
| INJ-7 | IC-7 | The farmer's two roles are stretched to 20 h and 10 h and made to overlap, claiming 30 h inside one 24 h window. | **FAIL** | — |
| INJ-8 | IC-8 | Pledge PL3 raised from 2 h to 100 h. | **FAIL** | — |
| INJ-9 | IC-9 | PL1's expiry pulled back to day 5, so the event that discharges it on day 6 happens after the pledge had already burned. | **FAIL** | — |
| INJ-10 | IC-10 | The published energetics model for milling is set to flour 1.1, bran -0.1. | **FAIL** | — |
| INJ-11 | IC-11 | The published energetics model for milling is set to flour 0.6, bran 0.3, summing to 0.9. | **FAIL** | — |
| INJ-12 | IC-12 | The sieve stage is re-split 0.8 / 0.2 while the whole process keeps 0.7 / 0.3. No event log is touched -- IC-12 does not read one. | **FAIL** | — |

### What fails to balance, and by how much

| # | target | where | quantity | expected | actual | off by | unit |
|---|---|---|---|---|---|---|---|
| INJ-1 | IC-1 | `E6` | mass in - mass out | 0 | -1 | **-1** | kg |
| INJ-2 | IC-2 | `E6` | energy in - (energy out + dissipation) | 0 | 200 | **200** | J |
| INJ-3 | IC-3 | `P:bread` | count of valid origin termini | 1 | 0 | **1** | termini (a count, not a balance) |
| INJ-4 | IC-4 | `P:bran` | mass whose fate the log does not name | 0 | 3 | **3** | kg |
| INJ-5 | IC-5 | `P:grain@E3` | declared source holder | miller | stranger | **identity mismatch (not a numeric residual)** | account name |
| INJ-6 | IC-6 | `E6 consumes P:flour` | event start - parcel creation instant | >= 0 | -86400 | **86400** | seconds early |
| INJ-7 | IC-7 | `farmer in the 24 h window from t=0.0` | credited hours inside one 24 h window | 24 | 30 | **6** | hours |
| INJ-8 | IC-8 | `farmer` | cumulative pledged hours - lifetime earned hours | <= 0 | 96.75 | **96.75** | hours |
| INJ-9 | IC-9 | `PL1 discharged by E10` | discharge instant - expiry instant | <= 0 | 86400 | **86400** | seconds after the pledge had burned |
| INJ-10 | IC-10 | `E3[energy] P:bran` | allocated share theta | >= 0 | -0.1 | **0.1** | share (dimensionless) |
| INJ-11 | IC-11 | `E3[energy]` | sum of allocated shares theta | 1 | 0.9 | **-0.1** | share (dimensionless) |
| INJ-12 | IC-12 | `flour per-unit debit` | whole-process debit - staged debit | 0 | -0.1142857143 | **0.1142857143** | hours per kg |
| INJ-12 | IC-12 | `bran per-unit debit` | whole-process debit - staged debit | 0 | 0.2666666667 | **0.2666666667** | hours per kg |

### The message each check prints when it fires

| # | message |
|---|---|
| INJ-1 | `E6: mass in 10.0 != out 11.0` |
| INJ-2 | `E6: energy in 200.0 != out 0 + dissipation 0.0` |
| INJ-3 | `parcel P:bread has no reservoir/genesis ancestry` |
| INJ-4 | `unaccounted parcels: ['P:bran']` |
| INJ-5 | `P:grain@E3: claims holder stranger, actually miller` |
| INJ-6 | `E6 consumes P:flour before it exists` |
| INJ-7 | `farmer: 30.0h in a 24h window from 0.0` |
| INJ-8 | `farmer: cumulative pledges 103.0h > lifetime earned 6.25h` |
| INJ-9 | `pledge PL1: discharged by E10 at 540000.0 after expiry 453600.0 -- it had already burned` |
| INJ-10 | `E3[energy]: theta[P:bran] = -0.1 < 0` |
| INJ-11 | `E3[energy]: theta sums to 0.8999999999999999, not 1 (dimension unallocated)` |
| INJ-12 | `whole vs staged diverge: flour 0.80000 vs 0.91429 (d=1.14e-01), bran 0.80000 vs 0.53333 (d=2.67e-01)` |

---

## 3. Exactly what each injection changes

Derived by comparing the injected log against the clean one, field by field. Not written by hand.

**INJ-1 → IC-1**

- `events.E6.outputs[0].magnitude`: `9.5` → `10.5`

**INJ-2 → IC-2**

- `events.E6.dissipation_j`: `200` → `0`

**INJ-3 → IC-3**

- `events.E5.outputs[0].endpoint_id`: `P:flour` → `P:phantom-orphan`
- `events.E6.inputs[0].endpoint_id`: `P:flour` → `P:phantom-flour`

**INJ-4 → IC-4**

- `events.E4.outputs[0].endpoint_id`: `soil:field-01` → `void:unregistered-sink`

**INJ-5 → IC-5**

- `events.E3.inputs[0].custody`: `miller` → `stranger`

**INJ-6 → IC-6**

- `events.E6.end_day`: `4.416667` → `1.416667`
- `events.E6.end_s`: `381600` → `122400`
- `events.E6.start_day`: `4.25` → `1.25`
- `events.E6.start_s`: `367200` → `108000`

**INJ-7 → IC-7**

- `events.E1.agents[0].end_day`: `0.5` → `0.833333`
- `events.E1.agents[0].end_s`: `43200` → `72000`
- `events.E1.agents[0].hours`: `6` → `20`
- `events.E1.agents[0].start_day`: `0.25` → `0`
- `events.E1.agents[0].start_s`: `21600` → `0`
- `events.E8.agents[0].end_day`: `5.510417` → `0.625`
- `events.E8.agents[0].end_s`: `476100` → `54000`
- `events.E8.agents[0].hours`: `0.25` → `10`
- `events.E8.agents[0].start_day`: `5.5` → `0.208333`
- `events.E8.agents[0].start_s`: `475200` → `18000`

**INJ-8 → IC-8**

- `pledges.PL3.hours`: `2` → `100`

**INJ-9 → IC-9**

- `pledges.PL1.expires_at_day`: `30.25` → `5.25`
- `pledges.PL1.expires_at_s`: `2613600` → `453600`

**INJ-10 → IC-10**

- `energetics_model.proc:milling.sub:wheat.bran`: `0.38` → `-0.1`
- `energetics_model.proc:milling.sub:wheat.flour`: `0.62` → `1.1`

**INJ-11 → IC-11**

- `energetics_model.proc:milling.sub:wheat.bran`: `0.38` → `0.3`
- `energetics_model.proc:milling.sub:wheat.flour`: `0.62` → `0.6`

**INJ-12 → IC-12**

- not a log change: `staged_theta` = `[0.8, 0.2]`
- no field of the event log differs from the clean fixture

---

## 4. Where the Python and the stated mathematics disagree

Found while writing `constraints.md` against the code. Recorded, not papered over.

**N1 — check_ic12_boundary_additivity, arithmetic_audits.py**

- *Finding:* IC-12 takes the event log as its first argument and never uses it. Its numbers come from a milling decomposition hard-coded inside `_milling_debit`: cultivation 6 h making 10 kg of grain, then either one 2 h milling step or a 1 h grind plus a 1 h sieve. Nothing in fixture.json can change the IC-12 row.
- *Consequence:* A reader checking IC-12 must check the numbers in constraints.md section IC-12, not the fixture.

**N2 — check_ic10_nonneg_allocation, arithmetic_audits.py**

- *Finding:* IC-10 returns FAIL for two different reasons: a negative allocated share, and an economy whose spectral radius is not below 1 so the solver is undefined. Only the first is a negative allocation.
- *Consequence:* A FAIL on IC-10 does not by itself mean a share went negative. The message distinguishes them; the verdict does not.

**N6 — check_ic2_energy_balance docstring**

- *Finding:* The docstring states the constraint without its genesis exemption. The code exempts genesis entries from IC-2 as well as from IC-1.
- *Consequence:* constraints.md states the exemption for both.

**N7 — LogState.parcel_status, arithmetic_audits.py**

- *Finding:* 'Released' requires the destroying event to emit a reservoir flow whose SUBSTANCE equals the parcel's own substance. The prose describes it only as being sent to a named reservoir.
- *Consequence:* Load-bearing on this fixture. E8 turns bread into CO2, water and sewage, none of them 'sub:bread', so the bread reads as consumed rather than released. Both are valid fates, so IC-4 still passes.

**N8 — log_to_economy + check_ic10_nonneg_allocation**

- *Finding:* IC-10 reports min(p) = 0.0000 and passes. The zero belongs to sub:steel-part, which no process in the derived economy makes: `log_to_economy` excludes genesis events, so a genesis-admitted substance has an all-zero row in B, an all-zero row in A~, and c = 0. Its per-unit debit is zero because it has no producer, not because a split came out at zero.
- *Consequence:* 'min(p) >= 0' is true and is weaker than it looks on this fixture. The estimated creation-cost that a genesis entry is supposed to carry does not reach the IC-10 projection at all.

**N9 — log_to_economy, the E10 repair event**

- *Finding:* The reported spectral radius rho = 0.980 is one number: A~[steel-tool, steel-tool] = theta * A / B = 1.0 * 5.0 / 5.1 = 0.98039..., the repair consuming a 5.0 kg tool and emitting a 5.1 kg tool. Every other entry of A~ is smaller. The amplification 1 / (1 - 0.98039) = 51 is what turns the mechanic's 3 hours into a per-unit tool debit of 30.0 h/kg.
- *Consequence:* The rho quoted beside the IC-10 verdict describes the repair loop, not the food chain. It is close to 1 for a structural reason a reader should be told, not because the economy is near collapse.

---

## 5. Agreement check

For every log below, the twelve shipped `check_*` functions were run, and the quantities in `constraints.md` were re-derived independently in `generate.py`. **Agree** means both said the same thing about whether the constraint holds.

| log | disagreements |
|---|---|
| clean | **none** |
| INJ-1 | **none** |
| INJ-2 | **none** |
| INJ-3 | **none** |
| INJ-4 | **none** |
| INJ-5 | **none** |
| INJ-6 | **none** |
| INJ-7 | **none** |
| INJ-8 | **none** |
| INJ-9 | **none** |
| INJ-10 | **none** |
| INJ-11 | **none** |
| INJ-12 | **none** |

