from Kogger_calculation import *
from openpyxl import Workbook

#13 mpen from runes
#~6 extra pen at lvl 11, ~8 at lvl 16
#Health, AP, Mpen, Base, MRignore, shots, liandrys burn, rylais, workbook

#Spreadsheet setup
wb = Workbook()

print("Scenario 1: Level 11, Optimal Target (1221hp)")
print("Build 1: Tear, Rylais, Sorc Boots, Chalice")
Barrage(1221, 100, 32, 140, 1, 10, 0, 0, wb)
Barrage(1221, 100, 32, 140, 0.65, 10, 0, 0, wb)

print("Scenario 2: Level 11, Tanky Target (1514)")
print("Build 1: Tear Rylais, Sorc Boots, Chalice")
Barrage(1514, 100, 32, 140, 1, 5, 1, 0, wb)

print("Scenario 3: Level 18, Optimal Target (1871hp)")
print("Build Standard (no void):Arch, Rylais, Sorc boots, Chalice, Liandrys, [armor]")

wb.save("Kogmaw Ult Calculations.xlsx")
