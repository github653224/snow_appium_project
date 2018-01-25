# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
import pymysql.cursors
from mysqlConfig.connect_to_mysqldb import connectToDB

connection,cursor=connectToDB()
print "connection",connection
print "cursor",cursor

# Connect to the database
# connection = pymysql.connect(host='127.0.0.1',
#                              user='root',
#                              password='panxueyan653224',
#                              db='django_guest',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record

        sql = 'INSERT INTO sign_event (event_name,people_limit,status,address,start_time,create_time)'\
              'VALUES ("小米MIX5 发布会",1000,0,"韩国",NOW(),NOW());'
        cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT event_name,people_limit,status,address, start_time FROM sign_event WHERE event_name=%s"
        cursor.execute(sql, ('小米MIX5 发布会',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()