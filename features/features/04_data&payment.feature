Feature: Data and Payment
    As a user, I want to provide my personal data and payment information to complete the appraisal process.

    Scenario: Fill in personal data and proceed to payment 
        Given the user is on the data and payment section
        When the user fills in the personal data:
            | field      | value                    |
            | Nombre     | Guillermo                |
            | Apellidos  | Leal Martinez            |
            | Email      | guillermo.leal@email.com |
            | DNI        | 43401519J                |
            | Teléfono   | 627347292                |

        
        # Paso 3.1: Los datos de facturación son los mismos que los personales (Opcion A)
        When the user selects "Los datos de facturación son los mismos que los personales"
        # And the user fills in the billing data:
        #   | field         | value        |
        #   | Calle         | Juan Magan 36|
        #   | Municipio     | Barcelona    |
        #   | Codigo postal | 20329        |
        #   | Provincia     | Barcelona    |

        # Paso 3.2 Introducir datos de facturación manualmente (Opcion B)
        # When the user fills in the billing data manually:
        #     | field      | value                    |
        #     | Nombre     | Guillermo                |
        #     | Apellidos  | Leal Martinez            |
        #     | Email      | guillermo.leal@email.com |
        #     | DNI        | 12345678A                |
        #     | Teléfono   | 627347292                |
        #     | Calle      | Oruro 1, 2               |
        #     | Código postal | 28016                 |
        #     | Municipio  | Madrid                   |
        #     | Provincia  | Madrid                   |

        # Paso 4: Añadir datos adicionales (opcional)
        # When the user fills in the additional data with "INTRODUCIR TEXTO AQUÍ"

    Scenario: Select payment method
        # Opción de tarjeta o bizum
        When the user selects the payment method "tarjeta" 
        When the user clicks the "Aceptar condiciones" checkbox
        And the user clicks the "Pagar" button
        And the user closes the "pagar" pop-up