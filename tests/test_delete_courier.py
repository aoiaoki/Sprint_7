import allure
import requests
from helpers.courier import (
    register_new_courier_and_return_login_password,
    login_courier,
    delete_courier
)

@allure.feature("Удаление курьера")
class TestDeleteCourier:

    def test_delete_courier_success(self):
        courier = register_new_courier_and_return_login_password()
        login_response = login_courier(courier["login"], courier["password"])
        courier_id = login_response.json()["id"]

        response = delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    def test_delete_courier_without_id(self):
        response = requests.delete(
            "https://qa-scooter.praktikum-services.ru/api/v1/courier/"
        )

        assert response.status_code == 404

    def test_delete_nonexistent_courier(self):
        response = delete_courier(999999)

        assert response.status_code == 404
