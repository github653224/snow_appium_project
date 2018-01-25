*** Settings ***
Library  Selenium2Library
Library  Collections
Library  String
Library  Screenshot
Library  OperatingSystem
Library  ../LibraryF/TemplateTool.py

*** Keywords ***
Generate Full JSON Body For Add Event HTTP Request
    [Documentation]  Generate full JSON body For Add Event HTTP request
    ...
    ...              Example:
    ...              | Generate Full JSON Body For HTTP Request | request_type =addevent|
    [Arguments]  ${request_type}  ${event_name}

    Should Not Be Empty  ${request_type}
    ${output}=  getEVENTJsonTemplate  ${request_type}  ${event_name}
    Log  ${output}
    [Return]  ${output}