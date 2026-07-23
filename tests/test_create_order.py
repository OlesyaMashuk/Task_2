import allure
import requests


from data.urls import Urls
from data.ingredients_data import Ingredients


class TestCreateOrder:
    
    @allure.title("Создание заказа авторизованным пользователем с выбранными ингредиентами")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        r = requests.post(f"{Urls.MAIN_URL}{Urls.URL_CREATE_ORDER}", headers=token, data=Ingredients.valid_ingredients_data)
        response_data = r.json()
        assert r.status_code == 200
        assert r.json().get("success") is True
        assert "name" in response_data
        assert "order" in response_data
        assert "success" in response_data

    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.URL_CREATE_ORDER}", data=Ingredients.valid_ingredients_data)
        assert r.status_code == 200
        assert r.json().get("success") is True


    @allure.title("Создание заказа без ингредиентов (пользователь авторизован)")
    def test_create_order_with_ingridient(self):
        r = requests.post(f"{Urls.MAIN_URL}{Urls.URL_CREATE_ORDER}")
        assert r.status_code == 400
        assert r.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание с невалидным хешем ингредиента (пользователь авторизован)")
    def test_create_order_invalid_hash_ingridient(self):
        response = requests.post(Urls.MAIN_URL + Urls.URL_CREATE_ORDER, headers=Urls.headers,
                                 json=Ingredients.invalid_ingredients_data)
        assert response.status_code == 500
        assert 'Internal Server Error' in response.text