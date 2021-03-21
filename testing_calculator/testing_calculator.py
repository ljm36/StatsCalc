import unittest
from src.calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication_method_calculator(self):
        self.assertEqual(self.calculator.multiplication(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.division(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_root_method_calculator(self):
        self.assertEqual(self.calculator.root(9), 3)
        self.assertEqual(self.calculator.result, 3)




if __name__ == '__main__':
    unittest.main()