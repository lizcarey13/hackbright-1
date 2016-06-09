import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(4, 8)
        self.assertEqual(12, result)

    def test_subtract(self):
        result = self.calc.subtract(8, 4)
        self.assertEqual(4, result)

    def test_multiply(self):
        result = self.calc.multiply(8, 4)
        self.assertEqual(32, result)

    def test_divide(self):
        result = self.calc.divide(8, 4)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()