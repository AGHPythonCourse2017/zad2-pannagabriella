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

        for i in range(0, len(self.list_x) - 1):
            print (scaled_x[1][i], " ", self.list_y[i])

        for x_list in scaled_x:

            polynomial = numpy.polyfit(x_list, self.list_y, 1)
            values = numpy.polyval(polynomial, x_list)

            square_error = (numpy.sqrt(sum((values - self.list_y) ** 2) / len(self.list_x)))

            print("BLAD to: ", square_error)



        plt.yscale('log')
        plt.ylabel('some numbers')
        plt.show()

        pass
