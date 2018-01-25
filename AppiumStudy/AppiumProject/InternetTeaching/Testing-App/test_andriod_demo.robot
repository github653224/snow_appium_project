*** Settings ***
Library  AppiumLibrary
Documentation   demo for appium library
Resource  ../global.robot

Force Tags  demo

*** Test Cases ***
test_demo
    [Tags]  regression
    Input Text      id=com.android.browser:id/url
