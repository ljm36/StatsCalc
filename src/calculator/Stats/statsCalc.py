from src.calculator.Calculator import Calculator
from src.calculator.Stats.Mean import mean
from src.calculator.Stats.Median import median
from src.calculator.Stats.Mode import mode
from src.calculator.Stats.Std import std

class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result


    def median(self, data):
        self.result = median(data)
        return self.result


    def mode(self, data):
        self.result = mode(data)
        return self.result

    def std(self, data):
        self.result = std(data)
        return self.result