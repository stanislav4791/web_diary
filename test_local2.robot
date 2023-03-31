
http://127.0.0.1:5000
tunnus antti ja salasana user

# Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
#     Kirjaudu järjestelmän tunnuksilla
#     Luo uusi artikkeli
#     Anna otsikko ja sisältö
#     Tallenna ja sulje artikkeli
#     Varmista että artikkeli on tallenettu

*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    http://127.0.0.1:5000
${USERNAME}    antti
${PASSWORD}    user
${LINKLOGIN}    http://127.0.0.1:5000/login
${LINKDIARY}    http://127.0.0.1:5000/diary
#${DATE}    30.3.2023        
#${Title}    Robot_testing_Login
#${Sisalto}    work in process

*** Tasks ***
Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
    Avaa selain ja http://127.0.0.1:5000 sivu
    Kirjaudu järjestelmän tunnuksilla
    Luo uusi artikkeli
    Anna pvm ja otsikko ja sisältö
    Tallenna ja sulje artikkeli
    Varmista että artikkeli on tallenettu

*** Keywords ***
Avaa selain ja http://127.0.0.1:5000 sivu            # Millä käskyllä se tekee:
    Open Available Browser    ${OSOITE}

Kirjaudu järjestelmän tunnuksilla
    Open Available Browser    ${LINK}
    #Click link    href    ${LINK}
   #Click Button    type:Log in    #${LINK} 
    Input Text    id:username    ${USERNAME}
    Input Text    id:password    ${PASSWORD}
    Click Button    class:submit 
    #login.html koodissa type locator vaihdettu class niin testi avaa webdiaryn
    #Click Element    xpath://button[@type='submit' and @name='Log In']

Luo uusi artikkeli
    Open Available Browser    ${LINKDIARY}
    #Click Element    class:j-links-link

Anna otsikko ja sisältö
    #Input Text    id:jform_title   ${Title}
    #Wait Until Element Is Visible    jform_articletext_ifr    20
    #Select Frame    id:jform_articletext_ifr
    #Input Text    id:tinymce    ${Sisalto}
    #Unselect Frame

Talenna ja sulje artikkeli
    #Click Button    class:button-save
Varmista että artikkeli on tallenettu
    #Element Should Contain    class:alert-message    Article saved.
