#!/usr/bin/env python3

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Unittest for Simple Calculator
    """
    def test_add_positive(self):
        result = SimpleCalculator.add(self, 3, 4)
        self.assertEqual(result, 7)

    def test_add_negative(self):
        result = SimpleCalculator.add(self, -3, 4)
        self.assertEqual(result, 1)

    def test_subtract_positive(self):
        result = SimpleCalculator.subtract(self, 3, 4)
        self.assertEqual(result, -1)
    
    def test_subtract_negative(self):
        result = SimpleCalculator.subtract(self, -3, 4)
        self.assertEqual(result, -7)

    def test_multiply_positive(self):
        result = SimpleCalculator.multiply(self, 3, 4)
        self.assertEqual(result, 12)

    def test_multiply_negative(self):
        result = SimpleCalculator.multiply(self, -3, 4)
        self.assertEqual(result, -12)

    def test_divide_positive(self):
        result = SimpleCalculator.divide(self, 6, 2)
        self.assertEqual(result, 3)

    def test_divide_positive(self):
        result = SimpleCalculator.divide(self, 6, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()