import datetime

from selenium.webdriver.common.by import By


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def comparison_of_parameters_product(self, expected_price):
        price_product_in_cart = self.get_price_product_in_cart()
        self.assert_price_product_in_cart(price_product_in_cart, expected_price)

    def assert_price_product_in_cart(self, price_product_in_cart, expected_price):
        value_price_product_in_cart = price_product_in_cart.text.replace(' ', '').replace('₽', '').strip()
        print(f"Formatted price from cart: {value_price_product_in_cart}")  
        assert value_price_product_in_cart == expected_price, f"Expected {expected_price}, but got {value_price_product_in_cart}"

    def get_price_product_in_cart(self):
        price_element = self.driver.find_element(By.CSS_SELECTOR, '#__next > div > div > main > div > div.Grid_col__4bXWJ.Grid_col-8__Ak95g.Grid_col-laptop-7-10__dOZHB.Grid_col-tablet-12-12__wjImf > div:nth-child(2) > div > div > div.BasketItem_content__HDK_u > div.BasketItem_bottom__qPFa5 > div.BasketItem_price__7DNH8 > span > span > span')
        return price_element


    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Галина\\PycharmProjects\\itog_project\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")


