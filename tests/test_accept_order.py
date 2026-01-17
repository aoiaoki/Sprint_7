import allure
from helpers.courier import (
    register_new_courier_and_return_login_password,
    login_courier
)
from helpers.order import (
    create_order,
    accept_order,
    cancel_order,
    get_order_by_track
)

@allure.feature("Принятие заказа")
class TestAcceptOrder:

    def test_accept_order_success(self):
        # создаём курьера
        courier = register_new_courier_and_return_login_password()
        login_response = login_courier(courier["login"], courier["password"])
        courier_id = login_response.json()["id"]

        # создаём заказ
        order_response = create_order()
        track = order_response.json()["track"]

        # получаем orderId по track
        order = get_order_by_track(track).json()["order"]
        order_id = order["id"]

        # принимаем заказ
        accept_response = accept_order(order_id, courier_id)

        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}

        # чистим данные
        cancel_order(track)

    def test_accept_order_without_courier_id(self):
        order_response = create_order()
        track = order_response.json()["track"]

        order = get_order_by_track(track).json()["order"]
        order_id = order["id"]

        response = accept_order(order_id, None)

        assert response.status_code == 400

        cancel_order(track)

    def test_accept_order_with_invalid_order_id(self):
        courier = register_new_courier_and_return_login_password()
        login_response = login_courier(courier["login"], courier["password"])
        courier_id = login_response.json()["id"]

        response = accept_order(999999, courier_id)

        assert response.status_code == 404
