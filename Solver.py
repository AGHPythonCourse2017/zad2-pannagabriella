import numpy
import sys

from FunctionBox import FunctionBox

import matplotlib.pyplot as plt

class Solver:
    def __init__(self, resources):
        self.list_x = resources[0]
        self.list_y = resources[1]
        self.function_box = FunctionBox()

    def solve(self):
        minimal_error = float('-inf')


        functions = [self.function_box.n, self.function_box.nlogn, self.function_box.n2]
        winner_function = functions[0]
        for function in functions:
            scaled_x_list = [function(x) for x in self.list_x]

            coefficients = numpy.polyfit(scaled_x_list, self.list_y, 1) # a, b
            y_values = numpy.polyval(coefficients, scaled_x_list) # y = a * x + b

            square_error = (numpy.sqrt(sum((y_values - self.list_y) ** 2) / len(self.list_y)))

            if (square_error < minimal_error ):
                winner_function = function
                minimal_error = square_error

        print("Winner: ", winner_function.__name__)
        pass
