import allure
from api.courier_api import create_courier

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_payload):
        response = create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier_payload):
        create_courier(courier_payload)
        response = create_courier(courier_payload)

        assert response.status_code == 409
        assert "message" in response.json()

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        response = create_courier({
            "password": "1234",
            "firstName": "test"
        })

        assert response.status_code == 400
        assert "message" in response.json()
