*** Settings ***
Library  AppiumLibrary
Library  Screenshot
Resource  ../Settings/AndroidCapacitySetting.robot
*** Variables ***

*** Test Cases ***
Test Procedure
    Test Browser

*** Keywords ***
Open Browser
    [Arguments]  ${browserName}
    Open Application  ${Remote_Url}  platformName=${platformName}  platformVersion=${platformVersion}  deviceName=${deviceName}  automationName=${automationName}  browserName=${browserName}  unicodeKeyboard=True  resetKeyboard=True

Click Shouji Baidu Tiyan Pop-ups
#    Wait Until Keyword Succeeds  10s  0.5s  Click Element  id=com.baidu.searchbox.lite:id/rs
    Wait Until Keyword Succeeds  10s  0.5s  Click Button  index=0
Go To And Open Url
    [Arguments]  ${url}
    Go To Url  ${url}


Test Browser
    Open Browser  Baidu
    Click Shouji Baidu Tiyan Pop-ups
#    Go To And Open Url  https://www.baidu.com
    Sleep  3s
    Close All Applications