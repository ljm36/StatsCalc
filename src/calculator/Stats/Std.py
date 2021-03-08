import statistics
from src.calculator.Stats.sample import getSample

def std(data):

    sample = getSample(data)

    return statistics.mode(sample)