import allure
import requests

from data.urls import Urls
from data.helpers import User



class TestChangingUserData:
    
    @allure.title("Успешное изменение адреса (email) авторизованного пользователя")
    def test_changing_user_email_with_auth(self, create_user):
        payload = {'email': User.generate_data_user()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json()['success'] == True
        assert r.json()['user']['email'] == payload['email']
    

    
    @allure.title("Успешное изменение пароля (password) авторизованного пользователя")
    def test_changing_user_password_with_auth(self, create_user):
        payload = {'password': User.generate_data_user()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json().get("success") is True
        

    
    @allure.title("Успешное изменение имени (name) авторизованного пользователя")
    def test_changing_user_name_with_auth(self, create_user):
        payload = {'name': User.generate_data_user()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.CHANGE_USER_DATA}", headers=token, data=payload)
        assert r.status_code == 200
        assert r.json()['user']['name'] == payload["name"]
        assert r.json().get("success") is True

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_not_auth(self):
        r = requests.patch(f"{Urls.MAIN_URL}{Urls.CHANGE_USER_DATA}", data=User.generate_data_user())
        assert r.status_code == 401
        assert r.json()['success']  == False
        assert r.reason == 'Unauthorized'
        assert r.json()['message'] == 'You should be authorised'