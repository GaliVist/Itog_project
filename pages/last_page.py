from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Last_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Methods

    def last(self):
        self.get_current_url()
        self.assert_url("https://www.regard.ru/cart")
        self.get_screenshot()





