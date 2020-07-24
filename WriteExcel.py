import openpyxl

path = 'C://Users//Grom//Downloads//Employe.xlsx'

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(7, 10):
    for c in range(1, 7):
        sheet.cell(row=r, column=c).value = "wrote data"

workbook.save(path)
