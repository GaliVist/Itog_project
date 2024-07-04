import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

     # Locators

    catalog_button = "//div[@class='NavigationBar_burger__j7lZE']" # нажатие на кнопку "каталог"
    catalog_category = "(//div[@class='Catalog_mainCategoryName__xzGxz'])[4]" # переход в категорию "компьютеры и ноутбуки"
    category_laptop = "//a[@class='CardCategory_wrap__JQAjO']" # выбор вкладки "ноутбуки"
# выбор чек-боксов
    filters_сheckbox = "(//span[@class='Checkbox_fakeCheckbox__BrwB1 Checkbox_red__2iX1_ Checkbox_small___nCE3'])[3]"
    manufacturer_сheckbox = "(//label[@for='id-Lenovo-Lenovo'])[1]"
    ram_checkbox = "(//label[@for='id-16-3990'])[1]"
    current_price = "(//span[@class='Price_price__m2aSe notranslate'])[1]"
    select_product_1 = "(//button[@class='Button_button__GeQ2O Button_small___Zwz0 Button_secondary__qJMHg Button_withIcon__It4jn Button_inGridCard__qoqah CardButton_btn__eIZJQ CardButton_listing__w9MTw Card_buyButton__iJIAi'])[1]" # выбор продукта
    car = "//div[@class='IconButton_btn__eHnyM IconButton_cart__Na0hE']"  # нажатие на корзину
    go_to_cart = "//a[@class='Button_button__GeQ2O Button_large__FQoDr Button_primaryBlue__Y7daK Button_fullWidth__NgObg']" # переход в корзину


    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_catalog_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_category)))

    def get_category_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_laptop)))

    def get_filters_сheckbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters_сheckbox)))

    def get_manufacturer_сheckbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_сheckbox)))

    def get_ram_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_checkbox)))

    def get_current_price(self):
        # Локатор для получения цены товара на странице
        price_element = self.driver.find_element(By.CSS_SELECTOR, '#__next > div > div > main > div > div.Grid_col__4bXWJ.Grid_col-10__fA59y.Grid_col-laptop-8-10__na3OC.Grid_col-tablet-12-12__wjImf.Listing_sticky-boundary > div.rendererWrapper > div > div > div:nth-child(1) > div.Card_row__6_JG5 > div > div.Card_right__HE_E_ > div.CardPrice_wrap__BhoEB.CardPrice_listing__Bl1pC > div > span > span')
        current_price = price_element.text.replace(' ', '').replace('₽', '').strip()
        return current_price

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.car)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))


     # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_catalog_category(self):
        self.get_catalog_category().click()
        print("Click catalog category")

    def click_category_laptop(self):
        self.get_category_laptop().click()
        print("Click category laptop")

    def click_filters_сheckbox(self):
        self.get_filters_сheckbox().click()
        print("Click filters сheckbox")

    def click_manufacturer_сheckbox(self):
        self.get_manufacturer_сheckbox().click()
        print("Click manufacturer сheckbox")

    def click_ram_checkbox(self):
        self.get_ram_checkbox().click()
        print("Click ram checkbox")

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    def click_car(self):
        self.get_car().click()
        print("Click car")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click go to cart")


    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_catalog_category()
        self.click_category_laptop()
        self.click_filters_сheckbox()
        self.click_manufacturer_сheckbox()
        self.click_ram_checkbox()
        self.click_select_product()
        time.sleep(10)
        self.click_car()
        self.click_go_to_cart()






