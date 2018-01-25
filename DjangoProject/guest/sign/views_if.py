# -*- coding:utf-8 -*-
from django.http import JsonResponse
from sign.models import Event,Guest
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError
import time

# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid','')                          # 发布会id
    event_name = request.POST.get('event_name','')                        # 发布会标题
    people_limit = request.POST.get('people_limit','')                      # 限制人数
    status = request.POST.get('status','')                    # 状态
    address = request.POST.get('address','')                  # 地址
    start_time = request.POST.get('start_time','')            # 发布会时间


    if eid == '' or event_name == '' or people_limit == '' or address == '' or start_time == '':
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})
    result = Event.objects.filter(event_name=event_name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid, event_name=event_name, people_limit=people_limit, address=address,status=int(status), start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})


# 查询发布会接口
def get_event_list(request):
    eid = request.GET.get("eid", "")  # 发布会id
    event_name = request.GET.get("event_name", "")  # 发布会名称

    if eid == '' and event_name == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            event['event_name'] = result.event_name
            event['people_limit'] = result.people_limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status': 200, 'message': 'success', 'data': event})
    if event_name != '':
        datas = []
        results = Event.objects.filter(event_name__contains=event_name)
        if results:
            for r in results:
                event = {}
                event['event_name'] = r.event_name
                event['people_limit'] = r.people_limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})


#添加嘉宾接口
def add_guest(request):
    eid = request.POST.get('eid', '')  # 关联发布会id
    realname = request.POST.get('realname', '')  # 姓名
    phone = request.POST.get('phone', '')  # 手机号
    email = request.POST.get('email', '')  # 邮箱
    if eid == '' or realname == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023,'message': 'event status is not available'})
    event_limit = Event.objects.get(id=eid).people_limit  # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数
    if len(guest_limit) >= event_limit:
        return JsonResponse({'status': 10024, 'message': 'event number is full'})
    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    etime = str(event_time).split(".")[0]
    timeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))
    now_time = str(time.time())  # 当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)
    if n_time >= e_time:
        return JsonResponse({'status': 10025, 'message': 'event has started'})
    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email,
                             sign=0, event_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status': 10026,
                             'message': 'the event guest phone number repeat'})
    return JsonResponse({'status': 200, 'message': 'add guest success'})


# 嘉宾查询接口
def get_guest_list(request):
    eid = request.GET.get("eid", "")  # 关联发布会id
    phone = request.GET.get("phone", "")  # 嘉宾手机号
    if eid == '':
        return JsonResponse({'status': 10021, 'message': 'eid cannot be empty'})

    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})


# 嘉宾签到接口
def user_sign(request):
    eid = request.POST.get('eid', '')  # 发布会id
    phone = request.POST.get('phone', '')  # 嘉宾手机号

    if eid == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})

    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})

    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    etime = str(event_time).split(".")[0]
    timeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time())  # 当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)

    if n_time >= e_time:
        return JsonResponse({'status': 10024, 'message': 'event has started'})

    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status': 10025, 'message': 'user phone null'})

    result = Guest.objects.filter(event_id=eid, phone=phone)
    if not result:
        return JsonResponse({'status': 10026,
                             'message': 'user did not participate in the conference'})
    result = Guest.objects.get(event_id=eid, phone=phone).sign
    if result:
        return JsonResponse({'status': 10027, 'message': 'user has sign in'})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return JsonResponse({'status': 200, 'message': 'sign success'})