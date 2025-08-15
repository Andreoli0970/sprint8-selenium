import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(5)

    def test_full_taxi_order(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO

        page.select_comfort_tariff()

        code = retrieve_phone_code(self.driver)
        page.enter_phone_number(data.PHONE_NUMBER, code)

        page.add_credit_card(data.CARD_NUMBER, data.CARD_DATE, data.CARD_CODE)

        page.set_driver_message(data.MESSAGE_FOR_DRIVER)
        page.request_blanket_and_tissues()
        page.add_ice_creams(2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()