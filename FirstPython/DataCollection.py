"""
在一个excel文件里新建一张表来存放之前的sheet数据的汇总
"""
import xlrd
import sys
from xlutils.copy import copy

fileReadWork = xlrd.open_workbook("./text2/python_test.xlsx")
file_list = fileReadWork.sheet_names()
new_sheet = None
nb = None
# 如果这个xlsx文件没有这个sheet
if "Bubble Class" not in file_list:
    # 将原先的复制下来
    nb = copy(fileReadWork)
    # 添加新的sheet
    new_sheet = nb.add_sheet("Bubble Class")
    # 添加头部
    new_sheet.write(0, 0, "序号")
    new_sheet.write(0, 1, "学号")
    new_sheet.write(0, 2, "姓名")
    new_sheet.write(0, 3, "班级")
else:
    print("已有此文件系统退出")
    sys.exit()

# 计数器
num = 1

for i in file_list:
    table = fileReadWork.sheet_by_name(i)
    rows = table.nrows
    for j in range(1, rows):
        if j != 0:
            # 添加一行数据
            new_sheet.write(num, 0, num)
            new_list = table.row_values(j)
            for k in range(len(new_list)):
                new_sheet.write(num, k+1, new_list[k])
            num += 1

nb.save("./text2/python_test.xlsx")
print("添加成功")
