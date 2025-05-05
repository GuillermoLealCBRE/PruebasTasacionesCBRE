from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-logging")  # Deshabilitar algunos logs
    chrome_options.add_argument("--log-level=3")  # Solo errores críticos
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Excluir logs de ChromeDriver

    service = Service(r"C:\Users\GLeal\.wdm\drivers\chromedriver\win64\136.0.7103.49\chromedriver-win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver