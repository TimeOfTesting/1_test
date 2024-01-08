import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://reqres.in/'

@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def setup_teardown(request, driver):
    driver.save_state = driver.get_window_rect()

    def teardown():
        driver.set_window_rect(**driver.save_state)

    request.addfinalizer(teardown)

