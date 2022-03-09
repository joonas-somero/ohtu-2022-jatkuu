*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is too short or contains invalid characters

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  pass1
    Set Confirmation  pass1
    Submit Registration
    Registration Should Fail With Message  Password must be atleast 8 characters long and contain atleast 1 non-alphabetic character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle000
    Submit Registration
    Registration Should Fail With Message  Password does not match confirmation

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle123
    Submit Registration
    Registration Should Fail With Message  Password does not match confirmation
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open
