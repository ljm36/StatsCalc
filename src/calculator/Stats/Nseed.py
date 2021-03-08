import random
from src.calculator.Stats.sample import getSample

sample = getSample()

for i in range(sample):

    random.seed(sample)
    print(random.randint(sample, sample))