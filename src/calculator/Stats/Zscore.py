import statistics

import numpy as np

from src.calculator.operations.division import division


def zscore(data):

    dataset = data.getSample()
    mean = np.mean(dataset)
    std = np.std(dataset)
    zsc = division(std,mean)
    return zsc

statistics.zscore = staticmethod(statistics.zscore)
