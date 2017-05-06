import numpy

from FunctionBox import FunctionBox

import matplotlib.pyplot as plt

class Solver:
    def __init__(self, resources):
        self.list_x = resources[0]
        self.list_y = resources[1]
        self.function_box = FunctionBox()

    def solve(self):

        scaled_x = []

        scaled_x.append(self.function_box.n_list(self.list_x))
        scaled_x.append(self.function_box.n2_list(self.list_x))
        scaled_x.append(self.function_box.nlogn_list(self.list_x))


        coefficients = numpy.polyfit(self.list_x, self.list_y, 1)
        y = self.regresionYs(coefficients)

        plt.plot(self.list_x, self.list_y, 'yo')

        type = 'b'
        for x_list in scaled_x:

            coefficients = numpy.polyfit(x_list, self.list_y, 1)
            y = self.regresionYs(coefficients)
            plt.plot(self.list_x, y, type)
            if type == 'b':
                type = 'g'
            elif type == 'g':
                type = 'r'
            elif type == 'r':
                type == 'y'



        plt.ylabel('some numbers')
        plt.show()

        pass

    def regresionYs(self, coefficients):
        return [coefficients[0] * x + coefficients[1] for x in self.list_x]