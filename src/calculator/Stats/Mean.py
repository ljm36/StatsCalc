import statistics
from src.calculator.Stats.sample import getSample

def mean(sample):
    sample = getSample()
    return statistics.mean(sample)

statistics.mean = staticmethod(statistics.mean)