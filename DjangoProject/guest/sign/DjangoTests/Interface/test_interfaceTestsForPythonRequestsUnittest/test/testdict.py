# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
data = {'id': 1, 'event_name': '红米', '`people_limit`': 2000, 'status': 1, 'address':
        '北京会展中心', 'start_time': '2018-01-20 00:25:42','create_time':'2018-01-20 00:25:42'}
# print data.keys()
#['status', 'event_name', 'start_time', 'create_time', 'address', '`people_limit`', 'id']
# key = ','.join(data.keys())
# print key
# status,event_name,start_time,create_time,address,`people_limit`,id

for key in data:
    # print key
    # print data[key]
    data[key] = "'" + str(data[key]) + "'"
key = ','.join(data.keys())
print key
value = ','.join(data.values())
print value

real_sql = "INSERT INTO " + "table_name" + " (" + key + ") VALUES (" + value + ")"
print real_sql