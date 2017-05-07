import multiprocessing
import numpy
import time

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
            print(scaled_x_list)
            coefficients = numpy.polyfit(scaled_x_list, self.list_y, 1) # a, b

            y_values = numpy.polyval(coefficients, scaled_x_list) # y = a * x + b

            square_error = (numpy.sqrt(sum((y_values - self.list_y) ** 2) / len(self.list_y)))

            if (square_error < minimal_error):
                winner_function = function
                minimal_error = square_error

        return winner_function

class TimeoutListException(Exception):
    pass
class DifferentListSizeException(Exception):
    pass

def count_time(ended, queueX, queueY, init_function, main_function, clean_function, start_a, start_b, stop_a, stop_b, step):
    for b in range(start_b, stop_b):
        for a in numpy.arange(start_a, stop_a, step):
            x = int(a * (10 ** b))

            data = init_function(x)

            start_time = time.time()
            main_function(data)
            end_time = time.time()

            print(x, " ", end_time - start_time)
            clean_function(data)

            queueX.put(x)
            queueY.put(end_time - start_time)
    ended.value = 1

def queue_to_list(queue):
    points = []
    while True:
        if queue.empty():
            return points
        points.append(queue.get())

def validate_lists_size(x_points, y_points):

    if len(x_points) != len(y_points):
        raise DifferentListSizeException

def validate_count_time_exit_status(ended):
    if (ended.value == 0):
        raise TimeoutListException

def start(init_function, main_function, clean_function, end_time = 30):

    ended = multiprocessing.Value('d', 0)
    qx = multiprocessing.Queue()
    qy = multiprocessing.Queue()
    p = multiprocessing.Process(target=count_time, name="count_time",
                                args=(ended, qx, qy, init_function, main_function, clean_function, 1, 2, 10, 3, 0.1))
    p.start()
    p.join(end_time)

    if p.is_alive():
        p.terminate()
        p.join()

    x_points = queue_to_list(qx)
    y_points = queue_to_list(qy)

    try:
        validate_count_time_exit_status(ended)
    except TimeoutListException:
        print("List was cut")

    try:
        validate_lists_size(x_points, y_points)
        solver = Solver(x_points, y_points)
    except DifferentListSizeException:
        solver = Solver(x_points[:len(y_points)], y_points)

    function = solver.solve()
    print("Function is", function.__name__)


