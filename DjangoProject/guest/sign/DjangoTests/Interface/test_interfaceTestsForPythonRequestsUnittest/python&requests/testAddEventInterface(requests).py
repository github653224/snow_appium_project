# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
import pymysql.cursors
from mysqlConfig.connect_to_mysqldb import connectToDB
connection,cursor=connectToDB()
print connection
print cursor

