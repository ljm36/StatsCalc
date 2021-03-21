import statistics
from src.calculator.Stats.sample import getSample

def mean(data, data2):
    sample = getSample(data, data2)
    return statistics.mean(sample)