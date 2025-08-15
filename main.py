from selenium import webdriver
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()  # Apenas para manter o padrão do curso
        cls.driver.maximize_window()
        cls.page = UrbanRoutesPage(cls.driver)
        cls.base_url = "https://cnt-8e216dd7-f82d-4fc6-92bd-ac7a10111398.containerhub.tripleten-services.com?lng=pt"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_full_taxi_booking(self):
        # Abrir página
        self.driver.get(self.base_url)

        # Definir endereços
        self.page.enter_locations("Avenida Paulista", "Rua Augusta")

        # Selecionar Comfort
        self.page.select_comfort_plan()

        # Inserir telefone
        self.page.enter_phone("11999999999")
        code = retrieve_phone_code(self.driver)
        self.page.enter_sms_code(code)

        # Adicionar cartão
        self.page.add_credit_card("4111111111111111", "12/25", "123")

        # Escrever comentário
        self.page.add_comment("Por favor, toque uma música suave.")

        # Cobertor e lenços
        self.page.request_blanket_and_tissues()

        # Sorvetes
        self.page.order_ice_creams(2)

        # Solicitar táxi Comfort
        self.page.book_taxi()
