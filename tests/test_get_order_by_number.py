import allure
from api.order_api import create_order, get_order_by_track, cancel_order

@allure.feature("Получение заказа по номеру")
class TestGetOrderByNumber:

    @allure.title("Можно получить заказ по номеру")
    def test_get_order_success(self):
        response = create_order()
        track = response.json()["track"]

        response = get_order_by_track(track)
        body = response.json()

        assert response.status_code == 200
        assert body["order"]["id"] > 0

        cancel_order(track)

    @allure.title("Ошибка если не передан номер заказа")
    def test_get_order_without_track(self):
        response = get_order_by_track(None)

        assert response.status_code == 400

    @allure.title("Ошибка при запросе несуществующего заказа")
    def test_get_nonexistent_order(self):
        response = get_order_by_track(999999)

        assert response.status_code == 404
