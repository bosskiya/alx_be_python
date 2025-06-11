#!/usr/bin/env python3

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Unittest for Simple Calculator
    """
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add_positive(self):
        result = self.calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative(self):
        result = self.calc.add(-3, 4)
        self.assertEqual(result, 1)

    def test_subtract_positive(self):
        result = self.calc.subtract(3, 4)
        self.assertEqual(result, -1)
    
    def test_subtract_negative(self):
        result = self.calc.subtract(-3, 4)
        self.assertEqual(result, -7)

    def test_multiply_positive(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiply_negative(self):
        result = self.calc.multiply(-3, 4)
        self.assertEqual(result, -12)

    def test_divide_positive(self):
        result = self.calc.divide(6, 2)
        self.assertEqual(result, 3)

    def test_divide_positive(self):
        result = self.calc.divide(6, 0)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()