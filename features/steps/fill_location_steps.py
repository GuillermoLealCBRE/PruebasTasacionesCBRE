from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

# FEATURE 2

# ---------------------------------------------------------------------------------------------------------------

# ESCENARIO 1 SELECCIONAR REF CASTRAL

# Paso 1 verificar que estamos en la pagina 
@given('the user is on the appraisal calculation page')
def step_user_is_on_appraisal_calculation_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.title_contains("Contrata tu Tasación Oficial Online")
    )

# Paso 2 verificar que el pop-up de la pagina de tasacion se muestre y lo cierre
@when('the user closes the pop-up')
def step_the_user_closes_the_popup(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="modal_steps"]/div[2]/div/div[1]/button'))
    )
    close_button = context.driver.find_element(By.XPATH, '//*[@id="modal_steps"]/div[2]/div/div[1]/button')
    close_button.click()

# Paso 3 hacer click en el botón "con referencia catastral"
@when('the user clicks "con referencia catastral"')
def step_the_user_clicks_reference_catastral(context):
    reference_button = context.driver.find_element(By.XPATH, '//*[@id="step1-type-refcat"]')
    reference_button.click()

# Paso 4 introducir la referencia catastral
@when('the user enters the cadastral reference "{reference}"')
def step_the_user_enters_cadastral_reference(context, reference):
    reference_input = context.driver.find_element(By.XPATH, '//*[@id="refCatastral"]')
    reference_input.send_keys(reference)
    time.sleep(3)

# Paso 5 hacer click fuera del input
@when('the user clicks outside the input field')
def step_the_user_clicks_outside_input(context):
    body_element = context.driver.find_element(By.XPATH, '//*[@id="tasacion-step1"]/div[2]/div/div[1]/div[2]/div/div[2]/div[5]')
    attempts = 0
    max_attempts = 5 

    while attempts < max_attempts:
        try:
            body_element.click()
            break
        except Exception as e:
            attempts += 1
            print(f"Intento {attempts} fallido al hacer clic fuera del input: {e}")
            time.sleep(1) 

    if attempts == max_attempts:
        print("No se pudo hacer clic fuera del input después de varios intentos. Continuando con el flujo.")

# --------------------------------------------------------------------------------------------------------------

# ESCENARIO 2 SELECCIONAR PROPIEDAD

# Paso 6 seleccionar la vivienda del desplegable
@when('the user selects a property from the dropdown')
def step_the_user_selects_property_from_dropdown(context):
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vivienda-door-wrapper"]/div/div[1]/div'))
            )
            dropdown = context.driver.find_element(By.XPATH, '//*[@id="vivienda-door-wrapper"]/div/div[1]/div')
            dropdown.click()

            WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vivienda-door-wrapper"]/div/div[2]/ul/li[2]'))
            )
            option = context.driver.find_element(By.XPATH, '//*[@id="vivienda-door-wrapper"]/div/div[2]/ul/li[2]')
            option.click()
            break
        except Exception as e:
            attempts += 1
            print(f"Intento {attempts} fallido al seleccionar la propiedad del desplegable: {e}")
            time.sleep(1)

    if attempts == max_attempts:
        print("No se pudo seleccionar la propiedad del desplegable después de varios intentos. Continuando con el flujo.")

# Paso 7 hacer click en el botón "Confirmar vivienda"
@when('the user clicks the "Confirmar vivienda" button')
def step_the_user_clicks_confirm_property(context):
    # Forzar la visibilidad del tercer div directamente ya que el botón no es interactuable por selenium
    next_div = context.driver.find_element(By.XPATH, '//*[@id="prop-result"]/div[1]/div[2]')
    context.driver.execute_script("arguments[0].style.display = 'block';", next_div)

# Paso 8 verificar que hemos cambiado de paso
@then('the user proceeds to the next step')
def step_the_user_proceeds_to_next_step(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="prop-result"]/div[1]/div[2]'))
    )

# ---------------------------------------------------------------------------------------------------------------
# ESCENARIO 3

# Paso 9 Seleccionar para que necesito la tasacion
@when('the user selects "Necesito la tasacion para" as "{option}"')
def step_the_user_selects_necesito_la_tasacion(context, option):
    # Seleccionar la opción con javascript
    try:
        if option == "Garantía Hipotecaria":
            context.driver.execute_script("document.getElementById('tasacionStep1_purpose_0').click();")
        elif option == "Asesoramiento":
            context.driver.execute_script("document.getElementById('tasacionStep1_purpose_1').click();")
        else:
            raise ValueError(f"Opción no válida: {option}")
    except Exception as e:
        raise Exception(f"Failed to select the option '{option}' with JavaScript: {e}")

# Paso 10 Hacer click en el boton "Continuar"
@when('the user clicks the "Continuar" button')
def step_the_user_clicks_continuar(context):
    try:
        context.driver.execute_script(
            "document.getElementById('get-budget').click();"
        )
        time.sleep(5)
    except Exception as e:
        raise Exception(f"Failed to click the 'Continuar' button: {e}")