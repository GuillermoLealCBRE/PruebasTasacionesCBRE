import driver_chrome

def before_all(context):
    """
    Inicializa el navegador antes de ejecutar cualquier escenario.
    """
    print("Initializing browser...")
    context.driver = driver_chrome.get_chrome_driver()

# def after_all(context):
    ##"""
    #Cierra el navegador después de ejecutar todos los escenarios.
    #"""
    # context.driver.quit()
    # print("Closing browser...")