import pytest
import random
import string
from api.courier_api import create_courier, delete_courier, get_courier_id

def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

@pytest.fixture
def courier_payload():
    return {
        "login": random_string(),
        "password": random_string(),
        "firstName": random_string()
    }

@pytest.fixture
def courier(courier_payload):
    create_courier(courier_payload)
    courier_id = get_courier_id(courier_payload)

    yield courier_payload, courier_id

    delete_courier(courier_id)
