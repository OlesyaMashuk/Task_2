import allure
import requests

from data.curls import Curls
from data.user_data import User


class TestloginUser:

    
    @allure.title('Авторизация существующего пользователя')
    def test_login_user(self):
        response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=User.data_correct)
        assert response.status_code == 200
        assert response.json().get('success') == True

    @allure.title('Авторизация пользователя без обязательных полей (логин/пароль)')
    def test_login_user_error(self):
        response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=User.data_negative)
        assert response.status_code == 401
        assert response.json().get('success') == False
        assert response.json().get('message') == "email or password are incorrect"