"""
Test file for power() function from main.py
Run: pytest test_power.py -v
"""

import pytest
from main import power


class TestPowerFunction:
    """Test cases for power(a, b) function"""
    
    # Basic functionality tests
    def test_power_positive_exponent(self):
        assert power(2, 3) == 8
        assert power(3, 4) == 81
        assert power(5, 2) == 25
    
    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1
        assert power(100, 0) == 1
    
    def test_power_zero_base(self):
        assert power(0, 5) == 0
        assert power(0, 1) == 0
    
    def test_power_one_exponent(self):
        assert power(10, 1) == 10
        assert power(999, 1) == 999
    
    def test_power_large_exponent(self):
        assert power(2, 10) == 1024
        assert power(3, 5) == 243
    
    # Edge case tests
    def test_power_negative_result(self):
        assert power(-2, 3) == -8
        assert power(-3, 2) == 9
    
    def test_power_one_base(self):
        assert power(1, 100) == 1
        assert power(1, 0) == 1