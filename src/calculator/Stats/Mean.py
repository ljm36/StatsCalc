import statistics
from src.calculator.Stats.sample import getSample

def mean():
    sample = getSample()
    return statistics.mean(sample)