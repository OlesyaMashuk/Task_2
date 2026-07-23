import allure
import requests

from data.urls import Urls
from data.helpers import User
from data.user_data import *


class TestLoginUser:

    
    @allure.title('Авторизация существующего пользователя')
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.URL_LOGIN}', data=data_correct)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == data_correct['email']
        assert response.json()['user']['name'] == data_correct['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title('Авторизация пользователя без обязательных полей (логин/пароль)')
    def test_login_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.URL_LOGIN}', data=data_negative)
        assert response.status_code == 401
        assert response.json().get('success') == False
        assert response.reason == 'Unauthorized'
        assert response.json().get('message') == "email or password are incorrect"