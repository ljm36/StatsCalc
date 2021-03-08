from src.calculator.Calculator import Calculator
from src.calculator.Stats.Mean import mean
from src.calculator.Stats.Mode import mode


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result