from app import add, multiply

def test_multiplication():
    assert multiply(2, 6) == 12

def test_addition():
    assert add(5, 3) == 8