# ☑️ En este archivo se ejecutan los tests ☑️
import pytest
import conftest
from utils.helpers import login_helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_01_login(driver):
    login_helper(driver)
    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"

def test_02_verificar_inventario(driver):
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text
    assert section_title == "Products" , f"ERROR: El título de la sección es incorrecto. Se esperaba 'Products' pero se obtuvo '{section_title}'"
    assert page_title == "Swag Labs" , f"ERROR: El título de la página es incorrecto. Se esperaba 'Swag Labs' pero se obtuvo '{page_title}'"

def test_03_productos_visibles(driver):
    inventory_item = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(inventory_item) > 0 , "ERROR: No se encontraron productos en el inventario"
    # ⚡En listas[],  len() se usa para ver el largo de una lista⚡

def test_04_validar_interfaz(driver):
    menu_button = driver.find_element(By.ID, 'reat-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    assert menu_button.is_displayed() , f"ERROR: El botón de menú no es visible"
    assert filtro.is_displayed() , f"ERROR: El filtro de productos no es visible"

def test_05_anadir_producto_al_carrito(driver):
    primer_item = driver.find_element(By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = primer_item.find_element(By.TAG_NAME, "button")
    boton_agregar.click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".inventory_item button"), "Remove"))
    boton_agregar = primer_item.find_element(By.TAG_NAME, "button") 
    assert boton_agregar.text == "Remove" , f"ERROR: El botón no cambió a 'REMOVE' después de agregar el producto al carrito"

def test_06_verificar_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_carrito.text == "1" , f"ERROR: El contador del carrito no muestra '1' después de agregar un producto. Se obtuvo '{contador_carrito.text}'"

def test_07_navegar_carrito(driver):
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()
    assert "/cart.html" in driver.current_url , "ERROR: No se redirigió a /cart.html"

def test_08_comprobar_producto_en_carrito(driver):
    producto_nombre_en_carrito = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert producto_nombre_en_carrito == "Sauce Labs Backpack" , f"ERROR: No es el mismo nombre"