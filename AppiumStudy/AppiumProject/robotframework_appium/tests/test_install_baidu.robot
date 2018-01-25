*** Settings ***
Library  AppiumLibrary  run_on_failure=Log Source
Library  Screenshot
Resource  ../Settings/AndroidCapacitySetting.robot
Library  ../Library/takepictrue.py
*** Variables ***

*** Test Cases ***
Test Procedure
    Shouji Baidu Search  潘雪岩
*** Keywords ***
App Property Settings
    [Arguments]  ${appPackage}  ${appActivity}
    Open Application  ${Remote_Url}  platformName=${platformName}  platformVersion=${platformVersion}  deviceName=${deviceName}  automationName=${automationName}  app=${shoujibaidu_app_path}  appPackage=${appPackage}  appActivity=${appActivity}  unicodeKeyboard=True



Click Shouji Baidu Tiyan Pop-ups
    Wait Until Keyword Succeeds  10s  0.5s  Click Element  id=com.baidu.searchbox.lite:id/rs


Click Shouji Baidu Searchbox
    Wait Until Keyword Succeeds  10s  0.5s  Click Element  xpath=//*[@class="android.widget.Button"]


Input Test into Shouji Baidu Searchbox
    [Arguments]  ${search_text}
    Wait Until Keyword Succeeds  10s  0.5s  Input Text  xpath=//*[@class="android.widget.EditText"]  ${search_text}

Clear Text in Shouji Baidu Searbox
    Wait Until Keyword Succeeds  10s  0.5s  Clear Text  xpath=//*[@class="android.widget.EditText"]

Click Shouji Baidu Search Button
     Wait Until Keyword Succeeds  10s  0.5s  Click Element  id=com.baidu.searchbox.lite:id/a25

Shouji Baidu Search
    [Arguments]  ${search_text}
    App Property Settings  com.baidu.searchbox.lite  com.baidu.searchbox.SplashActivity
    Click Shouji Baidu Tiyan Pop-ups
    Click Shouji Baidu Searchbox
    sleep  5s

    Input Test into Shouji Baidu Searchbox  ${search_text}
    Clear Text in Shouji Baidu Searbox
    Input Test into Shouji Baidu Searchbox  Halo3224
    Clear Text in Shouji Baidu Searbox
    Input Test into Shouji Baidu Searchbox  潘雪岩
    Click Shouji Baidu Search Button
    sleep  3s
    Go Back
    # 截屏 截正在测试的手机屏或者电脑屏幕不会截整个个屏幕
    Capture Page Screenshot  D:/AppiumProject/robotframework_appium/screenshots/a.png
    Sleep  3s
    #截屏 设置截屏路径
    Screenshot.Set Screenshot Directory  ${CURDIR}/screeshots
    #截屏 截整个电脑屏幕
    Take Screenshot     my_image.png

    Sleep  5s
    Close All Applications
