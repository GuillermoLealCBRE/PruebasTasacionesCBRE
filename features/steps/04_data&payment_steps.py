from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Paso 1 verficar que estamos en la pagina de datos y pago
@given('the user is on the data and payment section')
def step_user_is_on_data_payment_section(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tasacion-step3"]/div[1]/div/div[1]'))
    )
    time.sleep(2)

# Paso 2 rellenar campos de datos personales
@when('the user fills in the personal data')
def step_user_fills_personal_data(context):
    field_mapping = {
        "Nombre": (By.ID, "tasacionStep1_name"),
        "Apellidos": (By.ID, "tasacionStep1_surname"),
        "Email": (By.ID, "tasacionStep1_email"),
        "DNI": (By.ID, "tasacionStep1_dni"),
        "Teléfono": (By.ID, "tasacionStep1_phone1"),
    }

    for row in context.table:
        field = row['field']
        value = row['value']

        if field in field_mapping:
            selector_type, selector_value = field_mapping[field]
            input_element = context.driver.find_element(selector_type, selector_value)
            input_element.send_keys(value)
        else:
            raise ValueError(f"El campo '{field}' no es reconocido.")
    time.sleep(2)

# Paso 3.1.1 seleccionar check "Los datos de facturación son los mismos que los personales" (OPCION A)
@when('the user selects "Los datos de facturación son los mismos que los personales"')
def step_user_selects_billing_like_personal(context):
    try:
        checkbox = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "billing_like_personal"))
        )
        context.driver.execute_script("arguments[0].click();", checkbox)
    except Exception as e:
        raise Exception(f"Failed to select the checkbox 'Los datos de facturación son los mismos que los personales': {e}")

# Paso 3.1.2 rellenar datos de facturación (OPCION A)
@when('the user fills in the billing data')
def step_user_fills_billing_data(context):
    field_mapping = {
        "Calle": (By.ID, "tasacionStep1_billing_address"),
        "Municipio": (By.CLASS_NAME, "select2-selection__rendered"),
        "Codigo postal": (By.ID, "tasacionStep1_billing_postal"),
        "Provincia": (By.ID, "tasacionStep1_billing_state"),
    }

    for row in context.table:
        field = row['field']
        value = row['value']

        if field in field_mapping:
            selector_type, selector_value = field_mapping[field]

            # Manejar el campo Municipio de manera especial
            # -----
        
# Paso 4 rellenar datos adicionales (OPCIONAL)
@when('the user fills in the additional data with "{additional_text}"')
def step_user_fills_additional_data(context, additional_text):
    try:
        additional_data_field = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tasacionStep1_comments"))
        )
        additional_data_field.clear()
        additional_data_field.send_keys(additional_text)
    except Exception as e:
        raise Exception(f"Failed to fill in additional data: {e}")

# ESCENARIO 2 SELECCIONAR MÉTODO DE PAGO
# ------------------------------------------

# Paso 5: El usuario selecciona el método de pago
@when('the user selects the payment method "{payment_method}"')
def step_user_selects_payment_method(context, payment_method):
    try:
        payment_radio = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//input[@type="radio" and @value="{payment_method.lower()}"]'))
        )
        if not payment_radio.is_selected():
            context.driver.execute_script("arguments[0].click();", payment_radio)
    except Exception as e:
        raise Exception(f"Failed to select the payment method '{payment_method}': {e}")

# Paso 6: El usuario selecciona el checkbox de aceptar condiciones
@when('the user clicks the "Aceptar condiciones" checkbox')
def step_user_clicks_accept_conditions_checkbox(context):
    try:
        conditions_checkbox = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tasacionStep1_condition"))
        )
        if not conditions_checkbox.is_selected():
            context.driver.execute_script("arguments[0].click();", conditions_checkbox)
    except Exception as e:
        raise Exception(f'Failed to click the "Aceptar condiciones" checkbox: {e}')

# Paso 7: El usuario pulsa el botón de pagar
@when('the user clicks the "Pagar" button')
def step_user_clicks_pay_button(context):
    try:
        pay_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tasacion-step3"]/div[13]/div/button'))
        )
        context.driver.execute_script("arguments[0].scrollIntoView(true);", pay_button)
        context.driver.execute_script("arguments[0].click();", pay_button) 
    except Exception as e:
        raise Exception(f'Failed to click the "Pagar" button: {e}')

# Paso 8: El usuario cierra el pop-up
@when('the user closes the "pagar" pop-up')
def step_user_closes_popup(context):
    try:
        popup_close_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'modalFirmaContinuar'))
        )
        popup_close_button.click()
    except Exception as e:
        raise Exception(f'Failed to close the pop-up: {e}')

# ESCENARIO 3 PAGO CON TARJETA
# ------------------------------------------

# Paso 9: Comprobar que la pasarela de pago se ha cargado correctamente
@given('the user is on the payment page')
def step_user_is_on_payment_page(context):
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    except Exception as e:
        raise Exception(f"Error al cargar la página de pago: {e}")

# Paso 10: Rellenar datos de la tarjeta
@when('the user fills in the card details')
def step_user_fills_card_details(context):
    field_mapping = {
        "Número": (By.ID, "card-number"),
        "Caducidad": (By.ID, "card-expiration"),
        "CVV": (By.ID, "card-cvv"),
    }

    # Cambiamos al contexto del iframe
    WebDriverWait(context.driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )

    for row in context.table:
        field = row['field']
        value = row['value']
        
        if field in field_mapping:
            selector_type, selector_value = field_mapping[field]
            input_element = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located((selector_type, selector_value))
            )
            input_element.clear()

            for char in value :
                input_element.send_keys(char)
                time.sleep(0.1)
            if field == "CVV":
                input_element.send_keys(Keys.ENTER)
        else:
            raise ValueError(f"El campo '{field}' no es reconocido.")
        
    context.driver.switch_to.default_content()

    time.sleep(12)

# Paso 11: El usuario pulsa el botón de pagar
@when('the user clicks the "Pagar" button on the payment page')
def step_user_clicks_pay_button(context):
    context.driver.find_element(By.TAG_NAME, "body").click()
    pay_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'divImgAceptar'))
    )
    pay_button.click()
    time.sleep(15)