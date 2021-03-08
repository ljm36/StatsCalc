from random import random

def getSample():

    random_list = []
    for i in range(10):
        n = random.uniform(random(),random())
        random_list.append(n)
    return random_list
