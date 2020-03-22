 #读取
# import xlrd
# xlsx = xlrd.open_workbook(r"C:\Users\Admin\Desktop\刘军华3.21\刘军华3.22日报表.xlsx")
# table = xlsx.sheet_by_index(0)
# print(table.cell(2,2).value)
# print(table.cell_value(8,18))
#写入
import xlwt
new_workbook = xlwt.Workbook()
work_sheet = new_workbook.add_sheet("new_sheet")
work_sheet.write(0,0,"我爱你！")
new_workbook.save(r"C:\Users\Admin\Desktop\auto\test.xls")
