# -*- coding:utf-8 -*-
import os
#获取当前路径
pwd=os.getcwd()
pwd_path=pwd.replace("\\","/")
print "当前路径是：",pwd_path

# 获取当前项目的根路径
p=os.path.dirname(__file__)
print "p",p


path1=os.path.join(os.path.dirname(__file__),".")
print "path1:",path1

root_path1=os.path.abspath(path1)
print "root_path:1",root_path1

root_path2=os.path.abspath(os.path.join(os.path.dirname(__file__),"."))
print "root_path:2",root_path2

root_path3=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
print "root_path:3",root_path3


root_path4=os.path.abspath(os.path.join(os.path.dirname(__file__),"../../"))
print "root_path:4",root_path4