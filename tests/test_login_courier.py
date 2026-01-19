import allure
from api.courier_api import login_courier

@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, courier):
        payload, _ = courier

        response = login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при неверном пароле")
    def test_login_wrong_password(self, courier):
        payload, _ = courier

        response = login_courier({
            "login": payload["login"],
            "password": "wrong"
        })

        assert response.status_code == 404

    @allure.title("Ошибка при логине несуществующего пользователя")
    def test_login_nonexistent_user(self):
        response = login_courier({
            "login": "no_user",
            "password": "1234"
        })

        assert response.status_code == 404

    @allure.title("Ошибка если не передан логин")
    def test_login_without_login(self):
        response = login_courier({"password": "1234"})

        assert response.status_code == 400
