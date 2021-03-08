import numpy as np
from src.calculator.Stats.sample import getSample

def variance(data):

    dataset = getSample(data)
    var = np.var(dataset)
    return var
