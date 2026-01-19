import requests
import allure
from data.urls import BASE_URL, COURIER, COURIER_LOGIN

@allure.step("Создание курьера")
def create_courier(payload):
    return requests.post(f"{BASE_URL}{COURIER}", data=payload)

@allure.step("Логин курьера")
def login_courier(payload):
    return requests.post(f"{BASE_URL}{COURIER_LOGIN}", data=payload)

@allure.step("Удаление курьера")
def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}{COURIER}/{courier_id}")
