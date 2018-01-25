# -*- coding:utf-8 -*-
import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='panxueyan653224',
                             db='django_guest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # values_content = ("hardon",18800110002,"hardon@mail.com",0,1,NOW())
        # Create a new record
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time)' \
              ' VALUES ("halo3224",18800110002,"halo3224@mail.com",0,21,NOW());'
        cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()