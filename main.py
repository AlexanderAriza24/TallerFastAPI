from typing import Union
from funciones import *

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/mensaje/hello")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/isPrime/{number}")
def read_number_prime(number: int):
    if is_prime(number):
        return {"is_prime": True}
    else:
        return {"is_prime": False}

@app.get("/fibonacci_number/{number}")
def read_number_fibonacci(number: int):
    if number < 1:
        return {"error": "La posición debe ser un número entero positivo mayor o igual a 1"}
    elif number == 1:
        return {"el numero es": 1}
    else:
        return {"el numero es": fibonacci(number)}
