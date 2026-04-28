# Proyecto Urban Routes - Automatización de Pruebas (QA)

## Descripción del Proyecto
Este proyecto consiste en una suite de pruebas automatizadas para la aplicación **Urban Routes**. La automatización cubre el flujo completo de reservación de un taxi, desde la configuración de las direcciones de origen y destino hasta la confirmación de un conductor asignado, pasando por la selección de tarifas, registro de teléfono, métodos de pago y selección de servicios adicionales (manta, helados, etc.).

El objetivo principal es validar que la integración de los diferentes módulos de la aplicación funcione correctamente en un entorno de pruebas extremo a extremo (E2E).

## Tecnologías y Técnicas Utilizadas
Para este proyecto se implementaron las siguientes herramientas y patrones de diseño:

* **Lenguaje:** Python 3.x
* **Framework de Pruebas:** Pytest
* **Automatización de Navegador:** Selenium WebDriver
* **Patrón de Diseño:** **POM (Page Object Model)**. Se separó la lógica de los localizadores y métodos de interacción en la clase `UrbanRoutesPage` para mejorar la mantenibilidad del código.
* **Esperas Dinámicas:** Uso de `WebDriverWait` y `expected_conditions` para manejar la latencia de la red y elementos asíncronos (como la recepción del código SMS y la asignación del conductor).
* **Configuración de Logs:** Uso de `goog:loggingPrefs` para interceptar registros de rendimiento y recuperar códigos de confirmación dinámicos.

## Estructura del Repositorio
* `data.py`: Contiene las constantes y datos de prueba (URLs, direcciones, números de teléfono, etc.).
* `main.py`: Contiene la lógica de los Page Objects (clase `UrbanRoutesPage`), la función de utilidad para el código SMS y la clase de pruebas `TestUrbanRoutes`.
* `.gitignore`: Configurado para evitar subir archivos de entorno virtual (`.venv`) y configuraciones locales de IDE (`.idea`).

## Instrucciones para Ejecutar las Pruebas

1.  **Clonar el repositorio:**
    ```bash
    git clone [URL_DE_TU_REPOSITORIO]
    cd qa-project-Urban-Routes-es
    ```

2.  **Configurar el entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    source venv/Scripts/activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    Asegúrate de tener instaladas las librerías necesarias:
    ```bash
    pip install selenium pytest
    ```

4.  **Ejecutar los tests:**
    Desde la terminal en la raíz del proyecto, ejecuta:
    ```bash
    pytest main.py
    ```