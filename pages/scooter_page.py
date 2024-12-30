import allure

from pages.base_page import BasePage
from locators import Locators


class ScooterPage(BasePage):
    @allure.step('Закрываем куки')  # декоратор
    def close_cookie(self):
        self.find_element(locator= Locators.COOKIE_BUTTON).click()

    def find_last_question(self):
        self.find_element(locator=Locators.EIGHT_QUESTION)

    @allure.step('Кликаем на вопрос')  # декоратор
    def click_one_question(self, locator_param):
        click_question = self.find_element(locator= locator_param)
        click_question.click()

    @allure.step('Ищем текст')  # декоратор
    def element_text(self, locator_param):
        question_text = self.find_element(locator= locator_param).text
        return question_text

    @allure.step('Нажимаем на кнопку Заказать')  # декоратор
    def click_button_order(self, button_order):
        self.find_element(locator=button_order).click()

    @allure.step('Нажимаем на логотип Самоката')  # декоратор
    def click_button_logo(self):
        self.find_element(locator=Locators.BUTTON_LOGO).click()

    @allure.step('Нажимаем на логолтип Яндекса')  # декоратор
    def click_button_ya(self):
        self.find_element(locator=Locators.BUTTON_YA).click()



