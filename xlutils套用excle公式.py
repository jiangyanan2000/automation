from xlutils.copy import copy
import xlrd
import xlwt
temp_excel = xlrd.open_workbook(r"C:\Users\Admin\Desktop\heping.xls",formatting_info=True)
temp_sheet = temp_excel.sheet_by_index(0)
print(temp_sheet.cell(2,2).value)
new_excel = copy(temp_excel)
new_sheet = new_excel.get_sheet(0)


style = xlwt.XFStyle()

#设置字体
font = xlwt.Font()
font.name = "微软雅黑"
font.bold = True
font.height = 360
style.font = font
#设置边框
borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

#设置对齐方式
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment
new_sheet.write(20,20,"我在学习python",style)

new_excel.save(r"C:\Users\Admin\Desktop\heping1.xls")
