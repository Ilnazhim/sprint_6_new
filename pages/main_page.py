from selenium.webdriver.common.by import By
from base.base_page import BasePage
from src import assertions


class MainPage(BasePage):

    # Locators
    accept_cookies = By.XPATH, "//button[@id='rcc-confirm-button']"
    logo_link_to_main_page = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    logo_link_to_yandex = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"

    important_question_1 = By.XPATH, "//div[@id='accordion__heading-0']"
    important_question_2 = By.XPATH, "//div[@id='accordion__heading-1']"
    important_question_3 = By.XPATH, "//div[@id='accordion__heading-2']"
    important_question_4 = By.XPATH, "//div[@id='accordion__heading-3']"
    important_question_5 = By.XPATH, "//div[@id='accordion__heading-4']"
    important_question_6 = By.XPATH, "//div[@id='accordion__heading-5']"
    important_question_7 = By.XPATH, "//div[@id='accordion__heading-6']"
    important_question_8 = By.XPATH, "//div[@id='accordion__heading-7']"

    important_answer_1 = By.XPATH, "//div[@id='accordion__panel-0']//p"
    important_answer_2 = By.XPATH, "//div[@id='accordion__panel-1']//p"
    important_answer_3 = By.XPATH, "//div[@id='accordion__panel-2']//p"
    important_answer_4 = By.XPATH, "//div[@id='accordion__panel-3']//p"
    important_answer_5 = By.XPATH, "//div[@id='accordion__panel-4']//p"
    important_answer_6 = By.XPATH, "//div[@id='accordion__panel-5']//p"
    important_answer_7 = By.XPATH, "//div[@id='accordion__panel-6']//p"
    important_answer_8 = By.XPATH, "//div[@id='accordion__panel-7']//p"

    btn_header_order = By.XPATH, "//button[@class='Button_Button__ra12g']"
    btn_footer_order = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"

    list_question_answer_assert = [[important_question_1, important_answer_1, assertions.assert_important_answer_1],
                                   [important_question_2, important_answer_2, assertions.assert_important_answer_2],
                                   [important_question_3, important_answer_3, assertions.assert_important_answer_3],
                                   [important_question_4, important_answer_4, assertions.assert_important_answer_4],
                                   [important_question_5, important_answer_5, assertions.assert_important_answer_5],
                                   [important_question_6, important_answer_6, assertions.assert_important_answer_6],
                                   [important_question_7, important_answer_7, assertions.assert_important_answer_7],
                                   [important_question_8, important_answer_8, assertions.assert_important_answer_8]]

    def click_accept_cookies(self):
        self.click_element(self.accept_cookies)

    def click_logo_link_to_main_page(self):
        self.click_element(self.logo_link_to_yandex)

    def click_logo_link_to_yandex(self):
        self.click_element(self.logo_link_to_yandex)

    def click_important_question(self, question):
        self.click_element(question)

    def click_btn_header_order(self):
        self.click_element(self.btn_header_order)

    def click_btn_footer_order(self):
        self.click_element(self.btn_footer_order)

    def switch_to_new_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
