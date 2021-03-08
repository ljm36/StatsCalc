from random import random


def getSample(data, sample_size):
    # random_values = random.sample(data, k=sample_size)
    # return random_values

    randomlist = []
    for i in range(10):
        n = random.randint(random(),random())
        randomlist.append(n)
    return randomlist
