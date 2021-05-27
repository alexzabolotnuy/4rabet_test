import pytest
from selenium import webdriver

browser = webdriver.Chrome()


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser...")
    browser.quit()
