import pytest
import allure
from helpers.order import create_order, cancel_order

@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize(
        "colors",
        [["BLACK"], ["GREY"], ["BLACK", "GREY"], None]
    )
    def test_create_order_with_colors(self, colors):
        response = create_order(colors)

        assert response.status_code == 201
        assert "track" in response.json()

        cancel_order(response.json()["track"])
