import numpy
import matplotlib.pyplot as plt
class FunctionBox:
    def __init__(self):
        pass

    def n2(self, sources):
        coefficients = numpy.polyfit(sources[0], sources[1], 2)
        def n2_function(x):
            return x ** 2 * coefficients[0] + x * coefficients[1] + coefficients[2]
        return n2_function

    def n(self, sources):
        coefficients = numpy.polyfit(sources[0], sources[1], 1)
        def n_function(x):
            return x * coefficients[0] + coefficients[1]
        return n_function

    def s(self, sources):
        coefficient = numpy.polyfit(sources[0], sources[1], 0)
        def s_function(x):
            return coefficient
        return s_function

