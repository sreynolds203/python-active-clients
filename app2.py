import openpyxl
from datetime import datetime

file = 'sale_dates.xlsx'
wb = openpyxl.load_workbook(file)
sheet = wb['Transaction List by Customer']
writer_1 = open('delete_names_2.csv', 'w')
names = []
for value in sheet.iter_rows(values_only = True):
    if value[0]:
        client = value[0]
    if value[1]:
        date = datetime.strptime(value[1], '%m/%d/%Y')
        if date.year in (2019, 2020):
            if client in names:
                pass
            else:
                names.append(client)
for name in names:         
    writer_1.write(name + '\n')
writer_1.close
print('finished')