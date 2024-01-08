import time
from selenium.common import TimeoutException
from locators import *
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_window(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_the_browser_to_load(self, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

    def get_value_from_url(self, url):
        url = url.split('/')
        number = url.pop()
        if '=' in number:
            number = number.split('=')
            number = number.pop()
        return number

class RequestPage(BasePage):

    def get_users(self):
        request_get_list_users = self.driver.find_element(*REQUESTFIELDS.USERS)
        self.scroll_window(request_get_list_users)
        request_get_list_users.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def single_user_by_id(self):
        request_single_user = self.driver.find_element(*REQUESTFIELDS.USERS_SINGLE)
        self.scroll_window(request_single_user)
        request_single_user.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def single_user_by_id_not_found(self):
        request_single_user_not_found = self.driver.find_element(*REQUESTFIELDS.USERS_SINGLE_NOT_FOUND)
        self.scroll_window(request_single_user_not_found)
        request_single_user_not_found.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def get_resource(self):
        request_resource = self.driver.find_element(*REQUESTFIELDS.UNKNOWN)
        self.scroll_window(request_resource)
        request_resource.click()

        self.wait_for_the_browser_to_load()
        request = self.driver.find_element(*HOME.REQUEST).text
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def get_resource_by_id(self):
        request_resource = self.driver.find_element(*REQUESTFIELDS.UNKNOWN_SINGLE)
        self.scroll_window(request_resource)
        request_resource.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def get_resource_by_id_not_found(self):
        request_resource = self.driver.find_element(*REQUESTFIELDS.UNKNOWN_SINGLE_NOT_FOUND)
        self.scroll_window(request_resource)
        request_resource.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text

    def create_user(self):
        request_create_user = self.driver.find_element(*REQUESTFIELDS.POST)
        self.scroll_window(request_create_user)
        request_create_user.click()

        self.wait_for_the_browser_to_load()
        request = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request]
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return data, response_status_int, response_body_text

    def update_user_put(self):
        request_update_user = self.driver.find_element(*REQUESTFIELDS.PUT)
        self.scroll_window(request_update_user)
        request_update_user.click()

        self.wait_for_the_browser_to_load()
        request_url = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request_url, data, response_status_int, response_body_text

    def update_user_patch(self):
        request_update_user = self.driver.find_element(*REQUESTFIELDS.PATCH)
        self.scroll_window(request_update_user)
        request_update_user.click()

        self.wait_for_the_browser_to_load()
        request_url = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request_url, data, response_status_int, response_body_text

    def delete_user(self):
        request_delete_user = self.driver.find_element(*REQUESTFIELDS.DELETE)
        self.scroll_window(request_delete_user)
        request_delete_user.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int

    def registration_user(self):
        request_registration_user = self.driver.find_element(*REQUESTFIELDS.REGISTER_SUCCESSFUL)
        self.scroll_window(request_registration_user)
        request_registration_user.click()

        self.wait_for_the_browser_to_load()
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]

        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return data, response_status_int, response_body_text

    def registration_user_unsuccessful(self):
        request_registration_user_unsuccessful = self.driver.find_element(*REQUESTFIELDS.REGISTER_UNSUCCESSFUL)
        self.scroll_window(request_registration_user_unsuccessful)
        request_registration_user_unsuccessful.click()

        self.wait_for_the_browser_to_load()
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]

        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return data, response_status_int, response_body_text

    def login_user(self):
        request_login_user = self.driver.find_element(*REQUESTFIELDS.LOGIN_SUCCESSFUL)
        self.scroll_window(request_login_user)
        request_login_user.click()

        self.wait_for_the_browser_to_load()
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]

        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return data, response_status_int, response_body_text

    def login_user_unsuccessful(self):
        request_login_user_unsuccessful = self.driver.find_element(*REQUESTFIELDS.LOGIN_UNSUCCESSFUL)
        self.scroll_window(request_login_user_unsuccessful)
        request_login_user_unsuccessful.click()

        self.wait_for_the_browser_to_load()
        request_data = self.driver.find_elements(*HOME.REQUEST_DATA)
        data = [i.text.strip('"') for i in request_data]

        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return data, response_status_int, response_body_text

    def delay_list_users(self):
        request_delay_list_users = self.driver.find_element(*REQUESTFIELDS.DELAY)
        self.scroll_window(request_delay_list_users)
        request_delay_list_users.click()

        self.wait_for_the_browser_to_load()
        request = self.get_value_from_url(self.driver.find_element(*HOME.REQUEST).text)
        response_body = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_BODY,)))
        response_body_text = json.loads(response_body.text)
        response_status = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.RESPONSE_STATUS,)))
        response_status_int = int(response_status.text)
        return request, response_status_int, response_body_text


class HomePage(BasePage):

    def click_heroku(self):
        heroku = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((*HOME.HEROKU,)))
        self.scroll_window(heroku)
        heroku.click()
        time.sleep(3)
        return self.driver.current_url

    def click_swagger(self):
        self.driver.back()
        swagger = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((*HOME.SWAGGER,)))
        self.scroll_window(swagger)
        swagger.click()
        time.sleep(3)
        return self.driver.current_url

    def click_support(self, value):
        self.driver.back()
        support = self.driver.find_element(*HOME.SUPPORT_REQUEST)
        self.scroll_window(support)
        support.click()

        self.wait_for_the_browser_to_load()
        field_payment = self.driver.find_element(*HOME.FIELD_PAYMENT)
        field_payment.clear()
        field_payment.send_keys(value)

        button_support = self.driver.find_element(*HOME.BUTTON_SUPPORT).click()
        time.sleep(3)

        sum_support = self.driver.find_element(*HOME.SUMM_SUPPORT).text.strip('$').split(',00')
        sum_support = int(sum_support[0])
        time.sleep(2)

        self.driver.back()
        return self.driver.current_url, sum_support

    def click_monthly_support(self):
        self.driver.back()
        self.wait_for_the_browser_to_load()

        monthly_support = self.driver.find_element(*HOME.MONTH_SUPPORT_PAY).click()
        button_support = self.driver.find_element(*HOME.BUTTON_SUPPORT).click()
        time.sleep(3)

        sum_support = self.driver.find_element(*HOME.SUMM_SUPPORT).text.strip('$').split(',00')
        sum_support = int(sum_support[0])
        time.sleep(2)

        self.driver.back()
        return self.driver.current_url, sum_support

    def subscribe(self, email):
        button_upgrate = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*SUBSCRIBE.BUTTON_UPGRATE,)))
        self.scroll_window(button_upgrate)
        button_upgrate.click()

        input_email = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*HOME.INPUT_EMAIL,)))
        input_email.clear()
        input_email.send_keys(email)

        button_subscribe_home_page = self.driver.find_element(*SUBSCRIBE.BUTTON_SUBSCRIBE_HOME_PAGE).click()
        time.sleep(3)

        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

        try:
            text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((*SUBSCRIBE.SUBSCRIPTION_CONFIRMATION_TEXT,))).text
        except TimeoutException:
            text = "Введено некорретное значение email"

        all_windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(all_windows[0])

        return self.driver.current_url, text





















