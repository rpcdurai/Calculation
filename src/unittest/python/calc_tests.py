import unittest
from calc import Calculator

class CalculatorTest(unittest.TestCase):
    

    def test_addition_with_negative_numbers(self):
        calculator = Calculator()
        result = calculator.add(-2, 3)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

