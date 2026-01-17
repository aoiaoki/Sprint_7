import allure
from helpers.order import get_orders_list

@allure.feature("Список заказов")
class TestGetOrdersList:

    def test_get_orders_list(self):
        response = get_orders_list()

        assert response.status_code == 200
        assert "orders" in response.json()
