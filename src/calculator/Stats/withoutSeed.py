import random
from src.calculator.Stats.sample import getSample

sample = getSample()

for i in range(3):
    print(random.randint(sample, sample))