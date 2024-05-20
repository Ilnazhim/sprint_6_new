import allure
import pytest
from pages.main_page import MainPage
from src import urls


@allure.suite("Тесты по проверки текстов в блоке Вопросы о важном")
class TestQuestions:

    @pytest.mark.parametrize('question, answer, assert_answer', MainPage.list_question_answer_assert)
    @allure.title("Проверка текста в вопросах о важном")
    def test_check_important_question(self, browser, question, answer, assert_answer):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question(question)
        with allure.step("Сравнение ФР и ОР"):
            mp.assert_word(answer, assert_answer)
