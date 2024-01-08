import requests

base_url = 'https://reqres.in/api'

class ResourcePage:

    def get_list_resource(self):
        response = requests.get(f'{base_url}/unknown')
        return response

    def get_single_resource(self, id):
        response = requests.get(f'{base_url}/unknown/{id}')
        return response

class UserPage:

    def get_list_users(self, page):
        params = {'page': page}
        response = requests.get(f'{base_url}/users', params=params)
        return response

    def get_user_by_id(self, user_id):
        response = requests.get(f'{base_url}/users/{user_id}')
        return response

    def create_user(self, name, job):
        data = {"name": name,
                "job": job}
        response = requests.post(f'{base_url}/users', json=data)
        return response

    def update_user_put(self, user_id, name, job):
        params = {"name": name,
                  "job": job}
        response = requests.put(f'{base_url}/users/{user_id}', params=params)
        return response

    def update_user_patch(self, user_id, name, job):
        data = {"name": name,
                "job": job}
        response = requests.patch(f'{base_url}/users/{user_id}', data=data)
        return response

    def delete_user(self, user_id):
        response = requests.delete(f'{base_url}/users/{user_id}')
        return response

    def registration_user(self, email, password=None):
        data = {"email": email,
                "password": password}
        response = requests.post(f'{base_url}/register', json=data)
        return response

    def get_token_user(self, email, password=None):
        data = {"email": email,
                "password": password}
        response = requests.post(f'{base_url}/login', json=data)
        return response

    def delayed_responce_list_users(self, delay):
        params = {'delay': delay}
        responce = requests.get(f'{base_url}/users', params=params)
        return responce
