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

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-3, 4), 1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 4), -1)
        self.assertEqual(self.calc.subtract(-3, 4), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(6, 0), None)

if __name__ == "__main__":
    unittest.main()