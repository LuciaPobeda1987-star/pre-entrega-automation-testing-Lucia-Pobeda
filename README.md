##Propósito del proyecto##

Este proyecto automatiza las pruebas funcionales de una aplicación web de e-commerce, con el fin de validar que sus flujos principales funcionen correctamente y detectar errores de forma rápida y repetible. Los tests, escritos en Python con pytest y Selenium WebDriver, verifican que un usuario pueda:

Iniciar sesión con credenciales válidas.
Acceder al catálogo de productos.
Seleccionar un producto y agregarlo al carrito.

Cada prueba informa su resultado (PASSED o FAILED) y, al finalizar la ejecución, se genera un reporte en HTML que permite revisar el estado de la aplicación de un vistazo.


#Tecnologías utilizadas"

Python: lenguaje de los tests.
pytest: framework para organizar y ejecutar las pruebas.
Selenium WebDriver: automatización del navegador.
pytest-html: generación del reporte HTML (si usás otro plugin, cambiá el nombre).
Visual Studio Code: entorno de desarrollo.

#Instrucciones de instalación de dependencias#

1° Debemos posicionarnos en la terminal.
2° Se instalan con el comando pip install
Pytest: pip install pytest
Selenium:pip install selenium 
Selenium webmanager:pip install selenium webdriver-manager
Reporte HTML: pip install pytest-html

#Comando para ejecutar las pruebas#

pytest -v --html=reporte.html
