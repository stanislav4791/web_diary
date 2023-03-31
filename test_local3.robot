

http://127.0.0.1:5000
tunnus antti ja salasana user

# Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
#     Kirjaudu järjestelmän tunnuksilla
#     Avataan scraping välilehti
#     Avataan ensimmäinen uutinen
#     Painetaan Contact us buttonia

*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    http://127.0.0.1:5000
${USERNAME}    antti
${PASSWORD}    user
${LINKLOGIN}    http://127.0.0.1:5000/login
${LINKSCRAPING}    http://127.0.0.1:5000/news    
${LINKCONTACTUS}    http://127.0.0.1:5000/news#footer        
#${LINKNEWS2}    Robot_testing_Login


*** Tasks ***
Testataan että järjestelmään kirjautuminen ja uusien artikkelien luonti onnistuu
    Avaa selain ja http://127.0.0.1:5000 sivu
    Kirjaudu järjestelmän tunnuksilla
    Avataan scraping välilehti
   
*** Keywords ***
Avaa selain ja http://127.0.0.1:5000 sivu            # Millä käskyllä se tekee:
    Open Available Browser    ${OSOITE}

Kirjaudu järjestelmän tunnuksilla
    Open Available Browser    ${LINKLOGIN}
    #Click link    href    ${LINK}
    #Click Element    class:Log in    #${LINK} 
    Input Text    id:username    ${USERNAME}
    Input Text    id:password    ${PASSWORD}
    Click Button    class:submit
    #Click LINK    href:http://127.0.0.1:5000/news 
    #login.html koodissa type locator vaihdettu class niin testi avaa webdiaryn
    #Click Element    xpath://button[@type='submit' and @name='Log In']

Avataan scraping välilehti
    Open Available Browser    ${LINKSCRAPING}
    Click Element    class:news_link
    #Wait Until Element Is Visible    id:yle-consent-sdk-container    
    #Select Frame    class:ycd-content     
    #Click Button    class:ycd-consent-buttons_button primary        
    #Click link    href:class:news_link
    Open Available Browser    ${LINKCONTACTUS}    
    
#Painetaan Contact us buttonia
    #Switch Window    NEWS
    #Open Available Browser    ${LINKCONTACTUS}
    #Switch Window    news#footer
    #Click link    href:#footer