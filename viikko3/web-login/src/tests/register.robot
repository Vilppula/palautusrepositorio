** Settings **
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

** Test Cases **
Register With Valid Username And Password
    Set Username  anssi
    Set Password  kela1972
    Set Password Confirmation  kela1972
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  me
    Set Password  bonbonny1
    Set Password Confirmation  bonbonny1
    Submit Credentials
    Register Should Fail With Message  Username was too short

Register With Valid Username And Invalid Password
    Set Username  mister
    Set Password  spock
    Set Password Confirmation  spock
    Submit Credentials
    Register Should Fail With Message  Password should not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  anssi
    Set Password  kela1972
    Set Password Confirmation  kala1972
    Submit Credentials
    Register Should Fail With Message  You entered two different passwords


Login After Successful Registration
    Set Username  juice
    Set Password  le$kinen
    Set Password Confirmation  le$kinen
    Submit Credentials
    Register Should Succeed
    Go To Starting Page
    Click Link  Login
    Login Page Should Be Open
    Input Text  username  juice
    Input Password  password  le$kinen
    Click Button  Login
    Login Should Succeed


Login After Failes Registration
    Set Username  Juice
    Set Password  leskinen
    Set Password Confirmation  leskinen
    Submit Credentials
    Go To Starting Page
    Click Link  Login
    Login Page Should Be Open
    Input Text  username  Juice
    Input Password  password  leskinen
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password


** Keywords **
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

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

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}