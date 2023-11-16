*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  master  mixxxer88
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  master  mixxxer88
    Input Credentials  master  maxxxer99
    Output Should Contain  User with username master already exists

Register With Too Short Username And Valid Password
    Input Credentials  me  2Fancy4U
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Ol'DirtyBa$tard  mypassword
    Output Should Contain  Username is invalid

Register With Valid Username And Too Short Password
    Input Credentials  master  samwise
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  master  samwiseEEEE
    Output Should Contain  Password cannot contain only letters