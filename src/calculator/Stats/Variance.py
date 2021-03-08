import numpy as np

def variance(data):
    dataset = data.getSample()
    var = np.var(dataset)
    return var
