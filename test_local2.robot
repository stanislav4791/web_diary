
http://127.0.0.1:5000
tunnus antti ja salasana user

# Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
#     Kirjaudu järjestelmän tunnuksilla
#     Luo uusi artikkeli
#     Anna otsikko ja sisältö
#     Talenna ja sulje artikkeli
#     Varmista että artikkeli on tallenettu

*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    http://127.0.0.1:5000
${USERNAME}    antti
${PASSWORD}    user
${Title}    Story_of_manager
${Sisalto}    sisalto

*** Tasks ***
Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
    Avaa selain ja http://127.0.0.1:5000 sivu
    Kirjaudu järjestelmän tunnuksilla
    Luo uusi artikkeli
    Anna otsikko ja sisältö
    Talenna ja sulje artikkeli
    Varmista että artikkeli on tallenettu

*** Keywords ***
Avaa selain ja http://127.0.0.1:5000 sivu            # Millä käskyllä se tekee:
    Open Available Browser    ${OSOITE}

Kirjaudu järjestelmän tunnuksilla
    Click Button    type:Log in 
    Input Text    id:username    ${USERNAME}
    Input Text    id:password    ${PASSWORD}
    Click Button    class:submit

Luo uusi artikkeli
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
