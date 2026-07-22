import allure
import requests

from data.curls import Curls
from data.ingredients_data import Ingredients


class TestGetOrderUser:

    
    @allure.title("Получение списка заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(f"{Curls.MAIN_URL}{Curls.URL_CREATE_ORDER}", headers=token, data=Ingredients.invalid_ingredients_data)
        response_get_order = requests.get(f"{Curls.MAIN_URL}{Curls.URL_GET_USER_ORDERS}", headers=token)
        assert response_get_order.status_code == 200
        assert response_get_order.json()["success"] == True
        assert response_get_order.json()['orders'] is not None

    
    @allure.title("Неавторизованный пользователь не может получить список своих заказов")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{Curls.MAIN_URL}{Curls.URL_GET_USER_ORDERS}")
        assert r.status_code == 401
        assert r.json()['message'] == "You should be authorised"
        assert r.json()['success'] == False
