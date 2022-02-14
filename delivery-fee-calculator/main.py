import uvicorn
from fastapi import FastAPI


from service import get_delivery_fee
from schemas import ShoppingCart


app = FastAPI()


@app.get("/", status_code=200)
def index():
    """
    Basic index route.
    """
    return {"msg": "Hi! This is an API by Mariia Sizova"}


@app.post("/delivery-fee", status_code=200, summary="Calculate delivery fee")
def compute_delivery_fee(shopping_cart: ShoppingCart) -> dict:
    """
    Delivery fee calculation endpoint.
    ---

    Args:
        shopping_cart (ShoppingCart): schema

    Returns:
        dict: dictionary with calculation results
    """
    return get_delivery_fee(shopping_cart)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
