# -*- coding:utf-8 -*-
import os,time
from appium import webdriver
import sys

from appium.webdriver import webelement

reload(sys)
sys.setdefaultencoding('utf-8')


apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
print apk_path
desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
desired_caps['deviceName'] = 'samsung'  # 设备名称
# 在desired_caps配置里增加以下两项,就可以实现发送中文了
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
# desired_caps['noReset'] = False
# 测试apk包的路径
desired_caps['app'] = apk_path + '\\soft_packge\\shoujibaidu.apk'
# 不需要每次都安装apk

# 应用程序的包名
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(20)  # app启动后等待5秒，方便元素加载完成
# 根据元素id来定位
###################################################################
# 第一次安装时要执行这三句
#点击立即体验
# try:
#     driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()
# finally:
#     driver.quit()

try:
    #版本低用来点击去掉更新的弹框
    # driver.find_element_by_id("com.baidu.searchbox:id/close").click()
    # time.sleep(5)
    # # 关闭锁屏阅读提示框
    # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()
    # time.sleep(5)
    # 点击手机百度搜索框
    driver.find_element_by_xpath("//android.widget.Button[contains(@text,'点麦克风,百度一下')]").click()
    time.sleep(3)
    # driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'取消')]").click()
    driver.find_element_by_id("com.baidu.searchbox:id/float_search_or_cancel").click()

    #一个一个的点击
    # time.sleep(3)
    # driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'热点')]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'小说')]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'2018')]").click()

    #利用for循环点击元素并判断复合调价了跳出循环
    lists = driver.find_elements_by_xpath("//android.widget.TextView")
    for list in lists:
        name = list.get_attribute("text")
        if name=="2018":
            list.click()
            time.sleep(2)
            break
        else:
            time.sleep(2)
            list.click()

    driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()

    # # 向手机百度搜索框中输入
    driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").send_keys("Halo3224")
    time.sleep(3)
    # # 点击搜索按钮
    driver.find_element_by_id("com.baidu.searchbox:id/float_search_or_cancel").click()
    time.sleep(3)
    driver.find_element_by_class_name("android.view.View").click()
    time.sleep(3)
    driver.back()
    driver.back()

    driver.find_elements_by_android_uiautomator("text(\"图片\")")
    time.sleep(3)
    driver.find_element_by_id("com.baidu.searchbox:id/baidu_searchbox").click()
    time.sleep(3)
    driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").click()
    time.sleep(3)
    driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").send_keys(u"潘雪岩")
    time.sleep(3)
    driver.find_element_by_id("com.baidu.searchbox:id/float_search_or_cancel").click()
    time.sleep(3)

finally:
    driver.quit()