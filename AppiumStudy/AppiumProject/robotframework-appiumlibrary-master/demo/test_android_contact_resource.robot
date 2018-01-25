*** Settings ***
Library           AppiumLibrary

*** Variables ***
${REMOTE_URL}  http://localhost:4723/wd/hub
${PLATFORM_NAME}  Android
${PLATFORM_VERSION}  4.4.2
${DEVICE_NAME}  Android Emulator
${APP}  ${CURDIR}/demoapp/ContactManager.apk
*** Test Cases ***
Test Procetrue
    add new contact  pxy 18910193189  944851899@qq.com
*** Keywords ***
add new contact
    [Arguments]    ${contact_name}    ${contact_phone}    ${contact_email}
    Open Application  ${REMOTE_URL}  platformName=Android  platformVersion=${PLATFORM_VERSION}  deviceName=samsung  app=${APP}  automationName=appium  appPackage=com.example.android.contactmanager
    Click Element    accessibility_id=Add Contact
    Input Text    id=com.example.android.contactmanager:id/contactNameEditText    ${contact_name}
    Input Text    id=com.example.android.contactmanager:id/contactPhoneEditText    ${contact_phone}
    Input Text    id=com.example.android.contactmanager:id/contactEmailEditText    ${contact_email}
    Click Element
    uiautomator
    Click Element    accessibility_id=Save
