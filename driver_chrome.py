from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_chrome_driver():
    chrome_options = Options()
    
    # Configuración de opciones de Chrome
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-logging")  # Deshabilitar algunos logs
    chrome_options.add_argument("--log-level=3")  # Solo errores críticos
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Excluir logs de ChromeDriver

    # Ruta al ChromeDriver (asegúrate de que sea correcta)
    service = Service(r"C:\Users\GLeal\Downloads\chromedriver-win64\chromedriver.exe")
    
    # Redirigir la salida de errores estándar para evitar mensajes de USB
    service.log_path = os.devnull

    # Inicializar el driver con las opciones configuradas
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver