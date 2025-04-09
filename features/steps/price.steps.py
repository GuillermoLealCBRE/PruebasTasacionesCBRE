from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

# FEATURE 3 ESCENARIO 1

# ---------------------------------------

# Paso 1 Verificar que el usuario está en la página de precios
@given('the user is on the price section')
def step_user_is_on_price_step(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tasacion-step2"]/div[2]'))
    )

# Paso 2 Introducir un Cupón Promocional
# Comentado debido a ya incluir un cupon por defecto al estar en campaña por provincia
#@then('the user applies the promotional coupon "{coupon}"')
def step_user_applies_promotional_coupon(context, coupon):
    try:
        promo_input = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cupon_text"]'))
        )
        promo_input.clear()
        promo_input.send_keys(coupon)

        apply_button = context.driver.find_element(By.XPATH, '//*[@id="bt_desc"]')
        apply_button.click()
    except Exception as e:
        raise Exception(f"Failed to apply the promotional coupon '{coupon}': {e}")
    
# Paso 3 pulsar boton "Continuar"
@then('the user clicks the continue button')
def step_user_clicks_continue_button(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, 'tasacion-bottom-contact'))
        )
    except TimeoutException:
        print("The blocking element did not disappear. Proceeding to click the button anyway.")

    try:
        continue_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="aceptar-presupuesto"]'))
        )
        context.driver.execute_script("arguments[0].click();", continue_button)
        print("The user clicked the 'Continue' button using JavaScript.")
        time.sleep(15)
    except Exception as e:
        raise Exception(f"Failed to click the continue button: {e}")