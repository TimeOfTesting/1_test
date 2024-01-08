import pytest
from main_page_UI import *
from main_page_API import *
from conftest import *

class TestSuiteUI:

    @pytest.mark.positive
    def test_1(self, driver):
        """Получение списка пользователей, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.get_users()
        api_result = UserPage()
        assert response_status == api_result.get_list_users(request).status_code
        assert response_body == api_result.get_list_users(request).json()

    @pytest.mark.positive
    def test_2(self, driver):
        """Получение пользователя по его id, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.single_user_by_id()
        api_result = UserPage()
        assert response_status == api_result.get_user_by_id(request).status_code
        assert response_body == api_result.get_user_by_id(request).json()

    @pytest.mark.negative
    def test_3(self, driver):
        """Получение пользователя по его id, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.single_user_by_id_not_found()
        api_result = UserPage()
        assert response_status == api_result.get_user_by_id(request).status_code
        assert response_body == api_result.get_user_by_id(request).json()

    @pytest.mark.positive
    def test_4(self, driver):
        """Получение списка ресурсов, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.get_resource()
        api_result = ResourcePage()
        assert response_status == api_result.get_list_resource().status_code
        assert response_body == api_result.get_list_resource().json()

    @pytest.mark.positive
    def test_5(self, driver):
        """Получение ресурса по id, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.get_resource_by_id()
        api_result = ResourcePage()
        assert response_status == api_result.get_single_resource(request).status_code
        assert response_body == api_result.get_single_resource(request).json()

    @pytest.mark.negative
    def test_6(self, driver):
        """Получение ресурса по id, проверка результата UI с API - негативный тест"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.get_resource_by_id()
        api_result = ResourcePage()
        assert response_status == api_result.get_single_resource(request).status_code
        assert response_body == api_result.get_single_resource(request).json()

    @pytest.mark.positive
    def test_7(self, driver):
        """Создание пользователя, проверка результата UI с API"""
        request_page = RequestPage(driver)
        data, response_status, response_body = request_page.create_user()
        api_result = UserPage()
        assert response_status == api_result.create_user(*data).status_code
        assert response_body['name'] == api_result.create_user(*data).json()['name']
        assert response_body['job'] == api_result.create_user(*data).json()['job']

    @pytest.mark.positive
    def test_8(self, driver):
        """Изменение данных пользователя, проверка результата UI с API (PUT - запрос)"""
        request_page = RequestPage(driver)
        request_url, request_data, response_status, response_body = request_page.update_user_put()
        api_result = UserPage()
        assert response_status == api_result.update_user_put(request_url, *request_data).status_code

    @pytest.mark.positive
    def test_9(self, driver):
        """Изменение данных пользователя, проверка результата UI с API (PATCH - запрос)"""
        request_page = RequestPage(driver)
        request_url, request_data, response_status, response_body = request_page.update_user_patch()
        api_result = UserPage()
        assert response_status == api_result.update_user_patch(request_url, *request_data).status_code
        assert response_body['name'] == api_result.update_user_patch(request_url, *request_data).json()['name']
        assert response_body['job'] == api_result.update_user_patch(request_url, *request_data).json()['job']

    @pytest.mark.positive
    def test_10(self, driver):
        """Удаление пользователя, проверка результата UI с API (PUT - запрос)"""
        request_page = RequestPage(driver)
        request, response_status = request_page.delete_user()
        api_result = UserPage()
        assert response_status == api_result.delete_user(request).status_code

    @pytest.mark.positive
    def test_11(self, driver):
        """Регистрация нового пользователя, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request_data, response_status, response_body = request_page.registration_user()
        api_result = UserPage()
        assert response_status == api_result.registration_user(*request_data).status_code
        assert response_body['token'] == api_result.registration_user(*request_data).json()['token']

    @pytest.mark.negative
    def test_12(self, driver):
        """Регистрация нового пользователя, проверка результата UI с API - негативный тест"""
        request_page = RequestPage(driver)
        request_data, response_status, response_body = request_page.registration_user_unsuccessful()
        api_result = UserPage()
        assert response_status == api_result.registration_user(*request_data).status_code
        assert response_body == api_result.registration_user(*request_data).json()

    @pytest.mark.positive
    def test_13(self, driver):
        """Аутентификация пользователя, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request_data, response_status, response_body = request_page.login_user()
        api_result = UserPage()
        assert response_status == api_result.get_token_user(*request_data).status_code
        assert response_body['token'] == api_result.get_token_user(*request_data).json()['token']

    @pytest.mark.negative
    def test_14(self, driver):
        """Аутентификация пользователя, проверка результата UI с API - негативный тест"""
        request_page = RequestPage(driver)
        request_data, response_status, response_body = request_page.login_user_unsuccessful()
        api_result = UserPage()
        assert response_status == api_result.get_token_user(*request_data).status_code
        assert response_body == api_result.get_token_user(*request_data).json()

    @pytest.mark.positive
    def test_15(self, driver):
        """Список пользователей, проверка результата UI с API"""
        request_page = RequestPage(driver)
        request, response_status, response_body = request_page.delay_list_users()
        api_result = UserPage()
        assert response_status == api_result.delayed_responce_list_users(request).status_code
        assert response_body == api_result.delayed_responce_list_users(request).json()

    @pytest.mark.positive
    def test_click_heroku(self, driver):
        """Переход по ссылке на главную страницу сайта Heroku"""
        home_page = HomePage(driver)
        current_url = home_page.click_heroku()
        expected_url = 'https://www.heroku.com/'
        assert expected_url == current_url

    @pytest.mark.positive
    def test_click_swagger(self, driver):
        """Переход по страницу документации API"""
        home_page = HomePage(driver)
        current_url = home_page.click_swagger()
        expected_url = 'https://reqres.in/api-docs/'
        assert expected_url == current_url

    @pytest.mark.positive
    @pytest.mark.parametrize('value', [100], ids=['correct value'])
    def test_support_payment(self, driver, value):
        """Поддержка API"""
        home_page = HomePage(driver)
        current_url, sum_support = home_page.click_support(value)
        expected_url = 'https://checkout.stripe.com/c/pay/'
        assert expected_url in current_url
        assert value == sum_support

    @pytest.mark.xfail(reason='Баг, при вводе нулевого и отрицательного значения, осуществляется переход на оплату указывается значение по умолчанию - 15$')
    @pytest.mark.parametrize('value', [-100, 0], ids=['incorrect value', 'incorrect value'])
    def test_support_payment_negative(self, driver, value):
        """Поддержка API - негативный тест"""
        home_page = HomePage(driver)
        current_url, sum_support = home_page.click_support(value)
        expected_url = 'https://checkout.stripe.com/c/pay/'
        assert expected_url in current_url
        assert value != sum_support

    @pytest.mark.positive
    def test_monthly_support_payment(self, driver):
        """Поддержка API - оформление ежемесячной оплаты"""
        home_page = HomePage(driver)
        current_url, sum_support = home_page.click_monthly_support()
        expected_url = 'https://checkout.stripe.com/c/pay/'
        assert expected_url in current_url
        assert 5 == sum_support

    @pytest.mark.positive
    @pytest.mark.parametrize('email', ['test1234@mail.com'], ids=['correct email'])
    def test_subscribe_email(self, driver, email):
        home_page = HomePage(driver)
        current_url, text = home_page.subscribe(email)
        assert 'Subscription Confirmed' in text or 'Almost finished' in text




