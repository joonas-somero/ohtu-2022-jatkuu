*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  password1
    Output Should Contain  Username is too short or contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  pekka  pass1
    Output Should Contain  Password must be atleast 8 characters long and contain atleast 1 non-alphabetic character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  password    
    Output Should Contain  Password must be atleast 8 characters long and contain atleast 1 non-alphabetic character

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
