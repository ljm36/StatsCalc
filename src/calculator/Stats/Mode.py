import statistics
from src.calculator.Stats.sample import getSample

def mode(data):

    sample = getSample(data)

    return statistics.mode(sample)