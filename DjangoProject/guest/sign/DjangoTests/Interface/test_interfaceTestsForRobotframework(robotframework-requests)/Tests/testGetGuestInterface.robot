*** Settings ***
Library  RequestsLibrary
Library  Collections
*** Variables ***

*** Test Cases ***
Test for Checking Guest Interface
    Test Procedure
*** Keywords ***
Test Procedure
    ${payload}=  Create Dictionary  eid=1  phone=18000000000
    Create Session  event  http://127.0.0.1:8989/api
    ${r}=  Get Request  event  /get_guest_list/  params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    log  ${dict}

    #断言结果
    ${msg}    Get From Dictionary    ${dict}   message
    Should Be Equal    ${msg}    success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}
    ${data_dict}  Get From Dictionary  ${dict}  data
    ${phone_number}  Get From Dictionary  ${data_dict}  phone
    Should Be Equal As Strings  ${phone_number}  18000000000
