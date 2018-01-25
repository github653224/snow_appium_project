# coding=utf-8
from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    event_name = models.CharField(max_length=100)  # 发布会标题
    people_limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地址
    start_time = models.DateTimeField('events time')  # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.event_name

# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)  # 手机号
    email = models.EmailField()  # 邮箱
    sign = models.BooleanField()  # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）
    """
    对于一场发布会来说，因为手机号具有很强的唯一性，因此一般会选择手机号作为一位嘉宾的唯一验证信息。在嘉宾表中，
    除了嘉宾id为主键外，这里通过发布会id + 手机号来作为联合主键。Meta是Django模型类的一个内部类，它用于定义一些
    Django模型类的行为特性。unique_together用于设置两个字段为联合主键。
    """
    class Meta:
        unique_together = ("event", "phone")#unique_together用于设置两个字段为联合主键
    def __str__(self):
        return self.realname