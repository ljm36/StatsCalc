from src.calculator.Calculator import Calculator
from src.calculator.Stats.Mean import mean
from src.calculator.Stats.Median import median


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result
