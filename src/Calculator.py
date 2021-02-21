import math



def root(a):
    return math.sqrt(a)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        a = int(a)
        b = int(b)
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
        self.result = a - b
        return self.result

    def multiplication(self, a, b):
        a = int(a)
        b = int(b)
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        a = int(a)
        b = int(b)
        self.result = division(a, b)
        return self.result

    def square(self, a):
        a = int(a)
        self.result = square(a)
        return self.result

    def root(self, a):
        a = int(a)
        self.result = root(a)
        return self.result
