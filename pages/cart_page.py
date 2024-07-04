from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
value_price_product_in_catalog_text = None
from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


     # Locators

    word_cart = "//h1[@class='PageTitle_title__7XQYG']" # проверка слова в корзине
    name_product_in_cart = "//a[@title='Ноутбук Lenovo IdeaPad Slim 3 15IAH8 (83ER007QRK)']" # проверка наименования в корзине
    price_product_in_cart = "//span[@class='Price_price__m2aSe notranslate']" # проверка цены в корзине

     # Getters

    def get_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_cart)))

    def get_name_product_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_in_cart)))

    def get_price_product_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_in_cart)))

    #Methods

    def assert_word_cart(self, word_cart, expected_word):
        assert word_cart.text == expected_word, f"Expected {expected_word}, but got {word_cart.text}"

    def assert_name_product_in_cart(self, name_product_in_cart, expected_name):
        assert name_product_in_cart.text == expected_name, f"Expected {expected_name}, but got {name_product_in_cart.text}"

    def assert_price_product_in_cart(self, price_product_in_cart, expected_price):
        value_price_product_in_cart = price_product_in_cart.text.replace(' ', '').replace('₽', '').strip()
        print(f"Price from cart: {value_price_product_in_cart}")  # Отладочный вывод
        assert value_price_product_in_cart == expected_price, f"Expected {expected_price}, but got {value_price_product_in_cart}"

    def comparison_of_parameters_product(self, expected_price):
        self.get_current_url()
        self.assert_word_cart(self.get_word_cart(), 'Корзина')
        self.assert_name_product_in_cart(self.get_name_product_in_cart(), 'Ноутбук Lenovo IdeaPad Slim 3 15IAH8 (83ER007QRK)')
        self.assert_price_product_in_cart(self.get_price_product_in_cart(), expected_price)














