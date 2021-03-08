import numpy as np

def zscore(data):
    dataset = data.getSample()
    mean = np.mean(data)
    std = np.std(data)
    zsc = mean/std
    return zsc