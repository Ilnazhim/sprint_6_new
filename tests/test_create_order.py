import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from src import data, urls


@allure.suite("Тесты с созданием заказа")
class TestOrders:

    @pytest.mark.parametrize('phone', data.phone)
    @allure.title("Создание заказа из кнопки вверху страницы с черным самокатом")
    def test_make_order_up_button_black_samocat(self, browser, phone):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            op = OrderPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на кнопку Заказать в хедере страницы"):
            mp.click_btn_header_order()
        with allure.step("Заполнение формы заказа и заказ товара"):
            op.fill_form_order_black_samocat(phone)
        with allure.step("Сравнение ФР и ОР"):
            op.assert_success_order()

    @pytest.mark.parametrize('phone', data.phone)
    @allure.title("Создание заказа из кнопки снизу страницы с серым самокатом")
    def test_make_order_down_button_grey_samocat(self, browser, phone):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            op = OrderPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на кнопку Заказать внизу страницы"):
            mp.click_btn_footer_order()
        with allure.step("Заполнение формы заказа и заказ товара"):
            op.fill_form_order_grey_samocat(phone)
        with allure.step("Сравнение ФР и ОР"):
            op.assert_success_order()
