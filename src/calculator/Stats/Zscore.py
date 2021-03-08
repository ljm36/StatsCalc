import statistics

import numpy as np

def zscore(data):

    dataset = data.getSample()
    mean = np.mean(dataset)
    std = np.std(dataset)
    zsc = mean/std
    return zsc

statistics.zscore = staticmethod(statistics.zscore)
