from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = 'https://www.regard.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

     # Locators

    private_office = "(//span[@class='IconButton_text__B2OHa'])[1]" #нажатие на кнопку "кабинет"
    user_name = "//input[@name='login']" #ввод логина
    password = "//input[@name='password']" # ввод пароля
    button_login = "//button[@class='Button_button__GeQ2O Button_large__FQoDr Button_primaryBlue__Y7daK Auth_btnEnter__yG8s2']" #нажатие кнопки "войти"
    main_word = "(//h2[@class='PageTitle_title__7XQYG'])[1]" #слово на главной странице


     # Getters

    def get_private_office(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.private_office)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

     # Actions

    def click_private_office(self):
        self.get_private_office().click()
        print("Click private office")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click button login")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_private_office()
        self.input_user_name("wacotes690@nolanzip.com")
        self.input_password("27.06Test2024")
        self.click_button_login()
        self.assert_word(self.get_main_word(), 'Полезные страницы')



