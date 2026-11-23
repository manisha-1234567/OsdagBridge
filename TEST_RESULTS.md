# Test Results — OsdagBridge

**Build under test:** `dev` branch · **Report date:** 2026-11-23 · **Tester:** Manisha
**Source of results:** generated design report `Osdagbridge_Report.tex` (Rev 0). Figures below are taken from that report; hand-check numbers were computed from the report's own inputs.

## 1. Test case TC-01

| Input | Value |
|---|---|
| Location | Pasighat, Arunachal Pradesh (28.0667, 95.3333) |
| Seismic zone / wind | V / Vb = 42 m/s |
| Span / carriageway | 35 m / 7.8 m, no median, no footpath |
| Girders | 4 × welded symmetric, 1950 × 590 × 25 (web 10), spacing 2.175 m |
| Deck | 250 mm M40, Fe 500, overhang 1.0875 m |
| Steel | E350A (girder, bracing, diaphragm) |
| Skew | not entered |

## 2. Overall outcome

| Item | Result |
|---|---|
| Report generated | Yes |
| Overall status in report | **FAIL** (Fatigue normal stress; Int. stiffener leg ≤ H_limit) |
| Governing UR | 1.72 (stiffener leg 290 mm vs 169.03 mm) |
| Fatigue UR | 1.40–1.42 (Δσ 129–131 MPa vs 92.49 MPa) |

## 3. Checks that passed (as reported)

| Check | UR |
|---|---|
| Girder moment (2898.6 / 16133.69 kNm) | 0.18 |
| Girder shear (349.39 kN vs 616.47 kN) | 0.57 |
| LTB, construction stage | 0.28 |
| Deflection: LL 15.29 mm (≤ 43.8), total 50.39 mm (≤ 58.3) | 0.35 / 0.86 |
| Steel stress 72.16 MPa (≤ 315) | 0.23 |
| Deck sagging / hogging / overhang flexure | 0.90 / 0.88 / 0.90 |
| Deck punching / one-way shear | 0.34 / 0.82 |
| Crack width 0.217 mm (≤ 0.30) | 0.72 |
| Shear connector spacing (400 mm provided) | pass |

## 4. Defects found

Severity: H = high, M = medium, L = low. Issue column: fill in after filing.

| ID | Sev | Area | Observed | Expected / hand check | Issue |
|---|---|---|---|---|---|
| D-01 | H | Executive summary | "Girder design pass" while overall status is FAIL (fatigue, stiffener) | Summary must reflect FAIL | #TODO |
| D-02 | H | Cross bracing / diaphragm slenderness | KL/r = 128.8 / 114.9 / 144.5 with KL = 2735 / 2175 mm and r_min = 8.0 mm | 2735/8.0 = 341.9, 2175/8.0 = 271.9 → exceeds limit 250. Also G1-G2 and G2-G3 give different KL/r for identical section and length | #TODO |
| D-03 | H | Bracing section | Input table: IS 100×100×10; design tables: 40×40×3 | One section must be used throughout | #TODO |
| D-04 | M | Girder dimension table | Depth 1.95 mm, web 0.01 mm, flange 0.59 mm × 0.025 mm | 1950, 10, 590 × 25 mm (unit conversion error) | #TODO |
| D-05 | M | Shear utilisation | Design chapter: Vu 349.39 kN, UR 0.57; overall summary: Vu 456.77 kN, UR 0.74 | Same value in both places | #TODO |
| D-06 | M | LTB capacity | Design table Mb = 11905.97 kNm; overall summary capacity 1332.43 kNm | Same capacity in both | #TODO |
| D-07 | M | Deflection | Overall summary: 24.28 mm (total); design chapter: 50.34–50.39 mm | Same value | #TODO |
| D-08 | M | Stiffener data | Input: intermediate stiffener t = 10 mm; design summary: 24.5 mm; end panel t = 1.2 mm; spacing blank | Consistent and populated; 1.2 mm bearing stiffener not plausible | #TODO |
| D-09 | M | Unit weights | Self-weight table: steel 76.4, concrete 24.5 kN/m³; assumptions: 78.5 and 25.0 kN/m³ (IRC 6 Cl. 203) | Use code values or explain | #TODO |
| D-10 | M | Wearing course | Input "Concrete, 50 mm"; assumptions mention bituminous 24 kN/m³ | Consistent material | #TODO |
| D-11 | M | BOQ steel area | Girder area 0.04707 m² in BOQ; section area 485 cm² = 0.0485 m² | 0.0485 m² (≈ 3 % lower steel weight in BOQ) | #TODO |
| D-12 | M | Blank fields | Skew angle, no. of lanes, Vz, Pz, wind forces (T/L/V), seismic forces, footpath LL, stiffener spacing, reactions table rows are empty | Populated or "N/A" | #TODO |
| D-13 | M | End diaphragm | Tables identical to cross bracing; overall summary lists diaphragm "Moment/Shear" with kN demand/capacity | Own member forces and labels | #TODO |
| D-14 | M | Bracing count | 33 top / 33 bottom / 66 diagonals for 35 m span with 17.5 m spacing | Count consistent with spacing | #TODO |
| D-15 | M | Bearing stiffener | Web buckling resistance 190 984.95 kN | Implausible magnitude; recheck | #TODO |
| D-16 | M | Transverse shear | Overall summary row has "—" for all values although the check passed (UR 0.07) | Fill values | #TODO |
| D-17 | L | Code years | IRC 22: 2014 vs 2015; IRC 112: 2011 vs 2020; IRC 5: 2015 vs 2024 | One year per code | #TODO |
| D-18 | L | Units in summary | Girder spacing "2.175", deck thickness "250.0" without units | Add m / mm | #TODO |
| D-19 | L | Header text | Page header reads "OsdagBridge \|" with empty second part; reviewer/organisation/client/job no./version blank | Fill or hide | #TODO |
| D-20 | L | LaTeX | Hard-coded `C:/Users/.../Temp/...` image paths; duplicate `\label{sec:assumptions}`; `\sdstar` page footnote relies on `\AddToHook` (new LaTeX only) | Relative paths; unique labels | #TODO |

## 5. Observations

- Analysis envelopes are plausible: Envelope ULS moment 2898.6 kNm at 13.696 m, shear 456.77 kN at support.
- Mp/γm0 hand check: 37418.75 cm³ × 350 MPa / 1.1 = 11 905.97 kNm — matches the report.
- Concrete deck weight 76.12 m³ × 25 = 190.3 t and girder weight 1.6476 m³ × 7.85 = 12.93 t per girder — BOQ arithmetic is consistent with its own inputs.

## 6. Planned further test cases

| ID | Variation |
|---|---|
| TC-02 | Shorter span (20 m), 3 girders |
| TC-03 | Footpath + median |
| TC-04 | Skew 10° and 20° (limit check) |
| TC-05 | Different steel grade / thicker flanges (> 25 mm, μr) |
| TC-06 | Longitudinal stiffener / thick web philosophy |

## 7. GitHub Issues verification checklist

- [ ] One issue per defect D-01 … D-20 (or grouped by area)
- [ ] Each issue has: input values, expected vs actual, report page, severity label
- [ ] Issue numbers filled into the table above
- [ ] Issues open on the correct repo (`manisha-1234567/OsdagBridge`)
- [ ] Screenshot of Issues tab attached to the submission
