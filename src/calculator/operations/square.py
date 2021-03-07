import Calculator
def square(a):
    return a * a
Calculator.square = staticmethod(Calculator.square)