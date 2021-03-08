from random import random

def getSample():
    # random_values = random.sample(data, k=sample_size)
    # return random_values

    randomlist = []
    for i in range(10):
        n = random.uniform(random(),random())
        randomlist.append(n)
    return randomlist
