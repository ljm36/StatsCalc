from random import random

def getSample():

    random_list = []
    for i in range(int(random())):
        n = float(random())
        random_list.append(n)

    return random_list

def exception(random_list):

   if len(random_list)==0:
    try:
        a = random_list
        return a

    finally:
        return None