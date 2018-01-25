# -*- coding:utf-8 -*-
import sys
sys.path.append('../db_fixture')
from mysql_db import DB

# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event': [
        {'id': 1, 'event_name': '红米Pro发布会', '`people_limit`': 2000, 'status': 1,
         'address': '北京会展中心', 'start_time': '2018-08-20 14:00:00',"create_time":"2018-08-20 00:25:42"},
        {'id': 2, 'event_name': '可参加人数为0', '`people_limit`': 0, 'status': 1,
         'address': '北京会展中心', 'start_time': '2018-08-20 14:00:00',"create_time":"2018-08-20 00:25:42"},
        {'id': 3, 'event_name': '当前状态为0关闭', '`people_limit`': 2000, 'status': 0,
         'address': '北京会展中心', 'start_time': '2018-08-20 14:00:00',"create_time":"2018-08-20 00:25:42"},
        {'id': 4, 'event_name': '发布会已结束', '`people_limit`': 2000, 'status': 1,
         'address': '北京会展中心', 'start_time': '2018-08-20 14:00:00',"create_time":"2018-08-20 00:25:42"},
        {'id': 5, 'event_name': '小米5发布会', '`people_limit`': 2000, 'status': 1,
         'address': '北京国家会议中心', 'start_time': '2018-08-20 14:00:00',"create_time":"2018-08-20 00:25:42"},
    ],
# 嘉宾表数据
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 13511001100,
         'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,"create_time":"2018-08-20 00:25:42"},
        {'id': 2, 'realname': 'has sign', 'phone': 13511001101,
         'email': 'sign@mail.com', 'sign': 1, 'event_id': 1,"create_time":"2018-08-20 00:25:42"},
        {'id': 3, 'realname': 'tom', 'phone': 13511001102,
         'email': 'tom@mail.com', 'sign': 0, 'event_id': 5,"create_time":"2018-08-20 00:25:42"},
    ],
}


# 将测试数据插入表
def init_data():
    print "执行"
    db = DB()

    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


# if __name__ == '__main__':
#     init_data()