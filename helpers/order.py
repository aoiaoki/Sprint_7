import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def create_order(colors=None):
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2026-01-20",
        "comment": "Dattebayo",
        "color": colors
    }
    return requests.post(f"{BASE_URL}/orders", json=payload)

def cancel_order(track):
    return requests.put(
        f"{BASE_URL}/orders/cancel",
        params={"track": track}
    )

def accept_order(order_id, courier_id):
    return requests.put(
        f"{BASE_URL}/orders/accept/{order_id}",
        params={"courierId": courier_id}
    )

def get_orders_list():
    return requests.get(f"{BASE_URL}/orders")

def get_order_by_track(track):
    return requests.get(
        f"{BASE_URL}/orders/track",
        params={"t": track}
    )
