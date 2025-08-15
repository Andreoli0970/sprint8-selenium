from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_route(self, address_from, address_to):
        from_field = self.wait.until(EC.element_to_be_clickable((By.ID, "from")))
        from_field.clear()
        from_field.send_keys(address_from)
        from_field.send_keys(Keys.RETURN)

        to_field = self.wait.until(EC.element_to_be_clickable((By.ID, "to")))
        to_field.clear()
        to_field.send_keys(address_to)
        to_field.send_keys(Keys.RETURN)

    def get_from(self):
        return self.driver.find_element(By.ID, "from").get_attribute("value")

    def get_to(self):
        return self.driver.find_element(By.ID, "to").get_attribute("value")

    def select_comfort_tariff(self):
        comfort_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Comfort')]")))
        comfort_button.click()

    def enter_phone_number(self, phone_number, code):
        phone_field = self.wait.until(EC.element_to_be_clickable((By.ID, "phone")))
        phone_field.clear()
        phone_field.send_keys(phone_number)

        code_field = self.wait.until(EC.element_to_be_clickable((By.ID, "code")))
        code_field.clear()
        code_field.send_keys(code)

    def add_credit_card(self, number, date, code):
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-card"))).click()
        number_field = self.wait.until(EC.element_to_be_clickable((By.ID, "number")))
        number_field.send_keys(number)
        date_field = self.driver.find_element(By.ID, "date")
        date_field.send_keys(date)
        code_field = self.driver.find_element(By.ID, "code")
        code_field.send_keys(code)
        code_field.send_keys(Keys.TAB)  # tira foco para ativar botão
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar')]").click()

    def set_driver_message(self, message):
        message_field = self.wait.until(EC.element_to_be_clickable((By.ID, "comment")))
        message_field.send_keys(message)

    def request_blanket_and_tissues(self):
        blanket_toggle = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='blanket-toggle']")))
        blanket_toggle.click()

    def add_ice_creams(self, quantity):
        for _ in range(quantity):
            ice_cream_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-ice-cream']")))
            ice_cream_button.click()