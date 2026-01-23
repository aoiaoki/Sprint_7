import allure
from api.order_api import create_order, accept_order, cancel_order, get_order_by_track

@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(self, courier):
        _, courier_id = courier

        order_response = create_order()
        track = order_response.json()["track"]

        order = get_order_by_track(track).json()["order"]
        order_id = order["id"]

        response = accept_order(order_id, courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

        cancel_order(track)

    @allure.title("Ошибка, если не передан id курьера")
    def test_accept_order_without_courier_id(self):
        order_response = create_order()
        track = order_response.json()["track"]

        order = get_order_by_track(track).json()["order"]
        order_id = order["id"]

        response = accept_order(order_id, None)

        assert response.status_code == 400

        cancel_order(track)

    @allure.title("Ошибка при неверном id заказа")
    def test_accept_order_with_invalid_order_id(self, courier):
        _, courier_id = courier

        response = accept_order(999999, courier_id)

        assert response.status_code == 404
