
import pytest
import requests

from data.curls import Curls
from data.user_data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.generate_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Curls.MAIN_URL}{Curls.URL_REGISTRATION}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Curls.MAIN_URL}{Curls.DELETE_USER}", headers={'Authorization': f'{token}'})