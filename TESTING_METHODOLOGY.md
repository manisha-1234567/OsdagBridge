# Testing Methodology — OsdagBridge

## 1. Objective

Check that OsdagBridge (`dev` branch) produces a **complete, internally consistent and code-compliant** design report for a composite steel plate-girder highway bridge.

## 2. Scope

| In scope | Out of scope |
|---|---|
| Input handling and defaults | Substructure, foundations, bearings |
| Load generation and combinations | Splice connections |
| Grillage analysis output | Continuous spans |
| Girder, deck, shear connector, bracing, diaphragm checks | Skew > 15° |
| Report generation (LaTeX/PDF) and CAD images | Performance / load testing |

## 3. Approach

Black-box functional testing from the user's side, followed by a review of the generated report.

1. **Run** a defined test case through the software (inputs in TEST_RESULTS.md).
2. **Completeness check** – every table/field in the report is populated; no blank cells, no missing figures.
3. **Unit and format check** – values carry correct units (m vs mm, kN vs kN·m).
4. **Cross-consistency check** – the same quantity must have the same value everywhere in the report (executive summary vs design chapter vs overall summary vs BOQ).
5. **Hand-calculation spot checks** – recompute simple quantities (areas, weights, slenderness = KL/r, UR = demand/capacity, Mp/γm0).
6. **Code check** – input constants and clause references compared with the cited code (e.g. unit weights per IRC 6, code years).
7. **Logic check** – status words (PASS/FAIL) agree with UR values and with the overall status.
8. **Report build check** – the `.tex` compiles on a clean machine (no absolute paths, no missing packages).

## 4. Test levels

| Level | What is exercised |
|---|---|
| Input | Mandatory vs optional inputs; blank optional values (skew, lanes, footpath) |
| Analysis | Load cases, envelopes, reactions, deflections |
| Design | Each check table per girder / member |
| Output | Report text, tables, figures, BOQ |

## 5. Pass / fail criteria

- **Pass:** value present, correct unit, consistent everywhere, matches hand check within ~1–2 %, status agrees with UR.
- **Fail:** missing value, wrong unit, contradiction between two places, hand check mismatch, or status contradicts UR.
- **Severity:** *High* – wrong design conclusion or unsafe result; *Medium* – wrong/missing number that does not change the conclusion; *Low* – cosmetic/formatting.

## 6. Test data

TC-01: 35 m simply supported highway bridge, 4 girders, 7.8 m carriageway, E350A steel, M40 deck, Pasighat (Seismic Zone V, Vb = 42 m/s). Full inputs are in `TEST_RESULTS.md`. More cases (different span, skew, footpath, median, steel grade) are listed as planned there.

## 7. Defect reporting

Each defect is logged as a GitHub Issue with: title, severity, input values, expected vs actual, report page/table, and suggested fix. Issue links are recorded in TEST_RESULTS.md.

## 8. Tools

OsdagBridge `dev`, pdfLaTeX, a PDF viewer, a calculator/Python for hand checks, GitHub Issues.

## 9. Limitations of this test round

- A single test case was executed (TC-01).
- Results come from reviewing the generated report; the code path behind each number was not inspected.
- No independent FEM / commercial-software comparison yet.
