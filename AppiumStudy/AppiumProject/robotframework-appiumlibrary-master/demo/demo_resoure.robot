####################################################################################
# 一些Robot内建变量
# ${CURDIR}，提供当前测试文件存放的绝对路径，该变量是大小写敏感的
# ${TEMPDIR}，获取操作系统临时文件夹的绝对路径，在UNIX like系统中是/tmp，
#   在windows系统中是c:\Documents and Settings\<user>\Local Settings\Temp
# ${ECECDIR}，获取测试执行开始目录的绝对路径
# ${/}，操作系统的路径分隔符，在UNIX like系统中是‘/'，在windows系统中是'\'
# ${:}，系统路径元素分隔符，在UNIX like系统中是':'，在windows系统中是';'
#####################################################################################

*** Settings ***
Library         AppiumLibrary  run_on_failure=Log Source
#Library         AppiumLibrary

*** Variables ***
${REMOTE_URL}  http://localhost:4723/wd/hub

*** Test Cases ***
Test Protrue
    TestStart


*** Keywords ***
TestStart
    [Documentation]  just demo
    Open Application  ${REMOTE_URL}  platformName=Android  platformVersion=4.2.2  deviceName=169.254.228.101:5555  app=${CURDIR}/demoapp/OrangeDemoApp.apk  automationName=appium  appPackage=com.netease.qa.orangedemo  appActivity=MainActivity
    Capture Page Screenshot