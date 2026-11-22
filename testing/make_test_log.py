from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()

# ---------- Sheet 1: Test cases ----------
ws = wb.active
ws.title = "Test Cases"
headers = ["TC ID", "Category", "Parameters Used (exact)", "Expected",
           "Actual", "Result (Pass/Fail)", "osi file", "Screenshot / Log", "Issue Link"]
ws.append(headers)

samples = [
    ["TC01", "Default run", "All defaults, span=__, width=__", "Design completes",
     "", "", "osi_files/TC01_default.osi", "screenshots/TC01.png", ""],
    ["TC02", "Basic input", "Span=__, width=__, skew=__", "", "", "", "", "", ""],
    ["TC03", "Custom steel", "Girder fy=__, fu=__", "Input dict shows custom values", "", "", "", "", ""],
    ["TC04", "Custom concrete", "Deck fck=__", "Input dict shows custom value", "", "", "", "", ""],
    ["TC05", "Edge case", "Empty span / zero / negative", "Error message shown", "", "", "", "", ""],
]
for row in samples:
    ws.append(row)

# ---------- Sheet 2: Multi-run ----------
ws2 = wb.create_sheet("Multi-Run")
ws2.append(["Run No", "Inputs changed", "GUI updated?", "Output updated?",
            "3D CAD updated?", "Plots updated?", "Stale data / crash?", "Notes"])
for i in range(1, 6):
    ws2.append([f"Run {i}", "", "", "", "", "", "", ""])

# ---------- Sheet 3: Input dict comparison ----------
ws3 = wb.create_sheet("UI vs Input Dict")
ws3.append(["TC ID", "Field", "Value entered in UI", "Value in Input Dictionary", "Match? (Y/N)"])
ws3.append(["TC03", "material.girder.fy", "", "", ""])
ws3.append(["TC03", "geometry.span", "", "", ""])

# ---------- Sheet 4: Output dict comparison ----------
ws4 = wb.create_sheet("Output Dict vs Report")
ws4.append(["TC ID", "Output field", "Value in Output Dictionary", "Value in Report / Dock", "Match? (Y/N)"])
ws4.append(["TC01", "", "", "", ""])

# ---------- Formatting ----------
header_fill = PatternFill("solid", fgColor="1F4E78")
for sheet in wb.worksheets:
    for cell in sheet[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = header_fill
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for col in sheet.columns:
        sheet.column_dimensions[col[0].column_letter].width = 26
    sheet.freeze_panes = "A2"

wb.save("test_cases.xlsx")
print("test_cases.xlsx created")