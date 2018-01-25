*** Settings ***
Library  AppiumLibrary
 #Resource        demo_resources.txt
 #Variables    variables.py

*** Variables ***

*** Keywords ***
Start Suite Setup
#  Close All Applications
  Open Application  http://localhost:4723/wd/hub  platformName=Android  platformVersion=4.4.2  deviceName=samsung  app=D:/AppiumProject/InternetTeaching/apps/qihubrowser.apk  automationName=appium  appPackage=com.qihoo.browser  appActivity=com.qihoo.browser.launcher.LauncherActivity
  Sleep     20

Stop Suite Setup
 Close All Applications

Login Test Setup
 Portrait

Login Test Teardown
 Capture Page Screenshot