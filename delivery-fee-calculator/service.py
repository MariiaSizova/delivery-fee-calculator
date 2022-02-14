import math
from datetime import datetime

from schemas import ShoppingCart


def get_surcharge(cart_value: int, limit: int = 1000) -> float:
    """
    This function calculates surcharge if cart value is lower that the limit.
    ---

    Args: 
        cart_value (int): Value of the cart
        limit (int): Surcharge threshold. Default value is 1000 cents.

    Returns: 
        surcharge (float): surcharge fee
    """
    if cart_value < limit:
        return limit - cart_value
    return 0


def get_distance_charge(delivery_distance: int) -> float:
    """
    This function calculates distance fee and adds it to delivery fee.
    ---

    Args: 
        delivery_distance (int): distance of the delivery

    Returns: 
        distance_charge (float): fee for additional distance
    """
    first_kilometer = 1000
    additional_distance = 500
    additional_distance_fee = 100
    minimum_fee = 200

    if delivery_distance > 1000:
        additional_distance = math.ceil((delivery_distance - first_kilometer) / additional_distance)
        return additional_distance * additional_distance_fee + minimum_fee
    return minimum_fee


def get_item_charge(amount_of_items: int) -> float:
    """
    This function calculates extra item fee  and adds it to delivery fee.
    ---

    Args: 
        amount_of_items (int): amount of items in the basket

    Returns: 
        item_charge (float): fee for extra items
    """
    item_limit = 5
    free_items = 4
    extra_item_charge = 50
    if amount_of_items >= item_limit:
        extra_items = amount_of_items - free_items
        return extra_item_charge * extra_items
    return 0


def check_friday_rush(time: datetime, delivery_fee: float) -> float:
    """
    This function calculates the friday rush fee and adds it to delivery fee.
    ---

    Args: 
        time (object): datetime object
        delivery_fee (float): delivery_fee without friday rush fee

    Returns: 
        delivery_fee (float): delivery_fee with friday rush fee
    """
    friday = 4
    if time.weekday() == friday and 15 <= time.hour < 19:
        delivery_fee *= 1.1 
    return delivery_fee


def get_delivery_fee(shopping_cart: ShoppingCart) -> dict:
    """
    Delivery fee calculation.
    ---

    Args:
        shopping_cart (ShoppingCart): Schema for data validation

    Returns:
        dict: dict with fee delivery calculation results
    """
    delivery_fee = 0.0
    max_delivery_fee = 1500
    if shopping_cart.cart_value >= 10000:
        return {"delivery_fee": delivery_fee}
    else:
        surcharge = get_surcharge(shopping_cart.cart_value)
        distance_charge = get_distance_charge(shopping_cart.delivery_distance)
        item_charge = get_item_charge(shopping_cart.amount_of_items)
        delivery_fee = surcharge + distance_charge + item_charge
        delivery_fee = check_friday_rush(shopping_cart.time, delivery_fee)

        if delivery_fee > max_delivery_fee:
            delivery_fee = max_delivery_fee

    return {"delivery_fee": delivery_fee}
