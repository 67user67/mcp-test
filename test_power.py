import pytest
from main import power

def test_positive_exponent():
    assert power(2, 3) == 8

def test_zero_exponent():
    assert power(5, 0) == 1

def test_zero_base():
    assert power(0, 5) == 0

def test_exponent_one():
    assert power(7, 1) == 7

def test_large_exponent():
    assert power(2, 10) == 1024

def test_negative_result():
    assert power(-2, 3) == -8

def test_base_one():
    assert power(1, 100) == 1
