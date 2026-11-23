# OsdagBridge

Open-source software for the design of **composite steel plate-girder highway bridges** (Indian codes: IRC 5, 6, 22, 24, 112, SP 114 and IS 800). Part of the [Osdag](https://osdag.fossee.in/) project — FOSSEE, IIT Bombay.

> Status: development version (`dev` branch). Some modules are incomplete — see [KNOWN_LIMITATIONS.md](KNOWN_LIMITATIONS.md).

## What it does

Given basic bridge inputs, OsdagBridge:

1. Builds a 3D grillage model (OSPGrillage) of a simply supported I-girder bridge.
2. Applies IRC 6 dead, SIDL, live (Class A, 70R, AA, SV, Fatigue), wind, seismic and temperature loads and auto-generates ULS/SLS combinations.
3. Designs / checks:
   - Plate girders (moment, shear, interaction, LTB, stiffeners, deflection, stress, fatigue)
   - Shear connectors (capacity, spacing, transverse shear)
   - RCC deck slab (flexure, cantilever overhang, punching, one-way shear, crack width, detailing)
   - Cross bracing and end diaphragms
4. Generates CAD views (pythonOCC) and a LaTeX **Design Report** with bill of materials.

## Inputs

| Group | Examples |
|---|---|
| Location | Place / lat-long → seismic zone, basic wind speed, shade temperatures |
| Geometry | Span, carriageway width, median, footpath, skew angle |
| Materials | Girder / bracing steel grade (IS 2062), deck concrete grade |
| Additional | No. of girders, spacing, overhang, deck thickness, barrier, railing, wearing course, girder section, stiffeners, bracing, studs, safety factors |

Values not entered by the user are filled with IRC/IS defaults and marked with `*` in the report.

## Outputs

- Design Report (`.tex` → PDF): executive summary, inputs, loads, analysis, design checks, drawings, material take-off, assumptions.
- Utilization ratio (UR = demand / capacity) for every check; UR ≤ 1.0 is a pass.

## Installation

<!-- TODO: replace with the repo's real commands -->
```bash
git clone https://github.com/manisha-1234567/OsdagBridge.git
cd OsdagBridge
git checkout dev
# TODO: environment setup (Python version, conda/pip requirements)
# TODO: launch command
```

Requirements for the PDF report: a LaTeX distribution (pdfLaTeX) with `longtable`, `fancyhdr`, `titlesec`, `titletoc`, `etoolbox`, `needspace`, `makecell`, `lastpage` (LaTeX 2020+ for `\AddToHook`).

## Quick start

1. Launch OsdagBridge.
2. Enter project location, span, carriageway width and materials.
3. Review / edit additional inputs.
4. Run design; open the Design Report.

## Documentation

| File | Purpose |
|---|---|
| [TESTING_METHODOLOGY.md](TESTING_METHODOLOGY.md) | How the software was tested |
| [TEST_RESULTS.md](TEST_RESULTS.md) | Results of test case TC-01 and defects found |
| [KNOWN_LIMITATIONS.md](KNOWN_LIMITATIONS.md) | Scope limits and known issues |

## Design standards

IRC 5, IRC 6:2017, IRC 22, IRC 24:2010, IRC 112, IRC SP 114:2018, IS 800:2007, IS 2062, IS 456, IS 1786, IS 1893 (Part 3).

## Contributing

Report bugs via GitHub Issues with: input values, expected vs actual output, screenshot / report page, and software version.

## License / credits

Osdag · FOSSEE · Indian Institute of Technology Bombay. <!-- TODO: add licence name as in repo -->
