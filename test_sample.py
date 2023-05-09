from main import *
import pytest
from fastapi.testclient import TestClient

cliente = TestClient(app)

def test_fun_is_prime():
    assert read_number_prime(2) == {"is_prime": True}

def test_fibonacci():
    assert read_number_fibonacci(8) == {"el numero es": 21}

def test_is_prime_endpoint():
    response = cliente.get("/isPrime/7")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

    response = cliente.get("/isPrime/10")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_fibonacci_endpoint():
    response = cliente.get("/fibonacci_number/8")
    assert response.status_code == 200
    assert response.json() == {"el numero es": 21}

    response = cliente.get("/fibonacci_number/1")
    assert response.status_code == 200
    assert response.json() == {"el numero es": 1}

    response = cliente.get("/fibonacci_number/-1")
    assert response.status_code == 200
    assert response.json() == {"error": "La posición debe ser un número entero positivo mayor o igual a 1"}
    