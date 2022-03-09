*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short or contains invalid characters

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  pass1
    Set Confirmation  pass1
    Submit Credentials
    Register Should Fail With Message  Password must be atleast 8 characters long and contain atleast 1 non-alphabetic character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle000
    Submit Credentials
    Register Should Fail With Message  Password does not match confirmation

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open
