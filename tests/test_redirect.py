import allure
from pages.main_page import MainPage
from src import urls


@allure.suite("Тесты с переходом по ссылкам в шапке")
class TestRedirect:

    @allure.title("Переход на главную страницу самоката при нажатии на лого Самокат")
    def test_go_to_main_page_from_logo(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на кнопку лого Самокат"):
            mp.click_logo_link_to_main_page()
        with allure.step("Открылась главная страница самоката"):
            mp.assert_url(urls.URL)

    @allure.title("Переход на главную страницу Дзен при нажатии на лого Яндекс")
    def test_go_to_yandex_from_logo(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на кнопку лого Яндекс"):
            mp.click_logo_link_to_yandex()
        with allure.step("Переход на новую вкладку"):
            mp.switch_to_new_window()
        with allure.step("Открылась страница яндекс Дзен"):
            mp.assert_url(urls.URL_DZEN)
