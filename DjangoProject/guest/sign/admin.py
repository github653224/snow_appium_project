# coding=utf-8
from django.contrib import admin
from sign.models import Event,Guest

class EventInfoInline(admin.TabularInline):#admin.StackedInline
    model=Guest
    extra = 1
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', "people_limit",'status', 'address', 'start_time']
    search_fields = ['event_name']  # 搜索栏
    list_filter = ['status']  # 过滤器
    list_per_page = 5
    #修改属性时，把属性归类
    fieldsets=[
        ("basic",{"fields":["event_name","address","people_limit"]}),
        ("super",{"fields":["status","start_time"]}),
    ]
    inlines = [EventInfoInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器 ……
    list_per_page = 5

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)


# admin.site.register(Event)
# admin.site.register(Guest)
