from argparse import Action

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from constants import Constants

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL_MAIN

    @allure.step('Открываем страницу Смоката')  # декоратор
    def go_to_site(self):
        self.driver.get(self.url)

    @allure.step('Ищем элемент на странице')  # декоратор
    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView()",locator)