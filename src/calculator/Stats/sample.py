from random import random

def getSample():

    random_list = []
    for i in range(int(random())):
        n = random.uniform(random(),random())
        random_list.append(n)
    return random_list
