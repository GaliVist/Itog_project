from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


     # Locators

    user_name = "//input[@id='userName']" # ввод фио
    user_phone = "//input[@id='userPhone']" # ввод номера телефона
    user_email = "//input[@id='userEmail']" # ввод почты
    list_items = "//div[@class='ReceiveWay_panelEl__SIdJt']" #выбор вкладки "показать списком" адреса доставок
    address_items = "(//button[@class='Button_button__GeQ2O Button_large__FQoDr Button_tertiary__zgkBi ReceiveWay_chooseBtn__HXJT_'])[1]" # выбор адреса доставки

     # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_phone)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_list_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.list_items)))

    def get_address_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_items)))


     # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_user_phone(self, user_phone):
        self.get_user_phone().send_keys(user_phone)
        print("Input user phone")

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Input user email")

    def click_list_items(self):
        self.get_list_items().click()
        print("Click list items")

    def click_address_items(self):
        self.get_address_items().click()
        print("Click address items")


    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_user_name("Кохова Мария Анатольевна")
        self.input_user_phone("9169663536")
        self.input_user_email("kochova@mail.ru")
        self.click_list_items()
        self.click_address_items()



