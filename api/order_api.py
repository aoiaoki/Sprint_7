import requests
import allure
from data.urls import *
from data.order_data import ORDER_BODY

@allure.step("Создание заказа")
def create_order(colors=None):
    body = ORDER_BODY.copy()
    body["color"] = colors
    return requests.post(f"{BASE_URL}{ORDERS}", json=body)

@allure.step("Отмена заказа")
def cancel_order(track):
    return requests.put(f"{BASE_URL}{ORDERS_CANCEL}", params={"track": track})

@allure.step("Принятие заказа")
def accept_order(order_id, courier_id):
    return requests.put(
        f"{BASE_URL}{ORDERS_ACCEPT.format(order_id=order_id)}",
        params={"courierId": courier_id}
    )

@allure.step("Получение заказа по треку")
def get_order_by_track(track):
    return requests.get(f"{BASE_URL}{ORDERS_TRACK}", params={"t": track})

@allure.step("Получение списка заказов")
def get_orders_list():
    return requests.get(f"{BASE_URL}{ORDERS}")
