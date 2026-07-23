
import pytest
import requests

from data.urls import Urls
from data.helpers import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.generate_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.MAIN_URL}{Urls.URL_REGISTRATION}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Urls.DELETE_USER}", headers={'Authorization': f'{token}'})