from argparse import Action
from time import sleep
import allure
import pytest

from locators import Locators
from constants import Constants

from pages.scooter_page import ScooterPage

answer_dict = [
    {'question': Locators.ONE_QUESTION, 'answer': Locators.ONE_ANSWER, 'answer_text': Constants.ANSWER_ONE},
    {'question': Locators.TWO_QUESTION, 'answer': Locators.TWO_ANSWER, 'answer_text': Constants.ANSWER_TWO},
    {'question': Locators.THREE_QUESTION, 'answer': Locators.THREE_ANSWER, 'answer_text': Constants.ANSWER_THREE},
    {'question': Locators.FOUR_QUESTION, 'answer': Locators.FOUR_ANSWER, 'answer_text': Constants.ANSWER_FOUR},
    {'question': Locators.FIVE_QUESTION, 'answer': Locators.FIVE_ANSWER, 'answer_text': Constants.ANSWER_FIVE},
    {'question': Locators.SIX_QUESTION, 'answer': Locators.SIX_ANSWER, 'answer_text': Constants.ANSWER_SIX},
    {'question': Locators.SEVEN_QUESTION, 'answer': Locators.SEVEN_ANSWER, 'answer_text': Constants.ANSWER_SEVEN},
    {'question': Locators.EIGHT_QUESTION, 'answer': Locators.EIGHT_ANSWER, 'answer_text': Constants.ANSWER_EIGHT}
]

@allure.title('Проверка выпадающего списка') # декораторы
class TestDropdownList:
    @allure.title('Тест открытия выпадающего ответа при нажатии на вопрос')
    @pytest.mark.parametrize("data", answer_dict)# декораторы
    def test_first_question(self, driver, data):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site()
        scooter_page.close_cookie()
        scooter_page.click_one_question(data['question'])
        element = scooter_page.element_text(data['answer'])
        assert element == data['answer_text']
