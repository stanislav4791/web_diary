*** Settings ***
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    RPA.Desktop

*** Variables ***
${OSOITE}    https://www.taitotalo.fi
${HAKUSANA}    Python

*** Tasks ***
Etsi Taitotalon sivustolta python kurssia
    Avaa selain ja taitotalon sivu
    Hyväksy evästeet
    Täytä hakulomake hakusanalla
    Paina Etsi painiketta
    Hakeudu ensimmäiseen kurssiin
    Hae koulutuksen

*** Keywords ***
Avaa selain ja taitotalon sivu            # Millä käskyllä se tekee:
    Open Available Browser    ${OSOITE}

Hyväksy evästeet
    Click Button    class:coi-banner__accept

Täytä hakulomake hakusanalla
    Input Text    hakusanat    ${HAKUSANA}

Paina Etsi painiketta
    Click Element    id=edit-submit-search-results

Hakeudu ensimmäiseen kurssiin
    Click Element    class:button-register
 
Hae koulutuksen
    #Get Window Names
    Switch Window    New
    Click Element When Visible    class:cc-allow
    Click Element When Visible    class:btn-default
