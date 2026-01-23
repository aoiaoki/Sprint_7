import allure
from api.order_api import get_orders_list

@allure.feature("Список заказов")
class TestGetOrdersList:

    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_list(self):
        response = get_orders_list()
        body = response.json()

        assert response.status_code == 200
        assert isinstance(body["orders"], list)
