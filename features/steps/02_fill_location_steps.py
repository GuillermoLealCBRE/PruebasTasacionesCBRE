from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# FEATURE 2

# ---------------------------------------------------------------------------------------------------------------

# ESCENARIO 1 SELECCIONAR REF CASTRAL

# Paso 1 verificar que estamos en la pagina y refrescar si hay error de carga
@given('the user is on the appraisal calculation page')
def step_user_is_on_appraisal_calculation_page(context):
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(context.driver, 10).until(
            EC.title_contains("Contrata tu Tasación Oficial Online")
        )
    except TimeoutException:
        context.driver.refresh()
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    except Exception as e:
        raise Exception(f"Error al cargar la página de cálculo de tasación: {e}")

# Paso 2 verificar que el pop-up de la pagina de tasacion se muestre y lo cierre
@when('the user closes the pop-up')
def step_the_user_closes_the_popup(context):
    close_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "cbreModal_close") and @onclick="oncloseTasacionModal(event)"]'))
    )
    close_button.click()

# Paso 3 hacer click en el botón "con referencia catastral"
@when('the user clicks "con referencia catastral"')
def step_the_user_clicks_reference_catastral(context):
    reference_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "step1-type-refcat"))
    )
    reference_button.click()

# Paso 4 introducir la referencia catastral
@when('the user enters the cadastral reference "{reference}"')
def step_the_user_enters_cadastral_reference(context, reference):
    reference_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "refCatastral"))
    )
    reference_input.clear()
    
    # Método para simular escritura manual
    for char in reference:
        reference_input.send_keys(char)
        time.sleep(0.1)
    
    reference_input.send_keys("\n")

# Paso 5 hacer click en Buscar vivienda
@when('the user clicks the "Buscar vivienda" button')
def step_the_user_clicks_search_property(context):
    try:
        BuscarVivienda_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-parcel"))
        )
        if BuscarVivienda_button.is_enabled():
            BuscarVivienda_button.click()
            print('Botón "Buscar vivienda" clickeado correctamente.')
        else:
            raise Exception("El botón 'Buscar vivienda' está deshabilitado.")
    except Exception as e:
        print("Intentando hacer clic en el botón usando JavaScript...")
        try:
            BuscarVivienda_button = context.driver.find_element(By.ID, "search-parcel")
            context.driver.execute_script("arguments[0].click();", BuscarVivienda_button)
            print('Botón "Buscar vivienda" clickeado correctamente usando JavaScript.')
        except Exception as js_error:
            raise Exception(f"Failed to click the 'Buscar vivienda' button even with JavaScript: {js_error}")


# --------------------------------------------------------------------------------------------------------------

# ESCENARIO 2 SELECCIONAR PROPIEDAD

# Paso 6 seleccionar la vivienda del desplegable
@when('the user selects the property with rel "{rel_value}" from the dropdown')
def step_the_user_selects_property_from_dropdown(context, rel_value):
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cbreSelect-element"))
    )
    dropdown.click()
    desired_option = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//li[@rel="{rel_value}"]'))
    )
    desired_option.click()

# Paso 7 verificar que hemos cambiado de paso
@then('the user proceeds to the next step')
def step_the_user_proceeds_to_next_step(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'prop-result'))
    )

# Paso 8 hacer click en el botón confirmar vivienda
@when('the user clicks the "Confirmar vivienda" button')
def step_the_user_clicks_confirm_property(context):
    try:
        confirmar_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirm-vivienda-btn"))
        )
        if confirmar_button.is_enabled():
            context.driver.execute_script("arguments[0].click();", confirmar_button)
        else:
            raise Exception("El botón 'Confirmar vivienda' está deshabilitado.")
    except Exception as e:
        raise Exception(f"Failed to click the 'Confirmar vivienda' button: {e}")

# ---------------------------------------------------------------------------------------------------------------
# ESCENARIO 3

# Paso 9 Seleccionar para que necesito la tasacion
@when('the user selects "Necesito la tasacion para" as "{option}"')
def step_the_user_selects_necesito_la_tasacion(context, option):
    try:
        radio_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//input[@type="radio" and @value[contains(., "{option}")]]'))
        )
        context.driver.execute_script("arguments[0].click();", radio_button)
    except Exception as e:
        raise Exception(f"Failed to select the option '{option}' ")

# Paso 10 Hacer click en el boton "Continuar"
@when('the user clicks the "Continuar" button')
def step_the_user_clicks_continuar(context):
    try:
        continuar_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "get-budget"))
        )
        continuar_button.click()
    except Exception as e:
        raise Exception(f"Failed to click the 'Continuar' button: {e}")