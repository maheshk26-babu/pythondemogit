# -*- coding: utf-8 -*-
# @File    : testexcel.py
# @Time    : 4/29/2021 3:58 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

from Customreadwriteexcel import ReadWriteExcel

r = ReadWriteExcel("C:\\Users\\mkandukx\\PycharmProjects\\PyTestSample\\PYTHON BASICS\\Data.xlsx")
print(r.readByColIndex('TestData', 3, 3))
print(r.readByColName('TestData', 3, 'Name'))
print(r.getRowCount('TestData'))
print(r.getColCount('TestData'))

# read all row values
rows = r.getColCount('TestData') + 1
for colindex in range (1, rows):
    print(r.readByColIndex('TestData', 2, colindex))

#read all column values by column name
cols = r.getRowCount('TestData')
for rowindex in range (1, cols):
    print(r.readByColName('TestData', rowindex, 'Name'))

#read all column values by column index
cols = r.getRowCount('TestData')
for rowindex in range (1, cols):
    print(r.readByColIndex('TestData', rowindex, 3))

r.writeByColIndex('TestData', 4, 3, 'AWS')
r.writeByColName('TestData', 5, 'Role', 'Support')