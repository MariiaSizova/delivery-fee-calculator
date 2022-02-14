# Delivery fee calculator API
## **About**
### **Author:** Mariia Sizova | [Github](https://github.com/MariiaSizova)
### **Date:**  17.01.2022
### **About:** 
This API calculates delivery fees. I used FastAPI because its intuitive, requires less code, and as the name suggests its fast! Additionally, I wrote several tests with Pytest that check the basic functinality and some edge cases.

## **Folder Structure**

---

```
delivery-fee-calculator
│   README.md
│   Dockerfile
│   docker-compose.yml
│   requirements.txt            
└───delivery-fee-calculator    # API folder
│   │   main.py                # Main FastAPI app
│   │   test_fees.py           # Pytests
│   │   service.py             # Delivery fee calculators
│   │   schemas.py             # Schema for data validation

```

## **Installation**

---
## **Docker-Compose**

You can use Docker compose for installation.

```
docker compose up --build
```
[![LocalHost](https://img.shields.io/badge/Fast_API-delivery_fee_calculator-0088CC?style=for-the-badge&logo=fastAPI&logoColor=#419dda)](http://127.0.0.1:8000)
---

## **Testing**
You can either test the api with FastAPI docs:

[![Docs](https://img.shields.io/badge/Fast_API-/docs-0088CC?style=for-the-badge&logo=fastAPI&logoColor=#419dda)](http://127.0.0.1:8000/docs)

Sample request:
```
{
    "cart_value": 790,
    "delivery_distance": 2235,
    "amount_of_items": 4,
    "time": "2021-10-12T13:00:00Z"
}
```
Output:
```
{"delivery_fee":710}
```

## **Pytest**

Alternatively you can use the tests in test_fees.py by running "pytest" command in the project folder.

```
pytest
```
---
## Thank you!
