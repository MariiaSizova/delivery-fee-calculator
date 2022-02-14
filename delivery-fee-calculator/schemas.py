from datetime import datetime

from pydantic import BaseModel, PositiveInt


class ShoppingCart(BaseModel):
    cart_value: PositiveInt
    delivery_distance: PositiveInt
    amount_of_items: PositiveInt
    time: datetime
