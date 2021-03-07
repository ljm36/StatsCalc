from src.calculator.Calculator import Calculator
from src.calculator.Stats.Mean import mean
from src.calculator.Stats.SampleMean import sample_mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mean(self, data):
        self.result = sample_mean(data)
        return self.result
