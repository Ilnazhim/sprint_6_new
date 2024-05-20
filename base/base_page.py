from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        """Method open browser"""
        self.browser.get(url)
        self.url = url

    def find_element(self, locator, timeout=30):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return []

    def click_element(self, locator, timeout=30):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f"Failed to click on element with locator {locator}.")

    def enter_element(self, locator, text, timeout=30):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f"Failed to enter text in element with locator {locator}.")

    def get_current_url(self):
        """Method get current url"""
        return self.browser.current_url

    def assert_word(self, locator, result, timeout=30):
        """Method assert word"""
        value_word = self.find_element(locator, timeout).text
        value_result = result
        print(value_word)
        assert value_word == value_result

    def is_element_present(self, locator, timeout=30):
        """Method is element present"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.browser.current_url
        assert get_url == result
