import os,time
from appium import webdriver

def takePic():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """
   Take Screen Shot
   """
    img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
    # print img_folder
    time1 = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    screen_save_path = img_folder + time1 + '.png'
    webdriver().get_screenshot_as_file(screen_save_path)
    print "hello"
