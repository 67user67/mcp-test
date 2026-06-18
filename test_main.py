import unittest
from main import power


class TestPowerFunction(unittest.TestCase):
    """Test cases for power(a, b) function"""

    def test_positive_exponent(self):
        """Test with positive exponent"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(3, 4), 81)

    def test_zero_exponent(self):
        """Test with zero exponent (a^0 = 1)"""
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(0, 0), 1)  # Convention: 0^0 = 1

    def test_negative_exponent(self):
        """Test with negative exponent - EXPECTED TO FAIL (current bug)"""
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(4, -2), 0.25)

    def test_float_exponent(self):
        """Test with float exponent - EXPECTED TO FAIL (current bug)"""
        self.assertAlmostEqual(power(2, 1.5), 2.828, places=3)

    def test_zero_base_positive_exponent(self):
        """Test with zero base and positive exponent"""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 1), 0)

    def test_zero_base_negative_exponent(self):
        """Test with zero base and negative exponent - EXPECTED TO FAIL"""
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)


if __name__ == '__main__':
    unittest.main()