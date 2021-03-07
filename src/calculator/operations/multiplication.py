from src.calculator import Calculator
def multiplication(a, b):
    return a * b
Calculator.multiplication = staticmethod(Calculator.multiplication)