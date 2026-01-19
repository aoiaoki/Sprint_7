import pytest
import random
import string
from api.courier_api import create_courier, login_courier, delete_courier

def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

@pytest.fixture
def courier():
    payload = {
        "login": random_string(),
        "password": random_string(),
        "firstName": random_string()
    }
    create_courier(payload)

    response = login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })
    courier_id = response.json()["id"]

    yield payload, courier_id

    delete_courier(courier_id)

@pytest.fixture
def courier_payload():
    return {
        "login": random_string(),
        "password": random_string(),
        "firstName": random_string()
    }
