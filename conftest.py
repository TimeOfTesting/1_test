import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
import pytest

url = 'https://reqres.in/'

@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--headless')
    geckodriver_path = os.path.abspath('geckodriver.exe')

    firefox_service = FirefoxService(executable_path=geckodriver_path)
    browser = webdriver.Firefox(service=firefox_service, options=options)
    browser.get(url)

    yield browser

    browser.execute_script("window.localStorage.clear();")
    browser.execute_script("window.sessionStorage.clear();")
    browser.quit()

@pytest.fixture(autouse=True)
def setup_teardown(request, driver):
    driver.save_state = driver.get_window_rect()

    def teardown():
        driver.set_window_rect(**driver.save_state)

    request.addfinalizer(teardown)

