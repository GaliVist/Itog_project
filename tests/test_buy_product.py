import time
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.last_page import Last_page
from pages.login_page import Login_page
from pages.main_page import Main_page

from pages.client_information_page import Client_information_page



def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Галина\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    driver = webdriver.Chrome(options=options, service=s)

    print("Start Test")


    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    # Получаем актуальную цену до добавления в корзину
    current_price = mp.get_current_price()
    print(f"Current price from site: {current_price}")

    cp = Cart_page(driver)
    cp.comparison_of_parameters_product(current_price)

    cip = Client_information_page(driver)
    cip.input_information()

    lp = Last_page(driver)
    lp.last()

    print("Finish Test 1")
    time.sleep(10)
    driver.quit()


