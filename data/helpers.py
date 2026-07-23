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