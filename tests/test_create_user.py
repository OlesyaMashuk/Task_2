import pytest
import allure
import requests

from data.urls import Urls
from data.helpers import User
from data.user_data import *


class TestCreateUser:

   
    @allure.title('Создание нового (уникального) пользователя')
    def test_create_new_user_success(self, create_user):
        response, user_data, login_data, token = create_user
        assert response.status_code == 200
        assert response.json()["success"] == True
        
        

    @allure.title('Создание (дублирование) пользователя, который уже зарегистирован')
    def test_create_double_user_error(self):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.URL_REGISTRATION}', data=data_double)
        assert response.status_code == 403 
        assert response.reason == 'Forbidden'
        assert 'User already exists' in response.text

    @allure.title('Создание пользователя с незаполненными (одним или несколькими) обязательными полями')
    @pytest.mark.parametrize("user_data", [data_without_email, data_without_password, data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Urls.URL_REGISTRATION}', data=user_data)
        assert response.status_code == 403
        assert 'Email, password and name are required fields' in response.text