*** Settings ***
Library  RequestsLibrary
Library  Collections
Resource  ../resources/HTTPRequests.robot
*** Variables ***

*** Test Cases ***
Test for Guest If Sign Interface
    Test Procedure
*** Keywords ***
Test Procedure
    ${header} =  Create Dictionary  Content-Type=application/x-www-form-urlencoded
#    ${postdata}=  Create Dictionary  eid=18  name=test002  limit=2000  status=1  address=Tokoyou  start_time=2018-01-16 14:00:00.000000
    Create Session  event  http://127.0.0.1:8989/api
    ${postdata}=  Generate Full JSON Body For Add Event HTTP Request  signevent  SIGN
    Log  ${postdata}
    ${r}=  Post Request  event  /user_sign/  data=${postdata}  headers=${header}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    log  ${dict}

    #断言结果
    ${msg}    Get From Dictionary    ${dict}   message
    Should Be Equal    ${msg}    sign success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}
