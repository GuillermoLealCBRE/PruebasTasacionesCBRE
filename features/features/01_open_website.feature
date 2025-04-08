Feature: Open website and start appraisal process
    As a user, I want to open the website and click the "Calcular precio online" button to start the appraisal process.

    Scenario: Open the website and click "Calcular precio online"
        Given the user opens browser
        When the user navigates to "https://test-tasaciones.cbre.es/"
        Then the user clicks the "Calcular precio online" button