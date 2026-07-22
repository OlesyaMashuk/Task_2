import pytest
import allure
import requests

from data.curls import Curls
from data.user_data import User


class TestCreateUser:

   
    @allure.title('Создание нового (уникального) пользователя')
    def test_create_new_user_success(self):
        user_data = User.generate_data_user()
        response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data=user_data)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()['user']['email'] == user_data['email']
        assert response.json()['user']['name'] == user_data['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title('Создание (дублирование) пользователя, который уже зарегистирован')
    def test_create_double_user_error(self):
        response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data=User.data_double)
        assert response.status_code == 403 
        assert response.reason == 'Forbidden'
        assert 'User already exists' in response.text

    @allure.title('Создание пользователя с незаполненными (одним или несколькими) обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data=user_data)
        assert response.status_code == 403
        assert 'Email, password and name are required fields' in response.text