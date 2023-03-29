
http://localhost/phpmyadmin/
tunnus antti ja salasana user

# Testataan että järjestelmään kirjautuminen ja uusien tiedostojen=entries varmuuskopiointi onnistuu
#     Kirjaudu järjestelmän tunnuksilla
#     Luo uusi varmuukopio
#     Anna otsikko ja sisältö
#     Talenna ja sulje artikkeli
#     Varmista että artikkeli on tallenettu

*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    http://localhost/phpmyadmin/    
#${USERNAME}    antti
#${PASSWORD}    user
#${Title}    Story_of_manager
#${Sisalto}    sisalto

*** Tasks ***
Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
    Avaa selain ja http://localhost/phpmyadmin/ sivu
    Kirjaudu järjestelmän tunnuksilla
    Luo uusi artikkeli
    Anna otsikko ja sisältö
    Talenna ja sulje artikkeli
    Varmista että artikkeli on tallenettu

*** Keywords ***
Avaa selain ja j2store.net/freeadmin/administrator/ sivu            # Millä käskyllä se tekee:
    Open Available Browser    ${OSOITE}

Kirjaudu järjestelmän tunnuksilla
    #Input Text    id:mod-login-username    ${USERNAME}
    #Input Text    id:mod-login-password    ${PASSWORD}
    Click Button    class:nav-link text-nowrap

Luo uusi varmuuskopio SQL versio
    Click Element    class:btn btn-primary

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
