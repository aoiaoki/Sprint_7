import allure
from helpers.order import create_order, get_order_by_track, cancel_order

@allure.feature("Получение заказа по номеру")
class TestGetOrderByNumber:

    def test_get_order_success(self):
        order_response = create_order()
        track = order_response.json()["track"]

        response = get_order_by_track(track)

        assert response.status_code == 200
        assert "order" in response.json()

        cancel_order(track)

    def test_get_order_without_track(self):
        response = get_order_by_track(None)

        assert response.status_code == 400

    def test_get_nonexistent_order(self):
        response = get_order_by_track(999999)

        assert response.status_code == 404
