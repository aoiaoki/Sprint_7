import requests
import allure
from helpers.courier import register_new_courier_and_return_login_password

@allure.feature("Создание курьера")
class TestCreateCourier:

    def test_create_courier_success(self):
        courier = register_new_courier_and_return_login_password()

        assert courier != {}


    def test_create_duplicate_courier(self):
        data = register_new_courier_and_return_login_password()

        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier",
            data=data
        )

        assert response.status_code == 409

    def test_create_courier_without_login(self):
        response = requests.post(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier",
            data={"password": "1234"}
        )

        assert response.status_code == 400
