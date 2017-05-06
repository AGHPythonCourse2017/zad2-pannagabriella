import numpy
import time

x_points = []
y_points = []

class FunctionBox:
    def __init__(self):
        pass

    def n2(self, x):
        return x ** 2

    def n(self, x):
        return x

    def nlogn(self, x):
        return x * numpy.log2(x)

class Solver:
    def __init__(self, list_x, list_y):
        self.list_x = list_x
        self.list_y = list_y
        self.function_box = FunctionBox()

    def solve(self):
        minimal_error = float('inf')

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

        return winner_function

def count_time(init_function, main_function, clean_function, start_a, start_b, stop_a, stop_b, step):
    for b in range(start_b, stop_b):
        for a in numpy.arange(start_a, stop_a, step):
            x = a * (10 ** b)
            x_points.append(x)

            data = init_function(x)

            start_time = time.time()
            main_function(data)
            end_time = time.time()
            y_points.append(end_time - start_time)

            print(x, " ", end_time - start_time )

            clean_function(data)

def points_generator(init_function, main_function, clean_function):
    count_time(init_function, main_function, clean_function, 1, 1, 10, 3, 0.2)
    #count_time(init_function, main_function, clean_function, 1, 4, 10, 7, 1)

    return (x_points, y_points)

def start(init_function, main_function, clean_function):

    points_generator(init_function, main_function, clean_function)
    solver = Solver(x_points, y_points)
    function = solver.solve()

    print("Function is", function.__name__)

def bum():
    print("hello")