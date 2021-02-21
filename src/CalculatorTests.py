import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        testData = CsvReader('datafileaddition.csv').data

        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.division(10, 2), 5)
        self.assertEqual(self.calculator.result, 5)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_root_method_calculator(self):
        self.assertEqual(self.calculator.root(16), 4)
        self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
