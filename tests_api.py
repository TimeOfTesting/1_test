from main_page_API import *
import pytest

class TestSuiteAPI:

    @pytest.mark.positive
    @pytest.mark.parametrize('page', [2], ids=['correct page'])
    def test_1(self, page):
        """Получение списка пользователей"""
        user_page = UserPage()
        users = user_page.get_list_users(page)
        key_body_response = ['page', 'per_page', 'total', 'total_pages', 'data']
        assert users.status_code == 200
        assert users.json()['page'] == page
        for name in key_body_response:
            assert name in users.json()

    @pytest.mark.positive
    @pytest.mark.parametrize('id', [2], ids=['correct id'])
    def test_2(self, id):
        """Получение данных пользователя по его id"""
        user_page = UserPage()
        user = user_page.get_user_by_id(id)
        key_body_response = ['data', 'support']
        assert user.status_code == 200
        assert user.json()['data']['id'] == id
        for name in key_body_response:
            assert name in user.json()

    @pytest.mark.negative
    @pytest.mark.parametrize('id', [23, ' ', '!@fhn'], ids=['incorrect id', 'empty value', 'incorrect id'])
    def test_3(self, id):
        """Получение данных пользователя по его id - негативный тест"""
        user_page = UserPage()
        user = user_page.get_user_by_id(id)
        assert user.status_code == 404
        assert user.json() == {}

    @pytest.mark.positive
    def test_4(self):
        """Получение списка ресурсов"""
        resource_page = ResourcePage()
        list_resource = resource_page.get_list_resource()
        key_body_response = ['page', 'per_page', 'total', 'total_pages', 'data']
        assert list_resource.status_code == 200
        for name_key in key_body_response:
            assert name_key in list_resource.json()

    @pytest.mark.positive
    @pytest.mark.parametrize('id', [2], ids=['correct id'])
    def test_5(self, id):
        """Получение ресурса по id"""
        resource_page = ResourcePage()
        get_resource = resource_page.get_single_resource(id)
        key_body_response = ['data', 'support']
        assert get_resource.status_code == 200
        assert get_resource.json()['data']['id'] == id
        for name_key in key_body_response:
            assert name_key in get_resource.json()

    @pytest.mark.negative
    @pytest.mark.parametrize('id', ['aaaa12!@_', '23', ' '], ids=['incorrect id', 'incorrect id', 'empty value'])
    def test_6(self, id):
        """Получение ресурса по id - негативный тест"""
        resource_page = ResourcePage()
        get_resource = resource_page.get_single_resource(id)
        assert get_resource.status_code == 404
        assert get_resource.json() == {}

    @pytest.mark.positive
    @pytest.mark.parametrize('name, job', [('morpheus', 'leader')], ids=['correct name and job'])
    def test_7(self, name, job):
        """Создание пользователя"""
        user_page = UserPage()
        create_user = user_page.create_user(name, job)
        key_body_response = ['name', 'job', 'id', 'createdAt']
        assert create_user.status_code == 201
        for name_key in key_body_response:
            assert name_key in create_user.json()

    @pytest.mark.positive
    @pytest.mark.xfail(reason='Баг, запрос приходит без данных name, job')
    @pytest.mark.parametrize('user_id, name, job', [(2, 'morpheus', 'zion resident')], ids=['correct user_id, name and job'])
    def test_8(self, user_id, name, job):
        """Обновление информации о пользователе по его id (PUT-запрос)"""
        user_page = UserPage()
        update_user = user_page.update_user_put(user_id, name, job)
        key_body_not_in_response = ['name', 'job']
        print(update_user.json())
        assert update_user.status_code == 200
        assert 'updatedAt' in update_user.json()
        for name_key in key_body_not_in_response:
            assert name_key not in update_user.json()

    @pytest.mark.positive
    @pytest.mark.parametrize('user_id, name, job', [(2, 'morpheus', 'zion resident')], ids=['correct user_id, name and job'])
    def test_9(self, user_id, name, job):
        """Обновление информации о пользователе по его id (PATCH - запрос)"""
        user_page = UserPage()
        update_user = user_page.update_user_patch(user_id, name, job)
        key_body_response = ['name', 'job', 'updatedAt']
        assert update_user.status_code == 200
        for name in key_body_response:
            assert name in update_user.json()

    @pytest.mark.positive
    @pytest.mark.parametrize('user_id', [2], ids=['correct user_id'])
    def test_10(self, user_id):
        """Удаление пользователя"""
        user_page = UserPage()
        delete_user = user_page.delete_user(user_id)
        assert delete_user.status_code == 204

    @pytest.mark.positive
    @pytest.mark.parametrize('user_name, password', [('eve.holt@reqres.in', 'pistol')], ids=['correct name and password'])
    def test_11(self, user_name, password):
        """Регистрация нового пользователя"""
        user_page = UserPage()
        registration = user_page.registration_user(user_name, password)
        key_body_response = ['id', 'token']
        assert registration.status_code == 200
        for name_key in key_body_response:
            assert name_key in registration.json()

    @pytest.mark.negative
    @pytest.mark.parametrize('user_name', [('sydney@fife')], ids=['incorrect name,empty password'])
    def test_12(self, user_name):
        """Регистрация нового пользователя - негативный тест"""
        user_page = UserPage()
        registration = user_page.registration_user(user_name)
        error = {'error': 'Missing password'}
        assert registration.status_code == 400
        assert registration.json() == error

    @pytest.mark.positive
    @pytest.mark.parametrize('user_name, password', [('eve.holt@reqres.in', 'cityslicka')], ids=['correct name and password'])
    def test_13(self, user_name, password):
        """Аутентификация пользователя"""
        user_page = UserPage()
        token = user_page.get_token_user(user_name, password)
        assert token.status_code == 200
        assert 'token' in token.json()

    @pytest.mark.negative
    @pytest.mark.parametrize('user_name', [('peter@klaven'), ('340'), (' ')],
                             ids=['correct name', 'incorrect name', 'empty name'])
    def test_14(self, user_name):
        """Аутентификация пользователя - негативный тест"""
        user_page = UserPage()
        token = user_page.get_token_user(user_name)
        error = {'error': 'Missing password'}
        assert token.status_code == 400
        assert token.json() == error

    @pytest.mark.positive
    @pytest.mark.parametrize('delay', ['3'], ids=['correct data'])
    def test_15(self, delay):
        """Проверка запоздалого ответа"""
        user_page = UserPage()
        list_users = user_page.delayed_responce_list_users(delay)
        key_body_response = ['page', 'per_page', 'total', 'total_pages', 'data']
        assert list_users.status_code == 200
        for name in key_body_response:
            assert name in list_users.json()









