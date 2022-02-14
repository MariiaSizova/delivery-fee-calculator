FROM python:3.9

WORKDIR /delivery-fee-calculator

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./delivery-fee-calculator ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]