import random
from src.calculator.Stats.sample import getSample

sample = getSample()

for i in range(3):

    random.seed(sample)
    print(random.randint(sample, sample))