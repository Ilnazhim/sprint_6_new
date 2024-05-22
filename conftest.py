import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture()
def browser():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
