from src.calculator import Calculator
def division(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        print('Division by 0 error')

    return b / a

Calculator.division= staticmethod(Calculator.division)