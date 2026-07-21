from faker import Faker

class User:

    @staticmethod
    def generate_data_user():
        fake = Faker()

        generate_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return generate_data

    data_correct = {
        "email": 'diplom_ya34@yandex.ru',
        "password": "qwerty34", "name": "Olesya"}

    data_negative = {
        "email": 'negativ_user@yandex.ru',
        "password": "password"}

    data_double = {
        "email": 'diplom_ya34@yandex.ru',
        "password": "qwerty34",
        "name": "Olesya"}

    data_without_email = {
        "email": '',
        "password": "password",
        "name": "Olesya"}

    data_without_password = {
        "email": 'diplom_ya34@yandex.ru',
        "password": "",
        "name": "Olesya"}

    data_without_name = {
        "email": 'diplom_ya34@yandex.ru',
        "password": "qwerty34",
        "name": ""}

    data_updated = {
        "email": 'diplom_ya34@yandex.ru',
        "password": "qwerty34",
        "name": "User"}