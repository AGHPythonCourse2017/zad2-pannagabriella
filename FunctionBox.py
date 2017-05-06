import numpy
class FunctionBox:
    def __init__(self):
        pass

    def n2_list(self, x_list):
        return [x ** 2 for x in x_list]

    def n_list(self, x_list):
        return [x for x in x_list]

    def nlogn_list(self, x_list):
        return [x * numpy.log2(x) for x in x_list]

