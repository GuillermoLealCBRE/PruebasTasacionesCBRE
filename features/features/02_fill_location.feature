Feature: Fill in property location
    As a user, I want to provide the property location to proceed with the appraisal process.

    Scenario: Fill in property location
        Given the user is on the appraisal calculation page
        When the user closes the pop-up
        And the user clicks "con referencia catastral"
        And the user enters the cadastral reference "2487901VK4728G0004DX"
        And the user clicks the "Buscar vivienda" button

    Scenario: Select a property
        When the user selects the property with rel "2487901VK4728G0004DX" from the dropdown
        And the user clicks the "Confirmar vivienda" button
        Then the user proceeds to the next step
    
    Scenario: Necesito la tasacion para
        When the user selects "Necesito la tasacion para" as "Asesoramiento"
        And the user clicks the "Continuar" button