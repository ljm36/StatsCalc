import Calculator
def subtraction(a, b):
    return a - b
Calculator.subtraction = staticmethod(Calculator.subtraction)