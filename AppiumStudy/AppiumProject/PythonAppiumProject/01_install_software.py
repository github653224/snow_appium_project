# -*- coding:utf-8 -*-
import os,time
from appium import webdriver
class InstallSoftware:
    def __init__(self):
        # 获取当前项目的根路径
        self.apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

        #设置appium server可以接受的参数
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 设备系统
        self.desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
        self.desired_caps['deviceName'] = 'samsung'  # 设备名称

        # 在desired_caps配置里增加以下两项,就可以实现发送中文了
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
        self.desired_caps['noReset'] = False
        # self.desired_caps['noReset'] = True
        # # 测试apk包的路径
        self.desired_caps['app'] = self.apk_path + '\\soft_packge\\shoujibaidu.apk'

        # 应用程序的包名
        self.desired_caps['appPackage'] = 'com.baidu.searchbox'
        self.desired_caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'

        #天猫
        # self.desired_caps['app'] = self.apk_path + '\\soft_packge\\tianmao.apk'
        # self.desired_caps['appPackage'] = 'com.tmall.wireless'
        # self.desired_caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'

    def runAppiumServer(self):
        # 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(15)
        try:
            #去掉立即体验的弹框
            # time.sleep(3)
            # driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()

            # 版本低用来点击去掉更新的弹框
            driver.find_element_by_id("com.baidu.searchbox:id/close").click()

            # 去掉开启锁屏阅读的弹框
            # time.sleep(5)
            # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()
            time.sleep(3)

            driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()
            driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput").send_keys("Halo3224")
            time.sleep(3)
            # 点击搜索按钮
            driver.find_element_by_id("com.baidu.searchbox:id/float_search_or_cancel").click()
        finally:
            driver.quit()

    def click_redian_and_tuijian(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(15)
        try:
            # 去掉立即体验的弹框
            # time.sleep(3)
            # driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()

            # 版本低用来点击去掉更新的弹框
            driver.find_element_by_id("com.baidu.searchbox:id/close").click()

            # 去掉开启锁屏阅读的弹框
            # time.sleep(5)
            # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()
            time.sleep(3)


            # hot = driver.find_element_by_id('com.baidu.searchbox:id/tab_indi_title')
            hot = driver.find_element_by_android_uiautomator("text(\"热点\")")
            hot.click()
            # 点击“推荐”频道
            time.sleep(3)
            rec = driver.find_element_by_android_uiautomator("text(\"推荐\")")
            rec.click()
            hot.click()
        finally:
            driver.quit()

    def click_one_to_four(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(20)
        try:
            # 去掉立即体验的弹框
            # time.sleep(3)
            # driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()

            # 版本低用来点击去掉更新的弹框
            driver.find_element_by_id("com.baidu.searchbox:id/close").click()

            # 去掉开启锁屏阅读的弹框
            # time.sleep(5)
            # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()

            time.sleep(5)
            # 点击“我的”
            driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='4']").click()
            time.sleep(2)
            # 点击“我的关注“
            driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='3']").click()
            time.sleep(2)
            # 点击“麦克风“
            driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='2']").click()
            time.sleep(1)
            # 点击““视频
            driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='1']").click()
            time.sleep(1)
            # 点击“默认主页“
            driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='0']").click()
        finally:
            driver.quit()

    def accessibility_id_test(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(15)
        try:
            time.sleep(5)
            driver.find_element_by_accessibility_id("天猫超市").click()
        finally:
            driver.quit()

    def swipe_test(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(15)
        try:
            # 去掉立即体验的弹框
            # time.sleep(3)
            # driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()

            # 版本低用来点击去掉更新的弹框
            driver.find_element_by_id("com.baidu.searchbox:id/close").click()

            # 去掉开启锁屏阅读的弹框
            # time.sleep(5)
            # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()

            time.sleep(5)
            # 打印屏幕高和宽
            print(driver.get_window_size())
            # 获取屏幕的高
            x = driver.get_window_size()['width']
            # 获取屏幕宽
            y = driver.get_window_size()['height']
            # 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点tab
            driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 100)
            time.sleep(4)
            # 向右滑动，显示推荐tab 内容，第五个参数，时间设置大一点，否则容易看不到滑动效果
            driver.swipe(1 / 7 * x, 1 / 2 * y, 5 / 7 * x, 1 / 2 * y, 200)
            time.sleep(4)
            # 向上滑
            driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
            time.sleep(4)
            # 向下滑动
            driver.swipe(1 / 2 * x, 1 / 7 * y, 1 / 2 * x, 6 / 7 * y, 200)
        finally:
            driver.quit()

    def tag_test(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)  # 启动app
        time.sleep(15)
        try:
            # 去掉立即体验的弹框
            # time.sleep(3)
            # driver.find_element_by_id("com.baidu.searchbox:id/introduction_entrance").click()

            # 版本低用来点击去掉更新的弹框
            driver.find_element_by_id("com.baidu.searchbox:id/close").click()

            # 去掉开启锁屏阅读的弹框
            # time.sleep(5)
            # driver.find_element_by_id("com.baidu.searchbox:id/dialog_close").click()

            time.sleep(5)
            driver.tap([(64,1223),(99,1258)],100)
            time.sleep(10)

            # 截图
            img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
            time1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            screen_save_path = img_folder + time1 + '.png'
            driver.get_screenshot_as_file(screen_save_path)
        finally:
            driver.quit()


if __name__=="__main__":
    InstallSoftware().runAppiumServer()
    InstallSoftware().click_redian_and_tuijian()
    InstallSoftware().click_one_to_four()
    # InstallSoftware().accessibility_id_test()
    InstallSoftware().swipe_test()
    InstallSoftware().tag_test()