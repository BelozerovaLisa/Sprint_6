from time import sleep

import allure
import pytest
from locators import Locators
from constants import Constants

from pages.scooter_page import ScooterPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.title('Позитивный сценарий с 2 параметрами') # декораторы
    @pytest.mark.parametrize('button_order, name, last_name, address, phone, date',
                             [[Locators.BUTTON_ORDER_UP, "Иван", "Толстой", "Карла Маркса д.1", "88005553535","01.01.2020"],
                             [Locators.BUTTON_ORDER_DOWN, "Маша", "Достоевская", "Карла Маркса д.2", "+7005553535","01.01.2024"]])
    def test_positive_case(self, driver, button_order, name, last_name, address, phone, date):
        scooter_page = ScooterPage(driver)
        order_page = OrderPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_button_order(button_order)
        order_page.text_field_name(name)
        order_page.text_field_last_name(last_name)
        order_page.text_field_address(address)
        order_page.click_field_metro()
        order_page.select_metro()
        order_page.text_phone_number(phone)
        order_page.click_next_button()
        order_page.text_field_date(date)
        order_page.click_date()
        order_page.click_term()
        order_page.select_term()
        order_page.click_order()
        order_page.click_yes_button()
        assert order_page.success_order_text() == Constants.SUCCESS_TEXT_BUTTON

    @allure.title('Переход на сайт ДЗЕНа при нажатии на лого Яндекса')  # декораторы
    def test_button_yandex(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.click_button_ya()
        sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == Constants.URL_DZEN

    @allure.title('Переход на сайт Самоката при нажатии на лого "Самокат"')  # декораторы
    def test_button_logo(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.click_button_order(Locators.BUTTON_ORDER_UP)
        scooter_page.click_button_logo()
        assert driver.current_url == Constants.URL_MAIN