# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def init(request):
    return HttpResponse("Hello Django, it works !")


#使用django.http.HttpResponse函数向页面返回字符串！这种没有使用html模板
# def index(request):
#     return HttpResponse("Hello Django !")


# #使用django.shortcuts.render函数把模板中的html页面内容返回给页面
# def index(request):
#     return render(request,"sign/loginPage.html")

#通过if判断的形式来验证登陆完成登陆操作如下，后面会有Django认证系统的：
# def login_action(request):
#     if request.method=="POST":
#         username=request.POST.get("username","")
#         password=request.POST.get("password","")
#         if username=="admin" and password=="admin112233":
#             # return HttpResponse("Login Success !")
#             # return render(request,"sign/event_manage.html", {"success": "Login Success , welcome!"})
#
#             ################################################################################################################################
#             #注意：这里重定向的是url路径（event_manage_page）并不是下面的函数（event_manage），重定向后再由重定向的URL路径绑定views的函数：event_manage #
#             # HttpResponseRedirect，它可以对路径进行重定向，从而将登录成功之后的请求指向 / event_manage /                                      #
#             # 创建event_manage函数，用于返回发布会管理页面event_manage.html。                                                                 #
#             # 最后，不要忘记在.. / guest / urls.py文件中添加event_manage / 的路由                                                             #
#             #################################################################################################################################
#             # return HttpResponseRedirect('/event_manage_page/')
#             response = HttpResponseRedirect('/event_manage_page/')
#             #cookie机制
#             # response.set_cookie('user', username, 3600) # 添加浏览器cookie
#
#             #session机制
#             request.session['user'] = username  # 将session信息记录到浏览器
#             return response
#         else:
#
#             return` render(request,"sign/loginPage.html",{"error":"username or password is incorrect!"})
#
# def event_manage(request):
#     #cookie机制
#     # cookie_content = request.COOKIES.get('user', '')  # 读取浏览器cookie
#     # return render(request, "sign/event_manage.html", {"success": "Login Success , welcome!","user":"cookie_content"})
#
#     #session机制
#     session_content = request.session.get('user', '')  # 读取浏览器session
#     return render(request, "sign/event_manage.html", {"success": "Login Success , welcome!","user":"session_content"})


"""
引用Django认证登录，以下使用Django 用户认证登录系统来实现登陆操作
    # Django已帮我们封装好了用户认证和登录的相关方法，只需拿来使用即可。并且，同样使用auth_user表中的数据进行验证，
    # 前面已经通过Admin后台向该表中添加了用户信息。
"""

#使用django.shortcuts.render函数把模板中的html页面内容返回给页面
def index(request):
    return render(request,"sign/loginPage.html")


def login_action(request):
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #session机制
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,"sign/loginPage.html",{"error":"username or password is incorrect!"})

#发布会页面
@login_required
def event_manage(request):
    #session机制
    event_list = Event.objects.all()
    session_content = request.session.get('user', '')  # 读取浏览器session
    # 分页设置
    paginator = Paginator(event_list, 4)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)

    return render(request, "sign/event_manage.html", {"success": "Login success , welcome ","user":session_content,
                           "events":contacts})
# 发布会搜索
@login_required
def search_name(request):
    session_content=request.session.get("user","")
    search_name=request.GET.get("name","")
    event_list=Event.objects.filter(name__contains=search_name)
    return render(request, "sign/event_manage.html", {"success": "Login Success , welcome ","user": session_content, "events": event_list})

#嘉宾页面
@login_required
def guest_manage(request):
    session_content = request.session.get("user", "")
    guest_list=Guest.objects.all()
    #分页设置
    paginator = Paginator(guest_list, 4)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)

    return render(request, "sign/guest_manage.html", {"success": "Login success , welcome ","user":session_content,
                           "guests":contacts
                                                      })
#嘉宾搜索
@login_required
def search_phone(request):
    session_content=request.session.get("user","")
    search_phone=request.GET.get("name","")
    guest_list=Guest.objects.filter(phone__contains=search_phone)
    return render(request, "sign/guest_manage.html", {"success": "Login Success , welcome ","user": session_content,
                                                      "guests": guest_list})
#签到页
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign/sign_index.html', {'event': event})

#签到动作
@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event, id=eid)
    phone =  request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign/sign_index.html', {'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign/sign_index.html', {'event': event, 'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign/sign_index.html', {'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        return render(request, 'sign/sign_index.html', {'event': event, 'hint':'sign in success!','guest': result})


#退出动作
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/index/')
    return response

#参加的发布会详情：
@login_required
def event_details(request,eid):
    # event_list = Event.objects.all()
    session_content = request.session.get('user', '')  # 读取浏览器session
    # # 分页设置
    # paginator = Paginator(event_list, 4)
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     # 如果page不是整数，取第一页面数据
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     # 如果page不在范围，取最后一页面
    #     contacts = paginator.page(paginator.num_pages)

    # return render(request, "sign/event_manage.html", {"success": "Login success , welcome ", "user": session_content,
    #                                                   "events": contacts,"id":eid})
    event_list = Event.objects.filter(id=eid)

    return render(request, "sign/event_details.html", {"success": "Login success , welcome ", "user": session_content,
                                                      "events":event_list})

