# -*- coding: utf-8 -*-
# @File    : mysql_connector.py
# @Time    : 5/13/2021 8:00 PM
# @Author  : Mahesh
# @Email   : mahesh.babux.kandukuri@email

import  mysql.connector
mydb = mysql.connector.connect(host='localhost', user='mahesh', passwd='1234', database='Employee')
mycursor = mydb.curosr()
# mycursor.execute("show databases")
mycursor.execute('select * from student')
result = mycursor.fetchall()
# result = mycursor.fetchone()

for i in result:
    print(i)