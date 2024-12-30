import allure

from pages.base_page import BasePage
from locators import Locators


class OrderPage(BasePage):
    @allure.step('Ищем поле ввода имени и вводим имя')  # декоратор
    def text_field_name(self, name):
        self.find_element(locator=Locators.FIELD_NAME).send_keys(name)

    @allure.step('Ищем поле ввода фамилии и вводим фамилию')  # декоратор
    def text_field_last_name(self, last_name):
        self.find_element(locator=Locators.FIELD_LAST_NAME).send_keys(last_name)

    @allure.step('Ищем поле ввода адреса и вводим адрес')  # декоратор
    def text_field_address(self, address):
        self.find_element(locator=Locators.FIELD_ADDRESS).send_keys(address)

    @allure.step('Открываем выпадающий список')  # декоратор
    def click_field_metro(self):
        self.find_element(locator=Locators.FIELD_METRO).click()

    @allure.step('Выбрать станцию метро')  # декоратор
    def select_metro(self):
        self.find_element(locator=Locators.METRO_NAME_ONE).click()

    @allure.step('Вводим номер телефона')  # декоратор
    def text_phone_number(self, number):
        self.find_element(locator=Locators.FIELD_PHONE).send_keys(number)

    @allure.step('Нажимаем кнопку далее')  # декоратор
    def click_next_button(self):
        self.find_element(locator=Locators.BUTTON_NEXT).click()

    @allure.step('Вводим дату')  # декоратор
    def text_field_date(self, data):
        self.find_element(locator=Locators.FIELD_DATA).send_keys(data)

    @allure.step('Выбираем дату из календаря')  # декоратор
    def click_date(self):
        self.find_element(locator= Locators.CALENDAR_DATE).click()

    @allure.step('Нажимаем на поле срока аренды')  # декоратор
    def click_term(self):
        self.find_element(locator= Locators.FIELD_TERM).click()

    @allure.step('Выбираем 1 пункт из выпадающего списка')  # декоратор
    def select_term(self):
        self.find_element(locator=Locators.TERM_ONE_DAY).click()

    @allure.step('Нажимаем на кнопку Заказать')  # декоратор
    def click_order(self):
        self.find_element(locator=Locators.BUTTON_ORDER).click()

    @allure.step('Соглаашаемся заказать')  # декоратор
    def click_yes_button(self):
        self.find_element(locator=Locators.BUTTON_YES).click()

    @allure.step('Ищем текст удачного заказа')  # декоратор
    def success_order_text(self):
        success_text = self.find_element(locator=Locators.ORDER_TEXT_SUCCESS).text
        return success_text