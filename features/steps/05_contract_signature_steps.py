from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paso 1: Esperar a que la página de firma de contrato esté completamente cargada
@given('the user is on the contract signature page')
def step_user_is_on_contract_signature_page(context):
    WebDriverWait(context.driver, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    iframe = WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.ID, "docusign-iframe"))
    )
    context.driver.switch_to.frame(iframe)

# Paso 2: Marcar el checkbox de consentimiento
@when('the user checks the consent checkbox')
def step_user_checks_consent_checkbox(context):
    consent_checkbox = WebDriverWait(context.driver, 25).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-1xy7dcr"))
    )
    consent_checkbox.click()

# Paso 3: Hacer clic en el botón "Continuar"
@when('the user clicks the "Continuar" button on docusign')
def step_user_clicks_continuar_button(context):
    blocking_elements = context.driver.find_elements(By.CLASS_NAME, "stepwizard-row")
    for element in blocking_elements:
        context.driver.execute_script("arguments[0].style.display = 'none';", element)
        
    continuar_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="ersd-modal-agree"]'))
    )
    continuar_button.click()

# Paso 4: Hacer click en el botón "Firmar"
@when('the user clicks the "Firmar" button')
def step_user_clicks_iniciar_button(context):
    firmar_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "navigate-btn"))
    )
    context.driver.execute_script("arguments[0].click();", firmar_button)

# Paso 5: Hacer click en el botón "Firmar aquí"
@when('the user clicks the "Firmar aquí" button')
def step_user_clicks_firmar_aqui_button(context):
    firmar_aqui_image = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tab-complete-image.signature-image"))
    )
    context.driver.execute_script("arguments[0].click();", firmar_aqui_image)

# Paso 6: Hacer click en el botón "Aceptar y firmar"
@when('the user clicks the "Aceptar y firmar" button')
def step_user_clicks_adoptar_y_firmar_button(context):
    adoptar_y_firmar_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='adopt-submit']"))
    )
    adoptar_y_firmar_button.click()

# Paso 7: Hacer click en el botón "Finalizar"
@when('the user clicks the "Finalizar" button')
def step_user_clicks_finalizar_button(context):
    finalizar_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "slide-up-bar-finish-button"))
    )
    finalizar_button.click()

# Paso 8: Comprobar que la tasación se ha contratado correctamente
@then('the user should see the "Gracias por contratar tu tasación con CBRE" screen')
def step_user_sees_success_screen(context):
    success_message = WebDriverWait(context.driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Gracias por realizar tu tasación con CBRE')]"))
    )
    assert success_message.is_displayed(), "El mensaje de éxito no se mostró en la pantalla."