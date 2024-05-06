import xlsxwriter

file = ''
lines = open(file).readlines()

workbook = xlsxwriter.Workbook('Get_Outta_Town.xlsx')
for line in lines:
    
    worksheet = workbook.add_worksheet("")