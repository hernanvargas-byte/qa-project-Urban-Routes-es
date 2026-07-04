# 🚖 Urban Routes - End-to-End Automation Testing Framework

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/test--framework-pytest-green.svg)](https://docs.pytest.org/)
[![Automation Tool](https://img.shields.io/badge/automation-selenium--webdriver-orange.svg)](https://www.selenium.dev/)

*Read this document in other languages: [Español (Spanish)](./README.es.md)*

---

## 📋 Project Description
This repository contains a robust, scalable **End-to-End (E2E) Automated Testing Suite** designed for the **Urban Routes** application. The suite covers the complete user journey of booking a taxi—starting from setting origin/destination addresses to final driver assignment confirmation. 

The primary goal is to validate seamless cross-module data integration, business logic constraints, and dynamic element synchronization across a complete E2E transactional workflow.

### 🧪 Automated Workflows Covered
* 📍 Configuring origin and destination addresses.
* 💳 Selecting distinct tariff options and managing dynamic payment method registration.
* 📱 Phone number authentication and parsing verification.
* 🍦 Adding customizable extra services (blankets, ice cream, etc.).
* ⏳ Handling multi-stage asynchronous processing (waiting for dynamic driver dispatch loops).

---

## 🛠️ Tech Stack & Engineering Techniques

* **Language:** `Python 3.12+`
* **Test Runner:** `Pytest`
* **Browser Automation:** `Selenium WebDriver`
* **Architectural Pattern:** **Page Object Model (POM)**. Designed with strict separation of concerns, decoupling structural UI locators and page-interaction methods (`UrbanRoutesPage`) from structural assertions.
* **Dynamic Explicit Waits:** Implemented `WebDriverWait` combined with `expected_conditions` to smoothly handle asynchronous UI state shifts, network latency, and dynamic modal overlays.
* **Log Ingestion Workflows:** Configured native browser logging capabilities (`goog:loggingPrefs`) to programmatically intercept performance logs and dynamically extract SMS confirmation tokens directly from the backend stream.

---

## 📐 Architecture & Repository Structure

```mermaid
graph TD
    A[data.py: Test Data & Environment Constants] --> B[main.py: UrbanRoutesPage - Locators & Interaction Logic]
    B --> C[main.py: TestUrbanRoutes - Pytest Test Suite Executions]
    C --> D[Local Execution / WebDriver Instance]
   ```
   
* 📦 `data.py`: Centralized repository for static test inputs, address parameters, specific formatting regex, and target URLs.
* 🛠️ `main.py`: Core logic containing Page Objects components, SMS parsing utility scripts, and final structural test cases (`TestUrbanRoutes`).
* 🛡️ `.gitignore`: Tailored configuration guarding against checking in telemetry tracking, local IDE files (`.idea`), and heavy workspace virtual environments (`.venv`).

---

## 🚀 Getting Started & Execution Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/hernanvargas-byte/qa-project-Urban-Routes-es.git](https://github.com/hernanvargas-byte/qa-project-Urban-Routes-es.git)
cd qa-project-Urban-Routes-es
```

### 2. Configure the Virtual Environment
```bash
python -m venv .venv

# On Windows (Git Bash / PowerShell):
source .venv/Scripts/activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install selenium pytest
```

### 4. Execute the Test Suite

To run all tests in the repository and output results via the console, execute:

```bash
pytest main.py -v
```
