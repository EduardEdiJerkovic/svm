import xlrd 
from models.feature import Feature
from helper import ExtractData

# Give the location of the file 
loc = ("Dobre_znacajke.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 

data = ExtractData(sheet)  

print(data[0])

