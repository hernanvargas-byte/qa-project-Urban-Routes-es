# 🚖 Urban Routes - Framework de Automatización de Pruebas End-to-End

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/test--framework-pytest-green.svg)](https://docs.pytest.org/)
[![Automation Tool](https://img.shields.io/badge/automation-selenium--webdriver-orange.svg)](https://www.selenium.dev/)

*Leer este document en otros idiomas: [English (Inglés)](./README.md)*

---

## 📋 Descripción del Proyecto
Este repositorio contiene una **Suite de Pruebas Automatizadas End-to-End (E2E)** robusta y escalable, diseñada para la aplicación **Urban Routes**. La suite cubre el flujo completo del usuario al reservar un taxi, desde la configuración de las direcciones de origen/destino hasta la confirmación final de la asignación del conductor.

El objetivo principal es validar la integración perfecta de datos entre módulos, las restricciones de la lógica de negocio y la sincronización dinámica de elementos a lo largo de un flujo transaccional E2E completo.

### 🧪 Flujos de Trabajo Automatizados Cubiertos
* 📍 Configuración de direcciones de origen y destino.
* 💳 Selección de distintas opciones de tarifas y gestión del registro dinámico de métodos de pago.
* 📱 Autenticación del número de teléfono y verificación del procesamiento del código.
* 🍦 Agregado de servicios adicionales personalizados (mantas, helados, etc.).
* ⏳ Manejo de procesamiento asincrónico multi-etapa (espera de los bucles dinámicos de despacho de conductores).

---

## 🛠️ Stack Tecnológico y Técnicas de Ingeniería

* **Lenguaje:** `Python 3.12+`
* **Ejecutor de Pruebas:** `Pytest`
* **Automatización del Navegador:** `Selenium WebDriver`
* **Patrón Arquitectónico:** **Page Object Model (POM)**. Diseñado con una estricta separación de responsabilidades, desacoplando los localizadores estructurales de la interfaz de usuario y los métodos de interacción de la página (`UrbanRoutesPage`) de las aserciones estructurales.
* **Esperas Explícitas Dinámicas:** Se implementó `WebDriverWait` combinado con `expected_conditions` para manejar de manera fluida los cambios asincrónicos de estado en la interfaz de usuario, la latencia de la red y las superposiciones de modales dinámicos.
* **Flujos de Ingesta de Logs:** Se configuraron las capacidades de registro nativas del navegador (`goog:loggingPrefs`) para interceptar programáticamente los logs de rendimiento y extraer de forma dinámica los tokens de confirmación SMS directamente desde el flujo del backend.
---

## 📐 Arquitectura y Estructura del Repositorio

```mermaid
graph TD
    A[data.py: Datos de Prueba y Constantes de Entorno] --> B[main.py: UrbanRoutesPage - Localizadores y Lógica de Interacción]
    B --> C[main.py: TestUrbanRoutes - Ejecuciones de la Suite de Pruebas Pytest]
    C --> D[Ejecución Local / Instancia de WebDriver]
   ```
   
* 📦 `data.py`: Repositorio centralizado para entradas de prueba estáticas, parámetros de dirección, expresiones regulares de formato específico y URLs de destino.
* 🛠️ `main.py`: Lógica central que contiene los componentes de Page Objects, scripts de utilidad para el procesamiento de SMS y los casos de prueba estructurales finales (`TestUrbanRoutes`).
* 🛡️ `.gitignore`: Configuración personalizada para evitar la inclusión de rastreos de telemetría, archivos locales del IDE (`.idea`) y entornos virtuales pesados de trabajo (`.venv`).

---

## 🚀 Primeros Pasos e Instrucciones de Ejecución

### 1. Clonar el Repositorio
```bash
git clone [https://github.com/hernanvargas-byte/qa-project-Urban-Routes-es.git](https://github.com/hernanvargas-byte/qa-project-Urban-Routes-es.git)
cd qa-project-Urban-Routes-es
```

### 2. Configurar el Entorno Virtual
```bash
python -m venv .venv

# En Windows (Git Bash / PowerShell):
source .venv/Scripts/activate

# En macOS/Linux:
source .venv/bin/activate
```

### 3. Instalar las Dependencias Requeridas
```bash
pip install selenium pytest
```

### 4. Ejecutar la Suite de Pruebas
Para ejecutar todas las pruebas en el repositorio y mostrar los resultados a través de la consola, ejecutá:

```bash
pytest main.py -v
```
