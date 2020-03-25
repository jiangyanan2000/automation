import xlrd,xlwt
from xlutils import copy
xlsx = xlrd.open_workbook(r"C:\Users\Admin\Desktop\heping.xls")
table = xlsx.sheet_by_index(0)
all_data = []
print(table.nrows)
for n in range(1,table.nrows):
    branch_name = table.cell(n,1).value
    student_num = table.cell(n,2).value
    par = table.cell(n,7).value
    data = {"branch_name":branch_name,"student_num":student_num,"par":par}
    all_data.append(data)
print(all_data)