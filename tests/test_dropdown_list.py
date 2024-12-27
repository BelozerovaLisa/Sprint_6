from argparse import Action
from time import sleep
import allure
from locators import Locators
from constants import Constants

from pages.scooter_page import ScooterPage

@allure.title('Проверка выпадающего списка') # декораторы
class TestDropdownList:
    @allure.title('Тест открытия выпадающего ответа при нажатии на первый вопрос')  # декораторы
    def test_first_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.ONE_QUESTION)
        element = scooter_page.element_text(Locators.ONE_ANSWER)
        assert element == Constants.ANSWER_ONE

    @allure.title('Тест открытия выпадающего ответа при нажатии на второй вопрос')  # декораторы
    def test_second_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.TWO_QUESTION)
        element = scooter_page.element_text(Locators.TWO_ANSWER)
        assert element == Constants.ANSWER_TWO

    @allure.title('Тест открытия выпадающего ответа при нажатии на третий вопрос')  # декораторы
    def test_third_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.THREE_QUESTION)
        element = scooter_page.element_text(Locators.THREE_ANSWER)
        assert element == Constants.ANSWER_THREE

    @allure.title('Тест открытия выпадающего ответа при нажатии на четвертый вопрос')  # декораторы
    def test_fourth_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.FOUR_QUESTION)
        element = scooter_page.element_text(Locators.FOUR_ANSWER)
        assert element == Constants.ANSWER_FOUR

    @allure.title('Тест открытия выпадающего ответа при нажатии на пятый вопрос')  # декораторы
    def test_fifth_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.FIVE_QUESTION)
        element = scooter_page.element_text(Locators.FIVE_ANSWER)
        assert element == Constants.ANSWER_FIVE

    @allure.title('Тест открытия выпадающего ответа при нажатии на шестой вопрос')  # декораторы
    def test_sixth_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.SIX_QUESTION)
        element = scooter_page.element_text(Locators.SIX_ANSWER)
        assert element == Constants.ANSWER_SIX

    @allure.title('Тест открытия выпадающего ответа при нажатии на седьмой вопрос')  # декораторы
    def test_seventh_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.SEVEN_QUESTION)
        element = scooter_page.element_text(Locators.SEVEN_ANSWER)
        assert element == Constants.ANSWER_SEVEN

    @allure.title('Тест открытия выпадающего ответа при нажатии на восьмой вопрос')  # декораторы
    def test_eighth_question(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(Locators.EIGHT_QUESTION)
        element = scooter_page.element_text(Locators.EIGHT_ANSWER)
        assert element == Constants.ANSWER_EIGHT