import allure
from helpers.courier import register_new_courier_and_return_login_password, login_courier

@allure.feature("Логин курьера")
class TestLoginCourier:

    def test_login_success(self):
        courier = register_new_courier_and_return_login_password()

        response = login_courier(courier["login"], courier["password"])

        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_wrong_password(self):
        courier = register_new_courier_and_return_login_password()

        response = login_courier(courier["login"], "wrong")

        assert response.status_code == 404
