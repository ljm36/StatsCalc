from src.calculator.Calculator import Calculator
from src.calculator.Stats.Mean import mean



class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
