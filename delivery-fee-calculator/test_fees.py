from datetime import datetime

from fastapi.testclient import TestClient

from service import (check_friday_rush, get_distance_charge, get_item_charge,
                     get_surcharge)
from main import app

client = TestClient(app)


def test_surcharge_addition():
    """
    This method tests if surcharge is added to delivery fee.
    """
    cart_value = 790
    surcharge = 210
    assert get_surcharge(cart_value) == surcharge


def test_surcharge_absence():
    """

    This method tests if surcharge fee is skipped.
    """
    cart_value = 1100
    surcharge = 0
    assert get_surcharge(cart_value) == surcharge


def test_distance_fee_addition():
    """

    This method tests if distance fee is added to the delivery fee.
    """
    delivery_distance = 1501
    distance_charge = 400
    assert get_distance_charge(delivery_distance) == distance_charge


def test_distance_fee_absence():
    """

    This method tests if distance fee is skipped for small distances.
    """
    delivery_distance = 999
    distance_charge = 200
    assert get_distance_charge(delivery_distance) == distance_charge


def test_item_fee_addition():
    """

    This method tests if additional items fee is added to the delivery fee.
    """
    amount_of_items = 6
    extra_item_charge = 100
    assert get_item_charge(amount_of_items) == extra_item_charge


def test_item_fee_absence():
    """

    This method tests if additional items fee is skipped
    when items don't exceed the limit.
    """
    amount_of_items = 4
    extra_item_charge = 0
    assert get_item_charge(amount_of_items) == extra_item_charge


def test_before_friday_rush():
    """

    This method tests if friday rush fee is ignored 
    on a different weekday
    """
    time = datetime.strptime("2021-10-8T14:59:59Z", "%Y-%m-%dT%H:%M:%SZ")
    delivery_fee = 8
    friday_rush_fee = 8
    assert check_friday_rush(time, delivery_fee) == friday_rush_fee


def test_friday_rush_start():
    """

    This method tests friday rush start edge case.
    """
    time = datetime.strptime("2021-10-15T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    delivery_fee = 4
    friday_rush_fee = 4.4
    assert check_friday_rush(time, delivery_fee) == friday_rush_fee


def test_friday_rush_end():
    """

    This method tests friday rush end edge case.
    """
    time = datetime.strptime("2021-10-8T19:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    delivery_fee = 5
    friday_rush_fee = 5
    assert check_friday_rush(time, delivery_fee) == friday_rush_fee


# Test API responses
def test_get_index():
    """

    This method check that .get() request to index route  
    returns status code 200 and the predefined message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "msg": "Hi! This is an API by Mariia Sizova"
    }


def test_response_default_response():
    """

    This method check that .post() request to delivery-fee route  
    returns status code 200 and the correct calculated delivery fee value.
    """
    dict_to_send = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "amount_of_items": 4,
        "time": "2021-10-12T13:00:00Z",
    }
    response = client.post("/delivery-fee", json=dict_to_send)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 710}


def test_response_free_delivery():
    """

    This method check that .post() request to delivery-fee route  
    returns status code 200 and the correct calculated delivery fee value.
    Delivery should be free if cart_value is grater that the limit.
    """
    dict_to_send = {
        "cart_value": 10000,
        "delivery_distance": 2235,
        "amount_of_items": 10,
        "time": "2021-10-12T13:00:00Z"
    }
    response = client.post("/delivery-fee", json=dict_to_send)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 0}


def test_response_max_delivery_fee():
    """

    This method check that .post() request to delivery-fee route  
    returns status code 200 and the correct calculated delivery fee value.
    Delivery should not exceed the maximum value.
    """
    dict_to_send = {
        "cart_value": 1200,
        "delivery_distance": 5535,
        "amount_of_items": 10,
        "time": "2021-10-15T15:10:01Z",
    }
    response = client.post("/delivery-fee", json=dict_to_send)
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 1500}


def test_bad_request_wrong_value():
    """

    This method checks that ValueErrors return correct status code.
    """
    dict_to_send = { 
        "cart_value": 1200,
        "delivery_distance": 5535,
        "amount_of_items": "wrong data",
        "time": "2021-10-15T15:10:01Z",
    }
    response = client.post("/delivery-fee", json=dict_to_send)
    assert response.status_code == 422


def test_bad_request_wrong_key():
    """
    
    This method checks that KeyErrors return correct status code.
    """
    dict_to_send = {
        "wrong_key": 1200,
        "delivery_distance": 5535,
        "amount_of_items": "wrong data",
        "time": "2021-10-15T15:10:01Z",
    }
    response = client.post("/delivery-fee", json=dict_to_send)
    assert response.status_code == 422
