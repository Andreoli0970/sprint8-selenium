from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    # Localizadores
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    COMFORT_BTN = (By.XPATH, "//button[contains(@class, 'comfort')]")
    PHONE_INPUT = (By.CLASS_NAME, "phone-input")
    CODE_INPUT = (By.ID, "code")
    ADD_CARD_BTN = (By.XPATH, "//button[contains(text(), 'Adicionar')]")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='Número do cartão']")
    CARD_DATE_INPUT = (By.XPATH, "//input[@placeholder='MM/AA']")
    CARD_CVV_INPUT = (By.XPATH, "//input[@placeholder='CVV']")
    COMMENT_INPUT = (By.XPATH, "//textarea[@placeholder='Comentário']")
    BLANKET_SWITCH = (By.XPATH, "//div[@class='switch blanket']")
    BLANKET_ACTIVE = (By.XPATH, "//div[@class='switch blanket active']")
    ICE_CREAM_PLUS_BTN = (By.XPATH, "//div[@class='counter ice-cream']//button[@class='plus']")
    BOOK_BTN = (By.XPATH, "//button[contains(text(), 'Reservar')]")
    
    # Métodos
    def enter_locations(self, from_addr, to_addr):
        self.driver.find_element(*self.FROM_INPUT).send_keys(from_addr)
        self.driver.find_element(*self.TO_INPUT).send_keys(to_addr)
        time.sleep(1)

    def select_comfort_plan(self):
        comfort = self.driver.find_element(*self.COMFORT_BTN)
        if "active" not in comfort.get_attribute("class"):
            comfort.click()
            time.sleep(0.5)

    def enter_phone(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def enter_sms_code(self, code):
        self.driver.find_element(*self.CODE_INPUT).send_keys(code)

    def add_credit_card(self, number, date, cvv):
        self.driver.find_element(*self.ADD_CARD_BTN).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CARD_DATE_INPUT).send_keys(date)
        cvv_field = self.driver.find_element(*self.CARD_CVV_INPUT)
        cvv_field.send_keys(cvv)
        cvv_field.send_keys(Keys.TAB)
        time.sleep(0.5)

    def add_comment(self, comment):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.BLANKET_SWITCH).click()

    def order_ice_creams(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_PLUS_BTN).click()
            time.sleep(0.3)

    def book_taxi(self):
        self.driver.find_element(*self.BOOK_BTN).click()
        time.sleep(2)
