"""
excel操作
pip3 install xlrd
"""

import xlrd

# 1、打开工作簿
wordbook = xlrd.open_workbook('./res/excel/班级资料.xlsx')

# 2、工作表
# 输出所有sheet的名字
print(wordbook.sheet_names())
# 获取所有的sheet
print(wordbook.sheets())
# 根据索引获取sheet
print(wordbook.sheet_by_index(0))
# 根据名字获取sheet
# print(wordbook.sheet_by_name(''))

# 3、行、列操作
sheet1 = wordbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
# 获取第2行内容
print(sheet1.row_values(1))
# 获取第3列内容
print(sheet1.col_values(2))

# 单元格操作
cell1 = sheet1.cell(1, 1).value
print(cell1)
cell2 = sheet1.row(1)[1].value
print(cell2)
cell3 = sheet1.cell(1, 2).value
print(cell3)
cell4 = sheet1.col(2)[1].value
print(cell4)

# 5、日期类型（在对应的单元格准备好日期数据）
# data_value = xlrd.xldate_as_datetime(
#     sheet1.cell_value(5, 5), wordbook.datemode
# )
# print(type(data_value), data_value)
