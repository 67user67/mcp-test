import pytest
from main import power

def test_positive_exponent():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(3, 4) == 81

def test_zero_exponent():
    assert power(5, 0) == 1
    assert power(100, 0) == 1

def test_negative_exponent():
    assert power(2, -1) == 0.5
    assert power(4, -1) == 0.25
    assert power(2, -2) == 0.25

def test_float_exponent():
    assert abs(power(4, 0.5) - 2) < 0.0001
    assert abs(power(2, 1.5) - 2.828) < 0.001

def test_zero_base():
    assert power(0, 5) == 0
    assert power(0, 1) == 0

def test_zero_base_negative_exponent():
    import pytest
    with pytest.raises(ZeroDivisionError):
        power(0, -1)
