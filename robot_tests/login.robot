*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
Login Test

    Open Browser    https://www.saucedemo.com   chrome

    Input Text      id:user-name    standard_user

    Input Text      id:password     secret_sauce

    Click Button    id:login-button

    Close Browser