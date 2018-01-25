*** Settings ***
Library  AppiumLibrary
Resource  ../Settings/AndroidCapacitySetting.robot
*** Variables ***
#${REMOTE_URL}  http://localhost:4723/wd/hub
#${platformName}  Android
#${platformVersion}  4.4.2
#${deviceName}  samsung
#${automationName}  appium
#${tianmao_app_path}  D:/AppiumProject/soft_packge/tianmao.apk
#${appPackage}  com.tmall.wireless
#${appActivity}  com.tmall.wireless.splash.TMSplashActivity
*** Test Cases ***
Test Procedure
    Test Tianmao  com.tmall.wireless  com.tmall.wireless.splash.TMSplashActivity
*** Keywords ***
Test Tianmao
#    [Arguments]  ${appPackage}  ${appActivity}
    Open Application  ${Remote_Url}  platformName=${platformName}  platformVersion=${platformVersion}  deviceName=${deviceName}  app=${tianmao_app_path}  automationName=${automationName}  appPackage=${appPackage}  appActivity=${appActivity}
#    Open Application  ${REMOTE_URL}  platformName=${platformName}  platformVersion=${platformVersion}  deviceName=${deviceName}  app=${tianmao_app_path}  automationName=${automationName}  appPackage=${appPackage}  appActivity=${appActivity}
    Sleep  5s
    Close All Applications
