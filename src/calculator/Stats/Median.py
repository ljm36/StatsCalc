import statistics
from src.calculator.Stats.sample import getSample


def median(data):
    sample = getSample(data)
    return statistics.median(sample)
statistics.median = staticmethod(statistics.median)