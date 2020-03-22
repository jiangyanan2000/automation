from xlutils.copy import copy
import xlrd
import xlwt
temp_excel = xlrd.open_workbook(r"C:\Users\Admin\Desktop\刘军华3.21\刘军华3.22日报表.xls",formatting_info=True)
temp_sheet = temp_excel.sheet_by_index(0)
new_excel = copy(temp_excel)
new_sheet = new_excel.get_sheet(0)
new_sheet.write(5,27,1)
new_sheet.write(6,27,2)
new_sheet.write(7,27,3)
new_excel.save(r"C:\Users\Admin\Desktop\刘军华3.21\tianxe.xls")
