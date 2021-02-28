from calculator.operations.addition import addition
from calculator.operations.subtraction import subtraction
from calculator.operations.multiplication import multiplication
from calculator.operations.division import division
from calculator.operations.square import square
from calculator.operations.squareRoot import root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        a = float(a)
        b = float(b)
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        a = float(a)
        b = float(b)
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        a = float(a)
        b = float(b)
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        a = float(a)
        b = float(b)
        self.result = division(a, b)
        return self.result

    def square(self, a):
        a = float(a)
        self.result = square(a)
        return self.result

    def root(self, a):
        a = float(a)
        self.result = root(a)
        return self.result
