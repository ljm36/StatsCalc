import unittest
from calculator.Calculator import Calculator
from tests.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_add = CsvReader('/tests/Unit Test Addition.tests').data
        for row in test_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_method_calculator(self):
        test_sub = CsvReader('/tests/Unit Test Subtraction.tests').data
        for row in test_sub:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_multiplication_method_calculator(self):
        test_multiplication = CsvReader('/tests/Unit Test Multiplication.tests').data
        for row in test_multiplication:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_division_method_calculator(self):
        test_division = CsvReader('/tests/Unit Test Division.tests').data
        for row in test_division:
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_square = CsvReader('/tests/Unit Test Square.tests').data
        for row in test_square:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_root_method_calculator(self):
        test_root = CsvReader('/tests/Unit Test Square Root.tests').data
        for row in test_root:
            self.assertEqual(self.calculator.root(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
