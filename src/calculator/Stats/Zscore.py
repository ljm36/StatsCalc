import statistics

import numpy as np

from src.calculator.operations.division import division
from src.calculator.Stats.sample import getSample

def zscore():

    dataset = getSample()
    mean = np.mean(dataset)
    std = np.std(dataset)
    zsc = division(std,mean)
    return zsc

#statistics.zscore = staticmethod(statistics.zscore)
