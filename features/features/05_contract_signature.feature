Feature: Contract signature
    As a user, I want to sign the contract with docusign.

    Scenario: Sign contract
        Given the user is on the contract signature page
        When the user checks the consent checkbox
        And the user clicks the "Continuar" button on docusign
        And the user clicks the "Firmar" button
        And the user clicks the "Firmar aquí" button
        And the user clicks the "Aceptar y firmar" button
        And the user clicks the "Finalizar" button
        Then the user should see the "Gracias por contratar tu tasación con CBRE" screen