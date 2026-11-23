# Known Limitations — OsdagBridge

## A. By design (version scope)

- Substructure (piers, pile caps, foundations) and **bearing design** are not included.
- **Splice connections** are not designed.
- All girders are **simply supported**; continuous spans are not supported.
- **Skew > 15°** needs independent manual analysis (IRC 24 Cl. 504.8).
- Transverse member forces use an approximate 2D frame analogy; use 3D FEM for irregular or skewed geometry.
- Construction-stage analysis is approximate; do detailed staged analysis for long-term deflection.
- Bearing stiffness is idealised (fixed k = 1,000,000 kN/m, free k = 100 kN/m).
- Constant-amplitude fatigue stress range assumed.

## B. Issues found during testing (TC-01)

Details, expected values and severity are in [TEST_RESULTS.md](TEST_RESULTS.md).

| Area | Limitation / bug |
|---|---|
| Report logic | Executive summary says "pass" even when the design status is FAIL |
| Bracing & diaphragm | Slenderness values do not follow KL/r; section differs between input (100×100×10) and design (40×40×3); diaphragm tables duplicate cross bracing |
| Units | Girder dimension table prints mm values as metres (1.95 mm); some summary values lack units |
| Consistency | Shear, LTB capacity and deflection differ between design chapter and overall summary; unit weights differ from stated assumptions |
| Missing values | Skew, lanes, wind pressure/forces, seismic forces, footpath live load, stiffener spacing and the "Reactions at Supports" table are blank |
| Stiffeners | Reported thicknesses (24.5 mm, 1.2 mm) do not match input (10 mm); bearing-stiffener web-buckling value is implausible |
| BOQ | Girder steel area (0.04707 m²) differs from section area (0.0485 m²); crash barrier quantity is zero |
| Standards | Code years differ between sections (IRC 5, 22, 112) |
| Report build | Absolute Windows image paths and duplicate LaTeX labels; requires recent LaTeX (`\AddToHook`) |

## C. Use of results

OsdagBridge output is a design aid. A qualified engineer must verify the model, inputs and every governing check before the results are used for construction or tender documents.
