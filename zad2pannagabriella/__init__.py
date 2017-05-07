import multiprocessing
import numpy
import time


class TimeoutListException(Exception):
    pass


class DifferentListSizeException(Exception):
    pass


class FunctionBox:
    def __init__(self):
        pass

    def n2(self, x):
        return x ** 2

    def n(self, x):
        return x

    def nlogn(self, x):
        return x * numpy.log2(x)

    def linear_function(self, a, b):
        def linear(x):
            if a == 0:
                return b
            return a * x + b

        return linear


class Solver:
    def __init__(self, list_x, list_y):
        self.__list_x = list_x
        self.__list_y = list_y
        self.__function_box = FunctionBox()

        self.__winner_function = None
        self.__time_function = None
        self.__size_function = None

    def solve(self):
        minimal_error = float('inf')

        candidate_functions = [self.__function_box.n, self.__function_box.nlogn, self.__function_box.n2]

        for candidate_function in candidate_functions:
            scaled_x_list = [candidate_function(x) for x in self.__list_x]

            coefficients = numpy.polyfit(scaled_x_list, self.__list_y, 1)  # a, b
            y_values = numpy.polyval(coefficients, scaled_x_list)  # y = a * x + b

            square_error = (numpy.sqrt(sum((y_values - self.__list_y) ** 2) / len(self.__list_y)))

            if square_error < minimal_error:
                minimal_error = square_error

                self.__winner_function = candidate_function

                self.__time_function = self.__function_box.linear_function(coefficients[0], coefficients[1])

                if coefficients[0] != 0:
                    self.__size_function = self.__function_box.linear_function(
                        1 / coefficients[0], -coefficients[1] / coefficients[0])

    def get_expected_complexity_function_name(self):
        return self.__winner_function.__name__

    def get_time_expected_function(self):
        return self.__time_function

    def get_size_expected_function(self):
        return self.__size_function


class Generator:
    def __init__(self, init_function, main_function, clean_function):
        self.__init_function = init_function
        self.__main_function = main_function
        self.__clean_function = clean_function

        self.__times_counter_exit_status = multiprocessing.Value('d', 0)
        self.__queueX = multiprocessing.Queue()
        self.__queueY = multiprocessing.Queue()

        self.__solver = None

    def start(self, end_time=30):
        p = multiprocessing.Process(target=self.count_times, name="count_times", args=(1, 2, 10, 4, 0.1))
        p.start()
        p.join(end_time)

        if p.is_alive():
            p.terminate()
            p.join()

        x_points = self.__queue_to_list(self.__queueX)
        y_points = self.__queue_to_list(self.__queueY)

        try:
            self.__validate_count_time_exit_status()
        except TimeoutListException:
            print("List was cut")

        try:
            self.__validate_lists_size(x_points, y_points)
            self.__solver = Solver(x_points, y_points)
        except DifferentListSizeException:
            self.__solver = Solver(x_points[:len(y_points)], y_points)

        self.__solver.solve()

    def count_times(self, start_a, start_b, stop_a, stop_b, step):
        for b in range(start_b, stop_b):
            for a in numpy.arange(start_a, stop_a, step):
                x = int(a * (10 ** b))

                data = self.__init_function(x)

                start_time = time.time()
                self.__main_function(data)
                end_time = time.time()

                print(x, " ", end_time - start_time)

                self.__queueX.put(x)
                self.__queueY.put(end_time - start_time)

                self.__clean_function(data)

        self.__times_counter_exit_status.value = 1

    def __queue_to_list(self, queue):
        points = []
        while True:
            if queue.empty():
                return points
            points.append(queue.get())

    def __validate_lists_size(self, x_points, y_points):
        if len(x_points) != len(y_points):
            raise DifferentListSizeException

    def __validate_count_time_exit_status(self):
        if self.__times_counter_exit_status.value == 0:
            raise TimeoutListException

    def get_function_info(self):
        if self.__times_counter_exit_status.value == 0:
            return "Function probable not faster than " + self.__solver.get_expected_complexity_function_name()
        else:
            return "Function probable complexity: " + self.__solver.get_expected_complexity_function_name()

    def get_time_function(self):
        return self.__solver.get_time_expected_function()

    def get_size_function(self):
        return self.__solver.get_size_expected_function()