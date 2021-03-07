from src.calculator.Calculator import addition
from src.calculator.Calculator import division


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)