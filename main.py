import xlrd 
from models.feature import Feature
from helper import ExtractData
import csv

# Give the location of the file 
loc = ("dataTable.csv")
data = []

with open(loc) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            data.append(ExtractData(row))
            line_count += 1
    print(f'Processed {line_count} lines.')
#data = ExtractData(sheet)  

print(data[0])

