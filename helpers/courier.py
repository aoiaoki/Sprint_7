import requests
import random
import string

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_and_return_login_password():
    payload = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

    response = requests.post(f"{BASE_URL}/courier", data=payload)

    if response.status_code == 201:
        return payload
    return {}

def login_courier(login, password):
    return requests.post(
        f"{BASE_URL}/courier/login",
        data={"login": login, "password": password}
    )

def delete_courier(courier_id):
    return requests.delete(
        f"{BASE_URL}/courier/{courier_id}"
    )
