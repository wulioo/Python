# -*- codeing = utf-8 -*-
# @Time : 2020/8/24 8:00 下午

import xlwt

'''
# ------1.已utf-8编码创建一个Excel对象
wookbook = xlwt.Workbook(encoding="utf-8")
# ------2.创建一个Sheet表
wooksheet = wookbook.add_sheet('Sheet1')
# ------3.往单元格里面写入内容
wooksheet.write(0, 0, "hello")  # 参数（1）为行,参数（2）为列,参数（3）为内容
# ------4.保存表格
wookbook.save('student')
'''

# ------ 案列（一）------

wookbook = xlwt.Workbook(encoding="utf-8")
wookshell = wookbook.add_sheet('Sheet')
for i in range(0, 9):
    for j in range(0, i+1):
        wookshell.write(i, j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
wookbook.save('student.xls')


