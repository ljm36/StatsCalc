from src.calculator.Calculator import Calculator
def division(a, b):
    return b / a

Calculator.division= staticmethod(Calculator.division)