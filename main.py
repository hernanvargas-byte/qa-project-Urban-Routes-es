import data
import json
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common import WebDriverException


# --- Función de utilidad ---
def retrieve_phone_code(driver) -> str:
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            time.sleep(1)
            continue
        return code


class UrbanRoutesPage:
    # --- Localizadores ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_tariff_card = (By.XPATH, "//div[text()='Comfort']")

    phone_button = (By.CLASS_NAME, 'np-button')
    phone_input = (By.ID, 'phone')
    next_button_phone = (By.XPATH, "//button[text()='Siguiente']")
    confirmation_code_input = (By.ID, 'code')
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_input = (By.ID, 'number')
    card_cvv_input = (By.NAME, 'code')
    link_card_button = (By.XPATH, "//button[contains(., 'Agregar')]")
    close_payment_modal = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    comment_field = (By.ID, 'comment')
    blanket_switch = (By.CSS_SELECTOR, ".r-sw-container .slider")
    ice_cream_plus_button = (By.XPATH, "//div[text()='Helado']/..//div[@class='counter-plus']")

    final_order_button = (By.CLASS_NAME, 'smart-button')
    # Localizador relativo para esperar la info del conductor dentro del modal
    order_details_v2 = (By.XPATH, "//div[@class='order-body']//div[contains(text(), 'El conductor llegará')]")

    def __init__(self, driver):
        self.driver = driver

    # --- Métodos de interacción ---
    def set_route(self, from_addr, to_addr):
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def click_order_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.comfort_tariff_card)).click()

    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone_button).click()
        self.driver.find_element(*self.phone_input).send_keys(phone_number)
        self.driver.find_element(*self.next_button_phone).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.confirmation_code_input).send_keys(code)
        self.driver.find_element(*self.confirm_phone_button).click()

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_input).send_keys(card_number)
        self.driver.find_element(*self.card_cvv_input).send_keys(card_code)
        self.driver.find_element(*self.card_cvv_input).send_keys(Keys.TAB)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.link_card_button)).click()
        self.driver.find_element(*self.close_payment_modal).click()

    def set_comment(self, message):
        self.driver.find_element(*self.comment_field).send_keys(message)

    def toggle_blanket(self):
        self.driver.find_element(*self.blanket_switch).click()

    def add_ice_creams(self, count):
        for _ in range(count):
            self.driver.find_element(*self.ice_cream_plus_button).click()

    def click_final_order(self):
        self.driver.find_element(*self.final_order_button).click()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    def test_full_flow(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # 1. Configuración de ruta
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to
        time.sleep(2)

        # 2. Selección de tarifa Comfort
        routes_page.click_order_taxi()
        routes_page.select_comfort_tariff()
        time.sleep(2)

        # 3. Rellenar teléfono e interceptar código
        routes_page.set_phone(data.phone_number)
        code = retrieve_phone_code(self.driver)
        routes_page.set_confirmation_code(code)
        time.sleep(2)

        # 4. Agregar tarjeta de crédito
        routes_page.add_credit_card(data.card_number, data.card_code)
        time.sleep(2)

        # 5. Comentario y accesorios (Manta y Helados)
        routes_page.set_comment(data.message_for_driver)
        routes_page.toggle_blanket()
        routes_page.add_ice_creams(2)
        time.sleep(2)

        # 6. Finalizar pedido y esperar asignación de conductor
        routes_page.click_final_order()

        # Espera dinámica de hasta 60 segundos por la info del conductor
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(routes_page.order_details_v2)
        )

        # Pausa final de 3 segundos para observar los detalles antes de terminar
        time.sleep(3)

        # Verificación final
        assert self.driver.find_element(*routes_page.order_details_v2).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()