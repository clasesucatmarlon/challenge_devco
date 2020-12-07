""" 
Read and extract data from an Excel file and store it in a txt file
"""

import xlrd
import os

# Route of file
filePath = "./devco.xlsx"

# Open file
openFile = xlrd.open_workbook(filePath)

# sheet of work
sheet = openFile.sheet_by_name("Hoja1")

fileTxt = open('./fileTxt.txt', 'w')

for i in range(sheet.nrows):
    line = ''
    for j in range(sheet.nrows):
        line += str(sheet.cell_value(i, j))
        if (j < sheet.ncols - 1):
            line += str('|')
    fileTxt.write(line + os.linesep)
