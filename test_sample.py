from main import *

def test_fun_is_prime():
    assert read_number_prime(2) == {"is_prime": True}

def test_fibonacci():
    assert read_number_fibonacci(8) == {"el numero es": 21}
