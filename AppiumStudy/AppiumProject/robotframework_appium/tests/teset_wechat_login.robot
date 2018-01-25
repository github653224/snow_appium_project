*** Settings ***
Library  AppiumLibrary
*** Variables ***
*** Test Cases ***
Test Protrue
    Open Application Test  Android  4.4.2  samsung  D:/PythonProjects/AppiumProject/soft_packge/weixin.apk
#    Open Application Test  Android  4.2.2  169.254.190.101:5555  D:/PythonProjects/AppiumProject/soft_packge/weixin.apk

*** Keywords ***
Open Application Test
    [Arguments]  ${platformName}  ${platformVersion}  ${deviceName}  ${app_path}
    Open Application  http://localhost:4723/wd/hub  platformName=${platformName}  platformVersion=${platformVersion}  deviceName=${deviceName}  app=${app_path}  appPackage=com.tencent.mm  appActivity=com.tencent.mm.ui.LauncherUI  unicodeKeyboard=True  noReset=True
#    Wait Until Page Contains  登录  timeout=120
    Wait Until Page Contains  Log In  timeout=120
    Sleep  5s
    #这两句都可以
#    Click Element  xpath=//android.widget.Button[@text="登录"]
    Click Element  xpath=//*[@class="android.widget.Button"]
#    Page Should Contain Text  手机号登录
    Page Should Contain Text  Use WeChat ID/Email/QQ ID to Log in
    Click Element  xpath=//*[@class="android.widget.Button"]
#    Page Should Contain Text  用手机号登录
    Page Should Contain Text  Log in via mobile number
#    input text  xpath=//android.widget.EditText[contains(@text,"请填写微信号/QQ号/邮箱")][1]  944851899@qq.com
    input text  xpath=(//android.widget.EditText)[1]  eamil@qq.com
    input text  xpath=(//android.widget.EditText)[2]  password
#    Click Element  xpath=//android.widget.Button[contains(@text,"登录")]
    Click Element  xpath=//android.widget.Button[contains(@text,"Log In")]
    Sleep  6s
    Close All Applications