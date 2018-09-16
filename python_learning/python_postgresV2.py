#!/usr/bin/python

import psycopg2
import sys
import pprint
import xlwt
from datetime import datetime

#http://www.cnblogs.com/chen0427/p/5755094.html

def get_data(sql):

    conn_string = "host='localhost' dbname='db1' user='postgres' password='123456'"
    print "Connecting to database\n -> %s" % (conn_string)
    conn = psycopg2.connect(conn_string)
    global cursor
    cursor = conn.cursor()
    print "Connected! \n"
    #sql = "SELECT * FROM users"
    cursor.execute(sql)
    
    records = cursor.fetchall()
    return records

def write_data_to_excel():
    print "============ hanshu2"
    sql1 = "SELECT * FROM users"
    result = get_data(sql1)
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)
    today = datetime.today()

    today_date = datetime.date(today)
    for i in xrange(len(result)):
        for j in xrange(len(result[i])):
            sheet.write(i,j,result[i][j])
    wbk.save(str(today_date)+'.xlsx')

if __name__ == "__main__":

    write_data_to_excel()