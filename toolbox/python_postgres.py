#!/usr/bin/python

import psycopg2
import sys
import pprint

def main():

    conn_string = "host='localhost' dbname='db1' user='postgres' password='123456'"
    print "Connecting to database\n -> %s" % (conn_string)
    conn = psycopg2.connect(conn_string)
    global cursor
    cursor = conn.cursor()
    print "Connected! \n"
    cursor.execute("SELECT * FROM users")

def select():

    records = cursor.fetchall()
    pprint.pprint(records)

#def sendMail():

if __name__ == "__main__":

    main()
    select()