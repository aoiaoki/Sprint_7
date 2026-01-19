import pytest
import allure
from api.order_api import create_order, cancel_order

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с одним цветом")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"]])
    def test_create_order_with_one_color(self, color):
        response = create_order(color)

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order(response.json()["track"])

    @allure.title("Можно создать заказ с двумя цветами")
    def test_create_order_with_two_colors(self):
        response = create_order(["BLACK", "GREY"])

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order(response.json()["track"])

    @allure.title("Можно создать заказ без указания цвета")
    def test_create_order_without_color(self):
        response = create_order()

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order(response.json()["track"])
