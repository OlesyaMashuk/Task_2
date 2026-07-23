import allure
import requests

from data.urls import Urls
from data.ingredients_data import Ingredients


class TestGetOrderUser:

    
    @allure.title("Получение списка заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        response_get_order = requests.get(f"{Urls.MAIN_URL}{Urls.URL_GET_USER_ORDERS}", headers=token)
        assert response_get_order.status_code == 200
        assert response_get_order.json()["success"] == True
        assert response_get_order.json()['orders'] is not None

    
    @allure.title("Неавторизованный пользователь не может получить список своих заказов")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{Urls.MAIN_URL}{Urls.URL_GET_USER_ORDERS}")
        assert r.status_code == 401
        assert r.json()['message'] == "You should be authorised"
        assert r.json()['success'] == False
