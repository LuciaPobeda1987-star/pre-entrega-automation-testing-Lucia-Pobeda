# ☑️ En este archivo, configuramos el llamado del navegador para los tests ☑️
import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium .webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--lang=es") 
    driver = webdriver.Chrome(service=service, options=options )
    driver.implicitly_wait(10)  # 👽 Espera implícita de 10 segundos👽
    yield driver # 👽 Da los instrumentos del navegador al test 👽
    driver.quit()