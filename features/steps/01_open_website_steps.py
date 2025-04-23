from behave import given, when, then
from selenium.webdriver.common.by import By

# Paso 1 abrimos el navegador
@given('the user opens browser')
def step_given_user_has_opened_browser(context):
    assert context.driver is not None, "Browser is not initialized"

# Paso 2 navegamos a la web de tasaciones
@when('the user navigates to "{url}"')
def step_when_user_navigates_to_website(context, url):
    context.driver.get(url)

# Paso 3 hacer click en el botón "Calcular precio online"
@then('the user clicks the "Calcular precio online" button')
def step_the_user_click_calcularPrecioOnline(context):
    botonCalcularPrecioOnline = context.driver.find_element(By.CLASS_NAME, "primary-btn")
    botonCalcularPrecioOnline.click()