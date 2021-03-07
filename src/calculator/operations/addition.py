from src.calculator.Calculator import Calculator
def addition(a, b):
    return a + b

Calculator.addition = staticmethod(Calculator.addition)