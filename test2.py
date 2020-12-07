""" 
Read and extract data from an Excel file
"""


import pandas as pd

fileExcel = pd.read_excel('./devco.xlsx', sheet_name='Hoja1', header=None, skiprows=1, names=['Nombre', 'Apellido', 'Documento', 'Sueldo'])
print(fileExcel)
