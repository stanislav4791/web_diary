
http://127.0.0.1:5000
tunnus antti ja salasana user

# Testataan että järjestelmään kirjautuminen onnistuu
#     Kirjaudu järjestelmän tunnuksilla

*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    http://127.0.0.1:5000
${USERNAME}    antti
${PASSWORD}    user
${LINKLOGIN}    http://127.0.0.1:5000/login

*** Tasks ***
Testataan että järjestelmään kirjautuminen onnistuu
    Avaa selain ja http://127.0.0.1:5000 sivu
    Kirjaudu järjestelmän tunnuksilla
    
*** Keywords ***
Avaa selain ja http://127.0.0.1:5000 sivu            
    Open Available Browser    ${OSOITE}

Kirjaudu järjestelmän tunnuksilla
    Open Available Browser    ${LINKLOGIN}
    Input Text    id:username    ${USERNAME}
    Input Text    id:password    ${PASSWORD}
    Click Button    id:submit 
    #login.html koodissa type submit kohtaan lisätty id:locator    

