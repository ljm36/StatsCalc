import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('employee_birthday.txt')

    def test_return_data_as_objects(self):
        people =

if __name__ == '__main__':
    unittest.main()
