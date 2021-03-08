import statistics
from src.calculator.Stats.sample import getSample

def mean(data):
    sample = getSample(data)
    return statistics.mean(sample)
