from selenium.webdriver.common.by import By
from base.base_page import BasePage
from src import data, assertions



class OrderPage(BasePage):

    # Locators
    input_name = By.XPATH, "//input[@placeholder='* Имя']"
    input_surname = By.XPATH, "//input[@placeholder='* Фамилия']"
    input_address = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    open_list_metro_station = By.XPATH, "//input[@placeholder='* Станция метро']"
    select_metro_station = By.XPATH, "//li[@data-value='1']"
    input_phone = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    input_date_arrival = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    open_menu_time = By.XPATH, "//span[@class='Dropdown-arrow']"
    select_time_order = By.XPATH, "//div[text()='сутки']"
    black_color = By.XPATH, "//input[@id='black']"
    grey_color = By.XPATH, "//input[@id='grey']"
    input_comment = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    btn_next = By.XPATH, "//button[text()='Далее']"
    btn_make_order = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    btn_accept_order = By.XPATH, "//button[text()='Да']"
    success_order_text = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"

    def input_input_name(self, name):
        self.enter_element(self.input_name, name)

    def input_input_surname(self, surname):
        self.enter_element(self.input_surname, surname)

    def input_input_address(self, address):
        self.enter_element(self.input_address, address)

    def click_open_list_metro_station(self):
        self.click_element(self.open_list_metro_station)

    def click_select_metro_station(self):
        self.click_element(self.select_metro_station)

    def input_input_phone(self, phone):
        self.enter_element(self.input_phone, phone)

    def input_input_date_arrival(self, date_arrival):
        self.enter_element(self.input_date_arrival, date_arrival)

    def click_open_menu_time(self):
        self.click_element(self.open_menu_time)

    def click_select_time_order(self):
        self.click_element(self.select_time_order)

    def click_black_color(self):
        self.click_element(self.black_color)

    def click_grey_color(self):
        self.click_element(self.grey_color)

    def input_input_comment(self, comment):
        self.enter_element(self.input_comment, comment)

    def click_btn_next(self):
        self.click_element(self.btn_next)

    def click_btn_make_order(self):
        self.click_element(self.btn_make_order)

    def click_btn_accept_order(self):
        self.click_element(self.btn_accept_order)

    # Metods
    def fill_form_order_black_samocat(self, phone):
        self.input_input_name(data.name)
        self.input_input_surname(data.surname)
        self.input_input_address(data.address)
        self.click_open_list_metro_station()
        self.click_select_metro_station()
        self.input_input_phone(phone)
        self.click_btn_next()
        self.input_input_date_arrival(data.date_arrival)
        self.click_open_menu_time()
        self.click_select_time_order()
        self.click_black_color()
        self.input_input_comment(data.comment)
        self.click_btn_make_order()
        self.click_btn_accept_order()

    def fill_form_order_grey_samocat(self, phone):
        self.input_input_name(data.name)
        self.input_input_surname(data.surname)
        self.input_input_address(data.address)
        self.click_open_list_metro_station()
        self.click_select_metro_station()
        self.input_input_phone(phone)
        self.click_btn_next()
        self.input_input_date_arrival(data.date_arrival)
        self.click_open_menu_time()
        self.click_select_time_order()
        self.click_black_color()
        self.input_input_comment(data.comment)
        self.click_btn_make_order()
        self.click_btn_accept_order()

    def assert_success_order(self):
        self.assert_word(self.success_order_text, assertions.assert_success_order_text)
