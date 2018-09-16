#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xlsxwriter as wx

'''
官网Tutorial：http://xlsxwriter.readthedocs.io/tutorial
'''

#新加workbook

filename = '/Users/ruqin/Desktop/new.xlsx'
workbook =  wx.Workbook(filename)
worksheet1 = workbook.add_worksheet()

worksheet2 = workbook.add_worksheet('second sheet')

worksheet3  = workbook.add_worksheet('users')

#worksheet1.write(0, 0, 'Hello Excel')
#worksheet1.write(0, 1, '22')
#workbook.close()


expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row = 0
col = 0

for item, cost in expenses:
    worksheet1.write(row,col,item)
    worksheet1.write(row,col+1,cost)
    row += 1

worksheet1.write(row,0,'Total')
worksheet1.write(row,1,'=SUM(B1:B4)')
workbook.close()