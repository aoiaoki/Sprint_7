import allure
from api.courier_api import delete_courier

@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, courier):
        _, courier_id = courier

        response = delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Ошибка при удалении несуществующего курьера")
    def test_delete_nonexistent_courier(self):
        response = delete_courier(999999)

        assert response.status_code == 404
